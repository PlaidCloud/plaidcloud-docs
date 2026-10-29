---
title: Conector Xero REST
description: Configure uma conexão do Xero no PlaidCloud com uma concessão OAuth de um clique, importe entidades da Accounting API e lance diários manuais, faturas, contas a pagar, pagamentos e notas de crédito.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/xero.md
---

## Documentação da API

A [referência da Accounting API](https://developer.xero.com/documentation/api/accounting/overview) do Xero documenta as entidades, os filtros `where=` e os payloads de criação que este conector usa.

## Como a Autenticação Funciona

A conexão se autentica com a concessão **OAuth 2.0** do Xero. O próprio PlaidCloud registra o aplicativo OAuth; por isso, não há ID de cliente nem segredo de cliente para obter ou informar: você clica em **Conectar ao Xero**, entra no Xero e aprova a concessão. O PlaidCloud armazena os tokens resultantes na conexão e os atualiza para você, gravando cada token de atualização rotacionado para que uma conexão ociosa por muito tempo continue funcionando.

Uma concessão cobre todas as organizações do Xero para as quais você a aprovar. A conexão tem como destino exatamente uma delas: o seletor **Organização** lista as organizações retornadas pela concessão, e cada solicitação carrega o ID de tenant dessa organização. Para ler ou lançar em uma segunda organização, crie uma segunda conexão do Xero e escolha essa organização nela.

A Demo Company do Xero é uma propriedade da organização, não uma configuração da conexão: uma organização de demonstração aparece na lista **Organização** como qualquer outra, de modo que uma conexão de sandbox é aquela que aponta para ela.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| Conectar ao Xero | Botão | Inicia o fluxo de login e consentimento do Xero. |
| Status da conexão | Status | Mostra `Not connected` até a concessão ser concluída e, depois, informa quantas organizações ela cobre. |
| Organização | Seleção | A organização do Xero em que esta conexão lê e lança. Preenchida a partir da concessão. |

## Limites de Taxa

O Xero limita cada organização a 60 chamadas por minuto e 5.000 chamadas por dia, com um teto de 5 chamadas simultâneas. O PlaidCloud controla os limites por minuto e de simultaneidade por conexão; assim, a limitação de uma organização nunca trava as chamadas de outra conexão, e respeita o `Retry-After` do Xero em uma resposta limitada. O limite diário fica sob sua responsabilidade: agende extrações amplas em vez de executar muitas ao mesmo tempo.

## Entidades Disponíveis para Importação

A etapa **Xero: Importar entidade** cobre onze entidades da Accounting API: `accounts`, `contacts`, `invoices`, `credit_notes`, `payments`, `manual_journals`, `bank_transactions`, `items`, `tracking_categories`, `tax_rates` e `currencies`. Cada extração aceita um filtro opcional de status, um intervalo de datas e uma data limite de modificação. Consulte [Xero: Importar entidade](/pt-br/reference/workflow-steps/xero/import-xero-entity/) para ver a referência completa dos campos.

## Lançando Documentos

A etapa **Xero: Lançar documento** lança diários manuais, faturas, contas a pagar, pagamentos e notas de crédito pelo pipeline compartilhado de gravação em ERP do PlaidCloud, a partir de uma tabela de cabeçalho e uma tabela de linhas. Consulte [Xero: Lançar documento](/pt-br/reference/workflow-steps/xero/xero-post/) para ver a referência dos campos e [Conectar ao Xero](/pt-br/guides/connections/xero/) para ver o passo a passo completo de lançamento.

## Limitações Conhecidas

| Limitação | O que significa |
|---|---|
| Diários manuais e pagamentos não podem ser consultados após um resultado ambíguo | Faturas, contas a pagar e notas de crédito carregam um número de documento que o PlaidCloud grava e pode consultar de volta. A narração de um diário manual e a referência de um pagamento não são consultáveis; por isso, uma gravação incerta de qualquer um dos dois é colocada em quarentena para você resolver no Xero, em vez de ser adivinhada. |
| O estorno cobre apenas diários manuais e faturas | Um diário manual é estornado como um diário com débito e crédito invertidos; uma fatura é estornada como uma nota de crédito espelhada. Contas a pagar, pagamentos e notas de crédito não têm payload de desfazer documentado; por isso, o PlaidCloud recusa o estorno em vez de inventar um. |
| Os filtros são campos fixos, não uma linguagem de consulta | A API de consulta do Xero expõe um filtro de status e um intervalo de datas por entidade, não uma linguagem de filtro aberta; por isso, a etapa de importação oferece esses campos em vez de uma tabela de campo, operador e valor. |
| Uma organização por conexão | Cada solicitação carrega um único ID de tenant. Uma segunda organização exige uma segunda conexão. |

## Relacionados

- [Conectar ao Xero (guia)](/pt-br/guides/connections/xero/): passo a passo para criar a conexão, testá-la, importar uma entidade e lançar um documento.
- [Xero: Importar entidade](/pt-br/reference/workflow-steps/xero/import-xero-entity/)
- [Xero: Lançar documento](/pt-br/reference/workflow-steps/xero/xero-post/)
- [Revisar o Histórico de Lançamentos em ERP](/pt-br/guides/connections/erp-post-history/)
