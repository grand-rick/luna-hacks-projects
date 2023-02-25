#!/usr/bin/env python3
import cmd
from models.shortner import Shortener as sh
"""
URL shortner console module
"""

class UrlShortenerConsole(cmd.Cmd):
    intro = 'Welcome to the URL shortener CLI. Type "help" to list commands.\n'
    prompt = '(shortener) '
    
    def do_shorten(self, args):
        """Shorten a URL."""
        try:
            if len(args) != 2:
                print("You should specify the url and its short version")
            else:
                args = args.split(" ")
            short = args[1]
            url = args[0]
            sh.generate_short_url(self, url, short)
            print("URL  created {} -> {}".format(short, url))
        except Exception as e:
            print(e)
        # print(len(args.split(" ")))
    
    def do_redirect(self, short_url):
        """Redirect a short URL to its corresponding long URL."""
        if short_url in self.urls:
            print(f'Redirecting to: {self.urls[short_url]}')
        else:
            print(f'Error: Short URL {short_url} not found.')

    def do_load_urls(self):
        """
        Load URLs that are already saved print them to 
        stdout
        """
        sh.load_urls(self)
    
    def do_exit(self, arg):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    UrlShortenerConsole().cmdloop()
