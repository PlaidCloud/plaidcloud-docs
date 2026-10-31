---
title: Etiquetagem baseada em regras
description: Configure a etiquetagem baseada em regras nas alocações do PlaidCloud para categorizar e etiquetar automaticamente registos de dados com critérios definidos.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/rule-based-tagging.md
---

A etiquetagem baseada em regras permite-lhe marcar linhas de origem com metadados que o motor de alocação utiliza para decidir *para onde* essas linhas vão. Utilize-a quando precisar que o comportamento da alocação varie consoante a linha — por exemplo, quando os custos de um centro de custo devem ser repartidos por número de colaboradores, mas os de outro devem ser repartidos por receitas.

## Quando utilizar

- Uma regra de alocação uniforme não reflete a forma como o custo deve realmente ser repartido (regras diferentes para tipos de custo diferentes).
- Pretende encaminhar determinadas linhas de origem para destinos específicos, deixando as restantes repartir-se normalmente.
- Está a modelar uma alocação com vários conjuntos, em que cada conjunto utiliza um indutor diferente.

## Como funciona a etiquetagem

1. **Etiquete a origem.** A tabela de valores recebe uma ou mais colunas de etiquetas que classificam cada linha.
2. **Referencie as etiquetas na regra de alocação.** Ao configurar o passo de alocação, exprime as regras na forma *«se a etiqueta de origem X = valor Y, alocar com o indutor D e a dimensão de destino T.»*
3. **O motor encaminha as linhas.** Cada linha de origem é comparada com as regras por ordem; a primeira regra que corresponder decide o comportamento da alocação.

## Padrões de origem adequados à etiquetagem

- Uma coluna com o nome `cost_category` com valores como `payroll`, `facilities`, `it`, `marketing`
- Uma coluna com o nome `pool` que indica o conjunto de alocação a que a linha pertence
- Uma coluna booleana como `is_overhead` que desencadeia um tratamento diferente

## Exemplo

Uma tabela de custos com `cost_center` e `cost_category`:

| cost_center | cost_category | amount |
|---|---|---|
| 1010 | payroll | 50,000 |
| 1010 | it | 8,000 |
| 1020 | payroll | 35,000 |

Pode configurar duas regras de alocação:

- **As linhas de payroll** repartidas pelo indutor de número de colaboradores
- **As linhas de it** repartidas pelo indutor de número de utilizadores

Ambas as regras são executadas sobre a mesma tabela de origem; as etiquetas decidem qual se aplica a cada linha.

## Ligações relacionadas

- [Início rápido das alocações](/pt-pt/guides/allocations/getting-started/allocations-quick-start/) — o fluxo básico antes de adicionar etiquetagem
- [Configurar uma alocação](/pt-pt/guides/allocations/setup/configure-an-allocation/) — referência completa dos passos
- [Passo Allocation Rules](/pt-pt/reference/workflow-steps/allocation/allocation-rules/) — passo de fluxo de trabalho que consome dados etiquetados
