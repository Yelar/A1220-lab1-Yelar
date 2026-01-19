.PHONY: run

run:
	@if [ -z "$$OPENAI_API_KEY" ]; then \
		echo "Error: OPENAI_API_KEY environment variable is not set"; \
		echo "Please set it using: export OPENAI_API_KEY=your_key_here"; \
		exit 1; \
	fi
	PYTHONPATH=src .venv/bin/python -m receipt_processor.main app/receipts --print
