"""Command-line interface for processing receipt images."""

import json
import argparse
from receipt_processor import file_io as io_mod
from receipt_processor import gpt


def sanitize_amount(amount):
    """Sanitize and normalize the amount value from receipt extraction.

    This function removes currency symbols (specifically "$") and converts
    the amount string to a float. If the conversion fails, the original
    value is returned unchanged.

    Args:
        amount: The amount value from receipt extraction (str, float, or None).

    Returns:
        float or original value: The sanitized amount as a float if possible,
            otherwise returns the original value.
    """
    if amount is None:
        return amount
    
    # Convert to string if needed
    amount_str = str(amount)
    
    # Remove dollar sign if present
    amount_str = amount_str.replace("$", "").strip()
    
    # Try to convert to float
    try:
        return float(amount_str)
    except (ValueError, AttributeError):
        # If conversion fails, return original value
        return amount


def process_directory(dirpath):
    """Process all receipt images in a directory and extract information.

    This function iterates over all files in the specified directory,
    encodes each image as base64, sends it to the GPT model for information
    extraction, and collects the results.

    Args:
        dirpath (str): Path to the directory containing receipt images.

    Returns:
        dict: A dictionary mapping each receipt filename to its extracted
            information (date, amount, vendor, category).
    """
    results = {}
    for name, path in io_mod.list_files(dirpath):
        image_b64 = io_mod.encode_file(path)
        data = gpt.extract_receipt_info(image_b64)
        
        # Apply sanity checks to the amount field
        if "amount" in data:
            data["amount"] = sanitize_amount(data["amount"])
        
        results[name] = data
    return results


def main():
    """Main entry point for the receipt processor CLI.

    Parses command-line arguments and processes receipt images in the
    specified directory. If the --print flag is provided, outputs the
    extracted information as formatted JSON.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath")
    parser.add_argument("--print", action="store_true")
    args = parser.parse_args()

    data = process_directory(args.dirpath)
    if args.print:
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
