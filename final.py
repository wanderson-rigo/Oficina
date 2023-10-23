import pymsgbox

usuarios = {
    "Fulano": "123",
    "Beltrano": "345",
    "Ciclano": "678"
}

def cadastrar_usuario():
    nome = pymsgbox.prompt("Digite o nome de usuário: ")
    senha = pymsgbox.prompt("Digite a senha: ")
    usuarios[nome] = senha
    pymsgbox.alert("Usuário cadastrado com sucesso!")
    pymsgbox.alert(usuarios)

def recuperar_senha():
    nome = pymsgbox.prompt("Digite o nome de usuário para recuperar a senha: ")
    if nome in usuarios:
        pymsgbox.alert(f"A senha de {nome} é {usuarios[nome]}")
    else:
        pymsgbox.alert("Usuário não existe.")

def main():
    nome = pymsgbox.prompt("Diga o nome de usuário: ")
    senha = pymsgbox.prompt(nome, "digite a sua senha: ")

    if senha == "1234":
         pymsgbox.alert("Acertou!")       
    else:
        pymsgbox.alert("Usuário ou senha inválidos.")

        opcao = pymsgbox.confirm("Escolha uma opção:", 
                                 "Confirme",
                                 ["Cadastrar Novo Usuário", "Recuperar Senha", "Sair"])
        if opcao == "Cadastrar Novo Usuário":
            cadastrar_usuario()
        elif opcao == "Recuperar Senha":
            recuperar_senha()

if __name__ == "__main__":
    main()
