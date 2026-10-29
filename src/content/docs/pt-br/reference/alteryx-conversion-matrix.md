---
title: Matriz de conversão do Alteryx
description: Como o PlaidCloud converte ferramentas do Alteryx em etapas de fluxo de trabalho avançado nativas, macros, variáveis e executores gerenciados, com o status de suporte por ferramenta.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/alteryx-conversion-matrix.md
---

O PlaidCloud converte fluxos de trabalho, aplicativos e macros do Alteryx em fluxos de trabalho
avançados nativos. O importador mapeia cada ferramenta do Alteryx para uma etapa de fluxo de trabalho, uma construção
de macro, uma variável controlada, uma operação de arquivo baseada em Document ou um executor de
trabalho gerenciado, de modo que um fluxo de trabalho convertido é executado de forma nativa na nuvem, e não como uma emulação.

**Quase todas as ferramentas padrão do Alteryx são convertidas por completo.** O status de suporte abaixo
é por ferramenta:

- **Completo**: converte para uma etapa, macro, variável, artefato ou executor
  gerenciado nativo do PlaidCloud e executa a função da ferramenta. A maioria das ferramentas está aqui.
- **Parcial**: converte e é executado no uso comum, enquanto um *modo de capacidade* distinto
  da ferramenta ainda não é reproduzido. É raro.
- **Não compatível**: sem conversão; a capacidade é recriada de forma nativa.

