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