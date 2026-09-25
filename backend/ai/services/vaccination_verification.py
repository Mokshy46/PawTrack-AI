import json

from django.conf import settings
from google import genai


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def analyze_vaccination_image(image_path):

    uploaded_file = client.files.upload(
        file=image_path
    )

    prompt = """
    Analyze this street-dog vaccination evidence image.

    Return JSON with exactly these fields:

    {
        "dog_detected": true,
        "ear_tag_detected": true,
        "ear_tag_number": "",
        "ear_tag_readable": false,
        "image_quality": "GOOD",
        "issues": []
    }

    Rules:
    - dog_detected: whether a dog is visible.
    - ear_tag_detected: whether an ear tag is visible.
    - ear_tag_number: provide only if clearly readable.
    - ear_tag_readable: true only when the number can actually
      be read.
    - image_quality: GOOD, ACCEPTABLE, or POOR.
    - issues: list visual problems.

    Do not claim that the dog was medically vaccinated.
    Only analyze what is visually observable.

    Return JSON only.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=[
            uploaded_file,
            prompt
        ]
    )

    print("RAW GEMINI RESPONSE:")
    print(response.text)

    return response.text