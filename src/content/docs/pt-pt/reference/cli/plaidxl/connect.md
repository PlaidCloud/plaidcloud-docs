---
title: Iniciar sessão no PlaidXL
description: Ligue o PlaidXL à sua área de trabalho PlaidCloud com o seu e-mail e o seu início de sessão habitual, incluindo início de sessão único e autenticação de dois fatores, e depois termine a sessão ou mude de área de trabalho.
sidebar:
  label: Iniciar sessão
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

O PlaidXL inicia a sessão com a sua própria identidade, através do mesmo início de sessão que utiliza para o PlaidCloud num navegador. Não é necessário indicar o endereço de nenhum servidor nem fica guardada nenhuma palavra-passe no livro.

## Iniciar sessão

1. Abra o painel de tarefas: **PlaidCloud → Open PlaidXL** ou **Conta** no grupo **Ligar**.
2. Em **Enter your email**, introduza o endereço de e-mail que utiliza para o PlaidCloud e clique em **Sign In**. O PlaidXL memoriza o endereço para a próxima vez.
3. Se o seu e-mail pertencer a mais do que uma área de trabalho, escolha uma em **Select a workspace** e clique em **Sign In**. O PlaidXL memoriza a sua escolha. Se pertencer a uma única área de trabalho, o PlaidXL seleciona-a por si. Se nenhuma área de trabalho estiver associada ao e-mail, o painel indica-o; verifique o endereço e tente novamente.
4. O Excel pergunta se pretende permitir uma janela instantânea. Permita-a.
5. Na janela instantânea, inicie sessão da forma habitual:
   - **PlaidCloud sign-in** — o seu e-mail, a palavra-passe e qualquer código de dois fatores que tenha configurado.
   - **Single sign-on** — se já tiver sessão iniciada na sua organização, este passo é concluído automaticamente. Caso contrário, abre-se primeiro a página de início de sessão da sua organização.
6. Quando a janela instantânea indicar **Authenticated successfully**, feche-a se não se tiver fechado sozinha.

O cabeçalho do painel de tarefas mostra agora a sua área de trabalho e o projeto associado ao livro, com o menu da sua conta ao lado. Continue com [Trabalhar com tabelas e dimensões](/pt-pt/reference/cli/plaidxl/retrieve/).

Para configurar a autenticação de dois fatores ou o início de sessão único para a sua conta, consulte [Autenticação de membros](/pt-pt/administration/access/member-authentication/).

### Iniciar sessão com a sua conta Office

Se tiver sessão iniciada no Office com uma conta escolar ou profissional do Microsoft Entra ID e o PlaidXL não tiver nenhum início de sessão guardado, encontra as suas áreas de trabalho a partir dessa conta, pelo que não precisa de introduzir o e-mail:

- **Uma área de trabalho** — o PlaidXL começa a iniciar a sua sessão nessa área de trabalho. Permita a janela instantânea se o Excel o pedir; com o início de sessão único, é concluído automaticamente. No Excel para a Web, clique primeiro em **Continue as** e na sua conta.
- **Várias áreas de trabalho** — se o livro tiver sido utilizado pela última vez com uma delas, o PlaidXL inicia a sessão nessa. Caso contrário, escolha uma em **Select a workspace**.
- **Nenhuma área de trabalho** — abre-se o ecrã de e-mail com o seu endereço já preenchido.

Se iniciar sessão com um e-mail diferente do da sua conta Office, o PlaidXL indica qual é. Depois de **Log out**, o PlaidXL aguarda que seja o próprio a iniciar sessão.

### Comandos antes de iniciar sessão

Pode clicar em qualquer comando do PlaidXL no friso antes de ter iniciado sessão. O PlaidXL abre o painel de tarefas para iniciar a sua sessão ou para escolher um projeto e, depois, executa o comando na célula a partir da qual começou.

## Manter a sessão iniciada

O PlaidXL mantém a sua sessão iniciada neste computador e renova-a em segundo plano enquanto trabalha. Quando abre o painel de tarefas numa sessão posterior, vai diretamente para os seus projetos. Se o seu início de sessão tiver expirado por completo, o PlaidXL volta a pedir o seu e-mail. Um problema de rede breve durante a renovação não termina a sua sessão; o PlaidXL tenta novamente.

## O que pode ver

O PlaidXL lê com as suas permissões. Vê os projetos que pode abrir no PlaidCloud, bem como as tabelas e dimensões que contêm, e nada mais. Se faltar um projeto ou uma tabela, peça acesso a um proprietário do projeto. Consulte [Organizações e áreas de trabalho explicadas](/pt-pt/administration/access/overview/organizations-and-workspaces-explained/) para saber como funciona a pertença a uma área de trabalho.

## Terminar sessão ou mudar de área de trabalho

Clique no menu da conta (os três pontos) no canto superior direito do painel de tarefas. Mostra o seu nome e a área de trabalho, com três comandos:

- **Keyboard shortcuts** apresenta os atalhos de teclado do PlaidXL para que os possa alterar. Consulte [Atalhos de teclado](/pt-pt/reference/cli/plaidxl/ribbon/#atalhos-de-teclado).
- **Switch workspace** termina a sua sessão e regressa ao ecrã de e-mail, para que possa escolher outra área de trabalho em **Select a workspace**. Inicie sessão na nova área de trabalho quando for pedido. Voltar a uma área de trabalho em que já iniciou sessão não requer novo início de sessão, e cancelar o início de sessão mantém a área de trabalho em que estava.
- **Log out** apaga o seu início de sessão e regressa ao ecrã de e-mail.

Cada início de sessão só funciona na área de trabalho em que foi efetuado. Todos iniciam sessão uma vez após esta alteração. Quando a sua sessão está terminada, **Guardar** indica **Sign in to PlaidCloud to save.** e a obtenção de uma dimensão indica **Sign in to PlaidCloud to retrieve a dimension.**

O seu início de sessão é partilhado por todos os livros que tem abertos, mas cada livro mantém o seu próprio projeto. O projeto de um livro pertence a uma área de trabalho, pelo que, depois de mudar, um livro associado a um projeto da área de trabalho anterior fica sem projeto até escolher um. Consulte [O projeto pertence ao livro](/pt-pt/reference/cli/plaidxl/retrieve/#o-projeto-pertence-ao-livro).

## Tema claro e escuro

O painel de tarefas segue o tema do Office e muda quando o altera.

## Teclado e leitores de ecrã

As linhas das listas de projetos, tabelas e dimensões recebem o foco do teclado e respondem a **Enter** e **Space**. Um leitor de ecrã anuncia a linha selecionada, e os estados de seleção e de aviso têm um ícone além da cor.

## Relacionado

- [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/) — adicione o suplemento e abra o painel de tarefas
- [Resolução de problemas](/pt-pt/reference/cli/plaidxl/troubleshooting/) — quando a janela instantânea de início de sessão não abre ou falta uma área de trabalho
- [Ver e gerir áreas de trabalho](/pt-pt/administration/access/overview/viewing-and-managing-workspaces/) — as áreas de trabalho a que pertence
