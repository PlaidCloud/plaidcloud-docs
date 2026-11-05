---
title: Get Workspace Usage
description: Grava em uma tabela de projeto os totais de uso do espaço de trabalho dos Relatórios de uso, por dia ou mês, para que você possa montar gráficos de adoção ou acionar uma etapa seguinte.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Descrição

Grava em uma tabela de projeto um resumo de como o seu espaço de trabalho é usado. Use-a para acompanhar a adoção ao longo do tempo, criar seus próprios painéis de uso ou sinalizar uma queda de atividade em um fluxo de trabalho agendado. Os números são os mesmos que os [Relatórios de uso](/pt-br/administration/access/usage-reports/) mostram.

A saída contém apenas totais. Nenhuma linha identifica um membro, e os caminhos de notebooks são substituídos por `*`. Membros cujo uso foi apagado ficam de fora.

## Configuração

### Dados de uso

**Dataset** escolhe o que cada linha contém:

| Dataset | Uma linha para cada | Colunas |
|---|---|---|
| **Diário por item** | Dia, área, evento e assunto | `day`, `source`, `event`, `subject`, `events` |
| **Mensal por item** | Mês, área, evento e assunto | `month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial` |
| **Totais mensais** (padrão) | Mês e área | `month`, `source`, `active_users`, `coverage_start`, `partial` |

`partial` é verdadeiro para um mês que o histórico não cobre por completo, e `coverage_start` é a data em que a coleta começou.

**Área** limita as linhas a uma área: **Aplicativo PlaidCloud**, **Painéis**, **Aplicativos**, **Visitas ao aplicativo** ou **Notebooks**. Deixe em **Todas as áreas** para incluir todas.

### Intervalo de datas

**Intervalo** escolhe os dias a serem lidos:

- **Número de últimos dias** (padrão 30) lê os dias mais recentes, incluindo hoje.
- **Mês anterior** lê o último mês civil completo.
- **Mês até o momento** lê do primeiro dia deste mês até hoje.
- **Entre datas** lê de **Data inicial** a **Data final**. Deixe **Data final** vazia para ler até hoje.

Os dias e as datas são UTC. **Dias**, **Data inicial** e **Data final** aceitam uma [variável](/pt-br/guides/workflows/manage-workflow-variables/) como `{report_start}`, além de um número ou de uma data `YYYY-MM-DD`. A data inicial não pode ser posterior à final.

### Destino do uso

**Tabela de destino** recebe o resultado. A etapa substitui o que a tabela continha e sempre grava as colunas do dataset, mesmo quando não há linhas.

## Avisos

Estes casos não fazem a etapa falhar. Ela termina com um aviso que informa o que aconteceu e ainda grava a tabela:

- A coleta de uso ainda não está configurada para o espaço de trabalho.
- Não houve uso no intervalo.
- O intervalo começa antes do que é mantido, então foi reduzido para começar onde o histórico começa. Os dados diários são mantidos por 180 dias e os dados mensais por 25 meses.

## Log de segurança

Cada execução grava uma entrada no Log de segurança registrando o dataset, o intervalo, a tabela de destino, o fluxo de trabalho, a etapa e a execução, e o número de linhas gravadas.

## Relacionados

- [Etapas gerais](/pt-br/reference/workflow-steps/general/)
- [Relatórios de uso](/pt-br/administration/access/usage-reports/)
- [Get Workspace Members](/pt-br/reference/workflow-steps/general/get-workspace-members/)
