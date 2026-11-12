---
title: Iniciar sessão no PlaidXL
description: Ligue o PlaidXL à sua área de trabalho PlaidCloud com o seu email e o seu início de sessão habitual, incluindo início de sessão único e autenticação de dois fatores, e depois termine a sessão ou mude de área de trabalho.
sidebar:
  label: Iniciar sessão
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

O PlaidXL inicia sessão em seu nome, com o mesmo início de sessão que utiliza no PlaidCloud num navegador. Não é necessário indicar o endereço de nenhum servidor e não fica guardada nenhuma palavra-passe no livro.

## Iniciar sessão

1. Abra o painel de tarefas: **PlaidCloud → Open PlaidXL** ou **Conta** no grupo **Ligar**.
2. Em **Enter your email**, escreva o endereço de email que utiliza no PlaidCloud e clique em **Sign In**. O PlaidXL memoriza o endereço para a vez seguinte.
3. Se o seu email pertencer a mais do que uma área de trabalho, escolha uma em **Select a workspace** e clique em **Sign In**. O PlaidXL memoriza a sua escolha. Se pertencer a uma única área de trabalho, o PlaidXL seleciona-a por si. Se nenhuma área de trabalho estiver associada ao email, o painel indica-o; verifique o endereço e tente novamente.
4. O Excel pergunta se pretende permitir uma janela de pop-up. Permita-a.
5. No pop-up, inicie sessão da forma habitual:
   - **PlaidCloud sign-in** — o seu email, a palavra-passe e qualquer código de dois fatores que tenha configurado.
   - **Single sign-on** — se já tiver sessão iniciada na sua organização, este passo é concluído automaticamente. Caso contrário, abre-se primeiro a página de início de sessão da sua organização.
6. Quando o pop-up indicar **Authenticated successfully**, feche-o se ainda não se tiver fechado sozinho.

O cabeçalho do painel de tarefas mostra agora a sua área de trabalho e o projeto associado ao livro, com o menu da sua conta ao lado. Continue em [Trabalhar com tabelas e dimensões](/pt-pt/reference/cli/plaidxl/retrieve/).

Para configurar a autenticação de dois fatores ou o início de sessão único para a sua conta, consulte [Autenticação de membros](/pt-pt/administration/access/member-authentication/).

### Iniciar sessão com a sua conta do Office

Se tiver sessão iniciada no Office com uma conta profissional do Microsoft Entra ID e o PlaidXL não tiver nenhum início de sessão guardado, encontra as suas áreas de trabalho a partir dessa conta, pelo que não precisa de escrever o email:

- **Uma área de trabalho** — o PlaidXL começa a iniciar sessão nela. Permita o pop-up se o Excel o pedir; com o início de sessão único, é concluído automaticamente. No Excel na Web, clique primeiro em **Continue as** e na sua conta.
- **Várias áreas de trabalho** — se o livro foi utilizado pela última vez com uma delas, o PlaidXL inicia sessão nessa. Caso contrário, escolha uma em **Select a workspace**.
- **Nenhuma área de trabalho** — abre-se o ecrã de email com o seu endereço já preenchido.

Se iniciar sessão com um email diferente do da sua conta do Office, o PlaidXL indica qual. Depois de **Log out**, o PlaidXL aguarda que seja você a iniciar sessão.

### Comandos antes de iniciar sessão

Pode clicar em qualquer comando do PlaidXL na faixa de opções antes de iniciar sessão. O PlaidXL abre o painel de tarefas para iniciar sessão ou para escolher um projeto e, depois, executa o comando na célula a partir da qual começou.

## Manter a sessão iniciada

O PlaidXL mantém a sua sessão iniciada neste computador e renova o início de sessão em segundo plano enquanto trabalha. Quando abre o painel de tarefas numa sessão posterior, segue diretamente para os seus projetos. Se o seu início de sessão tiver expirado por completo, o PlaidXL pede novamente o seu email. Um problema de rede breve durante a renovação do início de sessão não termina a sua sessão; o PlaidXL tenta de novo.

## O que pode ver

O PlaidXL lê com as suas permissões. Vê os projetos que pode abrir no PlaidCloud e as tabelas e dimensões que contêm, e nada mais. Se um projeto ou uma tabela não aparecer, peça acesso a um proprietário do projeto. Consulte [Organizações e áreas de trabalho explicadas](/pt-pt/administration/access/overview/organizations-and-workspaces-explained/) para perceber como funciona a participação numa área de trabalho.

## Terminar a sessão ou mudar de área de trabalho

Clique no menu da conta (os três pontos) no canto superior direito do painel de tarefas. Mostra o seu nome e a área de trabalho, com três comandos:

- **Keyboard shortcuts** apresenta os atalhos do PlaidXL para que os possa alterar. Consulte [Atalhos de teclado](/pt-pt/reference/cli/plaidxl/ribbon/#atalhos-de-teclado).
- **Switch workspace** termina a sua sessão e regressa ao ecrã de email, para que possa escolher outra área de trabalho em **Select a workspace**. Inicie sessão na nova área de trabalho quando lhe for pedido. Voltar a uma área de trabalho na qual já iniciou sessão não exige novo início de sessão, e cancelar o início de sessão mantém a área de trabalho em que estava.
- **Log out** limpa o seu início de sessão e regressa ao ecrã de email.

Cada início de sessão só funciona para a área de trabalho em que foi feito. Todos iniciam sessão uma vez após esta alteração. Quando a sessão não está iniciada, **Guardar** indica **Sign in to PlaidCloud to save.** e obter uma dimensão indica **Sign in to PlaidCloud to retrieve a dimension.**

O seu início de sessão é partilhado por todos os livros que tenha abertos, mas cada livro mantém o seu próprio projeto. O projeto de um livro pertence a uma área de trabalho, pelo que, depois de mudar, um livro associado a um projeto da área de trabalho anterior fica sem projeto até escolher um. Consulte [O projeto pertence ao livro](/pt-pt/reference/cli/plaidxl/retrieve/#o-projeto-pertence-ao-livro).

## Tema claro e escuro

O painel de tarefas corresponde à aplicação Web do PlaidCloud, com azul da marca, separadores e listas em estilo de barra lateral, e tabelas, dimensões, projetos e colunas em cartões delimitados com deslocamento. Segue o tema do Office e muda quando o altera. Num painel estreito, os separadores ficam três por linha, em duas linhas; a partir de 560 píxeis de largura, ficam numa única linha.

## Teclado e leitores de ecrã

As linhas das listas de projetos, tabelas e dimensões recebem o foco do teclado e respondem a **Enter** e **Espaço**. Um leitor de ecrã anuncia a linha selecionada, os estados selecionado e de aviso incluem um ícone além da cor, e o controlo com foco do teclado tem um anel de foco bem visível.

## Números

Todos os números que o painel de tarefas mostra, como as contagens de linhas e colunas e as mensagens de atualização, recálculo, Explain, Formulas, Report e planeamento, seguem o idioma de apresentação do Excel. O Excel alemão mostra, por exemplo, 4.812.233. Os valores escritos nas células não mudam.

## Relacionado

- [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/) — adicione o suplemento e abra o painel de tarefas
- [Resolução de problemas](/pt-pt/reference/cli/plaidxl/troubleshooting/) — quando o pop-up de início de sessão não abre ou falta uma área de trabalho
- [Ver e gerir áreas de trabalho](/pt-pt/administration/access/overview/viewing-and-managing-workspaces/) — as áreas de trabalho a que pertence
