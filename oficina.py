nome = "Wanderson rigo"
print(nome)

sobrenome = "Rigo"
print("Meu nome completo é",nome,sobrenome,",entendeu?")

#letras em nome
tamanhoNome = (len(nome))
print("Meu nome tem",tamanhoNome,"letras")

tamanhoSobrenome = (len(sobrenome))
print("Meu sobrenome tem",tamanhoSobrenome,"letras")

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