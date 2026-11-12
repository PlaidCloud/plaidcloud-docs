---
title: Entrar no PlaidXL
description: Conecte o PlaidXL ao seu espaço de trabalho do PlaidCloud com seu e-mail e seu login habitual, incluindo logon único e autenticação de dois fatores, e depois saia ou troque de espaço de trabalho.
sidebar:
  label: Entrar
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

O PlaidXL conecta você como você mesmo, usando o mesmo login que você usa no PlaidCloud em um navegador. Não há endereço de servidor para digitar nem senha armazenada na pasta de trabalho.

## Entrar

1. Abra o painel de tarefas: **PlaidCloud → Open PlaidXL** ou **Conta** no grupo **Conectar**.
2. Em **Enter your email**, digite o endereço de e-mail que você usa no PlaidCloud e clique em **Sign In**. O PlaidXL lembra o endereço para a próxima vez.
3. Se o seu e-mail pertence a mais de um espaço de trabalho, escolha um em **Select a workspace** e clique em **Sign In**. O PlaidXL lembra sua escolha. Se você pertence a um único espaço de trabalho, o PlaidXL o seleciona para você. Se nenhum espaço de trabalho estiver vinculado ao e-mail, o painel informa; confira o endereço e tente novamente.
4. O Excel pergunta se deve permitir uma janela pop-up. Permita.
5. No pop-up, entre da maneira habitual:
   - **Login do PlaidCloud** — seu e-mail, sua senha e qualquer código de dois fatores que você tenha configurado.
   - **Logon único** — se você já estiver conectado à sua organização, esta etapa passa direto. Caso contrário, a página de login da sua organização abre primeiro.
6. Quando o pop-up exibir **Authenticated successfully**, feche-o se ele não tiver fechado sozinho.

O cabeçalho do painel de tarefas agora mostra seu espaço de trabalho e o projeto vinculado à pasta de trabalho, com o menu da sua conta ao lado. Continue com [Trabalhar com tabelas e dimensões](/pt-br/reference/cli/plaidxl/retrieve/).

Para configurar a autenticação de dois fatores ou o logon único para a sua conta, consulte [Autenticação de membros](/pt-br/administration/access/member-authentication/).

### Entrar com sua conta do Office

Se você está conectado ao Office com uma conta corporativa do Microsoft Entra ID e o PlaidXL não tem nenhum login salvo, ele encontra seus espaços de trabalho a partir dessa conta, então você não precisa digitar seu e-mail:

- **Um espaço de trabalho** — o PlaidXL começa a conectar você a ele. Permita o pop-up se o Excel perguntar; com logon único, ele passa direto. No Excel na web, clique primeiro em **Continue as** com sua conta.
- **Vários espaços de trabalho** — se a pasta de trabalho foi usada pela última vez com um deles, o PlaidXL conecta você a esse. Caso contrário, escolha um em **Select a workspace**.
- **Nenhum espaço de trabalho** — a tela de e-mail abre com o seu endereço preenchido.

Se você entrar com um e-mail diferente do da sua conta do Office, o PlaidXL informa qual é. Depois de **Log out**, o PlaidXL espera que você mesmo faça o login.

### Comandos antes de entrar

Você pode clicar em qualquer comando do PlaidXL na faixa de opções antes de entrar. O PlaidXL abre o painel de tarefas para você entrar, ou para escolher um projeto, e depois executa o comando na célula em que você começou.

## Permanecer conectado

O PlaidXL mantém você conectado neste computador e renova seu login em segundo plano enquanto você trabalha. Quando você abre o painel de tarefas em uma sessão posterior, ele vai direto para os seus projetos. Se o seu login expirou completamente, o PlaidXL pede seu e-mail novamente. Um problema de rede breve durante a renovação do login não desconecta você; o PlaidXL tenta de novo.

## O que você pode ver

O PlaidXL lê com as suas permissões. Você vê os projetos que pode abrir no PlaidCloud, e as tabelas e dimensões neles, e nada além disso. Se um projeto ou uma tabela estiver faltando, peça acesso a um proprietário do projeto. Consulte [Organizações e espaços de trabalho explicados](/pt-br/administration/access/overview/organizations-and-workspaces-explained/) para saber como funciona a associação a um espaço de trabalho.

## Sair ou trocar de espaço de trabalho

Clique no menu da conta (os três pontos) no canto superior direito do painel de tarefas. Ele mostra seu nome e seu espaço de trabalho, com três comandos:

- **Keyboard shortcuts** lista os atalhos do PlaidXL para que você possa alterá-los. Consulte [Atalhos de teclado](/pt-br/reference/cli/plaidxl/ribbon/#atalhos-de-teclado).
- **Switch workspace** desconecta você e volta para a tela de e-mail, para que você possa escolher outro espaço de trabalho em **Select a workspace**. Entre no novo espaço de trabalho quando solicitado. Voltar para um espaço de trabalho em que você já entrou não exige novo login, e cancelar o login mantém o espaço de trabalho em que você estava.
- **Log out** apaga seu login e volta para a tela de e-mail.

Cada login funciona apenas para o espaço de trabalho em que foi feito. Todos entram uma vez após esta alteração. Quando você está desconectado, **Salvar** diz **Sign in to PlaidCloud to save.** e a recuperação de uma dimensão diz **Sign in to PlaidCloud to retrieve a dimension.**

Seu login é compartilhado por todas as pastas de trabalho que você tem abertas, mas cada pasta de trabalho mantém o seu próprio projeto. O projeto de uma pasta de trabalho pertence a um espaço de trabalho, então, depois que você troca, uma pasta de trabalho vinculada a um projeto do espaço de trabalho antigo fica sem projeto até que você escolha um. Consulte [O projeto pertence à pasta de trabalho](/pt-br/reference/cli/plaidxl/retrieve/#o-projeto-pertence-à-pasta-de-trabalho).

## Tema claro e escuro

O painel de tarefas acompanha o aplicativo web do PlaidCloud, com azul da marca, guias e listas em estilo de trilho, e tabelas, dimensões, projetos e colunas em cartões de rolagem delimitados. Ele segue o tema do seu Office e muda quando você o altera. Em um painel estreito, as guias ficam três por linha em duas linhas; a partir de 560 pixels de largura, ficam em uma única linha.

## Teclado e leitores de tela

As linhas das listas de projetos, tabelas e dimensões recebem o foco do teclado e respondem a **Enter** e **Espaço**. Uma linha selecionada é anunciada por um leitor de tela, os estados selecionado e de aviso trazem um ícone além de uma cor, e o controle com foco do teclado tem um anel de foco bem visível.

## Números

Todo número que o painel de tarefas mostra, como contagens de linhas e colunas e as mensagens de atualização, recálculo, Explain, Formulas, Report e planejamento, segue o idioma de exibição do Excel. O Excel em alemão mostra 4.812.233, por exemplo. Os valores gravados nas células não mudam.

## Relacionados

- [Instalar o PlaidXL](/pt-br/reference/cli/plaidxl/install/) — adicione o suplemento e abra o painel de tarefas
- [Solução de problemas](/pt-br/reference/cli/plaidxl/troubleshooting/) — quando o pop-up de login não abre ou falta um espaço de trabalho
- [Exibir e gerenciar espaços de trabalho](/pt-br/administration/access/overview/viewing-and-managing-workspaces/) — os espaços de trabalho aos quais você pertence
