---
title: Migrar projetos do Prophecy
description: Converta a exportação de um projeto do Prophecy em fluxos de trabalho do PlaidCloud pelo aplicativo Analyze, pela API REST ou por um agente de IA conectado por MCP, vincule seus conjuntos de dados e conexões e leia o relatório de conversão.
sidebar:
  order: 31.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-prophecy-projects.md
---

O PlaidCloud é um substituto direto do Prophecy. Todo gem do Prophecy é convertido em etapas nativas de fluxo de trabalho do PlaidCloud que executam o trabalho do gem: o conversor cria um fluxo de trabalho para cada pipeline Spark e um para o projeto SQL, mapeia cada gem para uma etapa de fluxo de trabalho, uma variável de projeto ou um objeto da tela, mantém o grafo original e devolve um relatório de conversão. Os poucos comportamentos que um fluxo de trabalho convertido não reproduz por conta própria estão listados em [Casos extremos](#casos-extremos).

A conversão lê somente a exportação que você indicar. Ela nunca se conecta ao sistema de onde um conjunto de dados do Prophecy lê ou onde grava, e nunca executa o código do projeto.

A conversão é uma operação única. Converter o mesmo projeto novamente cria novos fluxos de trabalho e tabelas, e as edições feitas no PlaidCloud nunca são mescladas com uma exportação posterior.

## O que o PlaidCloud cria

- Cada gem do Prophecy se torna a etapa de fluxo de trabalho correspondente, com as relações a montante e a jusante preservadas.
- Os parâmetros do Prophecy se tornam variáveis de projeto, e as referências a eles nas configurações dos gems são reescritas para a sintaxe de variáveis do PlaidCloud. Você pode substituir os valores dos parâmetros na conversão.
- Cada conjunto de dados que um gem lê se torna uma etapa de importação ou lê uma tabela ou um documento existente, dependendo de como você o vincula.
- Cada job do Prophecy ou agendamento de pipeline SQL se torna um [evento agendado](/pt-br/administration/scheduled-events/) no fluxo de trabalho convertido, ativado quando está ativado no Prophecy. Consulte [Agendamentos](#serviços-e-controle).
- Scripts, instruções SQL, macros e outros códigos do projeto chegam dentro de etapas que carregam o código. Consulte [Código do projeto nas etapas](#código-do-projeto-nas-etapas).
- Um gem personalizado, incluindo um gem do Gem Builder, executa em uma etapa Python o código que a exportação traz para ele. Consulte [Código do projeto nas etapas](#código-do-projeto-nas-etapas).
- Um gem Pivot com condição HAVING ou com uma coluna de todos os valores é convertido, assim como os tipos de ordenação e de Deduplicate que o Prophecy oferece.
- As expressões são convertidas assumindo o comportamento do Spark SQL para tratamento de nulos, divisão de inteiros e conversões implícitas. Verifique os resultados onde isso diferir no seu mecanismo do PlaidCloud.

## Antes de começar

1. Exporte o projeto do Prophecy como um arquivo `.zip`, ou exporte um único pipeline, modelo ou subgrafo como um arquivo `.json`.
2. Carregue o arquivo em uma [conta de documentos](/pt-br/guides/documents/adding-accounts/) que você possa ler.
3. Escolha o projeto do PlaidCloud que receberá os fluxos de trabalho. Você precisa ter acesso de gravação a ele.
4. Decida de onde os arquivos dos conjuntos de dados não vinculados serão lidos. Escolha uma conta de documentos e uma pasta base.

## Converter o projeto

Converta pelo aplicativo Analyze, pela API REST ou pelo catálogo de ferramentas MCP. Os três usam os mesmos campos.

### Aplicativo Analyze

1. Abra o **Analyze** e escolha **Tools → Importar projeto do Prophecy**.
2. Escolha o **Projeto de destino**, o **Projeto Prophecy (.zip ou .json)** que você carregou em uma conta de documentos e o **Local dos arquivos de origem**, a conta de documentos e a pasta base de onde os arquivos dos conjuntos de dados não vinculados são lidos.
3. Em **Nomes de objetos e opções**, defina, se quiser, prefixos de fluxo de trabalho, de etapa e de tabela, escolha o **Tipo de fluxo de trabalho** e escolha se os componentes não convertidos serão importados como marcadores de passagem direta.
4. Em **Vínculos de origem e parâmetros**, vincule, se quiser, um conjunto de dados a uma tabela existente informando o nome do conjunto de dados e o ID da tabela, e substitua parâmetros do Prophecy pelo nome. Para vincular conexões, use a API REST ou a ferramenta MCP. Consulte [Vincular conexões](#vincular-conexões).
5. Selecione **Importar**.

A janela mostra o andamento enquanto lê o projeto, analisa os pipelines, os mapeia para operações do PlaidCloud e cria os fluxos de trabalho, as tabelas e as etapas. Ao terminar, a janela mostra o relatório de conversão: contagem de etapas por nível de confiança, avisos, conversões parciais, marcadores não convertidos, componentes descartados e os arquivos de origem a carregar.

### Campos

A API REST e a ferramenta MCP usam estes campos.

| Campo | Obrigatório | O que faz |
| --- | --- | --- |
| `source_account_id` | Sim | Conta de documentos que contém a exportação do Prophecy. |
| `source_file_path` | Sim | Caminho do `.zip` do projeto, ou de um arquivo `.json` de um pipeline, modelo ou subgrafo, dentro dessa conta. |
| `project_id` | Sim | Projeto em que os fluxos de trabalho são criados. |
| `document_account_id` | Sim | Conta de documentos da qual os conjuntos de dados não vinculados são lidos. |
| `document_account_path` | Sim | Pasta base, nessa conta, para os conjuntos de dados não vinculados. Um valor vazio ou `/` é a raiz da conta, e uma `/` inicial é ignorada. Caminhos com `..` ou segmentos iniciados por ponto, chaves, letra de unidade ou esquema de URL, ou caracteres de controle são recusados. |
| `workflow_prefix` | Não | Prefixo adicionado aos nomes dos fluxos de trabalho. |
| `step_prefix` | Não | Prefixo adicionado aos nomes das etapas. |
| `table_prefix` | Não | Prefixo adicionado aos nomes das tabelas. O padrão é o próprio nome do fluxo de trabalho. Um prefixo que reutilizaria o nome de uma tabela existente é recusado antes que qualquer coisa seja criada. O prefixo usado é devolvido no relatório de conversão. |
| `workflow_type` | Não | `advanced` (padrão) distribui o grafo na tela de DAG. `standard` produz uma lista serial de etapas. |
| `source_bindings` | Não | Vincula conjuntos de dados e operações a dados existentes. Consulte [Vincular origens](#vincular-origens). |
| `connection_bindings` | Não | Vincula os bancos de dados, armazenamentos de arquivos, APIs REST e e-mails que um projeto acessa a conexões e contas de documentos do PlaidCloud. Consulte [Vincular conexões](#vincular-conexões). |
| `parameters` | Não | Substitui parâmetros do Prophecy. Consulte [Parâmetros](#parâmetros). |
| `allow_unconverted_placeholders` | Não | Controla o que um marcador faz durante a execução. Consulte [Marcadores para gems não convertidos](#marcadores-para-gems-não-convertidos). |

### REST

Envie os campos como um corpo JSON para:

```text
POST /rest/v1/analyze/prophecy/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/prophecy/customer-360.zip",
  "project_id": "<project id>",
  "document_account_id": "<document account id>",
  "document_account_path": "/prophecy-inputs"
}
```

Você precisa da função `analyze.workflow.write`.

### MCP

Um agente de IA conectado por MCP chama a ferramenta `prophecy_convert` com os mesmos campos. Consulte [Agentes de IA (MCP)](/pt-br/integrations/ai-coding-agents/) para conectar um agente. A ferramenta altera o seu projeto, portanto revise a chamada antes de aprová-la.

## Vincular origens

Uma exportação do Prophecy descreve de onde seus dados vêm, mas não traz dados nem credenciais. Use `source_bindings` para conectar cada conjunto de dados aos dados que você já tem no PlaidCloud. A chave é o nome do conjunto de dados como o relatório de conversão o lista. O valor é um destes:

- Um ID `analyzetable_` de uma tabela do projeto de destino. O fluxo de trabalho convertido lê essa tabela diretamente.
- Um objeto com `account`, `path` e, opcionalmente, `sheet`, para ler um arquivo de uma conta de documentos.

```json
"source_bindings": {
  "customers": "analyzetable_1234",
  "budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Uma vinculação que você não pode ler é recusada. Uma chave que não corresponde a nenhum conjunto de dados é informada como aviso. A janela do Analyze vincula conjuntos de dados a tabelas; use a API REST ou a ferramenta MCP para vincular um conjunto de dados a um arquivo de documento.

### Conjuntos de dados não vinculados

Um conjunto de dados sem vinculação se torna uma etapa de importação ainda sem dados, e o relatório de conversão traz um aviso para ele. A etapa lê de:

```text
<document_account_path>/prophecy/<workflow id>/<dataset name>.csv
```

Carregue o arquivo nesse caminho e execute o fluxo de trabalho. Enquanto o arquivo não estiver lá, a etapa de importação termina com um aviso e cria uma tabela vazia, e o fluxo de trabalho continua. O relatório lista cada caminho em **Arquivos de origem a carregar**.

### Vincular operações de tabela e de arquivo

Gems que alteram tabelas ou arquivos, como Table Operations (update, delete, drop) e File Operation (copy), atuam somente sobre dados que a conversão criou. Para fazer um deles atuar sobre dados que já existem, vincule-os com uma chave no formato `operation:<pipeline>/<id>`, em que `<pipeline>` é o nome do pipeline e `<id>` é o ID do gem. O relatório de conversão informa a chave de cada um desses gems.

```json
"source_bindings": {
  "operation:daily_load/Operation_1": "analyzetable_5678"
}
```

Uma operação destrutiva de tabela ou de arquivo só é executada quando você a vincula. Sem vinculação, um gem Table Operations atua sobre uma tabela gravada por outro gem do mesmo projeto e, caso contrário, se torna um marcador que informa a sua chave. Um gem File Operation copia da sua própria pasta de preparação. Nada fora das tabelas e pastas da própria conversão é alterado, a menos que você o vincule.

## Vincular conexões

Um projeto do Prophecy acessa bancos de dados, armazenamentos de arquivos, APIs REST e servidores de e-mail por meio de conexões. A exportação traz os nomes das conexões, mas não as credenciais; por isso, use `connection_bindings` para apontar cada uma para uma conexão do PlaidCloud ou uma conta de documentos que você já tenha. O relatório de conversão lista todas as chaves em suas vinculações.

```json
"connection_bindings": {
  "connection:warehouse_pg": "<connection id>",
  "connection:landing_s3": "<document account id>",
  "operation:daily_load/Email_1": "<connection id>"
}
```

Uma chave é uma destas:

| Chave | Vincula | Valor |
| --- | --- | --- |
| `connection:<name>` | A conexão do Prophecy que um gem ou conjunto de dados de banco de dados nomeia. Uma vinculação atende a todos os gems dessa conexão. Um gem que não nomeia nenhuma conexão usa `connection:<pipeline>/<gem id>`, e um conjunto de dados de banco de dados usa `connection:<dataset name>`. | Um ID de conexão do PlaidCloud: uma conexão de banco de dados (BigQuery e SAP HANA incluídos), uma conexão MongoDB ou Apache Kafka, uma conexão Salesforce para leituras e gravações do Salesforce, uma conexão Tableau para um gem do Tableau, uma conexão REST para Azure Cosmos DB, Pinecone, Power BI e gravações do Smartsheet e do Slack, ou uma conexão baseada em Singer para leituras do Smartsheet, do Slack e do Iceberg. Um ID de conta de documentos para um gem File Storage ou Directory. |
| `operation:<pipeline>/<gem id>` | Um gem REST que envia qualquer método além de GET, HEAD ou OPTIONS, e todo gem Email. | Um ID de conexão. Para REST, uma conexão REST que contém a credencial. |

A vinculação é o seu consentimento para gems que alteram coisas fora da conversão:

- Uma solicitação REST que pode alterar o que a API armazena, e um e-mail que chega a pessoas reais, são convertidos em etapas funcionais somente quando você vincula a chave `operation:` correspondente. Sem vinculação, o gem é um marcador que informa a chave.
- Uma conta de documentos vinculada a um gem File Storage ou Directory permite que as etapas desse gem gravem, excluam ou movam arquivos nessa conta.
- Uma solicitação GET, HEAD ou OPTIONS é enviada como o gem a envia. Sem vinculação, ela fica sem credencial até que você selecione uma conexão REST na etapa convertida.

Um conjunto de dados de banco de dados ou um gem External Table sem vinculação é convertido em uma etapa que informa a sua chave e aguarda você selecionar uma conexão, e o relatório traz um aviso. Converta novamente com a chave vinculada ou selecione a conexão na etapa. Uma vinculação cujo ID é o tipo errado de armazenamento para os seus gems, ou que você não pode usar, é recusada. Uma chave que não corresponde a nada é informada como aviso.

## Parâmetros

`parameters` substitui parâmetros do Prophecy na conversão:

```json
"parameters": {
  "instance": "prod",
  "values": { "run_date": "2026-10-01", "region": "EMEA" },
  "pipelines": {
    "daily_load": { "instance": "prod", "values": { "region": "APAC" } }
  }
}
```

`instance` nomeia uma instância de configuração. `values` são textos, números ou booleanos. Uma entrada de pipeline substitui os valores do projeto inteiro para esse pipeline. O relatório lista os parâmetros usados e os que foram renomeados para se ajustar aos nomes de variáveis do PlaidCloud.

## Ler o relatório de conversão

A resposta traz o relatório de conversão. Leia-o antes de executar os fluxos de trabalho.

| Seção | O que ela informa |
| --- | --- |
| Resumo | Quantas etapas foram convertidas com confiança alta, média ou baixa e quantas não foram convertidas. |
| Avisos | Tudo o que o conversor presumiu, aproximou ou ignorou, incluindo conjuntos de dados não vinculados e chaves de vinculação que não corresponderam a nada. |
| Conversões parciais | Etapas que são convertidas, mas diferem do gem em algum modo ou opção. Cada uma traz uma observação sobre o que verificar. |
| Marcadores não convertidos | Gems sem equivalente no PlaidCloud, com o motivo. |
| Componentes descartados | Gems que não carregam trabalho próprio, como marcadores de limite de fluxo de controle, e a etapa que absorveu cada um. |
| Arquivos de origem a carregar | O caminho de documento de onde cada conjunto de dados não vinculado lê. |
| Fluxos de trabalho | O fluxo de trabalho criado para cada pipeline, na ordem de execução. Um pipeline que o conversor recusou é marcado. |

O relatório também informa o prefixo de tabela usado e os parâmetros aplicados. Uma etapa sobre a qual o conversor não tem certeza é convertida para a leitura mais provável e traz uma observação no relatório. Confira essas etapas com a saída do seu Prophecy.

## Código do projeto nas etapas

Os projetos do Prophecy carregam código: gems Script, instruções SQL, macros, entradas dinâmicas, chamadas de procedures armazenadas e gems personalizados. O conversor não executa esse código. Ele o coloca dentro de uma etapa:

- O SQL é traduzido para o dialeto SQL do seu tenant e colocado em uma etapa SQL, com as entradas do gem disponíveis sob os nomes pelos quais a consulta as lê.
- Os scripts Python são colocados em uma etapa Python, com o acesso a tabelas reescrito. Um script que chama métodos de data frame do Spark mantém essas chamadas e as executa na etapa.
- Um gem personalizado, incluindo um gem do Gem Builder, executa em uma etapa Python o código PySpark que a exportação do seu pipeline traz para ele.
- Uma macro de um pacote dbt conhecido se torna as etapas padrão que fazem o que a macro faz. Uma macro do seu próprio projeto, ou de um pacote incluído na exportação, também é lida e convertida, incluindo blocos if e for, set, filtros, macros aninhadas e despacho de adaptador.
- Uma função de agregação definida pelo usuário em Python, em um gem Aggregate, é executada em uma etapa Python para cada grupo.

Toda etapa que carrega código do projeto recebe um aviso, assim como o SQL traduzido. Revise o código de cada uma dessas etapas antes de executar o fluxo de trabalho. O conversor retém qualquer coisa que pareça uma credencial encontrada em cadeias de caracteres e comentários do código; portanto, adicione as credenciais a uma conexão, e não ao código.

## Marcadores para gems não convertidos

Um gem que o conversor não consegue reproduzir é criado como uma etapa de marcador que leva o nome do gem. Exemplos são um gem personalizado cujo código não está na exportação e um gem que altera dados fora da conversão, como uma solicitação REST que pode alterar dados, um Email ou uma operação de tabela ou de arquivo, quando você não vinculou a chave `operation:` dele. Um conjunto de dados de banco de dados ou um External Table sem conexão vinculada não é um marcador: ele é convertido em uma etapa que aguarda você selecionar uma conexão. Por padrão, um marcador falha quando o fluxo de trabalho chega a ele, de modo que uma execução não pode informar sucesso em um trabalho que nunca aconteceu.

Defina `allow_unconverted_placeholders` como `true` (na janela, **Importar componentes não convertidos como marcadores de passagem direta**) para importar cada marcador como uma etapa de passagem direta. A execução então continua após ele, e a saída do marcador é a sua entrada. O relatório conta os marcadores de passagem direta e lista as suas etapas. Recrie a funcionalidade com uma etapa nativa quando o resultado dela for importante.

## Executar os fluxos de trabalho convertidos

1. Abra os novos fluxos de trabalho no projeto. O relatório os lista na ordem de execução.
2. Defina as variáveis de projeto que vieram dos parâmetros do Prophecy.
3. Carregue os arquivos dos conjuntos de dados não vinculados nos caminhos indicados no relatório.
4. Revise as etapas que carregam código do projeto.
5. Execute os fluxos de trabalho e revise a tabela de saída de cada etapa.

Os eventos agendados criados a partir dos agendamentos do Prophecy ficam ativados quando estavam ativados no Prophecy, portanto começam a executar os fluxos de trabalho convertidos conforme o agendamento. Para revisar os fluxos de trabalho primeiro, desative os eventos em [Eventos agendados](/pt-br/administration/scheduled-events/) e ative-os quando estiver pronto.

## O que é convertido

Todo gem do Prophecy é convertido por completo em etapas nativas, variáveis de projeto, eventos agendados ou objetos da tela, com as opções que ele oferece. A [matriz de conversão do Prophecy](/pt-br/reference/prophecy-conversion-matrix/) lista cada gem com a etapa do PlaidCloud em que ele se torna, e os [Casos extremos](#casos-extremos) listam os poucos comportamentos a verificar; o relatório de conversão informa cada um onde ele ocorre.

### Movimentação de dados

| Funcionalidade | Como é convertida |
| --- | --- |
| Modos de gravação | Os modos de gravação de destino são convertidos em etapas da plataforma: SCD2 com as estratégias de verificação e de carimbo de data/hora (a estratégia de carimbo de data/hora data cada versão a partir da coluna que o `scd2.updatedAtColumn` do gem nomeia), merge, `replaceWhere` e `insertInto`. Um merge aplica as expressões SET por coluna de suas cláusulas de atualização por correspondência e de inserção sem correspondência; uma cláusula que não define nenhuma coluna usa todas as colunas da linha recebida. A primeira execução em um destino vazio grava todas as linhas, como fazem o dbt e o Delta. A primeira execução não precisa de uma tabela criada previamente, inclusive para um pipeline que lê um conjunto de dados que ele também grava, a menos que a exportação não informe quais colunas esse conjunto de dados tem: nesse caso, crie a tabela antes da primeira execução. As execuções seguintes aplicam o filtro incremental ou a condição de merge. Os modos `error` e `ignore` verificam com a [condição de existência de tabela](/pt-br/guides/workflows/step-conditions/#condições-de-existência-de-tabela). |
| Time travel | Uma origem de tabela Delta ou de catálogo que lê uma versão anterior da tabela, por `versionAsOf` ou `timestampAsOf`, lê essa versão do Databricks pela conexão que você vincular. |
| Streaming | Origens e destinos de streaming são executados como lotes agendados. O destino de streaming substitui a sua tabela em vez de acrescentar, de modo que uma nova execução nunca duplica linhas. Agende o fluxo de trabalho para capturar os dados recém-chegados. |
| Bancos de dados | Os gems JDBC, Snowflake, Redshift, Hive, BigQuery, SAP HANA e External Table leem e gravam pela conexão do PlaidCloud que você vincular. Um conjunto de dados do BigQuery é lido com [Importar SQL](/pt-br/reference/workflow-steps/import/import-sql/) e gravado com [Export External Database Tables](/pt-br/reference/workflow-steps/export/export-external-tables/) (etapa) em uma [conexão BigQuery](/pt-br/reference/connectors/google/big-query/). Uma tabela SAP HANA gravada em qualquer um dos modos de merge do gem HANA, incluindo SCD2 e os modos de exclusão, é preparada ao lado do destino e mesclada nele pela chave primária do destino ou pelas colunas de merge do gem; um destino ausente é criado primeiro. |
| MongoDB e Kafka | Um conjunto de dados do MongoDB é lido com [Importar MongoDB](/pt-br/reference/workflow-steps/import/import-mongodb/), incluindo o seu filtro ou pipeline de agregação, e uma leitura que não declara colunas toma as colunas dos primeiros documentos, como faz o conector do Spark. Uma gravação usa [Exportar MongoDB](/pt-br/reference/workflow-steps/export/export-mongodb/) no modo de gravação correspondente: `update` atualiza os campos do documento correspondente ou insere um, `ignore` grava somente enquanto a coleção não contiver documentos e `error` interrompe a execução quando ela contiver um. Uma origem Kafka lê seus tópicos entre os deslocamentos inicial e final com [Importar Kafka](/pt-br/reference/workflow-steps/import/import-kafka/), e um destino Kafka envia cada linha com [Exportar Kafka](/pt-br/reference/workflow-steps/export/export-kafka/). Um conjunto de dados Kafka que se autentica com `OAUTHBEARER` usa o [login OAuth](/pt-br/reference/connectors/databases/apache-kafka/#oauth-oauthbearer) da conexão Kafka que você vincular, porque a exportação não traz credenciais. |
| Azure Cosmos DB | Uma leitura envia a consulta do conjunto de dados, ou lê todos os documentos, com [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) em uma conexão REST com autenticação do Cosmos DB, e segue o cabeçalho de continuação de uma página para a outra. Uma gravação envia uma solicitação para cada linha conforme a estratégia de gravação do gem: sobrescrever, acrescentar, excluir ou aplicar patch. Uma linha que traz o ETag do seu documento é substituída ou excluída somente se o documento não tiver mudado desde então, e uma linha que o contêiner recusa por esse motivo, ou por um documento ausente ou existente, é ignorada, como faz o conector do Spark. O modo `ignore` grava somente enquanto o contêiner não contiver documentos. |
| Salesforce | Uma leitura usa [Salesforce: Consultar objeto](/pt-br/reference/workflow-steps/salesforce/query-salesforce-object/), incluindo registros excluídos e arquivados quando o gem os solicita. Uma gravação insere, atualiza, faz upsert ou exclui, com uma solicitação para cada linha; um upsert corresponde pelo campo de ID externo do gem, ou `Id` quando ele não nomeia nenhum. |
| Smartsheet, Slack e Pinecone | Uma leitura do Smartsheet de uma planilha nomeada com colunas declaradas busca a planilha pela sua conexão REST e grava uma linha para cada linha da planilha e uma coluna para cada coluna declarada. As outras leituras do Smartsheet, e as leituras do Slack e do Iceberg, usam a etapa [Import Singer Source](/pt-br/reference/workflow-steps/import/import-singer/). Uma gravação no Smartsheet adiciona as linhas à planilha nomeada, e uma sobrescrita exclui primeiro as linhas da planilha. Uma gravação no Slack publica uma mensagem para cada linha, e uma mensagem que o Slack recusa faz a etapa falhar. Um índice do Pinecone é lido como seus vetores e metadados, e uma gravação faz upsert das linhas como vetores. |
| Tableau e Power BI | Tableau e Tableau Write publicam a entrada como uma extração Hyper por meio de [Publish to Tableau](/pt-br/reference/workflow-steps/export/export-to-tableau/) (etapa) na conexão Tableau que você vincular. Power BI Write envia as entradas para um conjunto de dados push do Power BI por meio de uma conexão REST com OAuth 2.0, localizando o workspace pelo nome e criando o conjunto de dados quando ele é novo. |
| Formatos de arquivo | CSV, JSON, Parquet, Avro, Excel, XML, largura fixa e ORC por meio de [Importar ORC](/pt-br/reference/workflow-steps/import/import-orc/). As opções de formato são mapeadas ou marcadas como neutras quando não alteram nenhuma linha: a janela de data de modificação de uma leitura Avro, a codificação EBCDIC de um arquivo de largura fixa, registros de cabeçalho e rodapé e registros sem quebras de linha, o mapa de planilhas e a senha de uma leitura do Excel, as opções de aspas de uma gravação CSV e uma gravação do Excel com uma planilha para cada valor. Arquivos de texto compactados são lidos e gravados com gzip, Deflate (zlib), Zstandard, LZ4, Snappy e LZO; um arquivo compactado é lido quando o nome termina com a extensão do seu codec. Arquivos criptografados são descriptografados e criptografados no local. Consulte [Arquivos criptografados](#arquivos-criptografados). |
| File Operation | Copy e Move são convertidos em [Documento: Copiar arquivo](/pt-br/reference/workflow-steps/document/copy-document-file/) ou Copy Directory na pasta que você vincular, mantendo apenas os arquivos cujo nome corresponde ao `filenameRegex` do gem e mantendo o caminho de cada arquivo abaixo da pasta de origem quando o gem é recursivo. |
| Directory | Lista os arquivos da pasta de documentos vinculada com [Listagem de diretório](/pt-br/reference/workflow-steps/document/directory-listing/), nas colunas do gem. Com a opção de nome da planilha ativada, cada pasta de trabalho do Excel gera uma linha por planilha e o seu `sheet_name`; os outros arquivos geram uma linha com `sheet_name` vazio. |

### Colunas e linhas

| Gem ou função | Como é convertido |
| --- | --- |
| Surrogate Key | As chaves continuam a partir de uma tabela que guarda a última chave emitida, como faz o arquivo de chaves do gem. Todo gem que nomeia o mesmo arquivo de chaves compartilha essa tabela, de modo que suas chaves nunca se sobrepõem. Uma execução sem linhas a deixa como estava, e as chaves começam do valor inicial antes de qualquer execução ter emitido uma. |
| Column Parser, XML Parse, análise de JSON | Textos XML e JSON são analisados com as etapas [Análise de XML](/pt-br/reference/workflow-steps/tables/table-xml-parse/) e [Analisar JSON](/pt-br/reference/workflow-steps/tables/table-json-parse/), lendo cada campo do texto do elemento, de um atributo ou de um elemento filho. Um XML analisado sem esquema toma o tipo de cada campo dos dados, como faz o `schema_of_xml` do Spark. |
| Regras de negócio | Uma regra de negócio do projeto chamada em uma expressão é convertida nas mesmas condições, um `CASE` para cada coluna que ela define. |
| Conversões de tipo (casts) | Um cast de texto para decimal ou long segue exatamente o Spark: espaços e caracteres de controle ao redor do número são removidos, um decimal arredonda meio para cima até a sua escala, e um texto que não é um número, ou um valor fora do intervalo, vira nulo. |
| Datas e horas | Os formatos de data e hora são escritos para o mecanismo do seu espaço de trabalho, Databend incluído, e `window()` posiciona cada carimbo de data/hora em sua janela deslizante (tumbling), alinhada como o Spark a alinha. |
| Saídas de iteradores | Um Table Iterator ou While Iterator cujas colunas de saída só são conhecidas durante a execução reúne as linhas de cada passagem por posição com [Tabela: União total](/pt-br/reference/workflow-steps/tables/table-union-all/#correspondência-de-colunas), com cada coluna ampliada para um tipo que todas as passagens comportem, como o Prophecy empilha as passagens. |
| Data Encoder/Decoder AES | Executa em todos os mecanismos. A chave e, quando o gem os nomeia, o vetor de inicialização e os dados adicionais vêm das variáveis de fluxo de trabalho `aes_key`, `aes_iv` e `aes_aad`, que você define. |
| Hash do Data Masking | Calcula os mesmos valores que o `hash()` do Spark. |
| Buffer, Simplify, Heat Map | O Buffer desenha um canto arredondado com o mesmo número de segmentos que o Prophecy, o Simplify descarta os mesmos vértices, e o Heat Map soma o calor em hexágonos H3 na resolução do gem, com um calor decimal permanecendo decimal. |

### Serviços e controle

| Gem | Como é convertido |
| --- | --- |
| Pipeline | Executa o pipeline que ele nomeia com um [Workflow Loop](/pt-br/reference/workflow-steps/workflow-control/workflow-loop/) (etapa), uma vez para cada linha de entrada (uma vez quando não há entrada, nunca quando não há linhas), com cada parâmetro definido a partir de uma constante, de uma coluna da linha ou de uma expressão sobre ela. Cada execução prossegue mesmo quando uma anterior falha, e a saída do gem tem uma linha para cada execução com seu status, mensagem e horários, como o Prophecy os registra. |
| Agendamentos | Um job do Prophecy ou agendamento de pipeline SQL se torna um [evento agendado](/pt-br/administration/scheduled-events/) chamado `Prophecy <name>` no fluxo de trabalho convertido, ativado a menos que esteja desativado no Prophecy. Um job Spark é convertido dessa forma quando executa um pipeline convertido sem substituições de configuração nem condições de execução. |
| Script | Um script Python é colocado em uma etapa Python. Um valor que o script define em `Config` se torna uma variável de fluxo de trabalho que as etapas seguintes leem, redefinida para o valor do pipeline no início de cada execução, como o `Config` do Prophecy. |
| REST API, REST API Enrich | Etapas [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/), uma solicitação para cada linha de entrada, mantendo uma resposta de erro como faz o Prophecy. O Enrich também lê o status, o motivo e a URL final. Uma solicitação que aguarda um resultado assíncrono consulta repetidamente até a resposta indicar que terminou. |
| Stored Procedure | Um gem que passa argumentos chama a sua procedure com [Execução remota: SQL](/pt-br/reference/workflow-steps/agent/agent-remote-execution-of-sql/#executar-uma-instrução-uma-vez-por-linha) uma vez para cada linha de entrada, com cada argumento vinculado a partir da sua coluna como um parâmetro. Um gem sem argumentos a chama uma vez por meio de um agente. Escolha a conexão ou o agente na etapa convertida. |
| Email, Email Data | [Notify Via Email](/pt-br/reference/workflow-steps/notifications/notify-via-email/) (etapa) com Cc, Cco, Responder para e uma mensagem para cada linha quando um campo é lido de uma coluna. |
| OpenAI, Bedrock, SageMaker Endpoint | [Text: NLP (AI)](/pt-br/reference/workflow-steps/text-documents/nlp-ai/) (etapa) na conexão de LLM do seu espaço de trabalho. Os embeddings do OpenAI e do Bedrock usam a tarefa Embed, que exige uma conexão compatível com OpenAI ou Azure OpenAI; uma conexão Anthropic é recusada. |
| Pinecone Lookup | Uma solicitação REST para cada linha. |
| Data Quality Check, Deequ, Soda | As verificações são executadas no data warehouse e gravam a tabela de resultados. Um Data Quality Check interrompe a execução somente quando o gem define `minFailedChecks` ou uma ação posterior `fail_pipeline`; caso contrário, a tabela de resultados lista as falhas. Deequ e Soda nunca interrompem a execução. Uma verificação de comprimento mínimo ou máximo em uma coluna numérica mede o número como texto. As verificações do Soda são convertidas a partir do YAML do projeto, incluindo valores ausentes, inválidos e válidos, estatísticas, comprimentos, percentis, duplicidades entre colunas, atualidade, linhas com falha e as suas próprias consultas de métricas. |
| ToDo | Gera um erro que informa a ferramenta original e a mensagem quando a execução chega a ele. |

### Arquivos criptografados

Um gem File Storage que lê um arquivo criptografado é convertido em [Documento: descriptografar arquivo](/pt-br/reference/workflow-steps/document/encrypt-decrypt-file/), que descriptografa o arquivo em uma pasta própria antes de a importação lê-lo; a cópia descriptografada é removida depois. Um gem que grava um arquivo criptografado exporta para essa pasta e depois criptografa o arquivo no destino com Documento: criptografar arquivo. Arquivos AES e Blowfish e pastas de trabalho do Excel protegidas por senha são cobertos.

A exportação nunca traz uma chave; por isso, as etapas convertidas a leem de uma variável de fluxo de trabalho: `aes_key` para uma chave AES ou Blowfish, e `xlsx_password` para a senha de uma pasta de trabalho. Defina a variável antes de executar o fluxo de trabalho e use uma chave destinada somente a esses arquivos. Os campos de chave e de senha aceitam apenas uma referência de variável, de modo que uma chave nunca é digitada em uma etapa.

## Casos extremos

Estes são os comportamentos que um fluxo de trabalho convertido não reproduz por conta própria. O relatório de conversão informa cada um onde ele ocorre.

- **Código ou dados que a exportação não inclui**: um gem do Gem Builder ou outro gem personalizado cujo código não está na exportação, e uma chamada a uma macro de um pacote dbt que a exportação deixa de fora, se tornam uma etapa que informa o que está faltando; exporte o projeto com o código dos pipelines e os pacotes dbt, ou recrie a lógica em uma etapa Python ou SQL. Os gems Ab Initio Error Detection e MTime repassam a sua entrada, porque a regra que eles aplicam não está na exportação. As verificações do Soda lidas de um arquivo fora do projeto, e as verificações do Soda que comparam com varreduras anteriores ou com outro conjunto de dados, ou que testam um formato que o Soda nomeia, não têm linha na tabela de resultados; calcule-as em uma etapa posterior.
- **Resultados conhecidos apenas quando o pipeline é executado**: um gem REST API que achata a sua resposta coloca a resposta inteira em uma única coluna quando nada declara os nomes dos campos, o que só uma execução revela; extraia os campos de que você precisa em uma etapa posterior. Uma macro dbt que consulta o data warehouse enquanto o dbt compila se torna uma etapa que a nomeia; substitua a consulta pelos valores que ela devolve. Um gem StoredProcedure do Spark é executado, mas os seus valores OUT não são devolvidos; a saída são as colunas repassadas. `input_file_name()` devolve uma cadeia vazia sobre uma origem de tabela ou Delta, que não tem arquivo a nomear, e `hash()` / `xxhash64()` dentro de uma agregação, uma janela ou um gem com várias entradas são calculados pelo data warehouse, portanto podem diferir dos do Spark.
- **Valores gravados em uma etapa quando o projeto é convertido**: um valor de parâmetro que contém aspas, barra invertida ou chave, um valor de pipeline que uma etapa SQL lê e o banco de dados que uma operação de tabela Delta nomeia por configuração são gravados na etapa como valores fixos, portanto alterar a variável de fluxo de trabalho não os altera; edite a etapa quando a configuração mudar.
- **Código Scala**: um script Scala, uma expressão Scala ou uma função definida pelo usuário ou função de agregação em Scala se torna uma etapa que a nomeia; reescreva-a em SQL ou Python.
- **Login Kerberos do Kafka**: uma origem ou um destino Kafka que se autentica com Kerberos (GSSAPI) é convertido sem o nome do serviço Kerberos e o mecanismo de login; defina-os na conexão do PlaidCloud.
- **Streaming**: origens, destinos e pipelines de streaming são executados como fluxos de trabalho em lote sobre os dados presentes no momento da execução; agende o fluxo de trabalho para ser executado com a frequência de que você precisar.
- **Componentes de job**: um job Spark converte o seu único pipeline e agendamento; os seus outros componentes, condições de execução e substituições de configuração não são convertidos.
- **Chamadas incomuns**: uma função de agregação definida pelo usuário chamada a partir de um rollup ou de uma janela, e uma macro dbt que usa Jinja além de if, for, set e dos filtros comuns, se tornam uma etapa que nomeia o gem; chame a função a partir de um gem Aggregate ou incorpore a macro diretamente.

## Guias relacionados

- [Migrar análises do Savant](/pt-br/guides/workflows/migrate-savant-analyses/)
- [Migrar fluxos de trabalho do Alteryx](/pt-br/guides/workflows/migrate-alteryx-workflows/)
- [Adicionar contas de documentos](/pt-br/guides/documents/adding-accounts/)
- [Gerenciar variáveis de fluxo de trabalho](/pt-br/guides/workflows/manage-workflow-variables/)
- [Executar um fluxo de trabalho](/pt-br/guides/workflows/run-a-workflow/)
