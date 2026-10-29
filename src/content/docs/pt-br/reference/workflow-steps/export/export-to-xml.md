---
title: Export to XML (etapa)
description: Exporte dados como arquivos XML a partir de uma etapa de fluxo de trabalho do PlaidCloud, para intercâmbio de dados estruturados e integração de sistemas.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-xml.md
---

## Descrição

Grava uma tabela de projeto do PlaidCloud em uma conta de documentos como um arquivo XML. Use quando os sistemas downstream exigirem XML como entrada — comum em integrações corporativas mais antigas, declarações governamentais ou formatos específicos de intercâmbio de dados do setor.

A estrutura do XML espelha a tabela: um elemento por linha, com elementos filhos para cada coluna. Para ter mais controle sobre a estrutura, use uma abordagem baseada em modelo com [Document Text Substitution (etapa)](/pt-br/reference/workflow-steps/document/document-text-substitution/) sobre um arquivo de modelo.

## Se o arquivo existir

Em **Se o arquivo existir**, **Um arquivo que já existe** (`if_exists`) define o que acontece quando o arquivo já existe. **Sobrescrevê-lo** (`overwrite`, padrão) substitui um arquivo que já existe; **Fazer a etapa falhar sem gravar nada** (`fail`) interrompe a etapa, sem gravar nada, quando um arquivo que ela gravaria já existe.
