# Receipt Processor

A simple command-line application that processes receipt images and extracts structured information using OpenAI's GPT-4 Vision API.

## Features

- Extracts key information from receipt images:
  - Receipt date
  - Total amount spent
  - Vendor/merchant name
  - Expense category
- Processes entire directories of receipts
- Outputs results in JSON format

## Requirements

- Python 3.7 or higher
- OpenAI API key
- Required packages (see `requirements.txt`)

## Installation

1. Create a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

Run the program by providing the path to a directory containing receipt images:

```bash
python -m receipt_processor.main /path/to/receipts --print
```

### Using the Makefile

A convenience Makefile is provided. First, make sure your API key is set:

```bash
export OPENAI_API_KEY=your_api_key_here
```

Then run the program with the default settings:

```bash
make run
```

This will:
- Check that the OpenAI API key is set
- Run the program on the `app/receipts` directory
- Display the output in formatted JSON

### Output Format

The program outputs a JSON object mapping each receipt filename to its extracted information:

```json
{
  "receipt_1.jpg": {
    "date": "2024-01-15",
    "amount": "42.50",
    "vendor": "Coffee Shop",
    "category": "Meals"
  },
  "receipt_2.jpg": {
    "date": "2024-01-16",
    "amount": "120.00",
    "vendor": "Office Depot",
    "category": "Office Supplies"
  }
}
```

## Expense Categories

The application classifies expenses into the following predefined categories:
- Meals
- Transport
- Lodging
- Office Supplies
- Entertainment
- Other

## License

This project is licensed under the MIT License - see the LICENSE file for details.
