---
title: Conector Workday REST
description: Configure uma conexão da API REST do Workday no PlaidCloud para integrar dados de RH, finanças e planejamento aos seus fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday.md
---

## Documentação da API
A [referência da API do fornecedor](https://community.workday.com/sites/default/files/file-hosting/restapi/) cobre os endpoints deste conector.

## Configuração

Estes campos aparecem ao criar ou editar esta conexão. Se são obrigatórios ou opcionais depende das opções de autenticação que você ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| Alias | Texto (várias linhas) | Alias ou observações opcionais sobre a conexão. |
| Está ativa | Alternância | Indica se a conexão está ativada. Desative para pausar sem excluir. |
| Banco de dados somente leitura | Alternância | Restringe a conexão a operações somente de leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta conexão: somente leitura, somente gravação ou leitura e gravação. |

### Outros

| Campo | Tipo | Descrição |
|---|---|---|
| ID do cliente OAuth2 | Texto | — |
| Segredo do cliente OAuth2 | Texto | Credencial secreta, armazenada com criptografia. |
| URL do Workday | Texto | Endpoint de URL. |
| Token de atualização OAuth2 | Texto | — |
