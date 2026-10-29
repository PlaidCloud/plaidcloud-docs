---
title: Iniciar sessão no PlaidXL
description: Ligue o PlaidXL à sua área de trabalho do PlaidCloud com o seu e-mail e o seu início de sessão habitual, incluindo o início de sessão único e a autenticação de dois fatores, e depois termine a sessão ou mude de área de trabalho.
sidebar:
  label: Iniciar sessão
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

O PlaidXL inicia sessão como o próprio utilizador, com o mesmo início de sessão que usa para o PlaidCloud num navegador. Não há endereço de servidor para escrever nem palavra-passe guardada no livro.

## Iniciar sessão

1. Abra o painel de tarefas: **PlaidCloud → Show Taskpane**.
2. Em **Enter your email**, escreva o endereço de e-mail que usa para o PlaidCloud e clique em **Sign In**.
3. Se o seu e-mail pertencer a mais do que uma área de trabalho, escolha uma em **Select a tenant** e clique em **Sign In**. (No PlaidXL, um *tenant* é a sua área de trabalho do PlaidCloud.) Se pertencer a uma só área de trabalho, o PlaidXL escolhe-a por si.
4. O Excel pergunta se deve permitir uma janela de pop-up. Permita-a.
5. No pop-up, inicie sessão da forma habitual:
   - **Início de sessão do PlaidCloud** — o seu e-mail, a palavra-passe e qualquer código de dois fatores que tenha configurado.
   - **Início de sessão único** — se já tiver sessão iniciada na sua organização, este passo é concluído automaticamente. Caso contrário, abre-se primeiro a página de início de sessão da sua organização.
6. Quando o pop-up indicar **Authenticated successfully**, feche-o se não se tiver fechado sozinho.

O painel de tarefas mostra agora **Connected to** o ID da sua área de trabalho **as** o seu nome de utilizador, com os seus projetos listados abaixo. Continue com [Trabalhar com tabelas e dimensões](/pt-pt/reference/cli/plaidxl/retrieve/).

Para configurar a autenticação de dois fatores ou o início de sessão único para a sua conta, consulte [Autenticação de membros](/pt-pt/administration/access/member-authentication/).

## Manter a sessão iniciada

O PlaidXL mantém a sua sessão iniciada neste computador e renova o início de sessão em segundo plano enquanto trabalha. Quando abre o painel de tarefas numa sessão posterior, vai diretamente para os seus projetos. Se o seu início de sessão tiver expirado por completo, o PlaidXL volta a pedir o seu e-mail.

## O que pode ver

O PlaidXL lê com as suas permissões. Vê os projetos que pode abrir no PlaidCloud, bem como as tabelas e dimensões que contêm, e nada mais. Se faltar um projeto ou uma tabela, peça acesso a um proprietário do projeto. Consulte [Organizações e áreas de trabalho explicadas](/pt-pt/administration/access/overview/organizations-and-workspaces-explained/) para saber como funciona a participação numa área de trabalho.

## Terminar sessão ou mudar de área de trabalho

Clique em **Logout** na parte superior do painel de tarefas. O PlaidXL limpa o seu início de sessão e regressa ao ecrã do e-mail.

Para trabalhar numa área de trabalho diferente, termine a sessão, inicie-a novamente e escolha a outra área de trabalho em **Select a tenant**. O PlaidXL trabalha com uma área de trabalho de cada vez, para todos os livros que tenha abertos.

## Tema claro e escuro

O painel de tarefas segue o tema do Office. Para o fixar em claro ou escuro, clique no botão do sol ou da lua no canto superior esquerdo do painel de tarefas.

## Ver também

- [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/) — adicione o suplemento e abra o painel de tarefas
- [Resolução de problemas](/pt-pt/reference/cli/plaidxl/troubleshooting/) — quando o pop-up de início de sessão não abre ou falta uma área de trabalho
- [Ver e gerir áreas de trabalho](/pt-pt/administration/access/overview/viewing-and-managing-workspaces/) — as áreas de trabalho a que pertence
