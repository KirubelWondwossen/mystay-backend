from fastapi import FastAPI

from app.routes import hotel_manager, hotel, room

app = FastAPI(title='MyStay API')

app.include_router(hotel_manager.router, prefix='/api')
app.include_router(hotel.router, prefix='/api')
app.include_router(room.router, prefix='/api')
