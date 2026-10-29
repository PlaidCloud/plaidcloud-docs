---
title: Conector REST do Stripe
description: Configure uma conexão com a API REST do Stripe no PlaidCloud para integrar dados de processamento de pagamentos e financeiros aos seus fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/stripe.md
---

## Documentação da API
A [referência da API do fornecedor](https://docs.stripe.com/api) cobre os endpoints deste conector.

## Configuração

Estes campos aparecem ao criar ou editar esta conexão. Quais são obrigatórios ou opcionais depende das opções de autenticação que você ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| Alias | Texto (várias linhas) | Alias ou observações opcionais sobre a conexão. |
| Está ativa | Alternância | Indica se a conexão está ativada. Desative para pausá-la sem excluí-la. |

### Outros

| Campo | Tipo | Descrição |
|---|---|---|
| Host | Texto | — |
| Tipo de autenticação | Seleção | — |
| Ativar verificação SSL | Alternância | — |
| Seguir redirecionamentos | Alternância | — |
| Seguir método HTTP no redirecionamento | Alternância | — |
| Seguir autenticação no redirecionamento | Alternância | — |
| Remover referer no redirecionamento | Alternância | — |
| HTTP estrito | Alternância | — |
| Codificar URL | Alternância | Endpoint de URL. |
| Desativar cookie jar | Alternância | — |
| Cifra do servidor | Alternância | — |
| Máximo de redirecionamentos | Número | — |
| Endpoint de teste | Texto | — |
| Método de teste | Seleção | — |
