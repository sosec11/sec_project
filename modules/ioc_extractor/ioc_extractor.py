import re

from .patterns import ID_PATTERN, EMAIL_PATTERN, URL_PATTERN

def extract_iocs(text):
    ips = re.findall(ID_PATTERN, text)
    emails = re.findall(EMAIL_PATTERN, text)
    urls = re.findall(URL_PATTERN, text)

    return ips, emails, urls