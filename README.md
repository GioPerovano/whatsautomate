# WhatsApp Message Sender 📲

Este script Python permite o envio automático de mensagens para uma lista de números via WhatsApp Web, utilizando as bibliotecas `pywhatkit` e `pyautogui`.

## 📌 Funcionalidades
- Formata os números de telefone automaticamente para o padrão `+55` (Brasil).
- Abre o WhatsApp Web e envia a mensagem sem necessidade de interação manual.
- Fecha a aba após o envio para evitar múltiplas abas abertas.
- Simula o pressionamento da tecla `Enter` para enviar a mensagem.

## 🚀 Requisitos
Antes de rodar o script, certifique-se de ter instalado:

- Python 3+
- As bibliotecas necessárias:
  ```sh
  pip install pywhatkit pyautogui
  ```

## 🔧 Como Usar
1. **Edite a lista de números** no código, colocando os contatos desejados.
2. **Modifique a mensagem** conforme necessário.
3. **Mantenha o WhatsApp Web logado** no navegador para o envio funcionar corretamente.
4. **Execute o script**:
   ```sh
   python whats.py
   ```

## ⚠️ Observações
- O WhatsApp pode bloquear o envio de mensagens automáticas caso detecte spam.
- O intervalo entre os envios pode ser ajustado para evitar restrições.
- O script só funciona com o WhatsApp Web ativo.

### Contribuições são bem-vindas! ✨

