import os
from PIL import Image
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_image(image_path):

    image = Image.open(image_path)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Describe this event image in detail. Mention people, activities, emotions, decorations, and what is happening.",
            image
        ]
    )

    return response.text
    