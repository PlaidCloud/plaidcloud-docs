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
| **Completo¹** | Lido diretamente quando o sistema o contém. Um sistema sem os dados não interrompe o carregamento. Uma ligação sem acesso aos mesmos deixa esse conjunto de dados vazio ou faz falhar apenas esse conjunto de dados, e o resto é carregado. |
| **Ficheiro** | O sistema não fornece este conjunto de dados. Acrescente-o como ficheiro. |

## SAP, Oracle e Dynamics 365

| Conjunto de dados | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendário fiscal | Completo | Completo | Completo | Completo | Completo | Completo |
| Plano de contas | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo | Completo | Completo | Completo | Completo |
| Centros de lucro | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Ficheiro | Completo¹ |
| Locais | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Projetos | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Comerciais | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Produtos | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Clientes | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Fornecedores | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Razão geral | Completo | Completo | Completo | Completo | Completo | Completo |
| Balancete | Completo | Completo | Completo | Completo | Completo | Completo |
| Saldo de fim de mês | Ficheiro | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Ficheiro |
| Saldos bancários | Ficheiro | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Completo¹ |
| Linhas de vendas | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pipeline | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Linhas de faturas de fornecedores | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Encomendas de compra | Completo¹ | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Ficheiro |
| Partidas em aberto | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pagamentos | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Saldos de inventário | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Custos-padrão | Completo¹ | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Ficheiro |
| Ativos fixos | Completo¹ | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Ficheiro |
| Movimentos de ativos | Completo¹ | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Ficheiro |
| Orçamento | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Indutores de alocação | Completo¹ | Completo¹ | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Taxas de câmbio | Completo | Completo | Completo | Completo | Completo | Completo |
| Valores de segmento | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| CO-PA por valorização | Completo¹ | Completo¹ | Ficheiro | Ficheiro | Ficheiro | Ficheiro |

## Sistemas financeiros de média dimensão e na nuvem

| Conjunto de dados | Business Central | Sage 100 | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendário fiscal | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Plano de contas | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo¹ | Completo | Ficheiro | Completo¹ | Completo | Completo |
| Centros de lucro | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Completo¹ | Ficheiro | Completo¹ |
| Locais | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Completo¹ | Ficheiro | Completo¹ |
| Projetos | Ficheiro | Ficheiro | Completo¹ | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Comerciais | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Completo¹ |
| Produtos | Completo | Ficheiro | Completo | Completo¹ | Completo¹ | Completo¹ | Completo |
| Clientes | Completo | Ficheiro | Completo | Completo¹ | Completo¹ | Completo¹ | Completo |
| Fornecedores | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Razão geral | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Balancete | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Saldo de fim de mês | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Ficheiro |
| Saldos bancários | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Linhas de vendas | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo |
| Pipeline | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Linhas de faturas de fornecedores | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Partidas em aberto | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pagamentos | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Encomendas de compra | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Saldos de inventário | Completo¹ | Ficheiro | Ficheiro | Completo¹ | Ficheiro | Ficheiro | Completo¹ |
| Custos-padrão | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Ativos fixos | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Movimentos de ativos | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |
| Orçamento | Completo¹ | Ficheiro | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Indutores de alocação | Completo¹ | Ficheiro | Completo¹ | Ficheiro | Ficheiro | Completo¹ | Completo |
| Taxas de câmbio | Completo | Ficheiro | Completo | Completo¹ | Ficheiro | Completo | Completo¹ |
| Valores de segmento | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Completo¹ | Completo¹ |
| CO-PA por valorização | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro | Ficheiro |

## Origens de CRM, consolidação e planeamento

| Conjunto de dados | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entidades | Ficheiro | Ficheiro | Ficheiro |
| Calendário fiscal | Completo¹ | Ficheiro | Ficheiro |
| Plano de contas | Ficheiro | Ficheiro | Ficheiro |
| Departamentos | Ficheiro | Ficheiro | Ficheiro |
| Centros de lucro | Ficheiro | Ficheiro | Ficheiro |
| Projetos | Completo¹ | Ficheiro | Ficheiro |
| Comerciais | Completo¹ | Ficheiro | Ficheiro |
| Produtos | Completo¹ | Ficheiro | Ficheiro |
| Clientes | Completo¹ | Ficheiro | Ficheiro |
| Razão geral | Ficheiro | Ficheiro | Ficheiro |
| Balancete | Ficheiro | Ficheiro | Ficheiro |
| Linhas de vendas | Ficheiro | Ficheiro | Ficheiro |
| Pipeline | Completo¹ | Ficheiro | Ficheiro |
| Encomendas de venda | Completo¹ | Ficheiro | Ficheiro |
| Saldos de inventário | Ficheiro | Ficheiro | Ficheiro |
| Orçamento | Ficheiro | Completo | Completo |
| Indutores de alocação | Ficheiro | Completo¹ | Completo¹ |
| Taxas de câmbio | Ficheiro | Ficheiro | Ficheiro |
| Valores de segmento | Ficheiro | Ficheiro | Ficheiro |
| CO-PA por valorização | Ficheiro | Ficheiro | Ficheiro |

