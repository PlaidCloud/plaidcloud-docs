---
title: Convert Document Encoding to UTF-8
description: Converta a codificação de um ficheiro de documento para UTF-8 num passo de fluxo de trabalho do PlaidCloud, para ampla compatibilidade com sistemas e aplicações modernos.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-8.md
---

## Descrição

Reescreve um ficheiro de texto em UTF-8. É particularmente útil se a origem da informação tiver codificações mistas ou se outras ferramentas não suportarem determinadas codificações.

## Como funciona

- A codificação da origem é detetada. Um ficheiro UTF-8 é lido como UTF-8, e os carateres do Windows colados num ficheiro desses — aspas curvas do Word ou do Excel, por exemplo — passam intactos, por muitos que sejam. Um ficheiro noutra codificação é lido na codificação detetada a partir da primeira parte que não é UTF-8 válido.
- O texto é escrito sem alterações — letras acentuadas, símbolos e outros carateres passam exatamente como estavam.
- Um ficheiro cuja codificação não possa ser detetada faz o passo falhar, indicando o ficheiro.
- Se o caminho de entrada não existir ou não tiver ficheiros, o passo termina com um aviso que indica o caminho e não processa nada, e o fluxo de trabalho continua.

## Exemplos

Selecione o ficheiro de entrada e procure o ficheiro nessa localização. Selecione o local de saída pretendido e procure e selecione a localização pretendida para o ficheiro. Guarde e execute.
