##### Estrutura Workshop

Não deixar o próprio Python fazer a própria gestão de suas versões, para isso utilizamos do Pyenv, e qual a utilidade dela?

Enganar a máquina, setando um caminho especifico para ser utilizado com uma máquina virtual ou ambiente virtual, mudando o endereço/path pela váriavel de ambiente

- pyenv local ou global

- pyenv init

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"


poetry cria esse ambiente virtual

import site 
print(site.getsitepackages())
- Verificar minha versão(cd caminho da pasta e se der um ls vou ver tudo dessa versão do python, tudo que eu intalo NÃO utilizando uma máquina virtual vai para o sit packages)

poetry config virtualenvs.in-project true 
- Sempre usar esse primeiro comando sempre que cria pq ele cria o ambiente virtual

- poetry init
(
Package name [workshop]:  
Version [0.1.0]:  
Description []:  Projeto workshop
Author [None, n to skip]:  Moisés 
License []:  MIT
Compatible Python versions [^3.8]:  3.11.3

Would you like to define your main dependencies interactively? (yes/no) [yes] NO
Would you like to define your development dependencies interactively? (yes/no) [yes] no
)

Após isso tentar o comando
- poetry shell
Caso não dê certo clicar em CTRL + SHIFT + P, python: select interpreter e colocar a versão desejada

Se mesmo assim sua versão do python ainda for outra, como o erro abaixo(colocar imagem) use o seguinte comando para transformar esta versão para sua versão oficial python 

export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"

Agora sim tente (imagem 2) 
- poetry shell

Estou dentro do ambiente virtual agora (imagem 3) se eu rodar este mesmo código
- import site 
print(site.getsitepackages())
ele vai jogar para o meu site packages do  eu ambiente virtual, uma estrutura de pastas guardada para este projeto

Instalando bibliotecas(Caso parecido com o PIP)
- poetry add pandas
Realiza a instalação do pandas, atualiza o env e atualiza o pyproject.toml, quando uma pessoa for rodar este projeto irá utilizar as mesmas versões

Váriavel de ambiente path, o resultado(imagem4) é a ordem que o python tem para utilizar as bibliotecas
- import sys
 for path in sys.path:
    print(path)

Abrir uma pasta escondida git (imagem5)
- git init
Criar uma pasta chamada .vscode
Criar um arquivo settings.json dentro da pasta e colocar o comando abaixo
- {
    "files.exclude": {
        "**/.git": false
    
    }
}

criar um arquivo .gitignore fora de qualquer pasta colocar os arquivos que eu não quero que ele pegue(qualquer coisa existe o site toptal e pegar um compilado de .gitignore python)

Acessando Git e fazendo versionamento
Criando um arquivo README
- touch README.md
- git add README.md
- git branch -M main
- git push -u origin main

Cada arquivo que está com U não foi versionado(imagem 6), boas práticas é colocar 1 de cada vez para ir gerando o histórico
- git add .gitignore .python-version pyproject.toml
- git commit -m "Adicionando a estrutura do projeto"
- git push

Criar uma pasta aparte de desenvolvimento app ou src
- pasta pipeline dentro da src
- Dentro da pipeline extract.py
- dentro da src main.py

criar a pasta data, e colocar a pasta input

Quebrar a ETL em 3 momentos

o que é o if __name__ == "__main__"
- É um pacote em python que permite ser importado para outro local para serem trabalhados em conjunto, onde só irá rodar quando realmente for necessário

no meu main criar o pacote de extração do Extract

- git add app/
- git add data/
- git add pyproject.toml
- git commit -m "extract funcionando"
- git push 

trocando branch
- git branch transform
- git checkout transform

Criar um arquivo transform.py dentro de pipeline

Criar uma pasta aparte tests e criar um arquivo dentro chamado test_pipeline.py
- poetry add pytest
esse é o padrão dos testes https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/

exemplo de teste que ele forneceu

def testar_a_concatenacao_da_lista_de_df():
    arrange = 3

    act = 3

    assert arrange == act

    
parei no 2:39:35