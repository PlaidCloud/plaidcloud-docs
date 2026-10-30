---
title: Etapa Call SAP Master Data Table RFC
description: Chama uma Remote Function Call (RFC) do SAP ECC / S/4HANA projetada para acessar tabelas de dados mestres e recuperar os dados em formato tabular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-master-data-table-rfc.md
---

## Descrição


Chama uma Remote Function Call (RFC) do SAP ECC / S/4HANA projetada para acessar tabelas de dados mestres e recuperar os dados em formato tabular. Esses dados ficam disponíveis para os processos de transformação no PlaidCloud. A etapa também permite exportar a estrutura da tabela de dados mestres para um arquivo separado, com nomes de colunas, tipos de dados e ordem das colunas.


## Exemplos


### Parâmetros RFC


Selecione o Agente a usar. Selecione Diretório de destino na lista suspensa e navegue abaixo até a pasta filha correta de destino do arquivo. Em seguida, dê um nome apropriado ao “Target File Name”. Em “Function Call Information”, informe a função (Function), o Parâmetro de valor de retorno e selecione os parâmetros.



Você pode optar por Inserir linha ou Anexar linha na seção de parâmetros, além de nomear os parâmetros e atribuir valores a eles. Escolha o número de Máx. de solicitações simultâneas e selecione Wait for RFC to Complete. Clique em Salvar e executar etapa.
