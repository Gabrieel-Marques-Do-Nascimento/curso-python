nome = str(input('Qual seu nome: '))
if nome == 'gabriel':
    print('que nome bonito')
elif nome == 'pedro' or nome == 'camila' or nome == 'joao':
    print('seu nome e bem popular no Brasil')
elif nome in 'ana julia jessica  maria':
    print(f'Belo nome feminino')
else: # else e opcinal
    print('que nome e bem comum')
print(f'um bom dia {nome.capitalize()}')