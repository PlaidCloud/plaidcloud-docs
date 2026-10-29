---
title: Conector REST do Gusto
description: Configure uma conexão com a API REST do Gusto no PlaidCloud para integrar dados de folha de pagamento, benefícios e RH aos seus fluxos de trabalho de análise.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/gusto.md
---

## Documentação da API
A [referência da API do fornecedor](https://docs.gusto.com/app-integrations/reference/get-v1-token-info) cobre os endpoints deste conector.

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
