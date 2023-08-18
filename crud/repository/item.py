from sqlalchemy.orm import Session
from crud import schemas,database,models
from fastapi import APIRouter,Depends,HTTPException,status,Response


def get_item_by_id(item_id:int,db:Session):
    item = db.query(models.Items).filter(models.Items.id == item_id).first()
    if not item:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'blog with the id {item_id} is not found')
    return item

def get_all_items(db:Session):
    items = db.query(models.Items).all()
    return items

def create(request:schemas.Item,db:Session):
    new_item = models.Items(name=request.name,price=request.price,brand=request.brand)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update(item_id:int,request:schemas.UpdateItem,db:Session):
    item = db.query(models.Items).filter(models.Items.id == item_id)
    if not item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with the id {item_id} is not found')
    item.update(dict(request))
    db.commit()
    return {"success":"update item successfully"}

def delete(item_id:int,db:Session):
    item = db.query(models.Items).filter(models.Items.id == item_id).delete(synchronize_session=False)
    if not item:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f'blog with the id {item_id} is not found')
    db.commit()
    return {"success":"delete item successfully"}