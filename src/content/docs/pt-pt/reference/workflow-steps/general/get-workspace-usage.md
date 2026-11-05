---
title: Get Workspace Usage
description: Escreva os totais de utilização da área de trabalho dos Relatórios de utilização numa tabela do projeto, por dia ou por mês, para poder representar a adoção em gráficos ou alimentar um passo seguinte.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Descrição

Escreve um resumo da forma como a sua área de trabalho é utilizada numa tabela do projeto. Utilize-o para acompanhar a adoção ao longo do tempo, criar os seus próprios painéis de controlo sobre a utilização ou assinalar uma queda de atividade num fluxo de trabalho agendado. Os valores são os mesmos que os [Relatórios de utilização](/pt-pt/administration/access/usage-reports/) apresentam.

O resultado contém apenas totais. Nenhuma linha identifica um membro, e os caminhos de notebooks são substituídos por `*`. Os membros cuja utilização foi eliminada são excluídos.

## Configuração

### Dados de utilização

**Conjunto de dados** escolhe o que cada linha contém:

| Conjunto de dados | Uma linha por | Colunas |
|---|---|---|
| **Diário por item** | Dia, área, evento e assunto | `day`, `source`, `event`, `subject`, `events` |
| **Mensal por item** | Mês, área, evento e assunto | `month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial` |
| **Totais mensais** (predefinição) | Mês e área | `month`, `source`, `active_users`, `coverage_start`, `partial` |

`partial` é verdadeiro para um mês que o histórico não cobre na totalidade, e `coverage_start` é a data em que a recolha começou.

**Área** limita as linhas a uma área: **Aplicação PlaidCloud**, **Painéis de controlo**, **Aplicações**, **Visitas às aplicações** ou **Notebooks**. Deixe em **Todas as áreas** para incluir todas.

### Intervalo de datas

**Intervalo** escolhe os dias a ler:

- **Últimos N dias** (predefinição 30) lê os dias mais recentes, incluindo hoje.
- **Mês anterior** lê o último mês civil completo.
- **Mês até à data** lê desde o primeiro dia deste mês até hoje.
- **Entre datas** lê de **Data de início** a **Data de fim**. Deixe **Data de fim** vazia para ler até hoje.

Os dias e as datas são UTC. **Dias**, **Data de início** e **Data de fim** aceitam uma [variável](/pt-pt/guides/workflows/manage-workflow-variables/) como `{report_start}`, bem como um número ou uma data `YYYY-MM-DD`. O início não pode ser posterior ao fim.

### Destino da utilização

**Tabela de destino** recebe o resultado. O passo substitui o que a tabela continha e escreve sempre as colunas do conjunto de dados, mesmo quando não há linhas.

## Avisos

Estes não fazem o passo falhar. O passo termina com um aviso que indica o que aconteceu e escreve a tabela na mesma:

- A recolha de utilização ainda não está configurada para a área de trabalho.
- Não houve utilização no intervalo.
- O intervalo começa antes do que é conservado, pelo que foi reduzido para começar onde o histórico começa. Os dados diários são conservados durante 180 dias e os dados mensais durante 25 meses.

## Registo de segurança

Cada execução grava uma entrada no Registo de segurança com o conjunto de dados, o intervalo, a tabela de destino, o fluxo de trabalho, o passo e a execução, e o número de linhas escritas.

## Relacionados

- [Passos gerais](/pt-pt/reference/workflow-steps/general/)
- [Relatórios de utilização](/pt-pt/administration/access/usage-reports/)
- [Get Workspace Members](/pt-pt/reference/workflow-steps/general/get-workspace-members/)
