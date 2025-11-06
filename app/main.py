from fastapi import FastAPI

from app.routes import hotel_manager, hotel

app = FastAPI(title='MyStay API')

app.include_router(hotel_manager.router, prefix='/api')
app.include_router(hotel.router, prefix='/api')
