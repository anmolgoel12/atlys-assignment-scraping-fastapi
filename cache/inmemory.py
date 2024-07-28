import json
import os
from config.settings import settings


class InMemoryCache:
    keychain = {}

    def set_data(self, key, data):
        self.keychain[key] = data

    def remove_key(self, key):
        self.keychain.pop(key)

    def get_data(self, key):
        if key in self.keychain:
            return self.keychain[key]
        return None


custom_cache = InMemoryCache()
## init cache
data = {}
with open(os.path.join(settings.BASE_DIR, "data/products.json"), "r") as file:
    data = json.load(file)
custom_cache.set_data("products", data)
