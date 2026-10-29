---
title: Crop Image to Headshot
description: Recorte imagens em um retrato quadrado em uma etapa de fluxo de trabalho do PlaidCloud para padronizar retratos em diretórios e crachás.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/crop-image-to-headshot.md
---

Recorta uma imagem em um quadrado centralizado e a redimensiona para um JPEG de 500 × 500 pixels. É útil para normalizar diretórios de funcionários ou de membros em que as fotos de origem variam em proporção.

## Entradas

- **Arquivo ou diretório de entrada** — uma imagem, ou uma pasta de imagens, em uma conta de documentos.
- **Arquivo ou diretório de saída** — onde o retrato é gravado.

## Saída

Um JPEG de 500 × 500 recortado a partir do centro da origem. No caso de uma pasta, o retrato de cada arquivo é gravado em uma pasta com o nome do caminho de saída, sem a extensão.

## Observações

- O recorte é feito a partir do centro da imagem; a etapa não procura um rosto, portanto enquadre as fotos de origem com o assunto centralizado.
- Um arquivo que não pode ser lido como imagem é copiado para a saída sem alterações, em vez de fazer a etapa falhar.
- Se o caminho de entrada não existir ou não tiver arquivos, a etapa termina com um aviso que informa o caminho e não processa nada, e o fluxo de trabalho continua.
- O caminho de saída não pode ser o caminho de entrada.

## Usos comuns

- Padronizar as fotos do diretório de funcionários
- Gerar imagens de avatar consistentes para um portal interno
- Recortar fotos para crachás e credenciais

## Relacionados

- [Convert PDF or image to JPEG](/pt-br/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Fix file extension](/pt-br/reference/workflow-steps/document/fix-file-extension/)
