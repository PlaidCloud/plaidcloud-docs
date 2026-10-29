---
title: Calculate PCM Model
description: Acione cálculos de modelos do SAP PCM a partir de uma etapa de fluxo de trabalho do PlaidCloud para executar jobs de processamento de rentabilidade e alocação de custos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/calculate-pcm-model.md
---

## Descrição



Aciona o mecanismo de cálculo em um modelo do SAP Profitability and Cost Management (PCM). Use-a em um fluxo de trabalho para executar o cálculo de custos depois que cargas de dados anteriores tiverem preenchido as entradas do modelo (atribuições, direcionadores, dados de origem).

O cálculo é assíncrono no lado do servidor PCM; combine com [Stop PCM Model Calculation](/pt-br/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation/) se precisar interromper um cálculo de longa duração.


## Nossas Credenciais


O PlaidCloud é um parceiro oficial da SAP e um fornecedor preferencial de serviços relacionados ao projeto e à implementação de modelos do SAP PCM.







## Exemplos


Selecione Agente a usar na lista suspensa, insira o nome do modelo no campo “Model Name”, marque a caixa de seleção “Wait for Calculation to Complete” (se desejar) e clique em “Save and Run Step”.
