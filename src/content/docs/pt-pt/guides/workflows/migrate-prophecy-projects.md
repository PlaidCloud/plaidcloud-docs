---
title: Migrar projetos Prophecy
description: Converta uma exportação de um projeto Prophecy em fluxos de trabalho do PlaidCloud a partir da aplicação Analyze, da API REST ou de um agente de IA ligado por MCP, associe os respetivos conjuntos de dados e ligações e leia o relatório de conversão.
sidebar:
  order: 31.5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-prophecy-projects.md
---

O PlaidCloud é um substituto direto do Prophecy. Cada gem do Prophecy é convertido em passos nativos de fluxo de trabalho do PlaidCloud que executam o trabalho do gem: o conversor cria um fluxo de trabalho por cada pipeline Spark e um para o projeto SQL, mapeia cada gem para um passo de fluxo de trabalho, uma variável de projeto ou um objeto da área de desenho, mantém o grafo original e devolve um relatório de conversão. Os poucos comportamentos que um fluxo de trabalho convertido não reproduz por si só estão indicados em [Casos limite](#casos-limite).

A conversão lê apenas a exportação que indicar. Nunca contacta o sistema de que um conjunto de dados do Prophecy lê nem para o qual escreve, e nunca executa o código do projeto.

A conversão é um passo único. Converter novamente o mesmo projeto cria novos fluxos de trabalho e tabelas, e as alterações que tenha feito no PlaidCloud nunca são combinadas com uma exportação posterior.

## O que o PlaidCloud cria

- Cada gem do Prophecy torna-se o passo de fluxo de trabalho correspondente, com as relações a montante e a jusante preservadas.
- Os parâmetros do Prophecy tornam-se variáveis de projeto, e as referências a eles nas definições dos gems são reescritas para a sintaxe de variáveis do PlaidCloud. Pode substituir os valores dos parâmetros na conversão.
- Cada conjunto de dados que um gem lê torna-se um passo de importação, ou lê uma tabela ou um documento existente, consoante a forma como o associar.
- Cada tarefa do Prophecy ou agendamento de pipeline SQL torna-se um [evento agendado](/pt-pt/administration/scheduled-events/) no fluxo de trabalho convertido, ativado se estiver ativado no Prophecy. Consulte [Agendamentos](#serviços-e-controlo).
- Os scripts, as instruções SQL, as macros e outro código do projeto chegam dentro de passos que transportam o código. Consulte [Código do projeto nos passos](#código-do-projeto-nos-passos).
- Um gem personalizado, incluindo um gem do Gem Builder, executa num passo Python o código que a exportação transporta para ele. Consulte [Código do projeto nos passos](#código-do-projeto-nos-passos).
- Um gem Pivot com uma condição HAVING ou uma coluna de todos os valores é convertido, tal como os tipos de ordenação e de Deduplicate que o Prophecy oferece.
- As expressões são convertidas partindo do princípio do comportamento do Spark SQL no tratamento de nulos, na divisão de inteiros e nas conversões implícitas. Verifique os resultados nos casos em que isso difere no seu motor PlaidCloud.

## Antes de começar

1. Exporte o projeto do Prophecy como ficheiro `.zip`, ou exporte um único pipeline, modelo ou subgrafo como ficheiro `.json`.
2. Carregue o ficheiro para uma [conta de documentos](/pt-pt/guides/documents/adding-accounts/) que possa ler.
3. Escolha o projeto do PlaidCloud que deve receber os fluxos de trabalho. Precisa de acesso de escrita ao mesmo.
4. Decida de onde são lidos os ficheiros dos conjuntos de dados não associados. Escolha uma conta de documentos e uma pasta de base.

## Converter o projeto

Converta a partir da aplicação Analyze, da API REST ou do catálogo de ferramentas MCP. Os três aceitam os mesmos campos.

### Aplicação Analyze

1. Abra **Analisar** e escolha **Tools → Importar projeto Prophecy**.
2. Escolha o **Projeto de destino**, o **Projeto Prophecy (.zip ou .json)** que carregou para uma conta de documentos e a **Localização dos ficheiros de origem**, a conta de documentos e a pasta de base de onde são lidos os ficheiros dos conjuntos de dados não associados.
3. Em **Nomes de objetos e opções**, defina opcionalmente prefixos para fluxos de trabalho, passos e tabelas, escolha o **Tipo de fluxo de trabalho** e indique se pretende importar componentes não convertidos como marcadores de posição de passagem direta.
4. Em **Source Bindings and Parameters**, pode associar um conjunto de dados a uma tabela existente indicando o nome do conjunto de dados e o ID da tabela, e substituir os parâmetros do Prophecy por nome. Para associar ligações, utilize a API REST ou a ferramenta MCP. Consulte [Associar ligações](#associar-ligações).
5. Selecione **Importar**.

A janela mostra o progresso à medida que lê o projeto, analisa os pipelines, os mapeia para operações do PlaidCloud e cria os fluxos de trabalho, as tabelas e os passos. Quando termina, a janela apresenta o relatório de conversão: contagens de passos por nível de confiança, avisos, conversões parciais, marcadores de posição não convertidos, componentes omitidos e os ficheiros de origem a carregar.

### Campos

A API REST e a ferramenta MCP aceitam estes campos.

| Campo | Obrigatório | O que faz |
| --- | --- | --- |
| `source_account_id` | Sim | Conta de documentos que contém a exportação do Prophecy. |
| `source_file_path` | Sim | Caminho do `.zip` do projeto, ou de um ficheiro `.json` de um pipeline, modelo ou subgrafo, dentro dessa conta. |
| `project_id` | Sim | Projeto onde os fluxos de trabalho são criados. |
| `document_account_id` | Sim | Conta de documentos de onde os conjuntos de dados não associados são lidos. |
| `document_account_path` | Sim | Pasta de base nessa conta para os conjuntos de dados não associados. Um valor vazio ou `/` corresponde à raiz da conta, e uma `/` inicial é ignorada. São recusados os caminhos com `..` ou segmentos iniciados por ponto, chavetas, letra de unidade ou esquema de URL, ou caracteres de controlo. |
| `workflow_prefix` | Não | Prefixo acrescentado aos nomes dos fluxos de trabalho. |
| `step_prefix` | Não | Prefixo acrescentado aos nomes dos passos. |
| `table_prefix` | Não | Prefixo acrescentado aos nomes das tabelas. Por predefinição, é o nome do próprio fluxo de trabalho. Um prefixo que reutilizasse o nome de uma tabela existente é recusado antes de ser criado o que quer que seja. O prefixo utilizado é devolvido no relatório de conversão. |
| `workflow_type` | Não | `advanced` (predefinido) dispõe o grafo na área de desenho DAG. `standard` produz uma lista de passos em série. |
| `source_bindings` | Não | Associa conjuntos de dados e operações a dados existentes. Consulte [Associar origens](#associar-origens). |
| `connection_bindings` | Não | Associa as bases de dados, os repositórios de ficheiros, as APIs REST e o correio eletrónico a que um projeto acede a ligações do PlaidCloud e a contas de documentos. Consulte [Associar ligações](#associar-ligações). |
| `parameters` | Não | Substitui parâmetros do Prophecy. Consulte [Parâmetros](#parâmetros). |
| `allow_unconverted_placeholders` | Não | Controla o que faz um marcador de posição em tempo de execução. Consulte [Marcadores de posição para gems não convertidos](#marcadores-de-posição-para-gems-não-convertidos). |

### REST

Envie os campos como corpo JSON para:

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

Precisa do papel `analyze.workflow.write`.

### MCP

Um agente de IA ligado por MCP chama a ferramenta `prophecy_convert` com os mesmos campos. Consulte [Agentes de IA (MCP)](/pt-pt/integrations/ai-coding-agents/) para ligar um agente. A ferramenta altera o seu projeto, pelo que deve rever a chamada antes de a aprovar.

## Associar origens

Uma exportação do Prophecy descreve de onde provêm os seus dados, mas não contém dados nem credenciais. Utilize `source_bindings` para ligar cada conjunto de dados a dados que já tenha no PlaidCloud. A chave é o nome do conjunto de dados tal como o relatório de conversão o apresenta. O valor é um dos seguintes:

- Um ID `analyzetable_` de uma tabela do projeto de destino. O fluxo de trabalho convertido lê essa tabela diretamente.
- Um objeto com `account`, `path` e, opcionalmente, `sheet`, para ler um ficheiro de uma conta de documentos.

```json
"source_bindings": {
  "customers": "analyzetable_1234",
  "budget": { "account": "<document account id>", "path": "/finance/budget.xlsx", "sheet": "FY27" }
}
```

Uma associação que não possa ler é recusada. Uma chave que não corresponda a nenhum conjunto de dados é comunicada como aviso. A janela do Analyze associa conjuntos de dados a tabelas; utilize a API REST ou a ferramenta MCP para associar um conjunto de dados a um ficheiro de documentos.

### Conjuntos de dados não associados

Um conjunto de dados sem associação torna-se um passo de importação ainda sem dados, e o relatório de conversão inclui um aviso sobre ele. O passo lê a partir de:

```text
<document_account_path>/prophecy/<workflow id>/<dataset name>.csv
```

Carregue o ficheiro para esse caminho e execute o fluxo de trabalho. Enquanto o ficheiro não estiver lá, o passo de importação termina com um aviso e cria uma tabela vazia, e o fluxo de trabalho continua. O relatório lista cada caminho em **Ficheiros de origem a carregar**.

### Associar operações de tabelas e de ficheiros

Os gems que alteram tabelas ou ficheiros, como Table Operations (update, delete, drop) e File Operation (copy), atuam apenas sobre dados criados pela conversão. Para que um deles trabalhe sobre dados já existentes, associe-os com uma chave da forma `operation:<pipeline>/<id>`, em que `<pipeline>` é o nome do pipeline e `<id>` é o ID do gem. O relatório de conversão indica a chave de cada um desses gems.

```json
"source_bindings": {
  "operation:daily_load/Operation_1": "analyzetable_5678"
}
```

Uma operação destrutiva sobre uma tabela ou um ficheiro só é executada se a associar. Sem associação, um gem Table Operations trabalha sobre uma tabela escrita por outro gem do mesmo projeto e, caso contrário, torna-se um marcador de posição que indica a respetiva chave. Um gem File Operation copia a partir da sua própria pasta de preparação. Nada fora das tabelas e pastas da própria conversão é alterado, a menos que o associe.

## Associar ligações

Um projeto Prophecy acede a bases de dados, repositórios de ficheiros, APIs REST e servidores de correio através de ligações. A exportação contém os nomes das ligações, mas não as credenciais, pelo que deve usar `connection_bindings` para apontar cada uma para uma ligação do PlaidCloud ou uma conta de documentos que já tenha. O relatório de conversão lista todas as chaves nas respetivas associações.

```json
"connection_bindings": {
  "connection:warehouse_pg": "<connection id>",
  "connection:landing_s3": "<document account id>",
  "operation:daily_load/Email_1": "<connection id>"
}
```

Uma chave é uma das seguintes:

| Chave | Associa | Valor |
| --- | --- | --- |
| `connection:<name>` | A ligação do Prophecy que um gem ou um conjunto de dados de base de dados indica. Uma associação serve todos os gems dessa ligação. Um gem que não indica nenhuma ligação usa `connection:<pipeline>/<gem id>`, e um conjunto de dados de base de dados usa `connection:<dataset name>`. | O ID de uma ligação do PlaidCloud: uma ligação de base de dados (incluindo BigQuery e SAP HANA), uma ligação MongoDB ou Apache Kafka, uma ligação Salesforce para leituras e escritas do Salesforce, uma ligação Tableau para um gem Tableau, uma ligação REST para Azure Cosmos DB, Pinecone, Power BI e escritas do Smartsheet e do Slack, ou uma ligação baseada em Singer para leituras do Smartsheet, do Slack e do Iceberg. O ID de uma conta de documentos para um gem File Storage ou Directory. |
| `operation:<pipeline>/<gem id>` | Um gem REST que envia qualquer pedido que não seja GET, HEAD ou OPTIONS, e todos os gems Email. | O ID de uma ligação. No caso de REST, uma ligação REST que contenha a credencial. |

A associação é o seu consentimento para os gems que alteram coisas fora da conversão:

- Um pedido REST que pode alterar o que a API contém, e um e-mail que chega a pessoas reais, são convertidos em passos funcionais apenas quando associa a respetiva chave `operation:`. Sem associação, o gem é um marcador de posição que indica a chave.
- Uma conta de documentos associada a um gem File Storage ou Directory permite que os passos desse gem escrevam, eliminem ou movam ficheiros nessa conta.
- Um pedido GET, HEAD ou OPTIONS é enviado tal como o gem o envia. Sem associação, não tem credencial até selecionar uma ligação REST no passo convertido.

Um conjunto de dados de base de dados ou um gem External Table sem associação é convertido num passo que indica a respetiva chave e aguarda que selecione uma ligação, e o relatório inclui um aviso. Volte a converter com a chave associada, ou selecione a ligação no passo. Uma associação cujo ID seja do tipo errado de repositório para os respetivos gems, ou que não possa utilizar, é recusada. Uma chave que não corresponda a nada é comunicada como aviso.

## Parâmetros

`parameters` substitui os parâmetros do Prophecy na conversão:

```json
"parameters": {
  "instance": "prod",
  "values": { "run_date": "2026-10-01", "region": "EMEA" },
  "pipelines": {
    "daily_load": { "instance": "prod", "values": { "region": "APAC" } }
  }
}
```

`instance` indica uma instância de configuração. `values` são texto, números ou booleanos. Uma entrada de pipeline substitui os valores válidos para todo o projeto relativamente a esse pipeline. O relatório lista os parâmetros utilizados e os que foram renomeados para se adequarem aos nomes de variáveis do PlaidCloud.

## Ler o relatório de conversão

A resposta inclui o relatório de conversão. Leia-o antes de executar os fluxos de trabalho.

| Secção | O que indica |
| --- | --- |
| Resumo | Quantos passos foram convertidos com confiança alta, média ou baixa, e quantos não foram convertidos. |
| Avisos | Tudo o que o conversor assumiu, aproximou ou ignorou, incluindo conjuntos de dados não associados e chaves de associação que não corresponderam a nada. |
| Conversões parciais | Passos que são convertidos, mas diferem do gem em algum modo ou opção. Cada um inclui uma nota sobre o que verificar. |
| Marcadores de posição não convertidos | Gems sem equivalente no PlaidCloud, com o motivo. |
| Componentes omitidos | Gems que não têm trabalho próprio, como marcadores de limite do fluxo de controlo, e o passo que absorveu cada um. |
| Ficheiros de origem a carregar | O caminho de documentos de onde cada conjunto de dados não associado é lido. |
| Fluxos de trabalho | O fluxo de trabalho criado para cada pipeline, por ordem de execução. Um pipeline que o conversor recusou é assinalado. |

O relatório indica também o prefixo de tabela utilizado e os parâmetros aplicados. Um passo sobre o qual o conversor não tem certeza é convertido para a interpretação mais provável e inclui uma nota no relatório. Verifique esses passos em relação à saída do Prophecy.

## Código do projeto nos passos

Os projetos Prophecy contêm código: gems Script, instruções SQL, macros, entradas dinâmicas, chamadas a procedimentos armazenados e gems personalizados. O conversor não executa esse código. Coloca-o dentro de um passo:

- O SQL é traduzido para o dialeto SQL do seu inquilino e colocado num passo SQL, com as entradas do gem disponíveis sob os nomes pelos quais a consulta as lê.
- Os scripts Python são colocados num passo Python, com o acesso a tabelas reescrito. Um script que chama métodos de data frames do Spark mantém essas chamadas e executa-as no passo.
- Um gem personalizado, incluindo um gem do Gem Builder, executa num passo Python o código PySpark que a exportação do respetivo pipeline transporta para ele.
- Uma macro de um pacote dbt conhecido torna-se os passos padrão que fazem o que a macro faz. Uma macro do seu próprio projeto, ou de um pacote que a exportação inclui, também é lida e convertida, incluindo blocos if e for, set, filtros, macros aninhadas e adapter dispatch.
- Uma função de agregação Python definida pelo utilizador num gem Aggregate é executada num passo Python para cada grupo.

Cada passo que transporta código do projeto recebe um aviso, tal como o SQL traduzido. Reveja o código de cada um desses passos antes de executar o fluxo de trabalho. O conversor retém tudo o que se pareça com credenciais que encontre em cadeias de caracteres e comentários do código, pelo que deve acrescentar as credenciais a uma ligação e não ao código.

## Marcadores de posição para gems não convertidos

Um gem que o conversor não consegue reproduzir é criado como um passo de marcador de posição com o nome do gem. São exemplos um gem personalizado cujo código não está na exportação e um gem que altera dados fora da conversão, como um pedido REST que pode alterar dados, um Email ou uma operação sobre tabelas ou ficheiros, quando não associou a respetiva chave `operation:`. Um conjunto de dados de base de dados ou External Table sem ligação associada não é um marcador de posição: é convertido num passo que aguarda que selecione uma ligação. Por predefinição, um marcador de posição falha quando o fluxo de trabalho o alcança, para que uma execução não possa comunicar êxito em trabalho que nunca aconteceu.

Defina `allow_unconverted_placeholders` como `true` (na janela, **Importar componentes não convertidos como marcadores de posição de passagem direta**) para importar cada marcador de posição como um passo de passagem direta. A execução continua então para além dele e a saída do marcador de posição é a sua entrada. O relatório contabiliza os marcadores de posição de passagem direta e lista os respetivos passos. Reconstrua a capacidade com um passo nativo quando o seu resultado for importante.

## Executar os fluxos de trabalho convertidos

1. Abra os novos fluxos de trabalho no projeto. O relatório lista-os por ordem de execução.
2. Defina as variáveis de projeto que tenham origem em parâmetros do Prophecy.
3. Carregue os ficheiros dos conjuntos de dados não associados para os caminhos indicados no relatório.
4. Reveja os passos que transportam código do projeto.
5. Execute os fluxos de trabalho e reveja a tabela de saída de cada passo.

Os eventos agendados criados a partir de agendamentos do Prophecy ficam ativados se estavam ativados no Prophecy, pelo que começam a executar os fluxos de trabalho convertidos de acordo com o respetivo agendamento. Para rever primeiro os fluxos de trabalho, desative os eventos em [Eventos agendados](/pt-pt/administration/scheduled-events/) e ative-os quando estiver pronto.

## O que é convertido

Todos os gems do Prophecy são totalmente convertidos em passos nativos, variáveis de projeto, eventos agendados ou objetos da área de desenho, com as opções que oferecem. A [matriz de conversão do Prophecy](/pt-pt/reference/prophecy-conversion-matrix/) lista todos os gems com o passo do PlaidCloud em que se transformam, e [Casos limite](#casos-limite) lista os poucos comportamentos a verificar; o relatório de conversão indica cada um deles onde ocorre.

### Movimentação de dados

| Capacidade | Como é convertida |
| --- | --- |
| Modos de escrita | Os modos de escrita de destino são convertidos em passos da plataforma: SCD2 com as estratégias de verificação e de data/hora (a estratégia de data/hora data cada versão a partir da coluna indicada por `scd2.updatedAtColumn` do gem), merge, `replaceWhere` e `insertInto`. Um merge aplica as expressões SET por coluna das suas cláusulas de atualização por correspondência e de inserção sem correspondência; uma cláusula que não define nenhuma coluna toma todas as colunas da linha de entrada. Uma primeira execução sobre um destino vazio escreve todas as linhas, como fazem o dbt e o Delta. A primeira execução não exige nenhuma tabela criada previamente, incluindo num pipeline que lê um conjunto de dados que também escreve, a menos que a exportação não indique que colunas esse conjunto de dados tem: nesse caso, crie a tabela antes da primeira execução. As execuções seguintes aplicam o filtro incremental ou a condição de merge. Os modos `error` e `ignore` verificam com a [condição de existência da tabela](/pt-pt/guides/workflows/step-conditions/#condições-de-existência-de-tabelas). |
| Time travel | Uma origem de tabela Delta ou de catálogo que lê uma versão anterior da sua tabela, por `versionAsOf` ou `timestampAsOf`, lê essa versão a partir do Databricks através da ligação que associar. |
| Streaming | As origens e os destinos de streaming são executados como lotes agendados. O destino de streaming substitui a sua tabela em vez de acrescentar, pelo que uma nova execução nunca duplica linhas. Agende o fluxo de trabalho para recolher os dados entretanto chegados. |
| Bases de dados | Os gems JDBC, Snowflake, Redshift, Hive, BigQuery, SAP HANA e External Table leem e escrevem através da ligação do PlaidCloud que associar. Um conjunto de dados BigQuery é lido com [Importar SQL](/pt-pt/reference/workflow-steps/import/import-sql/) e escrito com [Export External Database Tables](/pt-pt/reference/workflow-steps/export/export-external-tables/) (passo) numa [ligação BigQuery](/pt-pt/reference/connectors/google/big-query/). Uma tabela SAP HANA escrita em qualquer um dos modos de merge do gem HANA, incluindo SCD2 e os modos de eliminação, é preparada junto ao destino e integrada nele pela chave primária do destino ou pelas colunas de merge do gem; um destino em falta é criado primeiro. |
| MongoDB e Kafka | Um conjunto de dados MongoDB é lido com [Importar MongoDB](/pt-pt/reference/workflow-steps/import/import-mongodb/), incluindo o respetivo filtro ou pipeline de agregação, e uma leitura que não declara colunas toma-as dos primeiros documentos, como faz o conector Spark. Uma escrita usa [Exportar MongoDB](/pt-pt/reference/workflow-steps/export/export-mongodb/) no modo de escrita correspondente: `update` atualiza os campos do documento correspondente ou insere um, `ignore` escreve apenas enquanto a coleção não contiver nenhum documento, e `error` interrompe a execução quando contém um. Uma origem Kafka lê os seus tópicos entre os desfasamentos inicial e final com [Importar Kafka](/pt-pt/reference/workflow-steps/import/import-kafka/), e um destino Kafka envia cada linha com [Exportar Kafka](/pt-pt/reference/workflow-steps/export/export-kafka/). Um conjunto de dados Kafka que inicia sessão com `OAUTHBEARER` utiliza o [início de sessão OAuth](/pt-pt/reference/connectors/databases/apache-kafka/#oauth-oauthbearer) da ligação Kafka que associar, porque a exportação não contém credenciais. |
| Azure Cosmos DB | Uma leitura envia a consulta do conjunto de dados, ou lê todos os documentos, com [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) numa ligação REST com autenticação Cosmos DB, e segue o cabeçalho de continuação de página em página. Uma escrita envia um pedido por cada linha, segundo a estratégia de escrita do gem: overwrite, append, delete ou patch. Uma linha que transporta o ETag do respetivo documento só é substituída ou eliminada se o documento não tiver sido alterado entretanto, e uma linha que o contentor recuse por esse motivo, ou por um documento em falta ou já existente, é ignorada, como faz o conector Spark. O modo `ignore` escreve apenas enquanto o contentor não contiver nenhum documento. |
| Salesforce | Uma leitura usa [Salesforce: Consultar objeto](/pt-pt/reference/workflow-steps/salesforce/query-salesforce-object/), incluindo os registos eliminados e arquivados quando o gem os pede. Uma escrita insere, atualiza, faz upsert ou elimina, com um pedido por cada linha; um upsert faz a correspondência pelo campo de ID externo do gem, ou `Id` quando este não indica nenhum. |
| Smartsheet, Slack e Pinecone | Uma leitura do Smartsheet de uma folha com nome e colunas declaradas obtém a folha através da sua ligação REST e produz uma linha por cada linha da folha e uma coluna por cada coluna declarada. As outras leituras do Smartsheet, e as leituras do Slack e do Iceberg, usam [Import Singer Source](/pt-pt/reference/workflow-steps/import/import-singer/) (passo). Uma escrita no Smartsheet acrescenta as linhas à folha indicada, e um overwrite elimina primeiro as linhas da folha. Uma escrita no Slack publica uma mensagem por cada linha, e uma mensagem que o Slack recuse faz falhar o passo. Um índice Pinecone é lido como os seus vetores e respetivos metadados, e uma escrita faz upsert das linhas como vetores. |
| Tableau e Power BI | Tableau e Tableau Write publicam a entrada como uma extração Hyper através de [Publish to Tableau](/pt-pt/reference/workflow-steps/export/export-to-tableau/) (passo) na ligação Tableau que associar. Power BI Write envia as entradas para um conjunto de dados push do Power BI através de uma ligação REST com OAuth 2.0, localizando a área de trabalho pelo nome e criando o conjunto de dados quando é novo. |
| Formatos de ficheiro | CSV, JSON, Parquet, Avro, Excel, XML, largura fixa e ORC através de [Importar ORC](/pt-pt/reference/workflow-steps/import/import-orc/). As opções de formato são mapeadas, ou assinaladas como neutras quando não alteram nenhuma linha: a janela de data/hora de modificação numa leitura Avro, a codificação EBCDIC de um ficheiro de largura fixa, os registos de cabeçalho e de rodapé e os registos sem quebras de linha, o mapa de folhas e a palavra-passe numa leitura Excel, as opções de aspas de uma escrita CSV e uma escrita Excel com uma folha por cada valor. Os ficheiros de texto comprimidos são lidos e escritos com gzip, Deflate (zlib), Zstandard, LZ4, Snappy e LZO; um ficheiro comprimido é lido quando o seu nome termina na extensão do respetivo codec. Os ficheiros encriptados são desencriptados e encriptados no local. Consulte [Ficheiros encriptados](#ficheiros-encriptados). |
| File Operation | Copy e Move são convertidos em [Documento: Copiar ficheiro](/pt-pt/reference/workflow-steps/document/copy-document-file/) ou em Copy Directory na pasta que associar, mantendo apenas os ficheiros cujo nome corresponde ao `filenameRegex` do gem, e mantendo o caminho de cada ficheiro abaixo da pasta de origem quando o gem é recursivo. |
| Directory | Lista os ficheiros da pasta de documentos associada com [Listagem de diretório](/pt-pt/reference/workflow-steps/document/directory-listing/), nas colunas do gem. Com a opção de nome da folha ativada, cada livro Excel dá uma linha por folha e o respetivo `sheet_name`; os outros ficheiros dão uma linha com um `sheet_name` vazio. |

### Colunas e linhas

| Gem ou função | Como é convertido |
| --- | --- |
| Surrogate Key | As chaves continuam a partir de uma tabela que guarda a última chave emitida, como faz o ficheiro de chaves do gem. Todos os gems que indicam o mesmo ficheiro de chaves partilham essa tabela, pelo que as suas chaves nunca se sobrepõem. Uma execução sem linhas deixa-a como estava, e as chaves começam no valor inicial antes de qualquer execução ter emitido alguma. |
| Column Parser, XML Parse, análise de JSON | O texto XML e JSON é analisado com os passos [Análise de XML](/pt-pt/reference/workflow-steps/tables/table-xml-parse/) e [Analisar JSON](/pt-pt/reference/workflow-steps/tables/table-json-parse/), lendo cada campo a partir do texto do elemento, de um atributo ou de um elemento filho. O XML analisado sem esquema toma o tipo de cada campo a partir dos dados, como faz o `schema_of_xml` do Spark. |
| Regras de negócio | Uma regra de negócio do projeto chamada numa expressão é convertida nas mesmas condições, um `CASE` por cada coluna que define. |
| Conversões de tipo | Uma conversão de texto para decimal ou long segue exatamente o Spark: os espaços e os caracteres de controlo à volta do número são removidos, um decimal arredonda por excesso a partir de metade até à sua escala, e o texto que não é um número, ou um valor fora do intervalo, é nulo. |
| Datas e horas | Os formatos de data e hora são escritos para o motor da sua área de trabalho, incluindo o Databend, e `window()` coloca cada data/hora na respetiva janela deslizante, alinhada como o Spark a alinha. |
| Saídas de iteradores | Um Table Iterator ou While Iterator cujas colunas de saída só são conhecidas em tempo de execução reúne as linhas de cada passagem por posição com [Tabela: União total](/pt-pt/reference/workflow-steps/tables/table-union-all/#correspondência-de-colunas), com cada coluna alargada a um tipo que todas as passagens cumpram, como o Prophecy empilha as passagens. |
| Data Encoder/Decoder AES | É executado em todos os motores. A chave, e o vetor de inicialização e os dados adicionais quando o gem os indica, provêm das variáveis de fluxo de trabalho `aes_key`, `aes_iv` e `aes_aad`, que define. |
| Hash do Data Masking | Calcula os mesmos valores que o `hash()` do Spark. |
| Buffer, Simplify, Heat Map | O Buffer desenha um canto arredondado com o mesmo número de segmentos que o Prophecy, o Simplify elimina os mesmos vértices, e o Heat Map soma o calor em hexágonos H3 à resolução do gem, mantendo-se decimal um calor decimal. |

### Serviços e controlo

| Gem | Como é convertido |
| --- | --- |
| Pipeline | Executa o pipeline que indica com um passo [Workflow Loop](/pt-pt/reference/workflow-steps/workflow-control/workflow-loop/), uma vez por cada linha de entrada (uma vez quando não tem entrada, nunca quando não há linhas), com cada parâmetro definido a partir de uma constante, de uma coluna da linha ou de uma expressão sobre ela. Todas as execuções avançam mesmo que uma anterior falhe, e a saída do gem tem uma linha por cada execução com o respetivo estado, mensagem e horas, como o Prophecy as regista. |
| Agendamentos | Uma tarefa do Prophecy ou um agendamento de pipeline SQL torna-se um [evento agendado](/pt-pt/administration/scheduled-events/) com o nome `Prophecy <name>` no fluxo de trabalho convertido, ativado a menos que esteja desativado no Prophecy. Uma tarefa Spark é convertida assim quando executa um pipeline convertido sem substituições de configuração nem condições de execução. |
| Script | Um script Python é colocado num passo Python. Um valor que o script define em `Config` torna-se uma variável de fluxo de trabalho que os passos seguintes leem, reposta no valor do pipeline no início de cada execução, tal como o `Config` do Prophecy. |
| REST API, REST API Enrich | Passos [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/), um pedido por cada linha de entrada, mantendo uma resposta de erro como o Prophecy faz. O Enrich lê também o estado, o motivo e o URL final. Um pedido que aguarda um resultado assíncrono faz consultas repetidas até a resposta indicar que terminou. |
| Stored Procedure | Um gem que passa argumentos chama o respetivo procedimento com [Execução remota: SQL](/pt-pt/reference/workflow-steps/agent/agent-remote-execution-of-sql/#executar-uma-instrução-uma-vez-por-linha) uma vez por cada linha de entrada, com cada argumento associado a partir da respetiva coluna como parâmetro. Um gem sem argumentos chama-o uma vez através de um agente. Escolha a ligação ou o agente no passo convertido. |
| Email, Email Data | [Notify Via Email](/pt-pt/reference/workflow-steps/notifications/notify-via-email/) (passo) com Cc, Bcc, Reply-To e uma mensagem por cada linha quando um campo é lido de uma coluna. |
| OpenAI, Bedrock, SageMaker Endpoint | [Text: NLP (AI)](/pt-pt/reference/workflow-steps/text-documents/nlp-ai/) (passo) na ligação LLM da sua área de trabalho. Os embeddings do OpenAI e do Bedrock usam a tarefa Embed, que exige uma ligação compatível com OpenAI ou Azure OpenAI; uma ligação Anthropic é recusada. |
| Pinecone Lookup | Um pedido REST por cada linha. |
| Data Quality Check, Deequ, Soda | As verificações são executadas no armazém de dados e escrevem a tabela de resultados. Um Data Quality Check só interrompe a execução quando o gem define `minFailedChecks` ou uma ação posterior `fail_pipeline`; caso contrário, a tabela de resultados lista as falhas. O Deequ e o Soda nunca interrompem a execução. Uma verificação de comprimento mínimo ou máximo numa coluna numérica mede o número como texto. As verificações do Soda são convertidas a partir do YAML do projeto, incluindo valores em falta, inválidos e válidos, estatísticas, comprimentos, percentis, duplicados entre colunas, atualidade, linhas com falhas e as suas próprias consultas de indicadores. |
| ToDo | Gera um erro que indica a ferramenta original e a mensagem quando a execução o alcança. |

### Ficheiros encriptados

Um gem File Storage que lê um ficheiro encriptado é convertido em [Documento: desencriptar ficheiro](/pt-pt/reference/workflow-steps/document/encrypt-decrypt-file/), que desencripta o ficheiro para uma pasta própria antes de a importação o ler; a cópia desencriptada é removida depois. Um gem que escreve um ficheiro encriptado exporta para essa pasta e depois encripta o ficheiro no destino com Documento: encriptar ficheiro. Estão abrangidos os ficheiros AES e Blowfish e os livros Excel protegidos por palavra-passe.

A exportação nunca contém uma chave, pelo que os passos convertidos leem-na de uma variável de fluxo de trabalho: `aes_key` para uma chave AES ou Blowfish e `xlsx_password` para a palavra-passe de um livro. Defina a variável antes de executar o fluxo de trabalho e atribua-lhe uma chave destinada exclusivamente a estes ficheiros. Os campos de chave e de palavra-passe aceitam apenas uma referência a uma variável, pelo que uma chave nunca é escrita num passo.

## Casos limite

Estes são os comportamentos que um fluxo de trabalho convertido não reproduz por si só. O relatório de conversão indica cada um deles onde ocorre.

- **Código ou dados que a exportação não inclui**: Um gem do Gem Builder ou outro gem personalizado cujo código não está na exportação, e uma chamada a uma macro de um pacote dbt que a exportação deixa de fora, tornam-se um passo que indica o que falta; exporte o projeto com o código dos pipelines e os pacotes dbt, ou reconstrua a lógica num passo Python ou SQL. Os gems Ab Initio Error Detection e MTime passam a entrada diretamente, porque a regra que aplicam não está na exportação. As verificações do Soda lidas de um ficheiro exterior ao projeto, as que comparam com análises anteriores ou com outro conjunto de dados e as que testam um formato que o Soda nomeia não têm linha na tabela de resultados; calcule-as num passo posterior.
- **Resultados só conhecidos quando o pipeline é executado**: Um gem REST API que nivela a sua resposta coloca toda a resposta numa só coluna quando nada declara os nomes dos campos, o que só uma execução revela; extraia os campos de que precisa num passo posterior. Uma macro dbt que consulta o armazém de dados enquanto o dbt compila torna-se um passo que a indica; substitua a consulta pelos valores que esta devolve. Um gem Spark StoredProcedure é executado, mas os seus valores OUT não são devolvidos; a saída são as colunas de passagem direta. `input_file_name()` devolve uma cadeia vazia sobre uma origem de tabela ou Delta, que não tem ficheiro a nomear, e `hash()` / `xxhash64()` dentro de uma agregação, de uma janela ou de um gem com várias entradas são calculados pelo armazém de dados, pelo que podem diferir dos do Spark.
- **Valores escritos num passo quando o projeto é convertido**: Um valor de parâmetro que contém aspas, barra invertida ou chaveta, um valor de pipeline que um passo SQL lê e a base de dados que uma operação de tabela Delta indica através da configuração são escritos no passo como valores fixos, pelo que alterar a variável de fluxo de trabalho não os altera; edite o passo quando a configuração mudar.
- **Código Scala**: Um script Scala, uma expressão Scala ou uma função Scala definida pelo utilizador ou de agregação torna-se um passo que a indica; reescreva-a em SQL ou Python.
- **Início de sessão Kerberos no Kafka**: Uma origem ou um destino Kafka que inicia sessão com Kerberos (GSSAPI) é convertido sem o nome do serviço Kerberos e o mecanismo de início de sessão; defina-os na ligação do PlaidCloud.
- **Streaming**: As origens, os destinos e os pipelines de streaming são executados como fluxos de trabalho em lote sobre os dados presentes quando são executados; agende o fluxo de trabalho para ser executado com a frequência de que precisar.
- **Componentes de tarefas**: Uma tarefa Spark é convertida com o seu único pipeline e agendamento; os restantes componentes, as condições de execução e as substituições de configuração não são convertidos.
- **Chamadas pouco comuns**: Uma função de agregação definida pelo utilizador chamada a partir de um rollup ou de uma janela, e uma macro dbt que usa Jinja para além de if, for, set e dos filtros comuns, tornam-se um passo que indica o gem; chame a função a partir de um gem Aggregate, ou incorpore a macro diretamente.

## Guias relacionados

- [Migrar análises Savant](/pt-pt/guides/workflows/migrate-savant-analyses/)
- [Migrar fluxos de trabalho do Alteryx](/pt-pt/guides/workflows/migrate-alteryx-workflows/)
- [Adicionar contas de documentos](/pt-pt/guides/documents/adding-accounts/)
- [Gerir variáveis de fluxo de trabalho](/pt-pt/guides/workflows/manage-workflow-variables/)
- [Executar um fluxo de trabalho](/pt-pt/guides/workflows/run-a-workflow/)
