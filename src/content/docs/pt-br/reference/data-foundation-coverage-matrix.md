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
| **Completo¹** | Lido diretamente quando o sistema o possui. Um sistema sem os dados não interrompe a carga. Uma conexão sem acesso a eles deixa esse dataset vazio ou faz falhar apenas esse dataset, e o restante é carregado. |
| **Arquivo** | O sistema não fornece este dataset. Adicione-o como arquivo. |

## SAP, Oracle e Dynamics 365

| Dataset | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendário fiscal | Completo | Completo | Completo | Completo | Completo | Completo |
| Plano de contas | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo | Completo | Completo | Completo | Completo |
| Centros de lucro | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Arquivo | Completo¹ |
| Locais | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Projetos | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| Representantes de vendas | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| Produtos | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Clientes | Completo | Completo | Completo | Completo¹ | Completo¹ | Completo |
| Fornecedores | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Razão geral | Completo | Completo | Completo | Completo | Completo | Completo |
| Balancete | Completo | Completo | Completo | Completo | Completo | Completo |
| Saldo de fim de mês | Arquivo | Completo¹ | Arquivo | Completo¹ | Completo¹ | Arquivo |
| Saldos bancários | Arquivo | Completo¹ | Arquivo | Completo¹ | Completo¹ | Completo¹ |
| Linhas de vendas | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pipeline | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| Linhas de faturas de fornecedor | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pedidos de compra | Completo¹ | Completo¹ | Arquivo | Completo¹ | Completo¹ | Arquivo |
| Partidas em aberto | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pagamentos | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Saldos de estoque | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Custos padrão | Completo¹ | Completo¹ | Arquivo | Completo¹ | Completo¹ | Arquivo |
| Ativos imobilizados | Completo¹ | Completo¹ | Arquivo | Completo¹ | Completo¹ | Arquivo |
| Movimentações de ativos | Completo¹ | Completo¹ | Arquivo | Completo¹ | Completo¹ | Arquivo |
| Orçamento | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Direcionadores de alocação | Completo¹ | Completo¹ | Arquivo | Arquivo | Arquivo | Arquivo |
| Taxas de câmbio | Completo | Completo | Completo | Completo | Completo | Completo |
| Valores de segmento | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| CO-PA por avaliação | Completo¹ | Completo¹ | Arquivo | Arquivo | Arquivo | Arquivo |

## Sistemas financeiros de médio porte e em nuvem

| Dataset | Business Central | Sage 100 | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Entidades | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Calendário fiscal | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Plano de contas | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Departamentos | Completo | Completo¹ | Completo | Arquivo | Completo¹ | Completo | Completo |
| Centros de lucro | Completo¹ | Arquivo | Completo¹ | Completo¹ | Completo¹ | Arquivo | Completo¹ |
| Locais | Completo¹ | Arquivo | Completo¹ | Completo¹ | Completo¹ | Arquivo | Completo¹ |
| Projetos | Arquivo | Arquivo | Completo¹ | Arquivo | Arquivo | Arquivo | Arquivo |
| Representantes de vendas | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Completo¹ |
| Produtos | Completo | Arquivo | Completo | Completo¹ | Completo¹ | Completo¹ | Completo |
| Clientes | Completo | Arquivo | Completo | Completo¹ | Completo¹ | Completo¹ | Completo |
| Fornecedores | Completo¹ | Arquivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Razão geral | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Balancete | Completo | Completo | Completo | Completo | Completo | Completo | Completo |
| Saldo de fim de mês | Completo¹ | Arquivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Arquivo |
| Saldos bancários | Completo¹ | Arquivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Linhas de vendas | Completo¹ | Arquivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo |
| Pipeline | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| Linhas de faturas de fornecedor | Completo¹ | Arquivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Partidas em aberto | Completo¹ | Arquivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pagamentos | Completo¹ | Arquivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Pedidos de compra | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| Saldos de estoque | Completo¹ | Arquivo | Arquivo | Completo¹ | Arquivo | Arquivo | Completo¹ |
| Custos padrão | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| Ativos imobilizados | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| Movimentações de ativos | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |
| Orçamento | Completo¹ | Arquivo | Completo¹ | Completo¹ | Completo¹ | Completo¹ | Completo¹ |
| Direcionadores de alocação | Completo¹ | Arquivo | Completo¹ | Arquivo | Arquivo | Completo¹ | Completo |
| Taxas de câmbio | Completo | Arquivo | Completo | Completo¹ | Arquivo | Completo | Completo¹ |
| Valores de segmento | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Completo¹ | Completo¹ |
| CO-PA por avaliação | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo | Arquivo |

## Fontes de CRM, consolidação e planejamento