Os conectores de sistemas externos (Salesforce, HTTP, Google Analytics, Cassandra,
e-mail, Hadoop, Spark e similares) são **conectados, não convertidos**. Consulte
[Conexão com sistemas externos](#conexão-com-sistemas-externos).

## Suporte por ferramenta

| Ferramenta do Alteryx | Status | Equivalente no PlaidCloud | Converte |
| --- | --- | --- | --- |
| Action | Completo | Vinculação de variável e configuração condicional de etapa | Atualiza as configurações das etapas posteriores a partir das entradas do aplicativo convertido. |
| Analytic App interface (`.yxwz`) | Parcial | Front-end "App Runner" do Panel publicado | O layout `<Questions>` do aplicativo é materializado em um aplicativo Panel funcional que coleta as entradas do usuário e aciona o fluxo de trabalho convertido, publicado automaticamente como parte da conversão (um aplicativo sem widgets de entrada é ignorado). Os tipos de pergunta comuns (texto, numérico (Numeric Up Down), data, caixa de seleção, botão de opção, lista suspensa, caixa de listagem, árvore, navegação de arquivo e navegação de pasta) tornam-se widgets do App Runner. Uma pergunta cujo valor não se vincula a nenhuma variável de fluxo de trabalho é renderizada com uma observação visível, em vez de coletar silenciosamente um valor inútil, e os tipos de pergunta menos comuns são sinalizados para revisão em vez de materializados. Consulte [Usar aplicativos Alteryx convertidos](/pt-br/guides/workflows/use-converted-alteryx-apps/#o-front-end-app-runner). |
| Append Fields | Completo | Transformação de acréscimo de campos | Acrescenta campos de um fluxo a outro. |
| Auto Field | Completo | Transformação de dimensionamento automático de campos | Preserva o dimensionamento de campos inferido. |
| AutoML | Completo | [ML: Treinar modelo](/pt-br/reference/workflow-steps/machine-learning/ml-train/) | Funde as seleções de método de modelo, destino e algoritmos candidatos em uma etapa ML Train, da mesma forma que Classification e Regression. O AutoML nunca registra qual algoritmo candidato realmente venceu no momento da execução no Alteryx, então a conversão escolhe o primeiro algoritmo marcado que o ML Train suporta e anota a escolha. Compare uma etapa AutoML convertida com os seus próprios resultados do Alteryx. |
| Barcode | Completo | Executor de código de barras | Lê ou grava códigos de barras na simbologia configurada. |
| Batch Macro | Parcial | Macro distribuída pela tabela de âncora de controle | O chamador executa a macro inteira uma vez por registro de sua entrada de controle, vinculando os parâmetros de controle do interior a cada passagem, inclusive um parâmetro de controle que o chamador renomeou para um rótulo de exibição quando exatamente um está em uso, e uma Action `UpdateRawXml` que reescreve a lista de campos de um Select a partir de uma variável. Os formatos cujo valor por passagem não pode ser reproduzido com segurança falham de forma fechada, pelo nome, em vez de converter incorretamente: um `UpdateRawXml` que reescreve qualquer coisa além da lista de campos de um Select e uma Action que substitui toda a expressão de um Filter por uma variável (sua sintaxe bruta por passagem seria avaliada incorretamente). |
| Browse | Completo | Browse / passagem direta | Preservado para inspeção, sem custo em tempo de execução. |
| Buffer | Completo | etapa [Spatial Buffer](/pt-br/reference/workflow-steps/spatial/spatial-buffer/) | Expande cada geometria por uma distância fixa. |
| Build Features | Parcial | etapa [Build Features](/pt-br/reference/workflow-steps/tables/table-build-features/) | Converte primitivos aritméticos e de interação, extração de partes de data, agrupamento em faixas com limites explícitos, escalonamento por z-score e mín-máx, e codificação one-hot. A agregação entre tabelas (Deep Feature Synthesis pela guia Manage Relationships), o PCA, a codificação de destino e o agrupamento automático orientado por dados não têm equivalente: cada um é sinalizado pelo nome no relatório de conversão, em vez de descartado silenciosamente. |
| Calgary Cross Count | Completo | Agregação de [banco de dados Calgary](/pt-br/guides/workflows/migrate-alteryx-workflows/#bancos-de-dados-calgary) | Agrupa campos indexados e conta os valores nomeados de cada campo personalizado. |
| Calgary Cross Count Append | Completo | [Calgary Cross Count Append](/pt-br/guides/workflows/migrate-alteryx-workflows/#calgary-join-e-cross-count-append) | Compara cada registro de entrada com um índice de valores e, depois, conta quantos registros do banco de dados ele correspondeu. |
| Calgary Input | Completo | Entrada de [banco de dados Calgary](/pt-br/guides/workflows/migrate-alteryx-workflows/#bancos-de-dados-calgary) | Lê o banco de dados com a consulta salva aplicada como filtro. |
| Calgary Join | Completo | [Calgary Join](/pt-br/guides/workflows/migrate-alteryx-workflows/#calgary-join-e-cross-count-append) | Compara cada registro com um índice de valores no banco de dados, mantendo os registros correspondentes. |
| Calgary Loader | Completo | Gravador de [banco de dados Calgary](/pt-br/guides/workflows/migrate-alteryx-workflows/#bancos-de-dados-calgary) | Grava a tabela substituta à qual todo leitor Calgary se vincula. |
| Centroid | Completo | Operação Centroid do executor | Reduz cada geometria ao seu ponto central, acrescentado como uma coluna `Centroid`. |
| Check Box | Completo | Variável de fluxo de trabalho controlada | Converte as escolhas de caixa de seleção do aplicativo em entrada controlada. |
| Classification | Completo | [ML: Treinar modelo](/pt-br/reference/workflow-steps/machine-learning/ml-train/) | Funde a cadeia do Assisted Modeling em uma única etapa ML Train com seu algoritmo, destino, atributos e hiperparâmetros. |
| Comment / Annotation / Link | Completo | Anotação da tela | Preservado como contexto do fluxo de trabalho. |
| Condition | Completo | Condição de etapa | Dispara avisos, erros ou ramificações a partir de uma expressão. |
| Control Parameter | Completo | Parâmetro de controle de macro | Mapeia para os parâmetros de macro do PlaidCloud. |
| Convex Hull | Completo | Operação Convex Hull do executor | Constrói o menor polígono convexo que envolve cada geometria, acrescentado como uma coluna `ConvexHull`. |
| Create Points | Completo | etapa [Table Extract](/pt-br/reference/workflow-steps/spatial/spatial-sql-recipes/) com `geom_point` | Constrói geometria de pontos a partir de colunas de longitude/latitude, em SQL. |
| Create Samples | Completo | etapa Table Extract, uma por saída | Divide a entrada em Estimation, Validation e Holdout nos percentuais configurados. |
| Cross Tab | Completo | Transformação de tabela dinâmica / tabulação cruzada | Gira linhas em colunas em todos os métodos de agregação e nos totais derivados. |
| Data Cleansing | Completo | Transformação de limpeza de dados | Limpa espaços em branco, nulos, pontuação e maiúsculas/minúsculas. |
| Date | Completo | Variável de fluxo de trabalho (data) | Emite valores de data ISO para etapas e condições. |
| DateTime | Completo | Transformação de data/hora | Converte a análise e a formatação de data e hora. |
| Detour | Completo | Roteamento condicional de ramificação | Converte a seleção de rota em condições do DAG. |
| Detour End | Completo | Mesclagem condicional de ramificação | Reúne as ramificações selecionadas condicionalmente. |
| Directory | Completo | Listagem de diretório do Document | Lista arquivos de um caminho do Document. |
| Distance | Completo | etapa [Table Extract](/pt-br/reference/workflow-steps/spatial/spatial-sql-recipes/) com `ST_DISTANCE_SPHERE` | Distância geodésica e direção entre pontos, em SQL. |
| Download | Completo | Etapa [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) em uma conexão REST | Baixa dados ou artefatos externos; atribua uma conexão REST à etapa convertida antes de executá-la. |
| Drop Down | Completo | Variável de fluxo de trabalho controlada | Converte as escolhas de lista suspensa do aplicativo em entrada controlada. |
| Dynamic Input | Parcial | Entrada Document dinâmica | Resolve padrões de arquivo e entradas orientadas por variáveis em tempo de execução. Uma *ReadList* do Excel (uma planilha lida de todas as pastas de trabalho listadas por uma ferramenta Directory e depois unida) é convertida em uma leitura de planilha por padrão de pasta quando um Filter anterior fixa a planilha em um único nome por correspondência exata. Uma planilha escolhida por Contains, por uma desigualdade ou por um filtro OR, ou uma leitura que abrange mais de uma planilha, é recusada em vez de ler a planilha errada. |
| Dynamic Rename | Completo | Transformação de renomeação dinâmica | Renomeia campos a partir de metadados ou regras. |
| Dynamic Replace | Completo | Transformação de substituição dinâmica | Aplica regras de substituição de um segundo fluxo. |
| Dynamic Select | Completo | Transformação de seleção dinâmica de campos | Seleciona campos por tipo, nome ou regra. |
| Error | Completo | Condição de etapa (erro) | Converte o comportamento de erro configurado em condições de etapa. |
| Feature Types | Completo | Configuração de atributos de [ML: Treinar modelo](/pt-br/reference/workflow-steps/machine-learning/ml-train/) | Leva a função de modelo atribuída a cada campo para a etapa ML Train fundida. |
| File Browse | Completo | Variável de arquivo do Document controlada | Permite que os usuários escolham um arquivo para a execução de um aplicativo convertido. |
| Filter | Completo | Transformação de filtro | Divide os registros por expressão em caminhos verdadeiro e falso. |
| Fit | Completo | [ML: Treinar modelo](/pt-br/reference/workflow-steps/machine-learning/ml-train/) | É incorporado à etapa ML Train fundida. |
| Folder Browse | Completo | Variável de pasta do Document controlada | Permite que os usuários escolham uma pasta para a execução de um aplicativo convertido. |
| Formatted Excel output into a styled template | Parcial | Gravador de Excel com reconhecimento de modelo (etapa [Export to Excel Sheets](/pt-br/reference/workflow-steps/export/export-to-excel-sheets/) para várias planilhas) | Gravar em um modelo com estilos preserva a formatação do modelo: valores, formatos numéricos, fontes, preenchimentos, bordas, células mescladas e larguras de coluna são transferidos para a planilha e o intervalo nomeados. Isso cobre tanto uma única planilha quanto várias saídas montadas em planilhas diferentes de uma mesma pasta de trabalho, preenchidas em uma única passagem, de modo que as planilhas não se sobrescrevem mais. Um caso continua parcial: um modelo que contém tabelas dinâmicas ou gráficos descarta esses objetos quando suas planilhas são gravadas. A saída simples (sem estilos) do Excel é Completo; consulte Output Data. |
| Formula | Completo | Transformação de fórmula | Converte expressões de campo em expressões ou SQL do PlaidCloud. |
| Fuzzy Match | Completo | Executor de correspondência aproximada | Faz a correspondência por chaves, limites e revisão de candidatos. |
| Generalize | Completo | etapa [Spatial Generalize](/pt-br/reference/workflow-steps/spatial/spatial-generalize/) | Simplifica a geometria até uma tolerância, preservando a topologia. |
| HTML | Completo | Texto de relatório / artefato HTML | Preserva o conteúdo como saída de relatório ou de artefato. |
| Image Processing | Completo | Executor de transformação de imagem | Aplica escala de cinza, escala, corte e rotação na ordem da tela. |
| Image Profile | Completo | Executor de perfil de imagem | Informa dimensões, modo, formato, canais e estatísticas de luminância. |
| Image to Text | Completo | Executor de OCR | Extrai texto de imagens por meio de OCR gerenciado. |
| Input Data | Completo | Entrada de arquivo baseada em Document | Carrega arquivos de origem `.yxdb`, `.dbf`, Excel e `.flat` de largura fixa em dados do fluxo de trabalho. |
| Insights | Completo | Saída de painel / artefato | Cria um artefato de revisão nativo da nuvem. |
| Interactive Chart | Completo | Artefato de gráfico | Cria um artefato de gráfico a partir dos dados convertidos. |
| Join | Completo | Transformação de junção | Produz fluxos unidos, somente à esquerda e somente à direita em uma chave de um ou vários campos ou por posição. |
| Join Multiple | Completo | Transformação de junção múltipla | Une vários fluxos de entrada. |
| Key/Value Pairs | Completo | [Text: NLP AI](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) (tarefa keyvalue) | Extrai pares chave/valor de uma coluna de texto por meio da etapa NLP AI baseada em LLM, com chaves candidatas opcionais e correspondência aproximada ou exata. |
| Line To Polygon | Completo | Operação Line To Polygon do executor | Fecha cada linha em um anel de polígono, acrescentado como uma coluna `Polygon`. |
| List Box | Completo | Variável de fluxo de trabalho controlada | Converte as seleções de lista do aplicativo em entrada controlada. |
| Location Optimizer | Parcial | etapa [Otimizador de localização](/pt-br/reference/workflow-steps/optimization/location-optimizer/) | Converte o caso linear de minimização de distância (escolher K locais para minimizar a distância total ou ponderada até a demanda) para a etapa MIP nativa de p-mediana. Uma pontuação de núcleo gravitacional, uma macro de pontuação personalizada ou qualquer outro objetivo de busca de candidatos ainda é recusado; consulte [Migrar fluxos de trabalho do Alteryx](/pt-br/guides/workflows/migrate-alteryx-workflows/#macros-em-um-fluxo-de-trabalho-convertido). |
| Macro calls | Completo | Invocação de macro | Importa fontes de macro conhecidas e mapeia as chamadas de macro para etapas de macro do PlaidCloud. |
| Macro Input / Macro Output | Completo | Porta de entrada / saída de macro | Mapeiam diretamente para as portas de macro do PlaidCloud. |
| Make Grid | Completo | etapa [Criar grade](/pt-br/reference/workflow-steps/spatial/spatial-make-grid/) | Divide uma extensão em células quadradas, uma linha por célula. |
| Map | Completo | Artefato de mapa | Cria um artefato de mapa do PlaidCloud. |
| Map Input | Completo | [Importar arquivo espacial](/pt-br/reference/workflow-steps/spatial/spatial-file-import/) | Lê arquivos MapInfo, ESRI, KML e GeoJSON com seus arquivos auxiliares. |
| Master Selector | Parcial | Variável de fluxo de trabalho controlada e visibilidade condicional de etapa | Converte as condições de mostrar/ocultar da ferramenta nos elementos de interface em visibilidade condicional de etapa. Converte qual subfluxo de trabalho a seleção executa com o melhor esforço; a validação com aplicativos reais no locatário ainda está pendente, então revise o destino de execução selecionado antes de depender dele em produção. |
| Message | Completo | Condição de etapa (mensagem) | Emite um aviso, uma mensagem ou um erro do fluxo de trabalho a partir de uma condição. |
| Modeling | Completo | [ML: Treinar modelo](/pt-br/reference/workflow-steps/machine-learning/ml-train/) | Funde-se à etapa ML Train com a escolha de modelo do pipeline. |
| Multi-Field Formula | Completo | Transformação de fórmula de vários campos | Aplica uma fórmula a campos selecionados. |
| Multi-Row Formula | Completo | Transformação de fórmula de janela / com reconhecimento de linha | Converte a lógica relativa a linhas em comportamento de janela, particionada por Agrupar por. |
| Named Entity Recognition (NER) | Completo | [Text: NLP AI](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) (tarefa ner) | Extrai entidades (pessoas, organizações, locais, datas, quantidades ou uma lista de tipos personalizada) de uma coluna de texto por meio da etapa NLP AI baseada em LLM. |
| Numeric Up Down | Completo | Variável numérica controlada | Converte a entrada numérica do aplicativo em uma variável tipada. |
| Output Data | Completo | Saída em Document / tabela | Grava a saída em Document ou em tabelas do PlaidCloud, incluindo arquivos Parquet e Avro; as saídas `.yxdb`, `.hyper` e `.dbf` são gravadas como Parquet. |
| Overlay | Completo | [Processo espacial](/pt-br/reference/workflow-steps/spatial/spatial-process/) | Interseção, união ou recorte de duas colunas de geometria. |
| PDF Input | Completo | Executor de extração de PDF | Extrai texto ou tabelas de PDFs. |
| Point To Line | Completo | Operação Point To Line do executor | Encadeia os pontos de cada grupo em uma `SequenceLine` por grupo, ordenada pelo campo de sequência. |
| Poly-Build | Completo | etapa [Spatial Poly-Build](/pt-br/reference/workflow-steps/spatial/spatial-poly-build/) | Constrói um polígono ou um casco convexo por grupo de pontos. |
| Poly-Split | Completo | etapa [Spatial Poly-Split](/pt-br/reference/workflow-steps/spatial/spatial-poly-split/) | Uma linha por vértice, polígono componente ou furo. |
| Portfolio Composer (Text / Table / Image / Layout / Render) | Completo | Artefatos de relatório | Convertem o conteúdo, o layout e a renderização do relatório em saída de relatório do PlaidCloud. |
| POS Tagger | Completo | [Text: NLP AI](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) (tarefa pos) | Marca a classe gramatical de cada token de uma coluna de texto por meio da etapa NLP AI baseada em LLM. |
| Predict | Completo | [ML: Pontuar](/pt-br/reference/workflow-steps/machine-learning/ml-score/) | Pontua os dados com a tabela do modelo treinado e acrescenta uma coluna de previsão. |
| Radio Button | Completo | Variável de fluxo de trabalho controlada | Converte as escolhas de botão de opção do aplicativo em entrada controlada. |
| Random % Sample | Completo | Table Extract (aleatório) | Retorna a contagem ou o percentual exato de registros solicitado. |
| Record ID | Completo | Transformação de identificador de linha | Adiciona um identificador de registro determinístico no tipo e no valor inicial configurados, reiniciando por grupo. |
| Redistribute | Completo | Operação Redistribute do executor | Realoca uma medida de um conjunto de áreas geográficas para outro pela área de sobreposição, acrescentada como uma coluna `Redistributed`. |
| RegEx | Completo | Transformação de expressão regular | Analisa, corresponde ou substitui texto. |
| Regression | Completo | [ML: Treinar modelo](/pt-br/reference/workflow-steps/machine-learning/ml-train/) | Funde a cadeia do Assisted Modeling em uma única etapa ML Train. |
| Report Map | Completo | Artefato de relatório de mapa | Produz um artefato de mapa/relatório nativo da nuvem. |
| Run Command | Parcial | Etapa [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) em uma conexão REST (somente `curl`/`wget`) | Converte uma linha de comando `curl` ou `wget` em uma etapa Solicitação REST. Comandos de interpretador e de script (`cscript`, PowerShell, Python e similares), automação COM do Excel, operações de sistema de arquivos e comandos opacos ou que iniciam fluxos de trabalho são sinalizados pelo nome para revisão manual, em vez de convertidos automaticamente. |
| Sample | Completo | Transformação de amostra | Mantém registros por contagem, percentual ou agrupamento. |
| Select | Completo | Etapa de seleção e projeção de esquema | Seleciona, renomeia, reordena e retipa campos. |
| Smooth | Completo | etapa [Spatial Smooth](/pt-br/reference/workflow-steps/spatial/spatial-smooth/) | Suaviza cada geometria ao longo de um número de passagens. |
| Sort | Completo | Transformação de ordenação | Ordena os registros pelos campos e direções configurados. |
| Spatial Info | Completo | etapa [Spatial Info](/pt-br/reference/workflow-steps/spatial/spatial-info/) | Área, comprimento, centroide e retângulo delimitador como medidas geodésicas. |
| Spatial Match | Completo | [Correspondência espacial](/pt-br/reference/workflow-steps/spatial/spatial-match/) / etapa [Spatial Match (Intersect / Unmatched)](/pt-br/reference/workflow-steps/spatial/spatial-match-executor/) | Converte todas as relações (Within, Contains, Intersects, Touches, Crosses, Overlaps e Centroid-In), correspondidas no banco de dados ou no mecanismo de fluxo de trabalho. |
| Spatial Process | Completo | [Processo espacial](/pt-br/reference/workflow-steps/spatial/spatial-process/) | Interseção, união ou recorte de colunas de geometria. |
| Summarize | Completo | Transformação de agregação | Agrupa e agrega: soma, contagem, média, mínimo, máximo, mediana, moda, desvio padrão, variância e contagem distinta. |
| Tab | Completo | Agrupamento de guias do aplicativo | Preservado como estrutura do aplicativo convertido. |
| Test | Completo | Condição de etapa | Converte as asserções de teste em condições de etapa. |
| Text Box | Completo | Variável de texto controlada | Converte a entrada de texto do aplicativo em uma variável tipada. |
| Text Input | Completo | Entrada de tabela embutida | Cria dados embutidos para o fluxo de trabalho. |
| Text Pre-processing | Completo | Executor de pré-processamento de PLN | Normaliza e pré-processa texto. |
| Text Summary | Completo | [Text: NLP AI](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) (tarefa summary) | Resume uma coluna de texto até um número máximo de frases configurado por meio da etapa NLP AI baseada em LLM. |
| Text To Columns | Completo | Transformação de divisão de colunas | Divide texto em campos ou linhas. |
| Tile | Completo | Transformação de blocos / agrupamento | Atribui grupos de blocos por uma regra configurada. |
| Tool Container | Completo | Contêiner da tela / grupo de execução | Preservado como organização do fluxo de trabalho. |
| Topic Modeling | Completo | Executor de modelagem de tópicos | Executa a modelagem de tópicos por meio de PLN gerenciado. |
| Transformation | Completo | Etapa de transformação | Converte a lógica de transformação em expressões ou SQL do PlaidCloud. |
| Transpose | Completo | Transformação de despivotamento | Converte colunas em linhas em um par Nome/Valor. |
| Tree | Completo | Variável de fluxo de trabalho controlada | Converte a seleção em árvore do aplicativo em entrada controlada. |
| Union | Completo | Transformação de união | Combina fluxos por nome, posição ou regras configuradas. |
| Unique | Completo | Transformação de divisão entre únicos / duplicados | Separa os primeiros registros exclusivos dos duplicados. |
| Visual Layout | Completo | Metadados de layout da tela | Preservado como contexto de design. |
| Word Cloud | Completo | Artefato de visualização de texto | Cria um artefato de visualização a partir da análise de texto. |
| XML Parse | Completo | Transformação de análise de XML | Extrai campos XML para os dados do fluxo de trabalho. |
| Zero-shot Text Classification | Completo | [Text: NLP AI](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) (tarefa zeroshot) | Classifica uma coluna de texto em relação a uma lista de rótulos candidatos por linha, com rótulo único ou múltiplo, por meio da etapa NLP AI baseada em LLM. |
| Find Nearest | Completo | etapa [Localizar mais próximo](/pt-br/reference/workflow-steps/spatial/spatial-find-nearest/) | Junção de vizinho mais próximo classificada por distância: em linha reta e por tempo de deslocamento (classificada em minutos em uma malha viária) por meio do mecanismo de roteamento auto-hospedado do PlaidCloud. O tempo de deslocamento é habilitado por espaço de trabalho. |
| Trade Area | Completo | etapa [Spatial Trade Area](/pt-br/reference/workflow-steps/spatial/spatial-trade-area/) | Buffers concêntricos dimensionados em unidades do mundo real: de raio fixo e por tempo de deslocamento (minutos em uma malha viária) por meio do mecanismo de roteamento auto-hospedado. O tempo de deslocamento é habilitado por espaço de trabalho. |
| Image Template | Completo | Operação Image Template do executor | O modo manual recorta a imagem em cada região que você desenha no modelo. O modo automático detecta as regiões da página para você com um modelo de layout de padrão aberto e emite uma linha por região, cada uma com seus limites detectados e a confiança para revisão; uma página que o modelo não consegue ler com confiança é sinalizada pelo nome em vez de recortada. A detecção de padrão aberto pode diferir da do próprio Alteryx; revise as regiões detectadas ou use o modo manual para ter controle exato. |
| Image Recognition | Completo | Executor de reconhecimento de imagem | Treina um classificador de imagens no fluxo de trabalho e pontua novas imagens com ele, no local, sem conta externa e sem que nenhum dado saia do PlaidCloud. O classificador é treinado novamente, e não copiado do Alteryx, portanto os resultados são uma aproximação fiel, e não uma correspondência bit a bit, e o treinamento é executado em CPU. Habilitado por espaço de trabalho. |
| Geocoder | Completo | Geocodificador auto-hospedado | Geocodifica endereços em coordenadas e faz a geocodificação reversa de coordenadas em endereços usando o próprio geocodificador do PlaidCloud, sem conta externa e sem que nenhum dado saia do PlaidCloud. Habilitado por espaço de trabalho. |

Os widgets de interface (listas suspensas, caixas de listagem, caixas de seleção, entradas de
texto/numéricas/de data, seletores de arquivo e de pasta), os objetos da tela (comentários, links,
contêineres) e as portas de macro são todos convertidos em variáveis controladas ou
objetos de tela nativos. O layout completo da interface de um aplicativo Alteryx (a definição `<Questions>`
do arquivo `.yxwz`) também é materializado em um front-end "App
Runner" do Panel publicado, de modo que a conversão do aplicativo produz um formulário de entrada funcional que
coleta os mesmos valores e aciona o fluxo de trabalho convertido, e não apenas as
variáveis controladas individuais. Consulte a linha Analytic App interface acima e
[Usar aplicativos Alteryx convertidos](/pt-br/guides/workflows/use-converted-alteryx-apps/#o-front-end-app-runner).

**Uma observação sobre a saída do Excel.** Uma pasta de trabalho nova e simples, com dados gravados com
formatação padrão, é convertida por completo. Gravar em um *modelo com estilos*, preenchendo planilhas e intervalos
nomeados e preservando a formatação deles, é convertido para uma única
planilha e para várias saídas montadas em planilhas diferentes de uma mesma pasta de trabalho
(a etapa [Export to Excel Sheets](/pt-br/reference/workflow-steps/export/export-to-excel-sheets/)
preenche todas as planilhas em uma única passagem). Os modelos que contêm tabelas dinâmicas ou gráficos
descartam esses objetos quando suas planilhas são gravadas; a manipulação de arquivos em nível de planilha conduzida
pelo Run Command (COM/VBS do Excel) é sinalizada pelo nome para revisão manual, em vez de
convertida automaticamente.

## Cobertura das ferramentas espaciais

Toda ferramenta da paleta **Spatial** do Alteryx tem uma rota no PlaidCloud, e cada
uma dessas rotas é uma etapa que você também pode criar manualmente: a conversão é uma
conveniência, não a única forma de entrada. Consulte [Etapas geoespaciais](/pt-br/reference/workflow-steps/spatial/)
para a referência completa e [Análise geoespacial](/pt-br/guides/workflows/geospatial-analytics/)
para saber como elas se encaixam.

| Ferramenta espacial do Alteryx | Rota no PlaidCloud | Executado em |
| --- | --- | --- |
| Buffer | etapa [Spatial Buffer](/pt-br/reference/workflow-steps/spatial/spatial-buffer/) | Mecanismo de fluxo de trabalho |
| Centroid | Operação Centroid do executor | Mecanismo de fluxo de trabalho |
| Convex Hull | Operação Convex Hull do executor | Mecanismo de fluxo de trabalho |
| Create Points | [Expressão da etapa Table Extract](/pt-br/reference/workflow-steps/spatial/spatial-sql-recipes/) | Banco de dados |
| Distance | [Expressão da etapa Table Extract](/pt-br/reference/workflow-steps/spatial/spatial-sql-recipes/) | Banco de dados |
| Find Nearest | etapa [Localizar mais próximo](/pt-br/reference/workflow-steps/spatial/spatial-find-nearest/) | Banco de dados; serviço de roteamento para tempo de deslocamento |
| Generalize | etapa [Spatial Generalize](/pt-br/reference/workflow-steps/spatial/spatial-generalize/) | Mecanismo de fluxo de trabalho |
| Heat Map | [Heat Map (macro)](/pt-br/reference/workflow-steps/macros/macro-heat-map/) | Mecanismo de fluxo de trabalho |
| Line To Polygon | Operação Line To Polygon do executor | Mecanismo de fluxo de trabalho |
| Make Grid | etapa [Criar grade](/pt-br/reference/workflow-steps/spatial/spatial-make-grid/) | Mecanismo de fluxo de trabalho |
| Point To Line | Operação Point To Line do executor | Mecanismo de fluxo de trabalho |
| Poly-Build | etapa [Spatial Poly-Build](/pt-br/reference/workflow-steps/spatial/spatial-poly-build/) | Mecanismo de fluxo de trabalho |
| Poly-Split | etapa [Spatial Poly-Split](/pt-br/reference/workflow-steps/spatial/spatial-poly-split/) | Mecanismo de fluxo de trabalho |
| Redistribute | Operação Redistribute do executor | Mecanismo de fluxo de trabalho |
| Smooth | etapa [Spatial Smooth](/pt-br/reference/workflow-steps/spatial/spatial-smooth/) | Mecanismo de fluxo de trabalho |
| Spatial Info | etapa [Spatial Info](/pt-br/reference/workflow-steps/spatial/spatial-info/) | Mecanismo de fluxo de trabalho |
| Spatial Match | [Correspondência espacial](/pt-br/reference/workflow-steps/spatial/spatial-match/) | Banco de dados |
| Spatial Match: objeto de interseção, Unmatched | etapa [Spatial Match (Intersect / Unmatched)](/pt-br/reference/workflow-steps/spatial/spatial-match-executor/) | Mecanismo de fluxo de trabalho |
| Spatial Process | [Processo espacial](/pt-br/reference/workflow-steps/spatial/spatial-process/) | Mecanismo de fluxo de trabalho |
| Trade Area (raio fixo + tempo de deslocamento) | etapa [Spatial Trade Area](/pt-br/reference/workflow-steps/spatial/spatial-trade-area/) | Mecanismo de fluxo de trabalho; serviço de roteamento para tempo de deslocamento |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/pt-br/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | Mecanismo de fluxo de trabalho |
| Entrada de arquivo espacial | [Importar arquivo espacial](/pt-br/reference/workflow-steps/spatial/spatial-file-import/) | Mecanismo de fluxo de trabalho |
| Summarize: SpatialObjCombine, SpatialObjConvexHull | [Combinação espacial](/pt-br/reference/workflow-steps/spatial/spatial-combine/) | Mecanismo de fluxo de trabalho |
| Report Map | etapa [Report Map](/pt-br/reference/workflow-steps/reports/report-map/) | Mecanismo de fluxo de trabalho |

**Áreas de influência e mais próximo por tempo de deslocamento**: os anéis de tempo de deslocamento da Trade Area e a classificação por tempo de deslocamento da Find
Nearest são executados no mecanismo de roteamento auto-hospedado do PlaidCloud
(isócronas da malha viária e matrizes de tempo de deslocamento), e não em uma API
hospedada de terceiros, portanto as coordenadas de origem nunca saem da plataforma. O tempo de deslocamento é habilitado por
espaço de trabalho. O roteamento e as áreas de tempo de deslocamento usam dados do OpenStreetMap:
© colaboradores do OpenStreetMap, disponíveis sob a [Open Database License
(ODbL)](https://www.openstreetmap.org/copyright).

### Pré-requisitos espaciais conhecidos

As próprias ferramentas espaciais são convertidas; estes são pré-requisitos da entrada.

- **O formato de GeoFile `.geo`.** O GeoFile binário proprietário do Alteryx não tem
  leitor aberto, portanto a importação de um falha de forma fechada em vez de travar
  em tempo de execução. No Alteryx, exporte a camada novamente para um formato espacial padrão
  (shapefile ou GeoJSON) e importe esse arquivo; os demais formatos espaciais
  não são afetados. Consulte
  [Migrar fluxos de trabalho espaciais do Alteryx](/pt-br/guides/workflows/migrate-spatial-alteryx-workflows/#empacotar-as-entradas-espaciais).
- **A medida Peano key do Spatial Info.** A Peano key é um índice espacial proprietário do Alteryx
  sem especificação pública, portanto um Spatial Info que a solicita
  ignora essa coluna e a cita em uma observação. Todas as outras medidas do Spatial Info
  (área, comprimento, centroide, retângulo delimitador, tipo de objeto, contagens de partes e de pontos
  e pontos finais) são convertidas.
- **Coordenadas projetadas do Create Points.** O Create Points converte diretamente coordenadas
  de lon/lat em ponto flutuante e em inteiro (×1.000.000). As coordenadas que já estão em um sistema projetado precisam ser reprojetadas para lon/lat WGS84
  antes, porque o fluxo de trabalho não registra qual projeção elas usam.

## Cobertura das ferramentas Calgary

Um banco de dados Calgary do Alteryx (`.cydb`) é um repositório indexado proprietário que o PlaidCloud não consegue abrir. A conversão trata cada um deles como representante de uma tabela comum do PlaidCloud, chamada `calgary_<database name>`, de modo que as ferramentas construídas em torno dele são convertidas em operações de tabela comuns, em vez de serem recusadas de imediato. Consulte [Bancos de dados Calgary](/pt-br/guides/workflows/migrate-alteryx-workflows/#bancos-de-dados-calgary) para saber como funciona a tabela substituta e [Calgary Join e Cross Count Append](/pt-br/guides/workflows/migrate-alteryx-workflows/#calgary-join-e-cross-count-append) para as ferramentas de correspondência de índice.

| Ferramenta Calgary do Alteryx | Rota no PlaidCloud | Converte |
| --- | --- | --- |
| Calgary Loader | Table Extract gravando `calgary_<database>` | Sim, quando o banco de dados tem nome e armazena pelo menos um campo de dados. |
| Calgary Input | Entrada Document dinâmica lendo `calgary_<database>`, com a consulta salva como filtro | Sim, inclusive uma consulta construída com um Or ou envolvida em um Not, e um filtro contains ou starts-with (reconstruído como um SQL LIKE). Recusa uma consulta de busca espacial e os limites Skip Records/Max Records. |
| Calgary Input (Count Only) / Calgary Cross Count | Transformação de agregação sobre `calgary_<database>` | Sim, inclusive um bucket construído com um Or ou envolvido em um Not. Recusa um cruzamento sobre mais de um campo personalizado e uma leitura somente de contagem que não cita nenhuma coluna para contar. |
| Calgary Join | Entrada Document dinâmica que compara cada registro de sua entrada com `calgary_<database>` | Quando o campo de entrada é um valor simples comparado com um índice de valores, inclusive o modo Count Only, que conta os registros do banco de dados que cada registro de entrada correspondeu, com um registro sem correspondência contando zero. Recusa quando o campo é espacial (reconstrua como Spatial Match) ou seu tipo não é resolvido, e em Joins de índice de intervalo ou com saída sem correspondência conectada, em um Join que não cita nenhum campo de correspondência e em um Join sem nada conectado à sua entrada. |
| Calgary Cross Count Append | Entrada Document dinâmica que compara cada registro, depois uma junção contada sobre `calgary_<database>` | Quando o campo de entrada é um valor simples comparado com um índice de valores: conta, por registro de entrada, os registros do banco de dados correspondidos, e um registro sem correspondência conta zero. Recusa um índice espacial ou não resolvido (reconstrua como Spatial Match), uma grade de contagem cruzada de valores personalizados, um índice de intervalo e uma correspondência que não cita nenhum campo. |

### Pré-requisitos conhecidos do Calgary

A maioria destes é pré-requisito da entrada, e não limite da conversão.

- **Uma correspondência de índice espacial precisa ser reconstruída como Spatial Match.** Um Calgary Join ou Cross Count Append comparado com um índice espacial é recusado, citando a tabela substituta: o fluxo de trabalho registra o nome do índice, mas não se ele contém valores comuns ou geometria espacial, e uma correspondência de valores (uma junção de igualdade) e uma correspondência espacial (ponto em polígono) são operações diferentes. Exporte o banco de dados para uma tabela e reconstrua a correspondência como um Join (índice de valores) ou um Spatial Match (índice espacial).
- **Uma leitura limitada por Skip Records ou Max Records precisa de uma ordem explícita.** A tabela substituta exportada não carrega ordem de registros, portanto adicione uma coluna de ordem ao exportar se precisar pegar os primeiros ou os últimos N registros por posição.
- **Um banco de dados demográfico ou de referência precisa ser carregado primeiro.** Uma leitura do Calgary antes de seu banco de dados ter sido carregado é interrompida, citando a tabela a ser criada. O próprio arquivo `.cydb` não tem leitor aberto, portanto exporte-o novamente no Alteryx (um Calgary Input em uma ferramenta Output Data gravando CSV ou Parquet) e importe-o como a tabela indicada; consulte [Bancos de dados .cydb (Calgary) ilegíveis](/pt-br/guides/workflows/troubleshoot-alteryx-imports/#bancos-de-dados-cydb-calgary-ilegíveis). Este é o caso comum dos arquivos `.cydb` demográficos e de referência licenciados que o Alteryx distribui (Experian, Census e similares): nenhum conversor consegue reproduzir esses dados de terceiros, portanto traga seus próprios dados de referência licenciados e carregue-os na tabela indicada, assim como os dados de referência do Geocoder.
- **Um Calgary Loader que não armazena nenhum campo de dados não é convertido**, pois a tabela que ele gravaria não teria colunas.
- **Uma grade de contagem cruzada de valores personalizados ainda não é convertida.** Um único campo de contagem cruzada simples é convertido (ele conta, por registro de entrada, os registros correspondentes do banco de dados), mas uma grade de valores personalizados *nomeados* acrescentaria uma coluna de contagem por valor, e o Alteryx não documenta quantas colunas são nem como as nomeia. Planejado para uma versão futura, aguardando uma exportação de referência para fazer engenharia reversa do contrato de colunas.

As consultas de valor, intervalo, contains e starts-with são todas convertidas em um filtro; somente uma consulta de busca espacial, uma operação de índice sem equivalente em nível de coluna, não é.

## Conexão com sistemas externos

Os endpoints de conectores do Alteryx (Salesforce, HTTP, Google Analytics, Cassandra,
e-mail, Hadoop e Spark, em ambas as direções) não são convertidos, porque
o PlaidCloud acessa esses sistemas por meio de uma conexão, e não de uma
ferramenta na tela. Cada um é recusado pelo nome e informa para onde o trabalho
deve ir:

| Ferramenta do Alteryx | Para onde vai no PlaidCloud |
| --- | --- |
| Salesforce Input / Output | Uma conexão **Salesforce** |
| Anaplan | Uma conexão **Anaplan** |
| HTTP Input | Uma etapa **Solicitação REST** em uma conexão **REST** |
| Google Analytics Input | **Importar: Origem Singer** com o tap do Google Analytics |
| Cassandra Input | **Importar: Origem Singer** com o tap do Cassandra |
| Email Input | **Importar: Origem Singer** com o tap do GMail |
| Hadoop Input / Output | **Importar: SQL** / **Exportar: SQL** por meio de uma conexão Hive, Impala ou Presto |
| Spark Input / Output | **Importar: SQL** / **Exportar: SQL** por meio de uma conexão Databricks |

Quatro destes não têm nenhum caminho de gravação. O PlaidCloud lê o Google Analytics
e o Cassandra, mas nunca grava neles, portanto uma ferramenta Google Analytics Output ou
Cassandra Output se torna uma etapa **Exportar: SQL** para um destino compatível.
O e-mail também não é um destino de dados: **Notificar: E-mail** envia uma
notificação a pessoas, portanto uma ferramenta Email Output se torna uma etapa de exportação mais uma
notificação separada. A conexão **Anaplan** é somente leitura do mesmo
modo: ela lê uma visão salva, executa uma ação de exportação preexistente ou carrega
listas em uma dimensão do PlaidCloud, mas não existe nenhuma etapa do PlaidCloud que
grave de volta no Anaplan.

## Validação de um fluxo de trabalho convertido

Para fluxos de trabalho de produção, valide as saídas convertidas em relação a saídas confiáveis do Alteryx.
A validação do PlaidCloud se concentra no esquema, na contagem de linhas e nos valores das linhas,
e ignora a ordem das linhas, a menos que o fluxo de trabalho dependa dela. As operações especializadas
(espacial, correspondência aproximada, OCR, PLN, relatórios) são executadas por executores de
trabalho gerenciados que mantêm o fluxo de trabalho nativo da nuvem; os pipelines de aprendizado de máquina
são convertidos nas etapas nativas [ML: Treinar modelo](/pt-br/reference/workflow-steps/machine-learning/ml-train/)
e [ML: Pontuar](/pt-br/reference/workflow-steps/machine-learning/ml-score/).
Consulte [Migrar fluxos de trabalho do Alteryx](/pt-br/guides/workflows/migrate-alteryx-workflows/)
para o guia completo de importação e validação.
