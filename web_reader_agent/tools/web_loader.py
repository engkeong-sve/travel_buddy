import asyncio
import json
import os
import time
import uuid

from crawl4ai import *
from crawl4ai.models import CrawlResult
from google.adk.agents import BaseAgent, LlmAgent
from google.adk.tools import ToolContext
from google.genai import types

directory = "saved/"
clean_directory = directory + "cleaned/"
original_directory = directory + "original/"
saved_urls_file = directory + "saved_urls.json"


async def web_loader(url: str, tool_context: ToolContext) -> str:
    if not url:
        raise ValueError("URL cannot be empty")

    # Check if the URL is already saved
    if is_saved(url):
        print(f"URL {url} is already saved. Loading from saved file.")
        html_content = read_by_url(url)
    else:
        async with AsyncWebCrawler() as crawler:
            result: CrawlResult = await crawler.arun(url=url)
            html_content = str(result.cleaned_html)

        save(url, str(result.html), html_content)

    return html_content


def url_to_filename(url: str) -> str:
    """Convert URL to a valid filename."""
    return url.replace("https://", "").replace("/", "_") + ".html"


def generate_filename() -> str:
    """Generate a unique filename based on the current timestamp."""
    # generate a unique filename by time (YYYYMMDDHHMMSS) + uuid (4digits)
    timestamp = time.strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4().hex[:4])  # take first 4 characters of uuid
    return f"{timestamp}_{unique_id}.html"


def is_saved(url: str) -> bool:
    """Check if the URL is already saved."""
    try:
        with open(saved_urls_file, "r", encoding="utf-8") as f:
            saved_urls = json.load(f)
            for record in saved_urls:
                if record["url"] == url:
                    return True
    except FileNotFoundError:
        return False
    return False


def save(url: str, html_content: str, html_clean: str) -> None:
    """Save the HTML content to a file."""

    filename = generate_filename()

    # create directories if they do not exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    if not os.path.exists(clean_directory):
        os.makedirs(clean_directory)
    if not os.path.exists(original_directory):
        os.makedirs(original_directory)

    # save the original HTML content
    with open(original_directory + filename, "w", encoding="utf-8") as file:
        file.write(html_content)

    # save the cleaned HTML content
    with open(clean_directory + filename, "w", encoding="utf-8") as file:
        file.write(html_clean)

    # add record in a JSON file
    record = {"url": url, "filename": filename}

    # ensure saved_urls.json exists
    if not os.path.exists(saved_urls_file):
        with open(saved_urls_file, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

    with open(saved_urls_file, "r", encoding="utf-8") as f:
        saved_urls = json.load(f)

    saved_urls.append(record)
    with open(saved_urls_file, "w", encoding="utf-8") as f:
        json.dump(saved_urls, f, indent=4)
    # print a message
    print(f"Saved HTML content to {filename} and updated saved_urls.json")


def read_by_url(url: str) -> str:
    """Read the HTML content by URL."""
    # get filename from saved_urls.json
    if not is_saved(url):
        raise ValueError(f"URL {url} is not saved. Please load it first.")

    with open(saved_urls_file, "r", encoding="utf-8") as f:
        saved_urls = json.load(f)
    for record in saved_urls:
        if record["url"] == url:
            filename = record["filename"]
            break
    else:
        raise ValueError(f"URL {url} not found in saved URLs.")

    try:
        with open(clean_directory + filename, "r", encoding="utf-8") as file:
            html_content = file.read()
        print(f"Loaded HTML content from {filename}")
        return html_content
    except FileNotFoundError:
        raise ValueError(f"HTML content for URL {url} not found. Please load it first.")
