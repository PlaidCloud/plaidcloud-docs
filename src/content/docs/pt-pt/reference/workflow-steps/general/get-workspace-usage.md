---
title: Passo Get Workspace Usage
description: Escreva a utilização da área de trabalho numa tabela do projeto como atividade, membros, conteúdo ou tendências, para comunicar a adoção ou alimentar um passo seguinte.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Descrição

Escreve numa tabela do projeto a forma como a área de trabalho é utilizada. Utilize-o para acompanhar a adoção ao longo do tempo, para comunicar a utilização por departamento ou equipa, para criar os seus próprios painéis de controlo ou para assinalar uma quebra de atividade num fluxo de trabalho agendado. Os valores provêm dos mesmos dados de utilização que os [Relatórios de utilização](/pt-pt/administration/access/usage-reports/), e cada conjunto de dados abrange todas as áreas.

**Atividade** e **Membros** contêm a identidade dos membros (ID de utilizador, nome de utilizador, correio eletrónico, nome próprio, apelido e grupos de segurança). A tabela de destino é uma tabela do projeto normal, pelo que qualquer pessoa com acesso ao projeto a pode ler: trate-a como trataria qualquer lista de membros. Cada execução que escreve a tabela fica registada no Registo de segurança.

## Configuração

### Dados de utilização

**Conjunto de dados** define o que contém cada linha. O texto por baixo descreve as linhas e indica as principais colunas do conjunto que escolher.

| Conjunto de dados | Valor | Uma linha por | Contém identidade |
|---|---|---|---|
| **Atividade** (predefinido) | `activity` | Dia, membro, ação e item | Sim |
| **Membros** | `members` | Membro, incluindo membros sem atividade | Sim |
| **Conteúdo** | `content` | Painel de controlo, aplicação e notebook, incluindo painéis de controlo e aplicações que ninguém utilizou | Não |
| **Tendências** | `trends` | Dia, semana e mês do intervalo | Não |

Os valores são os que um passo guarda quando o cria ou edita através da API ou de um assistente de IA. Um passo guardado com um conjunto de dados que não consta desta lista falha quando é executado, indicando os quatro conjuntos de dados: abra-o, escolha um **Conjunto de dados** e guarde-o. Um passo **Membros** ou **Conteúdo** guardado anteriormente continua a ser executado e escreve as colunas abaixo, e um passo que estava limitado a uma área passa a abranger todas as áreas. Em **Conteúdo**, `subject` passa a ser `item_id` e `type` contém `Dashboard`, `App` ou `Notebook`.

### Colunas

As datas e os dias são guardados como carimbos de data/hora à meia-noite UTC.

#### Colunas de membros

**Atividade** e **Membros** incluem estas colunas:

| Coluna | Contém |
|---|---|
| `user_id` | O ID do membro. |
| `user_name` | O nome de utilizador do membro. |
| `email` | O endereço de correio eletrónico do membro, em minúsculas. |
| `first_name` | Nome próprio. |
| `last_name` | Apelido. |
| `is_active` | Verdadeiro quando o membro está ativo, falso quando está desativado. |
| `groups` | Os grupos de segurança do membro, separados por `; `. |

`groups` lista os grupos de nível superior a que o membro pertence diretamente.

#### Atividade

| Coluna | Contém |
|---|---|
| `day` | O dia. |
| As colunas de membros | Como acima. |
| `member` | O nome próprio e o apelido do membro, ou o nome de utilizador quando nenhum deles está definido. |
| `area` | `PlaidCloud app`, `Dashboards`, `Apps` ou `Notebooks`. |
| `action` | `Opened app`, `Opened screen`, `Opened step`, `Saved step`, `Used palette action`, `Viewed dashboard`, `Used chart`, `Opened notebook` ou `Saved notebook`. |
| `item_type` | `App area`, `Screen`, `Step`, `Palette action`, `Dashboard`, `Chart`, `App` ou `Notebook`. |
| `item_id` | O ID do item. Para um notebook, o respetivo caminho. |
| `item_name` | O nome do item: um ecrã ou uma área da aplicação por extenso, como `Members List`; o tipo de passo; o nome do painel de controlo, do gráfico ou da aplicação; ou o caminho do notebook. Quando não é possível encontrar um nome, o ID do item. |
| `events` | Quantas vezes o membro o fez nesse dia. |
| `source` | A chave da área, tal como a designam as exportações dos [Relatórios de utilização](/pt-pt/administration/access/usage-reports/). |
| `event` | A chave da ação, tal como a designam as exportações. |

`member` e as colunas de membros dependem de quem a realizou:

- A atividade que não pode ser associada a nenhum membro tem `Unattributed` em `member` e as colunas de membros em branco.
- Um membro entretanto eliminado mantém apenas `user_id`, e `member` é `Deleted user`.
- Qualquer outra conta, como uma conta de serviço ou um agente, mantém apenas `user_id`, e `member` é o respetivo nome de utilizador.