## Notas por sistema

- As **encomendas de venda, contratos, receitas diferidas e movimentos de inventário** não são lidos de nenhum sistema, exceto as encomendas do Salesforce. Acrescente-os como ficheiros.
- O **Salesforce** é uma origem de CRM. Fornece clientes, produtos, o pipeline de vendas, os comerciais (utilizadores), as campanhas como projetos, os seus meses fiscais e as encomendas, nunca o razão. As encomendas exigem que Orders esteja ativado no Salesforce. Quando o Salesforce recusa a leitura das encomendas, apenas os meses das encomendas falham, e mantêm o que carregaram da última vez.
- O **OneStream** é uma origem de resultados. Fornece o conjunto de dados de orçamento, trazendo os resultados consolidados para que o Data Foundation possa reconciliar com eles a demonstração de resultados do grupo, e um cenário Budget ou Forecast como plano. Um segundo adaptador opcional fornece o número de colaboradores e as unidades planeados como indutores de alocação.
- O **Anaplan** é uma origem de planeamento. Fornece o conjunto de dados de orçamento, a partir de um plano de orçamento, previsão ou consolidado, e indutores de alocação a partir de uma segunda exportação opcional.
- O **SAP S/4HANA e o SAP ECC** leem os mesmos dados mestre, fornecedores, faturas de fornecedores, encomendas de compra, partidas em aberto, pagamentos, o registo de ativos fixos e os custos-padrão. O ECC lê o seu razão a partir das linhas de contabilidade financeira e de controlling, e os seus totais e o saldo de fim de mês a partir da tabela de totais do razão geral. Os centros de lucro e as fábricas (locais) são lidos quando o sistema os contém. As linhas de vendas são documentos de faturação. O CO-PA por valorização é lido a partir da tabela de linhas da área de resultados que indicar; se não indicar nenhuma, acrescente-o como ficheiro.
- O **Oracle E-Business Suite** lê os locais e os centros de lucro a partir do segmento do plano de contas que indicar para cada um.
- O **Oracle Fusion** lê cada conjunto de dados opcional a partir do seu próprio relatório BI Publisher. Um relatório de clientes, produtos, locais ou fornecedores que não implemente deixa esse conjunto de dados vazio com um aviso; o conjunto de dados de qualquer outro relatório falha e mantém o que carregou da última vez; tudo o resto é carregado.
- O **Workday** não tem serviço direto de diários ou saldos. O Data Foundation fornece os relatórios a criar e lê-os. Os valores de segmento (worktags), clientes, produtos, fornecedores, linhas de vendas, subrazões, saldos bancários, orçamentos e indutores provêm de relatórios opcionais, e o saldo de fim de mês provém do saldo final do relatório de saldos iniciais.
- O **Sage 100** é lido através de um agente PlaidLink, uma empresa por ligação. Mantém a contabilidade numa única moeda, pelo que não fornece taxas de câmbio, e o Data Foundation não lê os seus produtos, clientes nem linhas de vendas. Os departamentos são lidos do segmento de departamento da conta quando a máscara de conta o tem.
- O **Xero** não fornece taxas de câmbio. Acrescente-as como ficheiro se as suas entidades usarem mais do que uma moeda. Os departamentos, os locais e os centros de lucro são as opções das categorias de controlo com os nomes exatos Department, Site e Profit centre. O Xero permite duas categorias de controlo, pelo que uma organização tem no máximo duas das três.
- O **QuickBooks Online** não tem departamentos: as suas localizações são lidas como locais e as suas classes como centros de lucro. Os clientes, produtos, fornecedores, taxas de câmbio, orçamentos, inventário, vendas e compras são lidos quando a empresa os contém, e o inventário apenas quando a empresa controla a quantidade disponível.
- O **NetSuite** lê segmentos personalizados como valores de segmento, classes como centros de lucro e localizações como locais. As taxas de câmbio e o inventário são lidos quando a conta os disponibiliza, e os orçamentos quando a conta usa NetSuite Budgets e a função os consegue ler.

