from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import auth, event, registration

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(event.router)
app.include_router(registration.router)

@app.get("/")
def health_check():
    return {"message": "Healthy"}
