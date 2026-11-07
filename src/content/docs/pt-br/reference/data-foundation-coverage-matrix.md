---
title: Matriz de cobertura do Data Foundation
description: Qual dataset do Common Finance Model cada sistema ao qual o Data Foundation se conecta fornece diretamente e quais você adiciona como arquivo.
sidebar:
  label: Cobertura do Data Foundation
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/data-foundation-coverage-matrix.md
---

O Data Foundation lê diretamente cada sistema ERP e cada instância que você conecta em um único Common Finance Model. Os arquivos preenchem o que um sistema não guarda, então todos os datasets abaixo também podem ser fornecidos como arquivo.

## Legenda

| Marca | Significado |
| --- | --- |
| **Completo** | O Data Foundation lê o dataset diretamente do sistema. |
| **Completo¹** | Lido diretamente quando o sistema o possui. Um sistema sem os dados, ou uma conexão sem acesso a eles, não interrompe a carga. |
| **Arquivo** | O sistema não fornece este dataset. Adicione-o como arquivo. |

## SAP, Oracle e Dynamics 365

| Dataset | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendário fiscal | Completo | Completo | Completo | Completo | Completo | Completo |
| Plano de contas | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo | Completo | Completo | Completo | Completo |
| Centros de lucro | Completo¹ | Completo¹ | Arquivo | Arquivo | Arquivo | Arquivo |
| Produtos | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Clientes | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Razão geral | Completo | Completo | Completo | Completo | Completo | Completo |
| Balancete | Completo | Completo | Completo | Completo | Completo | Completo |
| Linhas de vendas | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pipeline | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| Saldos de estoque | Completo¹ | Completo¹ | Completo¹ | Arquivo | Arquivo | Completo¹ |
| Orçamento | Completo¹ | Completo¹ | Completo¹ | Arquivo | Arquivo | Completo¹ |
| Direcionadores de alocação | Completo¹ | Completo¹ | Arquivo | Arquivo | Arquivo | Arquivo |
| Taxas de câmbio | Completo | Completo | Completo | Completo | Completo | Completo |
| Valores de segmento | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| CO-PA por avaliação | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |

## Sistemas financeiros de médio porte e em nuvem

| Dataset | Business Central | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendário fiscal | Completo | Completo | Completo | Completo | Completo | Completo |
| Plano de contas | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo | Completo¹ | Completo | Completo | Completo |
| Centros de lucro | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| Produtos | Completo | Completo | Completo¹ | Completo | Completo¹ | Completo |
| Clientes | Completo | Completo | Completo¹ | Completo | Completo¹ | Completo |
| Razão geral | Completo | Completo | Completo | Completo | Completo | Completo |
| Balancete | Completo | Completo | Completo | Completo | Completo | Completo |
| Linhas de vendas | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo |
| Pipeline | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| Saldos de estoque | Arquivo | Arquivo | Completo¹ | Arquivo | Arquivo | Completo¹ |
| Orçamento | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Arquivo | Completo¹ |
| Direcionadores de alocação | Completo¹ | Completo¹ | Arquivo | Arquivo | Completo¹ | Completo |
| Taxas de câmbio | Completo | Completo | Completo¹ | Arquivo | Completo | Completo¹ |
| Valores de segmento | Arquivo | Arquivo | Arquivo | Arquivo | Completo¹ | Completo |
| CO-PA por avaliação | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |

## Fontes de CRM, consolidação e planejamento

| Dataset | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entidades | Arquivo | Arquivo | Arquivo |
| Calendário fiscal | Arquivo | Arquivo | Arquivo |
| Plano de contas | Arquivo | Arquivo | Arquivo |
| Departamentos | Arquivo | Arquivo | Arquivo |
| Centros de lucro | Arquivo | Arquivo | Arquivo |
| Produtos | Completo¹ | Arquivo | Arquivo |
| Clientes | Completo¹ | Arquivo | Arquivo |
| Razão geral | Arquivo | Arquivo | Arquivo |
| Balancete | Arquivo | Arquivo | Arquivo |
| Linhas de vendas | Arquivo | Arquivo | Arquivo |
| Pipeline | Completo¹ | Arquivo | Arquivo |
| Saldos de estoque | Arquivo | Arquivo | Arquivo |
| Orçamento | Arquivo | Completo | Completo |
| Direcionadores de alocação | Arquivo | Arquivo | Arquivo |
| Taxas de câmbio | Arquivo | Arquivo | Arquivo |
| Valores de segmento | Arquivo | Arquivo | Arquivo |
| CO-PA por avaliação | Arquivo | Arquivo | Arquivo |

