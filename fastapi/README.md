uvicorn main:app --reload

docker build . -t fastapi
docker run -p 8000:8000 -d fastapi
