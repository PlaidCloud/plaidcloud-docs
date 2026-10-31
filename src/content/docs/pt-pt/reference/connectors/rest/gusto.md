---
title: Conector REST Gusto
description: Configure uma ligação à API REST do Gusto no PlaidCloud para integrar dados de processamento salarial, benefícios e recursos humanos nos seus fluxos de trabalho de análise.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/gusto.md
---

## Documentação da API
A [referência da API do fornecedor](https://docs.gusto.com/app-integrations/reference/get-v1-token-info) abrange os pontos de acesso deste conector.

## Configuração

Estes campos aparecem ao criar ou editar esta ligação. Os campos obrigatórios e opcionais dependem das opções de autenticação que ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| Alias | Texto (várias linhas) | Alias ou notas opcionais sobre a ligação. |
| Está ativa | Comutador | Indica se a ligação está ativada. Desative para a suspender sem a eliminar. |

### Outros

| Campo | Tipo | Descrição |
|---|---|---|
| Anfitrião | Texto | — |
| Tipo de autenticação | Seleção | — |
| Ativar verificação SSL | Comutador | — |
| Seguir redirecionamentos | Comutador | — |
| Seguir redirecionamentos HTTP | Comutador | — |
| Seguir redirecionamentos de autenticação | Comutador | — |
| Remover referer no redirecionamento | Comutador | — |
| HTTP estrito | Comutador | — |
| Codificar URL | Comutador | Ponto de acesso URL. |
| Desativar o repositório de cookies | Comutador | — |
| Cifra do servidor | Comutador | — |
| Máximo de redirecionamentos | Número | — |
| Ponto de acesso de teste | Texto | — |
| Método de teste | Seleção | — |
