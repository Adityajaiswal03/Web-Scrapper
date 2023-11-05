# Web Scraping Price Comparison

This Python script demonstrates how to scrape product information, including product names and prices, from Amazon and Flipkart websites using the Requests and BeautifulSoup libraries.

## Prerequisites

Before running the script, ensure that you have Python installed and the following libraries are installed:

- Requests
- Beautiful Soup

You can install these libraries using `pip3`:

```bash
pip3 install requests
pip3 install beautifulsoup4
```

## Usage

1. Clone or download the script to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script by executing the following command:

   ```bash
   python3 price_comparison.py
   ```

4. You will be prompted to enter the URLs of products on Amazon and Flipkart that you want to compare.

5. The script will fetch the product information from both websites and display the results, including the product name and price.

## Script Components

- The script defines two functions: `amazon_scrapper` and `flipkart_scrapper`, which scrape product information from Amazon and Flipkart, respectively.

- Each function takes a URL as an input and uses Requests to make an HTTP request to the respective website.

- If the HTTP request is successful (status code 200), the script uses BeautifulSoup to parse the HTML content of the page.

- The script then looks for specific HTML elements (product name and price) based on their class or ID attributes on the web pages.

- If the elements are found, their content is extracted and returned in a dictionary with keys 'Product Name' and 'Price' for Amazon and Flipkart, respectively.

- If any errors occur during the process, such as an invalid URL or a failed HTTP request, the script will handle these exceptions and display an error message.

- In the main part of the script, the user is prompted to input the URLs for Amazon and Flipkart products. The script calls the scraping functions, and the extracted product information is displayed.

