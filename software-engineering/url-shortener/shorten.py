#!/usr/bin/env python3
import cmd
import json
import string
import random
import os
from selenium.webdriver import Firefox
"""
URL shortner module
"""

class UrlShortener(cmd.Cmd):
    """
    URL shortner console 
    """
    intro = 'Welcome to the URL shortener CLI. Type "help" to list commands.\n'
    prompt = '(shortener) '
    
    def __init__(self, urls_file='urls.json'):
        super().__init__()
        self.urls_file = urls_file
        self.urls = {}
        self.load_urls()
    
    def load_urls(self):
        try:
            with open(self.urls_file, 'r') as f:
                self.urls = json.load(f)
        except FileNotFoundError:
            pass
    
    def save_urls(self):
        with open(self.urls_file, 'w') as f:
            json.dump(self.urls, f)
    
    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))
    
    def do_shorten(self, url):
        """Shorten a URL.
        Args:
            url(str): The url to shorten
        For God's sake, include `https://`
        """
        while True:
            short_url = self.generate_short_url()
            if short_url not in self.urls:
                break
        self.urls[short_url] = url
        self.save_urls()
        print("URL shortened to {}".format(short_url))
    
    def do_redirect(self, short_url):
        """Redirect a short URL to its corresponding long URL."""
        if short_url in self.urls:
            print(f'Redirecting to: {self.urls[short_url]}')
            broswer = Firefox()
            broswer.get(self.urls[short_url])
        else:
            print(f'Error: Short URL {short_url} not found.')

    def do_list_all(self, self_):
        """
        List all shortened urls
        """
        if os.path.isfile("urls.json"):
            with open("urls.json", "r", encoding="UTF=8") as f:
                 data = json.load(f)
                 for k, v in data.items():
                    print("{} -> {}".format(k, v))
       
        else:
            print("There are no urls at the moment")
    
    def do_exit(self, arg):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    UrlShortener().cmdloop()
