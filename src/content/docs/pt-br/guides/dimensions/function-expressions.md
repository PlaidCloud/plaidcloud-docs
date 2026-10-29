---
title: Funções de dimensão para expressões e agregações
description: Use expressões de função em dimensões do PlaidCloud para definir valores calculados, lógica condicional e propriedades dinâmicas de membros.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/function-expressions.md
---

## Funções para uso em expressões de hierarquia de dimensão

Na tela Hierarquia da dimensão, é possível adicionar 'Agregações' e 'Expressões'. Uma descrição de cada uma está incluída abaixo.

## Agregações
Uma agregação é usada para exibir um valor agregado de uma tabela (que pode ser 'Sum', 'Count', 'Min' ou 'Max').
A imagem a seguir mostra uma agregação configurada para obter valores de uma tabela 'Valores de item de linha', de modo que os valores possam ser exibidos para cada 'Período' na hierarquia.

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_1_agg.png)

As agregações podem ser filtradas para que apenas os itens que correspondem ao filtro sejam exibidos. Na imagem a seguir, configuramos a agregação para mostrar valores de um item selecionado na dimensão 'Conta'.

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_2_agg.png)

Se esses filtros forem deixados em branco, os dados podem ser filtrados usando a barra de filtro de dimensão na parte superior da tela, como mostra a imagem a seguir:

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_3_agg.png)

## Expressões

Com as expressões, é possível exibir valores calculados a partir dos valores das agregações exibidas para a dimensão.
As expressões são criadas com fórmulas matemáticas, que podem conter vários tipos de operadores e algumas funções especiais. Consulte a [lista de operadores](https://mathjs.org/docs/expressions/syntax.html). As funções disponíveis são descritas abaixo.


## Funções
### Column(`<column_name>`)
Obtém um valor de uma coluna nomeada para a linha/nó atual.

Abaixo vemos um exemplo de uma expressão definida para exibir o resultado da multiplicação do Valor de item de linha por 2.

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_4_func_column.png)


![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_5_func_column.png)

### Childcount()

Retorna o número de filhos da linha/nó atual. Se a linha/nó atual for um item folha, retorna 0.

No exemplo a seguir, ela é usada para retornar o valor médio dos nós filhos de um nó pai.

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_6_func_childcount.png)

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_7_func_childcount.png)

### Leafcount()
Retorna o número de itens folha encontrados na árvore para a linha/nó atual. Se a linha/nó atual for um item folha, retorna 1.

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_8_func_leafcount.png)

### Descendantcount()
Retorna o número total de itens encontrados na árvore para a linha/nó atual. Se a linha/nó atual for um item folha, retorna 0.

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_9_func_desccount.png)


### Siblingcount()
Retorna o número de itens irmãos da linha/nó atual. O valor retornado inclui o nó atual.

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_10_func_siblingcount.png)


### Nodevalue("`<node_name>`","`<column_name>`")
Retorna o valor de uma coluna nomeada para um nó nomeado.
Eis um exemplo usado para mostrar o percentual do total "LIV" para cada linha/nó.

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_11_func_nodevalue.png)

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_12_func_nodevalue.png)


### Parentvalue("<column_name")
Retorna o valor de uma determinada coluna para o pai do nó atual.
Este exemplo mostra o percentual do valor de um nó pai que é usado por um nó filho.

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_13_func_parentvalue.png)

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_14_func_parentvalue.png)

### Columntextcompare("<column_name", "`<text>`")

Retorna um resultado numérico que indica se o texto de uma coluna nomeada é maior, menor ou igual a um valor informado.

Se o texto da coluna for igual ao texto informado, esta função retorna 0.

Se o texto da coluna for menor que o texto informado, esta função retorna -1.

Se o texto da coluna for maior que o texto informado, esta função retorna 0.


O exemplo a seguir compara o nome do Período com "Jun".


![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_15_func_textcompare.png)

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_16_func_textcompare.png)


## Expressões condicionais
Os exemplos mostrados acima são bastante simples. Usando condicionais dentro das expressões, é possível criar expressões mais complexas.
Dentro das expressões, as condicionais têm a seguinte forma:
`<condition>` ? `<value_if_true>` : `<value_if_false>`
por exemplo, '12 > 6 ? 1000: 0'

Combinando expressões que contêm condicionais e funções, podemos criar expressões mais complexas, como neste exemplo, em que 100.000 é somado a um Valor de item de linha se o mês for "Jun".

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_17_cond.png)

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_18_cond.png)


## Outro exemplo: alocação simples

Este exemplo mostra o valor do Valor de item de linha de um pai que é consumido usando o Valor de direcionador de recurso de um nó folha.

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_19_alloc.png)

![Carga de dimensão](/images/dimensions/expressions/dimension_expressions_20_alloc.png)

## Limitações:
Atualmente não é possível criar expressões baseadas em valores de outras expressões. As expressões só podem ser criadas usando valores de agregações.
