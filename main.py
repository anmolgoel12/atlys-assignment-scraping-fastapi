from fastapi import Depends, FastAPI, Query

from services.authentication import get_token
from services.scraper import DentalStallScrapper
from storage.file import FileStorage
from cache.inmemory import custom_cache

app = FastAPI()


@app.get("/scrape")
async def scrape(limit: int = Query(default=1), token: str = Depends(get_token)):
    scrape_service = DentalStallScrapper()
    data = scrape_service.scrape_products(limit=limit)
    db = FileStorage("data")
    custom_cache.get_data("products")
    count = db.set_data(data)
    return {
        "message": f"Scrapping successfull: Total product scrapped are {count['total']} out of which {count['added']} no of new products added and {count['updated']} no of product price was updated.",
        "status": 1,
    }
