import pywhatkit as kit
import pandas as pd
import pyautogui
import time

# Carregar números de telefone do arquivo CSV
df = pd.read_csv('numero.csv')  # Substitua 'numero.csv' pelo nome do seu arquivo

# Mensagem a ser enviada
mensagem = "Bom dia, \nMeu nome é Yuri Rangel, sou engenheiro da computação especializado em computação forense. Estou entrando em contato para me apresentar como auxiliar judiciário e consultor forense, oferecendo meus serviços para auxiliar em casos que demandem expertise técnica na análise de evidências digitais.\nEsta mensagem foi gerada automaticamente, e os dados de contato foram coletados em conformidade com a legislação vigente.\nEstou à disposição para discutir como posso contribuir para o sucesso dos seus casos.\nAtenciosamente,"
imagem = "img.jpg"  # Substitua pelo caminho da imagem

# Função para enviar a mensagem e a imagem via WhatsApp
def enviar_mensagem(numero, mensagem, imagem):
    try:
        # Enviar a imagem (o próprio pywhatkit já envia uma mensagem junto com a imagem)
        kit.sendwhats_image(f"+{numero}", imagem, mensagem)
        time.sleep(10)  # Aguarda para garantir que a imagem foi enviada

        # Automatizar o clique no botão "Enviar"
        pyautogui.press('enter')
        time.sleep(2)  # Aguarda para garantir que a mensagem foi enviada

        # Fechar a aba do navegador
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(2)  # Pequena pausa para garantir que a aba foi fechada

        print(f"Mensagem e imagem enviadas e aba fechada para: {numero}")
    except Exception as e:
        print(f"Falha ao enviar para {numero}: {e}")

# Loop através dos números e enviar a mensagem e imagem
for index, row in df.iterrows():
    numero = row['numero']  # Certifique-se de que a coluna esteja nomeada como 'numero'
    enviar_mensagem(numero, mensagem, imagem)
    time.sleep(10)  # Intervalo entre as mensagens para evitar bloqueios

print("Todas as mensagens foram enviadas e as abas foram fechadas!")
