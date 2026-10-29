---
title: Crie aplicativos Panel com o Weave
description: Descreva o aplicativo que você quer, deixe o Weave escrevê-lo no Panel Studio e aprove a alteração exata antes de qualquer coisa ser salva.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/build-with-weave.md
---

O Weave pode escrever e alterar aplicativos Panel para você. Ele trabalha no [Panel Studio](/pt-br/guides/panel-apps/studio/), no aplicativo que você tem aberto, e nada do que ele propõe altera o aplicativo até você aprovar.

## Pergunte ao Weave

1. Abra o aplicativo no Panel Studio.
2. Escolha **Ask Weave** e descreva o que você quer, por exemplo "Adicione um filtro de região e um gráfico de receita por mês."

O Weave já conhece o aplicativo em que está trabalhando: seus arquivos, o status de compilação e quaisquer erros de compilação, e a tabela ou visão em que ele se baseia. Você não precisa colar código nem erros na conversa. Se uma compilação falhar, peça ao Weave que a corrija.

## Aprove a alteração

Quando o Weave quer alterar o código do aplicativo, ele mostra um cartão de aprovação com a diferença completa: cada linha que ele adiciona e remove, arquivo por arquivo.

1. Leia a diferença.
2. Escolha **Aprovar** para salvar a alteração no rascunho do aplicativo ou **Rejeitar** para descartá-la.

Aprovar salva um rascunho. Não publica. Pré-visualize o resultado e [publique](/pt-br/guides/panel-apps/studio/#publicar) quando estiver satisfeito.

### Aprovações somente na web

Você só pode aprovar uma alteração de código no PlaidCloud na web. No aplicativo móvel PlaidCloud, você pode rejeitar uma alteração de código proposta, mas não aprová-la. Outras alterações do Weave ainda podem ser aprovadas no celular. Veja [Weave no celular](/pt-br/guides/mobile-app/weave-on-mobile/).

## Próximas etapas

- [Panel Studio](/pt-br/guides/panel-apps/studio/) — Salvar, pré-visualizar e publicar.
- [O Panel App Kit](/pt-br/guides/panel-apps/app-kit/) — os componentes com que o Weave constrói.
