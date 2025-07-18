from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from fastapi.staticfiles import StaticFiles

# ==== Cargar modelos ====
modelo_regresion = joblib.load("modelo_arbol_ultra_plus.pkl")
modelo_clasificacion = joblib.load("modelo_clasificacion_rf.pkl")

# ==== Inicializar app ====
app = FastAPI(
    title="API de Predicciones CSGO",
    description="🎯 API para predecir el tiempo de supervivencia y clasificación de jugadores en CS:GO usando modelos de ML.",
    version="1.0.0",
    docs_url="/api"
)

# ==== Montar frontend en /app ====
app.mount("/app", StaticFiles(directory="static", html=True), name="static")

# ==== Entrada completa para el modelo de regresión ====
class DatosEntradaRegresion(BaseModel):
    Distancia: float
    TeamStartingEquipmentValue: float
    RoundStartingEquipmentValue: float
    Granadas: int
    Participacion_Kills: float

# ==== Entrada reducida para el modelo de clasificación ====
class DatosEntradaClasificacion(BaseModel):
    Distancia: float
    TeamStartingEquipmentValue: float
    RoundStartingEquipmentValue: float
    Granadas: int

# ==== Ruta para predecir tiempo ====
@app.post("/predecir-tiempo", summary="Predecir Tiempo de Sobrevivencia (Regresión)")
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

# ==== Ruta para predecir si sobrevive ====
@app.post("/predecir-sobrevive", summary="Predecir si Sobrevive más de 70s (Clasificación)")
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