| Dataset | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| Entidades | Arquivo | Arquivo | Arquivo |
| Calendário fiscal | Completo¹ | Arquivo | Arquivo |
| Plano de contas | Arquivo | Arquivo | Arquivo |
| Departamentos | Arquivo | Arquivo | Arquivo |
| Centros de lucro | Arquivo | Arquivo | Arquivo |
| Projetos | Completo¹ | Arquivo | Arquivo |
| Representantes de vendas | Completo¹ | Arquivo | Arquivo |
| Produtos | Completo¹ | Arquivo | Arquivo |
| Clientes | Completo¹ | Arquivo | Arquivo |
| Razão geral | Arquivo | Arquivo | Arquivo |
| Balancete | Arquivo | Arquivo | Arquivo |
| Linhas de vendas | Arquivo | Arquivo | Arquivo |
| Pipeline | Completo¹ | Arquivo | Arquivo |
| Pedidos de venda | Completo¹ | Arquivo | Arquivo |
| Saldos de estoque | Arquivo | Arquivo | Arquivo |
| Orçamento | Arquivo | Completo | Completo |
| Direcionadores de alocação | Arquivo | Completo¹ | Completo¹ |
| Taxas de câmbio | Arquivo | Arquivo | Arquivo |
| Valores de segmento | Arquivo | Arquivo | Arquivo |
| CO-PA por avaliação | Arquivo | Arquivo | Arquivo |

## Observações por sistema

- **Pedidos de venda, contratos, receita diferida e movimentações de estoque** não são lidos de nenhum sistema, exceto os pedidos do Salesforce. Adicione-os como arquivos.
- **Salesforce** é uma fonte de CRM. Ele fornece clientes, produtos, o pipeline de vendas, representantes de vendas (usuários), campanhas como projetos, seus meses fiscais e pedidos, nunca o razão. Os pedidos exigem que Orders esteja habilitado no Salesforce. Quando o Salesforce recusa a leitura dos pedidos, apenas os meses de pedidos falham, e eles mantêm o que carregaram por último.
- **OneStream** é uma fonte de resultados. Ele fornece o dataset de orçamento, trazendo seus resultados consolidados para que o Data Foundation possa reconciliar com eles a demonstração do resultado do grupo, e um cenário de Budget ou Forecast como plano. Um segundo adaptador opcional fornece a quantidade de funcionários e as unidades planejadas como direcionadores de alocação.
- **Anaplan** é uma fonte de planejamento. Ele fornece o dataset de orçamento, a partir de um plano de Budget, Forecast ou Consolidated, e direcionadores de alocação a partir de uma segunda exportação opcional.
- **SAP S/4HANA e SAP ECC** leem os mesmos dados mestres, fornecedores, faturas de fornecedor, pedidos de compra, partidas em aberto, pagamentos, o registro de ativos imobilizados e os custos padrão. O ECC lê seu razão a partir das linhas de lançamento de contabilidade financeira e de controladoria, e seus totais e o saldo de fim de mês a partir da tabela de totais do razão geral. Os centros de lucro e os centros (locais) são lidos quando o sistema os possui. As linhas de vendas são documentos de faturamento. O CO-PA por avaliação é lido da tabela de linhas de lançamento da área de resultados que você nomear; se nenhuma for nomeada, adicione-o como arquivo.
- O **Oracle E-Business Suite** lê os locais e os centros de lucro do segmento do plano de contas que você nomear para cada um.
- O **Oracle Fusion** lê cada dataset opcional de um relatório próprio do BI Publisher. Um relatório de clientes, produtos, locais ou fornecedores que você não implantar deixa esse dataset vazio, com um aviso; o dataset de qualquer outro relatório falha e mantém o que carregou por último; todo o restante é carregado.
- O **Workday** não tem um serviço direto de lançamentos ou saldos. O Data Foundation fornece os relatórios a criar e os lê. Os valores de segmento (worktags), clientes, produtos, fornecedores, linhas de vendas, razões auxiliares, saldos bancários, orçamentos e direcionadores vêm de relatórios opcionais, e o saldo de fim de mês vem do saldo final do relatório de saldos iniciais.
- O **Sage 100** é lido por meio de um agente PlaidLink, uma empresa por conexão. Ele mantém sua contabilidade em uma única moeda, então não fornece taxas de câmbio, e o Data Foundation não lê seus produtos, clientes nem linhas de vendas. Os departamentos são lidos do segmento de departamento da conta quando a máscara da conta tem um.
- O **Xero** não fornece taxas de câmbio. Adicione-as como arquivo se suas entidades usam mais de uma moeda. Os departamentos, locais e centros de lucro são as opções das categorias de rastreamento chamadas exatamente Department, Site e Profit centre. O Xero permite duas categorias de rastreamento, então uma organização tem no máximo duas das três.
- O **QuickBooks Online** não tem departamentos: seus locations são lidos como locais, e suas classes, como centros de lucro. Clientes, produtos, fornecedores, taxas de câmbio, orçamentos, estoque, vendas e compras são lidos quando a empresa os possui, e o estoque apenas quando a empresa controla a quantidade disponível.
- O **NetSuite** lê segmentos personalizados como valores de segmento, classes como centros de lucro e locations como locais. As taxas de câmbio e o estoque são lidos quando a conta os oferece, e os orçamentos quando a conta usa o NetSuite Budgets e a função pode lê-los.

