---
title: Matriz de conversão do Savant
description: Como o PlaidCloud converte análises do Savant Labs em fluxos de trabalho avançados nativos, com o escalão de mapeamento de cada agente e os poucos casos limite identificados.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/savant-conversion-matrix.md
---

O PlaidCloud converte análises do Savant Labs em fluxos de trabalho avançados
nativos. O importador mapeia cada agente do Savant para um passo de fluxo de
trabalho, uma variável de projeto ou um objeto da área de desenho, de modo que
um fluxo de trabalho convertido é executado de forma nativa na cloud.

Para executar uma conversão, consulte [Migrar análises do Savant](/pt-pt/guides/workflows/migrate-savant-analyses/).

Cada agente tem um escalão de mapeamento. **Completo** significa que todas as
opções do agente têm um mapeamento válido para um passo do PlaidCloud. As
construções recusadas por nome estão listadas em Recusas Identificadas.

Os conectores de sistemas externos estão **ligados, não convertidos** — consulte
[Ligar a sistemas externos](#ligar-a-sistemas-externos).

## Suporte de Agentes

Todos os 33 agentes são convertidos com o escalão Completo.

| Agente | Escalão | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Adapter Agent (`adapter`) | Completo | Passo de seleção e projeção de esquema | Muda o nome, o tipo e a ordem dos campos. |
| API / Infer Agent (legacy service) (`service`) | Completo | Igual ao API Agent ou ao Infer Agent, consoante o serviceType | Um LLMService é convertido como Infer Agent e um APIService como API Agent; um serviceType em falta ou mal escrito é lido a partir das chaves do nó, com um aviso. |
| API Agent (`apiService`) | Completo | Table Extract, [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) e uma junção à esquerda de volta | Um pedido GET, POST, PUT, PATCH ou DELETE por linha de entrada; o corpo da resposta em bruto fica numa coluna de texto, os erros HTTP mantêm-se como linhas, todas as linhas de entrada são mantidas e uma quota por período torna-se um número fracionário de pedidos por segundo. Um URL relativo junta-se ao URL base de api_bindings ou ao anfitrião da ligação REST; um anfitrião, porta ou caminho obtido de um campo da linha é substituído por linha; a paginação por URL seguinte, cabeçalho Link, deslocamento e página é seguida, incluindo um início, tamanho de página ou nome de parâmetro definido por modelo a partir de um campo da linha. |
| Blend Agent (`blend`) | Completo | [Junção interna](/pt-pt/reference/workflow-steps/tables/table-inner-join/), [Junção externa](/pt-pt/reference/workflow-steps/tables/table-outer-join/), [Anti-junção](/pt-pt/reference/workflow-steps/tables/table-anti-join/) | Misturas interna, à esquerda, à direita, completa, anti e externa excluindo a interna, condições unidas por OR, contém e é-parte-de, com fluxos correspondentes e sem correspondência; as colunas que uma tabela dinâmica ou uma análise só nomeia em tempo de execução são transportadas. |
| Dedupe Agent (`deduplicate`) | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com linhas distintas | Mantém o primeiro registo por chave, dentro dos grupos de Agrupar por, e encaminha os duplicados para um segundo fluxo ou assinala-os. |
| Destination Agent (`destination`) | Completo | [Exportar: CSV](/pt-pt/reference/workflow-steps/export/export-to-csv/), [Exportar: Excel](/pt-pt/reference/workflow-steps/export/export-to-excel/), Exportar: Parquet, JSON, Avro ou XML, [Export to PDF](/pt-pt/reference/workflow-steps/export/export-to-pdf/), [Exportar: Tableau Hyper](/pt-pt/reference/workflow-steps/export/export-hyper/) com [Publish to Tableau](/pt-pt/reference/workflow-steps/export/export-to-tableau/), [Export: External Database Tables](/pt-pt/reference/workflow-steps/export/export-external-tables/), [Export to Google Spreadsheet](/pt-pt/reference/workflow-steps/export/export-to-google-spreadsheet/), [Notify via Slack](/pt-pt/reference/workflow-steps/notifications/notify-via-slack/) ou correio eletrónico | Escreve através de destination_bindings para uma conta de documentos (CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF ou um .hyper do Tableau, em qualquer conjunto de carateres Java, incluindo alias, CESU-8 e formas com marca de ordem de bytes; um caráter que o conjunto de carateres não tem é escrito como ?), uma tabela de ligação, uma Google Sheet, uma origem de dados do Tableau ou um canal do Slack, ou destinatários de correio eletrónico. Um destino não associado escreve antes uma tabela de projeto ou um ficheiro do Document (consulte Para Onde Vai mais abaixo). Um ficheiro, subpasta ou separador por valor de campo divide os ficheiros CSV, Excel, Parquet e PDF e os separadores das Google Sheets; um modelo inicializa todos os livros de uma divisão. As opções do Excel são mapeadas: os valores em branco vão para `Sheet1`, os nomes de folhas em colisão recebem um sufixo, `formatFromTemplate`, `topLeftCell` e o modo `create`. Append, upsert, update e groupReplace fundem pelas chaves de correspondência (um ficheiro ou uma tabela é relido e reescrito; uma divisão relê o ficheiro para o qual é escrito cada valor da execução e funde dentro dele, deixando os outros ficheiros como estão; o Tableau atualiza as suas linhas no próprio local). As colunas que só os dados nomeiam (as de um cabeçalho promovido, os valores de uma tabela dinâmica, as chaves de um JSON ou XML analisado) são escritas junto das conhecidas por todas as exportações e escritas em tabelas, ordenadas e divididas por elas, e acrescentadas ou fundidas numa tabela, ou num ficheiro relido com todas as colunas que tem. |
| Explode Agent (`explode`) | Completo | [Junção cruzada](/pt-pt/reference/workflow-steps/tables/table-cross-join/) | Faz a junção cruzada de um lado pequeno com o fluxo principal. |
| Filter Agent (`filter`) | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com uma expressão de filtro | Divide os registos por assistente ou expressão em caminhos verdadeiro e falso. |
| Filter Pushdown (`pdfilter`) | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com uma expressão de filtro | Filtro do lado da base de dados, convertido da mesma forma que o Filter. |
| Format Agent (`format`) | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com mudanças de nome de colunas, ou Promote Header | Oculta, altera o tipo, muda o nome e preenche campos identificados pelo nome (contém, começa com, termina com) ou por estarem vazios; um preenchimento escreve o valor predefinido em qualquer coluna para cujo tipo o valor predefinido possa ser convertido (texto, número, data). A promoção da linha de cabeçalho e a correspondência de vazios são executadas em tempo de execução no passo Promote Header, e um cabeçalho promovido lê todas as colunas do seu ficheiro. |
| Fuse Agent (`fuzzy_match`) | Completo | [Fuzzy Match](/pt-pt/reference/workflow-steps/tables/table-fuzzy-match/), entre um Union All e duas junções | Empilha ambas as entradas, faz corresponder os registos pelos campos-chave com um limiar de semelhança de 80 e volta a juntar ambos os lados com uma Confidence Score. |
| Group (`group`) | Completo | Contentor da área de desenho | Preservado como organização do fluxo de trabalho. |
| Infer Agent (`gen_ai`) | Completo | Tarefa de pedido de [AI/NLP](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) | O pedido é executado por linha sobre os campos de entrada, na ligação LLM visível que corresponde ao fornecedor e ao modelo do Savant; a resposta fica numa coluna AI Answer ao lado de todas as colunas de entrada. rowLimit limita as linhas respondidas por execução e mantém as respostas anteriores: uma linha respondida antes (mesmo pedido, modelo e valores de entrada) mantém a sua resposta, e apenas as linhas sem resposta contam para o limite. |
| JSON Agent (`json`) | Completo | [Analisar JSON](/pt-pt/reference/workflow-steps/tables/table-json-parse/) | Aplana um campo JSON em colunas com chaves separadas por pontos, ou expande uma matriz numa linha por elemento; as chaves são lidas dos dados em tempo de execução. |
| Notes Agent (`notes`) | Completo | Anotação da área de desenho | Preservado como contexto do fluxo de trabalho. |
| Pivot Agent (`pivot`) | Completo | [Pivot](/pt-pt/reference/workflow-steps/tables/table-pivot/) | Converte linhas em colunas com agregação. |
| Recursion Agent (`hierarchy`) | Completo | Hierarchy Closure, [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) e [Junção de várias tabelas](/pt-pt/reference/workflow-steps/tables/table-multi-table-join/) | Percorre uma árvore pai/filho a qualquer profundidade, agregando cada nó sobre os ids do seu caminho até à raiz, incluindo o próprio, e escrevendo Depth e Path; um ciclo pára no nó repetido. |
| Sample Agent (`sample`) | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com um limite de linhas | Mantém as primeiras N linhas, opcionalmente por grupo, uma percentagem aleatória ou N linhas, ou uma linha em cada N. |
| Search and Replace (`search_replace`) | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com expressões de substituição aninhadas, divididas por fases | Regras de localizar/substituir (contém ou corresponde; substituir ou acrescentar), com ou sem distinção de maiúsculas e minúsculas, palavra inteira ou não, aplicadas por ordem sobre os campos de texto escolhidos, ou sobre todos os campos de texto quando nenhum é indicado. |
| Source Agent (`source`) | Completo | Passos de importação associados através de `source_bindings` ([Importar: CSV](/pt-pt/reference/workflow-steps/import/import-csv/), [Import: Excel](/pt-pt/reference/workflow-steps/import/import-excel/), [Importar: SQL](/pt-pt/reference/workflow-steps/import/import-sql/)) ou uma tabela existente | Lê a tabela ou o documento associado; uma origem não associada cria uma importação vazia e um aviso. O texto XML lê o seu documento através de Importar XML (um não associado lê savant/<workflow>/<name>.xml). Uma origem associada a um documento XML escreve também as outras colunas da exportação: uma coluna de nome ou caminho de ficheiro a partir do documento, o resto em branco. Uma origem abaixo de um Format que promove uma linha de cabeçalho lê, por posição, todas as colunas do seu ficheiro CSV, Excel (incluindo Excel 97 .xls), JSON, Parquet ou Avro. |
| Spatial Match Agent (`spatial_match`) | Completo | [Correspondência espacial (executor)](/pt-pt/reference/workflow-steps/spatial/spatial-match-executor/), [Junção cruzada](/pt-pt/reference/workflow-steps/tables/table-cross-join/) ou [Localizar o mais próximo](/pt-pt/reference/workflow-steps/spatial/spatial-find-nearest/) | Correspondências por interseção, dentro de, contém, toca, cruza, sobrepõe, igual, disjunto e de várias regras com e/ou, distância geodésica entre quaisquer geometrias (pontos, linhas, polígonos: a menor distância numa esfera de 6371 km), os N mais próximos por essa mesma distância com uma distância máxima (uma regra de mais próximo isolada não escreve coluna Distance, tal como o Savant não escreve; combinada com outras regras como mais-próximo-depois-filtro, as junções AND e as uniões OR, cada regra de mais próximo acrescenta uma coluna Distance própria) e Cross, com fluxos correspondentes e sem correspondência. |
| Spatial Summarize Agent (`spatial_summarize`) | Completo | [Combinação espacial](/pt-pt/reference/workflow-steps/spatial/spatial-combine/), Spatial Centroid e passos de ponto para linha | União, interseção, caixa delimitadora, um ou vários centros geométricos e construções de polilinha ou polígono, por grupo com uma ordenação opcional. |
| Split Agent (`split`) | Completo | Split Text, ou [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com colunas split_part | Divide um campo de texto por um separador literal de qualquer comprimento em linhas ou colunas, com remoção de espaços e manutenção do original; o número de colunas é lido dos dados em tempo de execução. |
| Split Output (`outlet`) | Completo | Aresta do fluxo de trabalho | Encaminha uma saída com nome para os seus consumidores. |
| Stack Agent (`multi_stack`) | Completo | [Union All](/pt-pt/reference/workflow-steps/tables/table-union-all/) | Empilha qualquer número de entradas por nome ou posição. |
| Summarize Agent (`summarize`) | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com agregação | Agrupa e agrega, incluindo primeiro/último por uma ordenação determinística e agregados de janela por linha (useWindow). |
| Summarize Pushdown (`pdsummarize`) | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com agregação | Agregação do lado da base de dados, convertida da mesma forma que o Summarize. |
| Text (`text`) | Completo | Anotação da área de desenho | Preservado como contexto do fluxo de trabalho. |
| Time Series Agent (`rollup`) | Completo | Agregação de [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) sobre uma expressão de intervalo de período, Period Spine, [Anti-junção](/pt-pt/reference/workflow-steps/tables/table-anti-join/) e [Union All](/pt-pt/reference/workflow-steps/tables/table-union-all/) | Agrega registos por períodos de dia, semana, mês, trimestre, ano ou década entre datas de início e fim opcionais, por grupo, excluindo datas NULL e preenchendo com zero os períodos vazios. |
| Transform Agent (`edit`) | Completo | [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) com expressões de coluna | Colunas calculadas, alterações de tipo e cálculos de janela (lag, lead, soma cumulativa, número de linha, preenchimento para a frente e para trás), avaliados por ordem. Uma edição que apenas transporta os seus passos compilados é convertida como esses passos aplicados por ordem, alimentando cada um o seguinte. |
| Unpivot Agent (`unpivot`) | Completo | [Melt](/pt-pt/reference/workflow-steps/tables/table-melt/) | Converte colunas em linhas como um par nome/valor. |
| Vision Agent (`vision`) | Completo | [Image OCR](/pt-pt/reference/workflow-steps/text-documents/image-ocr/), seguido da tarefa de pedido de [AI/NLP](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) | Cada documento segue para o fornecedor como imagem ou PDF quando este aceita esse tipo e tamanho; caso contrário, é enviada a sua camada de texto PDF ou o texto OCR; a resposta ao pedido fica numa coluna AI Answer. |
| XML Agent (`xml`) | Completo | [Análise de XML](/pt-pt/reference/workflow-steps/tables/table-xml-parse/) | Seleciona elementos, extrai valores filhos e atributos para colunas, ou converte XML em JSON; um caminho simples //a/b é convertido como antes e qualquer outro caminho XPath 1.0 (predicados, testes de atributos, carateres universais, funções como count(), name() e contains()) é avaliado como XPath, com reconhecimento de espaços de nomes ou tal como escrito. |

As variantes de ligação, de área de desenho e de pushdown (Split Output, Group, Text, Filter Pushdown, Summarize Pushdown) são tipos de nó do Savant sem artigo próprio de agente no centro de ajuda; cada uma é convertida como o agente que espelha.

Uma credencial num pedido de API Agent nunca é copiada para um passo de fluxo de trabalho. Através de https, passa para uma ligação REST; através de http, sem permissão para escrever ligações, ou numa conversão feita através do MCP, é retida com um aviso. Isto é intencional e não reduz o escalão.

Dois limites de destino não reduzem o escalão. Alguns conjuntos de carateres raros (por exemplo `x-ISCII91` ou `JIS_X0212`) não podem ser escritos; o ficheiro é escrito em UTF-8 e a conversão avisa. Uma publicação no Tableau que funde por chaves precisa de `replace: true` na sua associação de destino; sem isso, a conversão avisa e publica uma nova origem de dados, o que falha numa execução em que já exista uma.

## Recusas Identificadas

Oito construções são recusadas por nome em vez de convertidas. Nenhuma reduz o escalão de um agente.

| Construção | Porque é Recusada |
| --- | --- |
| Um pedido de API Agent que transporta uma credencial e obtém o anfitrião de um campo de entrada | Cada linha poderia enviar a credencial para um anfitrião escolhido pelos dados. O pedido torna-se um marcador de posição com nome. Um pedido sem credencial e uma credencial num anfitrião fixo são convertidos. |
| Uma edição Transform sem expressão e sem passos compilados, como uma edição Copilot que tem apenas o seu pedido | Não há nada para converter: um pedido não é uma fórmula. Uma edição com passos compilados é convertida. |
| Uma construção de regex numa expressão Transform ou Filter que o PlaidCloud não consegue ler: uma classe dentro de uma classe, uma interseção de classes (`&&`) ou uma propriedade `\p{}` desconhecida | O passo torna-se um marcador de posição com nome que recusa em tempo de execução. |
| Uma função de agregação ou de janela numa expressão Transform ou Filter | O próprio Savant falha com ela em tempo de execução. Como cálculo de Transform ou num Summarize, é convertida. |
| `HASH` numa expressão Transform ou Filter com um algoritmo literal diferente de `md5` ou `sha1` | O próprio Savant falha com ela (o algoritmo é `md5` ou `sha1`). Um algoritmo lido de uma coluna é convertido, dando NULL para qualquer outro valor. |
| Uma ordenação de destino numa coluna que a sua entrada não transporta | O próprio Savant falha com ela em tempo de execução. |
| Um ficheiro, subpasta, separador ou folha de cálculo de destino por valor de uma coluna que a sua entrada não transporta | O próprio Savant falha com ele em tempo de execução. |
| Um caminho de XML Agent que não é XPath 1.0 | O Savant também não o consegue executar. |

Um URL de API relativo é convertido quando associa um URL base ou uma ligação REST com `api_bindings`; consulte [Associações no momento da conversão](/pt-pt/guides/workflows/migrate-savant-analyses/#associações-no-momento-da-conversão).

## Linguagem de Expressões

As funções e os operadores de expressão do Savant são convertidos em expressões do PlaidCloud. Escalão: **Completo**. Todas as funções e formatos são convertidos, incluindo `TO_TEXT` com um padrão numérico, um formato conhecido apenas por linha, símbolos de data com frações de segundo, baseados em semanas, trimestres e fusos, anos de dois dígitos e construções de Regex Java. As funções GEO_* em qualquer ponto de uma expressão são executadas em passos espaciais complementares. As exceções são as [recusas identificadas](#recusas-identificadas).

Casos limite conhecidos: `TO_DATE` ou `TO_DATETIME` com um formato que contém um literal `[`, `]`, aspas, barra invertida ou `^`, sobre texto que é lido como 9999-12-30 ou 9999-12-31, o que ultrapassa a última data e hora que o armazém suporta; a conversão avisa.

## Formatos de Exportação

O carregador aceita todas as formas de exportação do Savant — planas, envolvidas em modelo, registo de servidor, envelope de receita, envolvidas em matriz, com prefixo BOM e alias de tipo legados — e normaliza-as num único modelo. Escalão: **Completo**.

## Parâmetros de Análise

Os parâmetros de análise do Savant são convertidos em variáveis de fluxo de trabalho, e as referências a eles dentro das configurações dos nós são reescritas para a sintaxe de variáveis do PlaidCloud. Os parâmetros em forma de lista, dicionário e com alias são todos carregados. Escalão: **Completo**.

Casos limite conhecidos: um parâmetro cujo nome contém uma palavra secreta ou cujo valor parece uma credencial torna-se uma variável com valor em branco, com um aviso. Um parâmetro que um nó utiliza e que a exportação não declara torna-se uma variável com valor vazio, com um aviso.

## Ligar a Sistemas Externos

Os conectores do Savant são destinos de origem e de destino, não passos, e uma exportação não transporta conjuntos de dados nem credenciais. O PlaidCloud acede a estes sistemas através de uma ligação e não de um nó na área de desenho.

| Savant | Para Onde Vai no PlaidCloud |
| --- | --- |
| Conector de origem | `source_bindings` mapeia o nó ou conjunto de dados do Savant para uma tabela do PlaidCloud ou um ficheiro do Document, lido através do passo de importação correspondente; uma origem não associada avisa e não processa nada |
| Destino: CSV, Excel e outros formatos de ficheiro | Um passo de exportação ([Exportar: CSV](/pt-pt/reference/workflow-steps/export/export-to-csv/), [Exportar: Excel](/pt-pt/reference/workflow-steps/export/export-to-excel/), [Export to PDF](/pt-pt/reference/workflow-steps/export/export-to-pdf/)) |
| Destino: Google Sheets, Tableau, Slack | [Export to Google Spreadsheet](/pt-pt/reference/workflow-steps/export/export-to-google-spreadsheet/), [Publish to Tableau](/pt-pt/reference/workflow-steps/export/export-to-tableau/) ou [Notify via Slack](/pt-pt/reference/workflow-steps/notifications/notify-via-slack/), através de uma ligação que associa com `destination_bindings` |
| Destino: base de dados, armazém ou destino SaaS não associado (Oracle, base de dados genérica, Looker Studio, NetSuite, SAP, e Google Sheets, Tableau ou Slack sem ligação associada) | Uma tabela de projeto com o nome do nó de destino, com um aviso que indica o destino original |
| Destino: destino de sistema de ficheiros não associado (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | O ficheiro, no tipo de ficheiro do destino, numa pasta do Document que reflete a pasta de destino, com um aviso. As credenciais e os tokens de partilha são removidos do caminho da pasta |
| Destino: correio eletrónico não associado | Um CSV com um aviso |
| Destino: associação que não pode ser utilizada | Um CSV com um aviso que indica o destino original |

A conversão nunca contacta o sistema de origem nem de destino.
