### Helper functions file ###

import re

# example urls
# https://www.youtube.com/watch?v=sV5BjXgaFvI
# https://www.youtube.com/watch?v=sV5BjXgaFvI&t=63s
# https://youtu.be/sV5BjXgaFvI
def parse_youtube_url(url):
    match = re.search(r"youtube\.com/.*v=([^&]*)", url)
    if match:
        result = match.group(1)
    else:
        result = ""
    return result
    