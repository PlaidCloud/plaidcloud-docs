---
title: Get Workspace Usage
description: Grave os totais de uso do espaço de trabalho dos Relatórios de uso em uma tabela do projeto, por dia ou mês, para criar gráficos de adoção ou alimentar uma etapa posterior.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Descrição

Grava como o seu espaço de trabalho é usado em uma tabela do projeto. Use-a para acompanhar a adoção ao longo do tempo, relatar o uso por departamento ou equipe, criar seus próprios painéis ou sinalizar uma queda de atividade em um fluxo de trabalho agendado. Os números são os mesmos exibidos em [Relatórios de uso](/pt-br/administration/access/usage-reports/).

Três datasets contêm apenas totais: nenhuma linha identifica um membro, e os caminhos de notebooks são substituídos por `*`. Os outros quatro (**Membros**, **Diário por membro**, **Conteúdo** e **Conteúdo por membro**) foram criados para geração de relatórios. **Membros**, **Diário por membro** e **Conteúdo por membro** contêm a identidade do membro (ID de usuário, nome de usuário, e-mail, nome, sobrenome e grupos de segurança), portanto trate a tabela de destino como trataria qualquer lista de membros. Cada execução da etapa é registrada no Log de segurança.

## Configuração

### Dados de uso

**Dataset** define o que cada linha contém:

| Dataset | Valor | Uma linha para cada | Contém identidade |
|---|---|---|---|
| **Diário por item** | `daily_item` | Dia, área, evento e assunto | Não |
| **Mensal por item** | `monthly_item` | Mês, área, evento e assunto | Não |
| **Totais mensais** (padrão) | `monthly_tenant` | Mês e área | Não |
| **Membros** | `members` | Pessoa no espaço de trabalho | Sim |
| **Diário por membro** | `daily_user` | Pessoa, dia e área | Sim |
| **Conteúdo** | `content` | Painel, aplicativo ou notebook | Não |
| **Conteúdo por membro** | `content_user` | Pessoa e item | Sim |

**Área** limita as linhas a uma área. Deixe em **Todas as áreas** para incluir todas.

| Área | Valor |
|---|---|
| **Todas as áreas** (padrão) | `""` |
| **Aplicativo PlaidCloud** | `plaidclient` |
| **Painéis** | `superset` |
| **Aplicativos** | `panel` |
| **Visitas a apps** | `panel_visit` |
| **Servidores de notebooks** | `jupyterhub` |
| **Notebooks** | `jupyter` |

Os valores são o que uma etapa armazena quando você a cria ou edita pela API ou por um assistente de IA.

### Colunas

#### Diário por item

`day`, `source`, `event`, `subject`, `events`.

#### Mensal por item

`month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial`.

#### Totais mensais

`month`, `source`, `active_users`, `coverage_start`, `partial`.

`partial` é verdadeiro para um mês que o histórico não cobre por completo, e `coverage_start` é a data em que a coleta começou. Um mês é incluído 3 dias após seu fechamento, quando os números já se estabilizaram.

#### Colunas de membro

**Membros**, **Diário por membro** e **Conteúdo por membro** começam com as mesmas sete colunas:

| Coluna | Contém |
|---|---|
| `user_id` | O ID do membro. |
| `user_name` | O nome de usuário do membro. |
| `email` | O endereço de e-mail do membro, em minúsculas. |
| `first_name` | Nome. |
| `last_name` | Sobrenome. |
| `is_active` | Verdadeiro quando o membro está ativo, falso quando está desativado. |
| `groups` | Os grupos de segurança do membro, separados por `; `. |

`groups` lista apenas os grupos de nível superior. Os subgrupos não são expandidos.

#### Membros

As colunas de membro, seguidas de:

| Coluna | Contém |
|---|---|
| `first_seen` | O primeiro dia em que o membro usou o PlaidCloud, independentemente do intervalo de datas. Quando você define uma **Área**, é o primeiro dia nessa área. |
| `last_seen` | O último dia de atividade do membro dentro do intervalo. |
| `active_days` | Dias com atividade no intervalo. |
| `events` | Eventos de atividade no intervalo. |
| `active_minutes` | Minutos de atividade. Minutos sobrepostos entre áreas são contados uma vez. |
| `session_minutes` | Minutos em sessões. |
| `app_open_minutes` | Minutos em que o membro manteve aplicativos Panel abertos. |

Todo membro tem uma linha, exceto os membros cujo uso foi apagado. Contas de serviço e agentes não são listados. Um membro sem atividade no intervalo tem valores em branco após `groups`. Os totais correspondem aos de [Relatórios de uso](/pt-br/administration/access/usage-reports/), exceto os de membros excluídos desde então.

