---
title: Aguardar
description: Adicione um atraso cronometrado em uma etapa de fluxo de trabalho do PlaidCloud para pausar a execução por uma duração especificada antes de prosseguir para a próxima etapa.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/wait.md
---

## Descrição


A transformação Aguardar é usada para pausar o processamento por uma duração especificada. Isso pode ser especialmente útil ao esperar operações de E/S de outros sistemas ou para depurar fluxos de trabalho durante o desenvolvimento.



## Parâmetros de duração


Especifique um valor inteiro não negativo usando o seletor numérico **Duração**.



Em seguida, especifique a unidade de tempo no menu suspenso. As seguintes unidades estão disponíveis para seleção:


* Segundos
* Minutos
* Horas

## Aguardar um horário ou um arquivo

A seção **Outras esperas** tem estes campos. A etapa os aguarda nesta ordem, depois da duração:

* **Milissegundos** (`milliseconds`) — milissegundos aguardados além da duração.
* **Até a hora do dia** (`until_time`) — depois, espera até que o relógio marque este horário do dia, em UTC, no formato `HH:MM:SS`.
* **Aguardar um arquivo** (`file`) — depois, aguarda que este arquivo do Document, `{account, path}`, mude. **Alteração do arquivo** (`file_event`) é a alteração a aguardar: `modified` (padrão), `created` ou `deleted`. A etapa verifica a cada **Verificar o arquivo a cada (segundos)** (`poll_seconds`, padrão 5) por no máximo **Espera máxima do arquivo (segundos)** (`max_wait_seconds`, padrão 3600, no máximo um dia); depois termina com um aviso e o fluxo de trabalho continua. Um arquivo que já existe ao aguardar `created` encerra a espera imediatamente, e um arquivo ausente ao aguardar `modified` ou `deleted` termina com um aviso que nomeia o caminho, sem aguardar.
