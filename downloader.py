import os
import time
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote
from tqdm import tqdm


def safe_name(name):
    return (
        name.replace(":", "_")
        .replace("?", "")
        .replace("*", "")
        .replace("|", "")
        .replace("<", "")
        .replace(">", "")
        .replace('"', "")
    )


def download_with_progress(url, file_path):
    response = requests.get(url, stream=True, timeout=30)
    response.raise_for_status()

    total_size = int(response.headers.get("content-length", 0))
    chunk_size = 8192  # 8 KB

    with open(file_path, "wb") as f, tqdm(
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        desc=os.path.basename(file_path),
        ascii=True,
    ) as bar:
        for chunk in response.iter_content(chunk_size):
            if chunk:
                f.write(chunk)
                bar.update(len(chunk))


def crawl(url, local_dir):
    os.makedirs(local_dir, exist_ok=True)

    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
    except Exception as e:
        print(f"[!] Cannot open {url}: {e}")
        return

    soup = BeautifulSoup(r.text, "html.parser")

    for a in soup.find_all("a", href=True):
        href = a["href"]

        # Skip unwanted links
        if href in ("../", "./") or href.startswith(("?", "/", "#")):
            continue

        full_url = urljoin(url, href)
        name = safe_name(unquote(href.strip("/")))

        if href.endswith("/"):
            crawl(full_url, os.path.join(local_dir, name))
        else:
            file_path = os.path.join(local_dir, name)

            if os.path.exists(file_path):
                print(f"[=] Already exists: {file_path}")
                continue

            print(f"\n[↓] Downloading:")
            try:
                download_with_progress(full_url, file_path)
                time.sleep(0)  # be polite
            except Exception as e:
                print(f"[!] Failed: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Recursive course downloader with progress bar"
    )
    parser.add_argument(
        "-u", "--url",
        required=True,
        help="Base URL to crawl and download from"
    )
    parser.add_argument(
        "-o", "--output",
        default="Downloads",
        help="Output directory (will be created if not exists)"
    )

    args = parser.parse_args()

    print(f"[+] Starting download")
    print(f"    URL    : {args.url}")
    print(f"    Output : {args.output}\n")

    crawl(args.url, args.output)


if __name__ == "__main__":
    main()
