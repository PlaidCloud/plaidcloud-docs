---
title: Export to XML
description: Exporte dados como ficheiros XML a partir de um passo de fluxo de trabalho do PlaidCloud, para intercâmbio de dados estruturados e integração de sistemas.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-xml.md
---

## Descrição

Escreve uma tabela de projeto do PlaidCloud numa conta de documentos como um ficheiro XML. Utilize-o quando os sistemas a jusante exigem XML como entrada — algo comum em integrações empresariais mais antigas, declarações oficiais ou formatos de intercâmbio de dados específicos de um setor.

A estrutura XML reflete a tabela: um elemento por linha e elementos filhos para cada coluna. Para ter mais controlo sobre a estrutura, utilize uma abordagem com modelo através de [Document Text Substitution](/pt-pt/reference/workflow-steps/document/document-text-substitution/) num ficheiro de modelo.

## Se o ficheiro existir

Em **Se o ficheiro existir**, **Um ficheiro que já existe** (`if_exists`) decide o que acontece quando o ficheiro já existe. **Sobrescrevê-lo** (`overwrite`, predefinição) substitui um ficheiro que já exista; **Fazer a etapa falhar sem escrever nada** (`fail`) interrompe o passo, sem escrever nada, quando já existe um ficheiro que seria escrito.
