"""
Usage:
1. Install SDK:
   pip install groq

2. Set API key (macOS / Linux):
   export GROQ_API_KEY="your_api_key_here"

3. Run:
   python 1.foundation/1.hello-llm/python/Hellollm.py "Hello LLM!"

If no message argument is provided, defaults to "Hello LLM!".
"""
from groq import Groq
import os
import sys
import logging
import argparse

logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="Simple Groq chat completion example")
    parser.add_argument("message", nargs="?", default="Hello LLM!", help="Prompt message to send to the model")
    args = parser.parse_args()

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        logging.error("Environment variable GROQ_API_KEY is not set.")
        sys.exit(1)

    client = Groq(api_key=api_key)

    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": args.message}],
        )
    except Exception:
        logging.exception("Request to Groq API failed.")
        sys.exit(1)

    try:
        content = chat_completion.choices[0].message.content
    except Exception:
        logging.warning("Unexpected response structure; printing raw response.")
        content = str(chat_completion)

    print(content)

if __name__ == "__main__":
    main()