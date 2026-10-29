---
title: Passos de importação
description: Passos de fluxo de trabalho que trazem dados de origens externas para tabelas de projeto.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/import/index.md
---

Passos de fluxo de trabalho que trazem dados de origens externas para tabelas de projeto.

Uma importação de ficheiros verifica a consulta que carrega a respetiva tabela de destino antes de ser executada. Uma consulta que contenha algo diferente de uma instrução SQL simples sobre colunas com tipo é recusada antes de a tabela de destino ser criada, substituída ou carregada, pelo que a tabela fica exatamente como estava.

Um ficheiro de origem em falta não é um erro. A importação emite um aviso com o caminho e deixa a tabela de destino vazia com as colunas declaradas, pelo que os passos seguintes leem zero linhas. Isto aplica-se às importações de CSV, Excel, JSON, largura fixa, YXDB, dBASE, ORC, Avro, Parquet, XML e extração Db2. Uma importação de XML com etiquetas cria uma tabela vazia apenas para cada etiqueta que declare campos. As importações de arquivo e de Access também emitem um aviso, mas não declaram colunas, pelo que não criam nenhuma tabela. Uma importação de arquivo que encontra os seus ficheiros através de uma pesquisa de documentos não emite aviso de ficheiro em falta.

O mesmo acontece antes de um passo ser executado. **Preencher** no mapeamento de uma importação de ficheiros, e a leitura das colunas de um ficheiro através da API REST ou de um assistente de IA, respondem *Nada para preencher* (uma lista de colunas vazia através da API) com um aviso que indica o caminho quando o ficheiro está em falta ou vazio, em vez de um erro. Importar um ficheiro em falta para uma nova tabela ou passo a partir de Documentos não cria nada, marca o ficheiro como **ignorado** e mostra um aviso que indica o caminho.

## Passos

- [Importar Access](/pt-pt/reference/workflow-steps/import/import-access/)
- [Importar Alteryx YXDB](/pt-pt/reference/workflow-steps/import/import-alteryx-yxdb/)
- [Importar arquivo](/pt-pt/reference/workflow-steps/import/import-archive/)
- [Importar Avro](/pt-pt/reference/workflow-steps/import/import-avro/)
- [Importar CSV](/pt-pt/reference/workflow-steps/import/import-csv/)
- [Importar Delta Lake](/pt-pt/reference/workflow-steps/import/import-delta/)
- [Importar extração DB2](/pt-pt/reference/workflow-steps/import/import-db2-extract/)
- [Importar dBASE](/pt-pt/reference/workflow-steps/import/import-dbf/)
- [Importar Excel](/pt-pt/reference/workflow-steps/import/import-excel/)
- [Importar delimitado](/pt-pt/reference/workflow-steps/import/import-delimited/)
- [Importar tabelas de bases de dados externas](/pt-pt/reference/workflow-steps/import/import-external-database-tables/)
- [Importar largura fixa](/pt-pt/reference/workflow-steps/import/import-fixed-width/)
- [Importar Google BigQuery](/pt-pt/reference/workflow-steps/import/import-google-bigquery/)
- [Importar folha de cálculo Google](/pt-pt/reference/workflow-steps/import/import-google-spreadsheet/)
- [Importar HDF](/pt-pt/reference/workflow-steps/import/import-hdf/)
- [Importar JSON](/pt-pt/reference/workflow-steps/import/import-json/)
- [Importar Kafka](/pt-pt/reference/workflow-steps/import/import-kafka/)
- [Importar Monday](/pt-pt/reference/workflow-steps/import/import-monday/)
- [Importar MongoDB](/pt-pt/reference/workflow-steps/import/import-mongodb/)
- [Importar ORC](/pt-pt/reference/workflow-steps/import/import-orc/)
- [Importar Parquet](/pt-pt/reference/workflow-steps/import/import-parquet/)
- [Importar tabela de projeto](/pt-pt/reference/workflow-steps/import/import-project-table/)
- [Importar Quandl](/pt-pt/reference/workflow-steps/import/import-quandl/)
- [Importar: Origem Singer](/pt-pt/reference/workflow-steps/import/import-singer/)
- [Importar SPSS](/pt-pt/reference/workflow-steps/import/import-spss/)
- [Importar SQL](/pt-pt/reference/workflow-steps/import/import-sql/)
- [Importar Stata](/pt-pt/reference/workflow-steps/import/import-stata/)
- [Importar XML](/pt-pt/reference/workflow-steps/import/import-xml/)
- [Restaurar tabelas](/pt-pt/reference/workflow-steps/import/restore-tables/)
