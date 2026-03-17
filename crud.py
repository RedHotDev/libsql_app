from sqlalchemy import select, and_, func
from models import Category
from  database import get_db
from typing import List


def get_categories() :
    # выбрать все записи из таблицы Category
    with get_db() as db:
        stmt = select(Category)
        # return db.execute(stmt).all()
        return db.execute(stmt).scalars().all()
    
    
def get_category_id(id: int):
    with get_db() as db:
        stmt = select(Category).where(Category.id == id) 
        return db.execute(stmt).scalars().all()


def get_categories_count():
    # выбрать все записи из таблицы Category
    with get_db() as db:
        stmt = func.count(Category.id)
        return db.execute(stmt).scalar_one_or_none()
