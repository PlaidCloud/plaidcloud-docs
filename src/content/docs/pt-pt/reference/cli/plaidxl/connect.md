---
title: Iniciar sessão no PlaidXL
description: Ligue o PlaidXL à sua área de trabalho PlaidCloud com o seu correio eletrónico e o seu início de sessão habitual, incluindo o início de sessão único e a autenticação de dois fatores, e depois termine a sessão ou mude de área de trabalho.
sidebar:
  label: Iniciar sessão
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

O PlaidXL inicia a sessão como o próprio utilizador, através do mesmo início de sessão que utiliza para o PlaidCloud num navegador. Não é necessário escrever o endereço de nenhum servidor e não é guardada nenhuma palavra-passe no livro.

## Iniciar sessão

1. Abra o painel de tarefas: **PlaidCloud → Open PlaidXL**.
2. Em **Enter your email**, escreva o endereço de correio eletrónico que utiliza no PlaidCloud e clique em **Iniciar sessão**. O PlaidXL memoriza o endereço para a vez seguinte.
3. Se o seu correio eletrónico pertencer a mais do que uma área de trabalho, escolha uma em **Select a workspace** e clique em **Iniciar sessão**. O PlaidXL memoriza a sua escolha. Se pertencer a uma única área de trabalho, o PlaidXL escolhe-a por si. Se nenhuma área de trabalho estiver associada ao correio eletrónico, o painel indica-o; verifique o endereço e tente novamente.
4. O Excel pergunta se deve permitir uma janela instantânea. Permita-a.
5. Na janela instantânea, inicie sessão da forma habitual:
   - **Início de sessão do PlaidCloud** — o seu correio eletrónico, a palavra-passe e qualquer código de dois fatores que tenha configurado.
   - **Início de sessão único** — se já tiver sessão iniciada na sua organização, este passo é concluído automaticamente. Caso contrário, abre-se primeiro a página de início de sessão da sua organização.
6. Quando a janela instantânea indicar **Authenticated successfully**, feche-a se não se tiver fechado sozinha.

O cabeçalho do painel de tarefas mostra agora a sua área de trabalho e o projeto associado ao livro, com o menu da sua conta ao lado. Continue com [Trabalhar com tabelas e dimensões](/pt-pt/reference/cli/plaidxl/retrieve/).

Para configurar a autenticação de dois fatores ou o início de sessão único para a sua conta, consulte [Autenticação de membros](/pt-pt/administration/access/member-authentication/).

## Manter a sessão iniciada

O PlaidXL mantém a sua sessão iniciada neste computador e renova o início de sessão em segundo plano enquanto trabalha. Quando abre o painel de tarefas numa sessão posterior, este segue diretamente para os seus projetos. Se o seu início de sessão tiver expirado por completo, o PlaidXL volta a pedir o seu correio eletrónico. Um problema de rede breve durante a renovação do início de sessão não termina a sua sessão; o PlaidXL tenta novamente.

## O que pode ver

O PlaidXL lê com as suas permissões. Vê os projetos que pode abrir no PlaidCloud, bem como as tabelas e as dimensões que contêm, e nada mais. Se um projeto ou uma tabela não aparecer, peça acesso a um proprietário do projeto. Consulte [Organizações e áreas de trabalho explicadas](/pt-pt/administration/access/overview/organizations-and-workspaces-explained/) para saber como funciona a pertença a uma área de trabalho.

## Terminar sessão ou mudar de área de trabalho

Clique no menu da conta (os três pontos) no canto superior direito do painel de tarefas. Mostra o seu nome e a área de trabalho, com dois comandos:

- **Log out** limpa o seu início de sessão e regressa ao ecrã do correio eletrónico.
- **Switch workspace** termina a sua sessão e regressa ao ecrã do correio eletrónico, para que possa escolher outra área de trabalho em **Select a workspace**.

O seu início de sessão é partilhado por todos os livros que tenha abertos, mas cada livro mantém o seu próprio projeto. O projeto de um livro pertence a uma área de trabalho, pelo que, depois de mudar, um livro associado a um projeto da área de trabalho anterior fica sem projeto até escolher um. Consulte [O projeto pertence ao livro](/pt-pt/reference/cli/plaidxl/retrieve/#o-projeto-pertence-ao-livro).

## Tema claro e escuro

O painel de tarefas segue o tema do Office e muda quando o altera.

## Teclado e leitores de ecrã

As linhas das listas de projetos, tabelas e dimensões recebem o foco do teclado e respondem às teclas **Enter** e **Espaço**. Uma linha selecionada é anunciada por um leitor de ecrã, e os estados selecionado e de aviso têm um ícone além de uma cor.

## Relacionado

- [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/) — adicione o suplemento e abra o painel de tarefas
- [Resolução de problemas](/pt-pt/reference/cli/plaidxl/troubleshooting/) — quando a janela instantânea de início de sessão não abre ou falta uma área de trabalho
- [Ver e gerir áreas de trabalho](/pt-pt/administration/access/overview/viewing-and-managing-workspaces/) — as áreas de trabalho a que pertence
