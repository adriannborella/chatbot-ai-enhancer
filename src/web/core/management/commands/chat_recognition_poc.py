# core/management/commands/chat_recognition_poc.py
import os
from django.core.management.base import BaseCommand, CommandError
from core.utils import recognize_speech_from_audio


class Command(BaseCommand):
    help = "Test the speech recognition library with a sample audio file"

    def add_arguments(self, parser):
        parser.add_argument(
            "audio_path", type=str, help="The path to the audio file to be processed"
        )

    def handle(self, *args, **options):
        audio_path = options["audio_path"]

        if not os.path.exists(audio_path):
            raise CommandError('Audio file "%s" does not exist' % audio_path)

        try:
            text = recognize_speech_from_audio(audio_path)
            self.stdout.write(self.style.SUCCESS('Recognized text: "%s"' % text))
        except ValueError as ve:
            self.stdout.write(self.style.ERROR("Error: %s" % str(ve)))
        except ConnectionError as ce:
            self.stdout.write(self.style.ERROR("Error: %s" % str(ce)))
        except RuntimeError as re:
            self.stdout.write(self.style.ERROR("Error: %s" % str(re)))
