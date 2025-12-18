# compresion-videos-ffmpeg

## 📌 Estado del proyecto
🟡 **PENDIENTE / ARCHIVADO TEMPORALMENTE**

Este repositorio contiene un intento de implementar un microservicio de compresión de video (FFmpeg + Flask) desplegado en Railway.

El desarrollo se **detiene temporalmente** debido a conflictos persistentes entre:
- la imagen base `jrottenberg/ffmpeg`
- el manejo de `ENTRYPOINT / CMD`
- y el sistema de despliegue de Railway

El problema **no es de lógica ni de código**, sino de **infraestructura / plataforma**.

---

## 🎯 Objetivo original
Crear un servicio HTTP que:
- reciba un video vía POST
- lo comprima con FFmpeg a < 50 MB
- devuelva el archivo optimizado
- sea consumido por Make / Telegram / Meta-Agente

---

## ⚠️ Motivo de la pausa
- Railway ejecuta repetidamente el ENTRYPOINT de FFmpeg
- El contenedor nunca llega a ejecutar Flask
- El tiempo invertido adicional no es rentable en este momento

👉 Se decide **pausar conscientemente** para priorizar el avance del sistema principal.

---

## 🧠 Estado técnico
- Código: funcional a nivel local
- Arquitectura: válida
- Blo
