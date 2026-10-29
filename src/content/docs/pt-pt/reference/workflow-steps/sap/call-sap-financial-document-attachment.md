---
title: Call SAP Financial Document Attachment
description: Obtenha anexos de documentos financeiros do SAP a partir de um passo de fluxo de trabalho do PlaidCloud, para extração e processamento automatizados de documentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Descrição



Anexa um ficheiro a um documento FI (Financial Accounting) específico no SAP ECC / S/4HANA através de uma RFC (Remote Function Call). É útil para lançar documentação de suporte — faturas digitalizadas, fluxos de aprovação, cópias de contratos — juntamente com os lançamentos financeiros a que dão suporte.

Requer as credenciais RFC do SAP configuradas no conector SAP e o número do documento FI de destino (empresa, número do documento, exercício).


## O que é verificado ao guardar

O passo lê o caminho de cada ficheiro a partir de uma coluna `relative_file_path` entre as colunas de saída no separador **Seleção de dados da tabela**, e essa coluna tem de ser de texto. A gravação é recusada se não existir — *The output columns must include relative_file_path, the path of each file to attach.* — ou se tiver outro tipo — *The relative_file_path column must be text, not integer.*

Ao guardar com uma tabela de origem escolhida mas sem colunas de origem ou de destino, o lado vazio é preenchido a partir da origem, tal como faria **Preencher ambas as tabelas de mapeamento**.


## Exemplos


### Parâmetros RFC


Selecione o **Agente a utilizar**. Selecione o **Diretório de destino** na lista pendente e navegue abaixo até à subpasta de destino correta para o ficheiro. Em seguida, atribua um nome adequado ao "Nome do ficheiro de destino". Em "Informações da chamada de função", introduza a função e o **Parâmetro do valor de retorno**, e selecione os parâmetros.



Pode optar por **Inserir linha** ou **Acrescentar linha** na secção de parâmetros, bem como dar nome aos parâmetros e atribuir-lhes valores. Escolha o número em **Máximo de pedidos simultâneos** e selecione "Aguardar a conclusão da RFC". **Guardar e executar passo**.
