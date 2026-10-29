---
title: Merge Multiple PDFs
description: Mescle vários arquivos PDF em um único documento combinado em uma etapa de fluxo de trabalho do PlaidCloud, para montagem e consolidação de relatórios.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/merge-multiple-pdfs.md
---

Une os PDFs de uma pasta em um único PDF. Ao contrário de [Concatenate files](/pt-br/reference/workflow-steps/document/concatenate-files/), esta etapa entende o formato PDF e produz um documento mesclado válido.

## Entradas

- **Diretório de entrada** — a pasta cujos PDFs são mesclados, em uma conta de documentos. Em vez disso, pode-se informar um único arquivo compactado, como um ZIP de PDFs, e os PDFs dentro dele são mesclados.
- **Arquivo mesclado de saída** — onde o PDF mesclado é gravado.

## Como funciona

- Os PDFs são mesclados na ordem do caminho, com os números tomados pelo valor (`page2.pdf` vem antes de `page10.pdf`), portanto numere-os para controlar a ordem. Cada um mantém suas próprias páginas em ordem.
- Somente arquivos com nome `.pdf` são mesclados. Qualquer outra coisa na pasta fica de fora, e um arquivo compactado na pasta não é aberto.
- Os arquivos em subpastas são incluídos quando a conta de documentos os lista: as contas S3, Wasabi e Google Cloud Storage listam toda a árvore de pastas, enquanto as contas OneDrive, SFTP e Azure listam apenas o nível superior.
- No máximo 100 PDFs são mesclados; mais que isso faz a etapa falhar.

## Saída

Um único PDF no caminho de saída, com todas as páginas de todos os PDFs mesclados.

## Observações

- Uma pasta sem PDFs, ou que não existe, faz a etapa terminar com um aviso que informa a pasta e não mescla nada, e o fluxo de trabalho continua.
- O caminho de saída não pode ser o caminho de entrada.

## Usos comuns

- Montar relatórios mensais a partir de PDFs de relatórios individuais
- Combinar uma capa, o corpo e os apêndices em uma única entrega
- Agrupar faturas geradas em um arquivo por cliente ou por período

## Relacionados

- [Compress PDF](/pt-br/reference/workflow-steps/document/compress-pdf/) — reduz o resultado mesclado
- [Convert image to PDF](/pt-br/reference/workflow-steps/document/convert-image-to-pdf/) — transforma imagens em PDFs antes de mesclar
