---
title: Conector Xero REST
description: Configure uma ligação Xero no PlaidCloud com uma autorização OAuth num só clique, importe entidades da API Accounting e lance diários manuais, faturas, contas a pagar, pagamentos e notas de crédito.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/xero.md
---

## Documentação da API

A [referência da API Accounting](https://developer.xero.com/documentation/api/accounting/overview) do Xero documenta as entidades, os filtros `where=` e as estruturas de criação que este conector utiliza.

## Como funciona a autenticação

A ligação autentica-se com a autorização **OAuth 2.0** do Xero. O PlaidCloud regista a própria aplicação OAuth, pelo que não há ID de cliente nem segredo de cliente para obter ou introduzir: clique em **Ligar ao Xero**, inicie sessão no Xero e aprove a autorização. O PlaidCloud armazena na ligação os tokens resultantes e atualiza-os por si, guardando cada token de atualização rotativo para que uma ligação inativa durante muito tempo continue a funcionar.

Uma autorização abrange todas as organizações Xero para as quais a aprovar. A ligação tem como alvo exatamente uma delas: o seletor **Organização** lista as organizações devolvidas pela autorização e cada pedido inclui o ID de inquilino dessa organização. Para ler ou lançar numa segunda organização, crie uma segunda ligação Xero e escolha nela essa organização.

A Demo Company do Xero é uma propriedade da organização, não uma definição da ligação: uma organização de demonstração aparece na lista **Organização** como qualquer outra, pelo que uma ligação de sandbox é aquela que aponta para ela.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome a apresentar para esta ligação. |
| Ligar ao Xero | Botão | Inicia o fluxo de início de sessão e consentimento do Xero. |
| Estado da ligação | Estado | Indica `Not connected` até a autorização ser concluída e, depois, quantas organizações abrange. |
| Organização | Seleção | A organização Xero em que esta ligação lê e lança. Preenchida a partir da autorização. |

## Limites de taxa

O Xero limita cada organização a 60 chamadas por minuto e 5000 chamadas por dia, com um máximo de 5 chamadas em simultâneo. O PlaidCloud regula por ligação os limites por minuto e de simultaneidade, pelo que a limitação de uma organização nunca bloqueia as chamadas de outra ligação, e respeita o `Retry-After` do Xero numa resposta limitada. O limite diário fica à sua responsabilidade: agende as extrações grandes em vez de executar muitas ao mesmo tempo.

## Entidades disponíveis para importação

O passo **Xero: Importar entidade** abrange onze entidades da API Accounting: `accounts`, `contacts`, `invoices`, `credit_notes`, `payments`, `manual_journals`, `bank_transactions`, `items`, `tracking_categories`, `tax_rates` e `currencies`. Cada extração aceita uma restrição opcional por estado, um intervalo de datas e uma data-limite de modificação. Consulte [Xero: Importar entidade](/pt-pt/reference/workflow-steps/xero/import-xero-entity/) para a referência completa dos campos.

## Lançar documentos

O passo **Xero: Lançar documento** lança diários manuais, faturas, contas a pagar, pagamentos e notas de crédito através do circuito partilhado de escrita ERP do PlaidCloud, a partir de uma tabela de cabeçalhos e de uma tabela de linhas. Consulte [Xero: Lançar documento](/pt-pt/reference/workflow-steps/xero/xero-post/) para a referência dos campos e [Ligar ao Xero](/pt-pt/guides/connections/xero/) para o guia completo de lançamento.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| Os diários manuais e os pagamentos não podem ser consultados após um resultado ambíguo | As faturas, as contas a pagar e as notas de crédito têm um número de documento que o PlaidCloud atribui e que pode voltar a consultar. A narração de um diário manual e a referência de um pagamento não são consultáveis, pelo que uma escrita duvidosa de qualquer um deles fica em quarentena para que a resolva no Xero, em vez de ser adivinhada. |
| O estorno abrange apenas diários manuais e faturas | Um diário manual é estornado como um diário com débito e crédito trocados; uma fatura é estornada como uma nota de crédito espelhada. As contas a pagar, os pagamentos e as notas de crédito não têm estrutura de anulação documentada, pelo que o PlaidCloud recusa um estorno em vez de inventar um. |
| Os filtros são campos fixos, não uma linguagem de consulta | A API de consulta do Xero expõe, por entidade, uma restrição por estado e um intervalo de datas, e não uma linguagem de filtros aberta; por isso, o passo de importação oferece esses campos em vez de uma tabela de campo/operador/valor. |
| Uma organização por ligação | Cada pedido inclui um único ID de inquilino. Uma segunda organização requer uma segunda ligação. |

## Relacionado

- [Ligar ao Xero (guia)](/pt-pt/guides/connections/xero/): passo a passo para criar a ligação, testá-la, importar uma entidade e lançar um documento.
- [Xero: Importar entidade](/pt-pt/reference/workflow-steps/xero/import-xero-entity/)
- [Xero: Lançar documento](/pt-pt/reference/workflow-steps/xero/xero-post/)
- [Rever o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
