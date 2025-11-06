from fastapi import FastAPI

from app.routes import hotel_manager

app = FastAPI(title='MyStay API')

app.include_router(hotel_manager.router, prefix='/api')
