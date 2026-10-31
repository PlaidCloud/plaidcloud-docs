---
title: Convert Document Encoding
description: Converta a codificação de um arquivo de documento entre conjuntos de caracteres em uma etapa de fluxo de trabalho do PlaidCloud para resolver problemas de compatibilidade de codificação.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding.md
---

## Descrição



Recodifica um arquivo de texto de uma codificação de caracteres para outra. É útil quando os arquivos de origem chegam em codificações legadas (Windows-1252, ISO-8859-1), mas as ferramentas downstream precisam de UTF-8, ou vice-versa.

Quando o arquivo de origem não é UTF-8, sua codificação é determinada a partir do conteúdo do arquivo. Um arquivo muito curto ou muito repetitivo oferece pouca informação e pode ser lido incorretamente, portanto confira a saída convertida de um arquivo assim.

Um caractere que a codificação de destino não consegue representar faz a etapa falhar por padrão. Selecione **Substituir por ? os caracteres que a codificação de destino não suporta** para gravar um `?` no lugar dele, como faz um gravador Java, e a etapa termina normalmente.

Escolha a codificação de destino na configuração da etapa. Para atalhos de codificações específicas, consulte as variantes [UTF-8](/pt-br/reference/workflow-steps/document/convert-document-encoding-to-utf-8/), [UTF-16](/pt-br/reference/workflow-steps/document/convert-document-encoding-to-utf-16/) e [ASCII](/pt-br/reference/workflow-steps/document/convert-document-encoding-to-ascii/).


## Exemplos


Crie uma entrada de origem, selecione o arquivo de entrada e procure o arquivo dentro desse local. Selecione o local de saída desejado e procure o local desejado para o arquivo. Salve e execute.