#### Diário por membro

As colunas de membro, seguidas de `day`, `source` (a área), `events`, `active_minutes`, `session_minutes`, `first_at` e `last_at` (os horários da primeira e da última atividade no dia).

#### Conteúdo

| Coluna | Contém |
|---|---|
| `type` | `dashboard`, `panel_app`, `wasm_app` ou `notebook`. |
| `subject` | O ID do item. Todos os notebooks compartilham uma única linha, com `*` aqui. |
| `name` | O nome do item, ou `*` para notebooks. |
| `deleted` | Verdadeiro quando o item foi excluído desde então. |
| `users` | Membros que o abriram. |
| `opens` | Vezes em que foi aberto. |
| `last_used` | Quando foi usado pela última vez. |
| `app_open_minutes` | Minutos em que aplicativos Panel ficaram abertos. |

#### Conteúdo por membro

As colunas de membro, seguidas de `type`, `subject`, `name` (como em **Conteúdo**), `opens` (vezes em que este membro abriu o item) e `last_day` (o último dia de uso do membro).

### Observações sobre os datasets de membros

- A atividade de agentes, contas de serviço e membros excluídos desde então tem as colunas de identidade em branco. Um membro excluído mantém o `user_id` e nada mais.
- As aberturas em **Conteúdo** podem exceder a soma das aberturas em **Conteúdo por membro**. A diferença são aberturas que não podem ser atribuídas a um membro, como visualizações incorporadas ou de convidados de um painel. **Conteúdo** as conta, e **Conteúdo por membro** não consegue.

### Exemplo: minutos ativos por departamento

**Membros** e **Conteúdo por membro** trazem o `email` do membro, em minúsculas, para que você possa uni-los a uma tabela sua, como uma tabela mestre de RH ou da organização, e gerar relatórios por departamento.

1. Adicione uma etapa **Get Workspace Usage** com **Dataset** definido como **Membros** e uma tabela de destino como `usage_members`.
2. Adicione uma etapa **Tabela: Junção interna** que una `usage_members` à sua tabela da organização onde as colunas `email` em minúsculas coincidam. Mantenha o departamento da sua tabela e as colunas `active_minutes` e `events` de `usage_members`.
3. Na mesma etapa, agregue por departamento e some `active_minutes`.

O resultado são os minutos ativos por departamento. Os membros que não estão na sua tabela da organização ficam de fora de uma junção interna, portanto use uma junção à esquerda se quiser vê-los. Repita com uma segunda etapa em **Conteúdo por membro** e some `opens` por departamento para relatar quem usa quais painéis e aplicativos.

### Intervalo de datas

**Intervalo** define os dias a serem lidos:

| Intervalo | Valor | Lê |
|---|---|---|
| **Últimos N dias** (padrão 30) | `last_days` | Os dias mais recentes, incluindo hoje. |
| **Mês anterior** | `previous_month` | O último mês civil completo. |
| **Mês até o momento** | `month_to_date` | Do primeiro dia deste mês até hoje. |
| **Entre datas** | `dates` | De **Data inicial** até **Data final**. Deixe **Data final** vazia para ler até hoje. |

Dias e datas estão em UTC. **Dias**, **Data inicial** e **Data final** aceitam uma [variável](/pt-br/guides/workflows/manage-workflow-variables/) como `{report_start}`, além de um número ou de uma data `YYYY-MM-DD`. O início não pode ser posterior ao fim.

### Destino do uso

**Tabela de destino** recebe o resultado. A etapa substitui o que a tabela continha e sempre grava as colunas do dataset, mesmo quando não há linhas.

## Avisos

Estes casos não fazem a etapa falhar. Ela termina com um aviso que informa o que aconteceu e ainda grava a tabela:

- A coleta de uso ainda não está configurada para o espaço de trabalho.
- Não houve uso no intervalo.
- O intervalo começa antes do período retido, por isso foi reduzido para começar onde o histórico começa. Os dados diários são mantidos por 180 dias e os dados mensais por 25 meses.

## Log de segurança

Cada execução grava uma entrada no Log de segurança registrando o dataset, o intervalo, a tabela de destino, o fluxo de trabalho, a etapa e a execução, e o número de linhas gravadas.

## Relacionados

- [Etapas gerais](/pt-br/reference/workflow-steps/general/)
- [Relatórios de uso](/pt-br/administration/access/usage-reports/)
- [Get Workspace Members (etapa)](/pt-br/reference/workflow-steps/general/get-workspace-members/)