`Used chart` conta uma vez por membro e gráfico em cada janela de 5 minutos, pelo que mede a utilização, não as consultas.

#### Membros

| Coluna | Contém |
|---|---|
| As colunas de membros | Como acima. |
| `member` | O nome próprio e o apelido do membro, ou o nome de utilizador quando nenhum deles está definido. |
| `created` | O dia em que o membro foi adicionado à área de trabalho, quando é conhecido. |
| `status` | `Active` quando o membro esteve ativo no intervalo, `Dormant` quando utilizou o PlaidCloud antes mas não no intervalo, `Never active` quando não há utilização registada até ao fim do intervalo. |
| `first_seen` | O primeiro dia registado em que o membro utilizou o PlaidCloud, independentemente do intervalo. |
| `last_seen` | O último dia de atividade do membro no intervalo. |
| `active_days` | Dias com atividade no intervalo. |
| `events` | Eventos de atividade no intervalo. |
| `active_minutes` | Minutos de atividade no intervalo. |
| `session_minutes` | Minutos em sessões no intervalo. |
| `app_open_minutes` | Minutos em que o membro teve aplicações Panel abertas no intervalo. As pré-visualizações do Studio não são contadas. |

Todos os membros têm uma linha, incluindo os desativados, exceto aqueles cuja utilização foi apagada. As contas de serviço e os agentes não são listados. Um membro sem atividade no intervalo não tem `last_seen`, e as restantes colunas de atividade ficam em branco.

#### Conteúdo

| Coluna | Contém |
|---|---|
| `type` | `Dashboard`, `App` ou `Notebook`. |
| `item_id` | O ID do painel de controlo ou da aplicação, ou o caminho do notebook. |
| `name` | O nome do painel de controlo ou da aplicação, ou o caminho do notebook. Em branco quando o item foi eliminado ou não é possível ler os nomes. |
| `deleted` | Verdadeiro quando o painel de controlo ou a aplicação foi entretanto eliminado. |
| `unused` | Verdadeiro para um painel de controlo ou uma aplicação que ninguém utilizou no intervalo. |
| `users` | Membros que o utilizaram no intervalo. |
| `opens` | Número de vezes que foi aberto no intervalo, incluindo as aberturas que não podem ser associadas a um membro. |
| `last_used` | O último dia em que foi utilizado no intervalo. Para um item não utilizado, o último dia em que foi aberto antes do fim do intervalo, ou em branco. |
| `app_open_minutes` | Minutos em que uma aplicação Panel esteve aberta no intervalo. Em branco para painéis de controlo, notebooks e aplicações Dash e WASM. |

Cada caminho de notebook tem a sua própria linha. As linhas listam primeiro o que foi utilizado, começando pelo que teve mais utilizadores, e depois os painéis de controlo e as aplicações que ninguém utilizou. Estes são os painéis de controlo publicados e as aplicações que já existiam quando o intervalo começou. Só são listados quando o intervalo começa dentro dos dados diários que são conservados, a utilização desse tipo de item já estava a ser recolhida nessa altura e é possível ler os nomes. As pré-visualizações de aplicações no Studio ficam de fora.

#### Tendências

| Coluna | Contém |
|---|---|
| `period` | `Day`, `Week` ou `Month`. |
| `period_start` | O primeiro dia do período. As semanas começam à segunda-feira. |
| `active_members` | Membros ativos no período, dentro do intervalo. |
| `events` | Eventos de atividade no período. |
| `active_minutes` | Minutos de atividade no período. |
| `session_minutes` | Minutos em sessões no período. |
| `active_members_7d` | Numa linha `Day`, membros ativos nos 7 dias que terminam nesse dia. |
| `active_members_28d` | Numa linha `Day`, membros ativos nos 28 dias que terminam nesse dia. |
| `stickiness` | Numa linha `Day`, `active_members` a dividir por `active_members_28d`. |
| `complete` | Falso para hoje, para uma semana ou um mês que contenha hoje e para uma semana ou um mês que o intervalo corta. |

Cada dia do intervalo, a partir de onde começam os dados diários conservados, tem uma linha, mesmo sem utilização, tal como cada semana e cada mês em que esses dias se inserem. `active_members_7d`, `active_members_28d` e `stickiness` ficam em branco nas linhas `Week` e `Month`, e numa linha `Day` cujos 7 ou 28 dias recuam para antes dos dados diários que são conservados. `stickiness` também fica em branco quando `active_members_28d` é 0. Um mês que começa antes dos dados diários conservados e se encontra por inteiro no intervalo provém dos resumos mensais: tem `active_members`, mas eventos e minutos em branco, e `complete` indica se o resumo cobriu o mês inteiro.

