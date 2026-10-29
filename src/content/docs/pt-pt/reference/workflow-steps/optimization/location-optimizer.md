---
title: Otimizador de localização
description: Escolha K locais de entre um conjunto de candidatos que minimizem a distância total ou ponderada a um conjunto de pontos de procura.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/location-optimizer.md
---

O passo Otimizador de localização escolhe **K** locais de uma tabela de localizações candidatas que minimizem a distância total ou ponderada a uma tabela de pontos de procura — um modelo de localização de instalações p-mediana, resolvido como um programa inteiro misto no solver HiGHS do PlaidCloud.

O Otimizador de localização é executado num pod de tarefa do fluxo de trabalho, a mesma imagem de tarefa que o passo [Solver](/pt-pt/reference/workflow-steps/optimization/solver/) utiliza, e escreve os resultados em tabelas do projeto.

## Entradas

### Locais candidatos

A tabela de localizações possíveis, mapeada com o mesmo mapeamento de colunas de origem/destino, filtros e agregação que todas as entradas mapeadas por tabela utilizam.

### Pontos de procura

A tabela de pontos cuja distância ao local selecionado mais próximo é minimizada, mapeada da mesma forma.

### Tabela de distâncias (opcional)

Uma tabela pré-calculada de distâncias entre candidatos e pontos de procura. Deixe-a por definir para que o passo calcule as distâncias por si.

### K

O número de locais a selecionar de entre os Locais candidatos.

## Opções do solver

| Opção | Descrição |
| --- | --- |
| Limite de tempo | Limite opcional de tempo de execução, em segundos. |
| Folga MIP | Folga MIP relativa opcional. |
| Ativar pré-resolução | Permite que o solver simplifique o modelo antes de o resolver. Ativado por predefinição. |
| Utilizar recursos personalizados | Define os núcleos de CPU e a memória do pod da tarefa. |

Uma paragem por **Limite de tempo** ou **Folga MIP** devolve a melhor solução encontrada dentro desse limite em vez do verdadeiro ótimo — a mesma contrapartida que o [Solver](/pt-pt/reference/workflow-steps/optimization/solver/#comportamento-do-estado) faz num estado não ótimo. Deixe ambos por definir para resolver até à otimalidade total.

## Saídas

O Otimizador de localização escreve três tabelas de saída, que têm de ter todas nomes distintos.

### Tabela de saída dos locais selecionados

Uma linha por local escolhido.

### Tabela de saída das atribuições

Uma linha por ponto de procura, indicando o local selecionado ao qual foi atribuído.

### Tabela de saída do resumo

Uma linha com o estado do solver, o valor do objetivo e detalhes da execução.

## Limites e ressalvas

Este passo é um modelo de **p-mediana**: minimiza sempre a distância total (opcionalmente ponderada) dos pontos de procura ao local selecionado mais próximo. Não exprime uma pontuação ao estilo gravitacional, uma fórmula de pontuação personalizada nem qualquer objetivo em que uma pontuação mais alta seja melhor do que uma distância mais baixa. Um problema de seleção de locais que precise de algum destes pertence a um modelo [Solver](/pt-pt/reference/workflow-steps/optimization/solver/) construído à mão.

## Relacionado

- [Solver](/pt-pt/reference/workflow-steps/optimization/solver/): otimização linear e inteira mista geral, para um objetivo de seleção de locais que o modelo p-mediana fixo deste passo não cobre.
- [Matriz de conversão do Alteryx](/pt-pt/reference/alteryx-conversion-matrix/): a ferramenta Location Optimizer do Alteryx converte-se neste passo apenas no caso linear de minimização de distância; um núcleo gravitacional ou uma macro de pontuação personalizada continuam a ser recusados.
