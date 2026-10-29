---
title: Convert Document Encoding
description: Converta a codificação de ficheiros de documento entre conjuntos de carateres num passo de fluxo de trabalho do PlaidCloud, para resolver problemas de compatibilidade de codificação.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding.md
---

## Descrição



Recodifica um ficheiro de texto de uma codificação de carateres para outra. É útil quando os ficheiros de origem chegam em codificações antigas (Windows-1252, ISO-8859-1), mas as ferramentas a jusante precisam de UTF-8, ou vice-versa.

Quando o ficheiro de origem não é UTF-8, a sua codificação é determinada a partir do conteúdo do ficheiro. Um ficheiro muito curto ou muito repetitivo oferece pouca informação e pode ser lido incorretamente, por isso verifique a saída convertida de um ficheiro assim.

Um caráter que a codificação de destino não consiga representar faz o passo falhar por predefinição. Selecione **Substituir por ? os carateres que a codificação de destino não suporta** para escrever um `?` no seu lugar, como o faz um escritor Java, e o passo termina.

Escolha a codificação de destino na configuração do passo. Para atalhos de codificações específicas, consulte as variantes [UTF-8](/pt-pt/reference/workflow-steps/document/convert-document-encoding-to-utf-8/), [UTF-16](/pt-pt/reference/workflow-steps/document/convert-document-encoding-to-utf-16/) e [ASCII](/pt-pt/reference/workflow-steps/document/convert-document-encoding-to-ascii/).


## Exemplos


Crie uma origem de entrada, selecione o ficheiro de entrada e procure o ficheiro nessa localização. Selecione o local de saída pretendido e procure a localização pretendida para o ficheiro. Guarde e execute.
