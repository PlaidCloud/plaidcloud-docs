---
title: Instalar o PlaidXL
description: Adicione o suplemento PlaidXL ao Excel no Windows ou no Mac, localize o separador PlaidCloud do friso e abra o painel de tarefas do PlaidXL.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

O PlaidXL instala-se uma vez por computador, não uma vez por livro. Depois disso, o separador **PlaidCloud** está no friso do Excel em todos os livros que abrir.

## Antes de começar

- Utilize o Excel para Microsoft 365, ou o Excel 2021 ou posterior, no Windows ou no Mac.
- Se a sua organização gere os suplementos do Office de forma centralizada, o administrador do Microsoft 365 poderá ter de implementar o PlaidXL por si. Se não puder instalar suplementos, peça-lhe que adicione o suplemento **PlaidCloud**.

## Instalar no Windows

1. No Excel, abra **Insert → Add-ins** (em algumas versões, **Home → Add-ins**).
2. Escreva `PlaidCloud` na caixa de pesquisa de suplementos.
3. Selecione o suplemento **PlaidCloud** e clique em **Adicionar**.

## Instalar no Mac

1. No Excel para Mac, abra **Insert → Add-ins**. Em versões mais antigas, o menu é **Insert → Store**.
2. Escreva `PlaidCloud` na caixa de pesquisa de suplementos.
3. Selecione o suplemento **PlaidCloud** e clique em **Adicionar**.

## Abrir o painel de tarefas

1. Clique no separador **PlaidCloud** do friso.
2. No grupo **PlaidXL Controls**, clique em **Show Taskpane**.

O painel de tarefas do PlaidXL abre-se no lado direito da janela e pede-lhe que inicie sessão. Continue com [Iniciar sessão](/pt-pt/reference/cli/plaidxl/connect/).

O painel de tarefas mantém a sessão iniciada entre sessões de trabalho, pelo que, normalmente, inicia sessão uma vez e depois basta abrir o painel de tarefas quando precisar.

## Se o PlaidXL não aparecer

- Feche todas as janelas do Excel e volte a abri-lo. Muitas vezes, um suplemento só aparece no friso depois de o Excel ser reiniciado.
- Procure em **Insert → My Add-ins** (Windows) ou **Insert → Add-ins → My Add-ins** (Mac) e selecione aí **PlaidCloud**.
- Se a sua organização bloquear os suplementos da loja, peça ao administrador do Microsoft 365 que o implemente.

Encontra mais soluções na página [Resolução de problemas](/pt-pt/reference/cli/plaidxl/troubleshooting/).

## Ver também

- [Iniciar sessão](/pt-pt/reference/cli/plaidxl/connect/) — ligue o suplemento à sua área de trabalho
- [O friso do PlaidCloud](/pt-pt/reference/cli/plaidxl/ribbon/) — todos os comandos do separador **PlaidCloud**
