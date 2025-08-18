from datetime import datetime

# Diccionario global para mantener estados
usuarios = {}

def procesar_mensaje(numero, mensaje):
    # Si el usuario no existe, lo inicializamos
    if numero not in usuarios:
        usuarios[numero] = {"estado": "inicio"}

    estado = usuarios[numero]["estado"]

    if estado == "inicio":
        respuesta = (
            "👋 ¡Hola! Soy Nano, tu asistente virtual de Ingeniería Mendivil.\n"
            "¿En qué te puedo ayudar?\n"
            "1️⃣ Urgencia\n2️⃣ Presupuesto\n3️⃣ Información\n4️⃣ Otra consulta"
        )
        usuarios[numero]["estado"] = "esperando_opcion"

    elif estado == "esperando_opcion":
        usuarios[numero]["opcion"] = mensaje
        respuesta = "👉 Por favor, decime tu nombre y apellido."
        usuarios[numero]["estado"] = "esperando_nombre"

    elif estado == "esperando_nombre":
        usuarios[numero]["nombre"] = mensaje
        respuesta = "🏠 Ahora indicame tu dirección."
        usuarios[numero]["estado"] = "esperando_direccion"

    elif estado == "esperando_direccion":
        usuarios[numero]["direccion"] = mensaje
        respuesta = "✍️ Contame tu consulta."
        usuarios[numero]["estado"] = "esperando_descripcion"

    elif estado == "esperando_descripcion":
        usuarios[numero]["descripcion"] = mensaje
        respuesta = "✅ ¡Gracias! Hemos recibido tu consulta."
        
        # Guardar en archivo
        with open("consultas.txt", "a", encoding="utf-8") as f:
            f.write(f"--- Consulta recibida {datetime.now()} ---\n")
            for clave, valor in usuarios[numero].items():
                f.write(f"{clave}: {valor}\n")
            f.write("\n")

        usuarios[numero]["estado"] = "finalizado"

    else:
        respuesta = "¿Querés empezar otra vez? Escribí *Hola* para reiniciar."
        usuarios[numero]["estado"] = "inicio"

    return respuesta


# 🔹 Simulación paso a paso
numero = "38855928082"
print(procesar_mensaje(numero, "hola"))        # Va al inicio
print(procesar_mensaje(numero, "Presupuesto")) # Pasa a esperando_nombre
print(procesar_mensaje(numero, "Luis Mogro"))  # Pasa a esperando_direccion
print(procesar_mensaje(numero, "Av. Siempre Viva 123"))  # Pasa a esperando_descripcion
print(procesar_mensaje(numero, "Necesito una instalación eléctrica"))  # Finaliza
