// Safely alias Django's gettext in case the catalog hasn't loaded
const t = window.gettext || ((text) => text);

const LANGUAGE_CONFIG = {
    en: { speech: "en-IN", voices: ["Google English", "English"] },
    hi: { speech: "hi-IN", voices: ["Google हिन्दी", "Hindi"] },
    ta: { speech: "ta-IN", voices: ["Google Tamil", "Valluvar", "Tamil"] },
    te: { speech: "te-IN", voices: ["Google Telugu", "Telugu"] },
    ml: { speech: "ml-IN", voices: ["Google Malayalam", "Malayalam"] },
    kn: { speech: "kn-IN", voices: ["Google Kannada", "Kannada"] },
    mr: { speech: "mr-IN", voices: ["Google Marathi", "Marathi"] },
    gu: { speech: "gu-IN", voices: ["Google Gujarati", "Gujarati"] },
    bn: { speech: "bn-IN", voices: ["Google Bengali", "Bengali"] },
    pa: { speech: "pa-IN", voices: ["Google Punjabi", "Punjabi"] },
    or: { speech: "or-IN", voices: ["Odia"] },
    as: { speech: "as-IN", voices: ["Assamese"] },
    ur: { speech: "ur-IN", voices: ["Urdu"] },
    ne: { speech: "ne-NP", voices: ["Nepali"] },
    sa: { speech: "sa-IN", voices: ["Sanskrit"] },
    default: { speech: "en-IN", voices: ["Google English", "English"] }
};

let isSpeaking = false;
let recognition;
let availableVoices = [];

function populateVoiceList() {
    if (!window.speechSynthesis) return;
    
    availableVoices = window.speechSynthesis.getVoices();
    const voiceSelect = document.getElementById('voice-select');
    if (!voiceSelect) return;

    const currentSelection = voiceSelect.value;
    
    // Default gentle voice option placed first
    voiceSelect.innerHTML = `<option value="default-gentle">${t("Default Gentle Voice")}</option>
                             <option value="">${t("Auto (Best Female Voice)")}</option>`;

    availableVoices.forEach((voice, index) => {
        const option = document.createElement('option');
        option.value = index;
        option.textContent = `${voice.name} (${voice.lang})`;
        if (index.toString() === currentSelection) {
            option.selected = true;
        }
        voiceSelect.appendChild(option);
    });
}

if (typeof window !== 'undefined' && window.speechSynthesis) {
    populateVoiceList();
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
        window.speechSynthesis.onvoiceschanged = populateVoiceList;
    }
}

function getSpeechConfig() {
    const language = document.documentElement.lang || "en";
    return LANGUAGE_CONFIG[language] || LANGUAGE_CONFIG.default;
}

function getPreferredVoice(config, langCode) {
    const voiceSelect = document.getElementById('voice-select');
    
    // Explicit manual selection handler
    if (voiceSelect && voiceSelect.value !== "" && voiceSelect.value !== "default-gentle") {
        const selectedVoice = availableVoices[parseInt(voiceSelect.value, 10)];
        if (selectedVoice) return selectedVoice;
    }

    if (!availableVoices.length) {
        availableVoices = window.speechSynthesis.getVoices();
    }

    let languageVoices = availableVoices.filter(voice =>
        voice.lang === config.speech || voice.lang.startsWith(langCode)
    );

    if (!languageVoices.length) languageVoices = availableVoices; 
    if (!languageVoices.length) return null;

    for (const preferredName of config.voices) {
        const match = languageVoices.find((voice) => {
            const nameLower = voice.name.toLowerCase();
            const isFemale = nameLower.includes('female') || nameLower.includes('woman') || nameLower.includes('zira') || nameLower.includes('heera') || nameLower.includes('kalpana');
            return nameLower.includes(preferredName.toLowerCase()) && isFemale;
        });
        if (match) return match;
    }

    const generalFemaleMatch = languageVoices.find(voice => {
        const nameLower = voice.name.toLowerCase();
        return nameLower.includes('female') || nameLower.includes('woman') || nameLower.includes('google') || nameLower.includes('natural');
    });
    if (generalFemaleMatch) return generalFemaleMatch;

    return languageVoices.find((voice) => voice.localService) || languageVoices[0];
}

function speakText(text) {
    if (!window.speechSynthesis || !text) return;

    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);

    const langCode = document.documentElement.lang || "en";
    const config = getSpeechConfig();

    utterance.lang = config.speech;
    
    const voiceSelect = document.getElementById('voice-select');
    const isDefaultGentle = !voiceSelect || voiceSelect.value === "default-gentle" || voiceSelect.value === "";

    if (!isDefaultGentle) {
        const voice = getPreferredVoice(config, langCode);
        if (voice) utterance.voice = voice;
    }

    // Default gentle tone modifications (softer pitch and slower cadence)
    utterance.rate = 0.85;
    utterance.pitch = 0.95;
    utterance.volume = 0.90;

    utterance.onstart = () => { isSpeaking = true; };
    utterance.onend = () => { isSpeaking = false; };
    utterance.onerror = () => { isSpeaking = false; };

    window.speechSynthesis.speak(utterance);
}

