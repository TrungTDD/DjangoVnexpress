from typing import Any
import feedparser
from bs4 import BeautifulSoup

def parse_rss(rss_url: str) -> Any:
    try: 
        feed = feedparser.parse(rss_url)
        entries = feed.entries
        parsed_info = []
    except:
        return None
    else: 
        for item in entries:
            if item:
                parsed_html = BeautifulSoup(item["summary"], "html.parser")
                img_src = ""
                if parsed_html.find("a"):
                    img_src = parsed_html.find("a").find("img").get("src") 
                
                
                parsed_info.append({"title" : item["title"], "link" : item["link"], "description" : parsed_html.text, "img" : img_src})
        return parsed_info