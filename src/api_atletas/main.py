from fastapi import FastAPI
from uvicorn import run

app = FastAPI(title="API Atletas",
    description="API para gerenciamento de atletas",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000, reload=True, workers=1)