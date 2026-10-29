---
title: Início rápido de alocações
description: Configure rapidamente uma alocação de custos básica no PlaidCloud com este guia passo a passo sobre origens, direcionadores e mapeamento de destino.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/allocations-quick-start.md
---

Este passo a passo leva você dos dados brutos de custos até um modelo de alocação funcionando em cerca de 30 minutos.

## O que você vai precisar

- Um projeto com pelo menos duas tabelas:
  - **Valores a alocar** — os custos (ou receitas, ou volumes) que você quer distribuir. Uma linha por unidade de origem, com uma coluna para o valor.
  - **Dados do direcionador** — a base para a distribuição. Número de funcionários, metragem quadrada, contagem de transações, receita — seja o que for *pelo qual* você quer alocar.
- Uma dimensão que una origem e destino (centros de custo, departamentos, produtos — a taxonomia que se encaixar no seu modelo).

Se você ainda não tem tudo isso, os guias [Tabelas e visões](/pt-br/guides/data/) e [Dimensões](/pt-br/guides/dimensions/) explicam como carregar as entradas.

## Etapas

1. **Abra o projeto** que contém as suas tabelas de valores e de direcionadores.
2. **Crie um novo fluxo de trabalho.** As alocações sempre são executadas dentro de um fluxo de trabalho — elas não operam diretamente sobre tabelas fora de um.
3. **Adicione uma etapa de alocação.** Dentro do fluxo de trabalho, adicione uma etapa da categoria **Allocation**. O ponto de partida mais comum é **Allocation Rules**, para uma distribuição simples baseada em direcionador.
4. **Configure a origem.** Aponte a etapa para a sua tabela de valores e escolha a coluna que contém o valor a alocar.
5. **Configure o direcionador.** Aponte a etapa para a tabela de direcionadores e escolha a coluna que contém os valores do direcionador.
6. **Mapeie a dimensão.** Identifique qual coluna de cada tabela representa os membros da dimensão. A etapa de alocação usa essas colunas para associar as linhas de origem às linhas do direcionador.
7. **Execute a etapa.** A saída é uma nova tabela com uma linha por valor distribuído.
8. **Inspecione os resultados.** Confira se os totais correspondem ao esperado — a soma dos valores alocados deve ser igual à soma dos valores de origem (dentro da tolerância de arredondamento).

## Próximos passos comuns

- **Distribuição recursiva** — se um destino contém direcionadores para uma nova alocação, consulte [Alocações recursivas](/pt-br/guides/allocations/setup/recursive-allocations/).
- **Marcação de linhas para alocação** — para controlar *quais* linhas são alocadas para quais destinos, consulte [Marcação baseada em regras](/pt-br/guides/allocations/getting-started/rule-based-tagging/).
- **Investigação de resultados inesperados** — se os totais não conciliam ou linhas específicas parecem erradas, consulte [Solução de problemas de alocações](/pt-br/guides/allocations/results/troubleshooting-allocations/).

## Próximas etapas

- [Por que as alocações são úteis?](/pt-br/guides/allocations/getting-started/why-are-allocations-useful/) — quando usá-las
- [Configure uma alocação](/pt-br/guides/allocations/setup/configure-an-allocation/) — referência de configuração mais detalhada
- [Tipos de etapa de alocação](/pt-br/reference/workflow-steps/allocation/) — todas as etapas de fluxo de trabalho da categoria Allocation
