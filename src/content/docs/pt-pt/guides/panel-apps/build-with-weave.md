---
title: Criar aplicações Panel com o Weave
description: Descreva a aplicação que pretende, deixe o Weave escrevê-la no Panel Studio e aprove a alteração exata antes de qualquer coisa ser guardada.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/build-with-weave.md
---

O Weave pode escrever e alterar aplicações Panel por si. Trabalha no [Panel Studio](/pt-pt/guides/panel-apps/studio/) na aplicação que tem aberta, e nada do que propõe altera a aplicação até o aprovar.

## Perguntar ao Weave

1. Abra a aplicação no Panel Studio.
2. Escolha **Ask Weave** e descreva o que pretende, por exemplo "Add a region filter and a chart of revenue by month."

O Weave já conhece a aplicação em que está a trabalhar: os seus ficheiros, o estado da compilação e quaisquer erros de compilação, e a tabela ou vista em que se baseia. Não precisa de colar código nem erros na conversa. Se uma compilação falhar, peça ao Weave que a corrija.

## Aprovar a alteração

Quando o Weave quer alterar o código da aplicação, mostra um cartão de aprovação com a diferença completa: cada linha que adiciona e remove, ficheiro a ficheiro.

1. Leia a diferença.
2. Escolha **Aprovar** para guardar a alteração no rascunho da aplicação, ou **Rejeitar** para a descartar.

Aprovar guarda um rascunho. Não publica. Pré-visualize o resultado e depois [publique](/pt-pt/guides/panel-apps/studio/#publicar) quando estiver satisfeito.

### As aprovações só são possíveis na Web

Só pode aprovar uma alteração de código no PlaidCloud na Web. Na aplicação móvel PlaidCloud pode rejeitar uma alteração de código proposta, mas não aprová-la. As outras alterações do Weave continuam a poder ser aprovadas no telemóvel. Consulte [Weave no telemóvel](/pt-pt/guides/mobile-app/weave-on-mobile/).

## Passos seguintes

- [Panel Studio](/pt-pt/guides/panel-apps/studio/) — Guardar, Pré-visualizar e Publicar.
- [O Panel App Kit](/pt-pt/guides/panel-apps/app-kit/) — os componentes com que o Weave constrói.
