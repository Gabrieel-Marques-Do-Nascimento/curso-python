Para criar uma API simples sem depender de módulos externos, você pode usar o módulo embutido http.server do Python. Esse módulo oferece funcionalidade básica de servidor HTTP, que pode ser usada para criar uma API simples. No entanto, ele não tem recursos avançados como o Flask, mas pode servir bem para casos básicos.

Aqui está um exemplo de como você pode criar uma API sem bibliotecas externas, utilizando apenas o Python padrão.

1. Criando o Servidor API (sem módulos externos)

Módulo: simple_api.py

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Definindo os dados a serem retornados
def get_user_data():
    return {
        "id": 1,
        "nome": "João Silva",
        "email": "joao.silva@example.com"
    }

# Manipulador de requisições HTTP
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Verifica se a rota solicitada é "/api/v1/usuario"
        if self.path == '/api/v1/usuario':
            # Configura o cabeçalho da resposta (código 200 e tipo JSON)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            # Converte os dados do usuário em JSON e envia na resposta
            dados = get_user_data()
            self.wfile.write(json.dumps(dados).encode('utf-8'))
        else:
            # Caso a rota não seja encontrada, retorna um erro 404
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Recurso nao encontrado')

# Função para iniciar o servidor
def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor rodando na porta {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

2. Como funciona:

BaseHTTPRequestHandler: É a classe do Python que lida com as requisições HTTP. Nós estendemos essa classe e sobrescrevemos o método do_GET() para manipular as requisições GET.

get_user_data(): Esta função retorna os dados do usuário como um dicionário Python.

Verificação da rota: Dentro do método do_GET(), verificamos se a rota solicitada é /api/v1/usuario. Se for, retornamos os dados do usuário no formato JSON. Caso contrário, retornamos um erro 404.

Servidor: O servidor HTTP é iniciado na função run(), rodando na porta 8000.


3. Consumindo a API com urllib (sem módulos externos)

Agora, podemos criar um cliente que consuma a API usando o módulo embutido urllib para fazer uma requisição HTTP.

Módulo: client.py

import urllib.request
import json

def obter_dados_usuario():
    url = 'http://127.0.0.1:8000/api/v1/usuario'

    try:
        # Faz a requisição GET
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                # Lê e decodifica a resposta
                dados = response.read().decode('utf-8')
                # Converte a resposta JSON em dicionário Python
                return json.loads(dados)
            else:
                print(f"Erro ao obter dados: {response.status}")
                return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

# Testando o cliente
if __name__ == '__main__':
    usuario = obter_dados_usuario()
    if usuario:
        print(f"Usuário: {usuario['nome']}, Email: {usuario['email']}")

4. Executando o exemplo:

1. Inicie o servidor API executando o módulo simple_api.py:

python simple_api.py

Isso iniciará o servidor HTTP na porta 8000.


2. Execute o cliente (client.py) para consumir os dados:

python client.py

Se tudo estiver funcionando corretamente, o cliente irá fazer a requisição à API e imprimir o nome e o email do usuário.



5. Como funciona o cliente:

urllib.request.urlopen(): Esta função realiza uma requisição HTTP e retorna a resposta.

json.loads(): Converte o conteúdo JSON da resposta em um dicionário Python.


Resumo:

Este exemplo mostra como criar uma API em Python usando apenas bibliotecas padrão (sem bibliotecas externas como Flask). A API serve dados de um módulo e o cliente consome esses dados usando o módulo embutido urllib.

