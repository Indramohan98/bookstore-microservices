from fastapi import FastAPI

app = FastAPI(title="Order Service")

@app.get("/")
def health():
    return {"status": "Order service is running 🚀"}
