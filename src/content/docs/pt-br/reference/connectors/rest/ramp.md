---
title: Conector REST do Ramp
description: Configure uma conexão com a API REST do Ramp no PlaidCloud para integrar dados de gastos com cartão corporativo e de despesas aos seus fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/ramp.md
---

## Documentação da API
A [referência da API do fornecedor](https://docs.ramp.com/developer-api/v1) cobre os endpoints deste conector.

## Configuração

Estes campos aparecem ao criar ou editar esta conexão. Quais são obrigatórios ou opcionais depende das opções de autenticação que você ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| Alias | Texto (várias linhas) | Alias ou observações opcionais sobre a conexão. |
| Está ativa | Alternância | Indica se a conexão está ativada. Desative para pausá-la sem excluí-la. |
| Banco somente leitura | Alternância | Restringe a conexão a operações somente leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta conexão: somente leitura, somente gravação ou leitura e gravação. |

### Outros

| Campo | Tipo | Descrição |
|---|---|---|
| ID do cliente OAuth2 | Texto | — |
| Segredo do cliente OAuth2 | Texto | Credencial secreta, armazenada de forma criptografada. |
| Escopo do Ramp | Texto | — |