### Exemplo: minutos ativos por departamento

**Atividade** e **Membros** contêm o `email` do membro, em minúsculas, pelo que pode associá-los a uma tabela sua, como uma tabela mestre de RH ou da organização, e elaborar relatórios por departamento.

1. Adicione um passo **Get Workspace Usage** com **Conjunto de dados** definido como **Membros** e uma tabela de destino como `usage_members`.
2. Adicione um passo **Tabela: Junção interna** que una `usage_members` à sua tabela da organização onde as colunas `email` em minúsculas coincidam. Mantenha o departamento da sua tabela e as colunas `active_minutes` e `events` de `usage_members`.
3. No mesmo passo, agregue por departamento e some `active_minutes`.

O resultado são os minutos ativos por departamento. Os membros que não constam da sua tabela da organização são excluídos por uma junção interna, pelo que deve utilizar uma junção à esquerda se quiser vê-los. Repita com um segundo passo sobre **Atividade** e some `events` por departamento e `item_name` para comunicar quem utiliza que painéis de controlo e aplicações.

### Intervalo de datas

**Intervalo** define os dias a ler:

| Intervalo | Valor | Lê |
|---|---|---|
| **Últimos N dias** (predefinido 30) | `last_days` | Os dias mais recentes, incluindo hoje. |
| **Mês anterior** | `previous_month` | O último mês civil completo. |
| **Mês até à data** | `month_to_date` | Desde o primeiro dia deste mês até hoje. |
| **Entre datas** | `dates` | De **Data de início** a **Data de fim**. Deixe **Data de fim** vazia para ler até hoje. |

Os dias e as datas são UTC. **Dias** aceita um número inteiro. **Data de início** e **Data de fim** aceitam uma data `YYYY-MM-DD` ou uma [variável](/pt-pt/guides/workflows/manage-workflow-variables/) como `{report_start}`. O início não pode ser posterior ao fim.

Os dados diários são conservados durante 180 dias e os resumos mensais durante 25 meses.

### Destino da utilização

**Tabela de destino** recebe o resultado. O passo substitui o que a tabela continha e escreve sempre as colunas do conjunto de dados, mesmo quando não há linhas.

## Avisos

Estes não fazem o passo falhar. Este termina com o aviso e substitui a tabela na mesma, com as colunas do conjunto de dados:

| Aviso | Significado |
|---|---|
| "Usage data is not available yet: the usage database has not been set up on this workspace." | A recolha de utilização ainda não está configurada para a área de trabalho. |
| "Usage data is not available right now: the usage database could not be reached." | Não foi possível ler os dados de utilização. Execute o passo novamente mais tarde. |
| "No usage from *start* to *end*." | Não houve utilização no intervalo. |
| "Usage before *date* isn't kept, so the range was clipped to start there." | O intervalo começa antes dos dados diários que são conservados, pelo que a atividade é contada a partir de *date*. **Tendências** continua a ter os meses completos anteriores a essa data, a partir dos resumos mensais. |
| "This took too long to compute: narrow the date range." | A leitura esgotou o tempo, pelo que a tabela não tem linhas. Escolha um intervalo mais curto. |
| "Some names are unavailable right now, so those items are named by their id." | Apenas **Atividade**. Não foi possível ler alguns nomes de painéis de controlo, gráficos ou aplicações, pelo que `item_name` contém o ID. |
| "Members could not be read right now, so they are named by their id." | Apenas **Atividade**. Não foi possível ler a lista de membros, pelo que `member` contém o ID do membro e, das colunas de membros, só `user_id` está preenchida. |
| "Names are unavailable right now, so items nobody used are not listed." | Apenas **Conteúdo**. Não foi possível ler os nomes dos painéis de controlo ou das aplicações, pelo que só são listados os itens utilizados. |
| "Activity before *date* isn't kept, so items nobody used in this range can't be listed." | Apenas **Conteúdo**. O intervalo começa antes dos dados diários que são conservados, pelo que só são listados os itens utilizados. |

Quando não é possível ler a lista de membros, **Membros** falha em vez disso e deixa a tabela de destino como estava.

## Registo de segurança

Cada execução que escreve a tabela acrescenta uma entrada ao Registo de segurança que regista o conjunto de dados, o intervalo, a tabela de destino e o respetivo projeto, o fluxo de trabalho, o passo e a execução, o número de linhas escritas e, para **Atividade** e **Membros**, que as linhas contêm a identidade dos membros.

## Relacionado

- [Passos gerais](/pt-pt/reference/workflow-steps/general/)
- [Relatórios de utilização](/pt-pt/administration/access/usage-reports/)
- [Passo Get Workspace Members](/pt-pt/reference/workflow-steps/general/get-workspace-members/)
