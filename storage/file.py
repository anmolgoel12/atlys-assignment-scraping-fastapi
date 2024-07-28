import os, json

from fastapi import HTTPException
from pathlib import Path
from cache.inmemory import custom_cache

ROOT_DIrectory = Path(__file__).resolve().parent.parent


class FileStorage:
    path = None

    def __init__(self, path):
        if not os.path.exists(os.path.join(ROOT_DIrectory, path)):
            os.mkdir(os.path.join(ROOT_DIrectory, path))
        self.path = os.path.join(ROOT_DIrectory, path)

    def _dump_data_in_file(self, data):

        # Open the file and load the JSON data
        ## getting product from cache
        products = custom_cache.get_data("products")

        file_path = f"{self.path}/products.json"
        count = {"total": 0, "added": 0, "updated": 0}

        # with open(file_path, "r") as file:
        #     products = json.load(file)

        for product in data:
            if (
                product in products
                and data[product]["price"] != products[product]["price"]
            ):
                products[product]["price"] = data[product]["price"]
                count["updated"] += 1
            elif product not in products:
                products[product] = data[product]
                count["added"] += 1
            count["total"] += 1
        with open(file_path, "w") as file:
            data = json.dump(products, file)
        ## updating cache value
        custom_cache.set_data("products", products)
        return count

    def get_product_by_Id(self, id):
        # Define the path to your JSON file
        file_path = f"{self.path}/products.json"

        # Open the file and load the JSON data
        with open(file_path, "r") as file:
            data = json.load(file)

        # Print the data to verify it's loaded correctly
        print(data)
        if id not in data:
            raise HTTPException(400, f"Product with product id {id} not found")
        return data[id]

    def update_product_by_Id(self, id, data):
        # Define the path to your JSON file
        file_path = f"{self.path}/products.json"

        # Open the file and load the JSON data
        with open(file_path, "r") as file:
            data = json.load(file)

        # Print the data to verify it's loaded correctly
        print(data)
        if id not in data:
            raise HTTPException(400, f"Product with product id {id} not found")
        return data[id]

    def delete_product_by_Id(self, id):
        # Define the path to your JSON file
        file_path = f"{self.path}/products.json"

        # Open the file and load the JSON data
        with open(file_path, "r") as file:
            data = json.load(file)

        # Print the data to verify it's loaded correctly
        print(data)
        if id not in data:
            raise HTTPException(400, f"Product with product id {id} not found")
        return data[id]

    def add_product_by_Id(self, id, data):
        # Define the path to your JSON file
        file_path = f"{self.path}/products.json"

        # Open the file and load the JSON data
        with open(file_path, "r") as file:
            data = json.load(file)

        # Print the data to verify it's loaded correctly
        print(data)
        if id not in data:
            raise HTTPException(400, f"Product with product id {id} not found")
        return data[id]

    def set_data(self, data):
        count = self._dump_data_in_file(data)
        return count
