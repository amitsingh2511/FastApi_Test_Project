from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi_versioning import version

from ..dto import request_model


router = APIRouter()


# Dadabase Urls
DATABASE_URL = "sqlite:///./pythontest.db"

Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, index=True)
    village = Column(String, index=True)
    pincode = Column(String, index=True)
    distance = Column(String, index=True)
    state = Column(String, index=True)
    country = Column(String, index=True)

Base.metadata.create_all(bind=engine)


# Create Address using this api
@router.post("/addresses/")
def create_address(address: request_model.AddressCreate):
    db = SessionLocal()
    db_address = Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

# Update Address using this api
@router.get("/addresses/{address_id}", status_code=200)
@version(1)
def update_address(address_id: int, address: request_model.AddressUpdate):
    db = SessionLocal()
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    for key, value in address.dict().items():
        setattr(db_address, key, value)
    db.commit()
    db.refresh(db_address)
    return db_address

# Delete Address using this api
@router.delete("/addresses/{address_id}")
def delete_address(address_id: int):
    db = SessionLocal()
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    db.delete(db_address)
    db.commit()
    return db_address

# Get Address By Search Criteria using this api
@router.get("/addresses/",)
def get_addresses(address: request_model.SearchAddress = Depends()):
    db = SessionLocal()
    db_address = db.query(Address).all()
    if address.state:
        db_address = db.query(Address).filter(Address.state == address.state).all()
    if address.distance:
        db_address = db.query(Address).filter(Address.distance == address.distance).all()
    return db_address

# Get Address By Id using this api
@router.get("/addresses/{address_id}")
def get_address_by_id(address_id: int):
    db = SessionLocal()
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

# Update Address using this api
@router.put("/addresses/{address_id}")
def update_address(address_id: int, address: request_model.AddressUpdate):
    db = SessionLocal()
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    for key, value in address.dict().items():
        setattr(db_address, key, value)
    db.commit()
    db.refresh(db_address)
    return db_address