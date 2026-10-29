---
title: Solução de problemas de alocações
description: Resolva problemas de alocação do PlaidCloud, incluindo erros comuns, problemas de configuração e técnicas para depurar resultados.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/troubleshooting-allocations.md
---

## Por que uma etapa de alocação não é salva

O PlaidCloud verifica o mapeamento de colunas de uma etapa de alocação quando você a salva. Um mapeamento que não pode ser executado é recusado nesse momento, com uma notificação **Não é possível salvar** listando o que corrigir, e o formulário passa para a guia que contém o problema. Antes, uma etapa assim era salva sem reclamação e depois interrompia o fluxo de trabalho no meio de uma execução, muitas vezes minutos depois, e com uma mensagem que citava uma contagem em vez de um campo.

Nada é verificado até que você tenha escolhido a **Tabela de valores a alocar** e a **Tabela de dados do direcionador**. O mapeamento de colunas é construído a partir dessas duas tabelas, então, até que ambas estejam definidas, a etapa pede apenas as próprias tabelas.

### Mapa de origem da alocação

**"No columns specified for allocation."**
Defina a **Função** de pelo menos uma coluna como **Valor a alocar**. Essa coluna contém os valores que serão distribuídos entre os destinos.

**"Only numeric columns can be allocated, but ... is not numeric."**
Uma coluna marcada como **Valor a alocar** tem um **Tipo** não numérico. Altere o tipo para um numérico — Numeric, Currency, Integer, Inteiro grande, Inteiro pequeno, Inteiro minúsculo, Float, Double, Decimal, Serial ou Serial grande.

**"Rename the `alloc_status` target column."**
Uma alocação grava sua própria coluna `alloc_status` na tabela de resultado, então uma coluna de destino com esse nome entra em conflito com ela. Renomeie a sua.

### Mapa de dados do direcionador

**"No driver split value column found."**
Defina a **Função** de uma coluna do direcionador como **Dividir valor**. Essa coluna contém os pesos ou percentuais pelos quais a alocação divide.

**"The driver value column ... must be numeric."**
Altere o **Tipo** da coluna **Dividir valor** para um numérico.

**"No driver relation columns specified."**
Defina a **Função** de pelo menos uma coluna do direcionador como **Relação de origem (denominador)**. É isso que relaciona as linhas do direcionador de volta às linhas de origem.

**"No allocation target columns are indicated."**
Defina a **Função** de pelo menos uma coluna do direcionador como **Destino da alocação (numerador)**. Essas colunas se tornam os destinos da alocação e aparecem na tabela de resultado.

**"Driver relation columns do not exist in the source data."**
Uma coluna marcada como **Relação de origem (denominador)** não tem uma coluna de mesmo nome no **Mapa de origem da alocação**. Renomeie-a para corresponder ou adicione a coluna ao mapa de origem.

**"Allocation value column ... is also used as a numerator or denominator column."**
O mesmo nome de coluna é tanto um **Valor a alocar** no mapa de origem quanto uma **Relação de origem (denominador)** ou um **Destino da alocação (numerador)** no mapa do direcionador. Renomeie uma delas para que o valor que está sendo alocado seja distinto das colunas que descrevem para onde ele vai.

### Somente dividir usando dimensão

**"Please select a hierarchy to use for the allocation dimension."**
Escolha uma **Hierarquia da dimensão de atribuição** na guia **Configurações da tabela de dados**. Consulte [Configurar uma alocação](/pt-br/guides/allocations/setup/configure-an-allocation/).

## Custo não alocado

O custo não alocado é....

## Superalocação de custo

A superalocação de custo ocorre quando você acaba com mais custo na saída...

## Alocação incorreta de custo

A alocação incorreta de custos acontece quando...
