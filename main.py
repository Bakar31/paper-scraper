import arxiv
import csv
import os
import requests
from urllib.parse import urlparse


def search_and_download(keyword, max_results=10):
    search = arxiv.Search(
        query=keyword, max_results=max_results, sort_by=arxiv.SortCriterion.Relevance
    )

    with open(
        "output/arxiv_metadata.csv", "w", newline="", encoding="utf-8"
    ) as csvfile:
        fieldnames = [
            "Title",
            "Authors",
            "Published",
            "Summary",
            "PDF URL",
            "DOI",
            "Primary Category",
            "All Categories",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        os.makedirs("output/arxiv_pdfs", exist_ok=True)

        for result in search.results():
            writer.writerow(
                {
                    "Title": result.title,
                    "Authors": ", ".join(author.name for author in result.authors),
                    "Published": result.published.strftime("%Y-%m-%d"),
                    "Summary": result.summary,
                    "PDF URL": result.pdf_url,
                    "DOI": result.doi if result.doi else "N/A",
                    "Primary Category": result.primary_category,
                    "All Categories": ", ".join(result.categories),
                }
            )

            response = requests.get(result.pdf_url)
            if response.status_code == 200:
                filename = os.path.join(
                    "output/arxiv_pdfs",
                    f"{urlparse(result.pdf_url).path.split('/')[-1]}.pdf",
                )
                with open(filename, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded: {filename}")
            else:
                print(f"Failed to download: {result.pdf_url}")


if __name__ == "__main__":
    keyword = input("Enter a keyword to search for on arXiv: ")
    max_results = int(
        input("Enter the maximum number of results to retrieve (default is 10): ") or 10
    )
    search_and_download(keyword, max_results)
