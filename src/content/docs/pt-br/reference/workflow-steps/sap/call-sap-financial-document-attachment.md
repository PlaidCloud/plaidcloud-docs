---
title: Etapa Call SAP Financial Document Attachment
description: Recupere anexos de documentos financeiros do SAP a partir de uma etapa de fluxo de trabalho do PlaidCloud para extração e processamento automatizados de documentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Descrição



Anexa um arquivo a um documento FI (Financial Accounting) específico no SAP ECC / S/4HANA por meio de uma RFC (Remote Function Call). Útil para lançar a documentação de suporte, como faturas digitalizadas, fluxos de aprovação e cópias de contratos, junto com os lançamentos financeiros que ela sustenta.

Requer as credenciais RFC do SAP configuradas no conector do SAP e o número do documento FI de destino (empresa, número do documento, ano fiscal).


## O que é verificado ao salvar

A etapa lê o caminho de cada arquivo de uma coluna `relative_file_path` entre as colunas de saída na guia **Colunas**, e essa coluna deve ser de texto. O salvamento é recusado sem ela (*As colunas de saída devem incluir relative_file_path, o caminho de cada arquivo a anexar.*) ou quando ela tem outro tipo (*A coluna relative_file_path deve ser de texto, não inteiro.*)

Salvar com uma tabela de origem escolhida, mas sem colunas de origem ou sem colunas de destino, preenche o lado vazio a partir da origem, como faria **Preencher ambas as tabelas de mapeamento**.


## Exemplos


### Parâmetros RFC


Selecione o Agente a usar. Selecione o Diretório de destino na barra suspensa e navegue abaixo até a pasta filha de destino correta para o arquivo. Em seguida, dê o nome apropriado ao “Target File Name”. Em “Function Call Information”, insira a função, o Parâmetro de valor de retorno e selecione os parâmetros.



Você pode optar por Inserir linha ou Anexar linha na seção Parâmetros, além de nomear os parâmetros e atribuir valores a eles. Escolha o número de Máx. de solicitações simultâneas e selecione “Wait for RFC to Complete”. Salvar e executar a etapa.
