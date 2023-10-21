from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from app.address.controller import address_controller

app = FastAPI()

app.include_router(address_controller.router, prefix="/address", tags=["address"])

app = VersionedFastAPI(
    app,
    version_format="{major}",
    prefix_format="/fastapi-test/v{major}",
)