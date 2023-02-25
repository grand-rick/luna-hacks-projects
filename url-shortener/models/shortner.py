#!/usr/bin/env python3
import json
import re

def is_valid_url(url)  -> bool:
        regex = re.compile(
        r'^https?://'  # Scheme (http, https)
        r'([A-Za-z0-9-]+\.)+[A-Za-z]{2,}'  # Domain name (e.g. example.com)
        r'(:\d{1,5})?'  # Port number (optional)
        r'(/[-a-zA-Z0-9._~:/?#[\]@!$&\'()*+,;=]*)?'  # Path (optional)
        r'(\?[a-zA-Z0-9-._~:/?#[\]@!$&\'()*+,;=]*)?'  # Query string (optional)
        r'(#[-a-zA-Z0-9._~:/?#[\]@!$&\'()*+,;=]*)?$'  # Fragment identifier (optional)
        )
        return bool(regex.match(url))

class Shortener(object):
    """
    URL shortner class
    """
    url_file = "urls-file.json"
    objects = {}


    def __init__(self):
        self.urls_file = __class__.urls_file
        self.urls = {}
        self.load_urls()

    
   
    
    def load_urls(self) -> None:
        try:
            with open(self.urls_file, 'r', encoding="UTF-8") as f:
                return(json.loads(f))
        except FileNotFoundError:
            return "No urls Shortened"

    
    def generate_short_url(self, url, short) -> None:
        """
        Generate a short url
        Args:
            url (str): the url to shorten
            short (str): the name to associate the URL with
        """
        if not is_valid_url(url):
            raise ValueError("A valid URL please")
        if not isinstance(short, str):
            raise ValueError("short must be a string")
        if short in self.load_urls().keys():
            raise ValueError("That short value already exists")
        else:
            __class__.objects[url] = short
            self.save_urls()

        
    def save_urls(self):
        try:
            with open(Shortener.url_file,  "w", encoding="UTF-8") as storage:
                json.dump(__class__.objects, storage)
        except Exception as e:
            return ("Could not save because {}".format(e))