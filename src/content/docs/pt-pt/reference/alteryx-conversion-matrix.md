---
title: Matriz de conversão do Alteryx
description: Como o PlaidCloud converte as ferramentas do Alteryx em passos de fluxo de trabalho avançado nativos, macros, variáveis e executores geridos, com o estado de suporte por ferramenta.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/alteryx-conversion-matrix.md
---

O PlaidCloud converte fluxos de trabalho, aplicações e macros do Alteryx em fluxos de trabalho
avançados nativos. O importador mapeia cada ferramenta do Alteryx para um passo de fluxo de trabalho, uma construção
de macro, uma variável controlada, uma operação de ficheiros baseada em Document ou um executor de tarefas
gerido, pelo que um fluxo de trabalho convertido é executado de forma nativa na nuvem e não como emulação.

**Quase todas as ferramentas padrão do Alteryx são convertidas por completo.** O estado de suporte abaixo
é indicado por ferramenta:

- **Completo**: converte para um passo, macro, variável, artefacto ou
  executor gerido nativo do PlaidCloud e executa a função da ferramenta. A maioria das ferramentas está aqui.
- **Parcial**: converte e é executado na sua utilização comum, embora um *modo de capacidade*
  distinto da ferramenta ainda não seja reproduzido. Raro.
- **Não suportado**: sem conversão; a capacidade é reconstruída de forma nativa.

