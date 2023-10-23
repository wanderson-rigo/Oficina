# Usuários  tem senha e email 
usuarios = {
"Fulano": {
"senha": "123",
"email": "fulano@nada.com"
},
"Beltrano": { 
"senha": "456",
"email": "beltrano@nada.com"
},
"Sicrano": {
"senha": "789",
"email": "sicrano@nada.com"
}
}

for usuario, dados in usuarios.items():
    senha = dados["senha"]
if senha == "123"    :
        print(f"Usuário: {usuario} autorizado")
    else:
        print("Senha errada")

