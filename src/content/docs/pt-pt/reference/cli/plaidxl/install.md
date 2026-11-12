---
title: Instalar o PlaidXL
description: Adicione o suplemento PlaidXL ao Excel no Windows ou no Mac, localize o separador PlaidCloud no friso e abra o painel de tarefas do PlaidXL.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/install.md
---

O PlaidXL instala-se uma vez por computador, e não uma vez por livro. Depois disso, o separador **PlaidCloud** fica disponível no friso do Excel em todos os livros que abrir.

## Antes de começar

- Utilize o Excel para Microsoft 365, ou o Excel 2021 ou posterior, no Windows ou no Mac.
- A sua área de trabalho PlaidCloud tem de estar numa versão atual. Numa área de trabalho mais antiga, as extrações apresentam a mensagem **This PlaidCloud workspace needs an update for PlaidXL**; peça ao seu administrador que a atualize.
- Se a sua organização gere os suplementos do Office de forma centralizada, o administrador do Microsoft 365 pode ter de implementar o PlaidXL por si. Se não puder instalar suplementos, peça-lhe que adicione o suplemento **PlaidCloud**.

## Instalar no Windows

1. No Excel, abra **Inserir → Suplementos** (em algumas versões, **Base → Suplementos**).
2. Escreva `PlaidCloud` na caixa de pesquisa de suplementos.
3. Selecione o suplemento **PlaidCloud** e clique em **Adicionar**.

## Instalar no Mac

1. No Excel para Mac, abra **Inserir → Suplementos**. Nas versões mais antigas, o menu é **Inserir → Loja**.
2. Escreva `PlaidCloud` na caixa de pesquisa de suplementos.
3. Selecione o suplemento **PlaidCloud** e clique em **Adicionar**.

## Abrir o painel de tarefas

1. Clique no separador **PlaidCloud** do friso.
2. No grupo **Ligar**, clique em **Open PlaidXL**.

O painel de tarefas do PlaidXL abre-se no lado direito da janela e pede-lhe que inicie sessão. Continue com [Iniciar sessão](/pt-pt/reference/cli/plaidxl/connect/).

O painel de tarefas mantém a sessão iniciada entre sessões de utilização, pelo que, normalmente, inicia sessão uma única vez e depois basta abrir o painel de tarefas quando necessitar dele.

## Se o PlaidXL não aparecer

- Feche todas as janelas do Excel e volte a abrir o Excel. Muitas vezes, um suplemento só aparece no friso depois de o Excel ser reiniciado.
- Procure em **Inserir → Os meus suplementos** (Windows) ou **Inserir → Suplementos → Os meus suplementos** (Mac) e selecione aí **PlaidCloud**.
- Se a sua organização bloqueia os suplementos da loja, peça ao administrador do Microsoft 365 que o implemente.

Encontra mais soluções na página [Resolução de problemas](/pt-pt/reference/cli/plaidxl/troubleshooting/).

## Relacionado

- [Iniciar sessão](/pt-pt/reference/cli/plaidxl/connect/) — ligue o suplemento à sua área de trabalho
- [O friso PlaidCloud](/pt-pt/reference/cli/plaidxl/ribbon/) — todos os comandos do separador **PlaidCloud**
