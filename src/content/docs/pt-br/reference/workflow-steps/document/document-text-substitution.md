---
title: Document Text Substitution
description: Faça substituições de localizar e substituir texto em documentos em uma etapa de fluxo de trabalho do PlaidCloud para transformar o conteúdo de forma automatizada.
sidebar:
  order: 15
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-text-substitution.md
---

## Descrição

Localizar e substituir dentro de um arquivo de texto. Substitua cadeias de caracteres ou marcadores específicos por novos valores. É útil para criar modelos (trocar um marcador como `CUSTOMER_NAME` por um nome real) ou para higienizar texto (remover ou ocultar cadeias específicas).

Funciona com arquivos de texto UTF-8 (TXT, CSV, JSON, XML, HTML, RML) de qualquer tamanho. Um arquivo que não seja texto UTF-8, como um PDF ou um documento do Office, faz a etapa falhar.

## Entradas

- **Arquivo ou diretório de entrada** — o arquivo, ou uma pasta de arquivos, a ser alterado.
- **Arquivo ou diretório de destino** — onde o resultado é gravado. O resultado é sempre gravado na conta de documentos da entrada; o destino define o caminho.
- **Compactação** — Sem compactação, Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO ou Deflate (zlib) para a saída. Snappy e LZ4 são gravados no formato de bloco que o Spark e o Hadoop leem, e LZO como um arquivo `lzop`.
- **Ordem das operações de substituição de texto** — uma linha por substituição, cada uma com o texto original e sua substituição. É possível usar variáveis na substituição.

## Como funciona

- As substituições são executadas de cima para baixo, e cada uma atua sobre o resultado das anteriores, de modo que uma substituição pode alterar um texto colocado por uma linha anterior.
- A correspondência é exata e diferencia maiúsculas de minúsculas, e todas as ocorrências são substituídas.
- Uma linha cujo texto original esteja vazio é ignorada.
- No caso de uma pasta, cada arquivo é gravado em uma pasta com o nome do destino, sem a extensão, com o próprio nome do arquivo.
- Se o caminho de entrada não existir ou não tiver arquivos, a etapa termina com um aviso que informa o caminho e não processa nada, e o fluxo de trabalho continua.

## Exemplos

| Original | Substituição | `Dear CUSTOMER_NAME,` se torna |
|---|---|---|
| `CUSTOMER_NAME` | `Acme Ltd` | `Dear Acme Ltd,` |
