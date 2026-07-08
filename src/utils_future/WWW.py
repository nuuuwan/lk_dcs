import hashlib
import os
import tempfile

import requests

from utils_future.console.Log import Log
from utils_future.file.File import File

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

    @property
    def temp_file(self):
        temp_dir = os.path.join(tempfile.gettempdir(), "lk_dcs", "www")
        os.makedirs(temp_dir, exist_ok=True)
        h = hashlib.md5(self.url.encode("utf-8")).hexdigest()
        ext = self.url.split(".")[-1]
        return File(os.path.join(temp_dir, f"{h}.{ext}"))

    def get_response(self):
        response = requests.get(
            self.url,
            headers=self.HEADERS,
            timeout=self.T_TIMEOUT,
            verify=False,
        )
        response.raise_for_status()
        return response

    def download_binary(self) -> str:
        if self.temp_file.exists:
            return self.temp_file

        CHUNK_SIZE = 1024
        response = self.get_response()
        file_path = self.temp_file.path
        with open(file_path, "wb") as fd:
            for chunk in response.iter_content(CHUNK_SIZE):
                fd.write(chunk)
        return self.temp_file
