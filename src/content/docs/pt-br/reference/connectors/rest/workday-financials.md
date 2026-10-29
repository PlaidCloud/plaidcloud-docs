---
title: Conector Workday Financials
description: Configure uma conexão do Workday Financials no PlaidCloud com um Integration System User para importar dados por meio de um relatório RaaS e lançar lançamentos contábeis por SOAP.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/workday-financials.md
---

## Documentação da API

Os [serviços web SOAP](https://community.workday.com/sites/default/files/file-hosting/productionapi/) e o [Report-as-a-Service (RaaS)](https://doc.workday.com/) do Workday documentam as interfaces que este conector usa.

## Como a Autenticação Funciona

A conexão se autentica com um **Integration System User (ISU)**, um tipo de usuário do Workday criado para integração entre sistemas e protegido por um Integration System Security Group que concede apenas o acesso de que este conector precisa (acesso a relatórios para leituras e o processo de negócio Submit Accounting Journal para lançamentos). As solicitações carregam o nome de usuário e a senha do ISU; não há login interativo.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| Host do tenant | Texto | O host do seu Workday, por exemplo `wd5-impl.workday.com`. |
| Nome do tenant | Texto | O nome do seu tenant do Workday. |
| Nome de usuário do ISU | Texto | O nome de usuário do Integration System User. |
| Senha do ISU | Texto | A senha do Integration System User. Armazenada com criptografia. |

## Importando Dados

O Workday Financials não tem um conjunto fixo de entidades prontas. Em vez disso, a etapa **Import Workday Entity** chama um **relatório Report-as-a-Service (RaaS)** que você cria no Workday e publica com acesso de serviço web; você informa a URL dele. A etapa admite filtros em `company`, `ledger`, `period`, `accounting_date` (intervalo), `ledger_account` (intervalo) e `cost_center`, cada um repassado como parâmetro do relatório; portanto, um filtro só funciona se o seu relatório definir um prompt correspondente. Consulte [Import Workday Entity](/pt-br/reference/workflow-steps/workday-financials/import-workday-entity/) para ver a referência completa dos campos.

## Lançando Lançamentos Contábeis

A etapa **Workday Financials: Post Journal Entry** lança diários contábeis pelo pipeline compartilhado de gravação em ERP do PlaidCloud, usando a operação SOAP `Submit_Accounting_Journal` do Workday e consultando o status do processo de negócio do lançamento até um estado final antes de informar que ele foi lançado. Uma correção lança um novo lançamento de estorno, com débito e crédito invertidos, em vez de editar o original. Consulte [Workday Financials: Post Journal Entry](/pt-br/reference/workflow-steps/workday-financials/workday-post/) para ver a referência dos campos e [Conectar ao Workday Financials](/pt-br/guides/connections/workday-financials/) para ver o passo a passo completo de lançamento.

## Limitações Conhecidas

| Limitação | O que significa |
|---|---|
| O formato da importação depende do seu relatório RaaS | O PlaidCloud não tem entidades prontas para o Workday Financials: os campos, os prompts e o controle de acesso do relatório ficam no Workday. Uma alteração no relatório pode mudar o formato da sua importação sem nenhuma alteração no lado do PlaidCloud. |
| A aprovação do processo de negócio adiciona latência | Um diário encaminhado por uma etapa de aprovação no seu processo de negócio Submit Accounting Journal permanece `pending` até ser aprovado no Workday; a consulta até o estado final aguarda essa aprovação. |
## Relacionados

- [Conectar ao Workday Financials (guia)](/pt-br/guides/connections/workday-financials/): passo a passo para criar a conexão, testá-la, importar um relatório e lançar um diário.
- [Import Workday Entity](/pt-br/reference/workflow-steps/workday-financials/import-workday-entity/)
- [Workday Financials: Post Journal Entry](/pt-br/reference/workflow-steps/workday-financials/workday-post/)
- [Revisar o Histórico de Lançamentos em ERP](/pt-br/guides/connections/erp-post-history/)
- [Conector Workday REST](/pt-br/reference/connectors/rest/workday/): o conector genérico e separado do Workday para dados REST de RH e folha de pagamento.
