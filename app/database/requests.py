from app.database.models import User, Category, Item, Basket
from app.database.models import async_session

from sqlalchemy import select, update, delete


async def set_user(tg_id):
    async with async_session() as sesssion:
        user = await sesssion.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            sesssion.add(User(tg_id=tg_id))
            await sesssion.commit()

async def get_users():
    async with async_session() as sesssion:
        users = await sesssion.scalars(select(User))
        return users


async  def get_categories():
    async with async_session() as sesssion:
        categories = await sesssion.scalars(select(Category))
        return categories

async  def get_items_by_category(category_id: int):
    async with async_session() as sesssion:
        items = await sesssion.scalars(select(Item).where(Item.category == category_id))
        return items

async  def get_item_by_id(item_id: int):
    async with async_session() as sesssion:
        item = await sesssion.scalar(select(Item).where(Item.id == item_id))
        return item

