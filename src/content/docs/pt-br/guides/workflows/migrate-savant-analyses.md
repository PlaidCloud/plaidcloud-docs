---
title: Migrar análises do Savant
description: Converta a exportação de uma análise do Savant Labs em um fluxo de trabalho avançado do PlaidCloud pelo aplicativo Analyze, pela API REST ou por um agente de IA conectado por MCP, vincule suas origens e leia o relatório de conversão.
sidebar:
  order: 31
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-savant-analyses.md
---

O PlaidCloud é um substituto direto do Savant. Todo agente, expressão e configuração do Savant é convertido para o PlaidCloud e executa. O conversor transforma a exportação de uma análise do Savant Labs em um fluxo de trabalho avançado executável: ele mapeia cada agente do Savant para uma etapa de fluxo de trabalho, uma variável de projeto ou um objeto da tela, mantém o grafo original e devolve um relatório de conversão que indica tudo o que não pôde ser convertido.

A conversão lê o arquivo de exportação que você indicar e os cabeçalhos dos arquivos que você vincular às origens. Ela nunca se conecta ao sistema ao qual uma origem ou um destino do Savant se conecta.

## O que o PlaidCloud cria

- Cada agente do Savant se torna a etapa de fluxo de trabalho correspondente, com as relações a montante e a jusante preservadas. A [matriz de conversão do Savant](/pt-br/reference/savant-conversion-matrix/) lista todos os agentes e o nível de mapeamento de cada um.
- Os parâmetros de análise do Savant se tornam variáveis de projeto, e as referências a eles nas configurações dos agentes são reescritas para a sintaxe de variáveis do PlaidCloud.
- Notas e grupos chegam à tela como notas e grupos.
- Cada origem se torna uma etapa de importação ou lê uma tabela existente, dependendo de como você a vincula.
- Todo tipo de agente do Savant é convertido por completo: cada opção tem um mapeamento. Uma configuração em que o próprio Savant falha ou que ele não documenta chega como uma etapa de marcador nomeada. Consulte [Marcadores para configurações não convertidas](#marcadores-para-configurações-não-convertidas).

## Antes de começar

1. Exporte a análise do Savant com **Exportar JSON**.
2. Carregue o arquivo `.json` em uma [conta de documentos](/pt-br/guides/documents/adding-accounts/) que você possa ler.
3. Escolha o projeto do PlaidCloud que receberá o fluxo de trabalho. Você precisa ter acesso de gravação a ele.
4. Escolha uma conta de documentos e uma pasta base de onde os arquivos de origem da análise serão lidos.

## Converter uma análise

Converta pelo aplicativo Analyze, pela API REST ou pelo catálogo de ferramentas MCP. Os três usam os mesmos campos.

### Aplicativo Analyze

1. Abra o **Analyze** e escolha **Tools → Importar análise do Savant**.
2. Escolha o **Projeto de destino** e o **Arquivo de exportação do Savant (.json)** que você carregou em uma conta de documentos.
3. Selecione **Carregar origens**. A janela lista cada nó de origem da exportação.
4. Para conectar uma origem a dados que você já tem, selecione-a e escolha **Vincular…**. Escolha **Tabela do projeto** para ler uma tabela do projeto de destino, ou **Documento** para ler um arquivo de uma conta de documentos (com um nome de planilha opcional para o Excel). Escolha **Desvincular** para remover uma vinculação.
5. Em **Diretório de origens não vinculadas**, escolha a conta de documentos e a pasta base de onde os arquivos das origens não vinculadas são lidos.
6. Em **Opções de conversão**, escolha o **Tipo de fluxo de trabalho** e se deseja **Permitir marcadores não convertidos**. Em **Prefixos de objetos**, defina, se quiser, prefixos de fluxo de trabalho, de etapa e de tabela.
7. Selecione **Converter**.

Quando a conversão termina, a janela mostra o relatório de conversão: o nome do fluxo de trabalho e o prefixo de tabela, os avisos, uma tabela com os caminhos de documento onde carregar os arquivos das origens não vinculadas e as etapas que precisam de revisão. Se a lista de origens não puder ser carregada, adicione uma linha para cada origem com o ID do nó e o ID `analyzetable_` da tabela a vincular.

### Campos

A API REST e a ferramenta MCP usam estes campos.

| Campo | Obrigatório | O que faz |
| --- | --- | --- |
| `source_account_id` | Sim | Conta de documentos que contém a exportação do Savant. |
| `source_file_path` | Sim | Caminho da exportação dentro dessa conta. |
| `project_id` | Sim | Projeto em que o fluxo de trabalho é criado. |
| `document_account_id` | Sim | Conta de documentos da qual as origens não vinculadas são lidas. |
| `document_account_path` | Sim | Pasta base, nessa conta, para as origens não vinculadas. Um valor vazio ou `/` é a raiz da conta, e uma `/` inicial é ignorada. Caminhos com `..` ou segmentos iniciados por ponto, chaves, letra de unidade ou esquema de URL, ou caracteres de controle são recusados. |
| `workflow_prefix` | Não | Prefixo adicionado aos nomes dos fluxos de trabalho. |
| `step_prefix` | Não | Prefixo adicionado aos nomes das etapas. |
| `table_prefix` | Não | Prefixo adicionado aos nomes das tabelas. O padrão é o próprio nome do fluxo de trabalho. Um prefixo que reutilizaria o nome de uma tabela existente é recusado antes que qualquer coisa seja criada. O prefixo usado é devolvido no relatório de conversão. |
| `workflow_type` | Não | `advanced` (padrão) distribui o grafo na tela de DAG. `standard` produz uma lista serial de etapas. |
| `source_bindings` | Não | Vincula origens a dados existentes. Consulte [Vincular origens](#vincular-origens). |
| `destination_bindings` | Não | Direciona os destinos para uma conta de documentos, uma tabela de conexão, uma planilha Google, uma fonte de dados do Tableau, um canal do Slack ou destinatários de e-mail. Somente REST e MCP. Consulte [Destinos](#destinos). |
| `api_bindings` | Não | Informa para onde vai a URL relativa de um agente de API: uma URL base ou uma conexão REST. Somente REST e MCP. Consulte [Vincular solicitações de API](#vincular-solicitações-de-api). |
| `allow_unconverted_placeholders` | Não | Controla o que um marcador faz durante a execução. Consulte [Marcadores para configurações não convertidas](#marcadores-para-configurações-não-convertidas). |

### REST

Envie os campos como um corpo JSON para:

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

Para listar os nós de origem de uma exportação antes de montar `source_bindings`, envie `source_account_id` e `source_file_path` para:

```text
POST /rest/v1/analyze/savant/sources
```

Cada entrada da resposta traz o `node_id`, o `name` e o `connector` da origem.

### MCP

Um agente de IA conectado por MCP chama a ferramenta `savant_convert` com os mesmos campos. Consulte [Agentes de IA (MCP)](/pt-br/integrations/ai-coding-agents/) para conectar um agente. A ferramenta altera o seu projeto, portanto revise a chamada antes de aprová-la.

## Vinculações no momento da conversão

Uma exportação do Savant não traz dados, credenciais nem conexões; por isso, três parâmetros do momento da conversão a conectam aos seus. Cada um é um mapa de um ID ou nome de nó do Savant para um destino, e uma vinculação que você não pode usar faz a conversão inteira ser recusada antes que qualquer coisa seja criada.

| Parâmetro | Vincula | Seção |
| --- | --- | --- |
| `source_bindings` | Agentes de origem a tabelas ou arquivos | [Vincular origens](#vincular-origens) |
| `destination_bindings` | Agentes de destino a um arquivo, tabela, planilha, fonte de dados do Tableau, canal do Slack ou e-mail | [Destinos](#destinos) |
| `api_bindings` | Agentes de API com URL relativa a uma URL base ou conexão REST | [Vincular solicitações de API](#vincular-solicitações-de-api) |

## Vincular origens

Uma exportação do Savant descreve de onde seus dados vêm, mas não traz dados nem credenciais. Use `source_bindings` para conectar cada origem aos dados que você já tem no PlaidCloud. A chave é o ID do nó, o ID do conjunto de dados ou o nome da origem. O valor é um destes:

- Um ID `analyzetable_` de uma tabela do projeto de destino. O fluxo de trabalho convertido lê essa tabela diretamente.
- Um objeto com `account`, `path` e, opcionalmente, `sheet`, para ler um arquivo de uma conta de documentos.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "Budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Uma vinculação que você não pode ler é recusada. Uma chave que não corresponde a nenhuma origem é informada como aviso.

O caminho de um arquivo de origem na exportação pode começar com `/` ou passar por pastas iniciadas por ponto, como `.archive`, e é convertido normalmente. Uma origem que lê XML converte o texto XML, e uma origem de documento XML também traz as colunas de contexto de arquivo do Savant.

### Origens não vinculadas

Uma origem sem vinculação se torna uma etapa de importação ainda sem dados, e o relatório de conversão traz um aviso para ela. A etapa lê de:

```text
<document_account_path>/savant/<workflow id>/<source name>.csv
```

Carregue o arquivo nesse caminho e execute o fluxo de trabalho. Enquanto o arquivo não estiver lá, a etapa de importação termina com um aviso e cria uma tabela vazia, e o fluxo de trabalho continua.

## Como os agentes são convertidos

A maioria dos agentes é convertida na etapa que você criaria manualmente; a [matriz de conversão do Savant](/pt-br/reference/savant-conversion-matrix/) lista todos os agentes. Estes agentes exigem cuidado extra.

| Agente do Savant | Em que se torna | Ressalvas |
| --- | --- | --- |
| Infer Agent (`gen_ai` e, em versões antigas, `service` com um serviço de LLM) | Uma etapa [AI/NLP](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) com a tarefa **Prompt**. O prompt é executado uma vez por linha sobre os campos de entrada, e a resposta vai para uma coluna **AI Answer** ao lado de todas as colunas de entrada. Um limite de linhas se torna **Máximo de linhas**, e uma origem vazia gera um aviso e grava uma tabela vazia. **Max New Rows** responde apenas às linhas novas e mantém as respostas de execuções anteriores. | Um LLM responde, portanto a saída nunca é idêntica byte a byte à do Savant e pode variar entre execuções. Cada chamada tem um custo. Consulte [Provedores de IA](#provedores-de-ia). Um lote que falha mantém as suas linhas com a resposta vazia e gera um aviso. |
| Vision Agent (`vision`) | Uma etapa [Document Read Blob](/pt-br/reference/workflow-steps/text-documents/document-blob-extract/), [Image OCR](/pt-br/reference/workflow-steps/text-documents/image-ocr/) e, em seguida, a tarefa **Prompt** do AI/NLP. Cada documento vai para o provedor como imagem ou PDF quando o provedor aceita esse tipo e tamanho. Caso contrário, a etapa envia a camada de texto do PDF ou o texto do OCR. | As mesmas ressalvas de LLM do Infer Agent. Documentos inteiros saem do PlaidCloud para o provedor, e a conversão gera um aviso. Arquivos TIFF e BMP são enviados como texto de OCR, e não há configuração de tamanho máximo de documento. Um documento que não é encontrado é ignorado, e a etapa gera um aviso com o seu caminho. |
| API Agent (`apiService` e, em versões antigas, `service` com um serviço de API) | Uma etapa [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) que envia uma solicitação por linha de entrada, seguida de uma junção de volta que mantém todas as linhas de entrada. O corpo bruto da resposta vai para uma coluna de texto, com uma coluna de status ao lado. Uma cota por período se torna um **Máx. solic./s** fracionário. Uma URL relativa é unida à URL base ou à conexão REST que você vincular com `api_bindings`. Um host, porta ou caminho que vem de um campo da linha é preenchido linha a linha. A paginação por próxima URL, cabeçalho Link, deslocamento e número de página é seguida, e um valor de paginação (início, tamanho da página ou nome do parâmetro) pode vir de um campo de entrada ou de um parâmetro. | Um método diferente de GET é executado no sistema real uma vez por linha de entrada a cada execução do fluxo de trabalho, portanto confirme o destino antes da primeira execução. Solicitações que não são GET não são repetidas automaticamente. Uma solicitação com falha permanece como uma linha com o seu status. Uma solicitação que leva uma credencial não pode obter o host de um campo da linha. As credenciais são tratadas como descrito em [Etapas de API com credenciais](#etapas-de-api-com-credenciais). |
| Recursion Agent (`hierarchy`) | Uma etapa [Hierarchy Closure](/pt-br/reference/workflow-steps/tables/table-hierarchy-closure/) que percorre cada linha pela cadeia de pais até qualquer profundidade e depois agrega cada nó sobre os IDs do seu caminho até a raiz, ele mesmo incluído. Ela grava Depth e Path. Uma linha com pai em branco, ou que nomeia a si mesma como pai, é uma raiz. | Um ciclo nos IDs dos pais para no nó repetido e mantém todos os ancestrais anteriores a ele. Linhas com vários pais mantêm cada uma os seus próprios valores. |
| Search and Replace (`search_replace`) | Um [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/) que aplica cada regra, em ordem, às colunas de texto escolhidas, com ou sem distinção entre maiúsculas e minúsculas, palavra inteira ou não. Cada regra é executada no seu modo: substituir o texto correspondente, substituir a célula inteira quando ela contém o texto, substituir a célula inteira quando ela corresponde exatamente, ou anexar à célula. | As regras são textos literais, não padrões. |
| Split (`split`) | Uma etapa [Split Text](/pt-br/reference/workflow-steps/tables/table-split-text/). Ela divide em colunas ou linhas por um separador literal de qualquer comprimento e decide o número de colunas a partir dos dados quando o fluxo de trabalho é executado. | Nenhuma. |
| Time Series (`rollup`) | Um Table Extract que agrupa por uma expressão de período, com um [Period Spine](/pt-br/reference/workflow-steps/tables/table-period-spine/), uma anti junção e uma união que preenchem com zero os períodos sem registros. | Registros com data NULL são excluídos. O spine para em 100.000 períodos. |
| Format (`format`) | Um Table Extract com as renomeações, mudanças de tipo, ocultações e preenchimentos, ou uma etapa [Promote Header](/pt-br/reference/workflow-steps/tables/table-promote-header/) para substituir nomes pela linha. | Um preenchimento em uma coluna que não é de texto converte o valor padrão para o tipo da coluna. Promover um cabeçalho sobre uma origem que não declara colunas lê todas as colunas, de arquivos CSV, Excel, XLS, JSON, Parquet e Avro. Consulte [Arquivos sem colunas declaradas](#arquivos-sem-colunas-declaradas). |
| Spatial Match Agent (`spatial_match`) | Uma etapa [Correspondência espacial (executor)](/pt-br/reference/workflow-steps/spatial/spatial-match-executor/) para intersects, within, contains, touches, crosses, overlaps, equals e disjoint, com várias regras combinadas; Junção cruzada para uma correspondência cruzada; [Localizar mais próximo](/pt-br/reference/workflow-steps/spatial/spatial-find-nearest/) para uma correspondência do mais próximo. | Uma correspondência do mais próximo classifica e filtra pela distância de círculo máximo, como o Savant faz. Uma regra de mais próximo combinada com outras regras encontra primeiro os registros mais próximos e depois aplica as outras regras: com AND, o resultado mantém os registros que satisfazem todas as regras e, com OR, une os registros mais próximos aos registros que as outras regras encontram. Uma regra de mais próximo sem contagem nem distância máxima mantém o único registro mais próximo. Uma correspondência por distância também é convertida, em quilômetros quando a regra não informa unidade, e mede a distância geodésica entre quaisquer geometrias, não apenas pontos. Uma geometria que não pode ser analisada resulta em NULL ou em nenhuma correspondência, com um aviso. |
| Spatial Summarize Agent (`spatial_summarize`) | [Combinação espacial](/pt-br/reference/workflow-steps/spatial/spatial-combine/) para união, interseção e caixa delimitadora, além de [Spatial Centroid](/pt-br/reference/workflow-steps/spatial/spatial-centroid/), [Spatial Point to Line](/pt-br/reference/workflow-steps/spatial/spatial-point-to-line/) e [Spatial Line to Polygon](/pt-br/reference/workflow-steps/spatial/spatial-line-to-polygon/) para centro geométrico e construção de linhas ou polígonos. | Um polígono construído com menos de 3 pontos é um polígono vazio. |
| Destination Agent (`destination`) | Uma etapa de exportação para o destino que você vincular, ou uma tabela ou arquivo do projeto quando você não vincula. Consulte [Destinos](#destinos). | Consulte [O que continua limitado](#what-stays-limited). |

`GEO_POINT`, `GEO_TYPE` e `GEO_SPATIAL_DISTANCE` são convertidos em expressões. Uma edição cuja expressão inteira é outra função `GEO_*`, como `GEO_AREA` ou `GEO_UNION`, é convertida na etapa espacial correspondente, incluindo [Spatial Info](/pt-br/reference/workflow-steps/spatial/spatial-info/). A geometria trafega como texto WKT. `GEO_AREA`, `GEO_PERIMETER` e `GEO_SPATIAL_DISTANCE` em milhas usam a milha terrestre (statute mile).

Uma origem que lê arquivos binários, como os documentos que um agente Vision lê, é convertida em uma extração de documento do documento vinculado, ou do arquivo esperado no caminho das origens não vinculadas.

## Provedores de IA

Um agente Infer ou Vision é convertido em uma etapa AI/NLP que usa uma conexão de LLM. O conversor oferece suporte a Anthropic, OpenAI, Gemini, Azure OpenAI, Grok e GitHub Models.

- O conversor escolhe a conexão para o provedor e o modelo que o agente nomeia, entre as conexões de LLM que o usuário que importa pode ver. Ele nunca nomeia uma que o usuário não possa ver. Por meio de um assistente de IA (MCP), isso significa as conexões que o usuário do assistente pode ver.
- Quando o provedor não tem nenhuma conexão visível, ou o provedor do Savant não tem correspondente no PlaidCloud (uma API de modelo hospedada na nuvem ou um provedor com chave própria do espaço de trabalho do Savant), a etapa usa a conexão padrão do espaço de trabalho, se o usuário puder vê-la. Caso contrário, ela deixa a conexão em branco, e a etapa usa o padrão do espaço de trabalho quando é executada. O relatório de conversão gera um aviso nos dois casos; portanto, escolha uma conexão na etapa se outra diferente deve responder.

## Destinos

Um destino do Savant grava a tabela que recebe no destino que você vincular. Vincule os destinos com `destination_bindings` no corpo REST ou na chamada MCP. A chave é o ID do nó ou o nome do destino. A janela do Analyze não vincula destinos, portanto um destino convertido ali grava o resultado não vinculado descrito em [Destinos não vinculados](#destinos-não-vinculados).

| Destino | Vinculação | Resultado |
| --- | --- | --- |
| Conta de documentos | `{account, path[, file_name]}` | Um arquivo CSV, TSV, TXT, Excel, Parquet, JSON, Avro, XML, PDF ou Tableau Hyper, conforme o tipo de destino. Você precisa da permissão de gravação de armazenamento de documentos na conta. |
| Tabela em uma conexão | `{connection, table[, schema, replace]}` | Uma etapa [Export: External Database Tables](/pt-br/reference/workflow-steps/export/export-external-tables/). Você precisa da permissão de gravação na conexão. Substituir a tabela exige `replace: true`. |
| Google Sheets | `{connection, spreadsheet_name[, sheet_name, replace]}` ou `{connection, spreadsheet_id[, sheet_name, replace]}` | Uma etapa [Export to Google Spreadsheet](/pt-br/reference/workflow-steps/export/export-to-google-spreadsheet/) em uma conexão do Google Sheets. A guia padrão é a que o destino nomeia; caso contrário, `Sheet1`. Um destino que substitui as linhas da planilha limpa a guia, portanto exige `replace: true`. |
| Tableau | `{account, connection[, path, file_name, replace, datasource_name, tableau_project]}` | Uma extração Tableau Hyper gravada na pasta da conta, seguida de uma etapa [Publish to Tableau](/pt-br/reference/workflow-steps/export/export-to-tableau/) em uma [conexão Tableau](/pt-br/reference/connectors/collaboration/tableau/). Substituir a fonte de dados, ou alterar as suas linhas por chaves de correspondência, exige `replace: true`. |
| Slack | `{connection[, channel]}` | O CSV é gravado em uma conta de documentos, e depois uma etapa [Notify via Slack](/pt-br/reference/workflow-steps/notifications/notify-via-slack/) o carrega no canal. A conexão precisa de um token de bot, e o canal deve ser um ID de canal, obtido da vinculação ou, na falta dela, da exportação. |
| E-mail | `{email_to: [...]}` e `email_export_recipients: true` para usar também os destinatários que a exportação lista | O CSV é enviado por e-mail como anexo. Você precisa da permissão de gravação de e-mail. |

Uma conexão do Sheets, do Tableau ou do Slack é verificada da mesma forma que uma conexão de tabela: você precisa poder vê-la e ter permissão de gravação na conexão, ou a conversão é recusada.

### Modos de gravação

- Um destino de arquivo ou tabela que acrescenta lê o arquivo anterior de volta e o reescreve com as novas linhas. Ele nunca sobrescreve.
- Um destino upsert, update ou groupReplace faz merge pelas chaves de correspondência do destino. Um arquivo ou tabela é lido de volta e reescrito, e uma fonte de dados do Tableau tem as linhas correspondentes alteradas no local.
- Acrescentar e mesclar também funcionam em arquivos existentes divididos por valor, sem cabeçalho (as linhas correspondem por posição), arquivos do Excel ancorados em uma célula superior esquerda e arquivos em um conjunto de caracteres diferente de UTF-8. Uma divisão lê de volta o arquivo para o qual cada valor é gravado e faz o merge dentro dele, deixando os outros arquivos como estão.
- Um destino Tableau mapeia os modos do Savant para os seis [modos do Publish to Tableau](/pt-br/reference/workflow-steps/export/export-to-tableau/#modos): append e insert adicionam linhas, replace sobrescreve, e upsert, update e groupReplace correspondem por chaves. Um modo que altera dados existentes só publica quando a vinculação diz `replace: true`; caso contrário, o destino publica uma nova fonte de dados e o relatório informa isso.
- Um destino com codificação de saída grava o arquivo nesse conjunto de caracteres Java. Um caractere que o conjunto não possui é gravado como `?`, como o Savant faz. Aliases Java, CESU-8 e formas com marca de ordem de bytes são aceitos. Alguns conjuntos de caracteres raros (por exemplo, `x-ISCII91` ou `JIS_X0212`) não podem ser gravados; o arquivo é gravado em UTF-8 e o relatório gera um aviso. Uma divisão em um conjunto de caracteres diferente de UTF-8 converte a pasta.
- Os nomes dos arquivos de exportação devem permanecer dentro da pasta vinculada.

### O que os chamadores de IA podem vincular

Uma conversão por meio de um assistente de IA (MCP) vincula os mesmos formatos, com estas partes retidas, cada uma com um aviso que a nomeia:

| Retido | O que acontece em vez disso |
| --- | --- |
| `replace` em uma tabela, planilha ou fonte de dados do Tableau | Um destino que acrescenta continua acrescentando à sua tabela ou planilha vinculada. Um destino que substitui grava um CSV. Um destino Tableau publica uma nova fonte de dados. |
| Destinatários de e-mail | Um CSV é gravado no lugar do e-mail. |
| Slack | Um CSV é gravado no lugar da publicação no Slack. |

Converta pelo aplicativo Analyze ou pela API REST, ou entre você mesmo em vez de usar um assistente, para vincular estes itens.

### Destinos não vinculados

Um destino sem vinculação grava o seu equivalente no PlaidCloud e gera o aviso **Destination target unbound**, nomeando o destino original. A conversão nunca se conecta ao sistema de destino.

| Destino | Resultado |
| --- | --- |
| Destino de banco de dados, data warehouse ou SaaS (Oracle, banco de dados genérico, Looker Studio, NetSuite, SAP e Google Sheets, Tableau ou Slack sem conexão vinculada) | Uma tabela no projeto, com o nome do nó de destino. |
| Armazenamento de arquivos (S3, GCS, Box, SFTP, SharePoint, Google Drive, OneDrive) | O arquivo, no tipo de arquivo do destino, em uma pasta de documentos na conta que você informou para as origens não vinculadas. A pasta espelha a pasta de destino. Credenciais e tokens de compartilhamento são removidos do caminho. |
| E-mail | Um CSV, na conta de documentos que você informou para as origens não vinculadas. |

O aviso informa o que vincular para chegar ao destino real. Um destino cuja vinculação não pode ser usada grava um CSV e gera o aviso **Fallback, target not written**, com o destino original na mensagem; confira esse CSV antes de depender dele. Um destino CSV simples grava o seu próprio arquivo.

### Destinos divididos

Um destino que grava um arquivo, uma subpasta ou uma guia por valor de um campo divide arquivos CSV, Excel, Parquet e PDF e guias do Google Sheets.

- **Parquet e PDF.** Um arquivo por valor.
- **Google Sheets.** Uma guia por valor.
- **Modelo.** Uma pasta de trabalho modelo serve de base para a pasta de trabalho de cada valor. Um modelo ausente gera um aviso e a pasta de trabalho é gravada sem ele.
- **Valores NULL.** Um valor de divisão NULL é gravado em seu próprio arquivo ou guia, não descartado.
- **Um campo que a entrada não tem.** Uma divisão, ou uma ordenação, em um campo que a entrada não traz é recusada pelo nome, porque o Savant falha nesse caso.
- **Uma `/` ou `\` em um valor.** Um valor de divisão que contém barra ou barra invertida não pode ser nome de arquivo ou de guia, portanto é higienizado. Um valor alterado recebe um sufixo fixo de seis caracteres, `-` seguido dos seis primeiros caracteres do hash MD5 do valor, colocado antes da extensão do arquivo. Valores que não precisam de alteração mantêm o nome.

### Valores exportados e ordem das linhas

- **Números e booleanos simples.** As exportações CSV, TSV e TXT gravam números como números simples e booleanos como `true` e `false`, sem `+00:00` nos carimbos de data/hora.
- **Ordem estável das linhas.** Um destino que ordena grava uma única ordem de linhas em todas as execuções: os empates são resolvidos da mesma forma sempre, e as rotas de divisão e de partes também são ordenadas. Os destinos Parquet, Google Sheets, Tableau e tabela não mantêm ordem de linhas.

### Opções do Excel

Um destino Excel mapeia estas opções:

- **Guia por valor de campo.** Cada valor do campo se torna uma planilha. Valores em branco vão para `Sheet1`, e as planilhas cujos nomes colidem recebem um sufixo numérico.
- **Formato a partir de modelo.** A cada execução, o sistema primeiro copia `<name>_template.xlsx` da mesma pasta sobre a pasta de trabalho e depois grava nela, de modo que a pasta de trabalho é sempre substituída. Se o modelo não existir, a cópia gera um aviso e a pasta de trabalho é gravada sem ele.
- **Célula superior esquerda.** As linhas são gravadas na pasta de trabalho a partir dessa célula.
- **Modo `create`.** Cada execução grava o arquivo conforme o modo de gravação do destino determina.

## Vincular solicitações de API

Um agente de API cuja URL é relativa, como `/v2/customers`, não tem host para onde enviar. Vincule um com `api_bindings`. A chave é o ID ou o nome do nó de API, ou `*` para todo nó de API sem vinculação própria. O valor é um destes:

- Uma URL base, como texto ou `{"base_url": "https://host/path"}`. A URL relativa é unida a ela. A URL deve ser `http` ou `https` com um host público e não pode conter usuário, consulta nem fragmento.
- `{"connection": "<REST connection id>"}`. A solicitação vai para o host dessa [conexão REST](/pt-br/reference/connectors/rest/generic-rest/) e leva as suas credenciais. Você precisa da permissão de gravação na conexão, e a conexão deve ser uma conexão REST que você possa ver.

```json
"api_bindings": {
  "*": "https://api.example.com/v1",
  "Customers": { "connection": "<REST connection id>" }
}
```

Uma chave sem correspondência é um aviso, e uma vinculação que você não pode usar é recusada. Uma URL relativa sem vinculação permanece como um marcador nomeado.

Em um assistente de IA (MCP) sem permissão de gravação na conexão, uma vinculação de conexão é ignorada com um aviso, e a URL relativa que ela teria unido permanece como marcador. Vincule uma URL base ou converta pelo aplicativo Analyze ou pela API REST.

Um host, porta ou caminho que vem de um campo de entrada não precisa de vinculação. Ele é preenchido linha a linha, com cada valor verificado quando usado, e o relatório lista os hosts que uma linha pode nomear. Uma solicitação que leva uma credencial não pode obter o host de um campo da linha: enviar uma credencial a um host escolhido pelos dados é recusado.

A paginação também é convertida. Uma URL da próxima página na resposta, um cabeçalho `Link`, um deslocamento e um número de página se tornam, cada um, um modo de paginação na etapa [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/), que lê todas as páginas. Um valor de paginação pode vir de um campo de entrada (`{{Field}}`) ou de um parâmetro (`{{Param}}`), e um valor escrito como texto numérico, como `10.0`, é lido como número.

## Etapas de API com credenciais

Uma credencial nos cabeçalhos, no caminho da URL, na consulta ou no corpo de um agente de API é movida para uma conexão REST do PlaidCloud que a importação cria. A etapa Solicitação REST referencia essa conexão, de modo que a credencial nunca fica na etapa.

- A resposta lista as conexões que a importação criou ou reutilizou em `connections`, e o relatório de importação as nomeia. Importar a mesma análise novamente reutiliza a mesma conexão em vez de criar outra.
- As credenciais nas informações de usuário da URL e nos cabeçalhos vão para os campos de autenticação ou cabeçalhos padrão da própria conexão. Os segredos de caminho, consulta e corpo são armazenados criptografados na conexão e preenchidos durante a execução, somente para solicitações ao próprio host `https` dessa conexão.
- Um endpoint `http://` sem criptografia não é convertido com credenciais. A credencial é omitida e o relatório de conversão avisa que ela não foi copiada.
- Importar por meio de um assistente de IA (MCP) não cria conexões. As credenciais são omitidas e um aviso informa isso. Importe pelo aplicativo Analyze ou pela API REST, ou adicione a credencial a uma conexão REST manualmente e selecione-a na etapa.
- Um usuário sem permissão de gravação na conexão obtém o mesmo resultado: credenciais omitidas e um aviso.
- Somente um campo de credencial de API move um parâmetro para uma conexão. Um parâmetro de pipeline usado em um cabeçalho, consulta, caminho ou corpo no local de uma credencial de API é movido para os `secret_values` criptografados da conexão, e a etapa se refere a ele por meio da conexão. Ele nunca é criado como variável de fluxo de trabalho, qualquer que seja o nome do parâmetro.
- Qualquer outro parâmetro cujo nome contenha uma palavra de segredo (como `password`, `token`, `secret` ou `key`, com exceção de `key` depois de uma palavra de dados como `sort` ou `partition`) se torna uma variável de fluxo de trabalho com valor em branco e um aviso. Um nome como `api_key_2` também é esvaziado. Defina o valor na variável de projeto após a importação.
- Um parâmetro nomeado para uma contagem ou limite, como `max_tokens`, mantém o seu valor.
- Um segredo digitado em uma fórmula, filtro ou valor de substituição é omitido da etapa e o relatório de conversão avisa. Um caminho, uma URL e um resumo hexadecimal de 40 ou 64 caracteres são mantidos, a menos que parte deles ou o nome de um segredo indique o contrário. Links de compartilhamento de pastas e endereços de e-mail de destinatários nunca aparecem em avisos ou observações.
- Uma resposta que devolve uma credencial é armazenada como foi recebida. Trate a tabela de saída de uma solicitação desse tipo como sensível.

## JWT_ENCODE

`JWT_ENCODE` é convertido em uma etapa [JWT Encode](/pt-br/reference/workflow-steps/tables/table-jwt-encode/). Uma chave de assinatura literal vai para uma conexão dedicada vinculada à etapa, e o token é assinado durante a execução, de modo que a chave nunca aparece na configuração da etapa. Por meio de um assistente de IA, ou sem permissão de gravação na conexão, a chave é omitida, o token é NULL e um aviso orienta a importar novamente com permissão para criar conexões.

## Promover uma linha de dados a cabeçalhos de coluna

Um agente Format configurado como **replace names with row** é convertido em uma etapa [Promote Header](/pt-br/reference/workflow-steps/tables/table-promote-header/). Durante a execução, a linha escolhida, contada a partir de 1, se torna os nomes das colunas e é removida. Uma origem que não traz ordem de registros recebe uma observação, porque a linha que nomeia as colunas pode mudar de uma execução para outra. Uma coluna que essa linha nomeia, mas que nenhuma etapa posterior menciona, não é levada além de uma etapa que lista as colunas que lê.

## Arquivos sem colunas declaradas

Uma origem sem colunas declaradas mantém estas colunas:

- Uma origem CSV, TSV ou TXT vinculada na importação mantém todas as colunas do cabeçalho do arquivo.
- Qualquer outro tipo de arquivo, e qualquer origem não vinculada, mantém apenas as colunas que as etapas posteriores nomeiam, e o relatório de conversão gera um aviso.
- Um cabeçalho promovido sobre uma origem desse tipo lê todas as colunas, de arquivos CSV, Excel, XLS, JSON, Parquet e Avro.

Quando uma origem desse tipo alimenta apenas um cabeçalho promovido, a importação é uma etapa [Import Delimited](/pt-br/reference/workflow-steps/import/import-delimited/) que lê todas as colunas por posição. Uma etapa que exporta ou faz junção depois de um cabeçalho promovido leva todas as colunas que a tabela tem durante a execução (consulte **Levar também colunas nomeadas durante a execução** em [Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/)).

## Comportamentos que vale conhecer

Estas conversões se comportam da seguinte forma.

| Agente | Comportamento |
| --- | --- |
| Blend (`blend`) | Faz junção por predicados combinados com OR, contains e is-part-of. Blends de exclusão externa do interior e as saídas sem correspondência são convertidos nos fluxos de junção correspondentes. Para qualquer operador, a chave duplicada do lado direito é removida da saída. |
| Dedupe (`deduplicate`) | Mantém o primeiro registro por chave dentro de cada grupo de Agrupar por. O sinalizador de duplicatas marca todos os membros de um grupo duplicado, e as duplicatas também podem ser direcionadas a um segundo fluxo. Com uma única saída conectada, ele se comporta como o Savant. |
| Summarize (`summarize`) | Agregações de janela adicionam o agregado a todas as linhas em vez de recolher os grupos. |
| Sample (`sample`) | As primeiras N linhas, por grupo ou no total, uma porcentagem ou número aleatório de linhas, ou uma linha a cada N. |
| Time Series (`rollup`) | Períodos de dia, semana, mês, trimestre, ano e década entre as datas inicial e final opcionais, por grupo. Os períodos mensais são rotulados `YYYY-MM`, e os períodos sem registros aparecem com zeros. Registros com data NULL são excluídos. |
| Pivot (`pivot`) | COUNT conta linhas. |
| XML (`xml`) | SELECT extrai elementos, os caminhos podem ter namespaces e TO_JSON converte XML em JSON. Qualquer caminho XPath 1.0 é convertido, incluindo predicados, testes de atributo, curingas e funções como `count()`, `name()` e `contains()`, e a etapa [Análise de XML](/pt-br/reference/workflow-steps/tables/table-xml-parse/) o lê como XPath. Com `processNs` desativado, os nomes são comparados literalmente, prefixo incluído. Um arquivo XML ausente no momento da conversão tem o elemento raiz resolvido quando o fluxo de trabalho é executado. |
| JSON (`json`) | Achata em colunas largas. Um texto que não é JSON válido resulta em NULL, e os arrays saem como texto. |
| Split (`split`) | Divide em colunas ou linhas, com o número de colunas lido dos dados a cada execução do fluxo de trabalho. |

Estas funções de expressão seguem os resultados do Savant:

| Função | Comportamento |
| --- | --- |
| `DATE_DIFF` | Semanas e trimestres são contados como o Savant faz. |
| `PAD` | Não trunca um valor mais longo que a largura de destino. |
| `+` em texto | Concatena texto. Uma coluna de uma origem sem tipos declarados é lida como número, portanto `+` soma, e uma observação informa isso. |
| Divisão em linhas | Mantém partes vazias como linhas. |
| `LAST` sem ordenação | Devolve a última linha na ordem em que as linhas chegam, com uma observação de que o data warehouse não garante essa ordem. |
| `JOIN_STR` | Junta um número fracionário como o Savant o escreve, sem preenchimento de zeros à direita. |
| `JSON_FORMAT` | Formata o JSON de forma legível; no Snowflake, grava o JSON compacto em uma única linha. |
| `JSON_SET` | Mantém a ordem das chaves do Savant. |
| `GREATEST` e `LEAST` | Ignoram argumentos NULL. O resultado é NULL somente quando todos os argumentos são NULL. |
| `ROUNDUP` | Arredonda para cima até o próximo passo inteiro, de modo que um número negativo arredonda em direção a zero: -1,5 vira -1. `ROUNDDOWN` não muda. |
| `DURING_DAYLIGHT_SAVING` e `DURING_STANDARD` | Entrada NULL resulta em saída NULL. |
| `TO_TEXT` com formato de data | Lê os tokens de formato como o Savant. `YYYY`, `w` e `u` são o ano-semana, a semana e o dia da semana ISO, e uma letra de fuso ou de era é gravada como para um horário UTC. |
| `TO_TEXT` e saída de número para texto | Grava números simples como `12`, e não `12.0000000000`. |
| `TO_TEXT` com padrão numérico | Formata como o `DecimalFormat` do Java, arredondando meio para o par, incluindo padrões científicos como `##0.##E0`. |
| `TO_TEXT` e análise de datas com formato por linha | Lê o formato de cada linha. |
| Tokens de data de fração de segundo, mês estreito e baseados em semana | São convertidos. Os tokens de semana são lidos como semanas ISO. |
| Anos de dois dígitos (`yy`, `y`) | Lidos por uma janela de 80 anos para trás e 20 anos para a frente a partir do ano atual. |
| `REGEX_MATCH` | Uma correspondência parcial: o padrão corresponde em qualquer parte do texto, não ao texto inteiro. |

`TO_TEXT` e os formatos de data são convertidos em uma etapa [Text Function](/pt-br/reference/workflow-steps/tables/table-text-function/). Uma edição que traz apenas as suas etapas compiladas, sem expressão, é convertida como essas etapas aplicadas em ordem, cada uma alimentando a seguinte, e o relatório de conversão informa a ordem que presumiu. O conversor recusa pelo nome o que o próprio Savant não consegue executar ou o que não tem nada a converter, e a etapa se torna um marcador: uma função de agregação simples ou de janela dentro de uma expressão de Transform ou Filter (dentro de um cálculo ou de um Summarize ela é convertida), `HASH` com um algoritmo literal diferente de `md5` ou `sha1`, uma construção de regex que o PlaidCloud não consegue ler (uma classe dentro de uma classe, uma interseção de classes ou uma propriedade `\p{}` desconhecida), uma edição de Transform sem expressão e sem etapas compiladas (como uma edição do Copilot que tem apenas o seu prompt), um caminho XML que não é XPath 1.0 e uma solicitação de API que leva uma credencial e obtém o host de um campo da linha. A [matriz de conversão do Savant](/pt-br/reference/savant-conversion-matrix/#recusas-nomeadas) lista cada um com o seu motivo.

As funções de expressão também são convertidas para `sha1`, `NOT_TRUE`, `LEVENSHTEIN`, as funções de horário de verão (`DST`) e as funções de expressão regular que recebem a n-ésima correspondência. `DAY_OF_WEEK` numera o domingo como 7, e `DAY_NAME` devolve o nome do dia.

## Ler o relatório de conversão

A resposta traz o relatório de conversão: um resumo de quantas etapas foram convertidas com confiança alta, média ou baixa e quantas não foram convertidas, além dos avisos e dos nós que o conversor absorveu em outros. Leia-o antes de executar o fluxo de trabalho. Ele nomeia todos os marcadores, todas as origens não vinculadas e vinculações sem correspondência, e o prefixo de tabela usado.

## Marcadores para configurações não convertidas

Uma configuração que o conversor não consegue reproduzir é criada como uma etapa de marcador que leva o nome do agente, e o relatório de conversão a nomeia. Um marcador aparece para uma construção que o conversor recusa pelo nome (consulte a [matriz de conversão do Savant](/pt-br/reference/savant-conversion-matrix/#recusas-nomeadas)) ou que a exportação não descreve por completo, como uma configuração de API ausente. Por padrão, um marcador falha quando o fluxo de trabalho chega a ele, de modo que uma execução não pode informar sucesso em um trabalho que nunca aconteceu.

Defina `allow_unconverted_placeholders` como `true` para importar cada marcador como uma etapa de passagem direta. A execução então continua após ele, e a saída do marcador é a sua entrada. Recrie a funcionalidade com uma etapa nativa quando o resultado dela for importante.

## Executar o fluxo de trabalho convertido

1. Abra o novo fluxo de trabalho no projeto.
2. Defina as variáveis de projeto que vieram dos parâmetros do Savant.
3. Carregue os arquivos das origens não vinculadas nos caminhos indicados no relatório.
4. Execute o fluxo de trabalho e revise a tabela de saída de cada etapa.

## Casos extremos

Estas são as únicas diferenças conhecidas em relação ao Savant. O relatório de conversão nomeia cada uma que se aplica.

- **Formatos de data.** `TO_DATE` ou `TO_DATETIME` com um formato que contém um literal `[`, `]`, `'`, `\` ou `^`, sobre um texto que lê como 9999-12-30 ou 9999-12-31, passa do último carimbo de data/hora que o data warehouse comporta, e o relatório gera um aviso.
- **Parâmetros secretos.** Um parâmetro cujo nome contém uma palavra de segredo, ou cujo valor se parece com uma credencial, se torna uma variável de projeto com valor em branco, por design. Defina o valor na variável.
- **Parâmetros não declarados.** Um parâmetro que um nó usa e que a exportação não declara chega como uma variável de projeto com valor vazio.
- **`JSON_FORMAT` no Snowflake.** Grava JSON compacto em uma única linha.
- **Ordem das linhas.** Os destinos Parquet, Google Sheets, Tableau e tabela ordenados não mantêm ordem de linhas.
- **Google Sheets e Tableau.** Publicar em qualquer um deles exige que a sua conta seja vinculada por meio de `destination_bindings`.

## Guias relacionados

- [Matriz de conversão do Savant](/pt-br/reference/savant-conversion-matrix/)
- [Conexão REST](/pt-br/reference/connectors/rest/generic-rest/)
- [Adicionar contas de documentos](/pt-br/guides/documents/adding-accounts/)
- [Gerenciar variáveis de fluxo de trabalho](/pt-br/guides/workflows/manage-workflow-variables/)
- [Etapa AI/NLP](/pt-br/reference/workflow-steps/text-documents/nlp-ai/)
- [Etapa Solicitação REST](/pt-br/guides/workflows/rest-request-step/)
- [Executar um fluxo de trabalho](/pt-br/guides/workflows/run-a-workflow/)
