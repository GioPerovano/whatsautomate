import pywhatkit as kit
import pyautogui
import time
import re

# Lista de números desformatados
numeros = ["11000000000", "11000000001"]

# Mensagem a ser enviada
mensagem = """Olá! Esta é uma mensagem automática via Python."""

# Função para formatar os números corretamente com o código do Brasil (+55)
def formatar_numero(numero):
    numero_limpo = re.sub(r'\D', '', numero)  # Remove tudo que não for número
    if not numero_limpo.startswith("55"):  # Adiciona +55 se necessário
        numero_limpo = "55" + numero_limpo
    return f"+{numero_limpo}"

# Formatar todos os números da lista
numeros_formatados = [formatar_numero(num) for num in numeros]

# Intervalo entre os envios para evitar problemas com o WhatsApp Web

# Loop para enviar a mensagem para cada número
for numero in numeros_formatados:
    try:
        kit.sendwhatmsg_instantly(numero, mensagem, wait_time=10, tab_close=True)  # Fecha a aba automaticamente
        time.sleep(15)  # Tempo para carregar o chat
        pyautogui.press("enter")  # Simula o envio da mensagem
        print(f"Mensagem enviada para {numero}")
        time.sleep(15)  # Tempo antes de enviar para o próximo número
    except Exception as e:
        print(f"Erro ao enviar mensagem para {numero}: {e}")
