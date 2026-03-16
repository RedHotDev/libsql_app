from sqlalchemy import select, and_
from models import Category
from  database import get_db
from typing import List


def get_categories() :
    with get_db() as db:
        stmt = select(Category)
        return db.execute(stmt).all()
        return db.execute(stmt).scalars().all()
    
    
def get_category_id(id: int):
    with get_db() as db:
        stmt = select(Category).where(Category.id == id)
        
        return db.execute(stmt).scalars().all()
