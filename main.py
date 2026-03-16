from database import Base, engine, get_db
from models import Category
from crud import get_categories, get_category_id


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Создание таблиц")

def insert_data():
    with get_db() as db:
        categoryes = [
            Category(name='Контроллеры'),
            Category(name='Материнские платы'),
            Category(name='Процессоры'),  
        ]
        print("Вставка данных")
        db.add_all(categoryes)
        db.commit()

def select_data_id(id):
    s = get_category_id(id)
    print(s[0].name)
    

def select_data():
    s = get_categories()
    for i in s:
        print(i.Category.name)
    


init_db()
insert_data()
select_data()
