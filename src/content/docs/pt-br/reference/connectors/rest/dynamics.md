---
title: Conector REST do Microsoft Dynamics 365
description: Configure uma conexão com a API REST do Microsoft Dynamics no PlaidCloud para integrar dados de ERP e CRM aos seus fluxos de trabalho de análise.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics.md
---

## Documentação da API
A [referência da API do fornecedor](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) cobre os endpoints deste conector.

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
| Tenant do Dynamics | Texto | — |
| ID do cliente OAuth2 | Texto | — |
| Segredo do cliente OAuth2 | Texto | Credencial secreta, armazenada de forma criptografada. |
| CRM do Dynamics | Texto | — |
