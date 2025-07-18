document.getElementById("formulario").addEventListener("submit", async (e) => {
    e.preventDefault();

    // Capturar valores
    const Distancia = parseFloat(document.getElementById("Distancia").value);
    const TeamStartingEquipmentValue = parseFloat(document.getElementById("TeamStartingEquipmentValue").value);
    const RoundStartingEquipmentValue = parseFloat(document.getElementById("RoundStartingEquipmentValue").value);
    const Granadas = parseInt(document.getElementById("Granadas").value);
    const Participacion_Kills = parseFloat(document.getElementById("Participacion_Kills").value);

    const datosRegresion = {
        Distancia,
        TeamStartingEquipmentValue,
        RoundStartingEquipmentValue,
        Granadas,
        Participacion_Kills
    };

    const datosClasificacion = {
        Distancia,
        TeamStartingEquipmentValue,
        RoundStartingEquipmentValue,
        Granadas
    };

    try {
        const resTiempo = await fetch("/predecir-tiempo", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(datosRegresion)
        });

        const resSobrevive = await fetch("/predecir-sobrevive", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(datosClasificacion)
        });

        const dataTiempo = await resTiempo.json();
        const dataSobrevive = await resSobrevive.json();

        document.getElementById("resultado-tiempo").textContent = `${dataTiempo.tiempo_estimado} segundos`;
        document.getElementById("resultado-sobrevive").textContent = `${dataSobrevive.interpretacion}`;
    } catch (error) {
        console.error("Error en la predicción:", error);
        document.getElementById("resultado-tiempo").textContent = `Error`;
        document.getElementById("resultado-sobrevive").textContent = `Error`;
    }
});
