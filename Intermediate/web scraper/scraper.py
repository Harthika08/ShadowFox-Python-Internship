
import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "https://www.shadowfox.in/"

try:
    # Fetch webpage
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Store extracted information
    scraped_data = []

    # Extract website title
    if soup.title:
        scraped_data.append([
            "Title",
            soup.title.get_text(strip=True),
            ""
        ])

    # Extract headings
    for heading in soup.find_all(["h1", "h2", "h3"]):
        text = heading.get_text(strip=True)

        if text:
            scraped_data.append([
                "Heading",
                text,
                ""
            ])

    # Extract paragraphs
    for paragraph in soup.find_all("p"):
        text = paragraph.get_text(strip=True)

        if text:
            scraped_data.append([
                "Paragraph",
                text,
                ""
            ])

    # Extract hyperlinks
    for link in soup.find_all("a"):
        text = link.get_text(strip=True)
        href = link.get("href")

        if href:
            absolute_url = urljoin(url, href)

            scraped_data.append([
                "Link",
                text,
                absolute_url
            ])

   
    # Check whether any data was extracted
    if not scraped_data:
        print("No data was found on the website.")

    else:
        try:
            # Save data into CSV
            with open(
                "scraped_data.csv",
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)
                writer.writerow(["Type", "Content", "URL"])
                writer.writerows(scraped_data)

            print("\nScraping completed successfully!")
            print("Total records:", len(scraped_data))
            print("Data saved to scraped_data.csv")

        except OSError as e:
            print("File saving error:", e)

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)

except requests.exceptions.RequestException as e:
    print("Connection error:", e)
