---
title: Conector REST Ramp
description: Configure uma ligação à API REST do Ramp no PlaidCloud para integrar dados de despesas e gastos com cartões empresariais nos seus fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/ramp.md
---

## Documentação da API
A [referência da API do fornecedor](https://docs.ramp.com/developer-api/v1) abrange os pontos de acesso deste conector.

## Configuração

Estes campos aparecem ao criar ou editar esta ligação. Os campos obrigatórios e opcionais dependem das opções de autenticação que ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| Alias | Texto (várias linhas) | Alias ou notas opcionais sobre a ligação. |
| Está ativa | Comutador | Indica se a ligação está ativada. Desative para a suspender sem a eliminar. |
| Só de leitura na BD | Comutador | Restringe a ligação a operações de leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta ligação: só de leitura, só de escrita ou de leitura e escrita. |

### Outros

| Campo | Tipo | Descrição |
|---|---|---|
| ID de cliente OAuth2 | Texto | — |
| Segredo de cliente OAuth2 | Texto | Credencial secreta — guardada cifrada. |
| Âmbito Ramp | Texto | — |
