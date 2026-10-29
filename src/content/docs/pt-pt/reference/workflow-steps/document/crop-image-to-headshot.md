---
title: Crop Image to Headshot
description: Recorte imagens para um retrato quadrado num passo de fluxo de trabalho do PlaidCloud, para obter retratos normalizados em diretórios e crachás.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/crop-image-to-headshot.md
---

Recorta uma imagem para um quadrado centrado e redimensiona-a para um JPEG de 500 × 500 píxeis. É útil para normalizar diretórios de colaboradores ou de membros em que as fotografias de origem variam na proporção.

## Entradas

- **Ficheiro ou diretório de entrada** — uma imagem, ou uma pasta de imagens, numa conta de documentos.
- **Ficheiro ou diretório de saída** — onde o retrato é escrito.

## Saída

Um JPEG de 500 × 500 recortado a partir do centro da origem. No caso de uma pasta, o retrato de cada ficheiro é escrito numa pasta com o nome do caminho de saída, sem a extensão.

## Notas

- O recorte é feito a partir do centro da imagem; não procura um rosto, pelo que deve enquadrar as fotografias de origem com o motivo centrado.
- Um ficheiro que não possa ser lido como imagem é copiado para a saída sem alterações, em vez de fazer o passo falhar.
- Se o caminho de entrada não existir ou não tiver ficheiros, o passo termina com um aviso que indica o caminho e não processa nada, e o fluxo de trabalho continua.
- O caminho de saída não pode ser o caminho de entrada.

## Utilizações comuns

- Normalizar fotografias de diretórios de colaboradores
- Gerar imagens de avatar consistentes para um portal interno
- Recortar fotografias para crachás de identificação e credenciais

## Relacionado

- [Convert PDF or image to JPEG](/pt-pt/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Fix file extension](/pt-pt/reference/workflow-steps/document/fix-file-extension/)
