---
title: Conector REST do QuickBooks
description: Configure uma conexão com a API REST do QuickBooks no PlaidCloud para integrar dados contábeis e financeiros aos seus fluxos de trabalho de análise.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/quickbooks.md
---

## Documentação da API
A [referência da API do fornecedor](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api) cobre os endpoints deste conector.

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
