# Importação das bibliotecas
import tkinter as tk
from textblob import TextBlob
from googletrans import Translator

# Função para traduzir o texto do português para o inglês
def traduzir_texto(texto, src_lang='pt', dest_lang='en'):
    tradutor = Translator()
    traducao = tradutor.translate(texto, src=src_lang, dest=dest_lang)
    return traducao.text

# Função que chama a biblioteca textblob para identificar o sentimento da frase
def analisar_sentimento():
    texto = entrada.get("1.0", tk.END)
    texto_traduzido = traduzir_texto(texto)
    analise = TextBlob(texto_traduzido)
    sentimento = analise.sentiment.polarity

    if sentimento > 0:
        resultado.config(text="Sentimento: Positivo")
    elif sentimento < 0:
        resultado.config(text="Sentimento: Negativo")
    else:
        resultado.config(text="Sentimento: Neutro")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Analisador de Sentimentos")

# Elementos da interface
entrada = tk.Text(janela, height=10, width=50)
entrada.pack()

botao = tk.Button(janela, text="Analisar Sentimento", command=analisar_sentimento)
botao.pack()

resultado = tk.Label(janela, text="", font=("Helvetica", 14))
resultado.pack()

janela.mainloop()
