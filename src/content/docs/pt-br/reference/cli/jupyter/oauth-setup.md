---
title: Tokens OAuth
description: Configure tokens OAuth para acesso à API do PlaidCloud e autentique Notebooks Jupyter, ferramentas de CLI e conexões de aplicativos personalizados.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/oauth-setup.md
---

O PlaidCloud usa solicitações JSON-RPC padrão e pode ser usado com qualquer aplicativo capaz de fazer essas solicitações. As solicitações são protegidas por tokens OAuth.


## Obter um token OAuth

Os tokens OAuth são gerados no aplicativo PlaidCloud. Para ver a lista de tokens OAuth atribuídos a você e gerar novos, acesse `Analyze > Tools > Registered Systems`.

Lá você pode ver os tokens existentes ou optar por criar um novo.

## Baixar o arquivo de configuração OAuth do PlaidCloud
Selecione "Register a New System".

Preencha o formulário e anote o nome que você informou para poder encontrá-lo na lista.

Depois de criado, abra o registro do sistema registrado clicando no ícone de engrenagem. Isso exibirá o texto do arquivo de configuração.  

OBSERVAÇÃO: selecione o projeto para o qual você quer usar essa conexão na lista suspensa no topo. Isso adicionará o identificador exclusivo do projeto à configuração.

Copie esse texto para um arquivo plaid.conf no seu sistema. Coloque-o no diretório .plaid.

## Criar um arquivo de configuração local
Crie um diretório um nível acima do diretório do seu notebook ou do local em que você pretende usar a interação por linha de comando. Dê ao diretório o nome `.plaid`.

Dentro do diretório `.plaid`, crie um arquivo chamado `plaid.conf` e cole nele o conteúdo copiado acima. Salve o arquivo e isso permitirá que você se conecte usando os utilitários do PlaidCloud e os métodos rpc.


## Usos avançados

Embora seja conveniente colocar a pasta `.plaid` perto do ponto de uso, ela pode ficar em qualquer lugar da árvore de diretórios superior. O processo de inicialização percorrerá a árvore de diretórios para cima até encontrar o diretório `.plaid`.

Colocar o diretório `.plaid` em um nível mais alto pode ser útil se você tiver várias operações que precisam de acesso, mas não podem coexistir nas mesmas estruturas de diretórios de nível inferior.


## Especificação opcional de caminhos
Se você usa uma instalação local do Notebook Jupyter ou trabalha pela linha de comando, é possível exportar dados, arquivos do Excel e outros dados, além de ler dados locais em DataFrames, usando as ferramentas auxiliares. Para isso, é necessário um arquivo paths.yaml.

Além do arquivo `plaid.conf`, crie um arquivo `paths.yaml`. O `paths.yaml` deve ficar no mesmo nível do arquivo `plaid.conf`, dentro do diretório `.plaid`. Ele deve conter as seguintes informações de caminho:

```yaml
paths:
 PROJECT_ROOT: '{WORKING_USER}/Documents'
 LOCAL_STORAGE: '{PROJECT_ROOT}/local_storage'
 DEBUG: '{PROJECT_ROOT}/local_storage'
 REPORTS: '{PROJECT_ROOT}/reports'
 
 create: []
 local: {}
```
