---
title: A Data API para aplicativos Panel
description: Leia tabelas do PlaidCloud em um aplicativo Panel com panel_data — filtre, pagine, conte e agregue no servidor, como o visualizador conectado, com a segurança em nível de linha aplicada.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/data-api.md
---

`plaidcloud.utilities.panel_data` é a forma de um aplicativo Panel de servidor ler uma tabela sem carregar a tabela inteira no aplicativo. Você descreve o que quer — as linhas que correspondem a alguns filtros, uma página delas, uma contagem, um total agrupado — e o banco de dados do PlaidCloud faz o trabalho. Apenas o resultado volta para o aplicativo.

Cada solicitação é executada como a pessoa que está visualizando o aplicativo, então as permissões de projeto e a [segurança em nível de linha](/pt-br/guides/panel-apps/accessing-data/) dela se aplicam a tudo o que é retornado.

```python
from plaidcloud.utilities.panel_data import table

sales = table("sales")
```

`table(name)` abre uma tabela no projeto do aplicativo, que é o projeto ao qual o aplicativo foi [atribuído](/pt-br/guides/panel-apps/branding/#atribuir-um-aplicativo-a-um-projeto) quando foi publicado. Para ler uma tabela de outro projeto, informe-o: `table("sales", project="Finance")`. O projeto pode ser um ID, um nome ou um caminho.

Um identificador de tabela nunca muda. `filter` retorna um novo identificador, então você pode manter o que não tem filtro e derivar várias visões a partir dele.

## Filtrar

```python
emea = sales.filter(region="EMEA", year=[2025, 2026])
```

Cada palavra-chave é um nome de coluna. Um único valor corresponde às linhas iguais a ele. Uma lista, tupla ou conjunto corresponde às linhas iguais a qualquer membro. Várias palavras-chave se combinam com AND, e chamar `filter` novamente sobre o resultado adiciona mais condições.

Um valor `None`, uma string vazia ou uma lista vazia deixa essa coluna sem filtro. É isso que permite que um widget de filtro em branco deixe os dados em paz: `sales.filter(**widget_values)` funciona sem verificar valores em branco antes.

Informar uma coluna que não existe gera um erro que nomeia a tabela e a coluna.

## Paginar

```python
rows = emea.page(1, 200, sort=["-amount"], key="id")
```

`page(n, size, sort, key)` retorna a página `n` (contando a partir de 1) com `size` linhas, como um dataframe do pandas.

- `sort` é uma lista de nomes de colunas. Coloque o prefixo `-` em um nome para ordem decrescente: `["region", "-amount"]`.
- `key` é a coluna exclusiva, ou a lista de colunas exclusivas, da tabela. Sempre informe-a.

### Paginação estável

A paginação pega uma fatia de uma lista ordenada de linhas. Cada solicitação é uma consulta separada. Se duas linhas empatam nas colunas de ordenação, o banco de dados pode retorná-las em outra ordem na próxima solicitação, e uma linha pode aparecer em duas fatias ou em nenhuma. `key` fecha essa brecha: o PlaidCloud a adiciona depois das suas colunas de ordenação, então a ordem é sempre completa e cada linha cai em exatamente uma fatia.

Sem `key`, a paginação recorre à ordenação por todas as colunas. Isso é lento em uma tabela larga e ainda instável se duas linhas forem idênticas. Informe uma chave exclusiva sempre que paginar e, pelo mesmo motivo, informe-a também ao [`DataGrid`](/pt-br/guides/panel-apps/app-kit/#datagrid).

## Contar

```python
total_rows = emea.count()
```

Retorna o número de linhas que correspondem aos filtros, como um número inteiro.

## Agregar

```python
by_region = sales.aggregate(by=["region"], total=("amount", "sum"), orders=("id", "count"))
grand_total = emea.aggregate(total=("amount", "sum"))
```

`aggregate(by=(), limit=1000, **measures)` retorna um dataframe com uma linha por grupo, ordenado pelas colunas de `by`. Cada medida é `name=(column, function)`, em que a função é `sum`, `count`, `avg`, `min` ou `max`. É necessária pelo menos uma medida.

Sem `by`, você obtém uma única linha de totais sobre as linhas filtradas. `limit` limita o número de grupos retornados.

Colunas decimais podem chegar como strings. Converta-as com `float(...)` ou `astype(float)` antes de criar gráficos ou formatá-las.

## Juntando tudo

```python
import panel as pn
import plaidcloud_panel as pcp
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

orders = table("orders")
bar = pcp.FilterBar(orders, "status")

pcp.App(
    "Orders",
    sidebar=[bar],
    main=[
        pcp.KpiCard("Open value", bar.table, "amount"),
        pn.bind(lambda t: pcp.DataGrid(t, key="order_id"), bar.table),
    ],
).servable()
```

`FilterBar`, `KpiCard` e `DataGrid` aceitam todos esses identificadores de tabela, então a maioria dos aplicativos nunca chama `page`, `count` ou `aggregate` diretamente. Use-os ao criar suas próprias visões. Veja [O Panel App Kit](/pt-br/guides/panel-apps/app-kit/).

## Relacionados

- [Lendo dados e o usuário conectado](/pt-br/guides/panel-apps/accessing-data/) — conectar como o visualizador e quando usar `PlaidConnection` diretamente.
