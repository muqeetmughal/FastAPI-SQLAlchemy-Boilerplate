from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from apps.auth.dependencies import get_current_user
from database import engine, init_db
# from routers import auth, access, corporate
from apps.auth.views import auth
from apps.access.views import access
import time

app = FastAPI(
    title="Fast API Boilerplate Project",
    description="This project is the Boilerplate that includes Authentication and Authorization",

)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# init_db()

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):

#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response



app.include_router(auth,
                   prefix="/auth",
                   tags=["Authentication"]
                   )
app.include_router(access,
                   prefix="/access",
                   tags=["Roles and Permissions"],
                   )
# app.include_router(corporate.router,
#                    prefix="/corporate",
#                    tags=["Corporate Accounts"]
#                    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
