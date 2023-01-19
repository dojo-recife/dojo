# Setup Tests

Para criar o setup de testes de uma linguagem que ainda não tem o setup criado siga os seguintes passos:
 - Crie um arquivo com o modelo de testes na linguagem em questão;
 - Nomeie o arquivo com o padrão setup_{linguagem}.extension;
 - Adicione no [Makefile](https://github.com/dojo_recife/dojo/blob/main/Makefile) o comando {linguagem}_setup para criar um novo diretório com os arquivos necessários para escrever a função que será criada no dojo e com o arquivo de testes contendo o código do modelo do setup correspondente