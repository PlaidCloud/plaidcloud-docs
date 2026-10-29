---
title: Executar operação da aplicação
description: Invoque a partir de um fluxo de trabalho uma operação de aplicação registada, transmitindo opcionalmente um caminho de documento e parâmetros.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/run-script.md
---

## Descrição

Invoca uma operação de aplicação registada a partir de um fluxo de trabalho. Utilize-o para acionar trabalho da plataforma que não é uma transformação de dados — as operações que uma aplicação expõe para automação.

## Configuração

### Operação da aplicação a executar

A operação a invocar.

### Caminho do ficheiro

Para operações que recebem um ficheiro:

- **Document directory** — a conta de documentos e o caminho a transmitir.
- **File parameter name** — o parâmetro sob o qual a operação espera o caminho. A predefinição é `document_path`; altere-o apenas se a operação lhe der outro nome.

### Parâmetros opcionais

Pares nome/valor transmitidos à operação juntamente com o caminho do ficheiro.

## Relacionados

- [Passos gerais](/pt-pt/reference/workflow-steps/general/)
- [User Defined Transform](/pt-pt/reference/workflow-steps/general/user-defined-transform/)
- [Run Remote Python](/pt-pt/reference/workflow-steps/general/run-remote-python/)
