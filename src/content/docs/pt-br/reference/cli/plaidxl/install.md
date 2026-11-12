---
title: Instalar o PlaidXL
description: Adicione o suplemento PlaidXL ao Excel no Windows ou no Mac, encontre a guia PlaidCloud na faixa de opções e abra o painel de tarefas do PlaidXL.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

Você instala o PlaidXL uma vez por computador, não uma vez por pasta de trabalho. Depois disso, a guia **PlaidCloud** fica na faixa de opções do Excel em todas as pastas de trabalho que você abrir.

## Antes de começar

- Use o Excel para Microsoft 365, ou o Excel 2021 ou posterior, no Windows ou no Mac.
- Seu espaço de trabalho do PlaidCloud precisa estar em uma versão atual. Em um espaço de trabalho mais antigo, as extrações exibem **This PlaidCloud workspace needs an update for PlaidXL**; peça ao seu administrador que o atualize.
- Se sua organização gerencia os suplementos do Office de forma centralizada, talvez o administrador do Microsoft 365 precise implantar o PlaidXL para você. Se você não consegue instalar suplementos por conta própria, peça a ele que adicione o suplemento **PlaidCloud**.

## Instalar no Windows

1. No Excel, abra **Insert → Add-ins** (em algumas versões, **Home → Add-ins**).
2. Digite `PlaidCloud` na caixa de pesquisa de suplementos.
3. Selecione o suplemento **PlaidCloud** e clique em **Adicionar**.

## Instalar no Mac

1. No Excel para Mac, abra **Insert → Add-ins**. Em versões mais antigas, o menu é **Insert → Store**.
2. Digite `PlaidCloud` na caixa de pesquisa de suplementos.
3. Selecione o suplemento **PlaidCloud** e clique em **Adicionar**.

## Abrir o painel de tarefas

1. Clique na guia **PlaidCloud** na faixa de opções.
2. No grupo **Conectar**, clique em **Open PlaidXL**.

O painel de tarefas do PlaidXL abre no lado direito da janela e pede que você faça login. Continue em [Fazer login](/pt-br/reference/cli/plaidxl/connect/).

O painel de tarefas continua conectado entre as sessões, então você normalmente faz login uma vez e depois só abre o painel de tarefas quando precisar dele.

## Se o PlaidXL não aparecer

- Feche todas as janelas do Excel e reabra o Excel. Muitas vezes um suplemento só aparece na faixa de opções depois que o Excel é reiniciado.
- Procure em **Insert → My Add-ins** (Windows) ou **Insert → Add-ins → My Add-ins** (Mac) e selecione **PlaidCloud** por lá.
- Se sua organização bloqueia suplementos da loja, peça ao administrador do Microsoft 365 que o implante.

Mais soluções estão na página [Solução de problemas](/pt-br/reference/cli/plaidxl/troubleshooting/).

## Relacionado

- [Fazer login](/pt-br/reference/cli/plaidxl/connect/) — conecte o suplemento ao seu espaço de trabalho
- [A faixa de opções do PlaidCloud](/pt-br/reference/cli/plaidxl/ribbon/) — todos os comandos da guia **PlaidCloud**
