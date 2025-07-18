from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.staticfiles import StaticFiles

# ==== Cargar modelos desde carpeta 'models' ====
modelo_regresion = joblib.load("models/modelo_arbol_ultra_plus.pkl")
modelo_clasificacion = joblib.load("models/modelo_clasificacion_rf.pkl")

# ==== Inicializar app con custom info ====
app = FastAPI(
    title="API de Predicciones CSGO",
    description="🎯 API para predecir el tiempo de supervivencia y clasificación de jugadores en CS:GO usando modelos de ML.",
    version="1.0.0",
    docs_url="/api"
)

# ==== Montar frontend estático en /app (¡NO en "/") ====
app.mount("/app", StaticFiles(directory="static", html=True), name="static")

# ==== Entrada para regresión ====
class DatosEntradaRegresion(BaseModel):
    Distancia: float
    TeamStartingEquipmentValue: float
    RoundStartingEquipmentValue: float
    Granadas: int
    Participacion_Kills: float

# ==== Entrada para clasificación ====
class DatosEntradaClasificacion(BaseModel):
    Distancia: float
    TeamStartingEquipmentValue: float
    RoundStartingEquipmentValue: float
    Granadas: int

# ==== Endpoint de regresión ====
@app.post("/predecir-tiempo")
def predecir_tiempo(datos: DatosEntradaRegresion):
    entrada = np.array([[ 
        datos.Distancia,
        datos.TeamStartingEquipmentValue,
        datos.RoundStartingEquipmentValue,
        datos.Granadas,
        datos.Participacion_Kills
    ]])
    prediccion = modelo_regresion.predict(entrada)[0]
    return {
        "tiempo_estimado": round(prediccion, 2),
        "unidad": "segundos"
    }

# ==== Endpoint de clasificación ====
@app.post("/predecir-sobrevive")
def predecir_sobrevive(datos: DatosEntradaClasificacion):
    entrada = np.array([[ 
        datos.Distancia,
        datos.TeamStartingEquipmentValue,
        datos.RoundStartingEquipmentValue,
        datos.Granadas
    ]])
    prediccion = modelo_clasificacion.predict(entrada)[0]
    return {
        "sobrevive_70s": bool(prediccion),
        "interpretacion": "🟢 Sobrevive más de 70 segundos" if prediccion else "🔴 Muere antes de 70 segundos"
    }
