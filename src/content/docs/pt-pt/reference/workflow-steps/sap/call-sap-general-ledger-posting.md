---
title: Call SAP General Ledger Posting
description: Chama uma Remote Function Call (RFC) do SAP ECC / S/4HANA concebida para lançar um lançamento contabilístico, incluindo o IVA e as retenções na fonte aplicáveis.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-general-ledger-posting.md
---

## Descrição


Chama uma Remote Function Call (RFC) do SAP ECC / S/4HANA concebida para lançar um lançamento contabilístico, incluindo o IVA e as retenções na fonte aplicáveis. Também pode ser executada em modo de teste, que realiza o processo de lançamento mas não o conclui. Isto permite recolher erros detetáveis, como uma conta encerrada ou um cliente inexistente na empresa indicada. A verificação de erros é robusta e consegue devolver vários erros detetados num único teste.


## Exemplos


### Parâmetros RFC


Selecione o **Agente a utilizar**. Selecione o **Diretório de destino** na lista pendente e navegue abaixo até à subpasta de destino correta para o ficheiro. Em seguida, atribua um nome adequado ao "Nome do ficheiro de destino". Em "Informações da chamada de função", introduza a função e o **Parâmetro do valor de retorno**, e selecione os parâmetros. 



Pode optar por **Inserir linha** ou **Acrescentar linha** na secção de parâmetros, bem como dar nome aos parâmetros e atribuir-lhes valores. Escolha o número em **Máximo de pedidos simultâneos** e selecione "Aguardar a conclusão da RFC". **Guardar e executar passo**.
