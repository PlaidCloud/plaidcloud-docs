---
title: Get Workspace Usage
description: Grave o uso do espaço de trabalho em uma tabela do projeto como atividade, membros, conteúdo ou tendências, para relatar a adoção ou alimentar uma etapa posterior.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Descrição

Grava como o seu espaço de trabalho é usado em uma tabela do projeto. Use-a para acompanhar a adoção ao longo do tempo, relatar o uso por departamento ou equipe, criar seus próprios painéis ou sinalizar uma queda de atividade em um fluxo de trabalho agendado. Os números vêm dos mesmos dados de uso de [Relatórios de uso](/pt-br/administration/access/usage-reports/), e todo dataset abrange todas as áreas.

**Atividade** e **Membros** contêm a identidade do membro (ID de usuário, nome de usuário, e-mail, nome, sobrenome e grupos de segurança). A tabela de destino é uma tabela de projeto comum, e qualquer pessoa com acesso ao projeto pode lê-la: trate-a como trataria qualquer lista de membros. Cada execução que grava a tabela é registrada no Log de segurança.

## Configuração

### Dados de uso

**Dataset** define o que cada linha contém. A linha abaixo dele nomeia as linhas e as colunas do que você escolher.

| Dataset | Valor | Uma linha para cada | Contém identidade |
|---|---|---|---|
| **Atividade** (padrão) | `activity` | Dia, membro, ação e item | Sim |
| **Membros** | `members` | Membro, incluindo membros sem atividade | Sim |
| **Conteúdo** | `content` | Painel, aplicativo e notebook, incluindo painéis e aplicativos que ninguém usou | Não |
| **Tendências** | `trends` | Dia, semana e mês do intervalo | Não |

Os valores são o que uma etapa armazena quando você a cria ou edita pela API ou por um assistente de IA. Uma etapa salva com um dataset que não está nesta lista falha quando é executada, citando os quatro datasets: abra-a, escolha um **Dataset** e salve-a. Uma etapa **Membros** ou **Conteúdo** salva anteriormente continua sendo executada e grava as colunas abaixo, e uma etapa que era limitada a uma área agora abrange todas as áreas.

### Colunas

Datas e dias são gravados como carimbos de data e hora à meia-noite UTC.

#### Colunas de membro

**Atividade** e **Membros** incluem estas colunas:

| Coluna | Contém |
|---|---|
| `user_id` | O ID do membro. |
| `user_name` | O nome de usuário do membro. |
| `email` | O endereço de e-mail do membro, em minúsculas. |
| `first_name` | Nome. |
| `last_name` | Sobrenome. |
| `is_active` | Verdadeiro quando o membro está ativo, falso quando está desativado. |
| `groups` | Os grupos de segurança do membro, separados por `; `. |

`groups` lista os grupos aos quais o membro pertence diretamente. Os subgrupos não são expandidos.

#### Atividade

| Coluna | Contém |
|---|---|
| `day` | O dia. |
| As colunas de membro | Conforme acima. |
| `member` | O nome e o sobrenome do membro, ou o nome de usuário quando nenhum dos dois está definido. |
| `area` | `PlaidCloud app`, `Dashboards`, `Apps` ou `Notebooks`. |
| `action` | `Opened app`, `Opened screen`, `Opened step`, `Saved step`, `Used palette action`, `Viewed dashboard`, `Used chart`, `Opened notebook` ou `Saved notebook`. |
| `item_type` | `App area`, `Screen`, `Step`, `Palette action`, `Dashboard`, `Chart`, `App` ou `Notebook`. |
| `item_id` | O ID do item. Para um notebook, o caminho dele. |
| `item_name` | O nome do item: uma tela ou área de aplicativo em palavras, como `Members List`; o tipo de etapa; o nome do painel, do gráfico ou do aplicativo; ou o caminho do notebook. Quando não é possível encontrar um nome, o ID do item. |
| `events` | Quantas vezes o membro fez isso no dia. |
| `source` | A chave da área, como as exportações de [Relatórios de uso](/pt-br/administration/access/usage-reports/) a nomeiam. |
| `event` | A chave da ação, como as exportações a nomeiam. |

`member` e as colunas de membro dependem de quem realizou a ação:

- A atividade que não pode ser associada a nenhum membro tem `Unattributed` em `member` e as colunas de membro em branco.
- Um membro excluído desde então mantém apenas o `user_id`, e `member` é `Deleted user`.
- Qualquer outra conta, como uma conta de serviço ou um agente, mantém apenas o `user_id`, e `member` é o nome de usuário dela.

