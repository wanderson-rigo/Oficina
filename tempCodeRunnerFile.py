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

#itere sobre o dicionario
for usuario in usuarios:
    print(usuario)

for usuario, dados in usuarios.items():
    email = dados["email"]
    senha = dados["senha"]
    print(f"Usuário: {usuario}, Email: {email}, Senha: {senha}")