import requests
import os
from urllib.parse import urlparse
import re


def download_file(file_url: str, file_name: str) -> None:
    """
    Downloads a file from the given URL and saves it with the given filename.

    Args:
        file_url: The URL of the file to download.
        file_name: The filename to save the downloaded file as.
    """
    with requests.get(file_url, stream=True) as response:
        response.raise_for_status()
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)


def find_article_number(sciencedirect_url: str) -> str:
    """
    Finds the article number in the given ScienceDirect URL.

    Args:
        sciencedirect_url: The ScienceDirect URL to search for the article number.

    Returns:
        The article number if found, otherwise None.
    """
    match = re.search(r"/pii/(S\d+)", sciencedirect_url)
    return match.group(1) if match else None


def try_download_supplementary(
    base_url: str,
    article_number: str,
    extensions: list[str],
    max_supplementary_items: int,
    directory: str,
) -> None:
    """
    Attempts to download supplementary files for a given article number and list of file extensions.

    Args:
        base_url: The base URL for the supplementary files.
        article_number: The article number to download supplementary files for.
        extensions: A list of file extensions to try downloading.
        max_supplementary_items: The maximum number of supplementary items to try downloading.
        directory: The directory to save the downloaded files in.
    """
    for i in range(1, max_supplementary_items + 1):
        for ext in extensions:
            file_name = f"mmc{i}{ext}"
            file_url = f"{base_url}{article_number}-{file_name}"
            try:
                download_file(file_url, os.path.join(directory, file_name))
                print(f"Downloaded {file_name} to {directory}")
            except requests.exceptions.HTTPError:
                # File does not exist, move on to next file
                break


def main(
    sciencedirect_url: str,
    extensions: list[str] = [".docx", ".pdf"],
    max_supplementary_items: int = 3,
) -> None:
    """
    Downloads supplementary files for a given ScienceDirect article URL.

    Args:
        sciencedirect_url: The ScienceDirect URL for the article.
        extensions: A list of file extensions to try downloading.
        max_supplementary_items: The maximum number of supplementary items to try downloading.
    """
    base_url = "https://ars.els-cdn.com/content/image/1-s2.0-"
    article_number = find_article_number(sciencedirect_url)
    if article_number:
        try_download_supplementary(
            base_url, article_number, extensions, max_supplementary_items, "."
        )
    else:
        print("Could not find article number in URL")


if __name__ == "__main__":
    # Provide a ScienceDirect URL here
    sciencedirect_url = ""
    # Enjoy your supplementary files!
    main(sciencedirect_url)
