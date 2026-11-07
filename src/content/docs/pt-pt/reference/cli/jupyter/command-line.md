---
title: Linha de comandos
description: Utilize a interface de linha de comandos do PlaidCloud para automatizar tarefas, executar scripts e interagir com recursos do PlaidCloud através do terminal.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

O PlaidCloud tem uma API REST que qualquer aplicação capaz de enviar pedidos HTTP pode utilizar. Para facilitar, o pacote Python `plaidcloud-rpc` trata por si dos detalhes da ligação e dos pedidos.

:::caution[O JSON-RPC está obsoleto]
O JSON-RPC está obsoleto e será removido numa versão futura. Utilize o `plaidcloud-rpc` 1.25.0 ou posterior, que envia as suas chamadas para a API REST, e escreva as novas integrações com base na API REST. Consulte [O JSON-RPC está obsoleto](#o-json-rpc-está-obsoleto).
:::


## Instalação necessária

Num terminal, execute o seguinte comando:

```bash
pip install "plaidcloud-rpc>=1.25.0"
```


## Utilizar o objeto SimpleRPC para fazer um pedido

Para fazer um pedido com o pacote `plaidcloud-rpc`, utilize o objeto `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC

auth_token = "Your PlaidCloud OAuth token"  # See Obtaining an OAuth Token below
endpoint_uri = "https://<your-workspace>.plaid.cloud/json-rpc/"
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Depois de instanciar o objeto `SimpleRPC`, pode enviar pedidos ao PlaidCloud. Este exemplo pede os metadados de uma tabela.

```python
table = rpc.analyze.table.table(
            project_id=project_id,
            table_id=table_id
        )
```

O `SimpleRPC` envia cada chamada para a API REST em `/rest/v1/` no anfitrião da sua área de trabalho, com o mesmo token. Uma chamada que a API REST ainda não abrange, ou uma chamada para uma área de trabalho ainda numa versão anterior, utiliza o JSON-RPC, pelo que o mesmo código funciona em ambos os casos. Uma chamada falhada gera `RPCError` em ambos os casos.


## Chamar diretamente a API REST

O `call_rest` envia um pedido para qualquer endpoint da API REST com o mesmo token, as mesmas definições de TLS e as mesmas novas tentativas que o `SimpleRPC`. Indique o método HTTP, o caminho em `/rest/v1/` e, opcionalmente, `params` para a cadeia de consulta e `body` para um corpo de pedido JSON.

```python
dimensions = rpc.call_rest(
    'GET',
    'analyze/dimension/dimensions',
    params={'project_id': project_id},
)
```

Devolve a resposta JSON descodificada, ou `None` quando a resposta não tem corpo. Qualquer resposta que não seja de sucesso gera `RPCError`, com o estado HTTP como `code`.


## O JSON-RPC está obsoleto

O JSON-RPC está obsoleto e será removido numa versão futura. As versões do `plaidcloud-rpc` anteriores à 1.25.0 enviam todas as chamadas por JSON-RPC, pelo que deixarão de funcionar quando este for removido. Atualize para a 1.25.0 ou posterior; o seu código `SimpleRPC` não precisa de ser alterado. Escreva as novas integrações com base na API REST.


## Que APIs estão disponíveis?

Existem muitas APIs disponíveis que controlam quase todos os aspetos do PlaidCloud. A referência interativa da API é disponibilizada por inquilino, dentro de cada área de trabalho do PlaidCloud: abra a sua área de trabalho e navegue até ao menu de documentação da API para ver o catálogo de endpoints em direto.


## Obter um token OAuth

Consulte [Configuração de OAuth](/pt-pt/reference/cli/jupyter/oauth-setup/) para obter mais informações sobre como obter um token OAuth e como configurar o sistema para autenticação automatizada.
