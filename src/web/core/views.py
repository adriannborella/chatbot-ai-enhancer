# core/views.py
import random
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from core.utils import recognize_speech_from_audio


@csrf_exempt
def provide_random_text(request):
    # Generate random text for the user to read
    random_text = generate_random_text()

    # Return the random text to the user
    return JsonResponse({"random_text": random_text})


@csrf_exempt
def process_recorded_speech(request):
    if request.method == "POST" and request.FILES.get("audio"):
        # Process the recorded speech
        random_text = request.POST["random_text"]

        audio_file = request.FILES["audio"]
        audio_data = audio_file.read()

        try:
            text = recognize_speech_from_audio(audio_data)

            return JsonResponse({"recognized_text": text})
        except ValueError as ve:
            return JsonResponse({"error": str(ve)})
        except ConnectionError as ce:
            return JsonResponse({"error": str(ce)})
        except RuntimeError as re:
            return JsonResponse({"error": str(re)})
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)


def generate_random_text():
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "She sells sea shells by the sea shore.",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "Peter Piper picked a peck of pickled peppers.",
        "I scream, you scream, we all scream for ice cream.",
        "Betty Botter bought some butter, but she said the butter's bitter.",
        "Red lorry, yellow lorry.",
        "A big black bear sat on a big black rug.",
        "The sixth sick sheikh's sixth sheep's sick.",
        "Fred fed Ted bread, and Ted fed Fred bread.",
        "I saw Susie sitting in a shoeshine shop.",
        "How can a clam cram in a clean cream can?",
        "Six slippery snails slid slowly seaward.",
        "Lesser leather never weathered wetter weather better.",
        "The big black bug bled black blood.",
        "How many boards could the Mongols hoard if the Mongol hordes got bored?",
        "He threw three free throws.",
        "Greek grapes, Greek grapes.",
        "Six sleek swans swam swiftly southwards.",
        "Truly rural.",
        "A proper copper coffee pot.",
        "Eleven benevolent elephants.",
        "Chester Cheetah chews a chunk of cheap cheddar cheese.",
        "A skunk sat on a stump and thunk the stump stunk, but the stump thunk the skunk stunk.",
        "Blue bluebird.",
        "Willie’s really weary.",
        "Irish wristwatch.",
        "Toy boat, toy boat, toy boat.",
        "A noisy noise annoys an oyster.",
        "Any noise annoys an oyster but a noisy noise annoys an oyster more.",
        "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair. Fuzzy Wuzzy wasn’t very fuzzy, was he?",
    ]
    return random.choice(texts)
