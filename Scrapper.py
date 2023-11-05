import requests
from bs4 import BeautifulSoup

#Function to find the price and name from amazon
def amazon_scrapper(url_amazon):
    try:
        session = requests.Session()
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/95.0.4638.69 Safari/537.36"}
        html_amazon = session.get(url_amazon, headers=headers)

        if html_amazon.status_code != 200:
            print("Error: Request to Amazon failed with status code", html_amazon.status_code)
            return

        soup_amazon = BeautifulSoup(html_amazon.content, "html.parser")
        price_amazon = soup_amazon.find("span", attrs={"class": 'a-price-whole'})
        product_name_amazon = soup_amazon.find("span", attrs={"id": 'productTitle'})
        if product_name_amazon is not None:
            name_amazon = product_name_amazon.text.strip()
        else:
            name_amazon = None
        if price_amazon is not None:
            price_amazon = price_amazon.text.strip()
        else:
            price_amazon = None

        return {'Product Name from Amazon': name_amazon, 'Price from Amazon': price_amazon}
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to access the URL of Amazon: {e}")
        return

#Function to find the price and name from flipkart
def flipkart_scrapper(url_flipkart):
    try:
        html_flipkart = requests.get(url_flipkart)
        if html_flipkart.status_code != 200:
            print("Error: Request to Flipkart failed with status code", html_flipkart.status_code)
            return
        soup_flipkart = BeautifulSoup(html_flipkart.content, "html.parser")
        price_flipkart = soup_flipkart.find("div", attrs={"class": '_30jeq3 _16Jk6d'})
        product_name_flipkart = soup_flipkart.find("span", attrs={"class": 'B_NuCI'})
        if product_name_flipkart is not None:
            name_flipkart = product_name_flipkart.text.strip()
        else:
            name_flipkart = None
        if price_flipkart is not None:
            price_flipkart = price_flipkart.text.strip()
        else:
            price_flipkart = None
        return {'Product Name from Flipkart': name_flipkart, 'Price from Flipkart': price_flipkart}
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to access the URL of Flipkart: {e}")
        return None, None


if __name__ == '__main__':
    url_amazon = input("Please enter the Amzon url: ")
    url_flipkart = input("Please enter the Flipkart url: ")
    product_amazon = amazon_scrapper(url_amazon)
    print(product_amazon)
    product_flipkart = flipkart_scrapper(url_flipkart)
    print(product_flipkart)
