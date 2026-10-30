---
title: Document Text Substitution (passo)
description: Execute substituições de texto (localizar e substituir) em documentos num passo de fluxo de trabalho PlaidCloud para transformação automática de conteúdo.
sidebar:
  order: 15
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-text-substitution.md
---

## Descrição

Localizar e substituir dentro de um ficheiro de texto. Substitua cadeias ou marcadores de posição específicos por novos valores — útil para modelos (substituir um marcador como `CUSTOMER_NAME` por um nome real) ou para higienizar texto (remover ou ocultar cadeias específicas).

Funciona com ficheiros de texto UTF-8 (TXT, CSV, JSON, XML, HTML, RML) de qualquer dimensão. Um ficheiro que não seja texto UTF-8, como um PDF ou um documento do Office, faz o passo falhar.

## Entradas

- **Ficheiro ou diretório de entrada** — o ficheiro, ou uma pasta de ficheiros, a alterar.
- **Ficheiro ou diretório de destino** — onde o resultado é escrito. O resultado é sempre escrito na conta de documentos da entrada; o destino define o caminho.
- **Compressão** — Sem compressão, Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO ou Deflate (zlib) para a saída. Snappy e LZ4 são escritos no formato de blocos lido pelo Spark e pelo Hadoop, e LZO como um ficheiro `lzop`.
- **Ordem das operações de substituição de texto** — uma linha por substituição, cada uma com o texto original e o respetivo substituto. É possível utilizar variáveis na substituição.

## Como funciona

- As substituições são executadas de cima para baixo e cada uma atua sobre o resultado das anteriores — pelo que uma substituição pode alterar texto colocado por uma linha anterior.
- A correspondência é exata e distingue maiúsculas de minúsculas, e todas as ocorrências são substituídas.
- Uma linha cujo texto original esteja vazio é ignorada.
- No caso de uma pasta, cada ficheiro é escrito numa pasta com o nome do destino, sem a extensão, com o nome do próprio ficheiro.
- Se o caminho de entrada não existir ou não tiver ficheiros, o passo termina com um aviso que indica o caminho e não processa nada, e o fluxo de trabalho continua.

## Exemplos

| Original | Substituição | `Dear CUSTOMER_NAME,` passa a |
|---|---|---|
| `CUSTOMER_NAME` | `Acme Ltd` | `Dear Acme Ltd,` |
