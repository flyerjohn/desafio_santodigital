from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__) #criar o app utilizando o flask
api = Api(app) #utilizar a api, para obter algumas facilidades do rest api

class Hello(Resource): #classe inicial do projeto
    def get(self, name):
        return {"Hello":name}

api.add_resource(Hello, '/hello/<name>')

@app.route('/postjson', methods = ['POST']) # adicionar rota para receber o json
def jsonJHandler():
    print(request.is_json) # retorna true se o texto recebido é um json
    content = request.get_json() # transforma o json recebido em um dicionario
    textAnnotations = {}
    textAnnotations = content['textAnnotations'] # buscar a parte do json que possui as anotações de texto
    

    count = 0 # descobrir o indice dos valores desejados na lista

    for data in textAnnotations: #buscar pela nfe 
        if data['description'] == 'Nota':
            print("Nota encontrada")
            break
        count += 1
    print(textAnnotations[count+1]['description'])
    nfe = textAnnotations[count+1]['description']
    count = 0 # zerar contador para proxima busca
    for data in textAnnotations: #buscar pelo codigo de verificacao 
        if data['description'] == 'Verificação':
            print("Codigo encontrado")
            break
        count += 1
    
    codigo = textAnnotations[count+2]['description']
    codigo += textAnnotations[count+3]['description'] # devido ao formato de nota de SP, o cod de verificação fica dividido por duas descrpitions
    print(codigo)
    count = 0 # zerar contador para proxima busca
    for data in textAnnotations: #buscar pelo valor da nota 
        if data['description'] == '$':
            print("Valor encontrado")
            break
        count += 1
    print(textAnnotations[count+1]['description'])
    valor = textAnnotations[count+1]['description']
   
    return {"NFe" : nfe, "Código de Verificação" : codigo, "Valor Total" : valor}

if __name__ == '__main__':
    app.run(debug=True)