`Used chart` conta uma vez por membro e gráfico em cada janela de 5 minutos, portanto mede o uso, não as consultas.

#### Membros

| Coluna | Contém |
|---|---|
| As colunas de membro | Conforme acima. |
| `member` | O nome e o sobrenome do membro, ou o nome de usuário quando nenhum dos dois está definido. |
| `created` | O dia em que o membro foi adicionado ao espaço de trabalho, quando conhecido. |
| `status` | `Active` quando o membro esteve ativo no intervalo, `Dormant` quando ele usou o PlaidCloud antes, mas não no intervalo, `Never active` quando não há nenhum uso registrado até o fim do intervalo. |
| `first_seen` | O primeiro dia registrado em que o membro usou o PlaidCloud, independentemente do intervalo. |
| `last_seen` | O último dia de atividade do membro no intervalo. |
| `active_days` | Dias com atividade no intervalo. |
| `events` | Eventos de atividade no intervalo. |
| `active_minutes` | Minutos de atividade no intervalo. |
| `session_minutes` | Minutos em sessões no intervalo. |
| `app_open_minutes` | Minutos em que o membro manteve aplicativos Panel abertos no intervalo. As visualizações prévias do Studio não são contadas. |

Todo membro tem uma linha, inclusive os membros desativados, exceto os membros cujo uso foi apagado. Contas de serviço e agentes não são listados. Um membro sem atividade no intervalo não tem `last_seen`, e as outras colunas de atividade dele ficam em branco ou zero.

#### Conteúdo

| Coluna | Contém |
|---|---|
| `type` | `Dashboard`, `App` ou `Notebook`. |
| `item_id` | O ID do painel ou do aplicativo, ou o caminho do notebook. |
| `name` | O nome do painel ou do aplicativo, ou o caminho do notebook. Em branco quando o item foi excluído ou os nomes não podem ser lidos. |
| `deleted` | Verdadeiro quando o painel ou o aplicativo foi excluído desde então. |
| `unused` | Verdadeiro para um painel ou aplicativo que ninguém usou no intervalo. |
| `users` | Membros que o usaram no intervalo. |
| `opens` | Vezes em que foi aberto no intervalo, incluindo aberturas que não podem ser associadas a nenhum membro. |
| `last_used` | O último dia em que foi usado no intervalo. Para um item não utilizado, o último dia em que foi aberto antes do fim do intervalo, ou em branco. |
| `app_open_minutes` | Minutos em que um aplicativo Panel ficou aberto no intervalo. Em branco para painéis, notebooks e aplicativos Dash e WASM. |

Cada caminho de notebook tem a própria linha. As linhas listam primeiro o que foi usado, com mais usuários primeiro, e depois os painéis e aplicativos que ninguém usou. São os painéis publicados e os aplicativos que já existiam quando o intervalo começou. Eles só são listados quando o intervalo começa dentro dos dados diários mantidos, o uso desse tipo de item já estava sendo coletado nessa data e os nomes podem ser lidos. As visualizações prévias de aplicativos no Studio ficam de fora.

#### Tendências

| Coluna | Contém |
|---|---|
| `period` | `Day`, `Week` ou `Month`. |
| `period_start` | O primeiro dia do período. As semanas começam na segunda-feira. |
| `active_members` | Membros ativos no período, dentro do intervalo. |
| `events` | Eventos de atividade no período. |
| `active_minutes` | Minutos de atividade no período. |
| `session_minutes` | Minutos em sessões no período. |
| `active_members_7d` | Em uma linha `Day`, membros ativos nos 7 dias que terminam nesse dia. |
| `active_members_28d` | Em uma linha `Day`, membros ativos nos 28 dias que terminam nesse dia. |
| `stickiness` | Em uma linha `Day`, `active_members` dividido por `active_members_28d`. |
| `complete` | Falso para hoje, para uma semana ou um mês que contém hoje e para uma semana ou um mês que o intervalo corta. |

Todo dia do intervalo, a partir de onde começam os dados diários mantidos, tem uma linha, mesmo sem uso, assim como toda semana e todo mês em que esses dias se encaixam. `active_members_7d`, `active_members_28d` e `stickiness` ficam em branco nas linhas `Week` e `Month` e em uma linha `Day` cujos 7 ou 28 dias alcançam um período anterior aos dados diários mantidos. Um mês que começa antes dos dados diários mantidos e está inteiramente dentro do intervalo vem dos resumos mensais: ele tem `active_members`, mas eventos e minutos em branco, e `complete` informa se o resumo cobriu o mês inteiro.

