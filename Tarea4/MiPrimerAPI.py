from fastapi import FastAPI
app = FastAPI()

@app.get("/MiPrimerAPI")
def hola(name: str):
    return ("Hola " + name + "!")