from pydantic import BaseModel
from typing import List, Optional

# Defined Users Request for create address.
class AddressCreate(BaseModel):
    village: str
    pincode: str
    distance: str
    state: str
    country: str

# Defined Users request for update address based on this columns.
class AddressUpdate(BaseModel):
    village: Optional[str]
    pincode: Optional[str]
    distance: Optional[str]
    state: Optional[str]
    country: Optional[str]

class SearchAddress(BaseModel):
    pincode: Optional[str]
    distance: Optional[str]
    state: Optional[str]