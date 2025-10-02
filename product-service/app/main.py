from fastapi import FastAPI

app = FastAPI(title="Product Service")

@app.get("/")
def health():
    return {"status": "Product service is running 🚀"}
