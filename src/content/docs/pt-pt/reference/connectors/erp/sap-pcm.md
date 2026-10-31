---
title: Conector SAP Profitability and Cost Management (PCM)
description: Configure uma ligação ao SAP Profitability and Cost Management no PlaidCloud para integrar dados de alocação de custos nos fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-pcm.md
---

## Documentação do fabricante
[A documentação legada do SAP PCM](https://help.sap.com/docs/SAP_PROFITABILITY_AND_COST_MANAGEMENT).

## Configuração

Estes campos aparecem ao criar ou editar esta ligação. A obrigatoriedade de cada campo depende das opções de autenticação que ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| Alias | Texto (várias linhas) | Alias ou notas opcionais sobre a ligação. |
| Está ativa | Interruptor | Indica se a ligação está ativada. Desative-a para a suspender sem a eliminar. |
| Db só de leitura | Interruptor | Restringe a ligação a operações de leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta ligação: só de leitura, só de escrita ou de leitura e escrita. |

### Autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| Utilizador da Db | Texto | Nome de utilizador para a autenticação na base de dados. |
| Usar SSO | Interruptor | Autentica através de início de sessão único em vez de nome de utilizador/palavra-passe. |
| Palavra-passe da Db | Palavra-passe | Palavra-passe para a autenticação na base de dados. |
