---
title: Aguardar
description: Adicione um atraso temporizado num passo de fluxo de trabalho do PlaidCloud para pausar a execução durante um período especificado antes de avançar para o passo seguinte.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/wait.md
---

## Descrição


A transformação Wait é utilizada para pausar o processamento durante um período especificado. Pode ser especialmente útil ao aguardar operações de E/S de outros sistemas ou para depurar fluxos de trabalho durante o desenvolvimento.



## Parâmetros de duração


Especifique um valor inteiro não negativo com o botão rotativo **Duração**.



Em seguida, especifique a unidade de tempo no menu pendente. Estão disponíveis para seleção as seguintes unidades:


* Segundos
* Minutos
* Horas

## Aguardar por uma hora ou um ficheiro

A secção **Outras esperas** tem estes campos. O passo aguarda por eles por esta ordem, depois da duração:

* **Milissegundos** (`milliseconds`) — milissegundos de espera adicionais à duração.
* **Até a hora do dia** (`until_time`) — depois, aguarda até que o relógio volte a marcar esta hora do dia, em UTC, no formato `HH:MM:SS`.
* **Aguardar um ficheiro** (`file`) — depois, aguarda que este ficheiro do Document, `{account, path}`, seja alterado. **Alteração do ficheiro** (`file_event`) é a alteração a aguardar: `modified` (predefinição), `created` ou `deleted`. O passo verifica **Verificar o ficheiro a cada (segundos)** (`poll_seconds`, predefinição 5) durante no máximo **Espera máxima do ficheiro (segundos)** (`max_wait_seconds`, predefinição 3600, no máximo um dia), terminando depois com um aviso e o fluxo de trabalho continua. Um ficheiro que já exista ao aguardar por `created` termina a espera de imediato, e um ficheiro em falta ao aguardar por `modified` ou `deleted` termina com um aviso que nomeia o caminho, sem aguardar.
