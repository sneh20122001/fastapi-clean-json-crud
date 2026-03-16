from fastapi import HTTPException
from app.repositories.item_repository import ItemRepository
from app.core.logger import logger

class ItemService:

    def __init__(self):
        self.repo = ItemRepository()

    def get_items(self):
        logger.info("Fetching all items")
        return self.repo.get_all()
    
    def get_item(self, id):

        item = self.repo.get_by_id(id)
        if not item:
            logger.error(f"Item with id {id} not found")
            raise HTTPException(status_code=404, detail="Item not found")
        return item
    
    def create_item(self, item_data):
        logger.info(f"Creating item with data: {item_data}")
        return self.repo.create(item_data)
    
    def update_item(self, id, item_data):

        updated_item = self.repo.update(id, item_data)
        if not updated_item:
            logger.error(f"Item with id {id} not found for update")
            raise HTTPException(status_code=404, detail="Item not found")
        return updated_item
    
    def delete_item(self, id):

        deleted_item = self.repo.delete(id)
        if not deleted_item:
            logger.error(f"Item with id {id} not found for deletion")
            raise HTTPException(status_code=404, detail="Item not found")
        return deleted_item