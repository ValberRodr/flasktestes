from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_message = request.values.get('Body', '')

    # Crie uma resposta TwiML
    twiml_response = MessagingResponse()

    # Processar a mensagem recebida e gerar uma resposta
    if "Olá" in incoming_message:
        response_message = "Olá! Obrigado por entrar em contato."
    elif "Como você está?" in incoming_message:
        response_message = "Estou bem, obrigado! E você?"
    else:
        response_message = "Desculpe, não entendi. Por favor, envie uma mensagem válida."

    twiml_response.message(response_message)

    return str(twiml_response)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
