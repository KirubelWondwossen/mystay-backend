from app.database import Base, engine
from app.models.users import HotelManager, Guest
from app.models.hotel import Hotel
from app.models.room import Room

print("Creating tables in database...")
Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
