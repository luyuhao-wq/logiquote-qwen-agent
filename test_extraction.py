from pathlib import Path
from qwen_client import call_qwen


def load_prompt(prompt_path: str) -> str:
    """
    Load a prompt file from the repository.
    """
    return Path(prompt_path).read_text(encoding="utf-8")


def main():
    extraction_prompt = load_prompt("prompts/extraction_prompt.md")

    customer_inquiry = """
Hi, I need to ship 20 cartons of home decor products from Ningbo to Los Angeles.
Total weight is around 480 kg and volume is 3.2 CBM.
Could you quote me the cheapest option within 25 days?
"""

    final_prompt = f"""
{extraction_prompt}

Now extract structured quotation information from the following customer inquiry:

Customer inquiry:
{customer_inquiry}
"""

    result = call_qwen(final_prompt)

    print("===== Qwen Extraction Result =====")
    print(result)


if __name__ == "__main__":
    main()
  
