from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción, aquí pones la URL de tu frontend. "*" significa "todos".
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"mensaje": "Hola! Esta API está viva en la nube 🚀", "tecnologia": "FastAPI"}

@app.get("/usuarios")
def obtener_usuarios():
    # Aquí simulamos la seguridad que le vas a vender
    return [{"id": 1, "nombre": "Cliente Seguro", "email": "protegido@email.com"}]