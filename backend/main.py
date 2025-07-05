from fastapi import FastAPI
from backend.auth.routes import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
