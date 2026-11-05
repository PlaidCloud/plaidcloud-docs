---
title: Matriz de cobertura do Data Foundation
description: Que conjunto de dados do Common Finance Model cada sistema ao qual o Data Foundation se liga fornece diretamente, e quais acrescenta como ficheiro.
sidebar:
  label: Cobertura do Data Foundation
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/data-foundation-coverage-matrix.md
---

O Data Foundation lê diretamente todos os sistemas e instâncias ERP que ligar para um único Common Finance Model. Os ficheiros preenchem tudo o que um sistema não contém, pelo que todos os conjuntos de dados abaixo também podem ser fornecidos como ficheiro.

## Legenda

| Marca | Significado |
| --- | --- |
| **Completo** | O Data Foundation lê o conjunto de dados diretamente do sistema. |
| **Completo¹** | Lido diretamente quando o sistema o contém. Um sistema sem os dados, ou uma ligação sem acesso aos mesmos, não interrompe o carregamento. |
| **Ficheiro** | O sistema não fornece este conjunto de dados. Acrescente-o como ficheiro. |

## SAP, Oracle e Dynamics 365

| Conjunto de dados | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendário fiscal | Completo | Completo | Completo | Completo | Completo | Completo |
| Plano de contas | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo | Completo | Completo | Completo | Completo |
| Centros de lucro | Completo¹ | Completo¹ | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Produtos | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Clientes | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Razão geral | Completo | Completo | Completo | Completo | Completo | Completo |
| Balancete | Completo | Completo | Completo | Completo | Completo | Completo |
| Linhas de vendas | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pipeline | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Saldos de inventário | Completo¹ | Completo¹ | Completo¹ | Ficheiro | Ficheiro | Completo¹ |
| Orçamento | Completo¹ | Completo¹ | Completo¹ | Ficheiro | Ficheiro | Completo¹ |
| Indutores de alocação | Completo¹ | Completo¹ | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Taxas de câmbio | Completo | Completo | Completo | Completo | Completo | Completo |
| Valores de segmento | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| CO-PA por valorização | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |

## Sistemas financeiros de média dimensão e na nuvem

| Conjunto de dados | Business Central | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendário fiscal | Completo | Completo | Completo | Completo | Completo | Completo |
| Plano de contas | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo | Completo¹ | Completo | Completo | Completo |
| Centros de lucro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Produtos | Completo | Completo | Completo¹ | Completo | Completo¹ | Completo |
| Clientes | Completo | Completo | Completo¹ | Completo | Completo¹ | Completo |
| Razão geral | Completo | Completo | Completo | Completo | Completo | Completo |
| Balancete | Completo | Completo | Completo | Completo | Completo | Completo |
| Linhas de vendas | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo |
| Pipeline | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Saldos de inventário | Ficheiro | Ficheiro | Completo¹ | Ficheiro | Ficheiro | Completo¹ |
| Orçamento | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Ficheiro | Completo¹ |
| Indutores de alocação | Completo¹ | Completo¹ | Ficheiro | Ficheiro | Completo¹ | Completo |
| Taxas de câmbio | Completo | Completo | Completo¹ | Ficheiro | Completo | Completo¹ |
| Valores de segmento | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Completo¹ | Completo |
| CO-PA por valorização | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |

## Origens de CRM, consolidação e planeamento

| Conjunto de dados | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entidades | Ficheiro | Ficheiro | Ficheiro |
| Calendário fiscal | Ficheiro | Ficheiro | Ficheiro |
| Plano de contas | Ficheiro | Ficheiro | Ficheiro |
| Departamentos | Ficheiro | Ficheiro | Ficheiro |
| Centros de lucro | Ficheiro | Ficheiro | Ficheiro |
| Produtos | Completo¹ | Ficheiro | Ficheiro |
| Clientes | Completo¹ | Ficheiro | Ficheiro |
| Razão geral | Ficheiro | Ficheiro | Ficheiro |
| Balancete | Ficheiro | Ficheiro | Ficheiro |
| Linhas de vendas | Ficheiro | Ficheiro | Ficheiro |
| Pipeline | Completo¹ | Ficheiro | Ficheiro |
| Saldos de inventário | Ficheiro | Ficheiro | Ficheiro |
| Orçamento | Ficheiro | Completo | Completo |
| Indutores de alocação | Ficheiro | Ficheiro | Ficheiro |
| Taxas de câmbio | Ficheiro | Ficheiro | Ficheiro |
| Valores de segmento | Ficheiro | Ficheiro | Ficheiro |
| CO-PA por valorização | Ficheiro | Ficheiro | Ficheiro |

