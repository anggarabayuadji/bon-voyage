import requests
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from bs4 import BeautifulSoup

# Mencari lokasi yang dituju di Google
find = input()
url = f"https://www.google.com/search?q={find}"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
mysearch = soup.find
print(mysearch.text)

# Create your views here.