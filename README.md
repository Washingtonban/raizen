# Avaliação Técnica Backend Python

## Descrição
Elaborar uma aplicação de backend utilizando a linguagem de programação Python que deverá conter uma API retornando os dados da previsão do tempo dos próximos dias. Para elaborar essa aplicação, utilizar a API de previsão do tempo de 5 dias do [OpenWeatherMap](https://openweathermap.org/). Será necessário criar uma conta e subscrever para utilizar a API, porém é possível fazê-lo de forma gratuita. Salvar o histórico de chamadas para consulta posterior. A aplicação resultante deverá ser enviada ao seu GitHub em um repositório público, encaminhando o link ao time de recrutamento.

## Requisitos
- **Linguagem de programação:** Python;
- **Banco de Dados:** Poderá utilizar seu banco de dados à seu gosto, mas dê preferência para bancos não relacionais, como MongoDB;
- **Bibliotecas e Frameworks:** Utilizar quaisquer bibliotecas e frameworks à seu gosto (requests, flask, django, pymongo, etc), porém a chamada da API deve ser feita diretamente;
- **Documentação:** Elaborar um README com, no mínimo, as instruções referentes à subir o ambiente da sua aplicação;
- **Bônus:** Envie para o repositório quaisquer artefatos que tenha utilizado para implementar essa aplicação (collections do postman, testes unitários, etc).

## Ambiente do projeto

### .env

Existe um arquivo com o exemplo de como vc deve fazer o seu arquivo .env, o arquivo é o env.example

### Pyenv

O pyenv é um versionador de Python, é uma etapa opcional, mas muito recomendada para quem sua MacOs.

1. Instale o Homebrew
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

2. Instale o pyenv
```bash
brew install pyenv
```

3. Adicione pyenv init ao seu shell para habilitar o shims e autocompletion. Adicione ao seu arquivo ~/.zshrc:
```bash
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

```
4. Reinicie seu terminal.

#### Usando o Pyenv

1. Após a instalação, você pode usar o pyenv para instalar diferentes versões do Python. Por exemplo:
```bash
pyenv install 3.8.6
```

2. Para definir uma versão do Python como padrão global:
```bash
pyenv global 3.8.6
```

3. Para definir uma versão do Python em um diretório específico:

```bash
pyenv local 3.8.6
```

### Pipenv

O pipenv é um virtualizador de ambiente que pode trabalha com dois arquivos `Pipefile` e `Pipefile.lock`, ele tem um controle um pouco melhor que o virtualenv.

1. Instalar o pipenv

```bash
pip install pipenv
```

#### Uso do Pipenv

1. Criar um ambiente virtual e instalar dependências:
```bash
pipenv install
```

2. Ativar o ambiente virtual:
```bash
pipenv shell
```

3. Instalar um pacote no ambiente virtual:
```bash
pipenv install <nome_do_pacote>
```

4. Sair do ambiente virtual:
```bash
exit
```

### Rodar o projeto

Depois do ambiente configurado, você precisa executar dois comandos:

1. subir o banco:
```bash
make db-up
```

2. subir o backend:
```bash
make run
```

Obs: se vc precisar baixar o banco, roda esse comando:
```bash
make db-down
```



#### Endereço do swagger
http://127.0.0.1:5000/ 
