## 🧪 Hipótesis del Proyecto

**¿Podemos predecir si un jugador sobrevivirá más de 70 segundos en una ronda?**

Para responder esta pregunta, transformamos la variable `Tiempo` en una variable binaria (`Sobrevive_70`), donde:

- 1: el jugador sobrevivió más de 70 segundos.
- 0: el jugador sobrevivió 70 segundos o menos.

---

## 🔍 Preparación del Dataset

- Se eliminó el valor atípico de 73 segundos en la columna `Tiempo`.
- Se generó la variable objetivo `Sobrevive_70`.
- Se seleccionaron dos conjuntos de variables predictoras:
  - **Conjunto reducido (2 variables):** `Distancia`, `TeamStartingEquipmentValue`.
  - **Conjunto completo (4 variables):** `Distancia`, `Participacion_Kills`, `Granadas`, `TeamStartingEquipmentValue`.

Se dividieron los datos en entrenamiento (80%) y prueba (20%), manteniendo la proporción entre clases.

---

## 🤖 Modelos Implementados

### 1. Regresión Logística
- Modelo lineal probabilístico.
- **Mejor desempeño con 4 variables.**
- F1-score (4 vars): **0.6531**
- ROC AUC (4 vars): **0.71**

---

### 2. K-Nearest Neighbors (KNN)
- Algoritmo basado en la cercanía a los vecinos.
- Se normalizaron los datos antes de entrenar.
- F1-score (4 vars): **0.6531**
- ROC AUC (4 vars): **0.71**

---

### 3. Árbol de Decisión
- Algoritmo que divide recursivamente los datos según reglas de decisión.
- Fácil de interpretar.
- F1-score (4 vars): **0.6829**
- ROC AUC (4 vars): **0.74**

---

### 4. Random Forest
- Conjunto de árboles de decisión para reducir overfitting.
- Uno de los modelos con mejor rendimiento.
- F1-score (4 vars): **0.6866**
- ROC AUC (4 vars): **0.75**

---

### 5. Support Vector Machine (SVM)
- Clasificador basado en maximizar el margen entre clases.
- Usó `decision_function` en vez de `predict_proba` para ROC.
- F1-score (4 vars): **0.6461**
- ROC AUC (4 vars): **0.67**

---

## 🎯 Conclusiones

- **Random Forest con 4 variables** fue el mejor modelo general (F1 = 0.6866, AUC = 0.75).
- Los modelos mejoraron con más variables en todos los casos.
- La variable `TeamStartingEquipmentValue` fue una de las más importantes según el análisis de Feature Importance.
- La curva ROC mostró mejor discriminación con Random Forest y Árbol de Decisión.

