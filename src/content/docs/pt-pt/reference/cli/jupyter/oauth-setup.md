---
title: Tokens OAuth
description: Configure tokens OAuth para o acesso à API do PlaidCloud e autentique blocos de notas Jupyter, ferramentas CLI e ligações de aplicações personalizadas.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/oauth-setup.md
---

O PlaidCloud utiliza pedidos JSON-RPC padrão e pode ser utilizado com qualquer aplicação capaz de efetuar esses pedidos.  Os pedidos são protegidos com tokens OAuth.


## Obter um token OAuth

Os tokens OAuth são gerados a partir da aplicação PlaidCloud. Para ver a lista de tokens OAuth que lhe estão atribuídos e gerar novos, navegue até `Analyze > Tools > Registered Systems`.

Aí, pode ver os tokens existentes ou optar por criar um novo.

## Transferir o ficheiro de configuração OAuth do PlaidCloud
Selecione "Register a New System".

Preencha o formulário e tome nota do nome que introduziu, para o poder encontrar na lista.

Depois de criado, abra o registo do sistema registado clicando no ícone de engrenagem.  Será apresentado o texto do ficheiro de configuração.  

NOTA: Certifique-se de que seleciona, na lista pendente na parte superior, o projeto para o qual pretende utilizar esta ligação.  Isto adiciona o identificador único do projeto à configuração.

Copie este texto para um ficheiro plaid.conf no seu sistema.  Coloque-o no diretório .plaid.

## Criar um ficheiro de configuração local
Crie um diretório um nível acima do diretório do seu bloco de notas ou do local onde pretende utilizar a interação por linha de comandos.  Dê ao diretório o nome `.plaid`.

Dentro do diretório `.plaid`, crie um ficheiro chamado `plaid.conf` e cole nele o conteúdo copiado acima.  Guarde o ficheiro e passará a poder ligar-se com os utilitários do PlaidCloud e os métodos rpc.


## Utilizações avançadas

Embora seja conveniente colocar a pasta `.plaid` perto do ponto de utilização, esta pode ser colocada em qualquer ponto da árvore de diretórios superior.  O processo de inicialização percorre a árvore de diretórios para cima até encontrar o diretório `.plaid`.

Colocar o diretório `.plaid` mais acima pode ser útil se tiver várias operações que precisam de acesso mas não podem coexistir nas mesmas estruturas de diretórios de nível inferior.


## Especificação opcional de caminhos
Se utilizar uma instalação local do Jupyter Notebook ou trabalhar a partir da linha de comandos, é possível exportar dados, ficheiros Excel e outros dados, bem como ler dados locais para DataFrames, com as ferramentas auxiliares. Para tal, é necessário um ficheiro paths.yaml.

Além do ficheiro `plaid.conf`, crie um ficheiro `paths.yaml`.  O `paths.yaml` deve estar ao lado do ficheiro `plaid.conf`, dentro do diretório `.plaid`.  Deve conter as seguintes informações de caminhos:

```yaml
paths:
 PROJECT_ROOT: '{WORKING_USER}/Documents'
 LOCAL_STORAGE: '{PROJECT_ROOT}/local_storage'
 DEBUG: '{PROJECT_ROOT}/local_storage'
 REPORTS: '{PROJECT_ROOT}/reports'
 
 create: []
 local: {}
```
