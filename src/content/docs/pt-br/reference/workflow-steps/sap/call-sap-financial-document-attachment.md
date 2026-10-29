---
title: Etapa Call SAP Financial Document Attachment
description: Recupere anexos de documentos financeiros do SAP a partir de uma etapa de fluxo de trabalho do PlaidCloud para extrair e processar documentos de forma automatizada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Descrição



Anexa um arquivo a um documento FI (Financial Accounting) específico no SAP ECC / S/4HANA por meio de uma RFC (Remote Function Call). É útil para lançar a documentação de suporte — faturas digitalizadas, fluxos de aprovação, cópias de contratos — junto com os lançamentos financeiros que ela comprova.

Exige as credenciais RFC do SAP configuradas no conector SAP e o número do documento FI de destino (empresa, número do documento, exercício fiscal).


## O que é verificado ao salvar

A etapa lê o caminho de cada arquivo em uma coluna `relative_file_path` entre as colunas de saída na guia **Seleção de dados da tabela**, e essa coluna deve ser de texto. O salvamento é recusado se ela não existir — *The output columns must include relative_file_path, the path of each file to attach.* — ou se tiver outro tipo — *The relative_file_path column must be text, not integer.*

Ao salvar com uma tabela de origem escolhida, mas sem colunas de origem ou de destino, o lado vazio é preenchido a partir da origem, como faria **Preencher ambas as tabelas de mapeamento**.


## Exemplos


### Parâmetros RFC


Selecione o Agente a usar. Selecione Diretório de destino na lista suspensa e navegue abaixo até a pasta filha correta de destino do arquivo. Em seguida, dê um nome apropriado ao “Target File Name”. Em “Function Call Information”, informe a função (Function), o Parâmetro de valor de retorno e selecione os parâmetros.



Você pode optar por Inserir linha ou Anexar linha na seção de parâmetros, além de nomear os parâmetros e atribuir valores a eles. Escolha o número de Máx. de solicitações simultâneas e selecione Wait for RFC to Complete. Clique em Salvar e executar etapa.
