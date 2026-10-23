# SHA

Personal execution assistant: membantu mengubah niat menjadi tindakan lewat task breakdown, prioritas, reminder, dan replanning.

Status: in development.

## Tech stack

- Backend: FastAPI (Python)
- Frontend: Next.js, React, TypeScript, Tailwind CSS
- Database: PostgreSQL

## Menjalankan project (development)

### Prasyarat
Python 3.11+, Node.js 20+, PostgreSQL 16 dengan database `sha_dev`.

### Backend
```
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API: http://localhost:8000, dokumentasi: http://localhost:8000/docs

### Frontend
```
cd frontend
npm install
npm run dev
```
App: http://localhost:3000

### Environment
Salin `.env.example` menjadi `backend/.env`, lalu isi password database.

### Test
```
cd backend
pytest
```