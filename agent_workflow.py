import json
import re
from pathlib import Path
from qwen_client import call_qwen


def load_prompt(prompt_path: str) -> str:
    return Path(prompt_path).read_text(encoding="utf-8")


def clean_json_response(response: str) -> dict:
    """
    Clean Qwen response and parse JSON.
    The model may return JSON wrapped in ```json ... ```.
    """
    cleaned = response.strip()

    cleaned = re.sub(r"^```json", "", cleaned)
    cleaned = re.sub(r"^```", "", cleaned)
    cleaned = re.sub(r"```$", "", cleaned)
    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "raw_response": response,
            "parse_error": "Failed to parse response as JSON."
        }


def extract_fields(customer_inquiry: str) -> dict:
    prompt = load_prompt("prompts/extraction_prompt.md")

    final_prompt = f"""
{prompt}

Now extract structured quotation information from the following customer inquiry:

Customer inquiry:
{customer_inquiry}
"""

    response = call_qwen(final_prompt)
    return clean_json_response(response)


def check_missing_fields(extracted_fields: dict) -> dict:
    prompt = load_prompt("prompts/missing_fields_prompt.md")

    final_prompt = f"""
{prompt}

Now review the following extracted logistics information:

Extracted fields:
{json.dumps(extracted_fields, ensure_ascii=False, indent=2)}
"""

    response = call_qwen(final_prompt)
    return clean_json_response(response)


def generate_reply(customer_inquiry: str, extracted_fields: dict, missing_check: dict) -> dict:
    prompt = load_prompt("prompts/reply_generation_prompt.md")

    final_prompt = f"""
{prompt}

Original customer inquiry:
{customer_inquiry}

Extracted logistics fields:
{json.dumps(extracted_fields, ensure_ascii=False, indent=2)}

Missing fields and risk notes:
{json.dumps(missing_check, ensure_ascii=False, indent=2)}
"""

    response = call_qwen(final_prompt)
    return clean_json_response(response)


def run_logiquote_agent(customer_inquiry: str) -> dict:
    extracted_fields = extract_fields(customer_inquiry)
    missing_check = check_missing_fields(extracted_fields)
    reply_result = generate_reply(customer_inquiry, extracted_fields, missing_check)

    return {
        "original_inquiry": customer_inquiry,
        "extracted_fields": extracted_fields,
        "missing_field_check": missing_check,
        "reply_generation": reply_result
    }
