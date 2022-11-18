from fastapi import FastAPI
from routes.users import user

app = FastAPI(
    title="My API",
    version="0.0.1",
    description="Mi primera app",
    openapi_tags=[{
        "name": "users",
        "description": "user routes"
    }]
)

app.include_router(user)
