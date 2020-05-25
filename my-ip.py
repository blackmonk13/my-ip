#!/usr/bin/env python
# Copyright 2020 Blackmonk13. All rights reserved.
#
# This software is provided under under the 
# GNU GPL V3 License. See the accompanying LICENSE file
# for more information.
#
# Author:
#  blackmonk (@protonmail.com)
#
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'
    }

ipvoid_url = "https://www.ipvoid.com/my-ip/"

def get_ip():
    req = requests.get(ipvoid_url, headers=headers, timeout=10)

    if req.status_code == requests.codes.ok:
        ip_content = req.text
        ip_soup = BeautifulSoup(ip_content, features="html5lib")
        ip_addr_soup = ip_soup.find('textarea').text
        print(ip_addr_soup)

if __name__ == "__main__":
    get_ip()
