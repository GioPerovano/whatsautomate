import pywhatkit as kit
import pyautogui
import time
import re

# Lista de números desformatados
numeros = ["11000000000", "11000000001"]

# Mensagem a ser enviada
mensagem = """🚀 *Grupy no WhatsApp!* 🐍💬

Se você respondeu ao formulário, *bem-vindo à comissão organizadora dos eventos do Grupy*! 🎉 Este grupo foi criado para alinharmos as demandas e organizarmos encontros incríveis para a comunidade Python.

🔗 *Entre agora e participe!*
https://chat.whatsapp.com/GMh2TMDHtM9ASnEn1JyUz4

Vamos juntos fortalecer o Grupy! 💙💛."""

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
