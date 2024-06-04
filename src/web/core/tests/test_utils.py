# core/tests/test_utils.py
import os
from django.test import TestCase
from django.conf import settings
from core.utils import recognize_speech_from_audio
from unittest.mock import patch, MagicMock


class RecognizeSpeechTestCase(TestCase):
    def setUp(self):
        # Setup a sample audio file path
        self.sample_audio_path = os.path.join(
            settings.BASE_DIR, "core/tests/samples/hello.wav"
        )

    @patch("core.utils.sr.Recognizer")
    def test_recognize_speech_success(self, MockRecognizer):
        # Mock the speech recognition
        mock_recognizer = MockRecognizer.return_value
        mock_recognizer.record.return_value = "audio_data"
        mock_recognizer.recognize_google.return_value = "Hello, world!"

        text = recognize_speech_from_audio(self.sample_audio_path)
        self.assertEqual(text, "Hello, world!")

    @patch("core.utils.sr.Recognizer")
    def test_recognize_speech_unknown_value_error(self, MockRecognizer):
        mock_recognizer = MockRecognizer.return_value
        mock_recognizer.record.return_value = "audio_data"
        mock_recognizer.recognize_google.side_effect = sr.UnknownValueError

        with self.assertRaises(ValueError) as context:
            recognize_speech_from_audio(self.sample_audio_path)

        self.assertEqual(str(context.exception), "Could not understand audio")

    @patch("core.utils.sr.Recognizer")
    def test_recognize_speech_request_error(self, MockRecognizer):
        mock_recognizer = MockRecognizer.return_value
        mock_recognizer.record.return_value = "audio_data"
        mock_recognizer.recognize_google.side_effect = sr.RequestError(
            "API unavailable"
        )

        with self.assertRaises(ConnectionError) as context:
            recognize_speech_from_audio(self.sample_audio_path)

        self.assertEqual(str(context.exception), "Request error: API unavailable")

    @patch("core.utils.sr.Recognizer")
    def test_recognize_speech_runtime_error(self, MockRecognizer):
        mock_recognizer = MockRecognizer.return_value
        mock_recognizer.record.return_value = "audio_data"
        mock_recognizer.recognize_google.side_effect = Exception("Unexpected error")

        with self.assertRaises(RuntimeError) as context:
            recognize_speech_from_audio(self.sample_audio_path)

        self.assertEqual(str(context.exception), "Unexpected error")
