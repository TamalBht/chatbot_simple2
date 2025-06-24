import base64
import os
from google import genai
from google.genai import types
import pyttsx3

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)
def speak(text):
    engine.say(text)
    engine.runAndWait()


def generate():
    client = genai.Client(
        api_key=os.getenv("API_KEY"),
    )
    while True:
        response=input("Enter your response: ")
        if response.lower() == "exit":
            break
        response=response+"keep it short and concise, no more than 100 words"
        model = "gemini-1.5-flash-latest"
        contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=response),
            ],
        ),
    ]
        generate_content_config = types.GenerateContentConfig(
        temperature=0,
        response_mime_type="text/plain",
    )
        replyy=""

        for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
            print(chunk.text, end="")
            replyy += chunk.text
        speak(replyy)

if __name__ == "__main__":
    generate()
