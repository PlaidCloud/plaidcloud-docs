---
title: Migrar fluxos de trabalho KNIME
description: Converta um fluxo de trabalho KNIME (.knwf) ou um grupo de fluxos de trabalho (.knar) em fluxos de trabalho avançados do PlaidCloud a partir da aplicação Analyze, da API REST ou de um agente de IA ligado por MCP, associe as respetivas entradas e ligações e leia o relatório de conversão.
sidebar:
  order: 31.7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-knime-workflows.md
---

O PlaidCloud é um substituto direto do KNIME. 98,5 % das configurações de nós KNIME são convertidas na íntegra e 205 dos 207 tipos de nós principais são Full: cada um passa a ser constituído por passos de fluxo de trabalho padrão do PlaidCloud que executam o trabalho do nó. O conversor transforma um arquivo de fluxo de trabalho KNIME em fluxos de trabalho avançados executáveis, mantém o grafo original e devolve um relatório de conversão que indica tudo o que tem de definir. A [matriz de conversão KNIME](/pt-pt/reference/knime-conversion-matrix/) enumera todos os nós.

A conversão lê apenas o arquivo que indicar. Nunca contacta o sistema de que um nó KNIME lê ou para o qual escreve.

A conversão é um passo único. Se converter o mesmo arquivo novamente, são criados novos fluxos de trabalho, e as alterações que tiver feito no PlaidCloud nunca são combinadas com uma exportação posterior.

## O que o PlaidCloud cria

- Um fluxo de trabalho avançado por cada fluxo de trabalho KNIME. Um `.knwf` dá origem a um fluxo de trabalho e um `.knar` dá origem a um por cada fluxo de trabalho do grupo.
- Cada nó KNIME passa a ser o passo de fluxo de trabalho, a variável de projeto ou o objeto da área de desenho correspondente, mantendo-se as relações a montante e a jusante. Os metanós e os componentes são achatados no fluxo de trabalho, pelo que os respetivos nós são executados como passos normais.
- As variáveis de fluxo e os nós de configuração e de widget passam a ser variáveis de projeto com os respetivos valores predefinidos. Os comutadores e os ciclos cujos valores são conhecidos no momento da conversão são podados e expandidos nos passos que executam.
- As linguagens de expressão do KNIME — Expression, String Manipulation, Math Formula, Column Expressions e Rule Engine — são convertidas em expressões do PlaidCloud.
- Os ficheiros de dados incluídos no arquivo são carregados para uma pasta `knime/` na conta de documentos predefinida do projeto, uma pasta por fluxo de trabalho, e os leitores convertidos importam-nos a partir daí.
- As vistas, os gráficos e os gestores de cor não têm efeito nos dados. São descartados e enumerados no relatório de conversão.

## Antes de começar

