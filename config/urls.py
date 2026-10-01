"""Sahayika URL Configuration"""
from django.urls import path, include

from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path(
        "jsi18n/",
        JavaScriptCatalog.as_view(),
        name="javascript-catalog",
    ),
    path(
        "i18n/",
        include("django.conf.urls.i18n"),
    ),

    path("", include("apps.core.urls")),
]

