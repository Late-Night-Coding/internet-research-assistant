import bs4
import aiohttp
import asyncio
import re
import html
from data.web_content import WebContent

# characters which we allow in the output text
acceptable_characters = '!"#$%&\'()*+,-./:;?0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ \t'


async def download_page(url: str) -> WebContent:
    """This function downloads a webpage's content using aiohttp and returns it as a string.

    :param url: The url of the webpage to download.
    :return: The content of the webpage as a string.
    """
    async with aiohttp.ClientSession() as session:

        try:
            async with session.get(url, timeout=5) as response:
                # Download bytes of the webpage
                response_bytes: bytes = await response.read()

                site_title = ""

                # Use decode to convert bytes to string
                page_content = response_bytes.decode("utf-8", errors='replace')

                # Use beautifulsoup to get the text from the page
                soup = bs4.BeautifulSoup(page_content, 'html.parser')
                site_title = soup.title.string
                for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'footer']:
                    for element in soup.find_all(tag):
                        element.replaceWith('')

                text = soup.get_text(strip=True, separator=' ')

                # Do more preprocessing to remove non-natural-language text
                text = html.unescape(text)  # unescape characters
                text = "".join((  # remove punctuation & numbers
                    char for char in text if char in acceptable_characters
                ))
                text = re.sub(r"\s+", " ", text)  # remove excessive whitespace

                page_content = WebContent(site_title, text, url)
                print("returning from webpage downloader")

                return page_content

        except asyncio.TimeoutError:
            print("site timeout occurred")
            return WebContent("", "", "")

        except:
            return WebContent("", "", "")
