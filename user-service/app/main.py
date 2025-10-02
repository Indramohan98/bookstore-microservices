from fastapi import FastAPI

app = FastAPI(title="User Service")

@app.get("/")
def health():
    return {"status": "User service is running 🚀"}
