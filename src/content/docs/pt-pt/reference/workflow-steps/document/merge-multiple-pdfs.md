---
title: Merge Multiple PDFs (passo)
description: Combine vários ficheiros PDF num único documento num passo de fluxo de trabalho PlaidCloud, para montagem e consolidação de relatórios.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/merge-multiple-pdfs.md
---

Junta os PDF de uma pasta num único PDF. Ao contrário de [Concatenar ficheiros](/pt-pt/reference/workflow-steps/document/concatenate-files/), este passo compreende o formato PDF e produz um documento combinado válido.

## Entradas

- **Diretório de entrada** — a pasta cujos PDF são combinados, numa conta de documentos. Pode indicar-se, em alternativa, um único arquivo, como um ZIP de PDF, e os PDF que contém são combinados.
- **Ficheiro combinado de saída** — onde o PDF combinado é escrito.

## Como funciona

- Os PDF são combinados pela ordem do respetivo caminho, com os números considerados pelo valor — `page2.pdf` vem antes de `page10.pdf` — pelo que deve numerá-los para controlar a ordem. Cada um mantém as suas próprias páginas pela mesma ordem.
- Apenas os ficheiros com o nome `.pdf` são combinados. Tudo o resto na pasta é excluído, e um arquivo na pasta não é aberto.
- Os ficheiros em subpastas são incluídos quando a conta de documentos os lista: as contas S3, Wasabi e Google Cloud Storage listam toda a árvore de pastas, enquanto as contas OneDrive, SFTP e Azure listam apenas o nível superior.
- São combinados no máximo 100 PDF; um número superior faz o passo falhar.

## Saída

Um único PDF no caminho de saída, com todas as páginas de todos os PDF combinados.

## Notas

- Uma pasta sem PDF, ou que não existe, termina o passo com um aviso que indica a pasta e não combina nada, e o fluxo de trabalho continua.
- O caminho de saída não pode ser o caminho de entrada.

## Utilizações comuns

- Montar relatórios mensais a partir de PDF de relatórios individuais
- Combinar uma folha de rosto, o corpo e os anexos num único documento a entregar
- Reunir faturas geradas num arquivo por cliente ou por período

## Relacionado

- [Compress PDF (passo)](/pt-pt/reference/workflow-steps/document/compress-pdf/) — reduz o resultado combinado
- [Convert image to PDF](/pt-pt/reference/workflow-steps/document/convert-image-to-pdf/) — transforma imagens em PDF antes de as combinar
