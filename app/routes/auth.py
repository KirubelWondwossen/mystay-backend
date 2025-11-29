from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app.core.auth import oauth
from app.database import get_db
from app.models.users import Guest
from app.schemas.users import GuestDisplay
from jose import jwt
import os
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth/google", tags=["Google OAuth"])

JWT_SECRET = os.getenv("JWT_SECRET", "secret-key")  # for demo only



# Login to redirect user
@router.get("/login")
async def google_login(request: Request):
    redirect_uri = request.url_for("google_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)


# callback from google
@router.get("/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):

    # Fetch token from Google
    token = await oauth.google.authorize_access_token(request)

    # Get user info
    user_info = token.get("userinfo")
    if user_info is None:
        raise HTTPException(status_code=400, detail="Unable to get user info")

    google_id = user_info["sub"]
    email = user_info.get("email")
    full_name = user_info.get("name")
    avatar_url = user_info.get("picture")

    guest = db.query(Guest).filter(Guest.google_id == google_id).first()

    if not guest:
        guest = Guest(
            google_id=google_id,
            email=email,
            full_name=full_name,
            avater_url=avatar_url,
        )
        db.add(guest)
        db.commit()
        db.refresh(guest)

    token_data = {
        "user_id": guest.id,
        "role": "guest",
        "exp": datetime.utcnow() + timedelta(hours=24)
    }

    jwt_token = jwt.encode(token_data, JWT_SECRET, algorithm="HS256")

    return {
        "guest": GuestDisplay.from_orm(guest),
        "access_token": jwt_token
    }
