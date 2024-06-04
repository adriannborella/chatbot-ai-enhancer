# core/utils.py
import os
import tempfile
from pydub import AudioSegment
import speech_recognition as sr


def recognize_speech_from_audio(audio_data):
    try:
        # Create a temporary file to store the audio data
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(audio_data)
            temp_audio.seek(0)

            # Load the audio file from the temporary file
            audio = AudioSegment.from_file(temp_audio.name)
            if audio.frame_rate != 16000:
                audio = audio.set_frame_rate(16000)

            # Recognize speech using the Google Web Speech API
            recognizer = sr.Recognizer()
            with sr.AudioFile(temp_audio.name) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)

            return text
    except sr.UnknownValueError:
        raise ValueError("Could not understand audio")
    except sr.RequestError as e:
        raise ConnectionError(f"Request error: {e}")
    except Exception as e:
        raise RuntimeError(str(e))
    finally:
        # Clean up temporary file
        os.unlink(temp_audio.name)
