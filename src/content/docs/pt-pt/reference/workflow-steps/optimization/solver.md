---
title: Solver
description: Resolva problemas de otimização LP e MIP a partir dos dados de tabelas do fluxo de trabalho.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/solver.md
---

O passo Solver resolve problemas de programação linear e de programação inteira mista a partir de tabelas do PlaidCloud. Utilize-o quando um fluxo de trabalho precisar de escolher valores que minimizem ou maximizem um objetivo, cumprindo restrições lineares.

O Solver é executado num pod de tarefa do fluxo de trabalho e escreve os resultados em tabelas do projeto.

## Entradas

Configure quatro tabelas de entrada. Cada entrada tem uma tabela de origem, um mapeamento de dados e filtros. O PlaidCloud traduz estas definições na consulta à base de dados utilizada para ler cada entrada, pelo que a seleção ocorre antes de o Solver receber as linhas.

### Variáveis

Uma linha por variável de decisão.

| Coluna | Descrição |
| --- | --- |
| `variable_id` | Nome único da variável, utilizado pelas outras tabelas de entrada. |
| `lower_bound` | Valor mínimo. Deixe em branco para não ter limite inferior. |
| `upper_bound` | Valor máximo. Deixe em branco para não ter limite superior. |
| `type` | `continuous`, `integer` ou `binary`. As variáveis binárias utilizam os limites `0` e `1`. |

### Objetivo

Uma linha por variável com um coeficiente de objetivo diferente de zero.

| Coluna | Descrição |
| --- | --- |
| `variable_id` | Variável da entrada Variáveis. |
| `coefficient` | Coeficiente do objetivo para essa variável. |

As variáveis em falta nesta tabela utilizam o coeficiente `0`.

### Restrições

Uma linha por restrição linear.

| Coluna | Descrição |
| --- | --- |
| `constraint_id` | Nome único da restrição, utilizado pela entrada Coeficientes. |
| `lower_bound` | Atividade mínima permitida. Deixe em branco para não ter limite inferior. |
| `upper_bound` | Atividade máxima permitida. Deixe em branco para não ter limite superior. |

Defina o mesmo limite inferior e superior para uma restrição de igualdade.

### Coeficientes

Matriz esparsa de coeficientes das restrições.

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
| Folga MIP | Folga MIP relativa opcional para problemas de programação inteira mista. |
| Ativar pré-resolução | Permite que o solver simplifique o modelo antes de o resolver. |
| Utilizar recursos personalizados | Define os núcleos de CPU e a memória do pod da tarefa. |

## Saídas

O Solver escreve três tabelas de saída.

### Tabela de solução

Contém uma linha por variável com o valor resolvido, os limites, o tipo de variável, o coeficiente do objetivo e o custo reduzido, quando disponível.

### Tabela de resultados das restrições

Contém uma linha por restrição com a atividade, os limites, a folga e o valor dual, quando disponível.

### Tabela de resumo

Contém uma linha com o estado do solver, o valor do objetivo, o tempo de execução, a folga MIP, o limite dual MIP, o número de nós, o número de iterações, o número de variáveis e o número de restrições.

## Comportamento do estado

Uma resolução ótima conclui o passo com êxito. Se o solver devolver uma solução utilizável com um estado não ótimo, o passo termina com um aviso e escreve na mesma as tabelas de saída. Se não houver nenhuma solução utilizável, o passo falha com a mensagem de estado do solver.
