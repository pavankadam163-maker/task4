import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.amazon.in/s?k=mobiles"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Rating"])
    products = soup.find_all("div", {"data-component-type": "s-search-result"})
    for product in products:
        name_tag = product.h2
        name = name_tag.text.strip() if name_tag else "N/A"
        price_tag = product.find("span", class_="a-price-whole")
        price = price_tag.text.strip() if price_tag else "N/A"
        rating_tag = product.find("span", class_="a-icon-alt")
        rating = rating_tag.text.strip() if rating_tag else "N/A"
        writer.writerow([name, price, rating])

print("Product data extracted and saved to 'products.csv'")
