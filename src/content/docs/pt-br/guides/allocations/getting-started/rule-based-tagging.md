---
title: Marcação baseada em regras
description: Configure a marcação baseada em regras nas alocações do PlaidCloud para categorizar e rotular registros de dados automaticamente com critérios definidos.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/rule-based-tagging.md
---

A marcação baseada em regras permite marcar as linhas de origem com metadados que o mecanismo de alocação usa para decidir *para onde* essas linhas vão. Use-a quando o comportamento da alocação precisar variar por linha — por exemplo, quando os custos de um centro de custo devem ser distribuídos por número de funcionários, mas os de outro devem ser distribuídos por receita.

## Quando usar

- Uma regra de alocação fixa não reflete como o custo deveria realmente ser distribuído (regras diferentes para tipos de custo diferentes).
- Você quer direcionar certas linhas de origem para destinos específicos e deixar as demais serem distribuídas normalmente.
- Você está modelando uma alocação com vários pools, em que cada pool usa um direcionador diferente.

## Como a marcação funciona

1. **Marque a origem.** A tabela de valores recebe uma ou mais colunas de marcação que classificam cada linha.
2. **Faça referência às marcações na regra de alocação.** Ao configurar a etapa de alocação, você expressa as regras na forma *"se a marcação de origem X = valor Y, aloque usando o direcionador D e a dimensão de destino T."*
3. **O mecanismo encaminha as linhas.** Cada linha de origem é comparada com as regras em ordem; a primeira regra correspondente decide o comportamento da alocação.

## Padrões de origem adequados à marcação

- Uma coluna chamada `cost_category` com valores como `payroll`, `facilities`, `it`, `marketing`
- Uma coluna chamada `pool` que nomeia o pool de alocação a que a linha pertence
- Uma coluna booleana como `is_overhead` que aciona um tratamento diferente

## Exemplo

Uma tabela de custos com `cost_center` e `cost_category`:

| cost_center | cost_category | amount |
|---|---|---|
| 1010 | payroll | 50,000 |
| 1010 | it | 8,000 |
| 1020 | payroll | 35,000 |

Você pode configurar duas regras de alocação:

- **Linhas de folha de pagamento** distribuídas pelo direcionador de número de funcionários
- **Linhas de TI** distribuídas pelo direcionador de número de usuários

As duas regras são executadas sobre a mesma tabela de origem; as marcações decidem qual se aplica a cada linha.

## Relacionados

- [Início rápido de alocações](/pt-br/guides/allocations/getting-started/allocations-quick-start/) — o fluxo básico antes de adicionar a marcação
- [Configure uma alocação](/pt-br/guides/allocations/setup/configure-an-allocation/) — referência completa da etapa
- [Etapa Allocation Rules](/pt-br/reference/workflow-steps/allocation/allocation-rules/) — etapa de fluxo de trabalho que consome dados marcados
