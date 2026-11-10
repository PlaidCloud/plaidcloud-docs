---
title: PlaidCloud Git
description: Hospede, versione e colabore em repositórios Git dentro do PlaidCloud, com issues, pull requests, quadros de projeto, releases e wikis, e com início de sessão único integrado.
sidebar:
  label: Visão geral
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

O PlaidCloud Git é um serviço Git privado integrado na sua área de trabalho. Cada área de trabalho tem o seu próprio servidor Git para armazenar código, configuração, notebooks e quaisquer outros ficheiros versionados, junto com as issues, os pull requests e os quadros de projeto que a sua equipa usa para colaborar neles.

Inicia sessão com a sua conta do PlaidCloud, pelo que não há nome de utilizador nem palavra-passe separados para configurar. Os novos repositórios são privados por predefinição e visíveis apenas para os membros a quem concede acesso.

## Abrir o Git

Selecione **Git** na lista de aplicações da sua área de trabalho. O separador **Git** abre com o host da área de trabalho, a sua função e uma lista de **Repositories**. Use **View all in Git** para ir à interface web do Git, **Manage who can push** (se puder gerir grupos) para abrir a gestão de grupos e o botão de atualizar para recarregar. Use **← Back to** your workspace in Git para voltar ao PlaidCloud.

Um indicador de função mostra o seu nível: **Administrador**, **Colaborador** ou **Leitor**, com uma linha a dizer o que isso permite que faça. Cada linha de repositório mostra o seu nome, a sua descrição (quando houver), **Atualizado** com a data, um campo de clone somente leitura com um botão de copiar e **Abrir**, que abre o repositório no Git. Os repositórios que cria como privados ficam diretamente no Git, não nesta lista.

Se o Git não estiver configurado para a sua área de trabalho, ou não for possível aceder-lhe, o separador **Git** mostra **O Git não está disponível** com o motivo, e **Tentar novamente** volta a verificar.

## Clonar um repositório

Copie o endereço de clone do repositório a partir da linha dele. Na primeira vez que copiar, aparece um cartão **Set up Git on your computer** com os passos abaixo. Selecione **Dispensar** para escondê-lo e **How to clone** no cabeçalho para apresentá-lo novamente.

1. O Git tem de estar instalado no seu computador.
2. Crie um token em **Configurações → Aplicações** com a permissão **write:repository**. O cartão tem um link para essa página.
3. Indique ao Git quem é, usando os dois comandos `git config --global user.name` e `user.email` apresentados, que já contêm o seu nome e o seu e-mail.
4. Clone o repositório com o comando `git clone` apresentado. Quando o Git pedir uma palavra-passe, cole esse token, não a palavra-passe do PlaidCloud.

Cada comando tem o seu próprio botão de copiar. Consulte [Repositórios](/pt-pt/guides/git/repositories/) para o passo a passo completo. Copiar exige acesso de push e uma conta Git ativada: se o botão de copiar estiver desativado, abra qualquer repositório uma vez para ativar a sua conta ou, como **Leitor**, peça acesso de push conforme descrito abaixo.

## Níveis de acesso

Todos os que têm acesso ao Git podem ler os repositórios partilhados da área de trabalho. Dois níveis adicionais permitem fazer push.

| Função | O que pode fazer | Concedido por |
|---|---|---|
| **Leitor** | Ver e clonar os repositórios partilhados. | Predefinido para todos os membros. |
| **Colaborador** | Tudo o que a leitura permite e push para o repositório `apps`, onde fica o código de aplicações [Panel](/pt-pt/guides/panel-apps/deploy-from-git/) e [Dash](/pt-pt/guides/dash-apps/deploy-from-git/). | O grupo de segurança **Git Contributors**. |
| **Administrador** | Tudo o que o Colaborador pode e push para todos os repositórios, incluindo `udfs`, além de criar organizações. | O grupo de segurança **Git Administration**. |

O repositório `udfs` é limitado aos administradores porque as funções definidas pelo utilizador são executadas com a identidade do fluxo de trabalho que as chama.

Se for **Leitor**, o separador **Git** indica até três administradores da área de trabalho a quem pode pedir para adicioná-lo a **Git Contributors**.

## Git a partir de aplicações e UDFs

A janela de uma aplicação Panel ou Dash tem uma secção **Repositório** que mostra o seu repositório, ramo e estado de build, com **Edit in browser** e **Copy clone URL** para os membros que podem fazer push. A barra de ferramentas de uma UDF baseada em Git tem **Abrir**, que abre o repositório no ramo dela no Git, e **Edit in browser** para administradores.

## Conceder acesso ao Git

Os administradores da área de trabalho concedem acesso em **Identidade**, adicionando membros a um grupo de segurança ou adicionando a permissão a um grupo próprio.

1. Adicione o membro a **Git Contributors** para que ele possa fazer push de código de aplicações, ou a **Git Administration** para torná-lo administrador do Git.
2. Para dar a todo novo membro acesso de push ao código de aplicações, adicione **Git Contributors** aos seus grupos predefinidos. **Git Administration** não pode ser um grupo predefinido.
3. Para verificar o que um membro pode fazer, abra o membro e selecione o separador **Git**. Mostra o nome de utilizador do Git do membro, o nível dele e o grupo que o concede.

Uma alteração aplica-se na próxima vez que o membro iniciar sessão no Git ou abrir o separador **Git**. A conta Git de um membro acompanha a participação dele no PlaidCloud. Desativar ou remover um membro bloqueia a conta Git dele, incluindo os seus tokens e chaves SSH, em cerca de uma hora, e reativá-lo a desbloqueia. Nada é eliminado: os repositórios e o histórico dele permanecem. Iniciar sessão no Git com início de sessão único abre a conta do próprio membro. A equipa de suporte do PlaidCloud tem acesso de administrador automaticamente.

## O que há nesta secção

- [Repositórios](/pt-pt/guides/git/repositories/) – crie um repositório e depois clone, faça commit e push do seu trabalho
- [Issues](/pt-pt/guides/git/issues/) – acompanhe tarefas, bugs e ideias com etiquetas, marcos e responsáveis
- [Pull requests](/pt-pt/guides/git/pull-requests/) – proponha alterações em um ramo e revise-as antes do merge
- [Quadros de projeto](/pt-pt/guides/git/projects/) – organize issues e pull requests em um quadro Kanban
- [Releases e tags](/pt-pt/guides/git/releases-and-tags/) – marque e publique instantâneos versionados de um repositório
- [Wikis](/pt-pt/guides/git/wikis/) – mantenha documentação extensa ao lado do seu código
- [Pacotes](/pt-pt/guides/git/packages/) – publique e instale artefatos de build a partir do registo do repositório
- [Pesquisa de código](/pt-pt/guides/git/searching-code/) – encontre código, issues e pull requests em todos os seus repositórios

## Relacionados

- [Implementar uma aplicação Panel a partir do PlaidCloud Git](/pt-pt/guides/panel-apps/deploy-from-git/) – sirva uma aplicação HoloViz Panel diretamente de um repositório, com uma ligação gerida sem credenciais
- [Implementar uma aplicação Dash a partir do PlaidCloud Git](/pt-pt/guides/dash-apps/deploy-from-git/) – sirva uma aplicação Plotly Dash da mesma forma
- [Gestão de acesso](/pt-pt/administration/access/) – como a participação na área de trabalho e os grupos de segurança determinam quem pode ver e editar repositórios
