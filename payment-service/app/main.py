from fastapi import FastAPI

app = FastAPI(title="Payment Service")

@app.get("/")
def health():
    return {"status": "Payment service is running 🚀"}
