from fastapi import FastAPI

app = FastAPI(title="SHA API", version="0.1.0")


@app.get("/health")
def health():
    # Endpoint paling sederhana: dipakai deployment & monitoring
    # untuk mengecek apakah server hidup.
    return {"status": "ok"}