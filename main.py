from fastapi import FastAPI

import uvicorn
from database import engine, init_db
# from routers import auth, access, corporate

app = FastAPI()


init_db()

# app.include_router(auth.router,
#                    prefix="/auth",
#                    tags=["Authentication"]
#                    )
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
