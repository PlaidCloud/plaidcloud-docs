---
title: Faça login no PlaidXL
description: Conecte o PlaidXL ao seu espaço de trabalho do PlaidCloud com o seu e-mail e o seu login habitual, incluindo logon único e autenticação de dois fatores, e depois saia ou troque de espaço de trabalho.
sidebar:
  label: Login
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

O PlaidXL faz login como você, usando o mesmo login que você usa no PlaidCloud em um navegador. Não há endereço de servidor para digitar nem senha armazenada na pasta de trabalho.

## Faça login

1. Abra o painel de tarefas: **PlaidCloud → Open PlaidXL**.
2. Em **Enter your email**, digite o endereço de e-mail que você usa no PlaidCloud e clique em **Sign In**. O PlaidXL se lembra do endereço para a próxima vez.
3. Se o seu e-mail pertence a mais de um espaço de trabalho, escolha um em **Select a workspace** e clique em **Sign In**. O PlaidXL se lembra da sua escolha. Se você pertence a um único espaço de trabalho, o PlaidXL o escolhe por você. Se nenhum espaço de trabalho estiver vinculado ao e-mail, o painel informa; confira o endereço e tente novamente.
4. O Excel pergunta se deve permitir uma janela pop-up. Permita.
5. No pop-up, faça login da maneira habitual:
   - **Login do PlaidCloud**: seu e-mail, sua senha e qualquer código de dois fatores que você tenha configurado.
   - **Logon único**: se você já fez login na sua organização, esta etapa passa direto. Caso contrário, a página de login da sua organização é aberta primeiro.
6. Quando o pop-up mostrar **Authenticated successfully**, feche-o, caso ele não tenha se fechado sozinho.

O cabeçalho do painel de tarefas agora mostra o seu espaço de trabalho e o projeto vinculado à pasta de trabalho, com o menu da sua conta ao lado. Continue com [Trabalhe com tabelas e dimensões](/pt-br/reference/cli/plaidxl/retrieve/).

Para configurar a autenticação de dois fatores ou o logon único para a sua conta, consulte [Autenticação de membros](/pt-br/administration/access/member-authentication/).

## Como permanecer conectado

O PlaidXL mantém você conectado neste computador e renova o seu login em segundo plano enquanto você trabalha. Quando você abre o painel de tarefas em uma sessão posterior, ele vai direto para os seus projetos. Se o seu login tiver expirado por completo, o PlaidXL pede o seu e-mail novamente. Um problema breve de rede durante a renovação do login não desconecta você; o PlaidXL tenta de novo.

## O que você pode ver

O PlaidXL lê com as suas permissões. Você vê os projetos que pode abrir no PlaidCloud e as tabelas e dimensões neles, e nada além disso. Se um projeto ou uma tabela estiver faltando, peça acesso a um proprietário do projeto. Consulte [Organizações e espaços de trabalho: explicação](/pt-br/administration/access/overview/organizations-and-workspaces-explained/) para saber como funciona a participação em espaços de trabalho.

## Saia ou troque de espaço de trabalho

Clique no menu da conta (os três pontos) no canto superior direito do painel de tarefas. Ele mostra o seu nome e o seu espaço de trabalho, com dois comandos:

- **Log out** apaga o seu login e volta para a tela de e-mail.
- **Switch workspace** desconecta você e volta para a tela de e-mail, para que você possa escolher outro espaço de trabalho em **Select a workspace**.

O seu login é compartilhado por todas as pastas de trabalho que você tem abertas, mas cada pasta de trabalho mantém o seu próprio projeto. O projeto de uma pasta de trabalho pertence a um espaço de trabalho; por isso, depois de você trocar, uma pasta de trabalho vinculada a um projeto do espaço de trabalho anterior fica sem projeto até você escolher um. Consulte [O projeto pertence à pasta de trabalho](/pt-br/reference/cli/plaidxl/retrieve/#o-projeto-pertence-à-pasta-de-trabalho).

## Tema claro e escuro

O painel de tarefas segue o tema do seu Office e muda quando você o altera.

## Teclado e leitores de tela

As linhas das listas de projetos, tabelas e dimensões recebem o foco do teclado e respondem a **Enter** e **Espaço**. Uma linha selecionada é anunciada por um leitor de tela, e os estados selecionado e de aviso têm um ícone além de uma cor.

## Relacionados

- [Instalar o PlaidXL](/pt-br/reference/cli/plaidxl/install/): adicione o suplemento e abra o painel de tarefas
- [Solução de problemas](/pt-br/reference/cli/plaidxl/troubleshooting/): quando o pop-up de login não abre ou um espaço de trabalho está faltando
- [Visualização e gerenciamento de espaços de trabalho](/pt-br/administration/access/overview/viewing-and-managing-workspaces/): os espaços de trabalho aos quais você pertence