Os conectores de sistemas externos (Salesforce, HTTP, Google Analytics, Cassandra,
correio eletrónico, Hadoop, Spark e semelhantes) são **ligados, não convertidos**; consulte
[Ligar a sistemas externos](#ligar-a-sistemas-externos).

## Suporte de ferramentas

| Ferramenta Alteryx | Estado | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Action | Completo | Associação de variáveis e configuração condicional de passos | Atualiza as definições dos passos a jusante a partir das entradas da aplicação convertida. |
| Analytic App interface (`.yxwz`) | Parcial | Front-end "App Runner" Panel publicado | O esquema `<Questions>` da aplicação é materializado numa aplicação Panel funcional que recolhe as entradas do utilizador e aciona o fluxo de trabalho convertido, publicada automaticamente como parte da conversão (uma aplicação sem widgets de entrada é ignorada). Os tipos de pergunta comuns (texto, numérico (Numeric Up Down), data, caixa de verificação, botão de opção, lista pendente, caixa de lista, árvore, navegação de ficheiros e navegação de pastas) tornam-se widgets do App Runner. Uma pergunta cujo valor não esteja associado a nenhuma variável de fluxo de trabalho é apresentada com uma nota visível, em vez de recolher silenciosamente um valor inútil, e os tipos de pergunta menos comuns são assinalados para revisão em vez de materializados. Consulte [Utilizar aplicações Alteryx convertidas](/pt-pt/guides/workflows/use-converted-alteryx-apps/#a-interface-app-runner). |
| Append Fields | Completo | Transformação de anexação de campos | Anexa campos de um fluxo a outro. |
| Auto Field | Completo | Transformação de dimensionamento automático de campos | Preserva o dimensionamento de campos inferido. |
| AutoML | Completo | [ML: Treinar modelo](/pt-pt/reference/workflow-steps/machine-learning/ml-train/) | Funde as seleções de método de modelo, alvo e algoritmo candidato num passo ML Train, tal como a Classification e a Regression. O AutoML nunca regista qual o algoritmo candidato que realmente venceu em tempo de execução no Alteryx, pelo que a conversão escolhe o primeiro algoritmo selecionado que o ML Train suporta e regista a escolha numa nota. Compare um passo AutoML convertido com os seus próprios resultados do Alteryx. |
| Barcode | Completo | Executor de códigos de barras | Lê ou escreve códigos de barras na simbologia configurada. |
| Batch Macro | Parcial | Macro expandida pela tabela de âncora de controlo | Quem chama executa a macro completa uma vez por registo da sua entrada de controlo, associando em cada passagem os parâmetros de controlo do interior, incluindo um parâmetro de controlo que quem chama renomeou para uma etiqueta de apresentação quando só um está em jogo, e uma Action `UpdateRawXml` que reescreve a lista de campos de um Select a partir de uma variável. As formas cujo valor por passagem não pode ser reproduzido em segurança falham de forma fechada, por nome, em vez de converterem incorretamente: um `UpdateRawXml` que reescreve algo diferente da lista de campos de um Select e uma Action que substitui toda a expressão de um Filter por uma variável (a sua sintaxe bruta por passagem seria avaliada incorretamente). |
| Browse | Completo | Browse / passagem direta | Preservado para inspeção, sem custo em tempo de execução. |
| Buffer | Completo | [Spatial Buffer](/pt-pt/reference/workflow-steps/spatial/spatial-buffer/) | Aumenta cada geometria numa distância fixa. |
| Build Features | Parcial | [Build Features](/pt-pt/reference/workflow-steps/tables/table-build-features/) | Converte primitivas aritméticas e de interação, extração de partes de datas, categorização com limiares explícitos, escalonamento por z-score e mín-máx e codificação one-hot. A agregação entre tabelas (Deep Feature Synthesis através do separador Manage Relationships), a PCA, a codificação do alvo e a categorização automática orientada por dados não têm equivalente; cada uma é assinalada por nome no relatório de conversão em vez de ser silenciosamente descartada. |
| Calgary Cross Count | Completo | Agregação de [base de dados Calgary](/pt-pt/guides/workflows/migrate-alteryx-workflows/#bases-de-dados-calgary) | Agrupa campos indexados e conta os valores com nome de cada campo personalizado. |
| Calgary Cross Count Append | Completo | [Calgary Cross Count Append](/pt-pt/guides/workflows/migrate-alteryx-workflows/#calgary-join-e-cross-count-append) | Compara cada registo de entrada com um índice de valores e conta quantos registos da base de dados correspondeu. |
| Calgary Input | Completo | Entrada de [base de dados Calgary](/pt-pt/guides/workflows/migrate-alteryx-workflows/#bases-de-dados-calgary) | Lê a base de dados com a consulta guardada aplicada como filtro. |
| Calgary Join | Completo | [Calgary Join](/pt-pt/guides/workflows/migrate-alteryx-workflows/#calgary-join-e-cross-count-append) | Compara cada registo com um índice de valores da base de dados, mantendo os registos que correspondem. |
| Calgary Loader | Completo | Escritor de [base de dados Calgary](/pt-pt/guides/workflows/migrate-alteryx-workflows/#bases-de-dados-calgary) | Escreve a tabela substituta à qual todos os leitores Calgary se associam. |
| Centroid | Completo | Operação do executor Centroid | Reduz cada geometria ao seu ponto central, anexado como coluna `Centroid`. |
| Check Box | Completo | Variável de fluxo de trabalho controlada | Converte as escolhas de caixa de verificação da aplicação em entrada controlada. |
| Classification | Completo | [ML: Treinar modelo](/pt-pt/reference/workflow-steps/machine-learning/ml-train/) | Funde a cadeia do Assisted Modeling num único passo ML Train com o respetivo algoritmo, alvo, atributos e hiperparâmetros. |
| Comment / Annotation / Link | Completo | Anotação da área de desenho | Preservado como contexto do fluxo de trabalho. |
| Condition | Completo | Condição do passo | Aciona avisos, erros ou ramos a partir de uma expressão. |
| Control Parameter | Completo | Parâmetro de controlo de macro | Mapeia para parâmetros de macro do PlaidCloud. |
| Convex Hull | Completo | Operação do executor Convex Hull | Constrói o menor polígono convexo que envolve cada geometria, anexado como coluna `ConvexHull`. |
| Create Points | Completo | [Table Extract](/pt-pt/reference/workflow-steps/spatial/spatial-sql-recipes/) com `geom_point` | Constrói geometria de pontos a partir de colunas de longitude/latitude, em SQL. |
| Create Samples | Completo | Table Extract, um por saída | Divide a entrada em Estimation, Validation e Holdout segundo as percentagens configuradas. |
| Cross Tab | Completo | Transformação de tabela dinâmica / cross-tab | Roda linhas em colunas com todos os métodos de agregação e os totais derivados. |
| Data Cleansing | Completo | Transformação de limpeza de dados | Limpa espaços em branco, nulos, pontuação e maiúsculas/minúsculas. |
| Date | Completo | Variável de fluxo de trabalho (data) | Emite valores de data ISO para passos e condições. |
| DateTime | Completo | Transformação de data/hora | Converte a análise e a formatação de datas e horas. |
| Detour | Completo | Encaminhamento de ramos condicional | Converte a seleção de rota em condições do DAG. |
| Detour End | Completo | Fusão de ramos condicional | Volta a juntar os ramos selecionados condicionalmente. |
| Directory | Completo | Listagem de diretório de Document | Lista ficheiros a partir de um caminho de Document. |
| Distance | Completo | [Table Extract](/pt-pt/reference/workflow-steps/spatial/spatial-sql-recipes/) com `ST_DISTANCE_SPHERE` | Distância geodésica e azimute ponto a ponto, em SQL. |
| Download | Completo | Passo [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) numa ligação REST | Transfere dados ou artefactos externos; atribua uma ligação REST ao passo convertido antes de este ser executado. |
| Drop Down | Completo | Variável de fluxo de trabalho controlada | Converte as escolhas de lista pendente da aplicação em entrada controlada. |
| Dynamic Input | Parcial | Entrada de Document dinâmica | Resolve padrões de ficheiros e entradas orientadas por variáveis em tempo de execução. Uma *ReadList* do Excel (uma folha de cálculo lida de todos os livros que uma ferramenta Directory lista e depois reunida) converte-se numa leitura de folha com glob de pasta quando um Filter a montante fixa a folha num único nome por correspondência exata. Uma folha escolhida por um Contains, por uma desigualdade ou por um filtro OR, ou uma leitura que abranja mais do que uma folha, é recusada em vez de ler a folha errada. |
| Dynamic Rename | Completo | Transformação de mudança de nome dinâmica | Muda o nome de campos a partir de metadados ou regras. |
| Dynamic Replace | Completo | Transformação de substituição dinâmica | Aplica regras de substituição a partir de um segundo fluxo. |
| Dynamic Select | Completo | Transformação de seleção dinâmica de campos | Seleciona campos por tipo, nome ou regra. |
| Error | Completo | Condição do passo (erro) | Converte o comportamento de erro configurado em condições do passo. |
| Feature Types | Completo | Configuração de atributos de [ML: Treinar modelo](/pt-pt/reference/workflow-steps/machine-learning/ml-train/) | Transporta a função de modelo atribuída a cada campo para o passo ML Train fundido. |
| File Browse | Completo | Variável de ficheiro de Document controlada | Permite que os utilizadores escolham um ficheiro para uma execução de aplicação convertida. |
| Filter | Completo | Transformação de filtro | Divide os registos por expressão em caminhos verdadeiro e falso. |
| Fit | Completo | [ML: Treinar modelo](/pt-pt/reference/workflow-steps/machine-learning/ml-train/) | Colapsa no passo ML Train fundido. |
| Folder Browse | Completo | Variável de pasta de Document controlada | Permite que os utilizadores escolham uma pasta para uma execução de aplicação convertida. |
| Formatted Excel output into a styled template | Parcial | Escritor Excel com reconhecimento de modelos ([Export to Excel Sheets](/pt-pt/reference/workflow-steps/export/export-to-excel-sheets/) para várias folhas) | Escrever num modelo com estilos preserva a formatação do modelo: valores, formatos numéricos, tipos de letra, preenchimentos, limites, células intercaladas e larguras de coluna transitam para a folha e o intervalo indicados. Isto abrange uma única folha e várias saídas reunidas em folhas diferentes de um mesmo livro, preenchidas numa única passagem, de modo que as folhas deixam de se substituir umas às outras. Um caso continua parcial: um modelo que contenha tabelas dinâmicas ou gráficos perde esses objetos quando as suas folhas são escritas. A saída Excel simples (sem estilos) é Completo; consulte Output Data. |
| Formula | Completo | Transformação de fórmula | Converte expressões de campos em expressões ou SQL do PlaidCloud. |
| Fuzzy Match | Completo | Executor de correspondência difusa | Compara por chaves, limiares e revisão de candidatos. |
| Generalize | Completo | [Spatial Generalize](/pt-pt/reference/workflow-steps/spatial/spatial-generalize/) | Simplifica a geometria até uma tolerância, preservando a topologia. |
| HTML | Completo | Texto de relatório / artefacto HTML | Preserva o conteúdo como saída de relatório ou artefacto. |
| Image Processing | Completo | Executor de transformação de imagens | Aplica escala de cinzentos, redimensionamento, recorte e rotação pela ordem da área de desenho. |
| Image Profile | Completo | Executor de perfil de imagem | Reporta dimensões, modo, formato, canais e estatísticas de luminância. |
| Image to Text | Completo | Executor de OCR | Extrai texto de imagens através de OCR gerido. |
| Input Data | Completo | Entrada de ficheiros baseada em Document | Carrega ficheiros de origem `.yxdb`, `.dbf`, Excel e `.flat` de largura fixa para os dados do fluxo de trabalho. |
| Insights | Completo | Saída de painel de controlo / artefacto | Cria um artefacto de revisão nativo da nuvem. |
| Interactive Chart | Completo | Artefacto de gráfico | Cria um artefacto de gráfico a partir dos dados convertidos. |
| Join | Completo | Transformação de junção | Produz fluxos de junção, só à esquerda e só à direita, por chave de um ou vários campos ou por posição. |
| Join Multiple | Completo | Transformação de junção múltipla | Junta vários fluxos de entrada. |
| Key/Value Pairs | Completo | [Text: NLP AI](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) (tarefa keyvalue) | Extrai pares chave/valor de uma coluna de texto através do passo NLP AI baseado em LLM, com chaves candidatas opcionais e correspondência difusa ou exata. |
| Line To Polygon | Completo | Operação do executor Line To Polygon | Fecha cada linha num anel de polígono, anexado como coluna `Polygon`. |
| List Box | Completo | Variável de fluxo de trabalho controlada | Converte as seleções de caixa de lista da aplicação em entrada controlada. |
| Location Optimizer | Parcial | [Otimizador de localização](/pt-pt/reference/workflow-steps/optimization/location-optimizer/) | Converte o caso linear de minimização de distância (escolher K locais para minimizar a distância total ou ponderada à procura) para o passo MIP nativo de p-mediana. Uma pontuação por núcleo gravitacional, uma macro de pontuação personalizada ou qualquer outro objetivo de pesquisa de candidatos continua a ser recusado; consulte [Migrar fluxos de trabalho do Alteryx](/pt-pt/guides/workflows/migrate-alteryx-workflows/#macros-num-fluxo-de-trabalho-convertido). |
| Macro calls | Completo | Invocação de macro | Importa origens de macros conhecidas e mapeia as chamadas de macro para passos de macro do PlaidCloud. |
| Macro Input / Macro Output | Completo | Porta de entrada / saída de macro | Mapeiam diretamente para portas de macro do PlaidCloud. |
| Make Grid | Completo | [Spatial Make Grid](/pt-pt/reference/workflow-steps/spatial/spatial-make-grid/) | Divide uma extensão em células quadradas, uma linha por célula. |
| Map | Completo | Artefacto de mapa | Cria um artefacto de mapa do PlaidCloud. |
| Map Input | Completo | [Importação de ficheiro espacial](/pt-pt/reference/workflow-steps/spatial/spatial-file-import/) | Lê ficheiros MapInfo, ESRI, KML e GeoJSON com os respetivos ficheiros auxiliares. |
| Master Selector | Parcial | Variável de fluxo de trabalho controlada e visibilidade condicional de passos | Converte as condições de mostrar/ocultar da ferramenta em elementos da interface para visibilidade condicional de passos. Converte o subfluxo de trabalho que a seleção executa com o melhor esforço: a validação com aplicações reais num inquilino ainda está pendente, pelo que deve rever o alvo de execução selecionado antes de se basear nele em produção. |
| Message | Completo | Condição do passo (mensagem) | Emite um aviso, mensagem ou erro do fluxo de trabalho a partir de uma condição. |
| Modeling | Completo | [ML: Treinar modelo](/pt-pt/reference/workflow-steps/machine-learning/ml-train/) | Funde-se no passo ML Train com a escolha de modelo do pipeline. |
| Multi-Field Formula | Completo | Transformação de fórmula multicampo | Aplica uma fórmula a campos selecionados. |
| Multi-Row Formula | Completo | Transformação de fórmula de janela / com reconhecimento de linhas | Converte a lógica relativa a linhas em comportamento de janela, particionado por Agrupar por. |
| Named Entity Recognition (NER) | Completo | [Text: NLP AI](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) (tarefa ner) | Extrai entidades (pessoas, organizações, localizações, datas, quantidades ou uma lista de tipos personalizada) de uma coluna de texto através do passo NLP AI baseado em LLM. |
| Numeric Up Down | Completo | Variável numérica controlada | Converte a entrada numérica da aplicação numa variável com tipo. |
| Output Data | Completo | Saída para Document / tabela | Escreve a saída em Document ou em tabelas do PlaidCloud, incluindo ficheiros Parquet e Avro; as saídas `.yxdb`, `.hyper` e `.dbf` são escritas como Parquet. |
| Overlay | Completo | [Processamento espacial](/pt-pt/reference/workflow-steps/spatial/spatial-process/) | Interseta, une ou recorta duas colunas de geometria. |
| PDF Input | Completo | Executor de extração de PDF | Extrai texto ou tabelas de PDF. |
| Point To Line | Completo | Operação do executor Point To Line | Encadeia os pontos de cada grupo numa `SequenceLine` por grupo, ordenada pelo campo de sequência. |
| Poly-Build | Completo | [Spatial Poly-Build](/pt-pt/reference/workflow-steps/spatial/spatial-poly-build/) | Constrói um polígono ou um invólucro convexo por grupo de pontos. |
| Poly-Split | Completo | [Spatial Poly-Split](/pt-pt/reference/workflow-steps/spatial/spatial-poly-split/) | Uma linha por vértice, polígono componente ou buraco. |
| Portfolio Composer (Text / Table / Image / Layout / Render) | Completo | Artefactos de relatório | Convertem o conteúdo, o esquema e a renderização do relatório em saída de relatório do PlaidCloud. |
| POS Tagger | Completo | [Text: NLP AI](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) (tarefa pos) | Etiqueta a classe gramatical de cada token de uma coluna de texto através do passo NLP AI baseado em LLM. |
| Predict | Completo | [ML: Pontuar](/pt-pt/reference/workflow-steps/machine-learning/ml-score/) | Pontua os dados com a tabela do modelo treinado e anexa uma coluna de previsão. |
| Radio Button | Completo | Variável de fluxo de trabalho controlada | Converte as escolhas de botão de opção da aplicação em entrada controlada. |
| Random % Sample | Completo | Table Extract (aleatório) | Devolve a contagem ou percentagem exata de registos pedida. |
| Record ID | Completo | Transformação de identificador de linha | Adiciona um identificador de registo determinístico no tipo e valor inicial configurados, reiniciando por grupo. |
| Redistribute | Completo | Operação do executor Redistribute | Realoca uma medida de um conjunto de geografias para outro pela área de sobreposição, anexada como coluna `Redistributed`. |
| RegEx | Completo | Transformação de expressão regular | Analisa, compara ou substitui texto. |
| Regression | Completo | [ML: Treinar modelo](/pt-pt/reference/workflow-steps/machine-learning/ml-train/) | Funde a cadeia do Assisted Modeling num único passo ML Train. |
| Report Map | Completo | Artefacto de relatório de mapa | Produz um artefacto de mapa/relatório nativo da nuvem. |
| Run Command | Parcial | Passo [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) numa ligação REST (apenas `curl`/`wget`) | Converte uma linha de comandos `curl` ou `wget` num passo Pedido REST. Os comandos de interpretador e de script (`cscript`, PowerShell, Python e semelhantes), a automatização COM do Excel, as operações de sistema de ficheiros e os comandos opacos ou que iniciam fluxos de trabalho são assinalados por nome para revisão manual em vez de convertidos automaticamente. |
| Sample | Completo | Transformação de amostra | Mantém registos por contagem, percentagem ou agrupamento. |
| Select | Completo | Passo de seleção e projeção de esquema | Seleciona, muda o nome, reordena e altera o tipo de campos. |
| Smooth | Completo | [Spatial Smooth](/pt-pt/reference/workflow-steps/spatial/spatial-smooth/) | Suaviza cada geometria ao longo de um número de passagens. |
| Sort | Completo | Transformação de ordenação | Ordena os registos pelos campos e direções configurados. |
| Spatial Info | Completo | [Spatial Info](/pt-pt/reference/workflow-steps/spatial/spatial-info/) | Área, comprimento, centroide e retângulo delimitador como medidas geodésicas. |
| Spatial Match | Completo | [Correspondência espacial](/pt-pt/reference/workflow-steps/spatial/spatial-match/) / [Spatial Match (Intersect / Unmatched)](/pt-pt/reference/workflow-steps/spatial/spatial-match-executor/) | Converte todas as relações (Within, Contains, Intersects, Touches, Crosses, Overlaps e Centroid-In), comparadas na base de dados ou no motor de fluxos de trabalho. |
| Spatial Process | Completo | [Processamento espacial](/pt-pt/reference/workflow-steps/spatial/spatial-process/) | Interseta, une ou recorta colunas de geometria. |
| Summarize | Completo | Transformação de agregação | Agrupa e agrega: soma, contagem, média, mínimo, máximo, mediana, moda, desvio padrão, variância e contagem de distintos. |
| Tab | Completo | Agrupamento de separadores da aplicação | Preservado como estrutura da aplicação convertida. |
| Test | Completo | Condição do passo | Converte as asserções de teste em condições do passo. |
| Text Box | Completo | Variável de texto controlada | Converte a entrada de texto da aplicação numa variável com tipo. |
| Text Input | Completo | Entrada de tabela em linha | Cria dados em linha para o fluxo de trabalho. |
| Text Pre-processing | Completo | Executor de pré-processamento de NLP | Normaliza e pré-processa texto. |
| Text Summary | Completo | [Text: NLP AI](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) (tarefa summary) | Resume uma coluna de texto até um número máximo de frases configurado, através do passo NLP AI baseado em LLM. |
| Text To Columns | Completo | Transformação de divisão em colunas | Divide texto em campos ou linhas. |
| Tile | Completo | Transformação de mosaico / agrupamento | Atribui grupos de mosaico segundo a regra configurada. |
| Tool Container | Completo | Contentor da área de desenho / grupo de execução | Preservado como organização do fluxo de trabalho. |
| Topic Modeling | Completo | Executor de modelação de tópicos | Executa a modelação de tópicos através de NLP gerido. |
| Transformation | Completo | Passo de transformação | Converte a lógica de transformação em expressões ou SQL do PlaidCloud. |
| Transpose | Completo | Transformação de remoção de dinamização | Converte colunas em linhas num par Nome/Valor. |
| Tree | Completo | Variável de fluxo de trabalho controlada | Converte a seleção em árvore da aplicação em entrada controlada. |
| Union | Completo | Transformação de união | Combina fluxos por nome, posição ou regras configuradas. |
| Unique | Completo | Transformação de divisão único / duplicado | Separa os primeiros registos únicos dos duplicados. |
| Visual Layout | Completo | Metadados de esquema da área de desenho | Preservado como contexto de conceção. |
| Word Cloud | Completo | Artefacto de visualização de texto | Cria um artefacto de visualização a partir da análise de texto. |
| XML Parse | Completo | Transformação de análise de XML | Extrai campos XML para os dados do fluxo de trabalho. |
| Zero-shot Text Classification | Completo | [Text: NLP AI](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) (tarefa zeroshot) | Classifica uma coluna de texto face a uma lista de etiquetas candidatas por linha, com uma ou várias etiquetas, através do passo NLP AI baseado em LLM. |
| Find Nearest | Completo | [Spatial Find Nearest](/pt-pt/reference/workflow-steps/spatial/spatial-find-nearest/) | Junção do vizinho mais próximo classificada por distância: em linha reta e por tempo de condução (classificada em minutos numa rede viária) através do motor de encaminhamento autoalojado do PlaidCloud. Tempo de condução ativado por área de trabalho. |
| Trade Area | Completo | [Spatial Trade Area](/pt-pt/reference/workflow-steps/spatial/spatial-trade-area/) | Buffers concêntricos dimensionados em unidades do mundo real: de raio fixo e áreas de influência por tempo de condução (minutos numa rede viária) através do motor de encaminhamento autoalojado. Tempo de condução ativado por área de trabalho. |
| Image Template | Completo | Operação do executor Image Template | O modo manual recorta a imagem para cada região que desenha no modelo. O modo automático deteta por si as regiões da página com um modelo de esquema de padrão aberto e emite uma linha por região, cada uma com os seus limites detetados e a confiança para revisão; uma página que o modelo não consiga ler com confiança é assinalada por nome em vez de recortada. A deteção de padrão aberto pode diferir da do próprio Alteryx: reveja as regiões detetadas ou utilize o modo manual para um controlo exato. |
| Image Recognition | Completo | Executor de reconhecimento de imagens | Treina um classificador de imagens no fluxo de trabalho e pontua novas imagens com ele, no próprio local: sem conta externa e sem que quaisquer dados saiam do PlaidCloud. O classificador é treinado de novo em vez de copiado do Alteryx, pelo que os resultados são uma aproximação fiel e não uma correspondência exata bit a bit, e o treino é executado em CPU. Ativado por área de trabalho. |
| Geocoder | Completo | Geocodificador autoalojado | Geocodifica moradas em coordenadas e geocodifica inversamente coordenadas em moradas com o geocodificador do próprio PlaidCloud: sem conta externa e sem que quaisquer dados saiam do PlaidCloud. Ativado por área de trabalho. |

Os widgets de interface (listas pendentes, caixas de lista, caixas de verificação,
entradas de texto/numéricas/de data, seletores de ficheiros e de pastas), os objetos da área de desenho (comentários, ligações,
contentores) e as portas de macro são todos convertidos em variáveis controladas ou
objetos da área de desenho nativos. O esquema completo da interface de uma aplicação Alteryx (a definição `<Questions>`
do ficheiro `.yxwz`) também é materializado num front-end "App
Runner" Panel publicado, pelo que converter a aplicação produz um formulário de entrada funcional
que recolhe os mesmos valores e aciona o fluxo de trabalho convertido, e não apenas as
variáveis controladas individuais. Consulte a linha Analytic App interface acima e
[Utilizar aplicações Alteryx convertidas](/pt-pt/guides/workflows/use-converted-alteryx-apps/#a-interface-app-runner).

**Uma nota sobre a saída Excel.** Um livro novo simples (dados escritos com a
formatação predefinida) é convertido por completo. Escrever num *modelo com estilos*, preenchendo
folhas e intervalos com nome e preservando a respetiva formatação, converte-se para uma única
folha e para várias saídas reunidas em folhas diferentes de um mesmo livro
(o passo [Export to Excel Sheets](/pt-pt/reference/workflow-steps/export/export-to-excel-sheets/)
preenche todas as folhas numa única passagem). Os modelos que contêm tabelas dinâmicas ou gráficos
perdem esses objetos quando as suas folhas são escritas; a manipulação de ficheiros ao nível da folha, acionada
a partir do Run Command (Excel COM/VBS), é assinalada por nome para revisão manual em vez de
convertida automaticamente.

## Cobertura de ferramentas espaciais

Todas as ferramentas da paleta **Spatial** do Alteryx têm uma via no PlaidCloud, e cada
uma dessas vias é um passo que também pode criar manualmente: a conversão é
uma comodidade, não a única forma de entrada. Consulte [passos geoespaciais](/pt-pt/reference/workflow-steps/spatial/)
para a referência completa e [Análise geoespacial](/pt-pt/guides/workflows/geospatial-analytics/)
para saber como se articulam.

| Ferramenta espacial do Alteryx | Via no PlaidCloud | Executado em |
| --- | --- | --- |
| Buffer | [Spatial Buffer](/pt-pt/reference/workflow-steps/spatial/spatial-buffer/) | Motor de fluxos de trabalho |
| Centroid | Operação do executor Centroid | Motor de fluxos de trabalho |
| Convex Hull | Operação do executor Convex Hull | Motor de fluxos de trabalho |
| Create Points | [Expressão Table Extract](/pt-pt/reference/workflow-steps/spatial/spatial-sql-recipes/) | Base de dados |
| Distance | [Expressão Table Extract](/pt-pt/reference/workflow-steps/spatial/spatial-sql-recipes/) | Base de dados |
| Find Nearest | [Spatial Find Nearest](/pt-pt/reference/workflow-steps/spatial/spatial-find-nearest/) | Base de dados; serviço de encaminhamento para o tempo de condução |
| Generalize | [Spatial Generalize](/pt-pt/reference/workflow-steps/spatial/spatial-generalize/) | Motor de fluxos de trabalho |
| Heat Map | [Heat Map (macro)](/pt-pt/reference/workflow-steps/macros/macro-heat-map/) | Motor de fluxos de trabalho |
| Line To Polygon | Operação do executor Line To Polygon | Motor de fluxos de trabalho |
| Make Grid | [Spatial Make Grid](/pt-pt/reference/workflow-steps/spatial/spatial-make-grid/) | Motor de fluxos de trabalho |
| Point To Line | Operação do executor Point To Line | Motor de fluxos de trabalho |
| Poly-Build | [Spatial Poly-Build](/pt-pt/reference/workflow-steps/spatial/spatial-poly-build/) | Motor de fluxos de trabalho |
| Poly-Split | [Spatial Poly-Split](/pt-pt/reference/workflow-steps/spatial/spatial-poly-split/) | Motor de fluxos de trabalho |
| Redistribute | Operação do executor Redistribute | Motor de fluxos de trabalho |
| Smooth | [Spatial Smooth](/pt-pt/reference/workflow-steps/spatial/spatial-smooth/) | Motor de fluxos de trabalho |
| Spatial Info | [Spatial Info](/pt-pt/reference/workflow-steps/spatial/spatial-info/) | Motor de fluxos de trabalho |
| Spatial Match | [Correspondência espacial](/pt-pt/reference/workflow-steps/spatial/spatial-match/) | Base de dados |
| Spatial Match: objeto de interseção, Unmatched | [Spatial Match (Intersect / Unmatched)](/pt-pt/reference/workflow-steps/spatial/spatial-match-executor/) | Motor de fluxos de trabalho |
| Spatial Process | [Processamento espacial](/pt-pt/reference/workflow-steps/spatial/spatial-process/) | Motor de fluxos de trabalho |
| Trade Area (raio fixo + tempo de condução) | [Spatial Trade Area](/pt-pt/reference/workflow-steps/spatial/spatial-trade-area/) | Motor de fluxos de trabalho; serviço de encaminhamento para o tempo de condução |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/pt-pt/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | Motor de fluxos de trabalho |
| Entrada de ficheiro espacial | [Importação de ficheiro espacial](/pt-pt/reference/workflow-steps/spatial/spatial-file-import/) | Motor de fluxos de trabalho |
| Summarize: SpatialObjCombine, SpatialObjConvexHull | [Combinação espacial](/pt-pt/reference/workflow-steps/spatial/spatial-combine/) | Motor de fluxos de trabalho |
| Report Map | [Report Map](/pt-pt/reference/workflow-steps/reports/report-map/) | Motor de fluxos de trabalho |

**Áreas de influência por tempo de condução e vizinho mais próximo**: os anéis de tempo de condução da Trade Area e a classificação por tempo de condução da Find
Nearest são executados no motor de encaminhamento autoalojado do PlaidCloud
(isócronas da rede viária e matrizes de tempo de viagem), e não numa API
de terceiros alojada, pelo que as coordenadas de origem nunca saem da plataforma. O tempo de condução é ativado por
área de trabalho. O encaminhamento e as áreas de tempo de condução utilizam dados do OpenStreetMap:
© OpenStreetMap contributors, disponíveis ao abrigo da [Open Database License
(ODbL)](https://www.openstreetmap.org/copyright).

### Pré-requisitos espaciais conhecidos

As próprias ferramentas espaciais são convertidas; estes são pré-requisitos da entrada.

- **O formato GeoFile `.geo`.** O GeoFile binário proprietário do Alteryx não tem
  leitor aberto, pelo que a importação de um falha de forma fechada em vez de falhar em tempo
  de execução. No Alteryx, volte a exportar a camada para um formato espacial padrão
  (shapefile ou GeoJSON) e importe esse; os outros formatos espaciais não são
  afetados. Consulte
  [Migrar fluxos de trabalho espaciais do Alteryx](/pt-pt/guides/workflows/migrate-spatial-alteryx-workflows/#empacotar-as-entradas-espaciais).
- **A medida Peano key do Spatial Info.** A Peano key é um índice espacial proprietário do Alteryx
  sem especificação pública, pelo que um Spatial Info que a peça
  ignora essa coluna e indica-o numa nota. Todas as outras medidas do Spatial Info
  (área, comprimento, centroide, retângulo delimitador, tipo de objeto, contagens de partes e de pontos
  e pontos finais) são convertidas.
- **Coordenadas projetadas do Create Points.** O Create Points converte diretamente
  coordenadas lon/lat em vírgula flutuante e inteiras (×1.000.000).
  As coordenadas que já estejam num sistema projetado têm de ser primeiro reprojetadas para lon/lat WGS84
  a montante, porque o fluxo de trabalho não regista a projeção que utilizam.

## Cobertura de ferramentas Calgary

Uma base de dados Calgary (`.cydb`) do Alteryx é um repositório indexado proprietário que o PlaidCloud não consegue abrir. A conversão trata cada uma como correspondendo a uma tabela normal do PlaidCloud, com o nome `calgary_<database name>`, pelo que as ferramentas construídas em torno dela são convertidas como operações normais de tabelas em vez de serem recusadas por completo. Consulte [Bases de dados Calgary](/pt-pt/guides/workflows/migrate-alteryx-workflows/#bases-de-dados-calgary) para saber como funciona a tabela substituta e [Calgary Join e Cross Count Append](/pt-pt/guides/workflows/migrate-alteryx-workflows/#calgary-join-e-cross-count-append) para as ferramentas de correspondência de índices.

| Ferramenta Calgary do Alteryx | Via no PlaidCloud | Converte |
| --- | --- | --- |
| Calgary Loader | Table Extract a escrever `calgary_<database>` | Sim, depois de a base de dados ter nome e de armazenar pelo menos um campo de dados. |
| Calgary Input | Entrada de Document dinâmica a ler `calgary_<database>`, com a consulta guardada como filtro | Sim, incluindo uma consulta construída a partir de um Or ou envolvida num Not, e um filtro contains ou starts-with (reconstruído como um SQL LIKE). Recusa uma consulta de pesquisa espacial e os limites Skip Records/Max Records. |
| Calgary Input (Count Only) / Calgary Cross Count | Transformação de agregação sobre `calgary_<database>` | Sim, incluindo um grupo construído a partir de um Or ou envolvido num Not. Recusa um cruzamento sobre mais do que um campo personalizado e uma leitura de apenas contagem que não indique nenhuma coluna sobre a qual contar. |
| Calgary Join | Entrada de Document dinâmica que compara cada registo da sua entrada com `calgary_<database>` | Quando o campo de entrada é um valor simples comparado com um índice de valores, incluindo o modo Count Only, que conta os registos da base de dados com que cada registo de entrada correspondeu, contando zero um registo sem correspondências. Recusa quando o campo é espacial (reconstrua como Spatial Match) ou o seu tipo não está resolvido, e em Joins com índice de intervalo ou com saída sem correspondência ligada, num Join sem campo de correspondência indicado e num Join sem nada ligado à sua entrada. |
| Calgary Cross Count Append | Entrada de Document dinâmica que compara cada registo e, depois, uma junção com contagem sobre `calgary_<database>` | Quando o campo de entrada é um valor simples comparado com um índice de valores: conta, por registo de entrada, os registos da base de dados correspondidos, e um registo sem correspondências conta zero. Recusa um índice espacial ou não resolvido (reconstrua como Spatial Match), uma grelha de contagem cruzada de valores personalizados, um índice de intervalo e uma correspondência que não indique nenhum campo. |

### Pré-requisitos Calgary conhecidos

A maioria destes são pré-requisitos da entrada e não limites da conversão.

- **Uma correspondência de índice espacial tem de ser reconstruída como Spatial Match.** Um Calgary Join ou Cross Count Append comparado com um índice espacial é recusado, indicando a tabela substituta: o fluxo de trabalho regista o nome do índice, mas não se contém valores normais ou geometria espacial, e uma correspondência de valores (uma junção por igualdade) e uma correspondência espacial (ponto em polígono) são operações diferentes. Exporte a base de dados para uma tabela e reconstrua a correspondência como Join (índice de valores) ou Spatial Match (índice espacial).
- **Uma leitura limitada por Skip Records ou Max Records precisa de uma ordem explícita.** A tabela substituta exportada não tem ordem de registos, pelo que, se precisar de obter os primeiros ou os últimos N registos por posição, adicione uma coluna de ordem ao exportar.
- **Uma base de dados demográfica ou de referência tem de ser carregada primeiro.** Uma leitura Calgary antes de a respetiva base de dados ter sido carregada é interrompida, indicando a tabela a criar. O próprio ficheiro `.cydb` não tem leitor aberto, pelo que o deve voltar a exportar no Alteryx (um Calgary Input para uma ferramenta Output Data a escrever CSV ou Parquet) e importá-lo como a tabela com o nome indicado; consulte [Bases de dados .cydb (Calgary) ilegíveis](/pt-pt/guides/workflows/troubleshoot-alteryx-imports/#bases-de-dados-cydb-calgary-ilegíveis). Este é o caso comum dos ficheiros `.cydb` demográficos e de referência licenciados que o Alteryx fornece (Experian, Census e semelhantes): nenhum conversor consegue reproduzir esses dados de terceiros, pelo que deve trazer os seus próprios dados de referência licenciados e carregá-los na tabela com o nome indicado, tal como com os dados de referência do Geocoder.
- **Um Calgary Loader que não armazene nenhum campo de dados não converte**, uma vez que a tabela que escrevesse não teria colunas.
- **Uma grelha de contagem cruzada de valores personalizados ainda não converte.** Um único campo de contagem cruzada simples converte (conta, por registo de entrada, os registos correspondentes da base de dados), mas uma grelha de valores personalizados *com nome* anexaria uma coluna de contagem por valor, e o Alteryx não documenta quantas colunas são nem como as designa. Previsto para uma versão futura, a aguardar uma exportação de referência para fazer engenharia inversa do contrato de colunas.

As consultas por valor, intervalo, contains e starts-with são todas convertidas num filtro; apenas uma consulta de pesquisa espacial, uma operação de índice sem equivalente ao nível da coluna, não o é.

## Ligar a sistemas externos

Os pontos finais de conectores do Alteryx (Salesforce, HTTP, Google Analytics, Cassandra,
correio eletrónico, Hadoop e Spark, em ambas as direções) não são convertidos, porque
o PlaidCloud acede a estes sistemas através de uma ligação e não através de uma
ferramenta na área de desenho. Cada um é recusado por nome e indica onde o trabalho
deve ser feito:

| Ferramenta Alteryx | Onde fica no PlaidCloud |
| --- | --- |
| Salesforce Input / Output | Uma ligação **Salesforce** |
| Anaplan | Uma ligação **Anaplan** |
| HTTP Input | Um passo **Pedido REST** numa ligação **REST** |
| Google Analytics Input | **Importar: Origem Singer** com o tap do Google Analytics |
| Cassandra Input | **Importar: Origem Singer** com o tap do Cassandra |
| Email Input | **Importar: Origem Singer** com o tap do GMail |
| Hadoop Input / Output | **Importar: SQL** / **Exportar: SQL** através de uma ligação Hive, Impala ou Presto |
| Spark Input / Output | **Importar: SQL** / **Exportar: SQL** através de uma ligação Databricks |

Quatro destes não têm qualquer via de escrita. O PlaidCloud lê o Google Analytics
e o Cassandra, mas nunca escreve neles, pelo que uma ferramenta Google Analytics Output ou
Cassandra Output passa a ser um **Exportar: SQL** para um destino suportado. O correio eletrónico também não é um destino de dados: **Notificar: Correio eletrónico** envia uma
notificação a pessoas, pelo que uma ferramenta Email Output passa a ser um passo de exportação mais uma
notificação separada. A ligação **Anaplan** é só de leitura da mesma
forma: lê uma vista guardada, executa uma ação de exportação já existente ou carrega listas
para uma dimensão do PlaidCloud, mas não existe nenhum passo do PlaidCloud que
escreva de volta no Anaplan.

## Validar um fluxo de trabalho convertido

Para fluxos de trabalho de produção, valide as saídas convertidas face a saídas fiáveis do Alteryx:
a validação do PlaidCloud incide no esquema, na contagem de linhas e nos valores das linhas,
e ignora a ordem das linhas, a menos que o fluxo de trabalho dependa dela. As operações especializadas
(espaciais, correspondência difusa, OCR, NLP, relatórios) são executadas através de executores de tarefas geridos
que mantêm o fluxo de trabalho nativo da nuvem; os pipelines de aprendizagem automática
são convertidos nos passos nativos [ML: Treinar modelo](/pt-pt/reference/workflow-steps/machine-learning/ml-train/)
e [ML: Pontuar](/pt-pt/reference/workflow-steps/machine-learning/ml-score/).
Consulte [Migrar fluxos de trabalho do Alteryx](/pt-pt/guides/workflows/migrate-alteryx-workflows/)
para o guia completo de importação e validação.
