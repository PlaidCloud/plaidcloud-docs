---
title: Convert Document Encoding to UTF-8
description: Converta a codificação de um arquivo de documento para UTF-8 em uma etapa de fluxo de trabalho do PlaidCloud para ampla compatibilidade com sistemas e aplicativos modernos.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-8.md
---

## Descrição

Reescreve um arquivo de texto em UTF-8. É particularmente útil se a origem das informações tem codificações mistas ou se outras ferramentas não aceitam determinadas codificações.

## Como funciona

- A codificação da origem é detectada. Um arquivo UTF-8 é lido como UTF-8, e caracteres do Windows colados nele — aspas curvas do Word ou do Excel, por exemplo — passam intactos, em qualquer quantidade. Um arquivo em outra codificação é lido na codificação detectada a partir da primeira parte dele que não é UTF-8 válido.
- O texto é gravado sem alterações — letras acentuadas, símbolos e outros caracteres passam exatamente como estavam.
- Um arquivo cuja codificação não pode ser detectada faz a etapa falhar, informando o arquivo.
- Se o caminho de entrada não existir ou não tiver arquivos, a etapa termina com um aviso que informa o caminho e não processa nada, e o fluxo de trabalho continua.
- No caso de uma pasta, cada arquivo é convertido e gravado no destino com o próprio nome. Marque **Manter subpastas** para gravar um arquivo de uma subpasta na subpasta correspondente do destino; o conteúdo de um arquivo compactado vai então para a subpasta em que o arquivo compactado estava.
- Se dois arquivos fossem gravados no mesmo local do destino, a etapa falha antes de gravar o segundo, em vez de deixá-lo substituir o primeiro. A mensagem informa os dois arquivos, ou o arquivo compactado de que ambos vieram, e o local; se marcar **Manter subpastas** gravasse os dois em locais separados, ela também informa isso.

## Exemplos

Selecione o arquivo de entrada e procure o arquivo dentro desse local. Selecione o local de saída desejado e procure e selecione o local desejado para o arquivo. Salve e execute.
