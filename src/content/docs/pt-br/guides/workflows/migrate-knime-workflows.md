---
title: Migrar fluxos de trabalho do KNIME
description: Converta um fluxo de trabalho do KNIME (.knwf) ou um grupo de fluxos de trabalho (.knar) em fluxos de trabalho avançados do PlaidCloud a partir do aplicativo Analyze, da API REST ou de um agente de IA conectado por MCP, vincule suas entradas e conexões e leia o relatório de conversão.
sidebar:
  order: 31.7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-knime-workflows.md
---

O PlaidCloud é um substituto direto do KNIME. 98,5% das configurações de nós do KNIME são convertidas integralmente, e 205 dos 207 tipos de nós principais são Full: cada um se torna etapas padrão de fluxo de trabalho do PlaidCloud que executam o trabalho do nó. O conversor transforma um arquivo de fluxo de trabalho do KNIME em fluxos de trabalho avançados executáveis, mantém o grafo original e retorna um relatório de conversão que indica tudo o que você precisa configurar. A [Matriz de conversão do KNIME](/pt-br/reference/knime-conversion-matrix/) lista todos os nós.

A conversão lê apenas o arquivo que você indicar. Ela nunca entra em contato com o sistema do qual um nó do KNIME lê ou no qual grava.

A conversão é uma etapa única. Converter o mesmo arquivo novamente cria novos fluxos de trabalho, e as edições feitas no PlaidCloud nunca são mescladas com uma exportação posterior.

## O que o PlaidCloud cria

- Um fluxo de trabalho avançado para cada fluxo de trabalho do KNIME. Um `.knwf` gera um fluxo de trabalho, e um `.knar` gera um para cada fluxo de trabalho do grupo.
- Cada nó do KNIME se torna a etapa de fluxo de trabalho, a variável de projeto ou o objeto de tela correspondente, com as relações a montante e a jusante preservadas. Metanós e componentes são nivelados no fluxo de trabalho, de modo que seus nós são executados como etapas comuns.
- Variáveis de fluxo e nós de Configuration e Widget se tornam variáveis de projeto com seus valores padrão. Switches e loops cujos valores são conhecidos no momento da conversão são podados e expandidos nas etapas que executam.
- As linguagens de expressão do KNIME — Expression, String Manipulation, Math Formula, Column Expressions e Rule Engine — são convertidas em expressões do PlaidCloud.
- Os arquivos de dados que acompanham o arquivo compactado são carregados em uma pasta `knime/` da conta de documentos padrão do projeto, uma pasta por fluxo de trabalho, e os leitores convertidos os importam de lá.
- Visualizações, gráficos e gerenciadores de cores não têm efeito sobre os dados. Eles são descartados e listados no relatório de conversão.

## Antes de começar

