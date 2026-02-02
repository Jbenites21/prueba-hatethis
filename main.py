from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Hola! Esta API está viva en la nube 🚀", "tecnologia": "FastAPI"}

@app.get("/usuarios")
def obtener_usuarios():
    # Aquí simulamos la seguridad que le vas a vender
    return [{"id": 1, "nombre": "Cliente Seguro", "email": "protegido@email.com"}]