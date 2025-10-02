from fastapi import FastAPI

app = FastAPI(title="Gateway Service")

@app.get("/")
def health():
    return {"status": "Gateway service is running 🚀"}
