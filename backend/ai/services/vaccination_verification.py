import os
import tempfile,json,re

from django.conf import settings
from django.core.files.storage import default_storage
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
    - ear_tag_readable: true only when the number can actually be read.
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

    text = response.text.strip()

    # Remove Markdown code fences
    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    return json.loads(text)


def analyze_django_image(image_field):

    suffix = os.path.splitext(image_field.name)[1]

    with default_storage.open(image_field.name, "rb") as source:

        with tempfile.NamedTemporaryFile(
            suffix=suffix,
            delete=False
        ) as temp_file:

            temp_file.write(source.read())
            temp_path = temp_file.name

    try:
        return analyze_vaccination_image(temp_path)

    finally:
        os.remove(temp_path)