## Notas por sistema

- O **Salesforce** é uma origem de CRM. Fornece clientes, produtos e o pipeline de vendas, nunca o razão.
- O **OneStream** é uma origem de resultados. Fornece apenas o conjunto de dados de orçamento, trazendo os resultados consolidados para que o Data Foundation possa reconciliar com eles a demonstração de resultados do grupo.
- O **Anaplan** é uma origem de planeamento. Fornece apenas o conjunto de dados de orçamento, a partir de um plano de orçamento, previsão ou consolidado.
- O **SAP S/4HANA e o SAP ECC** leem os mesmos dados mestre. O ECC lê o seu razão a partir das linhas de contabilidade financeira e de controlling, e os seus totais a partir das tabelas de totais do razão geral. Os centros de lucro são lidos quando o sistema os contém. As linhas de vendas são documentos de faturação, não CO-PA.
- O **CO-PA por valorização** não é lido diretamente de nenhum sistema. Acrescente-o como ficheiro.
- O **Workday** não tem serviço direto de diários ou saldos. O Data Foundation fornece os relatórios a criar e lê-os. Os valores de segmento (worktags), clientes, produtos, linhas de vendas e indutores de número de colaboradores provêm de relatórios opcionais. Os orçamentos continuam a ser ficheiros.
- O **Xero** não fornece taxas de câmbio. Acrescente-as como ficheiro se as suas entidades usarem mais do que uma moeda.
- O **QuickBooks Online** lê departamentos, clientes, produtos, taxas de câmbio, orçamentos, inventário e linhas de vendas quando o ficheiro da empresa os contém.
- O **NetSuite** lê segmentos personalizados como valores de segmento. As taxas de câmbio e o inventário são lidos quando a conta os disponibiliza, e os orçamentos quando a conta usa NetSuite Budgets e a função os consegue ler.

## Ver também

- [Data Foundation](/pt-pt/guides/projects/data-foundation/)
- [Introdução ao Data Foundation](/pt-pt/guides/projects/data-foundation-getting-started/)
- [Adicionar ficheiros para dados fora do ERP](/pt-pt/guides/projects/data-foundation/#adicionar-ficheiros-para-dados-fora-do-erp)
- Guias de acesso às ligações:
  - [NetSuite](/pt-pt/guides/connections/netsuite-access-for-data-foundation/)
  - [Salesforce](/pt-pt/guides/connections/salesforce-access-for-data-foundation/)
  - [SAP S/4HANA](/pt-pt/guides/connections/sap-s4hana-access-for-data-foundation/)
  - [SAP ECC](/pt-pt/guides/connections/sap-ecc-access-for-data-foundation/)
  - [SAP S/4HANA Cloud](/pt-pt/guides/connections/s4hana-cloud-access-for-data-foundation/)
  - [Oracle E-Business Suite](/pt-pt/guides/connections/oracle-ebs-access-for-data-foundation/)
  - [Oracle Fusion](/pt-pt/guides/connections/oracle-fusion-access-for-data-foundation/)
  - [Dynamics 365 Finance and Operations](/pt-pt/guides/connections/dynamics-365-fo-access-for-data-foundation/)
  - [Business Central](/pt-pt/guides/connections/business-central-access-for-data-foundation/)
  - [Sage Intacct](/pt-pt/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/pt-pt/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/pt-pt/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/pt-pt/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/pt-pt/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/pt-pt/guides/connections/anaplan/#anaplan-como-origem-do-data-foundation)
