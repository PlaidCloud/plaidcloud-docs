---
title: Funções de dimensão para expressões e agregações
description: Utilize expressões de função nas dimensões do PlaidCloud para definir valores calculados, lógica condicional e propriedades dinâmicas dos membros.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/function-expressions.md
---

## Funções para utilizar em expressões de hierarquias de dimensão

No ecrã Hierarquia da dimensão é possível adicionar «Agregações» e «Expressões». Segue-se uma descrição de cada uma.

## Agregações
Uma agregação serve para apresentar um valor agregado de uma tabela (que pode ser «Sum», «Count», «Min» ou «Max»).
A imagem seguinte mostra uma agregação configurada para obter valores de uma tabela «Line Item Values», de forma a que possam ser apresentados valores para cada «Período» da hierarquia.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_1_agg.png)

As agregações podem ser filtradas para que só sejam apresentados os itens que correspondem ao filtro. Na imagem seguinte, configurámos a agregação para mostrar valores de um item selecionado da dimensão «Conta».

![Dimension Load](/images/dimensions/expressions/dimension_expressions_2_agg.png)

Se estes filtros ficarem em branco, os dados podem ser filtrados com a barra de filtros da dimensão, na parte superior do ecrã, como se pode ver na imagem seguinte:

![Dimension Load](/images/dimensions/expressions/dimension_expressions_3_agg.png)

## Expressões

Com as expressões é possível apresentar valores calculados com base nos valores das agregações apresentadas para a dimensão.
As expressões são construídas com fórmulas matemáticas, que podem conter vários tipos de operadores e algumas funções especiais. Consulte a [lista de operadores](https://mathjs.org/docs/expressions/syntax.html). As funções disponíveis são descritas abaixo.


## Funções
### Column(`<column_name>`)
Obtém um valor de uma coluna com nome para a linha/nó atual.

Abaixo vemos um exemplo de uma expressão definida para apresentar o resultado da multiplicação do valor de rubrica (Line Item Value) por 2.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_4_func_column.png)


![Dimension Load](/images/dimensions/expressions/dimension_expressions_5_func_column.png)

### Childcount()

Devolve o número de nós inferiores da linha/nó atual. Se a linha/nó atual for um item folha, devolve 0.

No exemplo seguinte, é utilizada para devolver o valor médio dos nós inferiores de um nó superior.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_6_func_childcount.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_7_func_childcount.png)

### Leafcount()
Devolve o número de itens folha encontrados na árvore para a linha/nó atual. Se a linha/nó atual for um item folha, devolve 1.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_8_func_leafcount.png)

### Descendantcount()
Devolve o número total de itens encontrados na árvore para a linha/nó atual. Se a linha/nó atual for um item folha, devolve 0.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_9_func_desccount.png)


### Siblingcount()
Devolve o número de itens irmãos da linha/nó atual. O valor devolvido inclui o nó atual.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_10_func_siblingcount.png)


### Nodevalue("`<node_name>`","`<column_name>`")
Devolve o valor de uma coluna com nome para um nó com nome.
Eis um exemplo que serve para mostrar a percentagem do total «LIV» para cada linha/nó.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_11_func_nodevalue.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_12_func_nodevalue.png)


### Parentvalue("<column_name")
Devolve o valor de uma determinada coluna para o nó superior do nó atual.
Este exemplo mostra a percentagem do valor de um nó superior que é utilizada por um nó inferior.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_13_func_parentvalue.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_14_func_parentvalue.png)

### Columntextcompare("<column_name", "`<text>`")

Devolve um resultado numérico que indica se o texto de uma coluna com nome é maior, menor ou igual a um valor fornecido.

Se o texto da coluna for igual ao texto fornecido, esta função devolve 0.

Se o texto da coluna for menor do que o texto fornecido, esta função devolve -1.

Se o texto da coluna for maior do que o texto fornecido, esta função devolve 0.


O exemplo seguinte compara o nome do período com «Jun»


![Dimension Load](/images/dimensions/expressions/dimension_expressions_15_func_textcompare.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_16_func_textcompare.png)


## Expressões condicionais
Os exemplos apresentados acima são bastante simples. Utilizando condicionais nas expressões, é possível criar expressões mais complexas.
Nas expressões, as condicionais têm a seguinte forma:
`<condition>` ? `<value_if_true>` : `<value_if_false>`
p. ex. '12 > 6 ? 1000: 0'

Ao combinar expressões que contêm condicionais e funções, podemos construir expressões mais complexas, como neste exemplo, em que se somam 100 000 a um valor de rubrica se o mês for «Jun»

![Dimension Load](/images/dimensions/expressions/dimension_expressions_17_cond.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_18_cond.png)


## Outro exemplo: alocação simples

Este exemplo mostra o montante do valor de rubrica de um nó superior que é consumido através do valor de driver de recurso de um nó folha.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_19_alloc.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_20_alloc.png)

## Limitações:
Atualmente não é possível construir expressões baseadas em valores de outras expressões. As expressões só podem ser construídas com valores de agregações.
