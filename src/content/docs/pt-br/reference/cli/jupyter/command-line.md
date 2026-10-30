---
title: Linha de comando
description: Use a interface de linha de comando do PlaidCloud para automatizar tarefas, executar scripts e interagir com os recursos do PlaidCloud pelo terminal.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

O PlaidCloud usa solicitações JSON-RPC padrão e pode ser usado com qualquer aplicativo capaz de fazer essas solicitações.


Para facilitar, há um pacote Python que simplifica o processo de conexão e de execução da API.


## Instalação necessária

Em um terminal, execute o seguinte comando:

```bash
pip install plaidcloud-rpc
```


## Usar o objeto SimpleRPC para fazer uma solicitação

Para fazer uma solicitação com o pacote `plaidcloud-rpc`, use o objeto `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC  
  
auth_token = "Your PlaidCloud Auth Token" # See Obtaining Token below  
endpoint_uri = "plaidcloud.com" # or plaidcloud.net  
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Com o objeto `SimpleRPC` instanciado, você pode enviar solicitações RPC ao PlaidCloud. Este exemplo solicita os metadados de uma tabela.

```python
table = rpc.analyze.table.table(  
            project_id=project_id,  
            table_id=table_id  
        )
```

## Quais APIs estão disponíveis?

Há muitas APIs disponíveis que controlam quase todos os aspectos do PlaidCloud. A referência interativa da API é disponibilizada por locatário, dentro de cada espaço de trabalho do PlaidCloud: abra seu espaço de trabalho e acesse o menu de documentação da API para ver o catálogo de endpoints em tempo real.


## Obter um token OAuth

Consulte [Configuração do OAuth](/pt-br/reference/cli/jupyter/oauth-setup/) para saber mais sobre como obter um token OAuth e como configurar o sistema para autenticação automatizada.
