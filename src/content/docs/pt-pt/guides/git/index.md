---
title: PlaidCloud Git
description: Aloje, versione e colabore em repositórios Git dentro do PlaidCloud — com issues, pull requests, quadros de projeto, versões e wikis, e início de sessão único incorporado.
sidebar:
  label: Visão geral
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

O PlaidCloud Git é um serviço Git privado incorporado na sua área de trabalho. Cada área de trabalho tem o seu próprio servidor Git para guardar código, configuração, blocos de notas e quaisquer outros ficheiros versionados — juntamente com os issues, os pull requests e os quadros de projeto que a sua equipa utiliza para colaborar neles.

Inicia sessão com a sua conta PlaidCloud, pelo que não há nome de utilizador nem palavra-passe separados a configurar. Os novos repositórios são privados por predefinição e só são visíveis para os membros a quem conceder acesso.

## Abrir o Git

Selecione **Git** na lista de aplicações da sua área de trabalho. O separador **Git** abre com o anfitrião da área de trabalho, a sua função e uma lista de **Repositórios**. Utilize **View all in Git** para aceder à interface web do Git, **Manage who can push** (se puder gerir grupos) para abrir a gestão de grupos e o botão de atualização para recarregar. Utilize **← Back to** a sua área de trabalho no Git para regressar ao PlaidCloud.

Um indicador de função mostra o seu nível: **Administrator**, **Contributor** ou **Leitor**, com uma linha a explicar o que este lhe permite fazer. Cada linha de repositório mostra o respetivo nome, a descrição (quando existe), **Atualizado** com a data, um campo de clonagem só de leitura com um botão de cópia e **Abrir**, que abre o repositório no Git. Os repositórios que criar como privados encontram-se diretamente no Git, não nesta lista.

Se o Git não estiver configurado para a sua área de trabalho, ou não for possível aceder-lhe, o separador **Git** mostra **O Git não está disponível** com o motivo, e **Tentar novamente** volta a verificar.

## Clonar um repositório

Copie o endereço de clonagem do repositório a partir da respetiva linha. Na primeira vez que copiar, aparece um cartão **Set up Git on your computer** com os passos abaixo. Selecione **Dispensar** para o ocultar e **How to clone** no cabeçalho para o voltar a apresentar.

1. O Git tem de estar instalado no seu computador.
2. Crie um token em **Definições → Aplicações** com a permissão **write:repository**. O cartão tem uma ligação para essa página.
3. Indique ao Git quem é, com os dois comandos `git config --global user.name` e `user.email` apresentados, que já contêm o seu nome e o seu e-mail.
4. Clone o repositório com o comando `git clone` apresentado. Quando o Git pedir uma palavra-passe, cole esse token, não a sua palavra-passe do PlaidCloud.

Cada comando tem o seu próprio botão de cópia. Consulte [Repositórios](/pt-pt/guides/git/repositories/) para o guia completo. Copiar exige acesso de envio e uma conta Git ativada: se o botão de cópia estiver desativado, abra qualquer repositório uma vez para ativar a sua conta ou, como **Leitor**, peça acesso de envio conforme descrito abaixo.

## Níveis de acesso

Todos os que têm acesso ao Git podem ler os repositórios partilhados da área de trabalho. Mais dois níveis permitem enviar alterações.

| Função | O que pode fazer | Concedido por |
|---|---|---|
| **Leitor** | Ver e clonar os repositórios partilhados. | Predefinição para todos os membros. |
| **Contributor** | Tudo o que o nível de leitura permite, e enviar para o repositório `apps`, onde reside o código das aplicações [Panel](/pt-pt/guides/panel-apps/deploy-from-git/) e [Dash](/pt-pt/guides/dash-apps/deploy-from-git/). | O grupo de segurança **Git Contributors**. |
| **Administrator** | Tudo o que um Contributor pode fazer, e enviar para todos os repositórios, incluindo `udfs`, e criar organizações. | O grupo de segurança **Git Administration**. |

O repositório `udfs` está limitado aos administradores porque as funções definidas pelo utilizador são executadas com a identidade do fluxo de trabalho que as chama.

Se for **Leitor**, o separador **Git** indica até três administradores da área de trabalho a quem pode pedir que o adicionem a **Git Contributors**.

## Git a partir de aplicações e UDFs

A janela de uma aplicação Panel ou Dash tem uma secção **Repository** que mostra o respetivo repositório, ramo e estado de compilação, com **Edit in browser** e **Copy clone URL** para os membros que podem enviar. A barra de ferramentas de uma UDF baseada em Git tem **Abrir**, que abre o repositório no respetivo ramo no Git, e **Edit in browser** para os administradores.

## Conceder acesso ao Git

Os administradores da área de trabalho concedem acesso em **Identidade**, adicionando membros a um grupo de segurança ou adicionando a permissão a um grupo próprio.

1. Adicione o membro a **Git Contributors** para lhe permitir enviar código de aplicações, ou a **Git Administration** para o tornar administrador do Git.
2. Para dar a todos os novos membros acesso de envio ao código das aplicações, adicione **Git Contributors** aos seus grupos predefinidos. **Git Administration** não pode ser um grupo predefinido.
3. Para verificar o que um membro pode fazer, abra o membro e selecione o separador **Git**. Este mostra o nome de utilizador Git do membro, o respetivo nível e o grupo que o concede.

Uma alteração aplica-se da próxima vez que o membro iniciar sessão no Git ou abrir o separador **Git**. O pessoal de suporte do PlaidCloud tem acesso de administrador automaticamente.

## O que contém esta secção

- [Repositórios](/pt-pt/guides/git/repositories/) — criar um repositório e, depois, clonar, fazer commit e enviar o seu trabalho
- [Issues](/pt-pt/guides/git/issues/) — acompanhar tarefas, erros e ideias com etiquetas, marcos e responsáveis
- [Pull requests](/pt-pt/guides/git/pull-requests/) — propor alterações num ramo e revê-las antes de serem integradas
- [Quadros de projeto](/pt-pt/guides/git/projects/) — organizar issues e pull requests num quadro Kanban
- [Versões e etiquetas](/pt-pt/guides/git/releases-and-tags/) — marcar e publicar instantâneos versionados de um repositório
- [Wikis](/pt-pt/guides/git/wikis/) — manter documentação extensa junto do seu código
- [Pacotes](/pt-pt/guides/git/packages/) — publicar e instalar artefactos de compilação a partir do registo do repositório
- [Pesquisar código](/pt-pt/guides/git/searching-code/) — encontrar código, issues e pull requests nos seus repositórios

## Relacionado

- [Implementar uma aplicação Panel a partir do PlaidCloud Git](/pt-pt/guides/panel-apps/deploy-from-git/) — disponibilizar uma aplicação HoloViz Panel diretamente a partir de um repositório, com uma ligação gerida sem credenciais
- [Implementar uma aplicação Dash a partir do PlaidCloud Git](/pt-pt/guides/dash-apps/deploy-from-git/) — disponibilizar uma aplicação Plotly Dash da mesma forma
- [Gestão de acessos](/pt-pt/administration/access/) — como a participação na área de trabalho e os grupos de segurança determinam quem pode ver e editar repositórios
