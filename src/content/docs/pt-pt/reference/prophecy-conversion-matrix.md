---
title: Matriz de conversão do Prophecy
description: Como o PlaidCloud converte pipelines e projetos SQL do Prophecy em passos nativos de fluxos de trabalho avançados, com o estado de suporte de cada gem.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/prophecy-conversion-matrix.md
---

O PlaidCloud converte pipelines Spark e projetos SQL do Prophecy em fluxos de trabalho
avançados nativos. O importador mapeia cada gem do Prophecy para um passo de fluxo de trabalho,
uma variável de projeto ou um objeto da área de desenho, pelo que um fluxo de trabalho convertido é executado de forma nativa na nuvem
e não como uma emulação.

Todas as gems, conectores e estruturas de projeto são convertidos: **Completo** significa que a gem
se torna um passo, uma variável ou um objeto de área de desenho nativo do PlaidCloud que executa o trabalho
da gem. Os poucos comportamentos que um fluxo de trabalho convertido não reproduz por si
estão listados em [Casos limite conhecidos](#casos-limite-conhecidos), cada um com o que
fazer.

Para executar uma conversão, consulte [Migrar projetos do Prophecy](/pt-pt/guides/workflows/migrate-prophecy-projects/).

## Gems de pipelines Spark

### Origem/Destino

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Lookup | Completo | [Pesquisa](/pt-pt/reference/workflow-steps/tables/table-lookup/) | Cada chamada de pesquisa torna-se um passo Pesquisa no passo que a utiliza; uma chave sem correspondência devolve NULL e uma chave duplicada devolve uma das suas linhas. |
| Source | Completo | Passo de importação escolhido pelo formato do conjunto de dados (consulte [Conectores](#conectores)) | Cada Source torna-se um passo de importação para uma tabela com o nome do conjunto de dados; um formato que o conversor não reconhece é lido como um ficheiro CSV carregado para a pasta de documentos do fluxo de trabalho, com um aviso. |
| Streaming Source | Completo | A mesma importação que um Source em lote | Os sources de streaming são convertidos numa importação em lote única, com um aviso. |
| Streaming Target | Completo | Carregamento em lote com acréscimo | Os targets de streaming são convertidos num acréscimo em lote, com um aviso. |
| Target | Completo | Passo de exportação/carregamento de tabela escolhido pelo formato do conjunto de dados e por writeMode | Cada Target torna-se um passo de carregamento ou exportação de tabela no modo de escrita da gem: acréscimo, substituição, fusão com as respetivas expressões SET, upsert, SCD2, replaceWhere e insertInto. |

### Preparar

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Data Cleansing | Completo | Expressões de coluna num passo [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Converte as opções de preenchimento de nulos, remoção de espaços e capitalização em expressões de coluna; as colunas limpas passam para o fim. |
| Sequence | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com uma expressão de número de linha | Acrescenta uma coluna de sequência a partir do valor inicial e do incremento. |
| Surrogate Key Generator | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com uma expressão de número de linha | Acrescenta uma chave sequencial a partir do valor inicial; as chaves continuam entre execuções a partir de uma tabela que guarda a última chave emitida. |

### Transformar

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Aggregate | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com agregação; [Pivot](/pt-pt/reference/workflow-steps/tables/table-pivot/) quando a gem faz pivô | Agrupa e agrega, aplica a condição HAVING e faz o pivô para uma coluna por valor de pivô; propagate-all transporta todas as outras colunas de entrada. |
| Bulk Column Expressions | Completo | Expande para uma expressão por coluna num passo [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Uma expressão por coluna listada num passo Table Extract; a conversão avisa que se presume o esquema da gem. |
| Bulk Column Rename | Completo | Mudança de nome de coluna num passo [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Uma mudança de nome por coluna listada num passo Table Extract; a conversão avisa que se presume o esquema da gem. |
| Deduplicate | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com distinct ou um filtro de número de linha | Mantém uma linha por chave: distinct, a primeira ou a última segundo a sua ordem de ordenação, qualquer uma, ou apenas as chaves que ocorrem uma vez. |
| Dynamic Replace | Completo | Transformação de substituição dinâmica, configurada manualmente | Converte-se em regras de substituição na transformação de substituição dinâmica; a conversão avisa que se presume o esquema da gem. |
| Dynamic Select | Completo | Seleção de colunas num passo [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) resolvida por tipo | Resolve as colunas por tipo no momento da conversão numa seleção explícita. |
| Filter | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com uma expressão de filtro | Converte-se num passo Table Extract com uma expressão de filtro; as condições NULL eliminam a linha. |
| Flatten Schema | Completo | [Analisar JSON](/pt-pt/reference/workflow-steps/tables/table-json-parse/) e [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Aplana os campos aninhados em colunas com o nome formado pelo delimitador da gem e expande as matrizes numa linha por elemento. |
| Fuzzy Match | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) e [User Defined Transform](/pt-pt/reference/workflow-steps/general/user-defined-transform/) | Emparelha os registos, pontua cada campo de correspondência pelo método da gem, calcula a média das pontuações e mantém os pares iguais ou superiores ao seu limiar. |
| Group By Rollup | Completo | União de passos de agregação [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) por nível de rollup | Expande o rollup numa agregação por nível de agrupamento, unidas com subtotais NULL. |
| Limit | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com um limite de linhas | Converte-se num limite de linhas; as referências de configuração tornam-se variáveis de projeto. |
| Normalize | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com uma expressão de expansão | Repete cada registo segundo a expressão de comprimento, calcula as colunas de saída por índice e para no primeiro índice em que a condição de conclusão se verifica. |
| Order By | Completo | Ordenação num passo [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Converte-se numa ordenação com as mesmas chaves, direção e posição dos nulos. |
| Reformat | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com expressões de coluna | Converte-se num passo Table Extract com uma expressão por coluna de saída; as colunas não listadas são eliminadas. |
| Sample Rows | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com um limite de linhas ou amostra aleatória | Mantém uma fração ou um número aleatório de linhas; as linhas escolhidas diferem da execução em Spark porque a amostragem é aleatória. |
| Schema Transform | Completo | Cadeia de passos [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) aplicados por ordem | Aplica cada operação por ordem: acrescentar ou substituir uma coluna, eliminar, mudar o nome, acrescentar se estiver em falta com o seu valor predefinido e acrescentar uma regra de negócio do projeto. |
| Set Operation | Completo | [União total](/pt-pt/reference/workflow-steps/tables/table-union-all/); [Anti-junção](/pt-pt/reference/workflow-steps/tables/table-anti-join/) para except; [Junção interna](/pt-pt/reference/workflow-steps/tables/table-inner-join/) para intersect | Union all empilha as entradas; except all e intersect all mantêm o número correto de linhas duplicadas. |
| TransposeAgg | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com agregação | Converte o agrupamento, as agregações e o pivô da gem como um Aggregate, com um aviso para o rever. |
| Unpivot | Completo | [Melt](/pt-pt/reference/workflow-steps/tables/table-melt/) | Empilha as colunas selecionadas em colunas de nome e de valor. |
| Watermark | Completo | Não é necessário nenhum passo | Descartado: uma execução em lote lê todos os dados presentes, pelo que não há limite de dados tardios a aplicar. |
| Window Function | Completo | Expressões de janela num passo [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Acrescenta colunas de janela com a partição, a ordem e o quadro da gem, em linhas ou intervalo, com limites ilimitados, na linha atual ou com deslocamento. |

### Junção/Divisão

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Compare Columns | Completo | Junção externa completa mais agregações por coluna | Compara as colunas através de uma junção externa completa dos dados desagregados, com contagens de correspondências e de divergências. |
| Join | Completo | [Junção interna](/pt-pt/reference/workflow-steps/tables/table-inner-join/), [Junção de várias tabelas](/pt-pt/reference/workflow-steps/tables/table-multi-table-join/), [Anti-junção](/pt-pt/reference/workflow-steps/tables/table-anti-join/) ou [Junção cruzada](/pt-pt/reference/workflow-steps/tables/table-cross-join/) | Constrói a junção de cada tipo, interna, à esquerda, à direita, completa, semi, anti, cruzada e natural, com qualquer condição de junção, aplica a cláusula where e escreve a lista de seleção. |
| Repartition | Completo | Não é necessário nenhum passo | Descartado: o PlaidCloud gere a partição, pelo que o passo seguinte lê diretamente a tabela a montante. |
| Row Distributor | Completo | Um filtro [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) por saída | Converte-se num filtro por saída; as linhas podem terminar em várias saídas. |

### Análise

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Column Parser | Completo | [Analisar JSON](/pt-pt/reference/workflow-steps/tables/table-json-parse/) / [Análise de XML](/pt-pt/reference/workflow-steps/tables/table-xml-parse/) | Converte-se numa análise de JSON ou XML da coluna indicada; a conversão avisa que se presume o esquema da gem. |

### Personalizado

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Custom Gem (Gem Builder) | Completo | [User Defined Transform](/pt-pt/reference/workflow-steps/general/user-defined-transform/) que executa o código gerado da gem | O código PySpark gerado da gem, a partir da exportação do pipeline, é executado num passo Python, com um aviso para o rever. |
| CustomReformatBitbucket | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Converte-se como o Reformat cujas expressões a gem contém, com um aviso para o rever. |
| Data Quality Check | Completo | [União total](/pt-pt/reference/workflow-steps/tables/table-union-all/) de uma linha de resultado por verificação; [Gerar erro de fluxo de trabalho](/pt-pt/reference/workflow-steps/workflow-control/raise-workflow-error/) para parar em caso de falhas | Avalia cada verificação sobre a entrada e escreve uma linha de resultado por verificação, com o respetivo estado e mensagem. Os dados passam sem alterações e a execução pára quando o limiar de falhas da gem é atingido. |
| Deequ | Completo | Verificações [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Transmite os dados e constrói a tabela de resultados das restrições para as regras isComplete, isUnique, isNonNegative e isContainedIn. |
| Delta Table Operations | Completo | [Table In-Place Delete](/pt-pt/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/pt-pt/reference/workflow-steps/tables/table-update/), [Table Drop](/pt-pt/reference/workflow-steps/tables/table-drop/), [Table Restore to Timestamp](/pt-pt/reference/workflow-steps/tables/table-restore-timestamp/) | Eliminar, atualizar, remover e restaurar para uma marca temporal correspondem a passos de tabela; otimizar, vacuum e restaurar por versão transmitem os dados com um aviso. |
| Directory | Completo | [Listagem de diretório](/pt-pt/reference/workflow-steps/document/directory-listing/) | Lista os ficheiros da pasta de documentos associada nas colunas da gem; com a opção de nome da folha, cada livro produz uma linha por folha. Uma pasta em falta produz zero linhas. |
| Email | Completo | [Notify Via Email](/pt-pt/reference/workflow-steps/notifications/notify-via-email/) | Envia a mensagem de correio eletrónico, com um anexo de dados opcional, através de uma ligação de correio eletrónico associada. |
| Email Data | Completo | [Notify Via Email](/pt-pt/reference/workflow-steps/notifications/notify-via-email/) | Envia por correio eletrónico as linhas de entrada como tabela e transmite a entrada sem alterações. |
| File Operation | Completo | [Copy Document File](/pt-pt/reference/workflow-steps/document/copy-document-file/) ou [Copy Document Directory](/pt-pt/reference/workflow-steps/document/copy-document-directory/) | Copia, move ou sincroniza ficheiros da pasta de documentos associada para a pasta de documentos do fluxo de trabalho convertido; uma movimentação remove os ficheiros de origem. |
| Log | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Escreve a linha de evento da gem (hora, nome da gem, tipo de evento e texto) na sua tabela de saída. |
| REST API Enrich | Completo | [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) | Chama a API uma vez por linha e acrescenta as colunas da resposta. |
| Script | Completo | Passo Python com reescrita do acesso a frames | Incorpora o corpo do script num passo Python, com o acesso a data frames reescrito; os corpos em Scala são mantidos com uma nota. |
| Soda Data Quality Check | Completo | Verificações [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Constrói a tabela de resultados das verificações a partir das verificações Soda. |
| SQL Statement | Completo | Passo SQL por separador de saída, com o texto traduzido para o dialeto do inquilino | Incorpora cada separador como um passo SQL com as entradas associadas como tabelas temporárias; traduzido para o dialeto do inquilino. |
| Todo | Completo | [Gerar erro de fluxo de trabalho](/pt-pt/reference/workflow-steps/workflow-control/raise-workflow-error/) ou [Notify via Log](/pt-pt/reference/workflow-steps/notifications/notify-via-log/) | Assinala lógica ainda por escrever: uma mensagem de registo quando nada a lê, ou um passo que pára a execução com a mensagem da gem quando um passo posterior depende dela. |

### Relatório

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Tableau | Completo | [Publish to Tableau](/pt-pt/reference/workflow-steps/export/export-to-tableau/) | Escreve uma extração Hyper e publica-a na ligação Tableau associada. |

### ML/IA

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Bedrock | Completo | [Text NLP AI](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) | Incorpora a coluna de texto através da ligação de IA da área de trabalho. |
| OpenAI | Completo | [Text NLP AI](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) | Responde a perguntas ou incorpora texto através da ligação de IA da área de trabalho. |
| Pinecone Lookup | Completo | [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) | Consulta o índice Pinecone para cada linha e acrescenta as colunas pinecone_matches e pinecone_error. |
| SageMaker Endpoint | Completo | [Text NLP AI](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) | Responde a perguntas através da ligação de IA da área de trabalho. |
| Text Processing | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) para divisão em blocos; [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) para recolha de dados da Web | A divisão em blocos torna-se uma expressão de blocos de carateres; a recolha de dados da Web obtém o URL de cada linha e junta o conteúdo da página de volta à linha. |

### Subgrafo/Controlo

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Control Flow Input | Completo | Descartado (apenas marcador de limite) | Descartado; apenas assinala o limite de entrada do subfluxo de trabalho do iterador. |
| Control Flow Output | Completo | Descartado (apenas marcador de limite) | Descartado; apenas assinala o limite de saída do subfluxo de trabalho do iterador. |
| Subgraph (Basic) | Completo | Contentor da área de desenho / fluxo de trabalho aninhado a partir de processos em linha | Converte o grafo interno em linha num fluxo de trabalho aninhado (ou em passos incorporados) com parâmetros de tabela de entrada/saída. |
| Table Iterator | Completo | [Workflow Loop](/pt-pt/reference/workflow-steps/workflow-control/workflow-loop/) | Executa o corpo do ciclo uma vez por linha de entrada, definindo cada valor de configuração a partir da respetiva coluna, até maxIteration. |
| While Iterator | Completo | [Workflow Loop](/pt-pt/reference/workflow-steps/workflow-control/workflow-loop/) | Executa o corpo do ciclo uma vez por passagem, transmitindo o número da iteração, até o corpo não devolver linhas ou o máximo da gem ser atingido. |

## Gems de SQL / Analyst

### Origem/Destino

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| External table Source/Target (BigQuery, Databricks, SAP HANA, MongoDB, MSSQL, Oracle, Postgres, Redshift, Salesforce, Snowflake, Synapse) | Completo | Passo de importação/exportação de dados externos com a ligação de base de dados correspondente | Lê ou escreve uma tabela numa base de dados externa através de uma ligação do PlaidCloud. |
| File storage Source/Target (ADLS, Databricks Volumes, GCS, OneDrive, S3, SFTP, SharePoint, Smartsheet) | Completo | Passos de importação/exportação de ficheiros numa conta de documentos (ADLS/GCS/S3/SFTP/SharePoint/OneDrive) | Lê ou escreve ficheiros em armazenamento na nuvem/SFTP com união por carateres universais, acionador, eliminação/movimentação e opções de encriptação. |
| Model | Completo | Tabela de saída do passo a montante | Lê outro modelo como a tabela produzida pelo passo a montante referenciado. |
| Seed | Completo | [Importar: CSV](/pt-pt/reference/workflow-steps/import/import-csv/) | O CSV de seed é importado para uma tabela do PlaidCloud. |
| Source | Completo | Passo de importação escolhido pelo formato do conjunto de dados (consulte [Conectores](#conectores)) | Cada Source torna-se um passo de importação para uma tabela com o nome do conjunto de dados; um formato que o conversor não reconhece é lido como um ficheiro CSV carregado para a pasta de documentos do fluxo de trabalho, com um aviso. |
| Target Model / Table (Target) | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/), [Upsert](/pt-pt/reference/workflow-steps/tables/table-upsert/), [Copiar tabela](/pt-pt/reference/workflow-steps/tables/table-copy/) e [União total](/pt-pt/reference/workflow-steps/tables/table-union-all/) | Escreve a seleção final do modelo numa tabela do PlaidCloud como substituição, acréscimo, upsert, eliminação e inserção, SCD2 ou substituição por predicado. |
| Upload Files | Completo | [Importar: CSV](/pt-pt/reference/workflow-steps/import/import-csv/) | Os ficheiros locais carregados tornam-se uma tabela através de um passo de importação. |

### Preparar

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Data Cleansing | Completo | Expressões de coluna num passo [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Converte as opções de preenchimento de nulos, remoção de espaços e capitalização em expressões de coluna; as colunas limpas passam para o fim. |
| Data Masking | Completo | Expressões de coluna para mascaramento de carateres ou hash | Mascara ou aplica hash às colunas de texto selecionadas no local ou como colunas novas. |
| Find Duplicates | Completo | Expressão de janela de número de linha mais filtro | Devolve as linhas únicas, duplicadas ou selecionadas por contagem/posição, por chave. |
| Generate Rows | Completo | Tabela de sequência associada e filtrada por linha de entrada | Gera linhas por linha de entrada a partir das expressões de inicialização, condição e ciclo. |
| Imputation | Completo | Agregação mais reassociação e expressão de coluna | Substitui nulos ou valores sentinela pela média, mediana, moda ou um valor fixo. |
| Multi-Column Edit | Completo | Expressões por coluna expandidas a partir do modelo | Aplica um modelo de expressão a todas as colunas selecionadas. |
| Multi-Column Rename | Completo | Mapeamento de mudança de nome de colunas num passo de seleção | Muda o nome das colunas selecionadas por prefixo, sufixo ou expressão de nome. |
| Record ID | Completo | Expressão de coluna de número de linha ou uuid | Acrescenta uma coluna de ID de registo UUID ou sequencial. |
| Sample | Completo | Limite de linhas ou opção de amostra na extração | Toma as primeiras/últimas/aleatórias/N-ésimas/percentagem de linhas no total ou por grupo. |
| Tile | Completo | Expressões de janela para o número do escalão e a sequência | Atribui números de escalão por soma igual, contagem, bandas de desvio-padrão, valores distintos ou limites manuais. |

### Transformar

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Aggregate | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com agregação; [Pivot](/pt-pt/reference/workflow-steps/tables/table-pivot/) quando a gem faz pivô | Agrupa e agrega, aplica a condição HAVING e faz o pivô para uma coluna por valor de pivô; propagate-all transporta todas as outras colunas de entrada. |
| Count Records | Completo | Passo de agregação com funções de contagem | Devolve contagens totais, não nulas ou distintas numa linha. |
| Data Encoder/Decoder | Completo | Expressões de coluna para codificação e descodificação base64/hex | Codifica ou descodifica as colunas selecionadas; AES apenas no Databricks. |
| Deduplicate | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com distinct ou um filtro de número de linha | Mantém uma linha por chave: distinct, a primeira ou a última segundo a sua ordem de ordenação, qualquer uma, ou apenas as chaves que ocorrem uma vez. |
| Dynamic Select | Completo | Seleção de colunas num passo [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) resolvida por tipo | Resolve as colunas por tipo no momento da conversão numa seleção explícita. |
| Filter | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com uma expressão de filtro | Converte-se num passo Table Extract com uma expressão de filtro; as condições NULL eliminam a linha. |
| Finance | Completo | Expressão de coluna que implementa a função financeira | Acrescenta o resultado de uma função financeira (FV, PV, NPV, IRR, ...) como uma coluna nova. |
| Flatten Schema | Completo | [Analisar JSON](/pt-pt/reference/workflow-steps/tables/table-json-parse/) e [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Aplana os campos aninhados em colunas com o nome formado pelo delimitador da gem e expande as matrizes numa linha por elemento. |
| Fuzzy Match | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) e [User Defined Transform](/pt-pt/reference/workflow-steps/general/user-defined-transform/) | Emparelha os registos, pontua cada campo de correspondência pelo método da gem, calcula a média das pontuações e mantém os pares iguais ou superiores ao seu limiar. |
| Limit | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com um limite de linhas | Converte-se num limite de linhas; as referências de configuração tornam-se variáveis de projeto. |
| Order By | Completo | Ordenação num passo [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Converte-se numa ordenação com as mesmas chaves, direção e posição dos nulos. |
| Pivot | Completo | [Pivot](/pt-pt/reference/workflow-steps/tables/table-pivot/) | Transforma os valores de pivô selecionados em colunas de agregações; uma lista de valores do modo Simple obtida em tempo de conceção é convertida como os valores listados. |
| Reformat | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com expressões de coluna | Converte-se num passo Table Extract com uma expressão por coluna de saída; as colunas não listadas são eliminadas. |
| Running Total | Completo | Coluna de expressão de janela de soma cumulativa | Acrescenta somas cumulativas por coluna selecionada. |
| Snowflake Unpivot (third-party) | Completo | [Melt](/pt-pt/reference/workflow-steps/tables/table-melt/) | Desagrega colunas através de UNPIVOT do Snowflake. |
| Transpose | Completo | [Melt](/pt-pt/reference/workflow-steps/tables/table-melt/) | Empilha colunas de dados em colunas de nome e de valor de texto. |
| TransposeAgg | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com agregação | Converte o agrupamento, as agregações e o pivô da gem como um Aggregate, com um aviso para o rever. |
| Unpivot | Completo | [Melt](/pt-pt/reference/workflow-steps/tables/table-melt/) | Empilha colunas de dados em colunas de nome e de valor. |
| Weighted Average | Completo | Passo de agregação com expressão de média ponderada | Calcula uma média ponderada no total ou por grupo. |
| Window Function | Completo | Expressões de janela num passo [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Acrescenta colunas de janela com a partição, a ordem e o quadro da gem, em linhas ou intervalo, com limites ilimitados, na linha atual ou com deslocamento. |

### Junção/Divisão

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Except | Completo | [Anti-junção](/pt-pt/reference/workflow-steps/tables/table-anti-join/) em todas as colunas mais um [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) distinct | Mantém as linhas da primeira entrada que não aparecem em nenhuma das outras entradas. |
| Intersect | Completo | [Junção interna](/pt-pt/reference/workflow-steps/tables/table-inner-join/) em todas as colunas mais Distinct | Mantém as linhas presentes em todas as entradas. |
| Join | Completo | [Junção interna](/pt-pt/reference/workflow-steps/tables/table-inner-join/), [Junção de várias tabelas](/pt-pt/reference/workflow-steps/tables/table-multi-table-join/), [Anti-junção](/pt-pt/reference/workflow-steps/tables/table-anti-join/) ou [Junção cruzada](/pt-pt/reference/workflow-steps/tables/table-cross-join/) | Constrói a junção de cada tipo, interna, à esquerda, à direita, completa, semi, anti, cruzada e natural, com qualquer condição de junção, aplica a cláusula where e escreve a lista de seleção. |
| Union | Completo | [União total](/pt-pt/reference/workflow-steps/tables/table-union-all/) | Empilha as entradas por posição, removendo duplicados quando a gem não os mantém. |
| Union By Name | Completo | [União total](/pt-pt/reference/workflow-steps/tables/table-union-all/) | Torna-se uma União total que alinha as colunas por nome e preenche com nulos as que estão em falta. |

### Análise

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| JSON Parse | Completo | [Analisar JSON](/pt-pt/reference/workflow-steps/tables/table-json-parse/) | Analisa uma coluna de texto JSON em campos estruturados. |
| Regex | Completo | Expressões regulares num passo Table Extract / Transform | Substitui, analisa, faz corresponder ou segmenta uma coluna de texto com uma expressão regular. |
| Text To Columns | Completo | Passos de divisão de coluna / expansão com delimitador de expressão regular | Divide uma coluna delimitada em colunas ou linhas usando um delimitador de expressão regular. |
| XML Parse | Completo | [Análise de XML](/pt-pt/reference/workflow-steps/tables/table-xml-parse/) | Analisa uma coluna de texto XML em campos estruturados. |

### Personalizado

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Directory | Completo | [Listagem de diretório](/pt-pt/reference/workflow-steps/document/directory-listing/) | Lista os ficheiros da pasta de documentos associada nas colunas da gem; com a opção de nome da folha, cada livro produz uma linha por folha. Uma pasta em falta produz zero linhas. |
| DynamicInput | Completo | Passo SQL para modelos de consulta; ciclo de fluxo de trabalho para o modo de vários ficheiros | O modo de modelo de consulta incorpora o modelo como um passo SQL; o modo de vários ficheiros é mapeado com pressupostos. |
| Email | Completo | [Notify Via Email](/pt-pt/reference/workflow-steps/notifications/notify-via-email/) | Envia a mensagem de correio eletrónico, com um anexo de dados opcional, através de uma ligação de correio eletrónico associada. |
| RestAPI | Completo | [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) | Envia um pedido por linha de entrada com o seu URL, cabeçalhos, consulta, corpo e novas tentativas, guarda a resposta e consulta periodicamente um pedido assíncrono até estar concluído. As credenciais provêm da ligação que associar. |
| Script | Completo | Passo Python com reescrita do acesso a frames | Incorpora o corpo do script num passo Python, com o acesso a data frames reescrito; os corpos em Scala são mantidos com uma nota. |
| SQL Statement | Completo | Passo SQL por separador de saída, com o texto traduzido para o dialeto do inquilino | Incorpora cada separador como um passo SQL com as entradas associadas como tabelas temporárias; traduzido para o dialeto do inquilino. |
| StoredProcedure | Completo | [Agent Remote Execution of SQL](/pt-pt/reference/workflow-steps/agent/agent-remote-execution-of-sql/) | Chama o procedimento no respetivo armazém através da ligação que escolher: uma vez por linha de entrada, com cada argumento associado a partir da sua coluna, ou uma vez quando não recebe argumentos. As colunas de entrada passam sem alterações. |
| Table Operations | Completo | [Table In-Place Delete](/pt-pt/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/pt-pt/reference/workflow-steps/tables/table-update/), [Table Drop](/pt-pt/reference/workflow-steps/tables/table-drop/) | Atualizar, eliminar e remover correspondem a passos de tabela; vacuum e otimizar tornam-se otimização de tabela ou uma operação nula, com um aviso. |
| ToDo | Completo | [Gerar erro de fluxo de trabalho](/pt-pt/reference/workflow-steps/workflow-control/raise-workflow-error/) ou [Notify via Log](/pt-pt/reference/workflow-steps/notifications/notify-via-log/) | Assinala lógica ainda por escrever: uma mensagem de registo quando nada a lê, ou um passo que pára a execução com a mensagem da gem quando um passo posterior depende dela. |

### Espacial

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Buffer | Completo | [Spatial Buffer](/pt-pt/reference/workflow-steps/spatial/spatial-buffer/) | Aumenta cada geometria na distância configurada, em milhas ou quilómetros. |
| CreatePoint | Completo | [Table Extract](/pt-pt/reference/workflow-steps/spatial/spatial-sql-recipes/) com `geom_point` | Constrói geometria de pontos a partir de colunas de longitude e latitude. |
| Distance | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Calcula a distância, a direção cardinal e o rumo entre dois pontos WKT. |
| FindNearest | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com uma junção cruzada | Encontra os N pontos de destino mais próximos de cada ponto de origem dentro de uma distância máxima. |
| HeatMap | Completo | [Heat Map (macro)](/pt-pt/reference/workflow-steps/macros/macro-heat-map/) | Agrupa pontos em hexágonos H3 na resolução da gem, distribui o calor pela distância da grelha com a respetiva atenuação e indica a densidade e o contorno de cada hexágono. |
| PolyBuild | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) e um passo Python | Constrói WKT de polígonos ou polilinhas a partir de pontos ordenados por grupo. |
| Simplify | Completo | [Spatial Generalize](/pt-pt/reference/workflow-steps/spatial/spatial-generalize/) | Simplifica geometrias WKT por uma tolerância em milhas/quilómetros. |
| SpatialMatch | Completo | [Correspondência espacial](/pt-pt/reference/workflow-steps/spatial/spatial-match/) | Faz corresponder geometrias de origem e de destino por interseção/contenção/pertença/toque/envelope. |

### Relatório

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| PowerBIWrite | Completo | [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) | Cria o conjunto de dados do Power BI e envia as linhas através da API REST do Power BI. |
| TableauWrite | Completo | [Publish to Tableau](/pt-pt/reference/workflow-steps/export/export-to-tableau/) | Escreve uma extração Hyper e publica-a na ligação Tableau associada. |
| Visualize | Completo | [Copiar tabela](/pt-pt/reference/workflow-steps/tables/table-copy/) | Transmite as linhas sem alterações; crie o gráfico como um painel de controlo do PlaidCloud sobre a mesma tabela. |

### Subgrafo/Controlo

| Gem | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Condition | Completo | [Junção cruzada](/pt-pt/reference/workflow-steps/tables/table-cross-join/) e [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) | Avalia as condições sobre toda a entrada e envia cada linha para a primeira saída cuja condição se verifica, ou para a última saída caso contrário. |
| Macro | Completo | Passo SQL com o corpo da macro expandido | Incorpora o corpo da macro como um passo SQL traduzido para o dialeto do inquilino, com as entradas associadas como tabelas temporárias. |
| Pipeline (trigger) | Completo | [Workflow Loop](/pt-pt/reference/workflow-steps/workflow-control/workflow-loop/) | Executa o pipeline indicado uma vez por linha de entrada com os seus parâmetros e condição de acionamento, continua após uma execução falhada e devolve uma linha por execução. |
| Subgraph (Basic) | Completo | Contentor da área de desenho / fluxo de trabalho aninhado a partir de processos em linha | Converte o grafo interno em linha num fluxo de trabalho aninhado (ou em passos incorporados) com parâmetros de tabela de entrada/saída. |

## Conectores

Os formatos de conjuntos de dados e os conectores são definições de origem e de destino de uma gem, não gems. Cada formato é convertido no passo de importação ou exportação indicado, e a conversão nunca contacta o sistema de origem ou de destino.

| Formato | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Avro | Completo | Importar: [Avro](/pt-pt/reference/workflow-steps/import/import-avro/); Exportar: [Avro](/pt-pt/reference/workflow-steps/export/export-to-avro/) | Lê e escreve ficheiros Avro. |
| BigQuery | Completo | Ligação a base de dados externa com importação de tabela | Lê e escreve através de uma ligação. |
| Binary files | Completo | [Listagem de diretório](/pt-pt/reference/workflow-steps/document/directory-listing/) com o conteúdo dos ficheiros; [Executor Alteryx](/pt-pt/reference/workflow-steps/general/alteryx-executor/) para escrever | Lê cada ficheiro da pasta com o respetivo caminho, hora de modificação, tamanho e conteúdo; escreve o conteúdo de cada linha no ficheiro indicado pelo respetivo caminho. |
| Catalog table | Completo | Associação a tabela existente do PlaidCloud | Associa-se a uma tabela por nome; a leitura e todos os modos de escrita são convertidos. |
| Cosmos DB | Completo | Importação e exportação: [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) | Lê e escreve os documentos do contentor através da sua ligação ao Cosmos DB. |
| CSV | Completo | [Importar: CSV](/pt-pt/reference/workflow-steps/import/import-csv/); Exportar: CSV | Lê e escreve ficheiros delimitados com opções de cabeçalho, separador, aspas, escape e codificação. |
| Data Generator | Completo | [Table Faker](/pt-pt/reference/workflow-steps/tables/table-faker/) | Gera as colunas do conjunto de dados com os mesmos tipos de dados fictícios. |
| DataHub table | Completo | [Importar SQL](/pt-pt/reference/workflow-steps/import/import-sql/) | Lê a tabela indicada pelo conjunto de dados através da sua ligação; uma escrita é guardada numa tabela do PlaidCloud. |
| Delta | Completo | Associação a tabela existente do PlaidCloud | Lê e escreve a tabela em todos os modos de escrita; a leitura de uma versão anterior é feita através da ligação Databricks que associar. |
| Excel (XLSX) | Completo | Importar: Excel; Exportar: Excel | Lê e escreve folhas e intervalos de livros. |
| Fixed format | Completo | Importar: [Largura fixa](/pt-pt/reference/workflow-steps/import/import-fixed-width/); Exportar: [CSV](/pt-pt/reference/workflow-steps/export/export-to-csv/) | Lê ficheiros de largura fixa dispostos segundo as larguras de coluna do conjunto de dados; escreve um ficheiro delimitado. |
| Hive | Completo | Importar: [SQL](/pt-pt/reference/workflow-steps/import/import-sql/); Exportar: [Tabelas externas](/pt-pt/reference/workflow-steps/export/export-external-tables/) | Lê e escreve a tabela através da sua ligação ao Hive. |
| Iceberg | Completo | Associação a tabela existente do PlaidCloud | Lê e escreve a tabela. |
| JDBC | Completo | Ligação a base de dados externa com importação de tabela | Lê uma tabela ou consulta e escreve em modo de substituição ou acréscimo através da sua ligação; uma instrução posterior à escrita é executada depois da escrita. |
| JSON | Completo | [Analisar JSON](/pt-pt/reference/workflow-steps/tables/table-json-parse/) | Carrega registos e aplana os campos aninhados. |
| Kafka | Completo | Importar: [Kafka](/pt-pt/reference/workflow-steps/import/import-kafka/); Exportar: [Kafka](/pt-pt/reference/workflow-steps/export/export-kafka/) | Lê um tópico como um único lote de mensagens e escreve as linhas como mensagens. |
| MongoDB | Completo | Importar: [MongoDB](/pt-pt/reference/workflow-steps/import/import-mongodb/); Exportar: [MongoDB](/pt-pt/reference/workflow-steps/export/export-mongodb/) | Lê e escreve a coleção através da sua ligação ao MongoDB. |
| ORC | Completo | Importar: [ORC](/pt-pt/reference/workflow-steps/import/import-orc/); Exportar: ORC | Lê e escreve ficheiros ORC. |
| Parquet | Completo | Importar: Parquet; Exportar: Parquet | Lê e escreve ficheiros Parquet. |
| Pinecone | Completo | Importação e exportação: [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) | Lê os registos de um índice e faz upsert das linhas como vetores através da API REST do Pinecone. |
| Redshift | Completo | Ligação a base de dados externa com importação de tabela | Lê e escreve através de uma ligação. |
| Salesforce | Completo | Importar: [Salesforce: Consultar objeto](/pt-pt/reference/workflow-steps/salesforce/query-salesforce-object/); Exportar: [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) | Lê um objeto ou uma consulta SOQL e escreve registos através da sua ligação ao Salesforce. |
| Seed (inline) | Completo | [Importar: CSV](/pt-pt/reference/workflow-steps/import/import-csv/) | Carrega as linhas em linha como uma tabela. |
| Slack | Completo | Importar: [Singer](/pt-pt/reference/workflow-steps/import/import-singer/); Exportar: [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) | Lê as mensagens de um canal e publica cada linha como uma mensagem através da sua ligação ao Slack. |
| Smartsheet | Completo | Importação e exportação: [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) | Lê e escreve as linhas da folha através da sua ligação ao Smartsheet. |
| Snowflake | Completo | Ligação a base de dados externa com importação de tabela | Lê e escreve através de uma ligação. |
| SQL file types (CSV, Excel, JSON, Parquet, Text, XML, fixed-width) | Completo | Passos de importação e exportação de ficheiros numa conta de documentos | Lê e escreve o tipo de ficheiro; as opções sem equivalente no PlaidCloud são assinaladas. |
| Text | Completo | [Importar: CSV](/pt-pt/reference/workflow-steps/import/import-csv/) como uma única coluna | Lê cada linha como uma coluna. |
| Web page | Completo | [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) | Lê a página do URL do conjunto de dados para uma tabela. |
| XML | Completo | [Análise de XML](/pt-pt/reference/workflow-steps/tables/table-xml-parse/) | Carrega registos pela etiqueta de linha. |

## Expressões e estrutura do projeto

| Área | Estado | Equivalente no PlaidCloud | Conversão |
| --- | --- | --- | --- |
| Expressões | Completo | Expressões SQL de Spark e de armazém traduzidas função a função | As funções e os operadores são convertidos em expressões do PlaidCloud; uma função sem equivalente é assinalada pelo nome. |
| Estrutura do projeto e do grafo | Completo | Carregador de projetos | Todos os formatos de exportação do Prophecy são carregados e normalizados num único modelo. |

## Casos limite conhecidos

| Caso | O que acontece |
| --- | --- |
| Código ou dados que a exportação não inclui | Uma Gem Builder ou outra gem personalizada cujo código não está na exportação, e uma chamada a uma macro de um pacote dbt que a exportação deixa de fora, tornam-se um passo que indica o que falta; exporte o projeto com o código do pipeline e os pacotes dbt, ou reconstrua a lógica num passo Python ou SQL. As gems Ab Initio Error Detection e MTime transmitem a sua entrada sem alterações, porque a regra que aplicam não está na exportação. As verificações Soda lidas de um ficheiro fora do projeto, e as verificações Soda que comparam com análises anteriores ou com outro conjunto de dados, ou que testam um formato que o Soda indica, não têm linha na tabela de resultados; calcule-as num passo posterior. |
| Resultados que só se conhecem quando o pipeline é executado | Uma gem REST API que aplana a sua resposta coloca a resposta inteira numa única coluna quando nada declara os nomes dos campos, o que só uma execução revela; extraia os campos de que precisa num passo posterior. Uma macro dbt que consulta o armazém à medida que o dbt compila torna-se um passo que a indica; substitua a consulta pelos valores que devolve. Uma gem StoredProcedure do Spark é executada, mas os seus valores OUT não são devolvidos; a saída são as colunas transmitidas. `input_file_name()` devolve uma cadeia vazia sobre uma origem de tabela ou Delta, que não tem ficheiro para nomear, e `hash()` / `xxhash64()` dentro de uma agregação, uma janela ou uma gem com várias entradas são calculados pelo armazém, pelo que podem diferir dos do Spark. |
| Valores escritos num passo quando o projeto é convertido | Um valor de parâmetro que contenha aspas, barra invertida ou chaveta, um valor de pipeline lido por um passo SQL e a base de dados que uma operação de tabela Delta indica através da configuração são escritos no passo como valores fixos, pelo que alterar a variável do fluxo de trabalho não os altera; edite o passo quando a configuração mudar. |
| Código Scala | Um script Scala, uma expressão Scala ou uma função definida pelo utilizador ou função de agregação em Scala torna-se um passo que a indica; reescreva-a em SQL ou Python. |
| Início de sessão Kerberos do Kafka | Um source ou target Kafka que inicia sessão com Kerberos (GSSAPI) é convertido sem o nome do serviço Kerberos nem o mecanismo de início de sessão; defina-os na ligação do PlaidCloud. |
| Streaming | Os sources, targets e pipelines de streaming são executados como fluxos de trabalho em lote sobre os dados presentes quando são executados; agende o fluxo de trabalho para ser executado com a frequência de que necessitar. |
| Componentes de tarefas | Uma tarefa Spark é convertida com o seu único pipeline e agendamento; os seus outros componentes, condições de execução e substituições de configuração não são convertidos. |
| Chamadas pouco comuns | Uma função de agregação definida pelo utilizador chamada a partir de um rollup ou de uma janela, e uma macro dbt que usa Jinja além de if, for, set e dos filtros comuns, tornam-se um passo que indica a gem; chame a função a partir de uma gem Aggregate ou incorpore a macro. |

## Validar um fluxo de trabalho convertido

Compare a saída do fluxo de trabalho convertido com a saída do seu próprio pipeline do Prophecy: esquema, contagem de linhas e valores das linhas. Ignore a ordem das linhas, a menos que o fluxo de trabalho dependa dela.
