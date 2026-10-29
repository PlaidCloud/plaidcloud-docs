---
title: Fazer login no PlaidXL
description: Conecte o PlaidXL ao seu espaço de trabalho do PlaidCloud com seu e-mail e o seu login habitual, incluindo logon único e autenticação de dois fatores, e depois saia ou troque de espaço de trabalho.
sidebar:
  label: Fazer login
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

O PlaidXL faz login como você, usando o mesmo login que você usa no PlaidCloud em um navegador. Não há endereço de servidor para digitar nem senha armazenada na pasta de trabalho.

## Fazer login

1. Abra o painel de tarefas: **PlaidCloud → Show Taskpane**.
2. Em **Enter your email**, digite o endereço de e-mail que você usa no PlaidCloud e clique em **Sign In**.
3. Se o seu e-mail pertencer a mais de um espaço de trabalho, escolha um em **Select a tenant** e clique em **Sign In**. (Um *tenant* no PlaidXL é o seu espaço de trabalho do PlaidCloud.) Se você pertence a um único espaço de trabalho, o PlaidXL o seleciona para você.
4. O Excel pergunta se deve permitir uma janela pop-up. Permita.
5. No pop-up, faça login da forma como você normalmente faz:
   - **Login do PlaidCloud** — seu e-mail, sua senha e qualquer código de dois fatores que você tenha configurado.
   - **Logon único** — se você já estiver conectado à sua organização, esta etapa passa direto. Caso contrário, a página de login da sua organização é aberta primeiro.
6. Quando o pop-up exibir **Authenticated successfully**, feche-o se ele não tiver se fechado sozinho.

O painel de tarefas agora mostra **Connected to** o ID do seu espaço de trabalho **as** o seu nome de usuário, com seus projetos listados abaixo. Continue com [Trabalhar com tabelas e dimensões](/pt-br/reference/cli/plaidxl/retrieve/).

Para configurar a autenticação de dois fatores ou o logon único para a sua conta, consulte [Autenticação de membros](/pt-br/administration/access/member-authentication/).

## Permanecer conectado

O PlaidXL mantém você conectado neste computador e renova o seu login em segundo plano enquanto você trabalha. Quando você abre o painel de tarefas em uma sessão posterior, ele vai direto para os seus projetos. Se o seu login tiver expirado por completo, o PlaidXL pede novamente o seu e-mail.

## O que você pode ver

O PlaidXL lê com as suas permissões. Você vê os projetos que pode abrir no PlaidCloud e as tabelas e dimensões neles, e nada além disso. Se um projeto ou uma tabela estiver faltando, peça acesso a um proprietário do projeto. Consulte [Organizações e espaços de trabalho explicados](/pt-br/administration/access/overview/organizations-and-workspaces-explained/) para saber como funciona a participação em um espaço de trabalho.

## Sair ou trocar de espaço de trabalho

Clique em **Logout** na parte superior do painel de tarefas. O PlaidXL limpa o seu login e volta para a tela de e-mail.

Para trabalhar em outro espaço de trabalho, saia, faça login novamente e escolha o outro espaço de trabalho em **Select a tenant**. O PlaidXL trabalha com um espaço de trabalho por vez, para todas as pastas de trabalho que você tiver abertas.

## Tema claro e escuro

O painel de tarefas segue o tema do seu Office. Para fixá-lo no claro ou no escuro, clique no botão de sol ou lua no canto superior esquerdo do painel de tarefas.

## Relacionados

- [Instalar o PlaidXL](/pt-br/reference/cli/plaidxl/install/) — adicione o suplemento e abra o painel de tarefas
- [Solução de problemas](/pt-br/reference/cli/plaidxl/troubleshooting/) — quando o pop-up de login não abre ou um espaço de trabalho está faltando
- [Visualização e gerenciamento de espaços de trabalho](/pt-br/administration/access/overview/viewing-and-managing-workspaces/) — os espaços de trabalho aos quais você pertence
