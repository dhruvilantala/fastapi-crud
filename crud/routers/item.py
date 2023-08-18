from fastapi import APIRouter,Depends,HTTPException,status,Response,Path
from typing import List
from crud import schemas
from crud.database import get_db
from sqlalchemy.orm import Session
from crud.repository import item

router = APIRouter(
    prefix='/items',
    tags=['CRUD items']
)


@router.get("/get-all-items", response_model=List[schemas.Item])
def all_item(db:Session=Depends(get_db)):
    return item.get_all_items(db)

@router.get('/{item_id}', response_model=schemas.Item)
def read_item(item_id: int = Path(description="The id of the item you'd like to view"),db:Session=Depends(get_db)):
    return item.get_item_by_id(item_id,db)

@router.post("/create-item", status_code=status.HTTP_201_CREATED)
def create_item(request:schemas.Item, db:Session=Depends(get_db)):
    return item.create(request,db)

@router.put("/update-item/{item_id}",status_code=status.HTTP_202_ACCEPTED)
def update_item(item_id:int ,request:schemas.UpdateItem, db:Session=Depends(get_db)):
    return item.update(item_id,request,db)

@router.delete("/delete-item", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id:int,db:Session=Depends(get_db)):
    return item.delete(item_id,db)