function hideEmptyState() {
    const emptyState = document.getElementById('empty-state');
    if (emptyState) {
        emptyState.style.display = 'none';
    }
}

function appendMessage(sender, text, isError = false) {
    hideEmptyState();

    const container = document.getElementById('chat-container');
    const msgWrapper = document.createElement('div');

    msgWrapper.className = `chat-message-wrapper ${sender === 'ai' ? 'ai-wrapper' : 'user-wrapper'}`;
    if (isError) msgWrapper.classList.add('error-wrapper');

    const msgContent = document.createElement('div');
    msgContent.className = 'chat-message-content';
    msgContent.style.display = 'flex';
    msgContent.style.maxWidth = '768px';
    msgContent.style.margin = '0 auto';

    const icon = document.createElement('span');
    icon.className = 'chat-icon';
    icon.textContent = sender === 'ai' ? '🪔' : '👤';
    icon.style.marginRight = '15px';
    icon.style.fontSize = '1.5rem';

    const textNode = document.createElement('div');
    textNode.className = 'chat-text';
    textNode.textContent = text;
    textNode.style.flex = '1';
    textNode.style.lineHeight = '1.6';

    msgContent.appendChild(icon);
    msgContent.appendChild(textNode);
    msgWrapper.appendChild(msgContent);
    container.appendChild(msgWrapper);

    container.scrollTo({ top: container.scrollHeight, behavior: 'smooth' });
}

function playGreeting() {
    const container = document.getElementById('chat-container');
    if (container.querySelectorAll('.chat-message-wrapper').length === 0) {
        const greeting = t("Hello! I'm Sahayika. I'm here to help you understand the PM Ujjwala Yojana. You can ask me anything in your language.");
        appendMessage("ai", greeting);
        setTimeout(() => speakText(greeting), 800);
    }
}

function getCSRFToken() {
    const csrfInput = document.querySelector('[name=csrfmiddlewaretoken]');
    return csrfInput ? csrfInput.value : '';
}

document.addEventListener("DOMContentLoaded", () => {
    populateVoiceList();

    const chatInput = document.getElementById('chat-input');
    if (chatInput) {
        chatInput.addEventListener('input', function () {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
            if (this.value === '') {
                this.style.height = 'auto';
            }
        });

        chatInput.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                document.getElementById('chat-form').dispatchEvent(new Event('submit', { cancelable: true, bubbles: true }));
            }
        });
    }

    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        recognition = new SpeechRecognition();
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            chatInput.value = transcript;
            chatInput.dispatchEvent(new Event('input'));
        };

        recognition.onerror = (event) => {
            if (event.error === "no-speech") {
                appendMessage("ai", t("I couldn't hear you. Please try again or type your question."), true);
            }
            document.getElementById('btn-voice').classList.remove('recording');
        };

        recognition.onend = () => {
            document.getElementById('btn-voice').classList.remove('recording');
        };
    } else {
        const voiceBtn = document.getElementById('btn-voice');
        if (voiceBtn) voiceBtn.style.display = 'none';
    }

    const voiceBtn = document.getElementById("btn-voice");
    if (voiceBtn) {
        voiceBtn.addEventListener("click", (e) => {
            e.preventDefault();
            if (recognition) {
                try {
                    window.speechSynthesis.cancel();
                    voiceBtn.classList.add('recording');
                    recognition.lang = getSpeechConfig().speech;
                    recognition.start();
                } catch (err) {
                    console.error("Speech recognition error:", err);
                    voiceBtn.classList.remove('recording');
                }
            }
        });
    }

    const chatForm = document.getElementById("chat-form");
    if (chatForm) {
        chatForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const text = chatInput.value.trim();
            if (!text) return;

            appendMessage("user", text);

            chatInput.value = '';
            chatInput.style.height = 'auto';
            document.getElementById('loading-indicator').classList.remove('hidden');

            const langDropdown = document.getElementById('language-select');
            const selectedLanguage = langDropdown ? langDropdown.value : 'en';

            try {
                const response = await fetch('/chat/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCSRFToken()
                    },
                    body: JSON.stringify({
                        message: text,
                        language: selectedLanguage
                    })
                });

                if (!response.ok) {
                    throw new Error(`Server returned status: ${response.status}`);
                }

                const data = await response.json();
                document.getElementById('loading-indicator').classList.add('hidden');

                if (data.success) {
                    appendMessage("ai", data.response);
                    speakText(data.response);
                } else {
                    appendMessage("ai", data.error || t("An error occurred."), true);
                    speakText(data.error || t("An error occurred."));
                }

            } catch (error) {
                console.error('Error fetching from backend:', error);
                document.getElementById('loading-indicator').classList.add('hidden');

                const fallbackReply = t("There was a connection error. Please check your internet or server.");
                appendMessage("ai", fallbackReply, true);
                speakText(fallbackReply);
            }
        });
    }

    setTimeout(playGreeting, 500);
});
