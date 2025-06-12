from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    user_input = None
    response = None

    if request.method == "POST":
        user_input = request.form["user_input"]
        mensaje = user_input.lower()

        # Lógica mejorada del bot
        if "hola" in mensaje:
            response = "¡Hola, pequeña y linda criatura humanoide! ¿Qué te trae por acá?"
        elif "cómo estás" in mensaje or "que tal" in mensaje:
            response = "¡Estoy mejor que nunca! Listo para chatear contigo 💬"
        elif "adiós" in mensaje or "bye" in mensaje:
            response = "¡Hasta pronto! Que tengas un día espectacular 🌟"
        elif "gracias" in mensaje:
            response = "¡De nada! Estoy aquí para ayudarte 🫶"
        elif "no entiendo" in mensaje or "qué dijiste" in mensaje:
            response = "Mmmm, creo que no te entiendo mucho, ¿y si mejor vamos por un café? ☕"
        elif "sexo" in mensaje or "política" in mensaje or "religión" in mensaje:
            response = "Esos son temas que aún no me entrenan para responder, pero espero que tu día vaya de maravilla ✨"
        else:
            response = "Hmm... eso no lo sé aún 🤔 pero estoy aprendiendo más cada día."

    return render_template("index.html", user_input=user_input, response=response)


if __name__ == "__main__":
    app.run(debug=True)
