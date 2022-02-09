from flask import Flask, jsonify
import pandas as pd

#Inicia aplicação Flask
app = Flask(__name__)

# Construir funcionalidae
@app.route('/')
def homepage():
  return 'A API está no ar'

@app.route('/pegarvendas')
def pegarvendas():
  #tabela = pd.read_csv('advertising.csv')
  #total_vendas = tabela['vendas'].sum()

  resposta = {'total_vendas': 25}
  return jsonify(resposta)

app.run(host='0.0.0.0')

!pip install requests

import requests
link = 'https://primeiraapi.joelmirramos.repl.co/pegarvendas'

requisicao = requests.get(link)
dicionario = requisicao.json()

print(requisicao) #status
print(requisicao.json()) #dicionário
print(dicionario['total_vendas'])
