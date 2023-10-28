#!/usr/bin/env python

import requests
from collections import OrderedDict
from bs4 import BeautifulSoup

# URL of the website you want to scrape
base = "https://dictionary.cambridge.org"
ench_dict = "dictionary/english-chinese-simplified"
agents = [
    "Mozilla/5.0 (X11; Linux x86_64)",
    "AppleWebKit/537.36 (KHTML, like Gecko)",
    "Chrome/115.0.0.0",
    "Safari/537.36",
    "Edg/115.0.1901.200",
]

# Send an HTTP request to the website
session = requests.Session()
session.trust_env = False
headers = {"User-Agent": " ".join(agents)}


def find_by_tag(soup, tag):
    return soup.find_all(tag)


def find_by_class(soup, cls):
    return soup.find_all(class_=cls)


def query(vocabulary):
    url = f"{base}/{ench_dict}/{vocabulary}"
    response = session.get(url, headers=headers)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    result = OrderedDict()
    sections = [
        "title",
        "explain",
        "explain_cn",
        "example",
        "example_cn",
        "phrase",
        "audio_src",
    ]
    for section in sections:
        result[section] = list()

    for element in find_by_class(soup, "hw dhw"):
        result["title"].append(element.text)

    for element in find_by_class(soup, "phrase-title dphrase-title"):
        result["phrase"].append(element.text)

    for element in find_by_class(soup, "def ddef_d db"):
        result["explain"].append(element.text)

    for element in find_by_class(soup, "eg deg"):
        result["example"].append(element.text)

    for element in find_by_class(soup, "trans dtrans dtrans-se break-cj"):
        result["explain_cn"].append(element.text)

    for element in find_by_class(soup, "trans dtrans dtrans-se hdb break-cj"):
        result["example_cn"].append(element.text)

    for element in find_by_tag(soup, "audio"):
        result["audio_src"].append(base + element.find("source")["src"])

    return result
