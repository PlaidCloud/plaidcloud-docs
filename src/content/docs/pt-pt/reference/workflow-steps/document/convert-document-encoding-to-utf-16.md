---
title: Convert Document Encoding to UTF-16
description: Converta a codificação de um ficheiro de documento para UTF-16 num passo de fluxo de trabalho do PlaidCloud, para suportar conjuntos de carateres multibyte e texto Unicode.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-16.md
---

## Descrição

Reescreve um ficheiro de texto em UTF-16. É útil quando um sistema a jusante exige UTF-16 ou quando uma origem mistura codificações que outras ferramentas rejeitam.

## Entradas

- **Ficheiro ou diretório de entrada** — o ficheiro de texto, ou uma pasta de ficheiros de texto, a converter.
- **Destino** — onde o ficheiro convertido é escrito.
- **Compressão** — Sem compressão, Zip, GZip ou BZip2 para a saída.
- **Endianness (ordem dos bytes)** — Little Endian ou Big Endian.
- **Include BOM** — assinale para iniciar o ficheiro com uma marca de ordem de bytes (`FF FE` para little-endian, `FE FF` para big-endian). Deixe desassinalado para não incluir marca.

## Como funciona

- A codificação da origem é detetada. Um ficheiro UTF-8 é lido como UTF-8, e os carateres do Windows colados num ficheiro desses — aspas curvas do Word ou do Excel, por exemplo — passam intactos, por muitos que sejam. Um ficheiro noutra codificação é lido na codificação detetada a partir da primeira parte que não é UTF-8 válido.
- O texto é escrito sem alterações — letras acentuadas, símbolos e outros carateres passam exatamente como estavam.
- Um ficheiro cuja codificação não possa ser detetada faz o passo falhar, indicando o ficheiro.
- Se o caminho de entrada não existir ou não tiver ficheiros, o passo termina com um aviso que indica o caminho e não processa nada, e o fluxo de trabalho continua.
- No caso de uma pasta, cada ficheiro é convertido e escrito no destino com o seu próprio nome. Os ficheiros das subpastas são escritos no próprio destino, e não em subpastas correspondentes.

## Exemplos

Selecione o ficheiro de entrada e procure o ficheiro nessa localização. Selecione o local de saída pretendido, escolha a ordem dos bytes e assinale **Include BOM** se o sistema recetor esperar uma. Guarde e execute.
