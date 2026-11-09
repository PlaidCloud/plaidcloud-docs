---
title: Get Workspace Usage
description: Escreva numa tabela do projeto os totais de utilização da área de trabalho dos Relatórios de utilização, por dia ou por mês, para poder representar a adoção em gráficos ou alimentar um passo seguinte.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Descrição

Escreve numa tabela do projeto a forma como a área de trabalho é utilizada. Utilize-o para acompanhar a adoção ao longo do tempo, para reportar a utilização por departamento ou equipa, para criar os seus próprios painéis de controlo ou para assinalar uma queda de atividade num fluxo de trabalho agendado. Os valores são os mesmos que os [Relatórios de utilização](/pt-pt/administration/access/usage-reports/) apresentam.

Três conjuntos de dados contêm apenas totais: nenhuma linha identifica um membro e os caminhos dos notebooks são substituídos por `*`. Os outros quatro (**Membros**, **Diário por membro**, **Conteúdo** e **Conteúdo por membro**) destinam-se a relatórios. **Membros**, **Diário por membro** e **Conteúdo por membro** contêm a identidade dos membros (ID de utilizador, nome de utilizador, correio eletrónico, nome próprio, apelido e grupos de segurança), pelo que deve tratar a tabela de destino como trataria qualquer lista de membros. Cada execução do passo fica registada no Registo de segurança.

## Configuração

### Dados de utilização

**Conjunto de dados** escolhe o que cada linha contém:

| Conjunto de dados | Uma linha por | Contém identidade |
|---|---|---|
| **Diário por item** | Dia, área, evento e assunto | Não |
| **Mensal por item** | Mês, área, evento e assunto | Não |
| **Totais mensais** (predefinição) | Mês e área | Não |
| **Membros** | Pessoa na área de trabalho | Sim |
| **Diário por membro** | Pessoa, dia e área | Sim |
| **Conteúdo** | Painel de controlo, aplicação ou notebook | Não |
| **Conteúdo por membro** | Pessoa e item | Sim |

**Área** limita as linhas a uma área: **Aplicação PlaidCloud**, **Painéis de controlo**, **Aplicações**, **Visitas às aplicações** ou **Notebooks**. Deixe em **Todas as áreas** para incluir todas.

### Colunas

#### Diário por item

`day`, `source`, `event`, `subject`, `events`.

#### Mensal por item

`month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial`.

#### Totais mensais

`month`, `source`, `active_users`, `coverage_start`, `partial`.

`partial` é verdadeiro para um mês que o histórico não cobre na totalidade e `coverage_start` é a data em que a recolha começou. Um mês é incluído depois de fechado e estabilizado, o que demora 3 dias.

#### Colunas de membros

**Membros**, **Diário por membro** e **Conteúdo por membro** começam com as mesmas sete colunas:

| Coluna | Contém |
|---|---|
| `user_id` | O ID do membro. |
| `user_name` | O nome de utilizador do membro. |
| `email` | O endereço de correio eletrónico do membro, em minúsculas. |
| `first_name` | Nome próprio. |
| `last_name` | Apelido. |
| `is_active` | Verdadeiro quando o membro está ativo, falso quando está desativado. |
| `groups` | Os grupos de segurança do membro, separados por `; `. |

`groups` lista apenas os grupos de nível superior. Os subgrupos não são expandidos.

#### Membros

As colunas de membros, seguidas de:

| Coluna | Contém |
|---|---|
| `first_seen` | O primeiro dia em que o membro utilizou o PlaidCloud, independentemente do intervalo de datas. |
| `last_seen` | O último dia de atividade do membro dentro do intervalo. |
| `active_days` | Dias com atividade no intervalo. |
| `events` | Eventos de atividade no intervalo. |
| `active_minutes` | Minutos de atividade. Os minutos sobrepostos entre áreas são contados uma só vez. |
| `session_minutes` | Minutos em sessões. |
| `app_open_minutes` | Minutos em que o membro teve aplicações Panel abertas. |

Todas as pessoas da área de trabalho têm uma linha. Um membro sem atividade no intervalo tem valores em branco depois de `groups`. Os totais coincidem com os [Relatórios de utilização](/pt-pt/administration/access/usage-reports/), exceto no caso de membros entretanto eliminados.

#### Diário por membro