## Saldo de fim de mês

O Data Foundation lê o saldo de fecho que cada sistema reporta em cada fim de mês (consulte [Os números são fiáveis?](/pt-pt/guides/projects/data-foundation-proof/)) a partir de:

| Sistema | Saldo de fim de mês lido a partir de |
| --- | --- |
| SAP ECC | A tabela de totais do razão geral (`FAGLFLEXT`, ou `GLT0` no razão geral clássico) |
| Oracle E-Business Suite | `GL_BALANCES`, que tem de conter todos os períodos |
| Oracle Fusion | O relatório PlaidCloudBalances, que abrange todos os períodos |
| Business Central | O balancete em cada fim de mês |
| Sage Intacct | Os saldos das contas (o saldo final de cada mês) |
| QuickBooks Online | O relatório Trial Balance em cada fim de mês |
| Xero | O relatório Trial Balance em cada fim de mês |
| Workday | O saldo final do relatório Beginning Balances |

O SAP S/4HANA, o SAP S/4HANA Cloud, o Dynamics 365 Finance and Operations, o NetSuite e o Sage 100 não reportam nenhum saldo separado que o Data Foundation leia. São carregados e funcionam como habitualmente. Quando o Business Central recusa o seu balancete num fim de mês, o saldo desse mês falha e mantém o que carregou da última vez.

## Detalhe dos diários

Além dos montantes, cada linha do razão geral indica o tipo do diário, a data do documento, quem o introduziu e quando, quem o aprovou, o diário que estorna e o respetivo imposto, quando o sistema contém essa informação. O calendário fiscal indica o estado de cada período.

| Sistema | Tipo de diário | Data do documento | Introduzido por e quando | Aprovador | Estorno | Imposto | Estado do período |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SAP S/4HANA | Sim | Sim | Sim | Não | Não | Código | Sim |
| SAP ECC | Sim | Sim | Sim | Não | Sim | Código e montante | Sim |
| SAP S/4HANA Cloud | Sim | Sim | Sim | Não | Sim | Não | Não |
| Oracle E-Business Suite | Sim | Sim | Sim | Sim | Sim | Não | Sim |
| Oracle Fusion | Sim | Sim | Sim | Sim | Sim | Não | Sim |
| Dynamics 365 Finance and Operations | Sim | Sim | Sim | Não | Não | Não | Sim |
| Business Central | Sim | Sim | Sim | Não | Sim | Não | Sim |
| Sage 100 | Não | Não | Não | Não | Não | Não | Fechado quando o período termina |
| Sage Intacct | Sim | Sim | Sim | Sim | Sim | Não | Sim |
| QuickBooks Online | Sim | Sim | Sim | Não | Não | Não | A data de fecho dos livros |
| Xero | Sim | Sim | Apenas quando | Não | Não | Não | A data de bloqueio |
| Workday | Sim | Sim | Sim | Sim | Sim | Código e montante | Sim |
| NetSuite | Sim | Sim | Sim | Não | Não | Não | Sim |

O SAP S/4HANA Cloud lê quem introduziu um diário e o que este estorna a partir do serviço Journal Entry, o Sage Intacct a partir dos lotes de diários, e o Oracle E-Business Suite lê o aprovador a partir de `GL_JE_BATCHES`. Uma ligação que não os consiga ler deixa essas colunas vazias.

## Ver também

- [Data Foundation](/pt-pt/guides/projects/data-foundation/)
- [Introdução ao Data Foundation](/pt-pt/guides/projects/data-foundation-getting-started/)
- [Adicionar ficheiros para dados fora do ERP](/pt-pt/guides/projects/data-foundation/#adicionar-ficheiros-com-dados-exteriores-ao-erp)
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
  - [Sage 100](/pt-pt/guides/connections/sage-100/)
  - [Sage Intacct](/pt-pt/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/pt-pt/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/pt-pt/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/pt-pt/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/pt-pt/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/pt-pt/guides/connections/anaplan/#anaplan-como-origem-do-data-foundation)
