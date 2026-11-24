---
title: Trilha de aprendizagem de Modelagem
description: O que ler antes dos laboratórios Profissional e Especialista de Modelagem do PlaidCloud e o que cada laboratório pede que você faça.
sidebar:
  label: Modelagem
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/modeling.md
---

A trilha de Modelagem trata de dimensões e alocações: construir hierarquias, distribuir custos por direcionadores e provar que os resultados batem. Comece pela trilha de aprendizagem de [Fundamentos](/pt-br/guides/certification/foundations/). Para saber como os laboratórios funcionam, consulte [Certificação PlaidCloud](/pt-br/guides/certification/).

## Profissional

### Leia nesta ordem

1. [Introdução às dimensões](/pt-br/guides/dimensions/getting-started/)
2. [Gerenciar hierarquias](/pt-br/guides/projects/managing-hierarchies/)
3. [Projete uma hierarquia de dimensão](/pt-br/get-started/tutorials/design-a-dimension/)
4. [Início rápido de alocações](/pt-br/guides/allocations/getting-started/allocations-quick-start/)
5. [Etapa Allocation Split](/pt-br/reference/workflow-steps/allocation/allocation-split/)
6. [Crie um modelo de alocação](/pt-br/get-started/tutorials/build-an-allocation/)
7. [Resultados da alocação](/pt-br/guides/allocations/results/allocation-results/)
8. [Ver o log do fluxo de trabalho](/pt-br/guides/workflows/viewing-workflow-log/)

### O que o laboratório pede

O laboratório se chama *Modelação: alocar o custo partilhado de TI*.

Uma tabela lista cada departamento e o departamento superior dele. Você constrói uma dimensão cuja hierarquia principal é exatamente essa árvore. Em seguida, no fluxo de trabalho do laboratório, você aloca um conjunto de custos aos departamentos em proporção ao número de funcionários, com uma linha de resultado por departamento. Há também uma segunda tabela de direcionadores, que não é o direcionador para este conjunto.

O laboratório verifica se o fluxo de trabalho é executado, se a hierarquia está certa, se o total alocado bate com a origem e se cada departamento recebe o valor certo.

## Especialista

O laboratório Especialista tem tempo limitado: você tem 4 horas a partir do momento em que o inicia.

### Leia nesta ordem

1. [Configurar uma alocação](/pt-br/guides/allocations/setup/configure-an-allocation/)
2. [Solução de problemas de alocações](/pt-br/guides/allocations/results/troubleshooting-allocations/)
3. [Rastreando alocações com um agente de IA conectado por MCP](/pt-br/integrations/ai-coding-agents/tracing-allocations/)
4. [Resultados da alocação](/pt-br/guides/allocations/results/allocation-results/)
5. [Testar um E se de direcionador](/pt-br/guides/allocations/results/driver-what-if/)
6. [Gerenciar hierarquias](/pt-br/guides/projects/managing-hierarchies/)

### O que o laboratório pede

O laboratório se chama *Modelação Especialista: reparar o modelo de alocação*.

Um modelo de alocação em dois estágios deixou de bater com o razão, e alguns departamentos estão claramente errados. Você rastreia a causa e corrige o modelo: cada estágio aloca exatamente o seu conjunto, os totais dos departamentos estão certos e somam o razão, e a dimensão de departamentos contém apenas os departamentos que existem. Nenhuma linha de balanceamento pode ser usada para fazer algo bater. Em seguida, você adiciona uma etapa que mostra quanto a TI custaria a cada departamento se fosse alocada por área em vez de por número de funcionários.

O laboratório verifica se o fluxo de trabalho é executado, se a hierarquia está certa, se cada estágio e os totais dos departamentos batem com o razão, se cada departamento recebe o total certo e se o cenário de área está certo.
