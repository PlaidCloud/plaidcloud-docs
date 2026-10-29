---
title: Solver
description: Resolva problemas de otimização LP e MIP a partir de dados de tabelas de fluxo de trabalho.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/solver.md
---

A etapa Solver resolve problemas de programação linear e de programação inteira mista a partir de tabelas do PlaidCloud. Use-a quando um fluxo de trabalho precisar escolher valores que minimizem ou maximizem um objetivo atendendo a restrições lineares.

O Solver é executado em um pod de job de fluxo de trabalho e grava os resultados de volta em tabelas do projeto.

## Entradas

Configure quatro tabelas de entrada. Cada entrada tem uma tabela de origem, um mapeamento de dados e filtros. O PlaidCloud traduz essas configurações na consulta de banco de dados usada para ler cada entrada, de modo que a seleção acontece antes de o Solver receber as linhas.

### Variáveis

Uma linha por variável de decisão.

| Coluna | Descrição |
| --- | --- |
| `variable_id` | Nome exclusivo da variável usado pelas outras tabelas de entrada. |
| `lower_bound` | Valor mínimo. Deixe em branco para não ter limite inferior. |
| `upper_bound` | Valor máximo. Deixe em branco para não ter limite superior. |
| `type` | `continuous`, `integer` ou `binary`. As variáveis binárias usam os limites `0` e `1`. |

### Objetivo

Uma linha por variável com coeficiente de objetivo diferente de zero.

| Coluna | Descrição |
| --- | --- |
| `variable_id` | Variável da entrada Variáveis. |
| `coefficient` | Coeficiente do objetivo para essa variável. |

As variáveis ausentes desta tabela usam o coeficiente `0`.

### Restrições

Uma linha por restrição linear.

| Coluna | Descrição |
| --- | --- |
| `constraint_id` | Nome exclusivo da restrição usado pela entrada Coeficientes. |
| `lower_bound` | Atividade mínima permitida. Deixe em branco para não ter limite inferior. |
| `upper_bound` | Atividade máxima permitida. Deixe em branco para não ter limite superior. |

Defina o mesmo limite inferior e superior para uma restrição de igualdade.

### Coeficientes

Matriz esparsa de coeficientes de restrição.

| Coluna | Descrição |
| --- | --- |
| `constraint_id` | Restrição da entrada Restrições. |
| `variable_id` | Variável da entrada Variáveis. |
| `coefficient` | Coeficiente dessa variável nessa restrição. |

## Opções do solver

| Opção | Descrição |
| --- | --- |
| Direção do objetivo | Escolha Minimizar ou Maximizar. |
| Limite de tempo | Limite opcional de tempo de execução, em segundos. |
| Gap MIP | Gap MIP relativo opcional para problemas de programação inteira mista. |
| Ativar presolve | Permite que o solver simplifique o modelo antes de resolver. |
| Usar recursos personalizados | Define os núcleos de CPU e a memória do pod do job. |

## Saídas

O Solver grava três tabelas de saída.

### Tabela de solução

Contém uma linha por variável com o valor resolvido, os limites, o tipo da variável, o coeficiente do objetivo e o custo reduzido, quando disponível.

### Tabela de resultados das restrições

Contém uma linha por restrição com a atividade, os limites, a folga e o valor dual, quando disponível.

### Tabela de resumo

Contém uma linha com o status do solver, o valor do objetivo, o tempo de execução, o gap MIP, o limite dual MIP, a contagem de nós, a contagem de iterações, a contagem de variáveis e a contagem de restrições.

## Comportamento de status

Uma resolução ótima conclui a etapa com sucesso. Se o solver retornar uma solução utilizável com status não ótimo, a etapa termina com um aviso e ainda grava as tabelas de saída. Se nenhuma solução utilizável estiver disponível, a etapa falha com a mensagem de status do solver.
