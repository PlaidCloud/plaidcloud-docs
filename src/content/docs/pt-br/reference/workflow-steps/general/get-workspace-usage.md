---
title: Get Workspace Usage
description: Grave em uma tabela de projeto os totais de uso do espaço de trabalho dos Relatórios de uso, por dia ou mês, para acompanhar a adoção em gráficos ou alimentar uma etapa seguinte.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Descrição

Grava em uma tabela de projeto como o seu espaço de trabalho é usado. Use-a para acompanhar a adoção ao longo do tempo, relatar o uso por departamento ou equipe, criar seus próprios painéis ou sinalizar uma queda de atividade em um fluxo de trabalho agendado. Os números são os mesmos exibidos em [Relatórios de uso](/pt-br/administration/access/usage-reports/).

Três datasets contêm apenas totais: nenhuma linha nomeia um membro, e os caminhos de notebooks são substituídos por `*`. Os outros quatro (**Membros**, **Daily per member**, **Conteúdo** e **Content per member**) são criados para relatórios. **Membros**, **Daily per member** e **Content per member** contêm a identidade do membro (ID de usuário, nome de usuário, e-mail, nome, sobrenome e grupos de segurança), portanto trate a tabela de destino como trataria qualquer lista de membros. Cada execução da etapa é registrada no Log de segurança.

## Configuração

### Dados de uso

**Dataset** escolhe o que cada linha contém:

| Dataset | Uma linha para cada | Contém identidade |
|---|---|---|
| **Daily per item** | Dia, área, evento e assunto | Não |
| **Monthly per item** | Mês, área, evento e assunto | Não |
| **Monthly totals** (padrão) | Mês e área | Não |
| **Membros** | Pessoa no espaço de trabalho | Sim |
| **Daily per member** | Pessoa, dia e área | Sim |
| **Conteúdo** | Painel, aplicativo ou notebook | Não |
| **Content per member** | Pessoa e item | Sim |

**Area** limita as linhas a uma área: **Aplicativo PlaidCloud**, **Painéis**, **Aplicativos**, **App visits** ou **Notebooks**. Deixe em **All areas** para incluir todas.

### Colunas

#### Diário por item

`day`, `source`, `event`, `subject`, `events`.

#### Mensal por item

`month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial`.

#### Totais mensais

`month`, `source`, `active_users`, `coverage_start`, `partial`.

`partial` é verdadeiro para um mês que o histórico não cobre por completo, e `coverage_start` é a data em que a coleta começou. Um mês é incluído depois de encerrado e consolidado, o que leva 3 dias.

#### Colunas de membro

**Membros**, **Daily per member** e **Content per member** começam com as mesmas sete colunas:

| Coluna | Contém |
|---|---|
| `user_id` | O ID do membro. |
| `user_name` | O nome de usuário do membro. |
| `email` | O endereço de e-mail do membro, em minúsculas. |
| `first_name` | Nome. |
| `last_name` | Sobrenome. |
| `is_active` | Verdadeiro quando o membro está ativo, falso quando desativado. |
| `groups` | Os grupos de segurança do membro, separados por `; `. |

`groups` lista apenas os grupos de nível superior. Os subgrupos não são expandidos.

#### Membros

As colunas de membro, depois:

| Coluna | Contém |
|---|---|
| `first_seen` | O primeiro dia em que o membro usou o PlaidCloud, qualquer que seja o intervalo de datas. |
| `last_seen` | O último dia de atividade do membro dentro do intervalo. |
| `active_days` | Dias com atividade no intervalo. |
| `events` | Eventos de atividade no intervalo. |
| `active_minutes` | Minutos de atividade. Os minutos sobrepostos entre áreas são contados uma vez. |
| `session_minutes` | Minutos em sessões. |
| `app_open_minutes` | Minutos em que o membro manteve aplicativos Panel abertos. |

Toda pessoa do espaço de trabalho tem uma linha. Um membro sem atividade no intervalo tem valores em branco depois de `groups`. Os totais correspondem aos [Relatórios de uso](/pt-br/administration/access/usage-reports/), exceto pelos membros excluídos desde então.

#### Diário por membro

