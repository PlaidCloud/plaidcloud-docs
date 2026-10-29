---
title: Otimizador de localização
description: Escolha K locais de um conjunto de candidatos que minimizem a distância total ou ponderada até um conjunto de pontos de demanda.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/optimization/location-optimizer.md
---

A etapa Otimizador de localização escolhe **K** locais de uma tabela de localizações candidatas que minimizam a distância total ou ponderada até uma tabela de pontos de demanda: um modelo de localização de instalações p-mediana, resolvido como um programa inteiro misto no solver HiGHS do PlaidCloud.

O Otimizador de localização é executado em um pod de job de fluxo de trabalho, a mesma imagem de job que o [Solver](/pt-br/reference/workflow-steps/optimization/solver/) usa, e grava os resultados de volta em tabelas do projeto.

## Entradas

### Locais candidatos

A tabela de possíveis localizações de locais, mapeada com o mesmo mapeamento de colunas de origem/destino, filtros e agregação que toda entrada mapeada por tabela usa.

### Pontos de demanda

A tabela de pontos cuja distância até o local selecionado mais próximo é minimizada, mapeada da mesma forma.

### Tabela de distâncias (opcional)

Uma tabela pré-calculada de distâncias entre candidatos e demanda. Deixe sem definir para que a etapa calcule as distâncias por conta própria.

### K

O número de locais a selecionar entre os Locais candidatos.

## Opções do solver

| Opção | Descrição |
| --- | --- |
| Limite de tempo | Limite opcional de tempo de execução, em segundos. |
| Gap MIP | Gap MIP relativo opcional. |
| Ativar presolve | Permite que o solver simplifique o modelo antes de resolver. Ativado por padrão. |
| Usar recursos personalizados | Define os núcleos de CPU e a memória do pod do job. |

Uma interrupção por **Limite de tempo** ou **Gap MIP** retorna a melhor solução encontrada dentro desse limite, e não o ótimo verdadeiro, o mesmo compromisso que o [Solver](/pt-br/reference/workflow-steps/optimization/solver/#comportamento-de-status) faz com um status não ótimo. Deixe ambos sem definir para resolver até a otimalidade completa.

## Saídas

O Otimizador de localização grava três tabelas de saída, que devem ter nomes distintos.

### Tabela de saída de locais selecionados

Uma linha por local escolhido.

### Tabela de saída de atribuições

Uma linha por ponto de demanda, indicando o local selecionado ao qual ele foi atribuído.

### Tabela de saída de resumo

Uma linha com o status do solver, o valor do objetivo e detalhes da execução.

## Limites e ressalvas

Esta etapa é um modelo de **p-mediana**: ela sempre minimiza a distância total (opcionalmente ponderada) dos pontos de demanda até o local selecionado mais próximo. Ela não expressa uma pontuação no estilo gravitacional, uma fórmula de pontuação personalizada nem qualquer objetivo em que uma pontuação maior é melhor que uma distância menor. Um problema de seleção de locais que precise de algum desses casos pertence a um modelo do [Solver](/pt-br/reference/workflow-steps/optimization/solver/) montado manualmente.

## Relacionados

- [Solver](/pt-br/reference/workflow-steps/optimization/solver/): otimização linear e inteira mista geral, para um objetivo de seleção de locais que o modelo fixo de p-mediana desta etapa não cobre.
- [Matriz de conversão do Alteryx](/pt-br/reference/alteryx-conversion-matrix/): a ferramenta Location Optimizer do Alteryx é convertida para esta etapa somente no caso linear de minimização de distância; um kernel gravitacional ou uma macro de pontuação personalizada ainda é recusado.