## Saldo de fim de mês

O Data Foundation lê o saldo de fechamento que cada sistema informa no fim de cada mês (consulte [Os números são confiáveis?](/pt-br/guides/projects/data-foundation-proof/)) a partir de:

| Sistema | Saldo de fim de mês lido de |
| --- | --- |
| SAP ECC | A tabela de totais do razão geral (`FAGLFLEXT`, ou `GLT0` no razão geral clássico) |
| Oracle E-Business Suite | `GL_BALANCES`, que deve conter todos os períodos |
| Oracle Fusion | O relatório PlaidCloudBalances, cobrindo todos os períodos |
| Business Central | O balancete no fim de cada mês |
| Sage Intacct | Os saldos das contas (o saldo final de cada mês) |
| QuickBooks Online | O relatório Trial Balance no fim de cada mês |
| Xero | O relatório Trial Balance no fim de cada mês |
| Workday | O saldo final do relatório Beginning Balances |

O SAP S/4HANA, o SAP S/4HANA Cloud, o Dynamics 365 Finance and Operations, o NetSuite e o Sage 100 não informam um saldo separado que o Data Foundation leia. Eles são carregados e funcionam normalmente. Quando o Business Central recusa seu balancete no fim de um mês, o saldo desse mês falha e mantém o que carregou por último.

## Detalhes dos lançamentos

Além dos valores, cada linha do razão geral traz o tipo do lançamento, a data do documento, quem o registrou e quando, quem o aprovou, o lançamento que ele estorna e seu imposto, quando o sistema os possui. O calendário fiscal traz o status de cada período.

| Sistema | Tipo de lançamento | Data do documento | Registrado por e quando | Aprovador | Estorno | Imposto | Status do período |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SAP S/4HANA | Sim | Sim | Sim | Não | Não | Código | Sim |
| SAP ECC | Sim | Sim | Sim | Não | Sim | Código e valor | Sim |
| SAP S/4HANA Cloud | Sim | Sim | Sim | Não | Sim | Não | Não |
| Oracle E-Business Suite | Sim | Sim | Sim | Sim | Sim | Não | Sim |
| Oracle Fusion | Sim | Sim | Sim | Sim | Sim | Não | Sim |
| Dynamics 365 Finance and Operations | Sim | Sim | Sim | Não | Não | Não | Sim |
| Business Central | Sim | Sim | Sim | Não | Sim | Não | Sim |
| Sage 100 | Não | Não | Não | Não | Não | Não | Fechado assim que o período termina |
| Sage Intacct | Sim | Sim | Sim | Sim | Sim | Não | Sim |
| QuickBooks Online | Sim | Sim | Sim | Não | Não | Não | A data de fechamento dos livros |
| Xero | Sim | Sim | Apenas quando | Não | Não | Não | A data de bloqueio |
| Workday | Sim | Sim | Sim | Sim | Sim | Código e valor | Sim |
| NetSuite | Sim | Sim | Sim | Não | Não | Não | Sim |

O SAP S/4HANA Cloud lê quem registrou um lançamento e o que ele estorna a partir do serviço Journal Entry, o Sage Intacct a partir dos lotes de lançamentos, e o Oracle E-Business Suite lê o aprovador a partir de `GL_JE_BATCHES`. Uma conexão que não consegue lê-los deixa essas colunas vazias.

## Relacionados

- [Data Foundation](/pt-br/guides/projects/data-foundation/)
- [Primeiros passos com o Data Foundation](/pt-br/guides/projects/data-foundation-getting-started/)
- [Adicione arquivos para dados fora do seu ERP](/pt-br/guides/projects/data-foundation/#adicionar-arquivos-com-dados-de-fora-do-erp)
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
  - [Sage 100](/pt-br/guides/connections/sage-100/)
  - [Sage Intacct](/pt-br/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/pt-br/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/pt-br/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/pt-br/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/pt-br/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/pt-br/guides/connections/anaplan/#anaplan-como-origem-do-data-foundation)
