---
title: Migrar análises Savant
description: Converta uma exportação de análise do Savant Labs num fluxo de trabalho avançado do PlaidCloud a partir da aplicação Analyze, da API REST ou de um agente de IA ligado por MCP, associe as respetivas origens e leia o relatório de conversão.
sidebar:
  order: 31
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-savant-analyses.md
---

O PlaidCloud é um substituto direto do Savant. Todos os agentes, expressões e definições do Savant são convertidos para o PlaidCloud e executados. O conversor transforma uma exportação de análise do Savant Labs num fluxo de trabalho avançado executável: mapeia cada agente do Savant para um passo de fluxo de trabalho, uma variável de projeto ou um objeto da área de desenho, mantém o grafo original e devolve um relatório de conversão que indica tudo o que não conseguiu converter.

A conversão lê o ficheiro de exportação que indicar e os cabeçalhos dos ficheiros que associar às respetivas origens. Nunca contacta o sistema a que uma origem ou um destino do Savant se liga.

## O que o PlaidCloud cria

- Cada agente do Savant torna-se o passo de fluxo de trabalho correspondente, com as relações a montante e a jusante preservadas. A [matriz de conversão do Savant](/pt-pt/reference/savant-conversion-matrix/) lista todos os agentes e o respetivo escalão de mapeamento.
- Os parâmetros de análise do Savant tornam-se variáveis de projeto, e as referências a eles nas definições dos agentes são reescritas para a sintaxe de variáveis do PlaidCloud.
- As notas e os grupos chegam à área de desenho como notas e grupos.
- Cada origem torna-se um passo de importação, ou lê uma tabela existente, consoante a forma como a associar.
- Todos os tipos de agente do Savant são totalmente convertidos: cada opção tem um mapeamento. Uma configuração em que o próprio Savant falha, ou que não documenta, chega como um passo de marcador de posição com nome. Consulte [Marcadores de posição para configurações não convertidas](#marcadores-de-posição-para-configurações-não-convertidas).

## Antes de começar

1. Exporte a análise do Savant com **Exportar JSON**.
2. Carregue o ficheiro `.json` para uma [conta de documentos](/pt-pt/guides/documents/adding-accounts/) que possa ler.
3. Escolha o projeto do PlaidCloud que deve receber o fluxo de trabalho. Precisa de acesso de escrita ao mesmo.
4. Escolha uma conta de documentos e uma pasta de base de onde serão lidos os ficheiros de origem da análise.

## Converter uma análise

Converta a partir da aplicação Analyze, da API REST ou do catálogo de ferramentas MCP. Os três aceitam os mesmos campos.

### Aplicação Analyze

1. Abra **Analisar** e escolha **Tools → Importar análise Savant**.
2. Escolha o **Projeto de destino** e o **Ficheiro de exportação do Savant (.json)** que carregou para uma conta de documentos.
3. Selecione **Carregar origens**. A janela lista cada nó de origem da exportação.
4. Para ligar uma origem a dados que já tenha, selecione-a e escolha **Associar…**. Escolha **Tabela do projeto** para ler uma tabela do projeto de destino, ou **Documento** para ler um ficheiro de uma conta de documentos (com um nome de folha de cálculo opcional para Excel). Escolha **Desassociar** para remover uma associação.
5. Em **Diretório de origens não associadas**, escolha a conta de documentos e a pasta de base de onde são lidos os ficheiros das origens não associadas.
6. Em **Opções de conversão**, escolha o **Tipo de fluxo de trabalho** e se pretende **Permitir marcadores de posição não convertidos**. Em **Prefixos de objetos**, defina opcionalmente prefixos para fluxos de trabalho, passos e tabelas.
7. Selecione **Converter**.

Quando a conversão termina, a janela apresenta o relatório de conversão: o nome do fluxo de trabalho e o prefixo das tabelas, os avisos, uma tabela com os caminhos de documentos para onde carregar ficheiros das origens não associadas e os passos que precisam de revisão. Se não for possível carregar a lista de origens, adicione uma linha por cada origem com o respetivo ID de nó e o ID `analyzetable_` da tabela a associar.

### Campos

A API REST e a ferramenta MCP aceitam estes campos.

| Campo | Obrigatório | O que faz |
| --- | --- | --- |
| `source_account_id` | Sim | Conta de documentos que contém a exportação do Savant. |
| `source_file_path` | Sim | Caminho da exportação dentro dessa conta. |
| `project_id` | Sim | Projeto onde o fluxo de trabalho é criado. |
| `document_account_id` | Sim | Conta de documentos de onde as origens não associadas são lidas. |
| `document_account_path` | Sim | Pasta de base nessa conta para as origens não associadas. Um valor vazio ou `/` corresponde à raiz da conta, e uma `/` inicial é ignorada. São recusados os caminhos com `..` ou segmentos iniciados por ponto, chavetas, letra de unidade ou esquema de URL, ou caracteres de controlo. |
| `workflow_prefix` | Não | Prefixo acrescentado aos nomes dos fluxos de trabalho. |
| `step_prefix` | Não | Prefixo acrescentado aos nomes dos passos. |
| `table_prefix` | Não | Prefixo acrescentado aos nomes das tabelas. Por predefinição, é o nome do próprio fluxo de trabalho. Um prefixo que reutilizasse o nome de uma tabela existente é recusado antes de ser criado o que quer que seja. O prefixo utilizado é devolvido no relatório de conversão. |
| `workflow_type` | Não | `advanced` (predefinido) dispõe o grafo na área de desenho DAG. `standard` produz uma lista de passos em série. |
| `source_bindings` | Não | Associa origens a dados existentes. Consulte [Associar origens](#associar-origens). |
| `destination_bindings` | Não | Encaminha os destinos para uma conta de documentos, uma tabela de ligação, uma Google Sheet, uma origem de dados Tableau, um canal do Slack ou destinatários de e-mail. Apenas REST e MCP. Consulte [Destinos](#destinos). |
| `api_bindings` | Não | Indica para onde vai o URL relativo de um agente de API: um URL de base ou uma ligação REST. Apenas REST e MCP. Consulte [Associar pedidos de API](#associar-pedidos-de-api). |
| `allow_unconverted_placeholders` | Não | Controla o que faz um marcador de posição em tempo de execução. Consulte [Marcadores de posição para configurações não convertidas](#marcadores-de-posição-para-configurações-não-convertidas). |

### REST

Envie os campos como corpo JSON para:

```text
POST /rest/v1/analyze/savant/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/savant/quarterly-margin.json",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/savant-inputs"
}
```

Para listar os nós de origem de uma exportação antes de construir `source_bindings`, envie `source_account_id` e `source_file_path` para:

```text
POST /rest/v1/analyze/savant/sources
```

Cada entrada da resposta tem o `node_id`, o `name` e o `connector` da origem.

### MCP

Um agente de IA ligado por MCP chama a ferramenta `savant_convert` com os mesmos campos. Consulte [Agentes de IA (MCP)](/pt-pt/integrations/ai-coding-agents/) para ligar um agente. A ferramenta altera o seu projeto, pelo que deve rever a chamada antes de a aprovar.

## Associações no momento da conversão

Uma exportação do Savant não contém dados, credenciais nem ligações, pelo que três parâmetros do momento da conversão a ligam aos seus. Cada um é um mapa de um ID ou nome de nó do Savant para um destino, e uma associação que não possa utilizar faz com que toda a conversão seja recusada antes de ser criado o que quer que seja.

| Parâmetro | Associa | Secção |
| --- | --- | --- |
| `source_bindings` | Agentes de origem a tabelas ou ficheiros | [Associar origens](#associar-origens) |
| `destination_bindings` | Agentes de destino a um ficheiro, uma tabela, uma folha, uma origem de dados Tableau, um canal do Slack ou um e-mail | [Destinos](#destinos) |
| `api_bindings` | Agentes de API com URL relativo a um URL de base ou a uma ligação REST | [Associar pedidos de API](#associar-pedidos-de-api) |

## Associar origens

Uma exportação do Savant descreve de onde provêm os seus dados, mas não contém dados nem credenciais. Utilize `source_bindings` para ligar cada origem a dados que já tenha no PlaidCloud. A chave é o ID de nó, o ID do conjunto de dados ou o nome da origem. O valor é um dos seguintes:

- Um ID `analyzetable_` de uma tabela do projeto de destino. O fluxo de trabalho convertido lê essa tabela diretamente.
- Um objeto com `account`, `path` e, opcionalmente, `sheet`, para ler um ficheiro de uma conta de documentos.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "Budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Uma associação que não possa ler é recusada. Uma chave que não corresponda a nenhuma origem é comunicada como aviso.

O caminho de um ficheiro de origem na exportação pode começar por `/` ou passar por pastas com ponto, como `.archive`, e é convertido. Uma origem que lê XML converte o texto XML, e uma origem de documento XML transporta também as colunas de contexto de ficheiro do Savant.

### Origens não associadas

Uma origem sem associação torna-se um passo de importação ainda sem dados, e o relatório de conversão inclui um aviso sobre ela. O passo lê a partir de:

```text
<document_account_path>/savant/<workflow id>/<source name>.csv
```

Carregue o ficheiro para esse caminho e execute o fluxo de trabalho. Enquanto o ficheiro não estiver lá, o passo de importação termina com um aviso e cria uma tabela vazia, e o fluxo de trabalho continua.

## Como são convertidos os agentes

A maioria dos agentes é convertida no passo que construiria manualmente; a [matriz de conversão do Savant](/pt-pt/reference/savant-conversion-matrix/) lista todos os agentes. Estes agentes exigem cuidados adicionais.

| Agente do Savant | O que se torna | Ressalvas |
| --- | --- | --- |
| Infer Agent (`gen_ai`, e `service` legado com um serviço LLM) | Um passo [AI/NLP](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) com a tarefa **Pedido**. O pedido é executado uma vez por linha sobre os campos de entrada, e a resposta fica numa coluna **AI Answer** ao lado de todas as colunas de entrada. Um limite de linhas torna-se **Máximo de linhas**, e uma origem vazia gera um aviso e escreve uma tabela vazia. **Max New Rows** responde apenas às linhas novas e mantém as respostas de execuções anteriores. | Responde um LLM, pelo que a saída nunca é idêntica byte a byte à do Savant e pode variar entre execuções. Cada chamada tem um custo. Consulte [Fornecedores de IA](#fornecedores-de-ia). Um lote que falha mantém as suas linhas com uma resposta vazia e gera um aviso. |
| Vision Agent (`vision`) | Um passo [Document Read Blob](/pt-pt/reference/workflow-steps/text-documents/document-blob-extract/), [Image OCR](/pt-pt/reference/workflow-steps/text-documents/image-ocr/) e, depois, a tarefa **Pedido** do AI/NLP. Cada documento é enviado ao fornecedor como imagem ou PDF quando o fornecedor aceita esse tipo e tamanho. Caso contrário, o passo envia a camada de texto do PDF ou o texto de OCR. | As mesmas ressalvas de LLM do Infer Agent. Os documentos completos saem do PlaidCloud para o fornecedor, e a conversão gera um aviso. Os ficheiros TIFF e BMP são enviados como texto de OCR, e não existe definição de tamanho máximo de documento. Um documento que não é encontrado é ignorado e o passo avisa com o respetivo caminho. |
| API Agent (`apiService`, e `service` legado com um serviço de API) | Um passo [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) que envia um pedido por linha de entrada, seguido de uma junção que mantém todas as linhas de entrada. O corpo bruto da resposta fica numa coluna de texto, com uma coluna de estado ao lado. Uma quota por período torna-se um **Máx. pedidos/seg.** fracionário. Um URL relativo junta-se ao URL de base ou à ligação REST que associar com `api_bindings`. Um anfitrião, uma porta ou um caminho que provém de um campo da linha é preenchido linha a linha. A paginação por URL seguinte, cabeçalho Link, desfasamento e página é seguida, e um valor de paginação (início, tamanho da página ou nome do parâmetro) pode provir de um campo de entrada ou de um parâmetro. | Um método diferente de GET é executado contra o sistema real uma vez por cada linha de entrada de cada vez que o fluxo de trabalho é executado, pelo que deve confirmar o destino antes da primeira execução. Os pedidos que não são GET não são repetidos automaticamente. Um pedido falhado permanece como uma linha com o seu estado. Um pedido que transporta uma credencial não pode obter o anfitrião a partir de um campo da linha. As credenciais são tratadas conforme descrito em [Passos de API com credenciais](#passos-de-api-com-credenciais). |
| Recursion Agent (`hierarchy`) | Um passo [Hierarchy Closure](/pt-pt/reference/workflow-steps/tables/table-hierarchy-closure/) que percorre cada linha ao longo da cadeia de pais até qualquer profundidade e depois agrega cada nó sobre os IDs do seu caminho até à raiz, ele próprio incluído. Escreve Depth e Path. Uma linha com pai em branco, ou que se indica a si própria como pai, é uma raiz. | Um ciclo nos IDs de pai termina no nó repetido e mantém todos os antecessores anteriores a ele. As linhas com vários pais mantêm cada uma os seus valores. |
| Search and Replace (`search_replace`) | Um passo [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/) que aplica cada regra por ordem às colunas de texto escolhidas, com ou sem distinção entre maiúsculas e minúsculas, palavra inteira ou não. Cada regra é executada no seu modo: substituir o texto correspondente, substituir a célula inteira quando contém o texto, substituir a célula inteira quando corresponde exatamente, ou acrescentar à célula. | As regras são texto literal, não padrões. |
| Split (`split`) | Um passo [Split Text](/pt-pt/reference/workflow-steps/tables/table-split-text/). Divide em colunas ou linhas por um separador literal de qualquer comprimento e decide o número de colunas a partir dos dados quando o fluxo de trabalho é executado. | Nenhuma. |
| Time Series (`rollup`) | Um passo Table Extract que agrupa por uma expressão de período, com um passo [Period Spine](/pt-pt/reference/workflow-steps/tables/table-period-spine/), uma anti-junção e uma união que preenchem com zeros os períodos sem registos. | Os registos com data NULL são excluídos. A espinha termina nos 100 000 períodos. |
| Format (`format`) | Um passo Table Extract com as mudanças de nome, as mudanças de tipo, as ocultações e os preenchimentos, ou um passo [Promote Header](/pt-pt/reference/workflow-steps/tables/table-promote-header/) para substituir nomes pela linha. | Um preenchimento numa coluna que não é de texto converte o valor predefinido para o tipo da coluna. Promover um cabeçalho sobre uma origem que não declara colunas lê todas as colunas, a partir de ficheiros CSV, Excel, XLS, JSON, Parquet e Avro. Consulte [Ficheiros sem colunas declaradas](#ficheiros-sem-colunas-declaradas). |
| Spatial Match Agent (`spatial_match`) | Um passo [Correspondência espacial (executor)](/pt-pt/reference/workflow-steps/spatial/spatial-match-executor/) para intersects, within, contains, touches, crosses, overlaps, equals e disjoint, com várias regras combinadas; Junção cruzada para uma correspondência cruzada; [Localizar o mais próximo](/pt-pt/reference/workflow-steps/spatial/spatial-find-nearest/) para uma correspondência mais próxima. | Uma correspondência mais próxima ordena e filtra por distância ortodrómica, como o Savant. Uma regra de mais próximo combinada com outras regras encontra primeiro os registos mais próximos e depois aplica as outras regras: com AND, o resultado mantém os registos que satisfazem todas as regras e, com OR, une os registos mais próximos com os registos que as outras regras encontram. Uma regra de mais próximo sem contagem nem distância máxima mantém o único registo mais próximo. Uma correspondência por distância também é convertida, em quilómetros quando a regra não indica unidade, e mede a distância geodésica entre quaisquer geometrias, não apenas pontos. Uma geometria que não pode ser analisada dá NULL ou nenhuma correspondência, com um aviso. |
| Spatial Summarize Agent (`spatial_summarize`) | [Combinação espacial](/pt-pt/reference/workflow-steps/spatial/spatial-combine/) para união, interseção e caixa delimitadora, além de [Spatial Centroid](/pt-pt/reference/workflow-steps/spatial/spatial-centroid/), [Spatial Point to Line](/pt-pt/reference/workflow-steps/spatial/spatial-point-to-line/) e [Spatial Line to Polygon](/pt-pt/reference/workflow-steps/spatial/spatial-line-to-polygon/) (passos) para o centro geométrico e para a construção de linhas ou polígonos. | Um polígono construído com menos de 3 pontos é um polígono vazio. |
| Destination Agent (`destination`) | Um passo de exportação para o destino que associar, ou uma tabela de projeto ou um ficheiro quando não o associar. Consulte [Destinos](#destinos). | Consulte [O que continua limitado](#what-stays-limited). |

`GEO_POINT`, `GEO_TYPE` e `GEO_SPATIAL_DISTANCE` são convertidos em expressões. Uma edição cuja expressão completa seja outra função `GEO_*`, como `GEO_AREA` ou `GEO_UNION`, é convertida no passo espacial correspondente, incluindo [Spatial Info](/pt-pt/reference/workflow-steps/spatial/spatial-info/) (passo). A geometria circula como texto WKT. `GEO_AREA`, `GEO_PERIMETER` e `GEO_SPATIAL_DISTANCE` em milhas usam a milha terrestre.

Uma origem que lê ficheiros binários, como os documentos que um agente Vision lê, é convertida numa extração de documento do documento associado, ou do ficheiro esperado no caminho das origens não associadas.

## Fornecedores de IA

Um agente Infer ou Vision é convertido num passo AI/NLP que utiliza uma ligação LLM. O conversor suporta Anthropic, OpenAI, Gemini, Azure OpenAI, Grok e GitHub Models.

- O conversor escolhe a ligação para o fornecedor e o modelo que o agente indica, de entre as ligações LLM que o utilizador que importa consegue ver. Nunca indica uma que o utilizador não consiga ver. Através de um assistente de IA (MCP), isso significa as ligações que o utilizador do assistente consegue ver.
- Quando o fornecedor não tem nenhuma ligação visível, ou o fornecedor do Savant não tem correspondência no PlaidCloud (uma API de modelos alojada na nuvem ou um fornecedor com chave própria da área de trabalho do Savant), o passo usa a ligação predefinida da área de trabalho, se o utilizador a conseguir ver. Caso contrário, deixa a ligação em branco, e o passo usa a predefinida da área de trabalho quando é executado. O relatório de conversão avisa em ambos os casos, pelo que deve escolher uma ligação no passo se outra diferente deve responder.

## Destinos

Um destino do Savant escreve a tabela que recebe no destino que associar. Associe os destinos com `destination_bindings` no corpo REST ou na chamada MCP. A chave é o ID de nó ou o nome do destino. A janela do Analyze não associa destinos, pelo que um destino convertido aí escreve o resultado não associado descrito em [Destinos não associados](#destinos-não-associados).

| Destino | Associação | Resultado |
| --- | --- | --- |
| Conta de documentos | `{account, path[, file_name]}` | Um ficheiro CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF ou Tableau Hyper, consoante o tipo de destino. Precisa da permissão de escrita no armazenamento de documentos na conta. |
| Tabela numa ligação | `{connection, table[, schema, replace]}` | Um passo [Export: External Database Tables](/pt-pt/reference/workflow-steps/export/export-external-tables/). Precisa da permissão de escrita na ligação. Substituir a tabela exige `replace: true`. |
| Google Sheets | `{connection, spreadsheet_name[, sheet_name, replace]}`, ou `{connection, spreadsheet_id[, sheet_name, replace]}` | Um passo [Export to Google Spreadsheet](/pt-pt/reference/workflow-steps/export/export-to-google-spreadsheet/) numa ligação Google Sheets. O separador é, por predefinição, o que o destino indica, ou então `Sheet1`. Um destino que substitui as linhas da folha limpa o separador, pelo que exige `replace: true`. |
| Tableau | `{account, connection[, path, file_name, replace, datasource_name, tableau_project]}` | Uma extração Tableau Hyper escrita na pasta da conta, seguida de um passo [Publish to Tableau](/pt-pt/reference/workflow-steps/export/export-to-tableau/) numa [ligação Tableau](/pt-pt/reference/connectors/collaboration/tableau/). Substituir a origem de dados, ou alterar as suas linhas por chaves de correspondência, exige `replace: true`. |
| Slack | `{connection[, channel]}` | O CSV é escrito numa conta de documentos e depois um passo [Notify via Slack](/pt-pt/reference/workflow-steps/notifications/notify-via-slack/) carrega-o para o canal. A ligação precisa de um token de bot, e o canal tem de ser um ID de canal, obtido da associação ou, caso contrário, da exportação. |
| E-mail | `{email_to: [...]}`, e `email_export_recipients: true` para usar também os destinatários que a exportação lista | O CSV é enviado por e-mail como anexo. Precisa da permissão de escrita de e-mail. |

Uma ligação Sheets, Tableau ou Slack é verificada da mesma forma que uma ligação de tabela: tem de a conseguir ver e deter a permissão de escrita na ligação, caso contrário a conversão é recusada.

### Modos de escrita

- Um destino de ficheiro ou tabela que acrescenta lê de volta o ficheiro anterior e reescreve-o com as novas linhas. Nunca substitui.
- Um destino upsert, update ou groupReplace faz merge pelas chaves de correspondência do destino. Um ficheiro ou uma tabela é lido de volta e reescrito, e uma origem de dados Tableau tem as linhas correspondentes alteradas no local.
- Acrescentar e fazer merge funcionam também em ficheiros existentes divididos por valor, sem cabeçalho (as linhas correspondem por posição), em ficheiros Excel ancorados numa célula superior esquerda e em ficheiros com um conjunto de carateres diferente de UTF-8. Uma divisão lê de volta o ficheiro para onde cada valor é escrito e faz o merge dentro dele, deixando os outros ficheiros como estão.
- Um destino Tableau mapeia os modos do Savant para os seis [modos](/pt-pt/reference/workflow-steps/export/export-to-tableau/#modos) do Publish to Tableau: append e insert acrescentam linhas, replace substitui, e upsert, update e groupReplace fazem a correspondência por chaves. Um modo que altera dados existentes só publica quando a associação indica `replace: true`; caso contrário, o destino publica uma nova origem de dados e o relatório assinala-o.
- Um destino com codificação de saída escreve o ficheiro nesse conjunto de carateres Java. Um carácter que o conjunto não tem é escrito como `?`, como faz o Savant. São aceites os alias Java, o CESU-8 e as formas com marca de ordem de bytes. Alguns conjuntos de carateres raros (por exemplo, `x-ISCII91` ou `JIS_X0212`) não podem ser escritos; o ficheiro é escrito em UTF-8 e o relatório avisa. Uma divisão num conjunto de carateres diferente de UTF-8 converte a pasta.
- Os nomes dos ficheiros exportados têm de permanecer dentro da pasta associada.

### O que os chamadores de IA podem associar

Uma conversão através de um assistente de IA (MCP) associa as mesmas formas com estas partes retidas, cada uma com um aviso que a indica:

| Retido | O que acontece em vez disso |
| --- | --- |
| `replace` numa tabela, folha ou origem de dados Tableau | Um destino que acrescenta continua a acrescentar à tabela ou folha associada. Um destino que substitui escreve um CSV. Um destino Tableau publica uma nova origem de dados. |
| Destinatários de e-mail | É escrito um CSV em vez do e-mail. |
| Slack | É escrito um CSV em vez da publicação no Slack. |

Converta a partir da aplicação Analyze ou da API REST, ou inicie sessão pessoalmente em vez de usar um assistente, para associar estes elementos.

### Destinos não associados

Um destino sem associação escreve a sua contrapartida no PlaidCloud e avisa **Destination target unbound**, indicando o destino original. A conversão nunca contacta o sistema de destino.

| Destino | Resultado |
| --- | --- |
| Destino de base de dados, armazém de dados ou SaaS (Oracle, base de dados genérica, Looker Studio, NetSuite, SAP e Google Sheets, Tableau ou Slack sem ligação associada) | Uma tabela no projeto, com o nome do nó de destino. |
| Armazenamento de ficheiros (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | O ficheiro, no tipo de ficheiro do destino, numa pasta de documentos na conta que indicou para as origens não associadas. A pasta reflete a pasta de destino. As credenciais e os tokens de partilha são removidos do caminho. |
| E-mail | Um CSV, na conta de documentos que indicou para as origens não associadas. |

O aviso indica o que associar para chegar ao destino real. Um destino cuja associação não pode ser utilizada escreve um CSV e avisa **Fallback, target not written**, com o destino original na mensagem; verifique esse CSV antes de confiar nele. Um destino CSV simples escreve o seu próprio ficheiro.

### Destinos divididos

Um destino que escreve um ficheiro, uma subpasta ou um separador por valor de um campo divide ficheiros CSV, Excel, Parquet e PDF e separadores do Google Sheets.

- **Parquet e PDF.** Um ficheiro por valor.
- **Google Sheets.** Um separador por valor.
- **Modelo.** Um livro modelo serve de base ao livro de cada valor. Um modelo em falta gera um aviso e o livro é escrito sem ele.
- **Valores nulos.** Um valor de divisão NULL é escrito no seu próprio ficheiro ou separador, não é descartado.
- **Um campo que a entrada não tem.** Uma divisão, ou uma ordenação, por um campo que a entrada não contém é recusada pelo nome, porque o Savant falha nesse caso.
- **Um `/` ou `\` num valor.** Um valor de divisão que contém uma barra ou uma barra invertida não pode ser nome de ficheiro nem de separador, pelo que é limpo. Um valor alterado recebe um sufixo fixo de seis carateres, `-` seguido dos primeiros seis carateres do hash MD5 do valor, colocado antes da extensão do ficheiro. Os valores que não precisam de alteração mantêm o nome.

### Valores exportados e ordem das linhas

- **Números e booleanos simples.** As exportações CSV, TSV e TXT escrevem números como números simples e booleanos como `true` e `false`, sem `+00:00` nas datas/horas.
- **Ordem das linhas estável.** Um destino que ordena escreve a mesma ordem de linhas em todas as execuções: os empates são resolvidos sempre da mesma forma, e as rotas de divisão e de partes também ordenam. Os destinos Parquet, Google Sheets, Tableau e tabela não mantêm ordem das linhas.

### Opções do Excel

Um destino Excel mapeia estas opções:

- **Separador por valor do campo.** Cada valor do campo torna-se uma folha. Os valores em branco vão para `Sheet1`, e as folhas cujos nomes colidem recebem um sufixo numérico.
- **Formato a partir de modelo.** Cada execução copia primeiro `<name>_template.xlsx` da mesma pasta por cima do livro e depois escreve nele, pelo que o livro é sempre substituído. Se o modelo não existir, a cópia gera um aviso e o livro é escrito sem ele.
- **Célula superior esquerda.** As linhas são escritas no livro a partir dessa célula.
- **Modo `create`.** Cada execução escreve o ficheiro conforme o modo de escrita do destino indica.

## Associar pedidos de API

Um agente de API cujo URL é relativo, como `/v2/customers`, não tem anfitrião para onde enviar. Associe um com `api_bindings`. A chave é o ID ou o nome do nó de API, ou `*` para todos os nós de API sem uma associação própria. O valor é um dos seguintes:

- Um URL de base, como cadeia de caracteres ou `{"base_url": "https://host/path"}`. O URL relativo é juntado a ele. O URL tem de ser `http` ou `https` com um anfitrião público e não pode conter utilizador, consulta nem fragmento.
- `{"connection": "<REST connection id>"}`. O pedido vai para o anfitrião dessa [ligação REST](/pt-pt/reference/connectors/rest/generic-rest/) e transporta as respetivas credenciais. Precisa da permissão de escrita na ligação, e a ligação tem de ser uma ligação REST que consiga ver.

```json
"api_bindings": {
  "*": "https://api.example.com/v1",
  "Customers": { "connection": "<REST connection id>" }
}
```

Uma chave sem correspondência é um aviso, e uma associação que não possa utilizar é recusada. Um URL relativo sem associação permanece um marcador de posição com nome.

Num assistente de IA (MCP) sem permissão de escrita na ligação, uma associação de ligação é ignorada com um aviso, e o URL relativo que teria juntado permanece um marcador de posição. Associe um URL de base ou converta a partir da aplicação Analyze ou da API REST.

Um anfitrião, uma porta ou um caminho que provém de um campo de entrada não precisa de associação. É preenchido linha a linha, com cada valor verificado à medida que é utilizado, e o relatório lista os anfitriões que uma linha pode indicar. Um pedido que transporta uma credencial não pode obter o anfitrião a partir de um campo da linha: enviar uma credencial para um anfitrião escolhido pelos dados é recusado.

A paginação também é convertida. Um URL de página seguinte na resposta, um cabeçalho `Link`, um desfasamento e um número de página tornam-se, cada um, um modo de paginação no passo [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/), que lê todas as páginas. Um valor de paginação pode provir de um campo de entrada (`{{Field}}`) ou de um parâmetro (`{{Param}}`), e um valor escrito como texto numérico, como `10.0`, é lido como número.

## Passos de API com credenciais

Uma credencial nos cabeçalhos, no caminho do URL, na consulta ou no corpo de um agente de API passa para uma ligação REST do PlaidCloud que a importação cria. O passo Pedido REST referencia essa ligação, pelo que a credencial nunca fica no passo.

- A resposta lista as ligações que a importação criou ou reutilizou em `connections`, e o relatório de importação indica-as. Importar novamente a mesma análise reutiliza a mesma ligação em vez de criar outra.
- As credenciais nas informações de utilizador do URL e nos cabeçalhos passam para os campos de autenticação da própria ligação ou para os cabeçalhos predefinidos. Os segredos do caminho, da consulta e do corpo são guardados encriptados na ligação e preenchidos em tempo de execução, apenas para pedidos ao anfitrião `https` da própria ligação.
- Um ponto final `http://` não encriptado não é convertido com credenciais. A credencial fica de fora e o relatório de conversão avisa que não foi copiada.
- Importar através de um assistente de IA (MCP) não cria ligações. As credenciais ficam de fora e um aviso assinala-o. Importe a partir da aplicação Analyze ou da API REST, ou acrescente a credencial manualmente a uma ligação REST e selecione-a no passo.
- Um utilizador sem permissão de escrita na ligação obtém o mesmo resultado: credenciais deixadas de fora e um aviso.
- Apenas um campo de credencial de API move um parâmetro para uma ligação. Um parâmetro de pipeline usado num cabeçalho, consulta, caminho ou corpo onde vai uma credencial de API passa para os `secret_values` encriptados da ligação, e o passo refere-se a ele através da ligação. Nunca é criado como variável de fluxo de trabalho, independentemente do nome do parâmetro.
- Qualquer outro parâmetro cujo nome contenha uma palavra secreta (como `password`, `token`, `secret` ou `key`, com exceção de `key` depois de uma palavra de dados como `sort` ou `partition`) torna-se uma variável de fluxo de trabalho com um valor em branco e um aviso. Um nome como `api_key_2` também é limpo. Defina o valor na variável de projeto após a importação.
- Um parâmetro com nome de contagem ou limite, como `max_tokens`, mantém o seu valor.
- Um segredo escrito numa fórmula, filtro ou valor de substituição é deixado de fora do passo e o relatório de conversão avisa. Um caminho, um URL e um resumo hexadecimal de 40 ou 64 carateres são mantidos, a menos que parte deles ou o nome de um segredo indique o contrário. As ligações de partilha de pastas e os endereços de e-mail dos destinatários nunca aparecem em avisos ou notas.
- Uma resposta que devolve uma credencial é guardada tal como foi recebida. Trate a tabela de saída desse pedido como sensível.

## JWT_ENCODE

`JWT_ENCODE` é convertido num passo [JWT Encode](/pt-pt/reference/workflow-steps/tables/table-jwt-encode/). Uma chave de assinatura literal vai para uma ligação dedicada associada ao passo, e o token é assinado em tempo de execução, pelo que a chave nunca aparece na configuração do passo. Através de um assistente de IA, ou sem permissão de escrita na ligação, a chave é deixada de fora, o token é NULL e um aviso indica que deve importar novamente com permissão para criar ligações.

## Promover uma linha de dados a cabeçalhos das colunas

Um agente Format definido como **replace names with row** é convertido num passo [Promote Header](/pt-pt/reference/workflow-steps/tables/table-promote-header/). Em tempo de execução, a linha escolhida, contada a partir de 1, passa a ser os nomes das colunas e é removida. Uma origem que não tem ordem de registos recebe uma nota, porque a linha que dá nome às colunas pode mudar de execução para execução. Uma coluna que essa linha nomeia mas que nenhum passo posterior menciona não é transportada para além de um passo que lista as colunas que lê.

## Ficheiros sem colunas declaradas

Uma origem sem colunas declaradas mantém estas colunas:

- Uma origem CSV, TSV ou TXT associada na importação mantém todas as colunas do cabeçalho do ficheiro.
- Qualquer outro tipo de ficheiro, e qualquer origem não associada, mantém apenas as colunas que os passos posteriores indicam, e o relatório de conversão avisa.
- Um cabeçalho promovido sobre uma origem desse tipo lê todas as colunas, a partir de ficheiros CSV, Excel, XLS, JSON, Parquet e Avro.

Quando uma origem desse tipo alimenta apenas um cabeçalho promovido, a importação é um passo [Import Delimited](/pt-pt/reference/workflow-steps/import/import-delimited/) que lê todas as colunas por posição. Um passo que exporta ou junta depois de um cabeçalho promovido transporta todas as colunas que a tabela tem em tempo de execução (consulte **Transportar também colunas indicadas em tempo de execução** em [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/)).

## Comportamentos a conhecer

Estas conversões comportam-se da seguinte forma.

| Agente | Comportamento |
| --- | --- |
| Blend (`blend`) | Junta por predicados combinados com OR, contains e is-part-of. Os blends que excluem a interseção externa e as saídas sem correspondência são convertidos nos fluxos de junção correspondentes. Para qualquer operador, a chave duplicada do lado direito é eliminada da saída. |
| Dedupe (`deduplicate`) | Mantém o primeiro registo por chave dentro de cada grupo de Agrupar por. O indicador de duplicados marca todos os membros de um grupo de duplicados, e os duplicados também podem ser encaminhados para um segundo fluxo. Com uma única saída ligada, comporta-se como o Savant. |
| Summarize (`summarize`) | Os agregados de janela acrescentam o agregado a todas as linhas em vez de colapsar os grupos. |
| Sample (`sample`) | As primeiras N linhas, por grupo ou no total, uma percentagem ou um número aleatório de linhas, ou uma linha em cada N. |
| Time Series (`rollup`) | Períodos de dia, semana, mês, trimestre, ano e década entre as datas opcionais de início e fim, por grupo. Os períodos mensais são etiquetados `YYYY-MM`, e os períodos sem registos aparecem com zeros. Os registos com data NULL são excluídos. |
| Pivot (`pivot`) | COUNT conta linhas. |
| XML (`xml`) | SELECT extrai elementos, os caminhos podem conter espaços de nomes e TO_JSON converte XML em JSON. Qualquer caminho XPath 1.0 é convertido, incluindo predicados, testes de atributos, carateres universais e funções como `count()`, `name()` e `contains()`, e o passo [Análise de XML](/pt-pt/reference/workflow-steps/tables/table-xml-parse/) lê-o como XPath. Com `processNs` desativado, os nomes são comparados literalmente, prefixo incluído. Um ficheiro XML em falta quando converte resolve o seu elemento raiz quando o fluxo de trabalho é executado. |
| JSON (`json`) | Nivela em colunas largas. O texto que não é JSON válido dá NULL, e as matrizes saem como texto. |
| Split (`split`) | Divide em colunas ou linhas, com o número de colunas lido a partir dos dados de cada vez que o fluxo de trabalho é executado. |

Estas funções de expressão seguem os resultados do Savant:

| Função | Comportamento |
| --- | --- |
| `DATE_DIFF` | As semanas e os trimestres são contados como o Savant os conta. |
| `PAD` | Não trunca um valor mais longo do que a largura de destino. |
| `+` em texto | Concatena texto. Uma coluna de uma origem sem tipos declarados é lida como número, pelo que `+` soma, e uma nota assinala-o. |
| Dividir em linhas | Mantém as partes vazias como linhas. |
| `LAST` sem ordenação | Devolve a última linha pela ordem em que as linhas chegam, com uma nota de que o armazém de dados não garante essa ordem. |
| `JOIN_STR` | Junta um número fracionário como o Savant o escreve, sem preenchimento com zeros à direita. |
| `JSON_FORMAT` | Formata o JSON de forma legível; no Snowflake, escreve o JSON compacto numa só linha. |
| `JSON_SET` | Mantém a ordem das chaves do Savant. |
| `GREATEST` e `LEAST` | Ignoram argumentos NULL. O resultado só é NULL quando todos os argumentos são NULL. |
| `ROUNDUP` | Arredonda para cima até ao passo inteiro seguinte, pelo que um número negativo arredonda em direção a zero: -1,5 torna-se -1. `ROUNDDOWN` não é alterado. |
| `DURING_DAYLIGHT_SAVING` e `DURING_STANDARD` | NULL à entrada dá NULL à saída. |
| `TO_TEXT` com um formato de data | Lê os símbolos de formato como o Savant. `YYYY`, `w` e `u` são o ano de semana, a semana e o dia da semana ISO, e uma letra de fuso ou de era é escrita como para uma hora UTC. |
| `TO_TEXT` e saída de número para texto | Escreve números simples como `12`, não `12.0000000000`. |
| `TO_TEXT` com um padrão numérico | Formata como o `DecimalFormat` do Java, com arredondamento ao par mais próximo, incluindo padrões científicos como `##0.##E0`. |
| `TO_TEXT` e análise de datas com um formato por linha | Lê o formato de cada linha. |
| Símbolos de data de frações de segundo, mês estreito e baseados em semana | São convertidos. Os símbolos de semana são lidos como semanas ISO. |
| Anos de dois dígitos (`yy`, `y`) | Lidos através de uma janela de 80 anos para trás e 20 anos para a frente a partir do ano atual. |
| `REGEX_MATCH` | Uma correspondência parcial: o padrão corresponde em qualquer parte do texto, não ao texto inteiro. |

`TO_TEXT` e os formatos de data são convertidos num passo [Text Function](/pt-pt/reference/workflow-steps/tables/table-text-function/). Uma edição que transporta apenas os seus passos compilados, sem expressão, é convertida como esses passos aplicados por ordem, cada um a alimentar o seguinte, e o relatório de conversão indica a ordem que assumiu. O conversor recusa, pelo nome, o que o próprio Savant falha ou o que não tem nada para converter, e o passo torna-se um marcador de posição: uma função de agregação ou de janela simples dentro de uma expressão Transform ou Filter (dentro de um cálculo ou de um Summarize é convertida), `HASH` com um algoritmo literal diferente de `md5` ou `sha1`, uma construção de expressão regular que o PlaidCloud não consegue ler (uma classe dentro de uma classe, uma interseção de classes ou uma propriedade `\p{}` desconhecida), uma edição Transform sem expressão e sem passos compilados (como uma edição do Copilot que só tem o seu pedido), um caminho XML que não é XPath 1.0 e um pedido de API que transporta uma credencial e obtém o anfitrião a partir de um campo da linha. A [matriz de conversão do Savant](/pt-pt/reference/savant-conversion-matrix/#recusas-identificadas) lista cada um com o respetivo motivo.

As funções de expressão são também convertidas para `sha1`, `NOT_TRUE`, `LEVENSHTEIN`, as funções de horário de verão (`DST`) e as funções de expressões regulares que aceitam a n-ésima correspondência. `DAY_OF_WEEK` numera o domingo como 7, e `DAY_NAME` devolve o nome do dia.

## Ler o relatório de conversão

A resposta inclui o relatório de conversão: um resumo de quantos passos foram convertidos com confiança alta, média ou baixa e quantos não foram convertidos, além dos avisos e dos nós que o conversor absorveu noutros. Leia-o antes de executar o fluxo de trabalho. Indica todos os marcadores de posição, todas as origens não associadas e associações sem correspondência, e o prefixo de tabela utilizado.

## Marcadores de posição para configurações não convertidas

Uma configuração que o conversor não consegue reproduzir é criada como um passo de marcador de posição com o nome do agente, e o relatório de conversão indica-o. Surge um marcador de posição para uma construção que o conversor recusa pelo nome (consulte a [matriz de conversão do Savant](/pt-pt/reference/savant-conversion-matrix/#recusas-identificadas)) ou que a exportação não descreve por completo, como uma configuração de API em falta. Por predefinição, um marcador de posição falha quando o fluxo de trabalho o alcança, para que uma execução não possa comunicar êxito em trabalho que nunca aconteceu.

Defina `allow_unconverted_placeholders` como `true` para importar cada marcador de posição como um passo de passagem direta. A execução continua então para além dele e a saída do marcador de posição é a sua entrada. Reconstrua a capacidade com um passo nativo quando o seu resultado for importante.

## Executar o fluxo de trabalho convertido

1. Abra o novo fluxo de trabalho no projeto.
2. Defina as variáveis de projeto que tenham origem em parâmetros do Savant.
3. Carregue os ficheiros das origens não associadas para os caminhos indicados no relatório.
4. Execute o fluxo de trabalho e reveja a tabela de saída de cada passo.

## Casos limite

Estas são as únicas diferenças conhecidas em relação ao Savant. O relatório de conversão indica cada uma das que se aplicam.

- **Formatos de data.** `TO_DATE` ou `TO_DATETIME` com um formato que contém um literal `[`, `]`, `'`, `\` ou `^`, sobre texto que lê para 9999-12-30 ou 9999-12-31, cai para além da última data/hora que o armazém de dados suporta, e o relatório avisa.
- **Parâmetros secretos.** Um parâmetro cujo nome contém uma palavra secreta, ou cujo valor se parece com uma credencial, torna-se uma variável de projeto com um valor em branco, por conceção. Defina o valor na variável.
- **Parâmetros não declarados.** Um parâmetro que um nó utiliza e que a exportação não declara chega como uma variável de projeto com um valor vazio.
- **`JSON_FORMAT` no Snowflake.** Escreve JSON compacto numa só linha.
- **Ordem das linhas.** Os destinos Parquet, Google Sheets, Tableau e tabela ordenados não mantêm ordem das linhas.
- **Google Sheets e Tableau.** Publicar em qualquer um deles exige que a respetiva conta seja associada através de `destination_bindings`.

## Guias relacionados

- [Matriz de conversão do Savant](/pt-pt/reference/savant-conversion-matrix/)
- [Ligação REST](/pt-pt/reference/connectors/rest/generic-rest/)
- [Adicionar contas de documentos](/pt-pt/guides/documents/adding-accounts/)
- [Gerir variáveis de fluxo de trabalho](/pt-pt/guides/workflows/manage-workflow-variables/)
- [Passo AI/NLP](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/)
- [Passo Pedido REST](/pt-pt/guides/workflows/rest-request-step/)
- [Executar um fluxo de trabalho](/pt-pt/guides/workflows/run-a-workflow/)