As colunas de membros, seguidas de `day`, `source` (a área), `events`, `active_minutes`, `session_minutes`, `first_at` e `last_at` (as horas da primeira e da última atividade nesse dia).

#### Conteúdo

| Coluna | Contém |
|---|---|
| `type` | `dashboard`, `panel_app`, `wasm_app` ou `notebook`. |
| `subject` | O ID do item. Todos os notebooks partilham uma só linha, com `*` aqui. |
| `name` | O nome do item ou `*` para notebooks. |
| `deleted` | Verdadeiro quando o item foi entretanto eliminado. |
| `users` | Membros que o abriram. |
| `opens` | Número de vezes que foi aberto. |
| `last_used` | Quando foi utilizado pela última vez. |
| `app_open_minutes` | Minutos em que as aplicações Panel estiveram abertas. |

#### Conteúdo por membro

As colunas de membros, seguidas de `type`, `subject`, `name` (como em **Conteúdo**), `opens` (número de vezes que este membro abriu o item) e `last_day` (o último dia de utilização do membro).

### Notas sobre os conjuntos de dados de membros

- A atividade de agentes, contas de serviço e membros entretanto eliminados tem as colunas de identidade em branco. Um membro eliminado mantém o `user_id` e mais nada.
- As aberturas em **Conteúdo** podem exceder a soma das aberturas em **Conteúdo por membro**. A diferença corresponde a aberturas que não podem ser atribuídas a um membro, como as visualizações incorporadas ou de convidados de um painel de controlo. **Conteúdo** conta-as e **Conteúdo por membro** não pode contá-las.

### Exemplo: minutos ativos por departamento

**Membros** e **Conteúdo por membro** incluem o `email` do membro, em minúsculas, pelo que pode associá-los a uma tabela própria, como uma tabela mestre de RH ou da organização, e reportar por departamento.

1. Adicione um passo **Get Workspace Usage** com **Conjunto de dados** definido como **Membros** e uma tabela de destino como `usage_members`.
2. Adicione um passo **Tabela: Junção interna** que junte `usage_members` à sua tabela da organização onde as colunas `email` em minúsculas coincidam. Mantenha o departamento da sua tabela e as colunas `active_minutes` e `events` de `usage_members`.
3. No mesmo passo, agregue por departamento e some `active_minutes`.

O resultado são os minutos ativos por departamento. Os membros que não estão na tabela da organização desaparecem numa junção interna, pelo que deve utilizar uma junção à esquerda se quiser vê-los. Repita com um segundo passo sobre **Conteúdo por membro** e some `opens` por departamento para reportar quem utiliza que painéis de controlo e aplicações.

### Intervalo de datas

**Intervalo** escolhe os dias a ler:

- **Último número de dias** (predefinição 30) lê os dias mais recentes, incluindo hoje.
- **Mês anterior** lê o último mês civil completo.
- **Mês até à data** lê desde o primeiro dia deste mês até hoje.
- **Entre datas** lê desde **Data de início** até **Data de fim**. Deixe **Data de fim** vazia para ler até hoje.

Os dias e as datas são UTC. **Dias**, **Data de início** e **Data de fim** aceitam uma [variável](/pt-pt/guides/workflows/manage-workflow-variables/) como `{report_start}`, bem como um número ou uma data `YYYY-MM-DD`. O início não pode ser posterior ao fim.

### Destino da utilização

**Tabela de destino** recebe o resultado. O passo substitui o que a tabela continha e escreve sempre as colunas do conjunto de dados, mesmo quando não há linhas.

## Avisos

Estes não fazem o passo falhar. Este termina com um aviso que indica o que aconteceu e escreve a tabela na mesma:

- A recolha de utilização ainda não está configurada para a área de trabalho.
- Não houve utilização no intervalo.
- O intervalo começa antes do que é conservado, pelo que foi cortado para começar onde o histórico começa. Os dados diários são conservados durante 180 dias e os dados mensais durante 25 meses.

## Registo de segurança

Cada execução escreve uma entrada no Registo de segurança que regista o conjunto de dados, o intervalo, a tabela de destino, o fluxo de trabalho, o passo e a execução, e o número de linhas escritas.

## Relacionado

- [Passos gerais](/pt-pt/reference/workflow-steps/general/)
- [Relatórios de utilização](/pt-pt/administration/access/usage-reports/)
- [Get Workspace Members](/pt-pt/reference/workflow-steps/general/get-workspace-members/)
