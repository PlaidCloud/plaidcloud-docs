---
title: Passo Call SAP Financial Document Attachment
description: Obtenha anexos de documentos financeiros do SAP a partir de um passo de fluxo de trabalho do PlaidCloud para extração e processamento automatizados de documentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Descrição



Anexa um ficheiro a um documento FI (Financial Accounting) específico no SAP ECC / S/4HANA através de uma RFC (Remote Function Call). Útil para lançar documentação de suporte — faturas digitalizadas, fluxos de aprovação, cópias de contratos — junto dos lançamentos financeiros que sustentam.

Requer as credenciais RFC do SAP configuradas no conector SAP e o número do documento FI de destino (código da empresa, número do documento, exercício).


## O que é verificado ao guardar

O passo lê o caminho de cada ficheiro a partir de uma coluna `relative_file_path` entre as colunas de saída no seu separador **Colunas**, e essa coluna tem de ser de texto. Guardar é recusado sem ela — *As colunas de saída têm de incluir relative_file_path, o caminho de cada ficheiro a anexar.* — ou quando tem outro tipo — *A coluna relative_file_path tem de ser de texto, não de inteiro.*

Guardar com uma tabela de origem escolhida mas sem colunas de origem ou sem colunas de destino preenche o lado vazio a partir da origem, tal como **Preencher ambas as tabelas de mapeamento** faria.


## Exemplos


### Parâmetros RFC


Selecione o Agente a utilizar. Selecione o Diretório de destino na barra pendente e navegue abaixo para encontrar a pasta secundária correta de destino do ficheiro. De seguida, dê o nome adequado a “Target File Name”. Em “Function Call Information”, introduza a Function, o Parâmetro do valor de retorno e selecione os parâmetros.



Pode optar por Inserir linha ou Acrescentar linha na secção Parâmetros, bem como dar nomes aos parâmetros e atribuir-lhes valores. Escolha o número de Máximo de pedidos simultâneos e selecione Wait for RFC to Complete. Guardar e executar passo.
