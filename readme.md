markdown.markdown(some_text, extensions=['fenced_code'])

# Variáveis e tipos

    x = 5
    print(type(x))

    x = "Olá"
    print(type(x))

    x = "11"
    y = 1
    z = x + y 

# adquirindo dados

    resposta = input("Digite seu nome:") or "Wanderson"
    print(resposta)

    nome = "Wanderson rigo"
    print(nome)

    sobrenome = "Rigo"
    print("Meu nome completo é",nome,sobrenome,",entendeu?")

# Tamanho do nome

    tamanhoNome = (len(nome))
    print("Meu nome tem",tamanhoNome,"letras")

    tamanhoSobrenome = (len(sobrenome))
    print("Meu sobrenome tem",tamanhoSobrenome,"letras")

# Criando função com parâmetros
    def contar_letras(nome, sobrenome):
        qtd_nome = len(nome)
        qtd_sobrenome = len(sobrenome)    
        return qtd_nome, qtd_sobrenome 

# Exemplo de uso da função
    nome = input("Digite o seu nome: ")
    sobrenome = input("Digite o seu sobrenome: ")
    resposta = contar_letras(nome, sobrenome)
    print(resposta)

# Desestruturação de tupla

    qtd_letras_nome, qtd_letras_sobrenome = resposta

    print(f"O nome '{nome}' tem {qtd_letras_nome} letras.")

    print(f"O sobrenome '{sobrenome}' tem {qtd_letras_sobrenome} letras.")

# Usando interfaces gráficas

    import pymsgbox

    pymsgbox.alert('Este é um alerta!', 'Título do Alerta')

    confirmarResposta = pymsgbox.confirm('Está certo disso?',
                                        'Confirme', 
                                        ['Sim', 'Não', 'Talvez'])
    print(confirmarResposta)

    nomeResposta = pymsgbox.prompt('Qual o seu nome?')
    print(nomeResposta)

    nomePadraoResposta = pymsgbox.prompt('Qual o seu nome?', default='Fulano')
    print(nomePadraoResposta)

    senha = pymsgbox.password(text='Diga a senha', title='Senha', mask='*')
    print(senha)

# Estrutura de dados Dicionário

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

# Iterando sobre os dados do Dicionário

    for usuario in usuarios:
        print(usuario)

    for usuario, dados in usuarios.items():
        email = dados["email"]
        senha = dados["senha"]
        print(f"Usuário: {usuario}, Email: {email}, Senha: {senha}")
    
# Selecionando dados

    if senha == "123":
        print(f"Usuário: {usuario} autorizado")
    else    
        print("Senha errada")

# Para saber mais

Crie um programa com interface gráfica. 

Sugestão 01: usar a biblioteca tkinter

Sugestão 02: Ver tutorial “Tkinter: Interfaces gráficas em Python”

https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956 

4) Sugestão 03: ferramenta gráfica em https://visualtk.com 
