from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
from datetime import datetime

# CREATE DATA FOLDER
if not os.path.exists("laptop_data"):
    os.makedirs("laptop_data")

# CHROME OPTIONS
options = Options()
options.add_argument("--start-maximized")

# OPEN CHROME
driver = webdriver.Chrome(options=options)

# SEARCH QUERY = LAPTOPS
query = "laptops"

file_count = 0

# SCRAPE AMAZON LAPTOP PAGES
for page in range(1, 6):

    url = f"https://www.amazon.in/s?k={query}&page={page}"

    driver.get(url)

    time.sleep(3)

    products = driver.find_elements(By.CLASS_NAME, "puis-card-container")

    print(f"Page {page} -> {len(products)} laptops found")

    for product in products:

        try:
            html = product.get_attribute("outerHTML")

            with open(f"laptop_data/laptop_{file_count}.html",
                      "w",
                      encoding="utf-8") as f:
                f.write(html)

            file_count += 1

        except Exception as e:
            print(e)

driver.quit()

# EXTRACT LAPTOP DETAILS
data = {
    "Title": [],
    "Price": [],
    "Rating": [],
    "Image": [],
    "Product Link": [],
    "Ad/Organic Result": []
}

# READ SAVED HTML FILES
for file in os.listdir("laptop_data"):

    try:
        with open(f"laptop_data/{file}", encoding="utf-8") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, "html.parser")

        # TITLE
        
        title_tag = soup.find("h2")

        if title_tag:
            title = title_tag.get_text(strip=True)
        else:
            title = "N/A"

        # PRODUCT LINK
 
        link_tag = soup.find("h2").find("a")

        if link_tag:
            product_link = "https://www.amazon.in" + link_tag.get("href")
        else:
            product_link = "N/A"

        # PRICE
        price_tag = soup.find("span", class_="a-price-whole")

        if price_tag:
            price = price_tag.get_text(strip=True)
        else:
            price = "N/A"
        # IMAGE
        image_tag = soup.find("img", class_="s-image")

        if image_tag:
            image = image_tag.get("src")
        else:
            image = "N/A"

        # RATING

        rating_tag = soup.find("span", class_="a-icon-alt")

        if rating_tag:
            rating = rating_tag.get_text(strip=True)
        else:
            rating = "N/A"

        # AD / ORGANIC RESULT
        sponsored = soup.find(
            string=lambda text: text and "Sponsored" in text
        )

        if sponsored:
            result_type = "Ad"
        else:
            result_type = "Organic"
        # STORE DATA
        data["Title"].append(title)
        data["Price"].append(price)
        data["Rating"].append(rating)
        data["Image"].append(image)
        data["Product Link"].append(product_link)
        data["Ad/Organic Result"].append(result_type)

    except Exception as e:
        print("Error:", e)

# CREATE DATAFRAME
df = pd.DataFrame(data)

# SAVE CSV WITH TIMESTAMP
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

csv_file = f"Laptop_Data_{timestamp}.csv"

df.to_csv(csv_file, index=False, encoding="utf-8")

# OUTPUT
print("\nLaptop Data Scraping Completed Successfully")
print(f"CSV File Saved As: {csv_file}")

print(df.head())