---
title: Call SAP Master Data Table RFC
description: Chama uma Remote Function Call (RFC) do SAP ECC / S/4HANA concebida para aceder a tabelas de dados mestre e obtém os dados em formato tabular.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-master-data-table-rfc.md
---

## Descrição


Chama uma Remote Function Call (RFC) do SAP ECC / S/4HANA concebida para aceder a tabelas de dados mestre e obtém os dados em formato tabular. Estes dados ficam então disponíveis para processos de transformação na PlaidCloud. Também permite exportar a estrutura da tabela de dados mestre para um ficheiro separado, com os nomes das colunas, os tipos de dados e a ordem das colunas.


## Exemplos


### Parâmetros RFC


Selecione o **Agente a utilizar**. Selecione o **Diretório de destino** na lista pendente e navegue abaixo até à subpasta de destino correta para o ficheiro. Em seguida, atribua um nome adequado ao "Nome do ficheiro de destino". Em "Informações da chamada de função", introduza a função e o **Parâmetro do valor de retorno**, e selecione os parâmetros.



Pode optar por **Inserir linha** ou **Acrescentar linha** na secção de parâmetros, bem como dar nome aos parâmetros e atribuir-lhes valores. Escolha o número em **Máximo de pedidos simultâneos** e selecione "Aguardar a conclusão da RFC". **Guardar e executar passo**.
