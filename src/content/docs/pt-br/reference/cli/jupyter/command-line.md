---
title: Linha de comando
description: Use a interface de linha de comando do PlaidCloud para automatizar tarefas, executar scripts e interagir com os recursos do PlaidCloud pelo terminal.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

O PlaidCloud tem uma API REST que qualquer aplicativo capaz de enviar solicitações HTTP pode usar. Para facilitar, o pacote Python `plaidcloud-rpc` cuida dos detalhes de conexão e de solicitação para você.

:::caution[O JSON-RPC está obsoleto]
O JSON-RPC está obsoleto e será removido em uma liberação futura. Use o `plaidcloud-rpc` 1.25.0 ou posterior, que envia suas chamadas para a API REST, e escreva novas integrações usando a API REST. Veja [O JSON-RPC está obsoleto](#o-json-rpc-está-obsoleto).
:::


## Instalação necessária

Em um terminal, execute o seguinte comando:

```bash
pip install "plaidcloud-rpc>=1.25.0"
```


## Usar o objeto SimpleRPC para fazer uma solicitação

Para fazer uma solicitação com o pacote `plaidcloud-rpc`, use o objeto `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC

auth_token = "Your PlaidCloud OAuth token"  # See Obtaining an OAuth Token below
endpoint_uri = "https://<your-workspace>.plaid.cloud/json-rpc/"
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Depois de instanciar o objeto `SimpleRPC`, você pode enviar solicitações ao PlaidCloud. Este exemplo solicita os metadados de uma tabela.

```python
table = rpc.analyze.table.table(
            project_id=project_id,
            table_id=table_id
        )
```

O `SimpleRPC` envia cada chamada para a API REST em `/rest/v1/` no host do seu espaço de trabalho, com o mesmo token. Uma chamada que a API REST ainda não cobre, ou uma chamada para um espaço de trabalho ainda em uma liberação anterior, usa o JSON-RPC, então o mesmo código funciona nos dois casos. Uma chamada com falha gera `RPCError` nos dois casos.


## Chamar a API REST diretamente

O `call_rest` envia uma solicitação para qualquer endpoint da API REST com o mesmo token, as mesmas configurações de TLS e as mesmas novas tentativas do `SimpleRPC`. Informe o método HTTP, o caminho em `/rest/v1/` e, opcionalmente, `params` para a string de consulta e `body` para um corpo de solicitação JSON.

```python
dimensions = rpc.call_rest(
    'GET',
    'analyze/dimension/dimensions',
    params={'project_id': project_id},
)
```

Ele retorna a resposta JSON decodificada, ou `None` quando a resposta não tem corpo. Qualquer resposta que não seja de sucesso gera `RPCError`, com o status HTTP como seu `code`.


## O JSON-RPC está obsoleto

O JSON-RPC está obsoleto e será removido em uma liberação futura. As versões do `plaidcloud-rpc` anteriores à 1.25.0 enviam todas as chamadas por JSON-RPC, então deixarão de funcionar quando ele for removido. Atualize para a 1.25.0 ou posterior; seu código `SimpleRPC` não precisa mudar. Escreva novas integrações usando a API REST.


## Quais APIs estão disponíveis?

Há muitas APIs disponíveis que controlam quase todos os aspectos do PlaidCloud. A referência interativa da API é disponibilizada por locatário, dentro de cada espaço de trabalho do PlaidCloud: abra seu espaço de trabalho e acesse o menu de documentação da API para ver o catálogo de endpoints em tempo real.


## Obter um token OAuth

Consulte [Configuração do OAuth](/pt-br/reference/cli/jupyter/oauth-setup/) para saber mais sobre como obter um token OAuth e como configurar o sistema para autenticação automatizada.
