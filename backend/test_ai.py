from ai.services.vaccination_verification import (
    analyze_vaccination_image
)


image_url = "/home/moxy/PawTrack/test_images/stray_dog_tag.webp"

result = analyze_vaccination_image(image_url)

print(result)