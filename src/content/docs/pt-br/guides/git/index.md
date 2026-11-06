---
title: PlaidCloud Git
description: Hospede, versione e colabore em repositórios Git dentro do PlaidCloud — com issues, pull requests, quadros de projeto, releases e wikis, e login único incorporado.
sidebar:
  label: Visão geral
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

O PlaidCloud Git é um serviço Git privado incorporado ao seu espaço de trabalho. Cada espaço de trabalho tem seu próprio servidor Git para armazenar código, configuração, notebooks e quaisquer outros arquivos versionados — junto com as issues, os pull requests e os quadros de projeto que sua equipe usa para colaborar neles.

Você entra com sua conta do PlaidCloud, então não há nome de usuário nem senha separados para configurar. Os novos repositórios são privados por padrão, visíveis apenas para os membros a quem você conceder acesso.

## Abrir o Git

Selecione **Git** na lista de aplicativos do seu espaço de trabalho. A guia **Git** abre com o host do espaço de trabalho, sua função e uma lista de **Repositories**. Use **View all in Git** para ir à interface web do Git, **Manage who can push** (se você puder gerenciar grupos) para abrir o gerenciamento de grupos e o botão de atualizar para recarregar. Use **← Back to** seu espaço de trabalho no Git para voltar ao PlaidCloud.

Um indicador de função mostra o seu nível: **Administrator**, **Contributor** ou **Visualizador**, com uma linha explicando o que isso permite. Cada linha de repositório mostra o nome, a descrição (quando houver), **Atualizado** com a data, um campo de clonagem somente leitura com um botão de cópia e **Abrir**, que abre o repositório no Git. Os repositórios que você cria como privados ficam diretamente no Git, não nesta lista.

## Clonar um repositório

Copie o endereço de clonagem do repositório a partir da linha dele. Na primeira vez que você copiar, aparece um cartão **Set up Git on your computer** com as etapas abaixo. Selecione **Dispensar** para ocultá-lo e **How to clone** no cabeçalho para exibi-lo novamente.

1. O Git precisa estar instalado no seu computador.
2. Crie um token em **Configurações → Applications** com a permissão **write:repository**. O cartão tem um link para essa página.
3. Informe ao Git quem você é, usando os dois comandos `git config --global user.name` e `user.email` exibidos, que já contêm seu nome e e-mail.
4. Clone o repositório com o comando `git clone` exibido. Quando o Git pedir uma senha, cole esse token, não a sua senha do PlaidCloud.

Cada comando tem seu próprio botão de cópia. Consulte [Repositórios](/pt-br/guides/git/repositories/) para o passo a passo completo. Copiar exige acesso de envio e uma conta Git ativada: se o botão de cópia estiver desabilitado, abra qualquer repositório uma vez para ativar sua conta ou, como **Visualizador**, peça acesso de envio conforme descrito abaixo.

## Níveis de acesso

Todos os que têm acesso ao Git podem ler os repositórios compartilhados do espaço de trabalho. Dois níveis adicionais permitem enviar código.

| Função | O que você pode fazer | Concedido por |
|---|---|---|
| **Visualizador** | Ver e clonar os repositórios compartilhados. | Padrão para todos os membros. |
| **Contributor** | Tudo o que a leitura permite e enviar para o repositório `apps`, onde fica o código dos aplicativos [Panel](/pt-br/guides/panel-apps/deploy-from-git/) e [Dash](/pt-br/guides/dash-apps/deploy-from-git/). | O grupo de segurança **Git Contributors**. |
| **Administrator** | Tudo o que Contributor permite, mais enviar para todos os repositórios, incluindo `udfs`, e criar organizações. | O grupo de segurança **Git Administration**. |

O repositório `udfs` é limitado aos administradores porque as funções definidas pelo usuário são executadas com a identidade do fluxo de trabalho que as chama.

Se você for **Visualizador**, a guia **Git** indica até três administradores do espaço de trabalho a quem você pode pedir que adicionem você a **Git Contributors**.

## Git a partir de aplicativos e UDFs

A janela de um aplicativo Panel ou Dash tem uma seção **Repository** que mostra o repositório, a branch e o status da criação, com **Edit in browser** e **Copy clone URL** para os membros que podem enviar código. A barra de ferramentas de uma UDF baseada em Git tem **Abrir**, que abre o repositório na branch dela no Git, e **Edit in browser** para administradores.

## Concessão de acesso ao Git

Os administradores do espaço de trabalho concedem acesso em **Identidade**, adicionando membros a um grupo de segurança ou adicionando a permissão a um grupo próprio.

1. Adicione o membro a **Git Contributors** para que ele possa enviar código de aplicativos, ou a **Git Administration** para torná-lo administrador do Git.
2. Para dar a todo novo membro acesso de envio ao código de aplicativos, adicione **Git Contributors** aos seus grupos padrão. **Git Administration** não pode ser um grupo padrão.
3. Para verificar o que um membro pode fazer, abra o membro e selecione a guia **Git**. Ela mostra o nome de usuário Git do membro, o nível dele e qual grupo o concede.

Uma alteração é aplicada na próxima vez que o membro entrar no Git ou abrir a guia **Git**. A equipe de suporte do PlaidCloud tem acesso de administrador automaticamente.

## O que há nesta seção

- [Repositórios](/pt-br/guides/git/repositories/) — crie um repositório e depois clone, faça commit e envie seu trabalho
- [Issues](/pt-br/guides/git/issues/) — acompanhe tarefas, bugs e ideias com rótulos, marcos e responsáveis
- [Pull requests](/pt-br/guides/git/pull-requests/) — proponha alterações em uma branch e revise-as antes de mesclar
- [Quadros de projeto](/pt-br/guides/git/projects/) — organize issues e pull requests em um quadro Kanban
- [Releases e tags](/pt-br/guides/git/releases-and-tags/) — marque e publique instantâneos versionados de um repositório
- [Wikis](/pt-br/guides/git/wikis/) — mantenha documentação extensa junto ao seu código
- [Pacotes](/pt-br/guides/git/packages/) — publique e instale artefatos de build a partir do registro do repositório
- [Pesquisa de código](/pt-br/guides/git/searching-code/) — encontre código, issues e pull requests em todos os seus repositórios

## Relacionados

- [Implantar um aplicativo Panel a partir do PlaidCloud Git](/pt-br/guides/panel-apps/deploy-from-git/) — sirva um aplicativo HoloViz Panel diretamente de um repositório, com uma conexão gerenciada sem credenciais
- [Implantar um aplicativo Dash a partir do PlaidCloud Git](/pt-br/guides/dash-apps/deploy-from-git/) — sirva um aplicativo Plotly Dash da mesma forma
- [Gerenciamento de acesso](/pt-br/administration/access/) — como a participação no espaço de trabalho e os grupos de segurança determinam quem pode ver e editar repositórios
