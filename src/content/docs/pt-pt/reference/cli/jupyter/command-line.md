---
title: Linha de comandos
description: Utilize a interface de linha de comandos do PlaidCloud para automatizar tarefas, executar scripts e interagir com recursos do PlaidCloud através do terminal.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

O PlaidCloud utiliza pedidos JSON-RPC padrão e pode ser utilizado com qualquer aplicação capaz de efetuar esses pedidos.


Para facilitar, está disponível um pacote Python que simplifica o processo de ligação e de execução da API.


## Instalação necessária

Num terminal, execute o seguinte comando:

```bash
pip install plaidcloud-rpc
```


## Utilizar o objeto Simplerpc para fazer um pedido

Para fazer um pedido com o pacote `plaidcloud-rpc`, utilize o objeto `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC  
  
auth_token = "Your PlaidCloud Auth Token" # See Obtaining Token below  
endpoint_uri = "plaidcloud.com" # or plaidcloud.net  
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Depois de instanciar o objeto `SimpleRPC`, pode emitir pedidos RPC ao PlaidCloud. Este exemplo pede os metadados de uma tabela.

```python
table = rpc.analyze.table.table(  
            project_id=project_id,  
            table_id=table_id  
        )
```

## Que APIs estão disponíveis?

Existem muitas APIs disponíveis que controlam quase todos os aspetos do PlaidCloud. A referência interativa da API é disponibilizada por inquilino, dentro de cada área de trabalho do PlaidCloud: abra a sua área de trabalho e navegue até ao menu de documentação da API para ver o catálogo de endpoints em direto.


## Obter um token OAuth

Consulte [Configuração de OAuth](/pt-pt/reference/cli/jupyter/oauth-setup/) para obter mais informações sobre como obter um token OAuth e como configurar o sistema para autenticação automatizada.
