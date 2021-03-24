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
    textAnnotations = content["textAnnotations"] # buscar a parte do json que possui as anotações de texto
    
    print(textAnnotations[]) # acessando e printando um dado do dicionario
    return 'JSON received'

if __name__ == '__main__':
    app.run(debug=True)

