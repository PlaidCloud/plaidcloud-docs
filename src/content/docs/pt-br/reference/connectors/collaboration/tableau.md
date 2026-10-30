---
title: Conexão do Tableau
description: Conecte o PlaidCloud ao Tableau Server ou ao Tableau Cloud com um token de acesso pessoal para que os fluxos de trabalho possam publicar fontes de dados.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/collaboration/tableau.md
---

Uma conexão do Tableau contém o endereço de um site do Tableau Server ou do Tableau Cloud e um token de acesso pessoal. A etapa [Publish to Tableau](/pt-br/reference/workflow-steps/export/export-to-tableau/) a usa para publicar extrações `.hyper` como fontes de dados.

## Antes de começar

No Tableau, crie um token de acesso pessoal para a conta que deve publicar: escolha **My Account Settings** e depois **Personal Access Tokens**. Copie o segredo do token quando o Tableau o exibir, porque o Tableau não o mostra novamente. A conta precisa de permissão para publicar fontes de dados no projeto em que você vai publicar.

## Criar a conexão

1. Abra **Analisar**, escolha **Tools → Conexões de dados externas** e selecione **+ Nova conexão → Tableau**.
2. Insira o nome e a descrição da conexão.
3. Insira as configurações da conexão:

| Campo | O que inserir |
| --- | --- |
| **URL do servidor** | O endereço do servidor ou do pod do Tableau Cloud, como `https://prod-useast-a.online.tableau.com`. Um host simples é lido como `https`, e um endereço `http` é recusado. |
| **Site** | A URL de conteúdo do site, a parte do endereço do navegador após `#/site/`. Deixe em branco para o site Default. |
| **Nome do token de acesso pessoal** | O nome que você deu ao token no Tableau. |
| **Segredo do token de acesso pessoal** | O segredo do token. Ele é armazenado criptografado e aparece em branco quando você reabre a conexão. Deixe em branco para manter o segredo salvo. |

4. Selecione **Criar**.

O servidor deve estar acessível pela internet. O PlaidCloud não se conecta a um servidor Tableau em uma rede privada.

## Relacionados

- [Publish to Tableau](/pt-br/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/pt-br/reference/workflow-steps/export/export-hyper/)
