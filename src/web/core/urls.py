# core/urls.py
from django.urls import path
from core.views import provide_random_text, process_recorded_speech

urlpatterns = [
    path("random-text/", provide_random_text, name="random_text"),
    path(
        "process-recorded-speech/",
        process_recorded_speech,
        name="process_recorded_speech",
    ),
]
