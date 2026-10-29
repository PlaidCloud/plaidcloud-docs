---
title: Matriz de conversão do Savant
description: Como o PlaidCloud converte análises do Savant Labs em fluxos de trabalho avançados nativos, com o nível de mapeamento de cada agente e os poucos casos extremos nomeados.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/savant-conversion-matrix.md
---

O PlaidCloud converte análises do Savant Labs em fluxos de trabalho avançados nativos. O
importador mapeia cada agente do Savant para uma etapa de fluxo de trabalho, uma variável de projeto ou um
objeto da tela, de modo que o fluxo de trabalho convertido é executado de forma nativa na nuvem.

Para executar uma conversão, consulte [Migrar análises do Savant](/pt-br/guides/workflows/migrate-savant-analyses/).

Cada agente tem um nível de mapeamento. **Full** significa que toda opção do agente tem um
mapeamento válido para uma etapa do PlaidCloud. As construções recusadas por nome estão listadas
em Recusas nomeadas.

Os conectores de sistemas externos são **conectados, não convertidos** — consulte
[Conexão com sistemas externos](#conexão-com-sistemas-externos).

## Suporte a agentes

Todos os 33 agentes são convertidos em Full.

| Agente | Nível | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Adapter Agent (`adapter`) | Full | Etapa de seleção e projeção de esquema | Renomeia, altera o tipo e ordena campos. |
| API / Infer Agent (serviço legado) (`service`) | Full | Igual ao API Agent ou ao Infer Agent, conforme o serviceType | Um LLMService é convertido como o Infer Agent e um APIService como o API Agent; um serviceType ausente ou com erro de grafia é lido a partir das chaves do nó, com um aviso. |
| API Agent (`apiService`) | Full | Table Extract, [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) e uma junção à esquerda de volta | Uma solicitação GET, POST, PUT, PATCH ou DELETE por linha de entrada; o corpo bruto da resposta é gravado em uma coluna de texto, os erros HTTP permanecem como linhas, todas as linhas de entrada são mantidas, e uma cota por período vira um número fracionário de solicitações por segundo. Uma URL relativa é unida à URL base de api_bindings ou ao host da conexão REST; um host, uma porta ou um caminho vindo de um campo da linha é substituído por linha; a paginação por próxima URL, cabeçalho Link, deslocamento e página é seguida, inclusive com início, tamanho de página ou nome de parâmetro modelado a partir de um campo da linha. |
| Blend Agent (`blend`) | Full | [Junção interna](/pt-br/reference/workflow-steps/tables/table-inner-join/), [Junção externa](/pt-br/reference/workflow-steps/tables/table-outer-join/), [Anti-junção](/pt-br/reference/workflow-steps/tables/table-anti-join/) | Combinações interna, à esquerda, à direita, completa, anti e externa excluindo a interna, condições com OR, contém e faz parte de, com fluxos de correspondentes e não correspondentes; as colunas que um pivô ou uma análise nomeia somente em tempo de execução são repassadas. |
| Dedupe Agent (`deduplicate`) | Full | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com linhas distintas | Mantém o primeiro registro por chave, dentro dos grupos de Agrupar por, e encaminha as duplicatas para um segundo fluxo ou as sinaliza. |
| Destination Agent (`destination`) | Full | [Exportar: CSV](/pt-br/reference/workflow-steps/export/export-to-csv/), [Exportar: Excel](/pt-br/reference/workflow-steps/export/export-to-excel/), Exportar: Parquet, JSON, Avro ou XML, [Export to PDF](/pt-br/reference/workflow-steps/export/export-to-pdf/), [Exportar: Tableau Hyper](/pt-br/reference/workflow-steps/export/export-hyper/) com [Publish to Tableau](/pt-br/reference/workflow-steps/export/export-to-tableau/), [Export: External Database Tables](/pt-br/reference/workflow-steps/export/export-external-tables/), [Export to Google Spreadsheet](/pt-br/reference/workflow-steps/export/export-to-google-spreadsheet/), [Notify via Slack](/pt-br/reference/workflow-steps/notifications/notify-via-slack/) ou e-mail | Grava por meio de destination_bindings em uma conta de documentos (CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF ou um .hyper do Tableau, em qualquer conjunto de caracteres Java, incluindo aliases, CESU-8 e formas com marca de ordem de bytes; um caractere que o conjunto de caracteres não possui é gravado como ?), uma tabela de conexão, uma planilha do Google, uma fonte de dados do Tableau ou um canal do Slack, ou destinatários de e-mail. Um destino sem vinculação grava uma tabela de projeto ou um arquivo de documento (veja Para onde vai abaixo). Um arquivo, subpasta ou guia por valor de campo divide arquivos CSV, Excel, Parquet e PDF e guias do Google Sheets; um modelo inicializa cada pasta de trabalho de uma divisão. As opções do Excel são mapeadas: valores em branco vão para `Sheet1`, nomes de planilha em colisão recebem um sufixo, `formatFromTemplate`, `topLeftCell` e o modo `create`. Append, upsert, update e groupReplace mesclam nas chaves de correspondência (um arquivo ou tabela é relido e regravado; uma divisão relê o arquivo em que cada valor da execução é gravado e mescla dentro dele, deixando os outros arquivos como estão; o Tableau atualiza suas linhas no próprio local). As colunas que somente os dados nomeiam (as de um cabeçalho promovido, os valores de um pivô, as chaves de um JSON ou XML analisado) são gravadas ao lado das conhecidas por todas as exportações e gravações em tabela, ordenadas e divididas por elas, e anexadas ou mescladas em uma tabela, ou em um arquivo relido com todas as suas colunas. |
| Explode Agent (`explode`) | Full | [Junção cruzada](/pt-br/reference/workflow-steps/tables/table-cross-join/) | Faz a junção cruzada de um lado pequeno com o fluxo principal. |
| Filter Agent (`filter`) | Full | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com uma expressão de filtro | Divide os registros por assistente ou expressão em caminhos verdadeiro e falso. |
| Filter Pushdown (`pdfilter`) | Full | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com uma expressão de filtro | Filtro no lado do banco de dados, convertido da mesma forma que o Filter. |
| Format Agent (`format`) | Full | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com renomeações de colunas, ou Promote Header | Oculta, altera o tipo, renomeia e preenche campos correspondidos por nome (contém, começa com, termina com) ou por estarem vazios; um preenchimento grava seu valor padrão em qualquer coluna cujo tipo aceite a conversão do padrão (texto, número, data). A promoção da linha de cabeçalho e a correspondência de vazios são executadas em tempo de execução na etapa Promote Header, e um cabeçalho promovido lê todas as colunas do seu arquivo. |
| Fuse Agent (`fuzzy_match`) | Full | [Fuzzy Match](/pt-br/reference/workflow-steps/tables/table-fuzzy-match/), entre uma Union All e duas junções | Empilha as duas entradas, correlaciona os registros pelos campos-chave com um limite de similaridade de 80 e junta os dois lados de volta com uma Pontuação de confiança. |
| Group (`group`) | Full | Contêiner da tela | Preservado como organização do fluxo de trabalho. |
| Infer Agent (`gen_ai`) | Full | Tarefa de prompt de [AI/NLP](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) | O prompt é executado por linha sobre os campos de entrada, na conexão LLM visível que corresponde ao provedor e ao modelo do Savant; a resposta é gravada em uma coluna AI Answer ao lado de todas as colunas de entrada. rowLimit limita as linhas respondidas por execução e mantém as respostas anteriores: uma linha respondida antes (mesmo prompt, modelo e valores de entrada) mantém sua resposta, e somente as linhas sem resposta contam para o limite. |
| JSON Agent (`json`) | Full | [Analisar JSON](/pt-br/reference/workflow-steps/tables/table-json-parse/) | Nivela um campo JSON em colunas com chaves separadas por ponto, ou expande uma matriz em uma linha por elemento; as chaves são lidas dos dados em tempo de execução. |
| Notes Agent (`notes`) | Full | Anotação da tela | Preservado como contexto do fluxo de trabalho. |
| Pivot Agent (`pivot`) | Full | [Pivot](/pt-br/reference/workflow-steps/tables/table-pivot/) | Transforma linhas em colunas com agregação. |
| Recursion Agent (`hierarchy`) | Full | Hierarchy Closure, [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) e [Junção de várias tabelas](/pt-br/reference/workflow-steps/tables/table-multi-table-join/) | Percorre uma árvore pai/filho em qualquer profundidade, agregando cada nó sobre os ids de seu caminho até a raiz, ele mesmo incluído, e gravando Depth e Path; um laço é interrompido no nó repetido. |
| Sample Agent (`sample`) | Full | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com um limite de linhas | Mantém as primeiras N linhas, opcionalmente por grupo, um percentual aleatório ou N linhas, ou uma linha a cada N. |
| Search and Replace (`search_replace`) | Full | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com expressões de substituição aninhadas, divididas em estágios | Regras de localizar/substituir (contém ou corresponde; substituir ou anexar), com ou sem distinção entre maiúsculas e minúsculas, palavra inteira ou não, aplicadas em ordem sobre os campos de texto escolhidos, ou sobre todos os campos de texto quando nenhum é nomeado. |
| Source Agent (`source`) | Full | Etapas de importação vinculadas por `source_bindings` ([Importar: CSV](/pt-br/reference/workflow-steps/import/import-csv/), [Importar: Excel](/pt-br/reference/workflow-steps/import/import-excel/), [Importar: SQL](/pt-br/reference/workflow-steps/import/import-sql/)) ou uma tabela existente | Lê a tabela ou o documento vinculado; uma origem sem vinculação cria uma importação vazia e um aviso. O texto XML lê seu documento por meio de Importar XML (um sem vinculação lê savant/<workflow>/<name>.xml). Uma origem vinculada a um documento XML também grava as outras colunas da exportação: uma coluna de nome ou caminho de arquivo vinda do documento, e as demais em branco. Uma origem abaixo de um Format que promove uma linha de cabeçalho lê, por posição, todas as colunas do seu arquivo CSV, Excel (incluindo Excel 97 .xls), JSON, Parquet ou Avro. |
| Spatial Match Agent (`spatial_match`) | Full | [Correspondência espacial (executor)](/pt-br/reference/workflow-steps/spatial/spatial-match-executor/), [Junção cruzada](/pt-br/reference/workflow-steps/tables/table-cross-join/) ou [Localizar mais próximo](/pt-br/reference/workflow-steps/spatial/spatial-find-nearest/) | Correspondências com intersecta, dentro de, contém, toca, cruza, sobrepõe, igual, disjunto e de várias regras com and/or, distância geodésica dentro de um limite entre quaisquer geometrias (pontos, linhas, polígonos: a menor distância em uma esfera de 6371 km), os N mais próximos por essa mesma distância com uma distância máxima (uma regra isolada de mais próximo não grava coluna Distance, como o Savant que não grava nenhuma; combinada com outras regras como mais próximo e depois filtro, junções AND e uniões OR, cada regra de mais próximo adiciona uma coluna Distance própria) e Cross, com fluxos de correspondentes e não correspondentes. |
| Spatial Summarize Agent (`spatial_summarize`) | Full | [Combinação espacial](/pt-br/reference/workflow-steps/spatial/spatial-combine/), Spatial Centroid e etapas de ponto para linha | União, interseção, caixa delimitadora, um ou vários centros geométricos e construções de polilinha ou polígono, por grupo com uma ordenação opcional. |
| Split Agent (`split`) | Full | Split Text, ou [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com colunas split_part | Divide um campo de texto por um separador literal de qualquer comprimento em linhas ou colunas, com remoção de espaços e manutenção do original; o número de colunas é lido dos dados em tempo de execução. |
| Dividir saída (`outlet`) | Full | Aresta do fluxo de trabalho | Encaminha uma saída nomeada aos seus consumidores. |
| Stack Agent (`multi_stack`) | Full | [Union All](/pt-br/reference/workflow-steps/tables/table-union-all/) | Empilha qualquer número de entradas por nome ou posição. |
| Summarize Agent (`summarize`) | Full | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com agregação | Agrupa e agrega, incluindo primeiro/último por uma ordenação determinística e agregações de janela por linha (useWindow). |
| Summarize Pushdown (`pdsummarize`) | Full | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com agregação | Agregação no lado do banco de dados, convertida da mesma forma que o Summarize. |
| Text (`text`) | Full | Anotação da tela | Preservado como contexto do fluxo de trabalho. |
| Time Series Agent (`rollup`) | Full | Agregação de [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) sobre uma expressão de intervalo de período, Period Spine, [Anti-junção](/pt-br/reference/workflow-steps/tables/table-anti-join/) e [Union All](/pt-br/reference/workflow-steps/tables/table-union-all/) | Consolida registros em períodos de dia, semana, mês, trimestre, ano ou década entre datas opcionais de início e fim, por grupo, excluindo datas NULL e preenchendo com zero os períodos vazios. |
| Transform Agent (`edit`) | Full | [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) com expressões de coluna | Colunas calculadas, alterações de tipo e cálculos de janela (lag, lead, soma acumulada, número da linha, preenchimento para frente e para trás), avaliados em ordem. Uma edição que carrega apenas seus passos compilados é convertida como esses passos aplicados em ordem, cada um alimentando o seguinte. |
| Unpivot Agent (`unpivot`) | Full | [Melt](/pt-br/reference/workflow-steps/tables/table-melt/) | Converte colunas em linhas como um par nome/valor. |
| Vision Agent (`vision`) | Full | [Image OCR](/pt-br/reference/workflow-steps/text-documents/image-ocr/) e depois a tarefa de prompt de [AI/NLP](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) | Cada documento é enviado ao provedor como imagem ou PDF quando ele aceita esse tipo e tamanho; caso contrário, é enviada a camada de texto do PDF ou o texto de OCR; a resposta do prompt é gravada em uma coluna AI Answer. |
| XML Agent (`xml`) | Full | [Análise de XML](/pt-br/reference/workflow-steps/tables/table-xml-parse/) | Seleciona elementos, extrai valores de filhos e atributos em colunas, ou converte XML em JSON; um caminho simples //a/b é convertido como antes e qualquer outro caminho XPath 1.0 (predicados, testes de atributo, curingas, funções como count(), name() e contains()) é avaliado como XPath, com reconhecimento de namespace ou como escrito. |

Os tipos de nó de ligação, tela e pushdown (Dividir saída, Group, Text, Filter Pushdown, Summarize Pushdown) são tipos de nó do Savant sem um artigo próprio de agente na central de ajuda; cada um é convertido como o agente que ele espelha.

Uma credencial em uma solicitação do API Agent nunca é copiada para uma etapa do fluxo de trabalho. Em https, ela é movida para uma conexão REST; em http, sem permissão para gravar conexões, ou em uma conversão feita por meio do MCP, ela é retida com um aviso. Isso é intencional e não reduz o nível.

Dois limites de destino não reduzem o nível. Alguns conjuntos de caracteres raros (por exemplo `x-ISCII91` ou `JIS_X0212`) não podem ser gravados; o arquivo é gravado em UTF-8 e a conversão emite um aviso. Uma publicação no Tableau que mescla nas chaves precisa de `replace: true` em sua vinculação de destino; sem isso, a conversão emite um aviso e publica uma nova fonte de dados, o que falha em uma execução em que já existe uma.

## Recusas nomeadas

Oito construções são recusadas por nome em vez de convertidas. Nenhuma reduz o nível de um agente.

| Construção | Por que é recusada |
| --- | --- |
| Uma solicitação do API Agent que carrega uma credencial e obtém seu host de um campo de entrada | Cada linha poderia enviar a credencial a um host escolhido pelos dados. A solicitação vira um marcador nomeado. Uma solicitação sem credencial, e uma credencial em um host fixo, são convertidas. |
| Uma edição do Transform sem expressão e sem passos compilados, como uma edição do Copilot que tem apenas seu prompt | Não há nada a converter: um prompt não é uma fórmula. Uma edição com passos compilados é convertida. |
| Uma construção de regex em uma expressão de Transform ou Filter que o PlaidCloud não consegue ler: uma classe dentro de uma classe, uma interseção de classes (`&&`) ou uma propriedade `\p{}` desconhecida | A etapa vira um marcador nomeado que é recusado em tempo de execução. |
| Uma função de agregação ou de janela em uma expressão de Transform ou Filter | O próprio Savant falha com ela em tempo de execução. Como cálculo do Transform ou em um Summarize, ela é convertida. |
| `HASH` em uma expressão de Transform ou Filter com um algoritmo literal diferente de `md5` ou `sha1` | O próprio Savant falha com ela (o algoritmo é `md5` ou `sha1`). Um algoritmo lido de uma coluna é convertido, resultando em NULL para qualquer outro valor. |
| Uma ordenação de destino por uma coluna que sua entrada não possui | O próprio Savant falha com ela em tempo de execução. |
| Um arquivo, subpasta, guia ou planilha de destino por valor de uma coluna que sua entrada não possui | O próprio Savant falha com ela em tempo de execução. |
| Um caminho do XML Agent que não é XPath 1.0 | O Savant também não consegue executá-lo. |

Uma URL de API relativa é convertida quando você vincula uma URL base ou uma conexão REST com `api_bindings`; consulte [Vinculações em tempo de conversão](/pt-br/guides/workflows/migrate-savant-analyses/#vinculações-no-momento-da-conversão).

## Linguagem de expressões

As funções e os operadores de expressão do Savant são convertidos em expressões do PlaidCloud. Nível: **Full**. Toda função e todo formato são convertidos, incluindo `TO_TEXT` com um padrão numérico, um formato conhecido apenas por linha, tokens de data de segundos fracionários, baseados em semana, de trimestre e de fuso, anos de dois dígitos e construções de regex Java. As funções GEO_* em qualquer lugar de uma expressão são executadas em etapas Spatial complementares. As exceções são as [recusas nomeadas](#recusas-nomeadas).

Casos extremos conhecidos: `TO_DATE` ou `TO_DATETIME` com um formato que contém um literal `[`, `]`, aspas, barra invertida ou `^`, sobre texto que resulta em 9999-12-30 ou 9999-12-31, que está além do último timestamp que o data warehouse comporta; a conversão emite um aviso.

## Formatos de exportação

O carregador aceita todos os formatos de exportação do Savant — simples, encapsulado em modelo, registro de servidor, envelope de receita, encapsulado em matriz, com BOM e aliases de tipo legados — e os normaliza em um único modelo. Nível: **Full**.

## Parâmetros de análise

Os parâmetros de análise do Savant são convertidos em variáveis de fluxo de trabalho, e as referências a eles dentro das configurações dos nós são reescritas para a sintaxe de variável do PlaidCloud. Os formatos de parâmetro em lista, dicionário e com alias são todos carregados. Nível: **Full**.

Casos extremos conhecidos: um parâmetro cujo nome contém uma palavra secreta ou cujo valor parece uma credencial vira uma variável com valor em branco, com um aviso. Um parâmetro que um nó usa e que a exportação não declara vira uma variável com valor vazio, com um aviso.

## Conexão com sistemas externos

Os conectores do Savant são destinos de origem e de saída, não etapas, e uma exportação não traz conjuntos de dados nem credenciais. O PlaidCloud alcança esses sistemas por meio de uma conexão, e não de um nó na tela.

| Savant | Para onde vai no PlaidCloud |
| --- | --- |
| Conector de origem | `source_bindings` mapeia o nó ou o conjunto de dados do Savant para uma tabela do PlaidCloud ou um arquivo de documento, lido pela etapa de importação correspondente; uma origem sem vinculação emite um aviso e não processa nada |
| Destino: CSV, Excel e outros formatos de arquivo | Uma etapa de exportação ([Exportar: CSV](/pt-br/reference/workflow-steps/export/export-to-csv/), [Exportar: Excel](/pt-br/reference/workflow-steps/export/export-to-excel/), [Export to PDF](/pt-br/reference/workflow-steps/export/export-to-pdf/)) |
| Destino: Google Sheets, Tableau, Slack | [Export to Google Spreadsheet](/pt-br/reference/workflow-steps/export/export-to-google-spreadsheet/), [Publish to Tableau](/pt-br/reference/workflow-steps/export/export-to-tableau/) ou [Notify via Slack](/pt-br/reference/workflow-steps/notifications/notify-via-slack/), por meio de uma conexão que você vincula com `destination_bindings` |
| Destino: banco de dados, data warehouse ou destino SaaS sem vinculação (Oracle, banco de dados genérico, Looker Studio, NetSuite, SAP, e Google Sheets, Tableau ou Slack sem conexão vinculada) | Uma tabela de projeto com o nome do nó de destino, com um aviso que informa o destino original |
| Destino: sistema de arquivos sem vinculação (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | O arquivo, no tipo de arquivo do destino, em uma pasta de documentos que espelha a pasta de destino, com um aviso. As credenciais e os tokens de compartilhamento são removidos do caminho da pasta |
| Destino: e-mail sem vinculação | Um CSV com um aviso |
| Destino: vinculação que não pode ser usada | Um CSV com um aviso que informa o destino original |

A conversão nunca contata o sistema de origem nem o de destino.
