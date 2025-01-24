run:
	uv run uvicorn scrape_articles.main:app --reload

.PHONY: test install clean

install:
	pip install -r requirements.txt

test:
	pytest tests/ -v

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete