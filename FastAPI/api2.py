from fastapi import FastAPI
import pandas as pd

iesazarquiel = FastAPI()
datos = pd.read_csv("uno.csv")

@iesazarquiel.get("/info-alumnos")
def info():
    listaIds = datos["ID"].tolist()
    return {"IDs disponibles ": listaIds}

@iesazarquiel.get("/asistencia")
def asistencia(id: int):
    alumno = datos.loc[id]
    return {
        "Nombre: ": alumno["Nombre"],
        "Apellidos: ": alumno["Apellidos"],
        "Porcentaje de asistencia: ": f"{alumno["Asistencia"]}%"
    }

@iesazarquiel.get("/notas")
def notas(id: int, nota: str):
    alumno = datos.loc[id]
    if nota not in datos.columns:
        return {
            "error": f"La nota '{nota}' no existe."
        }
    return {
        "Nombre: ": alumno["Nombre"],
        "Apellidos: ": alumno["Apellidos"],
        "Categoría: ": nota,
        "Calificación: ": alumno[nota]
    }