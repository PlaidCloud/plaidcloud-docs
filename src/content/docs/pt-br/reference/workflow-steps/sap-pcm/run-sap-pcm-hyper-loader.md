---
title: Etapa Run SAP PCM Hyper Loader
description: Execute o SAP PCM Hyper Loader a partir de uma etapa de fluxo de trabalho do PlaidCloud para carregar dados em massa em alta velocidade nos modelos do PCM.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader.md
---

## Descrição


Carrega um modelo do SAP Profitability and Cost Management (PCM) usando cargas diretas de tabelas. Esse processo é significativamente mais rápido que o Databridge. O Hyper Loader oferece suporte a praticamente todas as tabelas atuais de dados, atribuições e estrutura do PCM.


Esta é a lista atual de destinos de carga disponíveis:


* Aliases de atividade
* Hierarquia dimensional de atividade
* Aliases de direcionador de atividade
* Hierarquia dimensional de direcionador de atividade
* Valor do direcionador de atividade
* Composição padrão da lista de materiais
* Taxa unitária externa da lista de materiais
* Composição da lista de materiais
* BOM Production Volume
* Unidades vendidas da lista de materiais
* Aliases do objeto de custo 1
* Hierarquia dimensional do objeto de custo 1
* Aliases do objeto de custo 2
* Hierarquia dimensional do objeto de custo 2
* Aliases do objeto de custo 3
* Hierarquia dimensional do objeto de custo 3
* Aliases do objeto de custo 4
* Hierarquia dimensional do objeto de custo 4
* Aliases do objeto de custo 5
* Hierarquia dimensional do objeto de custo 5
* Atribuição de objeto de custo
* Direcionador de objeto de custo
* Aliases de item de linha
* Aliases de detalhe de item de linha
* Hierarquia dimensional de detalhe de item de linha
* Valor de detalhe de item de linha
* Hierarquia dimensional de item de linha
* Atribuição direta de atividade de item de linha
* Atribuição de direcionador de recurso de item de linha
* Valor de item de linha
* Aliases de período
* Hierarquia dimensional de período
* Aliases de direcionador de recurso
* Hierarquia dimensional de direcionador de recurso
* Divisão de direcionador de recurso
* Valor de direcionador de recurso
* Aliases de centro de responsabilidade
* Hierarquia dimensional de centro de responsabilidade
* Receita
* Aliases de receita
* Hierarquia dimensional de receita
* Aliases de serviço
* Hierarquia dimensional de serviço
* Aliases de distribuição
* Hierarquia dimensional de distribuição
* Valor de distribuição
* Aliases de versão
* Hierarquia dimensional de versão
* Aliases da planilha 1
* Hierarquia dimensional da planilha 1
* Aliases da planilha 2
* Hierarquia dimensional da planilha 2
* Valor da planilha

## Nossas credenciais


A PlaidCloud é uma parceira oficial da SAP e fornecedora preferencial de serviços relacionados ao projeto e à implementação de modelos do SAP PCM.


## O que é verificado ao salvar

Cada origem na guia **Etapas de carga** é carregada na tabela de carga escolhida como **Tabela de carga de destino**, com correspondência pelo nome da coluna. O salvamento é recusado, com o nome da origem, quando:

- Uma origem não tem Tabela de carga de destino, ou tem uma que não é uma tabela de carga do PCM — *Source 'activity_aliases' loads into 'ACTIVITY', which isn't a PCM loader table.*
- As colunas de uma origem não correspondem à tabela de carga: falta uma coluna da tabela de carga, ela tem um tipo diferente do da tabela de carga ou não tem origem, expressão nem constante — *Source 'activity_aliases' doesn't match loader table PPLOAD_ACTIVITY_AL: missing DEFAULTALIAS; no source, expression or constant for ALIAS.* **Redefinir colunas de destino para o esquema** preenche novamente as colunas de destino de uma origem a partir da tabela de carga.
- Duas origens têm o mesmo nome. Cada origem é exportada para um arquivo com o nome dela, então uma sobrescreveria a outra — *Source name 'activity_aliases' is used more than once; each source needs its own, or one overwrites the other.*


## Exemplos


Selecione o Agente a usar na lista suspensa. Informe o nome do modelo e selecione o local do caminho de armazenamento do pacote de carga; depois, selecione a pasta filha desejada dentro dele. Use a Seleção de dados da tabela abaixo para selecionar a tabela de origem do modelo e a tabela de carga de destino. Inspecionar origem>>propagar mostrará os dados nos dois lados da tabela. Clique em “Salvar e executar etapa” quando os dados estiverem informados e você tiver adicionado as expressões necessárias.
