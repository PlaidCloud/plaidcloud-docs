---
title: Executar operação do aplicativo
description: Invoque uma operação de aplicativo registrada a partir de um fluxo de trabalho, opcionalmente passando um caminho de documento e parâmetros.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/run-script.md
---

## Descrição

Invoca uma operação de aplicativo registrada dentro de um fluxo de trabalho. Use-a para disparar trabalhos da plataforma que não são transformações de dados — as operações que um aplicativo expõe para automação.

## Configuração

### Operação do aplicativo a executar

A operação a invocar.

### Caminho do arquivo

Para operações que recebem um arquivo:

- **Document directory** — a conta de documentos e o caminho a passar.
- **File parameter name** — o parâmetro sob o qual a operação espera o caminho. O padrão é `document_path`; altere-o somente se a operação o nomear de forma diferente.

### Parâmetros opcionais

Pares nome/valor passados à operação junto com o caminho do arquivo.

## Relacionados

- [Etapas gerais](/pt-br/reference/workflow-steps/general/)
- [User Defined Transform (etapa)](/pt-br/reference/workflow-steps/general/user-defined-transform/)
- [Run Remote Python (etapa)](/pt-br/reference/workflow-steps/general/run-remote-python/)
