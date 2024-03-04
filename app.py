import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)

def formatData(Dataframe):
  # Carrega a planilha Excel
    df = Dataframe
    # Inicializa a estrutura do dicionário
    result = {
        "name": "Produtos",
        "children": []
    }

    # Agrupa os dados por categoria
    grouped = df.groupby('categoria')

    # Itera sobre cada grupo, criando a estrutura desejada
    for category, group in grouped:
        category_dict = {
            "name": category,
            "children": []
        }
        for _, row in group.iterrows():
            category_dict["children"].append({
                "name": row['produto'],
                "value": row['volume']
            })
        result["children"].append(category_dict)

    # Converte o dicionário em uma string JSON
    json_result = json.dumps(result, ensure_ascii=False, indent=2)

    # Para visualizar o resultado
    return (json_result)
   
def spreadsheetConnect(filename, credentials, sheetIndex):
  # Definir o escopo de acesso
  scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

  # Carregar as credenciais a partir do arquivo JSON que você baixou do Google Cloud Console
  creds = ServiceAccountCredentials.from_json_keyfile_name(credentials, scope)

  # Autenticar com o Google Sheets e o Google Drive
  client = gspread.authorize(creds)

  # Abrir a planilha pelo nome
  spreadsheet = client.open(filename)

  # carrega os dados da página especificada pelo seu índice na planilha
  if spreadsheet:
    sheet = spreadsheet.get_worksheet(sheetIndex)
    return sheet
  else:
    print("Erro ao conectar a planilha")
    return None

@app.route("/", methods=['POST', 'GET'])
def index():

  return jsonify("Hello backend")

@app.route("/getnodeschartdata", methods=['POST', 'GET'])
def getnodeschartdata():
  #get the Links values
  graphSheet = spreadsheetConnect("Black-Friday 2022 Grafo Dados",'credentials2.json',1)
  sheetData = graphSheet.get_all_records()
  df = pd.DataFrame(sheetData)
  links = df.to_dict('records')
  
  #get the Node values
  graphSheet = spreadsheetConnect("Black-Friday 2022 Grafo Dados",'credentials2.json',0)
  sheetData = graphSheet.get_all_records()
  df = pd.DataFrame(sheetData)
  nodes = df.to_dict('records')

  response = {
        "links": links,
        "nodes": nodes
    }
  

  return jsonify(response)


@app.route("/getchartdata", methods=['POST', 'GET'])
def getChartData():
   sheet = spreadsheetConnect("Python Conn",'credentials.json',0 )
   sheetData = sheet.get_all_records()
   df = pd.DataFrame(sheetData)
   formated_json = formatData(df)
   
   return formated_json

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

