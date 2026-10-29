---
title: Formatação de números e outros tipos de dados
description: Formate números em painéis do PlaidCloud, incluindo moeda, porcentagens, casas decimais e padrões personalizados de exibição de números.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dashboards/formatting-numbers.md
---

## Formatação de números e outros tipos de dados

Há duas maneiras de formatar números no PlaidCloud. Uma é transformar diretamente os valores nas tabelas; a outra (mais comum) é formatá-los na exibição, para que os valores não percam precisão na tabela e o usuário os veja de uma forma mais limpa e adequada.

Quando exibo um valor em um painel, como o formato da maneira que quero?
A principal forma de exibir um valor é por meio de um objeto de gráfico em um painel. Os gráficos podem ser Tabelas, Números grandes, Gráficos de barras e assim por diante. Cada objeto de gráfico pode ter um lugar ou meio um pouco diferente para exibir os valores. Por exemplo, em Tabelas, você pode alterar o formato de cada coluna e, em um Número grande, pode alterar o formato do número.

Para alterar o formato, edite o gráfico e localize o campo `D3 FORMAT` ou `NUMBER FORMAT`. Em um gráfico de Número grande, clique na guia `CUSTOMIZE` e você verá `NUMBER FORMAT`. Em uma Tabela, clique na guia `CUSTOMIZE`, selecione uma coluna numérica (exibida com um #) em `CUSTOMIZE COLUMN` e você verá o campo `D3 FORMAT`.

O valor padrão é `Adaptive formatting`. Ele ajusta o formato com base nos valores. Mas, se você quiser fixar um formato (por exemplo, $12.23 ou 12,345,678), selecione o formato desejado na lista suspensa ou digite manualmente um valor diferente (se o campo permitir).

## Formatação D3 - o que é?

A formatação D3 é um meio estruturado e formal de exibir resultados de dados em um formato específico. Por exemplo, em certas situações você pode querer exibir um valor grande como 3B (3 bilhões), formatado como `.3s` no formato D3, ou como 3,001,238,383, formatado como `,d`. Outro exemplo comum é a decisão de representar valores em dólares com precisão de 2 casas decimais ou arredondá-los para o dólar mais próximo, $,d ou $,.2f, para mostrar o símbolo de dólar, as vírgulas, a precisão de 2 casas decimais e a notação de ponto fixo.
Para um aprofundamento em D3, consulte o seguinte site: [GitHub D3](https://github.com/d3/d3-format)


## Formato D3 geral

A estrutura geral do D3 é a seguinte:

`[​[fill]align][sign][symbol][0][width][,][.precision][~][type]`

O preenchimento (fill) pode ser qualquer caractere (como um ponto, x ou qualquer outro). Se você tiver um caractere de preenchimento, ele deve ser seguido por um caractere `align`, que deve ser um destes:

`>` - Alinhado à direita dentro do espaço disponível. (Comportamento padrão).
`<` - Alinhado à esquerda dentro do espaço disponível.
`^` - Centralizado dentro do espaço disponível.
`=` - como >, mas com qualquer sinal e símbolo à esquerda de qualquer preenchimento.

O `sign` pode ser:
`-` - vazio para zero ou positivo e um sinal de menos para negativo. (Comportamento padrão.)
`+` - um sinal de mais para zero ou positivo e um sinal de menos para negativo.
`(` - nada para zero ou positivo e parênteses para negativo.
(espaço) - um espaço para zero ou positivo e um sinal de menos para negativo.

O `symbol` pode ser:
`$` - aplica o símbolo de moeda.

A opção `zero` (0) ativa o preenchimento com zeros; isso define implicitamente o fill como 0 e o align como =.

O `width` define a largura mínima do campo; se não for especificado, a largura será determinada pelo conteúdo. Por exemplo, se você usar 8, a largura do campo será de 8 caracteres.

A opção `comma` (,) ativa o uso de vírgulas como separadores (por exemplo, de milhares).

Dependendo do tipo, a `precision` pode indicar o número de dígitos após o ponto decimal (tipos f e %) ou o número de dígitos significativos (tipos ​, g, r, s e p). Se a precisão não for especificada, o padrão é 6 para todos os tipos, exceto (nenhum), cujo padrão é 12.

A opção `tilde` ~ remove os zeros finais não significativos em todos os tipos de formato. É mais comumente usada em conjunto com os tipos r, s e %.

`types`
|Tipo |   Descrição                                                                                 |
|-----|---------------------------------------------------------------------------------------------|
|f    |notação de ponto fixo. **(comum)**
|d    |notação decimal, arredondada para inteiro. **(comum)**
|%    |multiplica por 100 e depois usa notação decimal com um sinal de porcentagem. **(comum)**
|g    |notação decimal ou exponencial, arredondada para dígitos significativos.
|r    |notação decimal, arredondada para dígitos significativos.
|s    |notação decimal com um prefixo do SI, arredondada para dígitos significativos.
|p    |multiplica por 100, arredonda para dígitos significativos e depois usa notação decimal com um sinal de porcentagem.

## Exemplos
|Expressão|Entrada|Saída|Observações|
|----------|-----|------|-----|
|,d|12345.67|12,346|arredonda o valor para o inteiro mais próximo, adiciona vírgulas
|,.2f|12345.678|12,345.68|Adiciona vírgulas, 2 casas decimais, arredonda para a segunda casa decimal
|$,.2f|12345.67|$12,345.67|Adiciona o símbolo $, tem vírgulas, 2 dígitos após o ponto decimal
|$,d|12345.67|$12,346|
|.&lt;10,|151925|151,925...|tem pontos à esquerda do valor, 10 caracteres de largura, com vírgulas
|0>10|12345|0000012345|preenche o valor com zeros à esquerda, 10 caracteres de largura. Funciona bem para fixar a largura de um valor de código 
|,.2%|13.215|1,321.50%|tem vírgulas, 2 dígitos à direita do ponto decimal, converte em porcentagem e mostra o símbolo %
|x^+$16,.2f|123456|xx+$123,456.00xx| preenche com "x", centralizado, com símbolo +/-, símbolo $, 16 caracteres de largura, com vírgulas, 2 casas decimais
