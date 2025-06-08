import base64
import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key="AIzaSyC1ycYj4yGZb4n_b0jJRTQs9YavW1sP0qI",
    )

    model = "gemini-1.5-flash-latest"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""what is the color of the sky?
                """),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=0,
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()
