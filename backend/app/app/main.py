from fastapi import FastAPI


from app.api.routes import api_router
from app.config.settingsConfiguration import settings


app = FastAPI()
app.include_router(api_router, prefix=settings.API_V1_STR)

