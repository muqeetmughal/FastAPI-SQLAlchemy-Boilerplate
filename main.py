from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from database import engine, init_db
# from routers import auth, access, corporate
from apps.auth.views import auth
app = FastAPI(title="Fast API Boilerplate Project", description="This project is the Boilerplate that includes Authentication and Authorization")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# init_db()

app.include_router(auth,
                   prefix="/auth",
                   tags=["Authentication"]
                   )
# app.include_router(access.router,
#                    prefix="/access",
#                    tags=["Roles and Permissions"]
#                    )
# app.include_router(corporate.router,
#                    prefix="/corporate",
#                    tags=["Corporate Accounts"]
#                    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
