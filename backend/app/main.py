from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SHA API", version="0.1.0")

# CORS: browser hanya mengizinkan frontend memanggil backend
# kalau backend secara eksplisit mengizinkan origin frontend tersebut.
# Jangan pakai "*" di production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    # Endpoint paling sederhana: dipakai deployment & monitoring
    # untuk mengecek apakah server hidup.
    return {"status": "ok"}