## Observações por sistema

- **Salesforce** é uma fonte de CRM. Ele fornece clientes, produtos e o pipeline de vendas, nunca o razão.
- **OneStream** é uma fonte de resultados. Ele fornece apenas o dataset de orçamento, trazendo seus resultados consolidados para que o Data Foundation possa reconciliar com eles a demonstração do resultado do grupo.
- **Anaplan** é uma fonte de planejamento. Ele fornece apenas o dataset de orçamento, a partir de um plano de Budget, Forecast ou Consolidated.
- **SAP S/4HANA e SAP ECC** leem os mesmos dados mestres. O ECC lê seu razão a partir das linhas de lançamento de contabilidade financeira e de controladoria, e seus totais a partir das tabelas de totais do razão geral. Os centros de lucro são lidos quando o sistema os possui. As linhas de vendas são documentos de faturamento, não CO-PA.
- **CO-PA por avaliação** não é lido diretamente de nenhum sistema. Adicione-o como arquivo.
- O **Workday** não tem um serviço direto de lançamentos ou saldos. O Data Foundation fornece os relatórios a criar e os lê. Os valores de segmento (worktags), clientes, produtos, linhas de vendas e direcionadores de quantidade de funcionários vêm de relatórios opcionais. Os orçamentos continuam sendo arquivos.
- O **Xero** não fornece taxas de câmbio. Adicione-as como arquivo se suas entidades usam mais de uma moeda.
- O **QuickBooks Online** lê departamentos, clientes, produtos, taxas de câmbio, orçamentos, estoque e linhas de vendas quando o arquivo da empresa os possui.
- O **NetSuite** lê segmentos personalizados como valores de segmento. As taxas de câmbio e o estoque são lidos quando a conta os oferece, e os orçamentos quando a conta usa o NetSuite Budgets e a função pode lê-los.

## Relacionados

- [Data Foundation](/pt-br/guides/projects/data-foundation/)
- [Primeiros passos com o Data Foundation](/pt-br/guides/projects/data-foundation-getting-started/)
- [Adicione arquivos para dados fora do seu ERP](/pt-br/guides/projects/data-foundation/#adicionar-arquivos-para-dados-fora-do-seu-erp)
- Guias de acesso da conexão:
  - [NetSuite](/pt-br/guides/connections/netsuite-access-for-data-foundation/)
  - [Salesforce](/pt-br/guides/connections/salesforce-access-for-data-foundation/)
  - [SAP S/4HANA](/pt-br/guides/connections/sap-s4hana-access-for-data-foundation/)
  - [SAP ECC](/pt-br/guides/connections/sap-ecc-access-for-data-foundation/)
  - [SAP S/4HANA Cloud](/pt-br/guides/connections/s4hana-cloud-access-for-data-foundation/)
  - [Oracle E-Business Suite](/pt-br/guides/connections/oracle-ebs-access-for-data-foundation/)
  - [Oracle Fusion](/pt-br/guides/connections/oracle-fusion-access-for-data-foundation/)
  - [Dynamics 365 Finance and Operations](/pt-br/guides/connections/dynamics-365-fo-access-for-data-foundation/)
  - [Business Central](/pt-br/guides/connections/business-central-access-for-data-foundation/)
  - [Sage Intacct](/pt-br/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/pt-br/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/pt-br/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/pt-br/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/pt-br/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/pt-br/guides/connections/anaplan/#anaplan-como-origem-do-data-foundation)
