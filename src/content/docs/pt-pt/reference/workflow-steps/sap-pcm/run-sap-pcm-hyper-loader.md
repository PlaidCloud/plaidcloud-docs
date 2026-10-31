---
title: Run SAP PCM Hyper Loader
description: Execute o SAP PCM Hyper Loader a partir de um passo de fluxo de trabalho do PlaidCloud, para realizar carregamentos de dados em massa de alta velocidade em modelos PCM.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader.md
---

## Descrição


Carrega um modelo do SAP Profitability and Cost Management (PCM) através de carregamentos diretos de tabelas. Este processo é significativamente mais rápido do que o Databridge. O Hyper Loader suporta praticamente todas as tabelas atuais de dados, atribuições e estrutura do PCM.


Esta é a lista atual de destinos de carregamento disponíveis:



* Activity Aliases
* Activity Dimensional Hierarchy
* Activity Driver Aliases
* Activity Driver Dimensional Hierarchy
* Activity Driver Value
* BOM Default Makeup
* BOM External Unit Rate
* BOM Makeup
* BOM Production Volume
* BOM Units Sold
* Cost Object 1 Aliases
* Cost Object 1 Dimensional Hierarchy
* Cost Object 2 Aliases
* Cost Object 2 Dimensional Hierarchy
* Cost Object 3 Aliases
* Cost Object 3 Dimensional Hierarchy
* Cost Object 4 Aliases
* Cost Object 4 Dimensional Hierarchy
* Cost Object 5 Aliases
* Cost Object 5 Dimensional Hierarchy
* Cost Object Assignment
* Cost Object Driver
* Line Item Aliases
* Line Item Detail Aliases
* Line Item Detail Dimensional Hierarchy
* Line Item Detail Value
* Line Item Dimensional Hierarchy
* Line Item Direct Activity Assignment
* Line Item Resource Driver Assignment
* Line Item Value
* Period Aliases
* Period Dimensional Hierarchy
* Resource Driver Aliases
* Resource Driver Dimensional Hierarchy
* Resource Driver Split
* Resource Driver Value
* Responsibility Center Aliases
* Responsibility Center Dimensional Hierarchy
* Revenue
* Revenue Aliases
* Revenue Dimensional Hierarchy
* Service Aliases
* Service Dimensional Hierarchy
* Spread Aliases
* Spread Dimensional Hierarchy
* Spread Value
* Version Aliases
* Version Dimensional Hierarchy
* Worksheet 1 Aliases
* Worksheet 1 Dimensional Hierarchy
* Worksheet 2 Aliases
* Worksheet 2 Dimensional Hierarchy
* Worksheet Value

## As nossas credenciais


O PlaidCloud é um parceiro oficial da SAP e um fornecedor preferencial de serviços relacionados com a conceção e a implementação de modelos SAP PCM.


## O que é verificado ao guardar

Cada origem do separador **Load Steps** é preparada na tabela de carregamento escolhida como **Target Load Table**, associada por nome de coluna. Guardar é recusado, com indicação da origem, quando:

- Uma origem não tem Target Load Table, ou tem uma que não é uma tabela de carregamento do PCM — *Source 'activity_aliases' loads into 'ACTIVITY', which isn't a PCM loader table.*
- As colunas de uma origem não correspondem à respetiva tabela de carregamento: falta uma coluna da tabela de carregamento, tem um tipo diferente do da tabela de carregamento, ou não tem origem, expressão nem constante — *Source 'activity_aliases' doesn't match loader table PPLOAD_ACTIVITY_AL: missing DEFAULTALIAS; no source, expression or constant for ALIAS.* **Reset Target Columns to Schema** volta a preencher as colunas de destino de uma origem a partir da respetiva tabela de carregamento.
- Duas origens partilham um nome. Cada origem é exportada para um ficheiro com o seu nome, pelo que uma substituiria a outra — *Source name 'activity_aliases' is used more than once; each source needs its own, or one overwrites the other.*


## Exemplos


Selecione Agente a utilizar na lista pendente. Introduza o nome do modelo e selecione a localização do caminho de armazenamento do pacote de carregamento e, depois, a subpasta pretendida dentro dele. Utilize a Table Data Selection abaixo para selecionar a tabela de origem do modelo e a tabela de carregamento de destino. Inspecionar a origem>>propagar ambos os lados da tabela revelará os dados. Clique em “Save and Run Step” quando os dados estiverem introduzidos e tiver adicionado quaisquer expressões.
