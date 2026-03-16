import json 
from pathlib import Path

DATA_FILE = Path("app/data/items.json")

class ItemRepository:

    def read(self):
        with open(DATA_FILE,"r") as file:
            return json.load(file)
    
    def write(self, data):
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    def get_all(self):
        return self.read()
    
    def get_by_id(self, id):
        items = self.read()

        for item in items:
            if item["id"] == id:
                return item
        return None
    
    def create(self, item_data):
        items = self.read()

        new_id = 1 if items else max(item["id"] for item in items) + 1
        item_data['id'] = new_id

        items.append(item_data)
        self.write(items)

        return item_data
    
    def update(self, id, item_data):
        items = self.read()

        for index, item in enumerate(items):
            if item["id"] == id:
                item_data['id'] = id
                items[index] = item_data
                self.write(items)
                return item_data
            
        return None
    
    def delete(self, id):
        items = self.read()

        for index, item in enumerate(items):
            if item["id"] == id:
                deleted = items.pop(index)
                self.write(items)
                return deleted 
            
        return None