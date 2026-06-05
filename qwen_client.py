import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


def get_qwen_client():
    """
    Create an OpenAI-compatible client for Qwen Cloud.
    The real API key should be stored in a local .env file.
    Do not upload the .env file to GitHub.
    """
    api_key = os.getenv("DASHSCOPE_API_KEY")
    base_url = os.getenv("QWEN_BASE_URL", "https://dashscope-intl.aliyuncs.com/compatible-mode/v1")

    if not api_key:
        raise ValueError(
            "DASHSCOPE_API_KEY is missing. Please create a local .env file and add your API key."
        )

    return OpenAI(
        api_key=api_key,
        base_url=base_url
    )


def call_qwen(prompt: str, model: str = None) -> str:
    """
    Send a prompt to Qwen Cloud and return the model response as text.
    """
    client = get_qwen_client()
    model_name = model or os.getenv("QWEN_MODEL", "qwen-plus")

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "You are LogiQuote, a professional AI assistant for cross-border logistics quotation preparation."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
