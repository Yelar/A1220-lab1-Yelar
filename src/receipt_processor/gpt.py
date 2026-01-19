"""OpenAI GPT integration for extracting receipt information."""

import json
from openai import OpenAI

CATEGORIES = ["Meals", "Transport", "Lodging", "Office Supplies", 
"Entertainment", "Other"]


def _get_client():
    """Get or create an OpenAI client instance.
    
    Returns:
        OpenAI: An initialized OpenAI client.
    """
    return OpenAI()


def extract_receipt_info(image_b64):
    """Extract structured information from a receipt image using GPT-4 Vision.

    This function sends a base64-encoded receipt image to the OpenAI API
    and requests extraction of key receipt fields: date, amount, vendor name,
    and expense category.

    Args:
        image_b64 (str): Base64-encoded string representation of a receipt image.

    Returns:
        dict: A dictionary containing the extracted fields:
            - date (str or None): The receipt date as a string.
            - amount (str or None): The total amount paid as it appears on the receipt.
            - vendor (str or None): The merchant or vendor name.
            - category (str or None): One of the predefined expense categories.

    Note:
        The function uses GPT-4.1-mini with a fixed seed for reproducibility.
        If a field cannot be determined, the value will be null/None.
    """
    prompt = f"""
You are an information extraction system.
Extract ONLY the following fields from the receipt image:

date: the receipt date as a string
amount: the total amount paid as it appears on the receipt
vendor: the merchant or vendor name
category: one of [{", ".join(CATEGORIES)}]

Return EXACTLY one JSON object with these four keys and NOTHING ELSE.
Do not include explanations, comments, or formatting.
Do not wrap the JSON in markdown.
If a field cannot be determined, use null.

The output must be valid JSON.
"""
    client = _get_client()
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        seed=43,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_b64}"
                        }
                    }
                ]
            }
        ]
    )
    return json.loads(response.choices[0].message.content)
