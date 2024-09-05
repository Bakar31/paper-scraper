# paper-scraper

## arXiv Search and Download Script

This Python script allows you to search arXiv for papers based on a keyword, download the corresponding PDFs, and create a CSV file with metadata.

## Features

- Search arXiv using a keyword
- Download PDFs of search results
- Create a CSV file with metadata including:
  - Title
  - Authors
  - Published Date
  - Summary
  - DOI
  - Primary Category
  - All Categories
  - PDF URL

## Requirements

- Python 3.10+
- `arxiv` library
- `requests` library

## Installation

1. Clone this repository or download the script.
2. Install the required libraries:

```
pip install arxiv requests
```

or

```
make install
```
Be sure to activate the `venv` in you are using `make install`.

## Usage

1. Run the script:

```
python main.py
```

2. Enter a keyword when prompted.
3. Enter the maximum number of results to retrieve (default is 10).

The script will create a folder named 'arxiv_pdfs' for the downloaded PDFs and a file named 'arxiv_metadata.csv' for the metadata.

## Note

Please ensure you comply with arXiv's terms of service and respect their policies when using this script. The script is set to respect rate limits, but be mindful of the number of requests you make.

## Disclaimer

This script is for educational purposes only. Users are responsible for ensuring they have the right to download and use the papers according to arXiv's terms of service.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.
