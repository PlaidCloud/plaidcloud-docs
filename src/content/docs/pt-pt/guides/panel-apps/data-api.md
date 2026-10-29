---
title: A Data API para aplicações Panel
description: Leia tabelas do PlaidCloud a partir de uma aplicação Panel com panel_data — filtre, pagine, conte e agregue no servidor, como o visualizador com sessão iniciada, com a segurança ao nível da linha aplicada.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/data-api.md
---

`plaidcloud.utilities.panel_data` é a forma de uma aplicação Panel de servidor ler uma tabela sem carregar a tabela inteira para a aplicação. Descreve o que pretende — linhas que correspondem a alguns filtros, uma página delas, uma contagem, um total agrupado — e a base de dados do PlaidCloud faz o trabalho. Apenas o resultado volta para a aplicação.

Cada pedido é executado como a pessoa que está a ver a aplicação, pelo que as suas permissões de projeto e a [segurança ao nível da linha](/pt-pt/guides/panel-apps/accessing-data/) se aplicam a tudo o que é devolvido.

```python
from plaidcloud.utilities.panel_data import table

sales = table("sales")
```

`table(name)` abre uma tabela no projeto da aplicação, que é o projeto a que a aplicação foi [atribuída](/pt-pt/guides/panel-apps/branding/#atribuir-uma-aplicação-a-um-projeto) quando foi publicada. Para ler uma tabela de um projeto diferente, passe-o: `table("sales", project="Finance")`. O projeto pode ser um id, um nome ou um caminho.

Um identificador de tabela nunca muda. `filter` devolve um novo identificador, pelo que pode manter o que não tem filtros e derivar várias vistas a partir dele.

## Filtrar

```python
emea = sales.filter(region="EMEA", year=[2025, 2026])
```

Cada argumento nomeado é o nome de uma coluna. Um único valor corresponde às linhas iguais a ele. Uma lista, tuplo ou conjunto corresponde às linhas iguais a qualquer um dos seus membros. Vários argumentos combinam-se com AND, e chamar `filter` novamente sobre o resultado acrescenta mais condições.

Um valor `None`, uma cadeia vazia ou uma lista vazia deixa essa coluna sem filtro. É isso que permite que um widget de filtro em branco deixe os dados em paz: `sales.filter(**widget_values)` funciona sem verificar primeiro se há valores em branco.

Indicar uma coluna que não existe gera um erro que nomeia a tabela e a coluna.

## Paginar

```python
rows = emea.page(1, 200, sort=["-amount"], key="id")
```

`page(n, size, sort, key)` devolve a página `n` (a contar a partir de 1) de `size` linhas como um dataframe do pandas.

- `sort` é uma lista de nomes de colunas. Coloque o prefixo `-` num nome para ordem descendente: `["region", "-amount"]`.
- `key` é a coluna única, ou lista de colunas únicas, da tabela. Passe-a sempre.

### Paginação estável

A paginação obtém uma fatia de uma lista ordenada de linhas. Cada pedido é uma consulta separada. Se duas linhas empatarem nas colunas de ordenação, a base de dados pode devolvê-las por outra ordem no pedido seguinte, pelo que uma linha pode aparecer em duas fatias ou em nenhuma. `key` fecha essa lacuna: o PlaidCloud acrescenta-a depois das suas colunas de ordenação, pelo que a ordem é sempre completa e cada linha fica exatamente numa fatia.

Sem `key`, a paginação recorre à ordenação por todas as colunas. Isso é lento numa tabela larga e continua instável se duas linhas forem idênticas. Passe uma chave única sempre que paginar e, pela mesma razão, passe-a à [`DataGrid`](/pt-pt/guides/panel-apps/app-kit/#datagrid).

## Contar

```python
total_rows = emea.count()
```

Devolve o número de linhas que correspondem aos filtros, como número inteiro.

## Agregar

```python
by_region = sales.aggregate(by=["region"], total=("amount", "sum"), orders=("id", "count"))
grand_total = emea.aggregate(total=("amount", "sum"))
```

`aggregate(by=(), limit=1000, **measures)` devolve um dataframe com uma linha por grupo, ordenado pelas colunas de `by`. Cada medida é `name=(column, function)`, em que a função é `sum`, `count`, `avg`, `min` ou `max`. É necessária pelo menos uma medida.

Sem `by`, obtém uma única linha de totais sobre as linhas filtradas. `limit` limita o número de grupos devolvidos.

As colunas decimais podem chegar como cadeias. Converta-as com `float(...)` ou `astype(float)` antes de as representar em gráficos ou formatar.

## Juntar tudo

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

`FilterBar`, `KpiCard` e `DataGrid` aceitam todos estes identificadores de tabela, pelo que a maioria das aplicações nunca chama `page`, `count` ou `aggregate` diretamente. Use-os quando criar as suas próprias vistas. Consulte [O Panel App Kit](/pt-pt/guides/panel-apps/app-kit/).

## Relacionado

- [Ler dados e o utilizador com sessão iniciada](/pt-pt/guides/panel-apps/accessing-data/) — ligar como o visualizador e quando usar `PlaidConnection` diretamente.