### Exemplo: minutos ativos por departamento

**Atividade** e **Membros** trazem o `email` do membro, em minúsculas, para que você possa uni-los a uma tabela sua, como uma tabela mestre de RH ou da organização, e gerar relatórios por departamento.

1. Adicione uma etapa **Get Workspace Usage** com **Dataset** definido como **Membros** e uma tabela de destino como `usage_members`.
2. Adicione uma etapa **Tabela: Junção interna** que una `usage_members` à sua tabela da organização onde as colunas `email` em minúsculas coincidam. Mantenha o departamento da sua tabela e as colunas `active_minutes` e `events` de `usage_members`.
3. Na mesma etapa, agregue por departamento e some `active_minutes`.

O resultado são os minutos ativos por departamento. Os membros que não estão na sua tabela da organização ficam de fora de uma junção interna, portanto use uma junção à esquerda se quiser vê-los. Repita com uma segunda etapa em **Atividade** e some `events` por departamento e `item_name` para relatar quem usa quais painéis e aplicativos.

### Intervalo de datas

**Intervalo** define os dias a serem lidos:

| Intervalo | Valor | Lê |
|---|---|---|
| **Últimos N dias** (padrão 30) | `last_days` | Os dias mais recentes, incluindo hoje. |
| **Mês anterior** | `previous_month` | O último mês civil completo. |
| **Mês até o momento** | `month_to_date` | Do primeiro dia deste mês até hoje. |
| **Entre datas** | `dates` | De **Data inicial** até **Data final**. Deixe **Data final** vazia para ler até hoje. |

Dias e datas estão em UTC. **Dias** aceita um número inteiro. **Data inicial** e **Data final** aceitam uma data `YYYY-MM-DD` ou uma [variável](/pt-br/guides/workflows/manage-workflow-variables/) como `{report_start}`. O início não pode ser posterior ao fim.

Os dados diários são mantidos por 180 dias e os resumos mensais por 25 meses.

### Destino do uso

**Tabela de destino** recebe o resultado. A etapa substitui o que a tabela continha e sempre grava as colunas do dataset, mesmo quando não há linhas.

## Avisos

Estes casos não fazem a etapa falhar. Ela termina com o aviso e ainda substitui a tabela, com as colunas do dataset:

| Aviso | Significado |
|---|---|
| "Usage data is not available yet: the usage database has not been set up on this workspace." | A coleta de uso ainda não está configurada para o espaço de trabalho. |
| "Usage data is not available right now: the usage database could not be reached." | Não foi possível ler os dados de uso. Execute a etapa novamente mais tarde. |
| "No usage from *start* to *end*." | Não houve uso no intervalo. |
| "Usage before *date* isn't kept, so the range was clipped to start there." | O intervalo começa antes dos dados diários mantidos, por isso a atividade é contada a partir de *data*. **Tendências** ainda traz os meses completos anteriores a ela a partir dos resumos mensais. |
| "This took too long to compute: narrow the date range." | A leitura excedeu o tempo limite, por isso a tabela não tem linhas. Escolha um intervalo menor. |
| "Some names are unavailable right now, so those items are named by their id." | Somente **Atividade**. Não foi possível ler alguns nomes de painéis, gráficos ou aplicativos, por isso `item_name` contém o ID. |
| "Members could not be read right now, so they are named by their id." | Somente **Atividade**. Não foi possível ler a lista de membros, por isso `member` contém o ID do membro e, entre as colunas de membro, somente `user_id` é preenchida. |
| "Names are unavailable right now, so items nobody used are not listed." | Somente **Conteúdo**. Não foi possível ler os nomes de painéis ou aplicativos, por isso somente os itens usados são listados. |
| "Activity before *date* isn't kept, so items nobody used in this range can't be listed." | Somente **Conteúdo**. O intervalo começa antes dos dados diários mantidos, por isso somente os itens usados são listados. |

Quando não é possível ler a lista de membros, **Membros** falha e deixa a tabela de destino como estava.

## Log de segurança

Cada execução que grava a tabela adiciona uma entrada ao Log de segurança registrando o dataset, o intervalo, a tabela de destino e o projeto dela, o fluxo de trabalho, a etapa e a execução, o número de linhas gravadas e, para **Atividade** e **Membros**, que as linhas contêm identidade de membros.

## Relacionados

- [Etapas gerais](/pt-br/reference/workflow-steps/general/)
- [Relatórios de uso](/pt-br/administration/access/usage-reports/)
- [Get Workspace Members (etapa)](/pt-br/reference/workflow-steps/general/get-workspace-members/)