1. Exporte o fluxo de trabalho a partir do KNIME Analytics Platform como ficheiro `.knwf`. Para converter vários fluxos de trabalho em simultâneo, exporte o respetivo grupo de fluxos de trabalho como ficheiro `.knar`. Mantenha os ficheiros que os seus leitores utilizam na pasta `data` do fluxo de trabalho, para que sejam incluídos no arquivo.
2. Carregue o arquivo para uma [conta de documentos](/pt-pt/guides/documents/adding-accounts/) que possa ler. Na aplicação Analyze, **Procurar** na janela de importação carrega-o a partir do seu computador.
3. Escolha o projeto do PlaidCloud que deve receber os fluxos de trabalho. Tem de ser Arquiteto ou Gestor do projeto, e o projeto tem de ter uma conta de documentos predefinida.
4. Tome nota das tabelas, dos ficheiros e das ligações do PlaidCloud que pretende que os leitores e os nós de conetor do fluxo de trabalho utilizem. Consulte [Associar origens](#associar-origens).

## Converter um fluxo de trabalho

Converta a partir da aplicação Analyze, da API REST ou de um agente de IA ligado por MCP. A API REST e a ferramenta MCP aceitam os mesmos campos; a janela aceita os que apresenta.

### Aplicação Analyze

1. Abra **Analyze** e escolha **Ferramentas → Importar fluxo de trabalho KNIME**.
2. Em **Importar origem e destino**, escolha o **Projeto de destino** e o **Arquivo KNIME (.knwf ou .knar)** numa conta de documentos. Selecione **Procurar** para carregar o arquivo a partir do seu computador.
3. Em **Prefixos de objetos**, defina opcionalmente o **Prefixo do fluxo de trabalho**, o **Prefixo do passo** e o **Prefixo da tabela**. O prefixo da tabela assume por predefinição o nome do fluxo de trabalho.
4. Em **Ligações de origem (opcional)**, associe opcionalmente um leitor a uma tabela existente no projeto de destino: selecione **Adicionar** e introduza o **Leitor KNIME** (o respetivo ID de nó, como `12:3`, o nome do nó ou o nome do ficheiro) e o **ID da tabela**. Para associar ligações, documentos ou tabelas de outros projetos, utilize a API REST ou a ferramenta MCP. Consulte [Associar origens](#associar-origens).
5. Selecione **Importar**.

A janela mostra o progresso enquanto converte o arquivo e, em seguida, o relatório de conversão: contagens de passos (**Passos**, **Confiança alta**, **Média**, **Baixa** e **Não convertidos**), os nós que não foi possível converter e os passos a jusante dos mesmos, as conversões parciais, os avisos, os ficheiros de origem a carregar e os nós sem passo. Uma conversão sem nada para rever indica-o e a janela fecha-se automaticamente.

### Campos

| Campo | Obrigatório | O que faz |
| --- | --- | --- |
| `source_account_id` | Sim | Conta de documentos que contém o arquivo KNIME. |
| `source_file_path` | Sim | Caminho do ficheiro `.knwf` ou `.knar` nessa conta. |
| `project_id` | Sim | Projeto onde os fluxos de trabalho são criados. |
| `workflow_prefix` | Não | Prefixo adicionado aos nomes dos fluxos de trabalho. |
| `step_prefix` | Não | Prefixo adicionado aos nomes dos passos. |
| `table_prefix` | Não | Prefixo adicionado aos nomes das tabelas. Assume por predefinição o nome do próprio fluxo de trabalho. Um prefixo que reutilizasse o nome de uma tabela existente é recusado antes de ser criado o que quer que seja. Num `.knar`, o prefixo de cada fluxo de trabalho é seguido do nome desse fluxo de trabalho. |
| `source_bindings` | Não | Associa leitores e nós de conetor a dados e ligações que já tem, até 500 entradas. Consulte [Associar origens](#associar-origens). |

### REST

Envie os campos como corpo JSON para:

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

Um agente de IA ligado por MCP chama a ferramenta `knime_convert` com os mesmos campos. Consulte [Agentes de IA (MCP)](/pt-pt/integrations/ai-coding-agents/) para ligar um agente. A ferramenta altera o seu projeto, por isso reveja a chamada antes de a aprovar.

## Associar origens

Utilize `source_bindings` para apontar um leitor KNIME para dados que já existem no PlaidCloud, em vez da cópia incluída no arquivo. Uma chave é um ID de nó (como `12:3`), um nome de nó, o caminho de um ficheiro incluído (como `data/sales.csv`) ou um nome de ficheiro; prevalece a primeira correspondência por esta ordem. Um valor é um dos seguintes:

- Um ID `analyzetable_` de uma tabela do projeto de destino. A tabela substitui o leitor.
- `{"project": "<project id>", "table": "<table id>"}` para uma tabela de outro projeto que possa ler. O leitor passa a ser um [passo Import Project Table](/pt-pt/reference/workflow-steps/import/import-project-table/) que a copia. O projeto de origem tem de partilhar a permissão de leitura com o projeto de destino, caso contrário o passo emite um aviso. Uma tabela regida por acesso às linhas é recusada.
- `{"account": "<document account id>", "path": "/finance/budget.xlsx"}` para um documento que possa ler. O leitor importa-o.
- `{"connection": "<connection id>"}` para um nó de conetor de base de dados ou REST. Os passos convertidos são executados nessa ligação.

A janela da aplicação Analyze associa leitores a tabelas do projeto de destino através do ID da tabela. Associe ligações, documentos e tabelas de outros projetos através da API REST ou da ferramenta MCP.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "data/budget.xlsx": { "account": "<document account id>", "path": "/finance/budget.xlsx" }
}
```

Uma tabela associada que não exista, ou uma chave que não corresponda a nenhum leitor, é um aviso. As associações aplicadas, com os nomes do projeto e da tabela, são enumeradas no relatório de conversão em `bindings`.

### Entradas não associadas

Um leitor cujo ficheiro não está no arquivo lê a partir de `inputs/<file name>` na pasta do fluxo de trabalho da conta de documentos predefinida, e o relatório de conversão enumera o caminho em `missing_inputs` com um aviso. Carregue o ficheiro para aí e execute o fluxo de trabalho. Enquanto o ficheiro não estiver lá, a importação termina com um aviso e cria uma tabela vazia, e o fluxo de trabalho continua.

## Credenciais e ligações

As credenciais do KNIME nunca são migradas. Cada passo que inicia sessão noutro sistema lê as respetivas credenciais de uma ligação do PlaidCloud ou de uma variável de projeto que defina, e o aviso do passo no relatório de conversão indica qual.

| KNIME | O que define |
| --- | --- |
| Conetores de bases de dados | Uma ligação de base de dados: associe-a com `{"connection": "<id>"}` ou escolha-a no passo. |
| Nós REST e de serviços Web que iniciam sessão | Uma [ligação REST](/pt-pt/reference/connectors/rest/generic-rest/): associe-a com `{"connection": "<id>"}` ou escolha-a no passo. |
| Speech Recognizer (IBM Watson) | Uma ligação REST cujo URL de base é o URL do serviço Watson indicado no aviso, com o utilizador `apikey` e a sua chave de API como início de sessão Basic. Associe-a ao nó. |
| Email Connector, com Email Reader ou Email Mover | Uma variável de projeto com a palavra-passe do servidor de correio, com o nome indicado no aviso. O anfitrião e o utilizador provêm do Email Connector. |
| Excel Reader ou Excel Writer com palavra-passe do livro | Uma variável de projeto com a palavra-passe, com o nome indicado no aviso. |
| Conetores e autenticadores de LLM | Uma ligação LLM no passo de IA. |

Consulte [Gerir variáveis do fluxo de trabalho](/pt-pt/guides/workflows/manage-workflow-variables/) para definir variáveis de projeto.

## Ler o relatório de conversão

A janela da aplicação Analyze mostra o relatório de conversão quando a importação termina, e as respostas REST e MCP incluem-no. Leia-o antes de executar os fluxos de trabalho.

- `summary` contabiliza os passos criados e quantos foram mapeados com confiança alta, média ou baixa.
- `warnings` enumera cada aviso com o respetivo nó, passo e a ação a tomar, incluindo todas as credenciais ou ligações a definir.
- `missing_inputs` enumera os caminhos de documentos para os quais carregar ficheiros referentes a entradas não associadas.
- `bindings` enumera as associações aplicadas.
- `table_prefix` é o prefixo utilizado. Num `.knar`, `workflows` enumera cada fluxo de trabalho com o seu próprio prefixo.
- `uploaded_files`, a par do relatório, enumera os ficheiros incluídos que foram carregados para a conta de documentos predefinida.
- `dropped_tools` enumera as vistas e os gráficos que foram descartados.

## Marcadores de posição

Um nó sem caminho de conversão permanece na área de desenho como um marcador de posição com nome. O marcador de posição transmite os respetivos dados e emite um aviso com o nome do nó KNIME, e todos os passos a jusante são assinalados no relatório, pelo que um resultado em falta nunca passa despercebido. Reconstrua a funcionalidade com um passo padrão quando o respetivo resultado for importante.

## Executar o fluxo de trabalho convertido

1. Abra o novo fluxo de trabalho no projeto.
2. Defina as variáveis de projeto e as ligações indicadas nos avisos.
3. Carregue os ficheiros das entradas não associadas para os caminhos indicados em **Ficheiros de origem a carregar** na janela, ou em `missing_inputs`.
4. [Execute o fluxo de trabalho](/pt-pt/guides/workflows/run-a-workflow/) e reveja a tabela de saída de cada passo.

## Casos limite

Estas são as únicas diferenças conhecidas em relação ao KNIME.

- **Crosstab.** É convertido no [passo Table: Pivot](/pt-pt/reference/workflow-steps/tables/table-pivot/). Algumas combinações de definições dão resultados diferentes dos do KNIME.
- **Loop End (Column Append).** É convertido em [Tabela: Junção interna](/pt-pt/reference/workflow-steps/tables/table-inner-join/). Algumas combinações de definições dão resultados diferentes dos do KNIME.
- **Sorteios aleatórios.** Row Sampler, Table Partitioner e Equal Size Sampling efetuam o sorteio aleatório próprio do KNIME com o [passo Table: KNIME Random Sample](/pt-pt/reference/workflow-steps/tables/table-knime-random-sample/), pelo que um nó com semente seleciona as mesmas linhas que no KNIME. O sorteio aceita uma tabela com um máximo de 10 000 000 de linhas; uma tabela maior faz o passo falhar.

## Guias relacionados

- [Matriz de conversão KNIME](/pt-pt/reference/knime-conversion-matrix/)
- [Ligação REST](/pt-pt/reference/connectors/rest/generic-rest/)
- [Adicionar contas de documentos](/pt-pt/guides/documents/adding-accounts/)
- [Gerir variáveis do fluxo de trabalho](/pt-pt/guides/workflows/manage-workflow-variables/)
- [Executar um fluxo de trabalho](/pt-pt/guides/workflows/run-a-workflow/)
