---
title: Matriz de conversão do Prophecy
description: Como o PlaidCloud converte pipelines e projetos SQL do Prophecy em etapas nativas de fluxo de trabalho avançado, com o status de suporte de cada gem.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/prophecy-conversion-matrix.md
---

O PlaidCloud converte pipelines Spark e projetos SQL do Prophecy em fluxos de
trabalho avançados nativos. O importador mapeia cada gem do Prophecy para uma etapa do fluxo de trabalho,
variável de projeto ou objeto da tela, de modo que um fluxo de trabalho convertido seja executado nativamente na nuvem
em vez de como uma emulação.

Todo gem, conector e estrutura de projeto é convertido: **Completo** significa que o gem
se torna uma etapa, variável ou objeto de tela nativo do PlaidCloud que realiza o trabalho
do gem. Os poucos comportamentos que um fluxo de trabalho convertido não reproduz por
conta própria estão listados em [Casos limite conhecidos](#casos-limite-conhecidos), cada um com o que
fazer.

Para executar uma conversão, consulte [Migrar projetos do Prophecy](/pt-br/guides/workflows/migrate-prophecy-projects/).

## Gems de pipeline Spark

### Origem/Destino

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Lookup | Completo | [Tabela: Consulta](/pt-br/reference/workflow-steps/tables/table-lookup/) | Cada chamada de lookup se torna uma etapa Tabela: Consulta na etapa que a usa; uma chave sem correspondência retorna NULL, e uma chave duplicada retorna uma de suas linhas. |
| Source | Completo | Etapa de importação escolhida pelo formato do conjunto de dados (consulte [Conectores](#conectores)) | Cada Source se torna uma etapa de importação em uma tabela com o nome do conjunto de dados; um formato que o conversor não reconhece é lido como um arquivo CSV carregado na pasta de documentos do fluxo de trabalho, com um aviso. |
| Streaming Source | Completo | Mesma importação do Source em lote | Origens de streaming são convertidas em uma importação em lote única, com um aviso. |
| Streaming Target | Completo | Carga em lote com anexação | Destinos de streaming são convertidos em uma anexação em lote, com um aviso. |
| Target | Completo | Etapa de exportação / carga de tabela escolhida pelo formato do conjunto de dados e por writeMode | Cada Target se torna uma etapa de carga ou exportação de tabela no modo de gravação do gem: append, overwrite, merge com suas expressões SET, upsert, SCD2, replaceWhere e insertInto. |

### Preparar

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Data Cleansing | Completo | Expressões de coluna em uma etapa [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Converte as opções de preenchimento de nulos, remoção de espaços e maiúsculas/minúsculas em expressões de coluna; as colunas limpas vão para o final. |
| Sequence | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com uma expressão de número de linha | Adiciona uma coluna de sequência a partir do valor inicial e do incremento. |
| Surrogate Key Generator | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com uma expressão de número de linha | Adiciona uma chave sequencial a partir do valor inicial; as chaves continuam entre execuções a partir de uma tabela que guarda a última chave emitida. |

### Transformar

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Aggregate | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com agregação; [Pivot](/pt-br/reference/workflow-steps/tables/table-pivot/) quando o gem faz pivot | Agrupa e agrega, aplica a condição HAVING e faz o pivot em uma coluna por valor de pivô; propagate-all transporta todas as outras colunas de entrada. |
| Bulk Column Expressions | Completo | Expande em uma expressão por coluna em uma etapa [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Uma expressão por coluna listada em uma etapa Table Extract; a conversão avisa que o layout do gem é presumido. |
| Bulk Column Rename | Completo | Renomeação de coluna em uma etapa [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Uma renomeação por coluna listada em uma etapa Table Extract; a conversão avisa que o layout do gem é presumido. |
| Deduplicate | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com distinct ou um filtro por número de linha | Mantém uma linha por chave: distinct, a primeira ou a última pela sua ordem de classificação, qualquer uma, ou apenas as chaves que ocorrem uma vez. |
| Dynamic Replace | Completo | Transformação de substituição dinâmica, configurada manualmente | Converte em regras de substituição na transformação de substituição dinâmica; a conversão avisa que o layout do gem é presumido. |
| Dynamic Select | Completo | Seleção de colunas em uma etapa [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) resolvida por tipo | Resolve as colunas por tipo no momento da conversão em uma seleção explícita. |
| Filter | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com uma expressão de filtro | Converte em uma etapa Table Extract com uma expressão de filtro; condições NULL descartam a linha. |
| Flatten Schema | Completo | [Analisar JSON](/pt-br/reference/workflow-steps/tables/table-json-parse/) e [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Nivela campos aninhados em colunas nomeadas com o delimitador do gem e expande matrizes em uma linha por elemento. |
| Fuzzy Match | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) e [User Defined Transform](/pt-br/reference/workflow-steps/general/user-defined-transform/) | Emparelha os registros, pontua cada campo de correspondência pelo método do gem, calcula a média das pontuações e mantém os pares iguais ou acima do seu limite. |
| Group By Rollup | Completo | União de etapas de agregação [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) por nível de rollup | Expande o rollup em uma agregação por nível de agrupamento, unidas com subtotais NULL. |
| Limit | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com um limite de linhas | Converte em um limite de linhas; referências de configuração se tornam variáveis de projeto. |
| Normalize | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com uma expressão de explosão | Repete cada registro pela expressão de comprimento, calcula as colunas de saída por índice e para no primeiro índice em que a condição de término é verdadeira. |
| Order By | Completo | Classificação em uma etapa [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Converte em uma classificação com as mesmas chaves, direção e posicionamento de nulos. |
| Reformat | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com expressões de coluna | Converte em uma etapa Table Extract com uma expressão por coluna de saída; colunas não listadas são descartadas. |
| Sample Rows | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com um limite de linhas ou amostra aleatória | Mantém uma fração ou quantidade aleatória de linhas; as linhas escolhidas diferem da execução no Spark porque a amostragem é aleatória. |
| Schema Transform | Completo | Cadeia de etapas [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) aplicadas em ordem | Aplica cada operação em ordem: adicionar ou substituir uma coluna, descartar, renomear, adicionar se ausente com seu valor padrão e adicionar uma regra de negócio do projeto. |
| Set Operation | Completo | [Tabela: União total](/pt-br/reference/workflow-steps/tables/table-union-all/); [Tabela: Anti-junção](/pt-br/reference/workflow-steps/tables/table-anti-join/) para except; [Tabela: Junção interna](/pt-br/reference/workflow-steps/tables/table-inner-join/) para intersect | Union all empilha as entradas; except all e intersect all mantêm o número correto de linhas duplicadas. |
| TransposeAgg | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com agregação | Converte o agrupamento, as agregações e o pivot do gem como um Aggregate, com um aviso para revisá-lo. |
| Unpivot | Completo | [Melt](/pt-br/reference/workflow-steps/tables/table-melt/) | Empilha as colunas selecionadas em colunas de nome e de valor. |
| Watermark | Completo | Nenhuma etapa necessária | Descartado: uma execução em lote lê todos os dados presentes, portanto não há corte de dados tardios a aplicar. |
| Window Function | Completo | Expressões de janela em uma etapa [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Adiciona colunas de janela com a partição, a ordem e o quadro do gem, em linhas ou intervalo, com limites ilimitados, na linha atual ou com deslocamento. |

### Junção/Divisão

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Compare Columns | Completo | Junção externa completa mais agregações por coluna | Compara as colunas por meio de uma junção externa completa dos dados despivotados, com contagens de correspondências e divergências. |
| Join | Completo | [Tabela: Junção interna](/pt-br/reference/workflow-steps/tables/table-inner-join/), [Junção de várias tabelas](/pt-br/reference/workflow-steps/tables/table-multi-table-join/), [Tabela: Anti-junção](/pt-br/reference/workflow-steps/tables/table-anti-join/) ou [Tabela: Junção cruzada](/pt-br/reference/workflow-steps/tables/table-cross-join/) | Cria a junção de cada tipo, inner, left, right, full, semi, anti, cross e natural, com qualquer condição de junção, aplica a cláusula where e grava a lista de seleção. |
| Repartition | Completo | Nenhuma etapa necessária | Descartado: o PlaidCloud gerencia o particionamento, portanto a próxima etapa lê diretamente a tabela de origem. |
| Row Distributor | Completo | Um filtro [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) por saída | Converte em um filtro por saída; as linhas podem ir para várias saídas. |

### Análise

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Column Parser | Completo | [Analisar JSON](/pt-br/reference/workflow-steps/tables/table-json-parse/) / [Análise de XML](/pt-br/reference/workflow-steps/tables/table-xml-parse/) | Converte em uma análise de JSON ou XML da coluna nomeada; a conversão avisa que o layout do gem é presumido. |

### Personalizado

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Custom Gem (Gem Builder) | Completo | [User Defined Transform](/pt-br/reference/workflow-steps/general/user-defined-transform/) executando o código gerado do gem | O código PySpark gerado do gem, a partir da exportação do pipeline, é executado em uma etapa Python, com um aviso para revisá-lo. |
| CustomReformatBitbucket | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Converte como o Reformat cujas expressões o gem carrega, com um aviso para revisá-lo. |
| Data Quality Check | Completo | [Tabela: União total](/pt-br/reference/workflow-steps/tables/table-union-all/) de uma linha de resultado por verificação; [Gerar erro no fluxo de trabalho](/pt-br/reference/workflow-steps/workflow-control/raise-workflow-error/) para parar em caso de falhas | Avalia cada verificação sobre a entrada e grava uma linha de resultado por verificação com seu status e mensagem. Os dados passam adiante, e a execução para quando o limite de falhas do gem é atingido. |
| Deequ | Completo | Verificações [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Repassa os dados e cria a tabela de resultados de restrições para as regras isComplete, isUnique, isNonNegative e isContainedIn. |
| Delta Table Operations | Completo | [Table In-Place Delete](/pt-br/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/pt-br/reference/workflow-steps/tables/table-update/), [Table Drop](/pt-br/reference/workflow-steps/tables/table-drop/), [Table Restore to Timestamp](/pt-br/reference/workflow-steps/tables/table-restore-timestamp/) | Delete, update, drop e restore para um carimbo de data/hora são mapeados para etapas de tabela; optimize, vacuum e restore por versão repassam os dados com um aviso. |
| Directory | Completo | [Listagem de diretório](/pt-br/reference/workflow-steps/document/directory-listing/) | Lista os arquivos da pasta de documentos vinculada nas colunas do gem; com a opção de nome de planilha, cada pasta de trabalho gera uma linha por planilha. Uma pasta ausente gera zero linhas. |
| Email | Completo | [Notify Via Email](/pt-br/reference/workflow-steps/notifications/notify-via-email/) | Envia o e-mail, com um anexo de dados opcional, por meio de uma conexão de e-mail vinculada. |
| Email Data | Completo | [Notify Via Email](/pt-br/reference/workflow-steps/notifications/notify-via-email/) | Envia por e-mail as linhas de entrada como uma tabela e repassa a entrada sem alterações. |
| File Operation | Completo | [Copy Document File](/pt-br/reference/workflow-steps/document/copy-document-file/) ou [Copy Document Directory](/pt-br/reference/workflow-steps/document/copy-document-directory/) | Copia, move ou sincroniza arquivos da pasta de documentos vinculada para a pasta de documentos do fluxo de trabalho convertido; uma movimentação remove os arquivos de origem. |
| Log | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Grava a linha de evento do gem (hora, nome do gem, tipo de evento e texto) em sua tabela de saída. |
| REST API Enrich | Completo | [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) | Chama a API uma vez por linha e adiciona as colunas da resposta. |
| Script | Completo | Etapa Python com reescrita do acesso a frames | Incorpora o corpo do script em uma etapa python, com o acesso a data frames reescrito; corpos em Scala são transportados com uma observação. |
| Soda Data Quality Check | Completo | Verificações [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Cria a tabela de resultados das verificações a partir das verificações do Soda. |
| SQL Statement | Completo | Etapa SQL por guia de saída, texto traduzido para o dialeto do tenant | Incorpora cada guia como uma etapa SQL com as entradas vinculadas como tabelas temporárias; traduzido para o dialeto do tenant. |
| Todo | Completo | [Gerar erro no fluxo de trabalho](/pt-br/reference/workflow-steps/workflow-control/raise-workflow-error/) ou [Notify via Log](/pt-br/reference/workflow-steps/notifications/notify-via-log/) | Marca lógica ainda por escrever: uma mensagem de log quando nada a lê, ou uma etapa que interrompe a execução com a mensagem do gem quando uma etapa posterior depende dela. |

### Relatório

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Tableau | Completo | [Publish to Tableau](/pt-br/reference/workflow-steps/export/export-to-tableau/) | Grava uma extração Hyper e a publica na conexão Tableau vinculada. |

### ML/IA

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Bedrock | Completo | [Text NLP AI](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) | Incorpora a coluna de texto por meio da conexão de IA do espaço de trabalho. |
| OpenAI | Completo | [Text NLP AI](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) | Responde a perguntas ou incorpora texto por meio da conexão de IA do espaço de trabalho. |
| Pinecone Lookup | Completo | [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) | Consulta o índice do Pinecone para cada linha e adiciona as colunas pinecone_matches e pinecone_error. |
| SageMaker Endpoint | Completo | [Text NLP AI](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) | Responde a perguntas por meio da conexão de IA do espaço de trabalho. |
| Text Processing | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) para divisão em blocos; [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) para web scraping | A divisão em blocos se torna uma expressão de blocos de caracteres; o web scraping busca a URL de cada linha e reúne o conteúdo da página de volta à linha. |

### Subgrafo/Controle

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Control Flow Input | Completo | Descartado (apenas marcador de limite) | Descartado; apenas marca o limite de entrada do subfluxo de trabalho iterador. |
| Control Flow Output | Completo | Descartado (apenas marcador de limite) | Descartado; apenas marca o limite de saída do subfluxo de trabalho iterador. |
| Subgraph (Basic) | Completo | Contêiner de tela / fluxo de trabalho aninhado a partir de processos em linha | Converte o grafo interno em linha em um fluxo de trabalho aninhado (ou etapas incorporadas) com parâmetros de tabela de entrada/saída. |
| Table Iterator | Completo | [Workflow Loop](/pt-br/reference/workflow-steps/workflow-control/workflow-loop/) | Executa o corpo do loop uma vez por linha de entrada, definindo cada valor de configuração a partir de sua coluna, até maxIteration. |
| While Iterator | Completo | [Workflow Loop](/pt-br/reference/workflow-steps/workflow-control/workflow-loop/) | Executa o corpo do loop uma vez por passagem, passando o número da iteração, até que o corpo não retorne linhas ou o máximo do gem seja atingido. |

## Gems de SQL / Analista

### Origem/Destino

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| External table Source/Target (BigQuery, Databricks, SAP HANA, MongoDB, MSSQL, Oracle, Postgres, Redshift, Salesforce, Snowflake, Synapse) | Completo | Etapa de importação/exportação de dados externos com a conexão de banco de dados correspondente | Lê ou grava uma tabela em um banco de dados externo por meio de uma conexão do PlaidCloud. |
| File storage Source/Target (ADLS, Databricks Volumes, GCS, OneDrive, S3, SFTP, SharePoint, Smartsheet) | Completo | Etapas de importação/exportação de arquivos em uma conta de documentos (ADLS/GCS/S3/SFTP/SharePoint/OneDrive) | Lê ou grava arquivos em armazenamento na nuvem/SFTP com união por curinga, gatilho, exclusão/movimentação e opções de criptografia. |
| Model | Completo | Tabela de saída da etapa de origem | Lê outro modelo como a tabela produzida pela etapa de origem referenciada. |
| Seed | Completo | [Importar: CSV](/pt-br/reference/workflow-steps/import/import-csv/) | O CSV de seed é importado para uma tabela do PlaidCloud. |
| Source | Completo | Etapa de importação escolhida pelo formato do conjunto de dados (consulte [Conectores](#conectores)) | Cada Source se torna uma etapa de importação em uma tabela com o nome do conjunto de dados; um formato que o conversor não reconhece é lido como um arquivo CSV carregado na pasta de documentos do fluxo de trabalho, com um aviso. |
| Target Model / Table (Target) | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/), [Upsert](/pt-br/reference/workflow-steps/tables/table-upsert/), [Copiar tabela](/pt-br/reference/workflow-steps/tables/table-copy/) e [Tabela: União total](/pt-br/reference/workflow-steps/tables/table-union-all/) | Grava o select final do modelo em uma tabela do PlaidCloud como replace, append, upsert, delete-and-insert, SCD2 ou replace por predicado. |
| Upload Files | Completo | [Importar: CSV](/pt-br/reference/workflow-steps/import/import-csv/) | Os arquivos locais carregados se tornam uma tabela por meio de uma etapa de importação. |

### Preparar

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Data Cleansing | Completo | Expressões de coluna em uma etapa [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Converte as opções de preenchimento de nulos, remoção de espaços e maiúsculas/minúsculas em expressões de coluna; as colunas limpas vão para o final. |
| Data Masking | Completo | Expressões de coluna para mascaramento de caracteres ou hash | Mascara ou aplica hash às colunas de texto selecionadas no local ou como novas colunas. |
| Find Duplicates | Completo | Expressão de janela de número de linha mais filtro | Retorna linhas únicas, duplicadas ou selecionadas por contagem/posição, por chave. |
| Generate Rows | Completo | Tabela de sequência unida e filtrada por linha de entrada | Gera linhas por linha de entrada a partir das expressões de inicialização, condição e loop. |
| Imputation | Completo | Agregação mais junção de retorno e expressão de coluna | Substitui nulos ou valores sentinela pela média, mediana, moda ou um valor fixo. |
| Multi-Column Edit | Completo | Expressões por coluna expandidas a partir do modelo | Aplica um modelo de expressão a todas as colunas selecionadas. |
| Multi-Column Rename | Completo | Mapeamento de renomeação de colunas em uma etapa de seleção | Renomeia as colunas selecionadas por prefixo, sufixo ou expressão de nome. |
| Record ID | Completo | Expressão de coluna de número de linha ou uuid | Adiciona uma coluna de ID de registro UUID ou sequencial. |
| Sample | Completo | Limite de linhas ou opção de amostra no extract | Obtém linhas primeiras/últimas/aleatórias/N-ésimas/por porcentagem no total ou por grupo. |
| Tile | Completo | Expressões de janela para número do tile e sequência | Atribui números de tile por soma igual, contagem, faixas de desvio padrão, valores distintos ou cortes manuais. |

### Transformar

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Aggregate | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com agregação; [Pivot](/pt-br/reference/workflow-steps/tables/table-pivot/) quando o gem faz pivot | Agrupa e agrega, aplica a condição HAVING e faz o pivot em uma coluna por valor de pivô; propagate-all transporta todas as outras colunas de entrada. |
| Count Records | Completo | Etapa de agregação com funções de contagem | Retorna contagens totais, não nulas ou distintas em uma linha. |
| Data Encoder/Decoder | Completo | Expressões de coluna para codificação e decodificação base64/hex | Codifica ou decodifica as colunas selecionadas; AES somente no Databricks. |
| Deduplicate | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com distinct ou um filtro por número de linha | Mantém uma linha por chave: distinct, a primeira ou a última pela sua ordem de classificação, qualquer uma, ou apenas as chaves que ocorrem uma vez. |
| Dynamic Select | Completo | Seleção de colunas em uma etapa [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) resolvida por tipo | Resolve as colunas por tipo no momento da conversão em uma seleção explícita. |
| Filter | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com uma expressão de filtro | Converte em uma etapa Table Extract com uma expressão de filtro; condições NULL descartam a linha. |
| Finance | Completo | Expressão de coluna que implementa a função financeira | Anexa o resultado de uma função financeira (FV, PV, NPV, IRR, ...) como uma nova coluna. |
| Flatten Schema | Completo | [Analisar JSON](/pt-br/reference/workflow-steps/tables/table-json-parse/) e [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Nivela campos aninhados em colunas nomeadas com o delimitador do gem e expande matrizes em uma linha por elemento. |
| Fuzzy Match | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) e [User Defined Transform](/pt-br/reference/workflow-steps/general/user-defined-transform/) | Emparelha os registros, pontua cada campo de correspondência pelo método do gem, calcula a média das pontuações e mantém os pares iguais ou acima do seu limite. |
| Limit | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com um limite de linhas | Converte em um limite de linhas; referências de configuração se tornam variáveis de projeto. |
| Order By | Completo | Classificação em uma etapa [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Converte em uma classificação com as mesmas chaves, direção e posicionamento de nulos. |
| Pivot | Completo | [Pivot](/pt-br/reference/workflow-steps/tables/table-pivot/) | Transforma os valores de pivô selecionados em colunas de agregações; uma lista de valores do modo Simples obtida no momento do design é convertida como os valores listados. |
| Reformat | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com expressões de coluna | Converte em uma etapa Table Extract com uma expressão por coluna de saída; colunas não listadas são descartadas. |
| Running Total | Completo | Coluna de expressão de janela de soma cumulativa | Anexa somas cumulativas por coluna selecionada. |
| Snowflake Unpivot (third-party) | Completo | [Melt](/pt-br/reference/workflow-steps/tables/table-melt/) | Faz o unpivot de colunas por meio do UNPIVOT do Snowflake. |
| Transpose | Completo | [Melt](/pt-br/reference/workflow-steps/tables/table-melt/) | Empilha colunas de dados em colunas de nome e de valor de texto. |
| TransposeAgg | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com agregação | Converte o agrupamento, as agregações e o pivot do gem como um Aggregate, com um aviso para revisá-lo. |
| Unpivot | Completo | [Melt](/pt-br/reference/workflow-steps/tables/table-melt/) | Empilha colunas de dados em colunas de nome e de valor. |
| Weighted Average | Completo | Etapa de agregação com expressão de média ponderada | Calcula uma média ponderada no total ou por grupo. |
| Window Function | Completo | Expressões de janela em uma etapa [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Adiciona colunas de janela com a partição, a ordem e o quadro do gem, em linhas ou intervalo, com limites ilimitados, na linha atual ou com deslocamento. |

### Junção/Divisão

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Except | Completo | [Tabela: Anti-junção](/pt-br/reference/workflow-steps/tables/table-anti-join/) em todas as colunas mais um [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) distinct | Mantém as linhas da primeira entrada que não aparecem em nenhuma das outras entradas. |
| Intersect | Completo | [Tabela: Junção interna](/pt-br/reference/workflow-steps/tables/table-inner-join/) em todas as colunas mais Distinct | Mantém as linhas presentes em todas as entradas. |
| Join | Completo | [Tabela: Junção interna](/pt-br/reference/workflow-steps/tables/table-inner-join/), [Junção de várias tabelas](/pt-br/reference/workflow-steps/tables/table-multi-table-join/), [Tabela: Anti-junção](/pt-br/reference/workflow-steps/tables/table-anti-join/) ou [Tabela: Junção cruzada](/pt-br/reference/workflow-steps/tables/table-cross-join/) | Cria a junção de cada tipo, inner, left, right, full, semi, anti, cross e natural, com qualquer condição de junção, aplica a cláusula where e grava a lista de seleção. |
| Union | Completo | [Tabela: União total](/pt-br/reference/workflow-steps/tables/table-union-all/) | Empilha as entradas por posição, removendo duplicatas quando o gem não as mantém. |
| Union By Name | Completo | [Tabela: União total](/pt-br/reference/workflow-steps/tables/table-union-all/) | Torna-se uma União total que alinha as colunas por nome e preenche com nulos as ausentes. |

### Análise

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| JSON Parse | Completo | [Analisar JSON](/pt-br/reference/workflow-steps/tables/table-json-parse/) | Analisa uma coluna de texto JSON em campos estruturados. |
| Regex | Completo | Expressões regex em uma etapa Table Extract / Transform | Substitui, analisa, corresponde ou tokeniza uma coluna de texto com uma regex. |
| Text To Columns | Completo | Etapas de divisão de coluna / explosão com delimitador regex | Divide uma coluna delimitada em colunas ou linhas usando um delimitador regex. |
| XML Parse | Completo | [Análise de XML](/pt-br/reference/workflow-steps/tables/table-xml-parse/) | Analisa uma coluna de texto XML em campos estruturados. |

### Personalizado

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Directory | Completo | [Listagem de diretório](/pt-br/reference/workflow-steps/document/directory-listing/) | Lista os arquivos da pasta de documentos vinculada nas colunas do gem; com a opção de nome de planilha, cada pasta de trabalho gera uma linha por planilha. Uma pasta ausente gera zero linhas. |
| DynamicInput | Completo | Etapa SQL para modelos de consulta; loop de fluxo de trabalho para o modo de vários arquivos | O modo de modelo de consulta incorpora o modelo como uma etapa SQL; o modo de vários arquivos é mapeado com premissas. |
| Email | Completo | [Notify Via Email](/pt-br/reference/workflow-steps/notifications/notify-via-email/) | Envia o e-mail, com um anexo de dados opcional, por meio de uma conexão de e-mail vinculada. |
| RestAPI | Completo | [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) | Envia uma solicitação por linha de entrada com sua URL, cabeçalhos, consulta, corpo e novas tentativas, mantém a resposta e consulta periodicamente uma solicitação assíncrona até que ela termine. As credenciais vêm da conexão que você vincula. |
| Script | Completo | Etapa Python com reescrita do acesso a frames | Incorpora o corpo do script em uma etapa python, com o acesso a data frames reescrito; corpos em Scala são transportados com uma observação. |
| SQL Statement | Completo | Etapa SQL por guia de saída, texto traduzido para o dialeto do tenant | Incorpora cada guia como uma etapa SQL com as entradas vinculadas como tabelas temporárias; traduzido para o dialeto do tenant. |
| StoredProcedure | Completo | [Agent Remote Execution of SQL](/pt-br/reference/workflow-steps/agent/agent-remote-execution-of-sql/) | Chama o procedimento em seu data warehouse por meio da conexão que você escolhe: uma vez por linha de entrada, com cada argumento vinculado à sua coluna, ou uma vez quando não recebe argumentos. As colunas de entrada passam adiante. |
| Table Operations | Completo | [Table In-Place Delete](/pt-br/reference/workflow-steps/tables/table-in-place-delete/), [Table Update](/pt-br/reference/workflow-steps/tables/table-update/), [Table Drop](/pt-br/reference/workflow-steps/tables/table-drop/) | Update, delete e drop são mapeados para etapas de tabela; vacuum e optimize se tornam a otimização de tabela ou uma operação nula, com um aviso. |
| ToDo | Completo | [Gerar erro no fluxo de trabalho](/pt-br/reference/workflow-steps/workflow-control/raise-workflow-error/) ou [Notify via Log](/pt-br/reference/workflow-steps/notifications/notify-via-log/) | Marca lógica ainda por escrever: uma mensagem de log quando nada a lê, ou uma etapa que interrompe a execução com a mensagem do gem quando uma etapa posterior depende dela. |

### Espacial

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Buffer | Completo | [Spatial Buffer](/pt-br/reference/workflow-steps/spatial/spatial-buffer/) | Amplia cada geometria pela distância configurada em milhas ou quilômetros. |
| CreatePoint | Completo | [Table Extract](/pt-br/reference/workflow-steps/spatial/spatial-sql-recipes/) com `geom_point` | Cria geometria de ponto a partir de colunas de longitude e latitude. |
| Distance | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Calcula a distância, a direção cardeal e o rumo entre dois pontos WKT. |
| FindNearest | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com uma junção cruzada | Encontra os N pontos de destino mais próximos de cada ponto de origem dentro de uma distância máxima. |
| HeatMap | Completo | [Heat Map (macro)](/pt-br/reference/workflow-steps/macros/macro-heat-map/) | Agrupa pontos em hexágonos H3 na resolução do gem, distribui o calor pela distância da grade com seu decaimento e fornece a densidade e o contorno de cada hexágono. |
| PolyBuild | Completo | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) e uma etapa Python | Cria WKT de polígono ou polilinha a partir de pontos ordenados por grupo. |
| Simplify | Completo | [Spatial Generalize](/pt-br/reference/workflow-steps/spatial/spatial-generalize/) | Simplifica geometrias WKT por uma tolerância em milhas/km. |
| SpatialMatch | Completo | [Correspondência espacial](/pt-br/reference/workflow-steps/spatial/spatial-match/) | Faz a correspondência de geometrias de origem e destino por intersects/contains/within/touches/envelope. |

### Relatório

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| PowerBIWrite | Completo | [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) | Cria o conjunto de dados do Power BI e envia as linhas pela API REST do Power BI. |
| TableauWrite | Completo | [Publish to Tableau](/pt-br/reference/workflow-steps/export/export-to-tableau/) | Grava uma extração Hyper e a publica na conexão Tableau vinculada. |
| Visualize | Completo | [Copiar tabela](/pt-br/reference/workflow-steps/tables/table-copy/) | Repassa as linhas sem alterações; crie o gráfico como um painel do PlaidCloud sobre a mesma tabela. |

### Subgrafo/Controle

| Gem | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Condition | Completo | [Tabela: Junção cruzada](/pt-br/reference/workflow-steps/tables/table-cross-join/) e [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) | Avalia as condições sobre toda a entrada e envia cada linha à primeira saída cuja condição é verdadeira, ou à última saída caso contrário. |
| Macro | Completo | Etapa SQL com o corpo da macro expandido | Incorpora o corpo da macro como uma etapa SQL traduzida para o dialeto do tenant, com as entradas vinculadas como tabelas temporárias. |
| Pipeline (trigger) | Completo | [Workflow Loop](/pt-br/reference/workflow-steps/workflow-control/workflow-loop/) | Executa o pipeline nomeado uma vez por linha de entrada com seus parâmetros e condição de gatilho, continua após uma execução com falha e retorna uma linha por execução. |
| Subgraph (Basic) | Completo | Contêiner de tela / fluxo de trabalho aninhado a partir de processos em linha | Converte o grafo interno em linha em um fluxo de trabalho aninhado (ou etapas incorporadas) com parâmetros de tabela de entrada/saída. |

## Conectores

Os formatos de conjuntos de dados e os conectores são configurações de origem e destino de um gem, não gems. Cada formato é convertido na etapa de importação ou exportação indicada, e a conversão nunca entra em contato com o sistema de origem ou de destino.

| Formato | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Avro | Completo | Importar: [Avro](/pt-br/reference/workflow-steps/import/import-avro/); Exportar: [Avro](/pt-br/reference/workflow-steps/export/export-to-avro/) | Lê e grava arquivos Avro. |
| BigQuery | Completo | Conexão de banco de dados externo com importação de tabela | Lê e grava por meio de uma conexão. |
| Binary files | Completo | [Listagem de diretório](/pt-br/reference/workflow-steps/document/directory-listing/) com o conteúdo dos arquivos; [Executor Alteryx](/pt-br/reference/workflow-steps/general/alteryx-executor/) para gravar | Lê cada arquivo da pasta com seu caminho, hora de modificação, tamanho e conteúdo; grava o conteúdo de cada linha no arquivo que seu caminho nomeia. |
| Catalog table | Completo | Vinculação a uma tabela existente do PlaidCloud | Vincula-se a uma tabela por nome; a leitura e todos os modos de gravação são convertidos. |
| Cosmos DB | Completo | Importação e exportação: [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) | Lê e grava os documentos do contêiner por meio da sua conexão do Cosmos DB. |
| CSV | Completo | [Importar: CSV](/pt-br/reference/workflow-steps/import/import-csv/); Exportar: CSV | Lê e grava arquivos delimitados com opções de cabeçalho, separador, aspas, escape e codificação. |
| Data Generator | Completo | [Table Faker](/pt-br/reference/workflow-steps/tables/table-faker/) | Gera as colunas do conjunto de dados com os mesmos tipos de dados fictícios. |
| DataHub table | Completo | [Importar SQL](/pt-br/reference/workflow-steps/import/import-sql/) | Lê a tabela que o conjunto de dados nomeia por meio da sua conexão; uma gravação vai para uma tabela do PlaidCloud. |
| Delta | Completo | Vinculação a uma tabela existente do PlaidCloud | Lê e grava a tabela em todos os modos de gravação; a leitura de uma versão anterior é feita por meio da conexão Databricks que você vincula. |
| Excel (XLSX) | Completo | Importar: Excel; Exportar: Excel | Lê e grava planilhas e intervalos de pastas de trabalho. |
| Fixed format | Completo | Importar: [Largura fixa](/pt-br/reference/workflow-steps/import/import-fixed-width/); Exportar: [CSV](/pt-br/reference/workflow-steps/export/export-to-csv/) | Lê arquivos de largura fixa organizados a partir das larguras de coluna do conjunto de dados; grava um arquivo delimitado. |
| Hive | Completo | Importar: [Importar SQL](/pt-br/reference/workflow-steps/import/import-sql/); Exportar: [Tabelas externas](/pt-br/reference/workflow-steps/export/export-external-tables/) | Lê e grava a tabela por meio da sua conexão Hive. |
| Iceberg | Completo | Vinculação a uma tabela existente do PlaidCloud | Lê e grava a tabela. |
| JDBC | Completo | Conexão de banco de dados externo com importação de tabela | Lê uma tabela ou consulta e grava nos modos replace ou append por meio da sua conexão; uma instrução pós-gravação é executada após a gravação. |
| JSON | Completo | [Analisar JSON](/pt-br/reference/workflow-steps/tables/table-json-parse/) | Carrega registros e nivela campos aninhados. |
| Kafka | Completo | Importar: [Importar Kafka](/pt-br/reference/workflow-steps/import/import-kafka/); Exportar: [Exportar Kafka](/pt-br/reference/workflow-steps/export/export-kafka/) | Lê um tópico como um lote de mensagens e grava linhas como mensagens. |
| MongoDB | Completo | Importação: [MongoDB](/pt-br/reference/workflow-steps/import/import-mongodb/); Exportação: [MongoDB](/pt-br/reference/workflow-steps/export/export-mongodb/) | Lê e grava a coleção por meio da sua conexão MongoDB. |
| ORC | Completo | Importar: [ORC](/pt-br/reference/workflow-steps/import/import-orc/); Exportar: ORC | Lê e grava arquivos ORC. |
| Parquet | Completo | Importar: Parquet; Exportar: Parquet | Lê e grava arquivos Parquet. |
| Pinecone | Completo | Importação e exportação: [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) | Lê os registros de um índice e faz upsert de linhas como vetores pela API REST do Pinecone. |
| Redshift | Completo | Conexão de banco de dados externo com importação de tabela | Lê e grava por meio de uma conexão. |
| Salesforce | Completo | Importar: [Salesforce: Consultar objeto](/pt-br/reference/workflow-steps/salesforce/query-salesforce-object/); Exportar: [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) | Lê um objeto ou uma consulta SOQL e grava registros por meio da sua conexão Salesforce. |
| Seed (inline) | Completo | [Importar: CSV](/pt-br/reference/workflow-steps/import/import-csv/) | Carrega as linhas em linha como uma tabela. |
| Slack | Completo | Importar: [Singer](/pt-br/reference/workflow-steps/import/import-singer/); Exportar: [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) | Lê mensagens de canais e publica cada linha como uma mensagem por meio da sua conexão Slack. |
| Smartsheet | Completo | Importação e exportação: [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) | Lê e grava as linhas da planilha por meio da sua conexão Smartsheet. |
| Snowflake | Completo | Conexão de banco de dados externo com importação de tabela | Lê e grava por meio de uma conexão. |
| SQL file types (CSV, Excel, JSON, Parquet, Text, XML, fixed-width) | Completo | Etapas de importação e exportação de arquivos em uma conta de documentos | Lê e grava o tipo de arquivo; opções sem equivalente no PlaidCloud são sinalizadas. |
| Text | Completo | [Importar: CSV](/pt-br/reference/workflow-steps/import/import-csv/) como uma única coluna | Lê cada linha como uma coluna. |
| Web page | Completo | [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) | Lê a página na URL do conjunto de dados em uma tabela. |
| XML | Completo | [Análise de XML](/pt-br/reference/workflow-steps/tables/table-xml-parse/) | Carrega registros pela tag de linha. |

## Expressões e estrutura do projeto

| Área | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Expressions | Completo | Expressões SQL de Spark e do data warehouse traduzidas função por função | Funções e operadores são convertidos em expressões do PlaidCloud; uma função sem equivalente é sinalizada pelo nome. |
| Project and graph structure | Completo | Carregador de projeto | Todo formato de exportação do Prophecy é carregado e normalizado em um único modelo. |

## Casos limite conhecidos

| Caso | O que acontece |
| --- | --- |
| Code or data the export does not include | Um Gem Builder ou outro gem personalizado cujo código não está na exportação, e uma chamada a uma macro de um pacote dbt que a exportação deixa de fora, se tornam uma etapa que nomeia o que está faltando; exporte o projeto com o código do pipeline e os pacotes dbt, ou recrie a lógica em uma etapa Python ou SQL. Os gems Ab Initio Error Detection e MTime repassam a entrada, porque a regra que aplicam não está na exportação. As verificações do Soda lidas de um arquivo fora do projeto, e as verificações do Soda que comparam com varreduras anteriores ou com outro conjunto de dados ou testam um formato que o Soda nomeia, não têm linha na tabela de resultados; calcule-as em uma etapa posterior. |
| Results only known when the pipeline runs | Um gem REST API que nivela sua resposta coloca a resposta inteira em uma coluna quando nada declara os nomes dos campos, o que só uma execução revela; extraia os campos de que precisa em uma etapa posterior. Uma macro dbt que consulta o data warehouse enquanto o dbt compila se torna uma etapa que a nomeia; substitua a consulta pelos valores que ela retorna. Um gem StoredProcedure do Spark é executado, mas seus valores OUT não são retornados; a saída são as colunas repassadas. `input_file_name()` retorna uma string vazia sobre uma origem de tabela ou Delta, que não tem arquivo a nomear, e `hash()` / `xxhash64()` dentro de uma agregação, de uma janela ou de um gem com várias entradas são calculados pelo data warehouse, portanto podem diferir dos do Spark. |
| Values written into a step when the project converts | Um valor de parâmetro que contém aspas, barra invertida ou chave, um valor de pipeline que uma etapa SQL lê e o banco de dados que uma operação de tabela Delta nomeia por meio da configuração são gravados na etapa como valores fixos, portanto alterar a variável do fluxo de trabalho não os altera; edite a etapa quando a configuração mudar. |
| Scala code | Um script Scala, uma expressão Scala ou uma função definida pelo usuário ou de agregação em Scala se torna uma etapa que a nomeia; reescreva-a em SQL ou Python. |
| Kafka Kerberos sign-in | Uma origem ou um destino Kafka que faz login com Kerberos (GSSAPI) é convertido sem o nome do serviço Kerberos e o mecanismo de login; defina-os na conexão do PlaidCloud. |
| Streaming | Origens, destinos e pipelines de streaming são executados como fluxos de trabalho em lote sobre os dados presentes quando são executados; agende o fluxo de trabalho para ser executado com a frequência de que você precisar. |
| Job components | Um job do Spark é convertido em seu único pipeline e agendamento; seus outros componentes, condições de execução e substituições de configuração não são convertidos. |
| Uncommon calls | Uma função de agregação definida pelo usuário chamada a partir de um rollup ou de uma janela, e uma macro dbt que usa Jinja além de if, for, set e dos filtros comuns, se tornam uma etapa que nomeia o gem; chame a função a partir de um gem Aggregate ou incorpore a macro. |

## Validação de um fluxo de trabalho convertido

Compare a saída do fluxo de trabalho convertido com a saída do seu próprio pipeline do Prophecy: esquema, contagem de linhas e valores das linhas. Ignore a ordem das linhas, a menos que o fluxo de trabalho dependa dela.
