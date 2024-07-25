from typing import List
import requests as _requests
import bs4 as _bs4


class DentalStallScrapper:
    base_url = "https://dentalstall.com"
    limit = None

    def _get_soup_from_url(self, url: str) -> _bs4.BeautifulSoup:
        page = _requests.get(url)
        soup = _bs4.BeautifulSoup(page.content, "html.parser")
        return soup

    def _parse_soup_product_details(self, soup: _bs4.BeautifulSoup):
        products = []
        product_list = soup.select("li.product.type-product")
        for product in product_list:
            image = (product.select("div.mf-product-thumbnail")[0]).find("img")[
                "data-lazy-src"
            ]
            name = (
                (product.find("h2", class_="woo-loop-product__title"))
                .find("a")
                .text.strip()
            )
            print(name)
            id = (product.find("div", class_="addtocart-buynow-btn")).find("a")[
                "data-product_id"
            ]

            price = (
                (product.find("span", class_="woocommerce-Price-amount amount"))
                .find("bdi")
                .text.strip()
            )
            products.append(
                {
                    "id": id,
                    "name": name,
                    "price": price,
                    "image": image,
                }
            )
        return products

    def scrape_products(self, limit=1):
        products = []
        product_url = "/shop"
        page1_products = self._get_soup_from_url(f"{self.base_url}{product_url}")
        products_list = self._parse_soup_product_details(page1_products)
        products += products_list
        for page in range(2, limit + 1):
            products_soup = self._get_soup_from_url(
                f"{self.base_url}{product_url}/page/{page}/"
            )
            products_list = self._parse_soup_product_details(products_soup)
            products += products_list
            pass
        return products
