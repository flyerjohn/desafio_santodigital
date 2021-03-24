# desafio_santodigital
Este repositório está destinado à documentação e desenvolvimento do desafio proposto pela SantoDigital.

# Rodar o programa localmente
Para fazer o código funcionar, é preciso ter certeza de que os módulos Flask, Flask-Restful estejam instalados em seu path.
Caso não estejam, faça:

```bash
pip install -U Flask
```

e depois: 

```bash
pip install flask-restful
```

Feito isso, navegue até o diretório em que o arquivo **api.py** esteja presente e rode o seguinte comando no terminal:

```bash
python api.py
```

O localhost já deve estar funcionando, a essa altura, e, para que você receba o resultado do programa, envie uma requisição POST, via Postman, Insomnia ou qualquer outra forma que desejar, contendo o JSON gerado pela Google Vision API, para a rota: http://localhost:5000/postjson.

O comportamento esperado do código é retornar o JSON requisitado pelo desafio, e printar as informações no terminal.

## Observações
O estilo de nota fiscal utilizado para realizar a solução desse desafio foi o da nota fiscal de São Paulo.