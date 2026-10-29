---
title: Conector Workday Financials
description: Configure uma ligação Workday Financials no PlaidCloud com um utilizador do sistema de integração para importar dados através de um relatório RaaS e lançar lançamentos de diário através de SOAP.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday-financials.md
---

## Documentação da API

Os [serviços web SOAP](https://community.workday.com/sites/default/files/file-hosting/productionapi/) e o [Report-as-a-Service (RaaS)](https://doc.workday.com/) do Workday documentam as interfaces que este conector utiliza.

## Como funciona a autenticação

A ligação autentica-se com um **utilizador do sistema de integração (ISU)**, um tipo de utilizador do Workday concebido para integração entre sistemas, protegido por um grupo de segurança do sistema de integração que lhe concede apenas o acesso de que este conector precisa (acesso a relatórios para leituras e o processo de negócio Submit Accounting Journal para lançamentos). Os pedidos incluem o nome de utilizador e a palavra-passe do ISU; não há início de sessão interativo.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome a apresentar para esta ligação. |
| Anfitrião do inquilino | Texto | O seu anfitrião Workday, por exemplo `wd5-impl.workday.com`. |
| Nome do inquilino | Texto | O nome do seu inquilino Workday. |
| Nome de utilizador do ISU | Texto | O nome de utilizador do utilizador do sistema de integração. |
| Palavra-passe do ISU | Texto | A palavra-passe do utilizador do sistema de integração. Armazenada de forma cifrada. |

## Importar dados

O Workday Financials não tem um conjunto fixo de entidades predefinidas. Em vez disso, o passo **Import Workday Entity** chama um **relatório Report-as-a-Service (RaaS)** que cria no Workday e publica com acesso a serviços web, e para o qual indica o URL. O passo suporta filtros em `company`, `ledger`, `period`, `accounting_date` (intervalo), `ledger_account` (intervalo) e `cost_center`, cada um transmitido como parâmetro do relatório, pelo que um filtro só funciona se o relatório definir um pedido correspondente. Consulte [Import Workday Entity](/pt-pt/reference/workflow-steps/workday-financials/import-workday-entity/) para a referência completa dos campos.

## Lançar lançamentos de diário

O passo **Workday Financials: Post Journal Entry** lança diários contabilísticos através do circuito partilhado de escrita ERP do PlaidCloud, utilizando a operação SOAP `Submit_Accounting_Journal` do Workday e consultando o estado do processo de negócio do lançamento até um estado terminal, antes de o comunicar como lançado. Uma correção lança um novo lançamento de estorno, com débito e crédito trocados, em vez de editar o original. Consulte [Workday Financials: Post Journal Entry](/pt-pt/reference/workflow-steps/workday-financials/workday-post/) para a referência dos campos e [Ligar ao Workday Financials](/pt-pt/guides/connections/workday-financials/) para o guia completo de lançamento.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| A forma da importação depende do seu relatório RaaS | O PlaidCloud não tem entidades predefinidas para o Workday Financials: os campos, os pedidos e o controlo de acesso do relatório residem todos no Workday. Uma alteração ao relatório aí pode alterar a forma da sua importação sem qualquer alteração do lado do PlaidCloud. |
| A aprovação do processo de negócio acrescenta latência | Um diário encaminhado por um passo de aprovação no seu processo de negócio Submit Accounting Journal mantém-se `pending` até ser aprovado no Workday; a consulta do estado terminal aguarda por isso. |
## Relacionado

- [Ligar ao Workday Financials (guia)](/pt-pt/guides/connections/workday-financials/): passo a passo para criar a ligação, testá-la, importar um relatório e lançar um diário.
- [Import Workday Entity](/pt-pt/reference/workflow-steps/workday-financials/import-workday-entity/)
- [Workday Financials: Post Journal Entry](/pt-pt/reference/workflow-steps/workday-financials/workday-post/)
- [Rever o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
- [Conector Workday REST](/pt-pt/reference/connectors/rest/workday/): o conector Workday genérico e independente para dados REST de RH/processamento salarial.
