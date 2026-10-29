---
title: Resolução de problemas de alocações
description: Resolva problemas de alocação do PlaidCloud, incluindo erros comuns, problemas de configuração e técnicas para depurar resultados.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/troubleshooting-allocations.md
---

## Porque é que um passo de alocação não é guardado

O PlaidCloud verifica o mapeamento de colunas de um passo de alocação quando o guarda. Um mapeamento que não possa ser executado é recusado nesse momento, com uma notificação **Não é possível guardar** que lista o que deve corrigir, e o formulário passa para o separador que contém o problema. Anteriormente, um passo destes era guardado sem reclamação e depois interrompia o fluxo de trabalho a meio de uma execução — muitas vezes minutos depois, e com uma mensagem que indicava uma contagem em vez de um campo.

Nada é verificado até ter escolhido a **Tabela de valores a alocar** e a **Tabela de dados de driver**. O mapeamento de colunas é construído a partir dessas duas tabelas, pelo que, enquanto ambas não estiverem definidas, o passo pede apenas as próprias tabelas.

### Mapa de origem da alocação

**"No columns specified for allocation."**
Defina a **Função** de pelo menos uma coluna como **Valor a alocar**. Essa coluna contém os valores que são repartidos pelos destinos.

**"Only numeric columns can be allocated, but ... is not numeric."**
Uma coluna marcada como **Valor a alocar** tem um **Tipo** não numérico. Altere o tipo para um numérico — Numeric, Currency, Integer, Inteiro grande, Inteiro pequeno, Inteiro minúsculo, Float, Double, Decimal, Serial ou Série grande.

**"Rename the `alloc_status` target column."**
Uma alocação escreve a sua própria coluna `alloc_status` na tabela de resultados, pelo que uma coluna de destino com esse nome colide com ela. Mude o nome da sua.

### Mapa de dados de driver

**"No driver split value column found."**
Defina a **Função** de uma coluna de driver como **Valor de divisão**. Essa coluna contém as ponderações ou percentagens pelas quais a alocação divide.

**"The driver value column ... must be numeric."**
Altere o **Tipo** da coluna **Valor de divisão** para um numérico.

**"No driver relation columns specified."**
Defina a **Função** de pelo menos uma coluna de driver como **Relação de origem (denominador)**. É isto que relaciona as linhas do driver com as linhas de origem.

**"No allocation target columns are indicated."**
Defina a **Função** de pelo menos uma coluna de driver como **Destino da alocação (numerador)**. Estas passam a ser os destinos da alocação e aparecem na tabela de resultados.

**"Driver relation columns do not exist in the source data."**
Uma coluna marcada como **Relação de origem (denominador)** não tem uma coluna correspondente com o mesmo nome no **Mapa de origem da alocação**. Mude-lhe o nome para coincidir ou adicione a coluna ao mapa de origem.

**"Allocation value column ... is also used as a numerator or denominator column."**
O mesmo nome de coluna é simultaneamente um **Valor a alocar** no mapa de origem e uma **Relação de origem (denominador)** ou um **Destino da alocação (numerador)** no mapa de driver. Mude o nome de uma delas para que o valor a alocar seja distinto das colunas que descrevem para onde vai.

### Apenas Dividir por dimensão

**"Please select a hierarchy to use for the allocation dimension."**
Escolha uma **Hierarquia da dimensão de atribuição** no separador **Definições da tabela de dados**. Consulte [Configurar uma alocação](/pt-pt/guides/allocations/setup/configure-an-allocation/).

## Custo órfão

Stranded cost is....

## Sobrealocação de custo

Over allocation of cost is when you end up with more output cost...

## Alocação incorreta de custo

Incorrect allocation of costs happens when...
