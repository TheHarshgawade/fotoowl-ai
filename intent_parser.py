import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def parse_intent(user_prompt):

    prompt = f"""
Convert this user request into JSON only.

User Prompt:
{user_prompt}

Return ONLY this JSON format:

{{
  "style":"",
  "pacing":"",
  "caption_tone":"",
  "transition":""
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)
    