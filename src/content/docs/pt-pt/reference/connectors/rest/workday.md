---
title: Conector Workday REST
description: Configure uma ligação à API REST do Workday no PlaidCloud para integrar dados de RH, finanças e planeamento nos seus fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday.md
---

## Documentação da API
A [referência da API do fornecedor](https://community.workday.com/sites/default/files/file-hosting/restapi/) abrange os pontos de acesso deste conector.

## Configuração

Estes campos aparecem ao criar ou editar esta ligação. A obrigatoriedade de cada um depende das opções de autenticação que ativar.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome a apresentar para esta ligação. |
| Alias | Texto (várias linhas) | Alias ou notas opcionais sobre a ligação. |
| Está ativa | Comutador | Indica se a ligação está ativada. Desative-a para a pausar sem a eliminar. |
| Base de dados só de leitura | Comutador | Restringe a ligação a operações de leitura. |
| Tipo de acesso | Seleção | Nível de acesso desta ligação: só de leitura, só de escrita ou leitura e escrita. |

### Outros

| Campo | Tipo | Descrição |
|---|---|---|
| ID de cliente OAuth2 | Texto | — |
| Segredo de cliente OAuth2 | Texto | Credencial secreta, armazenada de forma cifrada. |
| URL do Workday | Texto | Ponto de acesso por URL. |
| Token de atualização OAuth2 | Texto | — |
