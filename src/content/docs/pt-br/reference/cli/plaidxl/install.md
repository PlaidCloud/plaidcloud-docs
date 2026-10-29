---
title: Instalar o PlaidXL
description: Adicione o suplemento PlaidXL ao Excel no Windows ou Mac, encontre a guia PlaidCloud da faixa de opções e abra o painel de tarefas do PlaidXL.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

Você instala o PlaidXL uma vez por computador, não uma vez por pasta de trabalho. Depois disso, a guia **PlaidCloud** fica na faixa de opções do Excel em todas as pastas de trabalho que você abrir.

## Antes de começar

- Use o Excel para Microsoft 365, ou o Excel 2021 ou posterior, no Windows ou Mac.
- Se a sua organização gerencia os suplementos do Office de forma centralizada, talvez o administrador do Microsoft 365 precise implantar o PlaidXL para você. Se você não conseguir instalar suplementos por conta própria, peça a ele que adicione o suplemento **PlaidCloud**.

## Instalar no Windows

1. No Excel, abra **Insert → Add-ins** (em algumas versões, **Home → Add-ins**).
2. Digite `PlaidCloud` na caixa de pesquisa de suplementos.
3. Selecione o suplemento **PlaidCloud** e clique em **Adicionar**.

## Instalar no Mac

1. No Excel para Mac, abra **Insert → Add-ins**. Em versões mais antigas, o menu é **Insert → Store**.
2. Digite `PlaidCloud` na caixa de pesquisa de suplementos.
3. Selecione o suplemento **PlaidCloud** e clique em **Adicionar**.

## Abrir o painel de tarefas

1. Clique na guia **PlaidCloud** da faixa de opções.
2. No grupo **PlaidXL Controls**, clique em **Show Taskpane**.

O painel de tarefas do PlaidXL abre no lado direito da janela e pede que você faça login. Continue com [Fazer login](/pt-br/reference/cli/plaidxl/connect/).

O painel de tarefas permanece conectado entre sessões, então normalmente você faz login uma vez e depois apenas abre o painel de tarefas quando precisar dele.

## Se o PlaidXL não aparecer

- Feche todas as janelas do Excel e abra o Excel novamente. Muitas vezes um suplemento não aparece na faixa de opções até o Excel ser reiniciado.
- Procure em **Insert → My Add-ins** (Windows) ou **Insert → Add-ins → My Add-ins** (Mac) e selecione **PlaidCloud** a partir de lá.
- Se a sua organização bloqueia suplementos da loja, peça ao administrador do Microsoft 365 que o implante.

Há mais soluções na página [Solução de problemas](/pt-br/reference/cli/plaidxl/troubleshooting/).

## Relacionados

- [Fazer login](/pt-br/reference/cli/plaidxl/connect/) — conecte o suplemento ao seu espaço de trabalho
- [A faixa de opções do PlaidCloud](/pt-br/reference/cli/plaidxl/ribbon/) — todos os comandos da guia **PlaidCloud**
