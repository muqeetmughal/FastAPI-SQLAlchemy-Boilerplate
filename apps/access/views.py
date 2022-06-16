from fastapi import APIRouter, Depends
from dependencies import get_db
from . import models, schema
from sqlalchemy.orm import Session

access = APIRouter()


@access.post("/role/add")
async def create_role(request: schema.CreateRoleSchema, db: Session = Depends(get_db)):

    role = models.Role()
    role.name = request.name

    db.add(role)
    db.commit()

    return request