1. Exporte o fluxo de trabalho do KNIME Analytics Platform como um arquivo `.knwf`. Para converter vários fluxos de trabalho de uma vez, exporte o grupo de fluxos de trabalho como um arquivo `.knar`. Mantenha os arquivos usados pelos seus leitores na pasta `data` do fluxo de trabalho para que acompanhem o arquivo compactado.
2. Carregue o arquivo compactado em uma [conta de documentos](/pt-br/guides/documents/adding-accounts/) que você possa ler. No aplicativo Analyze, **Procurar** na janela de importação carrega o arquivo do seu computador.
3. Escolha o projeto do PlaidCloud que deve receber os fluxos de trabalho. Você precisa ser Arquiteto ou Gerente do projeto, e o projeto deve ter uma conta de documentos padrão.
4. Anote as tabelas, os arquivos e as conexões do PlaidCloud que você quer que os leitores e os nós conectores do fluxo de trabalho usem. Consulte [Vincular origens](#vincular-origens).

## Converter um fluxo de trabalho

Converta a partir do aplicativo Analyze, da API REST ou de um agente de IA conectado por MCP. A API REST e a ferramenta MCP recebem os mesmos campos; a janela recebe os que ela exibe.

### Aplicativo Analyze

1. Abra o **Analyze** e escolha **Ferramentas → Importar fluxo de trabalho do KNIME**.
2. Em **Importar origem e destino**, escolha o **Projeto de destino** e o **Arquivo KNIME (.knwf ou .knar)** em uma conta de documentos. Selecione **Procurar** para carregar o arquivo do seu computador.
3. Em **Prefixos de objetos**, defina opcionalmente o **Prefixo do fluxo de trabalho**, o **Prefixo da etapa** e o **Prefixo da tabela**. O prefixo da tabela usa por padrão o nome do fluxo de trabalho.
4. Em **Vínculos de origem (opcional)**, vincule opcionalmente um leitor a uma tabela existente no projeto de destino: selecione **Adicionar** e informe o **Leitor do KNIME** (o id do nó, como `12:3`, o nome do nó ou o nome do arquivo) e o **ID da tabela**. Para vincular conexões, documentos ou tabelas de outros projetos, use a API REST ou a ferramenta MCP. Consulte [Vincular origens](#vincular-origens).
5. Selecione **Importar**.

A janela mostra o progresso enquanto converte o arquivo compactado e, em seguida, o relatório de conversão: contagens de etapas (**Etapas**, **Alta confiança**, **Média**, **Baixa** e **Não convertidos**), os nós que não puderam ser convertidos e as etapas a jusante deles, conversões parciais, avisos, os arquivos de origem a carregar e os nós sem etapa. Uma conversão sem nada a revisar informa isso, e a janela se fecha sozinha.

### Campos

| Campo | Obrigatório | O que faz |
| --- | --- | --- |
| `source_account_id` | Sim | Conta de documentos que contém o arquivo do KNIME. |
| `source_file_path` | Sim | Caminho do arquivo `.knwf` ou `.knar` dentro dessa conta. |
| `project_id` | Sim | Projeto em que os fluxos de trabalho são criados. |
| `workflow_prefix` | Não | Prefixo adicionado aos nomes dos fluxos de trabalho. |
| `step_prefix` | Não | Prefixo adicionado aos nomes das etapas. |
| `table_prefix` | Não | Prefixo adicionado aos nomes das tabelas. Usa por padrão o próprio nome do fluxo de trabalho. Um prefixo que reutilizaria o nome de uma tabela existente é recusado antes de qualquer criação. Para um `.knar`, o prefixo de cada fluxo de trabalho é seguido do nome desse fluxo de trabalho. |
| `source_bindings` | Não | Vincula leitores e nós conectores a dados e conexões que você já tem, com até 500 entradas. Consulte [Vincular origens](#vincular-origens). |

### REST

Envie os campos como um corpo JSON para:

```text
POST /rest/v1/analyze/knime/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/knime/monthly-close.knwf",
  "project_id": "<project id>"
}
```

### MCP

Um agente de IA conectado por MCP chama a ferramenta `knime_convert` com os mesmos campos. Consulte [Agentes de IA (MCP)](/pt-br/integrations/ai-coding-agents/) para conectar um agente. A ferramenta altera seu projeto, portanto revise a chamada antes de aprová-la.

## Vincular origens

Use `source_bindings` para apontar um leitor do KNIME para dados que já existem no PlaidCloud, em vez da cópia contida no arquivo compactado. Uma chave é um id de nó (como `12:3`), um nome de nó, um caminho de arquivo incluído (como `data/sales.csv`) ou um nome de arquivo; vale a primeira correspondência nessa ordem. Um valor é um destes:

- Um id `analyzetable_` de uma tabela no projeto de destino. A tabela substitui o leitor.
- `{"project": "<project id>", "table": "<table id>"}` para uma tabela em outro projeto que você pode ler. O leitor se torna uma etapa [Import Project Table](/pt-br/reference/workflow-steps/import/import-project-table/) que a copia. O projeto de origem deve compartilhar Leitura com o projeto de destino, ou a etapa emite um aviso. Uma tabela regida por acesso às linhas é recusada.
- `{"account": "<document account id>", "path": "/finance/budget.xlsx"}` para um documento que você pode ler. O leitor o importa.
- `{"connection": "<connection id>"}` para um nó conector de banco de dados ou REST. As etapas convertidas são executadas nessa conexão.

A janela do aplicativo Analyze vincula leitores a tabelas do projeto de destino pelo id da tabela. Vincule conexões, documentos e tabelas de outros projetos pela API REST ou pela ferramenta MCP.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "data/budget.xlsx": { "account": "<document account id>", "path": "/finance/budget.xlsx" }
}
```

Uma tabela vinculada que não existe, ou uma chave que não corresponde a nenhum leitor, gera um aviso. As vinculações aplicadas, com os nomes de projeto e de tabela, são listadas no relatório de conversão em `bindings`.

### Entradas não vinculadas

Um leitor cujo arquivo não está no arquivo compactado lê de `inputs/<file name>` na pasta do fluxo de trabalho da conta de documentos padrão, e o relatório de conversão lista o caminho em `missing_inputs` com um aviso. Carregue o arquivo nesse local e execute o fluxo de trabalho. Enquanto o arquivo não estiver lá, a importação termina com um aviso e cria uma tabela vazia, e o fluxo de trabalho continua.

## Credenciais e conexões

As credenciais do KNIME nunca são migradas. Cada etapa que faz login em outro sistema lê suas credenciais de uma conexão do PlaidCloud ou de uma variável de projeto que você define, e o aviso da etapa no relatório de conversão informa qual.

| KNIME | O que você define |
| --- | --- |
| Conectores de banco de dados | Uma conexão de banco de dados: vincule-a com `{"connection": "<id>"}` ou escolha-a na etapa. |
| Nós REST e de serviços web que fazem login | Uma [conexão REST](/pt-br/reference/connectors/rest/generic-rest/): vincule-a com `{"connection": "<id>"}` ou escolha-a na etapa. |
| Speech Recognizer (IBM Watson) | Uma conexão REST cuja URL base é a URL do serviço Watson indicada no aviso, com o usuário `apikey` e sua chave de API como login básico. Vincule-a ao nó. |
| Email Connector, com Email Reader ou Email Mover | Uma variável de projeto com a senha do servidor de e-mail, com o nome indicado no aviso. O host e o usuário vêm do Email Connector. |
| Excel Reader ou Excel Writer com senha na pasta de trabalho | Uma variável de projeto com a senha, com o nome indicado no aviso. |
| Conectores e autenticadores de LLM | Uma conexão de LLM na etapa de IA. |

Consulte [Gerenciar variáveis do fluxo de trabalho](/pt-br/guides/workflows/manage-workflow-variables/) para definir variáveis de projeto.

## Ler o relatório de conversão

A janela do aplicativo Analyze mostra o relatório de conversão quando a importação termina, e as respostas REST e MCP o incluem. Leia-o antes de executar os fluxos de trabalho.

- `summary` conta as etapas criadas e quantas foram mapeadas com confiança alta, média ou baixa.
- `warnings` lista cada aviso com seu nó, sua etapa e a ação a tomar, incluindo cada credencial ou conexão a definir.
- `missing_inputs` lista os caminhos de documentos para os quais carregar arquivos de entradas não vinculadas.
- `bindings` lista as vinculações aplicadas.
- `table_prefix` é o prefixo usado. Para um `.knar`, `workflows` lista cada fluxo de trabalho com seu próprio prefixo.
- `uploaded_files`, ao lado do relatório, lista os arquivos incluídos que foram carregados na conta de documentos padrão.
- `dropped_tools` lista as visualizações e os gráficos que foram descartados.

## Marcadores de posição

Um nó sem caminho de conversão permanece na tela como um marcador de posição nomeado. O marcador repassa seus dados e emite um aviso com o nome do nó do KNIME, e toda etapa a jusante dele é sinalizada no relatório, de modo que um resultado ausente nunca passa despercebido. Reconstrua o recurso com uma etapa padrão quando o resultado dele for importante.

## Executar o fluxo de trabalho convertido

1. Abra o novo fluxo de trabalho no projeto.
2. Defina as variáveis de projeto e as conexões indicadas nos avisos.
3. Carregue os arquivos das entradas não vinculadas nos caminhos listados em **Arquivos de origem a carregar** na janela, ou em `missing_inputs`.
4. [Execute o fluxo de trabalho](/pt-br/guides/workflows/run-a-workflow/) e revise a tabela de saída de cada etapa.

## Casos extremos

Estas são as únicas diferenças conhecidas em relação ao KNIME.

- **Crosstab.** Converte para a etapa [Table: Pivot](/pt-br/reference/workflow-steps/tables/table-pivot/). Algumas combinações de configurações geram resultados diferentes dos do KNIME.
- **Loop End (Column Append).** Converte para a etapa [Tabela: Junção interna](/pt-br/reference/workflow-steps/tables/table-inner-join/). Algumas combinações de configurações geram resultados diferentes dos do KNIME.
- **Sorteios aleatórios.** Row Sampler, Table Partitioner e Equal Size Sampling fazem o sorteio aleatório próprio do KNIME com a etapa [Table: KNIME Random Sample](/pt-br/reference/workflow-steps/tables/table-knime-random-sample/), de modo que um nó com semente seleciona as mesmas linhas que no KNIME. O sorteio aceita uma tabela de no máximo 10.000.000 de linhas; uma tabela maior faz a etapa falhar.

## Guias relacionados

- [Matriz de conversão do KNIME](/pt-br/reference/knime-conversion-matrix/)
- [Conexão REST](/pt-br/reference/connectors/rest/generic-rest/)
- [Adicionar contas de documentos](/pt-br/guides/documents/adding-accounts/)
- [Gerenciar variáveis do fluxo de trabalho](/pt-br/guides/workflows/manage-workflow-variables/)
- [Executar um fluxo de trabalho](/pt-br/guides/workflows/run-a-workflow/)
