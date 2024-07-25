from fastapi import FastAPI, Query

from services.scraper import DentalStallScrapper

app = FastAPI()


@app.get("/test")
async def root(limit: int = Query(default=1)):
    scrape_service = DentalStallScrapper()
    return scrape_service.scrape_products(limit=limit)
