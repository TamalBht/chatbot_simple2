import base64
import os
from google import genai
from google.genai import types
from gtts import gTTS
import tempfile
import pygame

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

from gtts import gTTS
import tempfile
import os
import pygame

def speak(text):
    # Create a temp file path without keeping it open
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tmp_path = tmp_file.name
    tmp_file.close()

    # Save gTTS output
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(tmp_path)

    # Initialize and play audio
    pygame.mixer.init()
    pygame.mixer.music.load(tmp_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
    os.remove(tmp_path)


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
