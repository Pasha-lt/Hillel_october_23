import requests

url_picture = 'https://www.imgonline.com.ua/examples/bee-on-daisy.jpg'
response = requests.get(url_picture)

with open("image.jpg", "wb") as f:
    for chunk in response.iter_content(chunk_size=1024):
        f.write(chunk)
        