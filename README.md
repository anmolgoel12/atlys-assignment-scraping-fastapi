# Atlys Web Scraping Project with Fast API

## Architecture
- Service `DentalStallScrapper` class is responsible to scrape data from respective website and return data in structure format.
    - Retry mechanism is handled by `HTTPAdapter` & `Retry` module of `requests.adapter`
- Storage `FileStorage` class acts as persistant storage, data scrapped is stored in file products.json, indexed with product id scrapped from URL.
    - This class is responsible to update and add product depending upon price update
- Custom In memory `InMemoryCache` Class handles the cache mechanism, which stores in key value format
    - `set_data` function set the value for a key
    - `get_data` function returns the cached value for a key
    - `remove_key` function deletes the key from cache