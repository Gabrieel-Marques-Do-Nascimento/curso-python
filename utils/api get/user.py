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