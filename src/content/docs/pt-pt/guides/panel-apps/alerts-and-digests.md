---
title: Alertas e resumos
description: Notifique as pessoas quando um número numa aplicação Panel ultrapassa um limite, ou envie um resumo agendado de números-chave por notificação push, correio eletrónico, Slack ou Microsoft Teams.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/alerts-and-digests.md
---

Um **alerta** vigila um número dos dados de uma aplicação Panel e avisa-o no momento em que ultrapassa um limite. Um **resumo** envia um breve sumário com até 10 números todos os dias ou todas as semanas. Ambos são configurados a partir da aplicação no [Panel Studio](/pt-pt/guides/panel-apps/studio/), e ambos são seus: só vê e altera os seus.

## Abrir alertas e resumos

1. Em **As minhas aplicações Panel** ou no quadro **Início** de um projeto, escolha **Open in Studio** na aplicação.
2. Escolha **Alerts & Digests**.

A janela tem um separador **Alerts** e um separador **Digests**. A aplicação tem de estar atribuída a um projeto, e as suas tabelas são as desse projeto.

## Definir um número a vigiar

Os alertas e os resumos medem um **KPI** que cria a partir de uma tabela do projeto da aplicação:

| Campo | O que define |
|---|---|
| **Tabela** | A tabela a ler. Tem de estar criada. |
| **Measure column** | A coluna a totalizar ou contar. |
| **Função** | `sum`, `avg`, `min`, `max`, `count` ou `count_distinct`. |
| **Adicionar filtro** | Condições opcionais que restringem as linhas, cada uma com uma coluna, uma comparação e um valor. Para *is in*, separe os valores por vírgulas. **Remove filter** remove uma. |

O número é sempre calculado com o seu próprio acesso à tabela, incluindo a [segurança ao nível da linha](/pt-pt/guides/panel-apps/accessing-data/). Nunca vê, nem envia, um valor relativo a linhas que não pode ler.

## Criar um alerta

1. No separador **Alerts**, escolha **Novo**.
2. Introduza um **Nome**.
3. Crie o KPI.
4. Em **Alert when the KPI is**, selecione `>`, `>=`, `<` ou `<=` e introduza um **Limite**.
5. Escolha como ser avisado em **Send by** (consulte [Canais](#canais)).
6. Deixe **Ativado** assinalado e escolha **Guardar**.

O PlaidCloud verifica todos os alertas ativados uma vez por hora. Um alerta dispara uma vez de cada vez que o número ultrapassa o limite e depois fica em silêncio até o número voltar ao lado seguro e o ultrapassar novamente. A lista mostra quando cada alerta disparou pela última vez e **(off)** a seguir ao nome de um que esteja desativado.

Pode ter até 20 alertas seus numa aplicação.

## Criar um resumo

1. No separador **Digests**, escolha **Novo**.
2. Introduza um **Nome**.
3. Escolha **Add KPI**, atribua-lhe uma **KPI label** e crie o número. Repita até 10 KPIs. **Remove KPI** remove um.
4. Junto a **Enviar**, selecione **Cada dia** ou **Every week**.
5. Escolha como o enviar em **Send by** e escolha **Guardar**.

Um resumo é enviado uma vez por dia ou por semana, na primeira verificação horária após o início do período, com o período em UTC. A lista mostra quando cada resumo foi enviado pela última vez. Um KPI que o seu acesso à tabela deixe sem linhas aparece como sem dados, nunca como um valor sem filtro.

Pode ter até 10 resumos seus numa aplicação e 20 no total entre aplicações.

## Canais

| Send by | Para onde vai |
|---|---|
| **Push notification** | A aplicação móvel PlaidCloud nos seus dispositivos. Apenas alertas. |
| **Correio eletrónico** | O endereço de correio eletrónico da sua conta. |
| **Slack** | Um canal do Slack, através de uma ligação ao Slack. |
| **Microsoft Teams** | Um canal do Teams, através de uma ligação ao Microsoft Teams. |

Para **Slack** e **Microsoft Teams**, escolha a **Ligação** através da qual publicar. Um administrador da área de trabalho cria a ligação, e tem de lhe ter sido concedido acesso a ela. O endereço da ligação tem de começar por `https`.

### O que mostra um cartão do Slack ou do Teams

Um cartão só mostra os valores quando o seu acesso à tabela não tem restrições, ou seja, quando nenhuma segurança ao nível da linha limita as linhas que pode ler. Se o seu acesso estiver limitado a algumas linhas, o cartão indica que há novos valores disponíveis e liga à aplicação, onde cada leitor vê apenas as linhas que o seu próprio acesso permite. Todos os cartões incluem uma ligação à aplicação. Os membros de um canal são geridos fora do PlaidCloud, razão pela qual os números de um proprietário com restrições não são enviados para um canal.

## Quando a entrega falha

Um alerta ou resumo que não possa ser entregue durante 24 horas seguidas, por exemplo porque a sua ligação ao Slack foi removida, é desativado. A lista mostra-o como **(off)** e o formulário indica quantas entregas falharam. Corrija o canal, assinale **Ativado** e escolha **Guardar** para o voltar a ativar.

## Editar ou eliminar

Escolha um item na lista para o alterar e **Guardar**. Escolha **Eliminar** para o remover. Se mudar de item com alterações por guardar, o PlaidCloud pergunta antes de as descartar.

## Passos seguintes

- [Panel Studio](/pt-pt/guides/panel-apps/studio/) — onde acede a **Alerts & Digests**.
- [O Panel App Kit](/pt-pt/guides/panel-apps/app-kit/) — crie a aplicação que os alertas vigiam.
