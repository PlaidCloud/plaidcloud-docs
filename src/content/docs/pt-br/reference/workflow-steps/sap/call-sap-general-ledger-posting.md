---
title: Etapa Call SAP General Ledger Posting
description: Chama uma Remote Function Call (RFC) do SAP ECC / S/4HANA projetada para lançar um lançamento contábil, incluindo os impostos aplicáveis de IVA e retenção na fonte.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-general-ledger-posting.md
---

## Descrição


Chama uma Remote Function Call (RFC) do SAP ECC / S/4HANA projetada para lançar um lançamento contábil, incluindo os impostos aplicáveis de IVA e retenção na fonte. Ela também pode ser executada em modo de teste, que realiza o processo de lançamento sem concluí-lo. Isso permite coletar erros detectáveis, como uma conta encerrada ou um cliente que não existe na empresa especificada. A verificação de erros é robusta e pode retornar vários erros detectados em um único teste.


## Exemplos


### Parâmetros RFC


Selecione o Agente a usar. Selecione Diretório de destino na lista suspensa e navegue abaixo até a pasta filha correta de destino do arquivo. Em seguida, dê um nome apropriado ao “Target File Name”. Em “Function Call Information”, informe a função (Function), o Parâmetro de valor de retorno e selecione os parâmetros. 



Você pode optar por Inserir linha ou Anexar linha na seção de parâmetros, além de nomear os parâmetros e atribuir valores a eles. Escolha o número de Máx. de solicitações simultâneas e selecione Wait for RFC to Complete. Clique em Salvar e executar etapa.
