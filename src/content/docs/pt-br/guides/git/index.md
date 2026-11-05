---
title: PlaidCloud Git
description: Hospede, versione e colabore em repositórios Git dentro do PlaidCloud — com issues, pull requests, quadros de projeto, releases e wikis, e login único incorporado.
sidebar:
  label: Visão geral
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

O PlaidCloud Git é um serviço Git privado incorporado ao seu espaço de trabalho. Cada espaço de trabalho tem o próprio servidor Git para armazenar código, configuração, notebooks e quaisquer outros arquivos versionados, junto com as issues, os pull requests e os quadros de projeto que sua equipe usa para colaborar neles.

Você entra com sua conta do PlaidCloud, então não é preciso configurar um nome de usuário ou uma senha separados. Os novos repositórios são privados por padrão e ficam visíveis apenas para os membros aos quais você concede acesso.

## Abrir o Git

Selecione **Git** na lista de aplicativos do seu espaço de trabalho. A guia **Git** mostra os repositórios do seu espaço de trabalho com o nome, a descrição, o branch padrão e a data da última atualização de cada um, e uma linha no topo informa o que você pode fazer. Selecione um repositório para abri-lo ou **View all in Git** para ir à interface web do Git. Use **← Back to** seu espaço de trabalho no Git para voltar ao PlaidCloud.

Para clonar um repositório, selecione **Copy clone URL** na linha dele. Na primeira vez, uma dica mostra o que você precisa:

1. O Git deve estar instalado no seu computador.
2. Crie um token de acesso no Git em **Settings → Applications**, com a permissão **write:repository**. A dica tem um link para essa página.
3. Quando o Git pedir uma senha, cole o token, não a sua senha do PlaidCloud.
4. Execute os dois comandos `git config --global user.name` e `user.email` exibidos, que já contêm seu nome e e-mail.

Consulte [Repositórios](/pt-br/guides/git/repositories/) para o passo a passo completo. Se você não consegue copiar uma URL de clone, você tem acesso de Leitura; veja abaixo.

## Níveis de acesso

Todos que têm acesso ao Git podem ler os repositórios compartilhados do espaço de trabalho. Dois outros níveis permitem enviar alterações.

| Nível | O que você pode fazer | Concedido por |
|---|---|---|
| **Leitura** | Ver e clonar os repositórios compartilhados. | Padrão para todos os membros. |
| **Contributor** | Tudo o que o nível Leitura permite e enviar para o repositório `apps`, onde fica o código dos aplicativos [Panel](/pt-br/guides/panel-apps/deploy-from-git/) e [Dash](/pt-br/guides/dash-apps/deploy-from-git/). | O grupo de segurança **Git Contributors**. |
| **Administrador** | Tudo o que o nível Contributor permite, enviar para todos os repositórios, incluindo `udfs`, e criar organizações. | O grupo de segurança **Git Administration**. |

O repositório `udfs` é restrito a Administradores porque as funções definidas pelo usuário são executadas com a identidade do fluxo de trabalho que as chama.

Se você tem acesso de Leitura, a guia **Git** indica até três administradores do espaço de trabalho a quem você pode pedir que o adicionem a **Git Contributors**.

## Git a partir de aplicativos e UDFs

A janela de um aplicativo Panel ou Dash tem uma seção **Repositório** que mostra o repositório, o branch e o status de compilação dele, com **Edit in browser** e **Copy clone URL** para os membros que podem enviar alterações. A barra de ferramentas de uma UDF com suporte do Git tem **Open**, que abre o repositório em seu branch no Git, e, para Administradores, **Edit in browser**.

## Conceder acesso ao Git

Os administradores do espaço de trabalho concedem acesso em **Identidade**, adicionando membros a um grupo de segurança ou adicionando a permissão a um grupo próprio.

1. Adicione o membro a **Git Contributors** para que ele possa enviar código de aplicativos, ou a **Git Administration** para torná-lo administrador do Git.
2. Para dar a todo novo membro acesso de envio ao código de aplicativos, adicione **Git Contributors** aos seus grupos padrão. **Git Administration** não pode ser um grupo padrão.
3. Para verificar o que um membro pode fazer, abra o membro e selecione a guia **Git**. Ela mostra o nome de usuário do membro no Git, o nível dele e qual grupo o concede.

Uma alteração é aplicada na próxima vez que o membro entrar no Git ou abrir a guia **Git**. A equipe de suporte do PlaidCloud tem acesso de Administrador automaticamente.

## O que há nesta seção

- [Repositórios](/pt-br/guides/git/repositories/) — crie um repositório e depois clone, faça commit e envie seu trabalho
- [Issues](/pt-br/guides/git/issues/) — acompanhe tarefas, bugs e ideias com rótulos, marcos e responsáveis
- [Pull requests](/pt-br/guides/git/pull-requests/) — proponha alterações em um branch e revise-as antes de mesclá-las
- [Quadros de projeto](/pt-br/guides/git/projects/) — organize issues e pull requests em um quadro Kanban
- [Releases e tags](/pt-br/guides/git/releases-and-tags/) — marque e publique instantâneos versionados de um repositório
- [Wikis](/pt-br/guides/git/wikis/) — mantenha documentação extensa junto ao seu código
- [Pacotes](/pt-br/guides/git/packages/) — publique e instale artefatos de build a partir do registro do repositório
- [Pesquisa de código](/pt-br/guides/git/searching-code/) — encontre código, issues e pull requests em todos os seus repositórios

## Relacionados

- [Implantar um aplicativo Panel a partir do PlaidCloud Git](/pt-br/guides/panel-apps/deploy-from-git/) — sirva um aplicativo HoloViz Panel diretamente de um repositório, com uma conexão gerenciada sem credenciais
- [Implantar um aplicativo Dash a partir do PlaidCloud Git](/pt-br/guides/dash-apps/deploy-from-git/) — sirva um aplicativo Plotly Dash da mesma forma
- [Gerenciamento de acesso](/pt-br/administration/access/) — como a participação no espaço de trabalho e os grupos de segurança determinam quem pode ver e editar repositórios
