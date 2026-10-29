---
title: Ligação Tableau
description: Ligue o PlaidCloud ao Tableau Server ou ao Tableau Cloud com um token de acesso pessoal para que os fluxos de trabalho possam publicar origens de dados.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/collaboration/tableau.md
---

Uma ligação Tableau contém o endereço de um site do Tableau Server ou do Tableau Cloud e um token de acesso pessoal. O passo [Publish to Tableau](/pt-pt/reference/workflow-steps/export/export-to-tableau/) utiliza-a para publicar extrações `.hyper` como origens de dados.

## Antes de começar

No Tableau, crie um token de acesso pessoal para a conta que deve publicar: escolha **My Account Settings** e, em seguida, **Personal Access Tokens**. Copie o segredo do token quando o Tableau o mostrar, porque o Tableau não volta a mostrá-lo. A conta precisa de permissão para publicar origens de dados no projeto em que vai publicar.

## Criar a ligação

1. Abra o **Analyze**, escolha **Tools → Ligações de dados externas** e selecione **+ Nova ligação → Tableau**.
2. Introduza o nome e a descrição da ligação.
3. Introduza as definições da ligação:

| Campo | O que introduzir |
| --- | --- |
| **URL do servidor** | O endereço do servidor ou do pod do Tableau Cloud, como `https://prod-useast-a.online.tableau.com`. Um nome de anfitrião simples é interpretado como `https` e um endereço `http` é recusado. |
| **Site** | O URL de conteúdo do site, a parte do endereço do navegador depois de `#/site/`. Deixe em branco para o site Default. |
| **Nome do token de acesso pessoal** | O nome que atribuiu ao token no Tableau. |
| **Segredo do token de acesso pessoal** | O segredo do token. É guardado cifrado e aparece em branco quando volta a abrir a ligação. Deixe em branco para manter o segredo guardado. |

4. Selecione **Criar**.

O servidor tem de estar acessível a partir da Internet. O PlaidCloud não se liga a um servidor Tableau numa rede privada.

## Ver também

- [Publish to Tableau](/pt-pt/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/pt-pt/reference/workflow-steps/export/export-hyper/)
