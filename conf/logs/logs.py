import sys
import traceback
import requests
import datetime

LOG_FILE = "log.log"

def format_error_message(exception_type, exception_value, exception_traceback):
    formatted_message = "🔓 **Erro LIBinsta**\n\n"
    formatted_message += f"**Tipo de exceção:** {exception_type}\n"
    formatted_message += f"**Valor da exceção:** {exception_value}\n"
    formatted_message += "**Traceback:**\n"
    formatted_message += f"```\n{exception_traceback}\n```"
    return formatted_message

def send_message(webhook_url, message):
    try:
        payload = {
            "embeds": [
                {
                    "description": message,
                    "color": 0xFF0066
                }
            ]
        }
        requests.post(webhook_url, json=payload)
    except requests.RequestException as e:
        print(f"Desculpe, não foi possível enviar a mensagem. Erro: {e}")

def log_to_file(log_message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {log_message}\n"
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)

if __name__ == "__main__":
    # Redefinindo o hook de exceção para enviar mensagens e também registrar no arquivo de log
    def exception_hook(exctype, value, tb):
        error_message = format_error_message(exctype.__name__, str(value), "".join(traceback.format_tb(tb)))
        send_message(
            "https://discord.com/api/webhooks/1204891971748106250/sTcUux4b7nXO0q2dcp0_j3z5UiuDzaoZtM7-u1m7JMj4-HcfNPzKseDP_n0nuOkG15wN",
            error_message
        )
        log_to_file(error_message)

    sys.excepthook = exception_hook
