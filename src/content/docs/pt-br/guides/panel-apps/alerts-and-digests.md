---
title: Alertas e resumos
description: Notifique as pessoas quando um número em um aplicativo Panel ultrapassar um limite ou envie um resumo agendado dos números principais por notificação push, e-mail, Slack ou Microsoft Teams.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/alerts-and-digests.md
---

Um **alerta** monitora um número dos dados de um aplicativo Panel e avisa você no momento em que ele ultrapassa um limite. Um **resumo** envia um breve sumário de até 10 números todos os dias ou todas as semanas. Ambos são configurados a partir do aplicativo no [Panel Studio](/pt-br/guides/panel-apps/studio/), e ambos são seus: você vê e altera somente os seus.

## Abrir alertas e resumos

1. Em **Meus aplicativos Panel** ou no quadro **Início** de um projeto, escolha **Open in Studio** no aplicativo.
2. Escolha **Alerts & Digests**.

A janela tem uma guia **Alerts** e uma guia **Digests**. O aplicativo precisa estar atribuído a um projeto, e as tabelas dele são as desse projeto.

## Definir um número a monitorar

Alertas e resumos medem um **KPI** que você cria a partir de uma tabela do projeto do aplicativo:

| Campo | O que define |
|---|---|
| **Tabela** | A tabela a ser lida. Ela precisa estar construída. |
| **Measure column** | A coluna a totalizar ou contar. |
| **Função** | `sum`, `avg`, `min`, `max`, `count` ou `count_distinct`. |
| **Adicionar filtro** | Condições opcionais que restringem as linhas, cada uma com uma coluna, uma comparação e um valor. Para *is in*, separe os valores com vírgulas. **Remove filter** remove uma condição. |

O número é sempre calculado com o seu próprio acesso à tabela, incluindo a [segurança em nível de linha](/pt-br/guides/panel-apps/accessing-data/). Você nunca vê nem envia um valor de linhas que não pode ler.

## Criar um alerta

1. Na guia **Alerts**, escolha **Novo**.
2. Informe um **Nome**.
3. Construa o KPI.
4. Em **Alert when the KPI is**, escolha `>`, `>=`, `<` ou `<=` e informe um **Limite**.
5. Escolha como ser avisado em **Send by** (veja [Canais](#canais)).
6. Deixe **Ativado** marcado e escolha **Salvar**.

O PlaidCloud verifica todos os alertas ativados uma vez por hora. Um alerta é disparado uma vez cada vez que o número ultrapassa o limite e depois fica em silêncio até o número voltar ao lado seguro e ultrapassar novamente. A lista mostra quando cada alerta foi disparado pela última vez e **(off)** após o nome de um alerta que está desativado.

Você pode ter até 20 alertas seus em um aplicativo.

## Criar um resumo

1. Na guia **Digests**, escolha **Novo**.
2. Informe um **Nome**.
3. Escolha **Add KPI**, dê a ele um **KPI label** e construa o número. Repita para até 10 KPIs. **Remove KPI** remove um.
4. Ao lado de **Enviar**, escolha **Todos os dias** ou **Toda semana**.
5. Escolha como enviá-lo em **Send by** e escolha **Salvar**.

Um resumo é enviado uma vez por dia ou por semana, na primeira verificação horária após o início do período, com o período em UTC. A lista mostra quando cada resumo foi enviado pela última vez. Um KPI cujo acesso à tabela não deixa nenhuma linha aparece como sem dados, nunca como um valor sem filtro.

Você pode ter até 10 resumos seus em um aplicativo e 20 no total entre aplicativos.

## Canais

| Send by | Para onde vai |
|---|---|
| **Notificação push** | O aplicativo móvel PlaidCloud nos seus dispositivos. Somente para alertas. |
| **E-mail** | O endereço de e-mail da sua conta. |
| **Slack** | Um canal do Slack, por meio de uma conexão do Slack. |
| **Microsoft Teams** | Um canal do Teams, por meio de uma conexão do Microsoft Teams. |

Para **Slack** e **Microsoft Teams**, escolha a **Conexão** pela qual publicar. Um administrador do espaço de trabalho cria a conexão, e você precisa ter recebido acesso a ela. O endereço da conexão deve começar com `https`.

### O que um cartão do Slack ou do Teams mostra

Um cartão mostra os valores somente quando o seu próprio acesso à tabela é irrestrito, ou seja, nenhuma segurança em nível de linha limita as linhas que você pode ler. Se o seu acesso é limitado a algumas linhas, o cartão informa que há novos valores prontos e tem um link para o aplicativo, onde cada leitor vê somente as linhas que o próprio acesso permite. Todo cartão traz um link para o aplicativo. Os membros de um canal são gerenciados fora do PlaidCloud, e é por isso que os números de um proprietário com acesso restrito não vão para um canal.

## Quando a entrega falha

Um alerta ou resumo que não pode ser entregue por 24 horas seguidas, por exemplo porque a conexão do Slack dele foi removida, é desativado. A lista o mostra como **(off)** e o formulário informa quantas entregas falharam. Corrija o canal, marque **Ativado** e escolha **Salvar** para reativá-lo.

## Editar ou excluir

Escolha um item na lista para alterá-lo e **Salvar**. Escolha **Excluir** para removê-lo. Se você trocar de item com alterações não salvas, o PlaidCloud pergunta antes de descartá-las.

## Próximas etapas

- [Panel Studio](/pt-br/guides/panel-apps/studio/) — onde você acessa **Alerts & Digests**.
- [O Panel App Kit](/pt-br/guides/panel-apps/app-kit/) — crie o aplicativo que os alertas monitoram.
