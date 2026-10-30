---
title: Convert Document Encoding to UTF-16
description: Converta a codificação de um arquivo de documento para UTF-16 em uma etapa de fluxo de trabalho do PlaidCloud para oferecer suporte a conjuntos de caracteres multibyte e a texto Unicode.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-16.md
---

## Descrição

Reescreve um arquivo de texto em UTF-16. É útil quando um sistema downstream exige UTF-16 ou quando uma origem mistura codificações que outras ferramentas rejeitam.

## Entradas

- **Arquivo ou diretório de entrada** — o arquivo de texto, ou a pasta de arquivos de texto, a converter.
- **Destino** — onde o arquivo convertido é gravado.
- **Compactação** — Sem compactação, Zip, GZip ou BZip2 para a saída.
- **Endianness (ordem dos bytes)** — Little Endian ou Big Endian.
- **Include BOM** — marque para iniciar o arquivo com uma marca de ordem de bytes (`FF FE` para little-endian, `FE FF` para big-endian). Deixe desmarcado para não incluir a marca.

## Como funciona

- A codificação da origem é detectada. Um arquivo UTF-8 é lido como UTF-8, e caracteres do Windows colados nele — aspas curvas do Word ou do Excel, por exemplo — passam intactos, em qualquer quantidade. Um arquivo em outra codificação é lido na codificação detectada a partir da primeira parte dele que não é UTF-8 válido.
- O texto é gravado sem alterações — letras acentuadas, símbolos e outros caracteres passam exatamente como estavam.
- Um arquivo cuja codificação não pode ser detectada faz a etapa falhar, informando o arquivo.
- Se o caminho de entrada não existir ou não tiver arquivos, a etapa termina com um aviso que informa o caminho e não processa nada, e o fluxo de trabalho continua.
- No caso de uma pasta, cada arquivo é convertido e gravado no destino com o próprio nome. Os arquivos de subpastas são gravados no próprio destino, e não em subpastas correspondentes.

## Exemplos

Selecione o arquivo de entrada e procure o arquivo dentro desse local. Selecione o local de saída desejado, escolha a ordem dos bytes e marque **Include BOM** se o sistema receptor esperar uma marca. Salve e execute.
