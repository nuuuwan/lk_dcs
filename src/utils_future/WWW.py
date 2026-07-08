import requests

from utils_future.console.Log import Log

log = Log("WWW")


class WWW:

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        + " AppleWebKit/537.36 (KHTML, like Gecko)"
        + " Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application"
        + "/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    T_TIMEOUT = 120

    def __init__(self, url: str):
        self.url = url

    def __str__(self) -> str:
        return f"🌐{self.url}"

    def get_response(self):
        response = requests.get(
            self.url,
            headers=self.HEADERS,
            timeout=self.T_TIMEOUT,
            verify=False,
        )
        response.raise_for_status()
        return response

    def download_binary(self, file_path) -> str:
        CHUNK_SIZE = 1024
        response = self.get_response()
        with open(file_path, "wb") as fd:
            for chunk in response.iter_content(CHUNK_SIZE):
                fd.write(chunk)
        return file_path
