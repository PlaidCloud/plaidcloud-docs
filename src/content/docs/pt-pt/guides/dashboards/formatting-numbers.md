---
title: Formatar números e outros tipos de dados
description: Formate números nos painéis de controlo do PlaidCloud, incluindo moeda, percentagens, casas decimais e padrões personalizados de apresentação de números.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dashboards/formatting-numbers.md
---

## Formatar números e outros tipos de dados

Existem 2 formas de formatar números no PlaidCloud. Uma consiste em transformar diretamente os valores nas tabelas e a segunda (mais comum) consiste em formatá-los na apresentação, para que os valores não percam precisão na tabela e o utilizador possa ver os valores de uma forma mais limpa e adequada.

Quando apresento um valor num painel de controlo, como o formato da forma que pretendo?
A forma principal de apresentar um valor é através de um objeto de gráfico num painel de controlo. Os gráficos podem ser Tabelas, Números grandes, Gráficos de barras, etc. Cada objeto de gráfico pode ter um local ou meio ligeiramente diferente para apresentar os valores. Por exemplo, nas Tabelas, pode alterar o formato de cada coluna e, num Número grande, pode alterar o formato do número.

Para alterar o formato, edite o gráfico e localize o campo `D3 FORMAT` ou `NUMBER FORMAT`. Para um gráfico de Número grande, clique no separador `CUSTOMIZE` e verá `NUMBER FORMAT`. Para uma Tabela, clique no separador `CUSTOMIZE`, selecione uma coluna numérica (apresentada com um #) em `CUSTOMIZE COLUMN` e verá o campo `D3 FORMAT`.

O valor predefinido é `Adaptive formatting`. Este ajusta o formato com base nos valores. Mas se pretender fixá-lo a um formato (por exemplo, $12.23 ou 12,345,678), selecione o formato pretendido na lista pendente ou escreva manualmente um valor diferente (se o campo o permitir).

## Formatação D3 — o que é?

A formatação D3 é uma forma estruturada e formalizada de apresentar resultados de dados num formato específico. Por exemplo, em determinadas situações pode pretender apresentar um valor grande como 3B (3 mil milhões), formatado como `.3s` em formato D3, ou como 3,001,238,383, formatado como `,d`. Outro exemplo comum é a decisão de representar valores em dólares com 2 casas decimais de precisão, ou de os arredondar ao dólar mais próximo, $,d ou $,.2f para mostrar o símbolo do dólar, as vírgulas, 2 casas decimais de precisão e uma notação de vírgula fixa.
Para um estudo mais aprofundado do D3, consulte o seguinte site: [GitHub D3](https://github.com/d3/d3-format)


## Formato D3 geral

A estrutura geral do D3 é a seguinte:

`[​[fill]align][sign][symbol][0][width][,][.precision][~][type]`

O preenchimento (fill) pode ser qualquer caráter (como um ponto, x ou qualquer outro). Se tiver um caráter de preenchimento, segue-se-lhe um caráter `align`, que tem de ser um dos seguintes:

`>` - Alinhado à direita dentro do espaço disponível. (Comportamento predefinido).
`<` - Alinhado à esquerda dentro do espaço disponível.
`^` - Centrado dentro do espaço disponível.
`=` - como >, mas com qualquer sinal e símbolo à esquerda de qualquer preenchimento.

O `sign` pode ser:
`-` - vazio para zero ou positivo e um sinal de menos para negativo. (Comportamento predefinido.)
`+` - um sinal de mais para zero ou positivo e um sinal de menos para negativo.
`(` - nada para zero ou positivo e parênteses para negativo.
(espaço) - um espaço para zero ou positivo e um sinal de menos para negativo.

O `symbol` pode ser:
`$` - aplicar o símbolo de moeda.

A opção `zero` (0) ativa o preenchimento com zeros; isto define implicitamente o fill como 0 e o align como =.

O `width` define a largura mínima do campo; se não for especificado, a largura é determinada pelo conteúdo. Por exemplo, se tiver 8, a largura do campo será de 8 carateres.

A opção `comma` (,) ativa o uso de vírgulas como separadores (por exemplo, para milhares).

Consoante o tipo, a `precision` pode indicar o número de dígitos que se seguem à vírgula decimal (tipos f e %) ou o número de algarismos significativos (tipos ​, g, r, s e p). Se a precisão não for especificada, assume por predefinição 6 para todos os tipos exceto (nenhum), que assume por predefinição 12.

A opção `tilde` ~ elimina os zeros finais não significativos em todos os tipos de formato. É mais comummente usada em conjunto com os tipos r, s e %.

`types`
|Tipo |   Descrição                                                                                 |
|-----|---------------------------------------------------------------------------------------------|
|f    |notação de vírgula fixa. **(comum)**
|d    |notação decimal, arredondada para inteiro. **(comum)**
|%    |multiplica por 100 e depois notação decimal com um sinal de percentagem. **(comum)**
|g    |notação decimal ou exponencial, arredondada para algarismos significativos.
|r    |notação decimal, arredondada para algarismos significativos.
|s    |notação decimal com um prefixo SI, arredondada para algarismos significativos.
|p    |multiplica por 100, arredonda para algarismos significativos e depois notação decimal com um sinal de percentagem.

## Exemplos
|Expressão|Entrada|Saída|Notas|
|----------|-----|------|-----|
|,d|12345.67|12,346|arredonda o valor para o inteiro mais próximo, adiciona vírgulas
|,.2f|12345.678|12,345.68|Adiciona vírgulas, 2 casas decimais, arredonda para a segunda casa decimal
|$,.2f|12345.67|$12,345.67|Adiciona um símbolo $, tem vírgulas, 2 dígitos após a vírgula decimal
|$,d|12345.67|$12,346|
|.&lt;10,|151925|151,925...|tem pontos à esquerda do valor, 10 carateres de largura, com vírgulas
|0>10|12345|0000012345|preenche o valor com zeros à esquerda, 10 carateres de largura. Funciona bem para fixar a largura de um valor de código 
|,.2%|13.215|1,321.50%|tem vírgulas, 2 dígitos à direita da vírgula decimal, converte em percentagem e mostra um símbolo %
|x^+$16,.2f|123456|xx+$123,456.00xx| preenche com "x", centrado, tem um símbolo +/-, símbolo $, 16 carateres de largura, tem vírgulas, 2 casas decimais
