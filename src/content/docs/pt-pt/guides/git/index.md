---
title: PlaidCloud Git
description: Aloje, versione e colabore em repositórios Git dentro do PlaidCloud — com issues, pull requests, quadros de projeto, versões e wikis, e início de sessão único integrado.
sidebar:
  label: Visão geral
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

O PlaidCloud Git é um serviço Git privado integrado na área de trabalho. Cada área de trabalho tem o seu próprio servidor Git para armazenar código, configuração, blocos de notas e quaisquer outros ficheiros versionados — juntamente com as issues, os pull requests e os quadros de projeto que a equipa usa para colaborar nesses ficheiros.

A sessão é iniciada com a conta PlaidCloud, pelo que não há nome de utilizador nem palavra-passe separados a configurar. Os novos repositórios são privados por predefinição, visíveis apenas para os membros a quem conceder acesso.

## Abrir o Git

Selecione **Git** na lista de aplicações da área de trabalho. O separador **Git** mostra os repositórios da área de trabalho com o nome, a descrição, o ramo predefinido e a data da última atualização de cada um, e uma linha no topo indica o que pode fazer. Selecione um repositório para o abrir, ou **View all in Git** para aceder à interface web do Git. Use **← Back to** a sua área de trabalho no Git para regressar ao PlaidCloud.

Para clonar um repositório, selecione **Copy clone URL** na respetiva linha. Na primeira vez, uma sugestão mostra o que é necessário:

1. O Git tem de estar instalado no computador.
2. Crie um token de acesso no Git em **Definições → Aplicações**, com a permissão **write:repository**. A sugestão contém uma ligação para essa página.
3. Quando o Git pedir uma palavra-passe, cole o token, não a palavra-passe do PlaidCloud.
4. Execute os dois comandos `git config --global user.name` e `user.email` apresentados, que já contêm o seu nome e e-mail.

Consulte [Repositórios](/pt-pt/guides/git/repositories/) para o guia completo. Se não conseguir copiar um URL de clonagem, tem acesso de Leitura; veja abaixo.

## Níveis de acesso

Todos os que têm acesso ao Git podem ler os repositórios partilhados da área de trabalho. Mais dois níveis permitem enviar alterações.

| Nível | O que pode fazer | Atribuído por |
|---|---|---|
| **Leitura** | Ver e clonar os repositórios partilhados. | Predefinido para todos os membros. |
| **Contributor** | Tudo o que o nível de Leitura permite e enviar alterações para o repositório `apps`, onde reside o código das aplicações [Panel](/pt-pt/guides/panel-apps/deploy-from-git/) e [Dash](/pt-pt/guides/dash-apps/deploy-from-git/). | O grupo de segurança **Git Contributors**. |
| **Administrador** | Tudo o que o nível Contributor permite, enviar alterações para todos os repositórios, incluindo `udfs`, e criar organizações. | O grupo de segurança **Git Administration**. |

O repositório `udfs` está limitado aos Administradores porque as funções definidas pelo utilizador são executadas sob a identidade do fluxo de trabalho que as chama.

Se tem acesso de Leitura, o separador **Git** indica até três administradores da área de trabalho a quem pode pedir que o adicionem a **Git Contributors**.

## Git a partir de aplicações e UDFs

A janela de uma aplicação Panel ou Dash tem uma secção **Repositório** que mostra o respetivo repositório, ramo e estado da criação, com **Edit in browser** e **Copy clone URL** para os membros que podem enviar alterações. A barra de ferramentas de uma UDF suportada por Git tem **Open**, que abre o repositório no respetivo ramo no Git, e, para os Administradores, **Edit in browser**.

## Conceder acesso ao Git

Os administradores da área de trabalho concedem acesso em **Identidade**, adicionando membros a um grupo de segurança ou adicionando a permissão a um grupo próprio.

1. Adicione o membro a **Git Contributors** para lhe permitir enviar código de aplicações, ou a **Git Administration** para o tornar administrador do Git.
2. Para dar a todos os novos membros acesso de envio ao código das aplicações, adicione **Git Contributors** aos grupos predefinidos. **Git Administration** não pode ser um grupo predefinido.
3. Para verificar o que um membro pode fazer, abra o membro e selecione o separador **Git**. Mostra o nome de utilizador Git do membro, o respetivo nível e o grupo que o concede.

Uma alteração aplica-se na próxima vez que o membro iniciar sessão no Git ou abrir o separador **Git**. Os colaboradores do suporte do PlaidCloud têm acesso de Administrador automaticamente.

## O que contém esta secção

- [Repositórios](/pt-pt/guides/git/repositories/) — criar um repositório e, depois, clonar, fazer commit e enviar o trabalho
- [Issues](/pt-pt/guides/git/issues/) — acompanhar tarefas, erros e ideias com etiquetas, marcos e responsáveis
- [Pull requests](/pt-pt/guides/git/pull-requests/) — propor alterações num ramo e revê-las antes de serem integradas
- [Quadros de projeto](/pt-pt/guides/git/projects/) — organizar issues e pull requests num quadro Kanban
- [Versões e etiquetas](/pt-pt/guides/git/releases-and-tags/) — marcar e publicar instantâneos versionados de um repositório
- [Wikis](/pt-pt/guides/git/wikis/) — manter documentação extensa junto ao código
- [Pacotes](/pt-pt/guides/git/packages/) — publicar e instalar artefactos de compilação a partir do registo do repositório
- [Pesquisar código](/pt-pt/guides/git/searching-code/) — encontrar código, issues e pull requests nos repositórios

## Relacionado

- [Implementar uma aplicação Panel a partir do PlaidCloud Git](/pt-pt/guides/panel-apps/deploy-from-git/) — disponibilizar uma aplicação HoloViz Panel diretamente a partir de um repositório, com uma ligação gerida sem credenciais
- [Implementar uma aplicação Dash a partir do PlaidCloud Git](/pt-pt/guides/dash-apps/deploy-from-git/) — disponibilizar uma aplicação Plotly Dash da mesma forma
- [Gestão de acessos](/pt-pt/administration/access/) — como a pertença à área de trabalho e os grupos de segurança determinam quem pode ver e editar repositórios
