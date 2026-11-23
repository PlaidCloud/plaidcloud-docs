---
title: Percurso de aprendizagem de Modelação
description: O que ler antes dos laboratórios de Profissional e Especialista de Modelação da certificação PlaidCloud e o que cada laboratório pede.
sidebar:
  label: Modelação
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/modeling.md
---

O percurso de Modelação trata de dimensões e alocações: construir hierarquias, repartir custos por indutores e provar que os resultados batem certo. Comece pelo percurso de [Fundamentos](/pt-pt/guides/certification/foundations/). Para saber como funcionam os laboratórios, consulte [Certificação PlaidCloud](/pt-pt/guides/certification/).

## Profissional

### Leia por esta ordem

1. [Introdução às dimensões](/pt-pt/guides/dimensions/getting-started/)
2. [Gerir hierarquias](/pt-pt/guides/projects/managing-hierarchies/)
3. [Conceber uma hierarquia da dimensão](/pt-pt/get-started/tutorials/design-a-dimension/)
4. [Início rápido das alocações](/pt-pt/guides/allocations/getting-started/allocations-quick-start/)
5. [Allocation Split](/pt-pt/reference/workflow-steps/allocation/allocation-split/)
6. [Construir um modelo de alocação](/pt-pt/get-started/tutorials/build-an-allocation/)
7. [Resultados da alocação](/pt-pt/guides/allocations/results/allocation-results/)
8. [Ver o registo do fluxo de trabalho](/pt-pt/guides/workflows/viewing-workflow-log/)

### O que o laboratório pede

O laboratório chama-se *Modelação: alocar o custo partilhado de TI*.

Uma tabela lista cada departamento e o respetivo departamento superior. Constrói uma dimensão cuja hierarquia principal é exatamente essa árvore. Depois, no fluxo de trabalho do laboratório, aloca um conjunto de custos aos departamentos na proporção do respetivo número de colaboradores, com uma linha de resultado por departamento. Existe também uma segunda tabela de indutores, que não é o indutor para este conjunto.

O laboratório verifica se o fluxo de trabalho é executado, se a hierarquia está correta, se o total alocado bate certo com a origem e se cada departamento recebe o montante certo.

## Especialista

O laboratório de Especialista tem limite de tempo: dispõe de 4 horas a partir do momento em que o inicia.

### Leia por esta ordem

1. [Configurar uma alocação](/pt-pt/guides/allocations/setup/configure-an-allocation/)
2. [Resolução de problemas de alocações](/pt-pt/guides/allocations/results/troubleshooting-allocations/)
3. [Rastrear alocações com um agente de IA ligado por MCP](/pt-pt/integrations/ai-coding-agents/tracing-allocations/)
4. [Resultados da alocação](/pt-pt/guides/allocations/results/allocation-results/)
5. [Experimentar um cenário hipotético de indutor](/pt-pt/guides/allocations/results/driver-what-if/)
6. [Gerir hierarquias](/pt-pt/guides/projects/managing-hierarchies/)

### O que o laboratório pede

O laboratório chama-se *Modelação Especialista: reparar o modelo de alocação*.

Um modelo de alocação em duas fases deixou de bater certo com o razão, e alguns departamentos estão claramente errados. Rastreia a causa e corrige o modelo: cada fase aloca exatamente o seu conjunto, os totais dos departamentos estão certos e somam o valor do razão, e a dimensão de departamentos contém apenas os departamentos que existem. Não pode ser usada nenhuma linha de compensação para fazer algo bater certo. Depois adiciona um passo que mostra quanto custaria a TI a cada departamento se fosse alocada por área de piso em vez de por número de colaboradores.

O laboratório verifica se o fluxo de trabalho é executado, se a hierarquia está correta, se cada fase e os totais dos departamentos batem certo com o razão, se cada departamento recebe o total certo e se o cenário da área de piso está correto.
