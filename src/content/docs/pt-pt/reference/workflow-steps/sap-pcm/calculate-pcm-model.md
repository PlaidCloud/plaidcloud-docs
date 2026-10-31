---
title: Calculate PCM Model
description: Acione cálculos de modelos SAP PCM a partir de um passo de fluxo de trabalho do PlaidCloud para executar tarefas de processamento de rentabilidade e alocação de custos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/calculate-pcm-model.md
---

## Descrição



Aciona o motor de cálculo de um modelo do SAP Profitability and Cost Management (PCM). Utilize-o num fluxo de trabalho para executar o cálculo de custos depois de os carregamentos de dados a montante terem preenchido as entradas do modelo (atribuições, indutores, dados de origem).

O cálculo é assíncrono no lado do servidor PCM; combine com [Stop PCM Model Calculation](/pt-pt/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation/) se precisar de interromper um cálculo de longa duração.


## As nossas credenciais


O PlaidCloud é um parceiro oficial da SAP e um fornecedor preferencial de serviços relacionados com a conceção e a implementação de modelos SAP PCM.







## Exemplos


Selecione Agente a utilizar na lista pendente, introduza o nome do modelo no campo “Model Name”, marque a caixa de seleção “Wait for Calculation to Complete” (se pretendido) e clique em “Save and Run Step”.
