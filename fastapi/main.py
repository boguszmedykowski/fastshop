from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "siemka"}


@app.get("/products")
async def products():
    return {"results": {"name": "paprotka"}}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