As colunas de membro, depois `day`, `source` (a área), `events`, `active_minutes`, `session_minutes`, `first_at` e `last_at` (os horários da primeira e da última atividade do dia).

#### Conteúdo

| Coluna | Contém |
|---|---|
| `type` | `dashboard`, `panel_app`, `wasm_app` ou `notebook`. |
| `subject` | O ID do item. Todos os notebooks compartilham uma linha, com `*` aqui. |
| `name` | O nome do item, ou `*` para notebooks. |
| `deleted` | Verdadeiro quando o item foi excluído desde então. |
| `users` | Membros que o abriram. |
| `opens` | Vezes em que foi aberto. |
| `last_used` | Quando foi usado pela última vez. |
| `app_open_minutes` | Minutos em que os aplicativos Panel ficaram abertos. |

#### Conteúdo por membro

As colunas de membro, depois `type`, `subject`, `name` (como em **Conteúdo**), `opens` (vezes em que este membro abriu o item) e `last_day` (o último dia de uso do membro).

### Observações sobre os datasets de membros

- A atividade de agentes, contas de serviço e membros excluídos desde então tem colunas de identidade em branco. Um membro excluído mantém o `user_id` e nada mais.
- As aberturas em **Conteúdo** podem exceder a soma das aberturas em **Content per member**. A diferença são aberturas que não podem ser atribuídas a um membro, como visualizações incorporadas ou de convidados de um painel. **Conteúdo** as conta, e **Content per member** não consegue.

### Exemplo: minutos ativos por departamento

**Membros** e **Content per member** trazem o `email` do membro, em minúsculas, para que você possa uni-los a uma tabela sua, como uma tabela mestre de RH ou da organização, e relatar por departamento.

1. Adicione uma etapa **Get Workspace Usage** com **Dataset** definido como **Membros** e uma tabela de destino como `usage_members`.
2. Adicione uma etapa **Tabela: Junção interna** que una `usage_members` à sua tabela da organização onde as colunas `email` em minúsculas correspondam. Mantenha o departamento da sua tabela e as colunas `active_minutes` e `events` de `usage_members`.
3. Na mesma etapa, agregue por departamento e some `active_minutes`.

O resultado são os minutos ativos por departamento. Os membros que não estão na sua tabela da organização ficam de fora de uma junção interna, então use uma junção à esquerda se quiser vê-los. Repita com uma segunda etapa em **Content per member** e some `opens` por departamento para relatar quem usa quais painéis e aplicativos.

### Intervalo de datas

**Range** escolhe os dias a ler:

- **Last number of days** (padrão 30) lê os dias mais recentes, incluindo hoje.
- **Previous month** lê o último mês civil completo.
- **Mês até o momento** lê do primeiro dia deste mês até hoje.
- **Between dates** lê de **Data inicial** a **Data final**. Deixe **Data final** vazia para ler até hoje.

Os dias e as datas estão em UTC. **Dias**, **Data inicial** e **Data final** aceitam uma [variável](/pt-br/guides/workflows/manage-workflow-variables/) como `{report_start}`, além de um número ou de uma data `YYYY-MM-DD`. O início não pode ser posterior ao fim.

### Destino do uso

**Tabela de destino** recebe o resultado. A etapa substitui o que a tabela continha e sempre grava as colunas do dataset, mesmo quando não há linhas.

## Avisos

Estes não fazem a etapa falhar. Ela termina com um aviso que informa o que aconteceu e ainda grava a tabela:

- A coleta de uso ainda não está configurada para o espaço de trabalho.
- Não houve uso no intervalo.
- O intervalo começa antes do que é mantido, então foi cortado para começar onde o histórico começa. Os dados diários são mantidos por 180 dias e os dados mensais por 25 meses.

## Log de segurança

Cada execução grava uma entrada no Log de segurança registrando o dataset, o intervalo, a tabela de destino, o fluxo de trabalho, a etapa e a execução, e o número de linhas gravadas.

## Relacionados

- [Etapas gerais](/pt-br/reference/workflow-steps/general/)
- [Relatórios de uso](/pt-br/administration/access/usage-reports/)
- [Get Workspace Members](/pt-br/reference/workflow-steps/general/get-workspace-members/)
