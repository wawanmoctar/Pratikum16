import requests

def indo():
    api_url="https://api.kawalcorona.com/indonesia/"
    rstl= requests.get(api_url).json()
    return rstl

def JawaBarat():
    api_url="https://api.kawalcorona.com/indonesia/provinsi/"
    rstl= requests.get(api_url).json()
    return rstl

data_indo=indo()
data_JawaBarat=JawaBarat()
