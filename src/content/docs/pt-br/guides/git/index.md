---
title: PlaidCloud Git
description: Hospede, versione e colabore em repositórios Git dentro do PlaidCloud, com issues, pull requests, quadros de projeto, releases e wikis, e com login único integrado.
sidebar:
  label: Visão geral
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

O PlaidCloud Git é um serviço Git privado integrado ao seu espaço de trabalho. Cada espaço de trabalho tem seu próprio servidor Git para armazenar código, configuração, notebooks e quaisquer outros arquivos versionados, junto com as issues, os pull requests e os quadros de projeto que sua equipe usa para colaborar neles.

Você entra com sua conta do PlaidCloud, portanto não há nome de usuário nem senha separados para configurar. Os novos repositórios são privados por padrão e visíveis apenas para os membros aos quais você conceder acesso.

## Abrir o Git

Selecione **Git** na lista de aplicativos do seu espaço de trabalho. A guia **Git** abre com o host do espaço de trabalho, sua função e uma lista de **Repositórios**. Use **View all in Git** para ir à interface web do Git, **Manage who can push** (se você puder gerenciar grupos) para abrir o gerenciamento de grupos e o botão de atualizar para recarregar. Use **← Back to** your workspace in Git para voltar ao PlaidCloud.

Um indicador de função mostra seu nível: **Administrador**, **Colaborador** ou **Visualizador**, com uma linha dizendo o que isso permite fazer. Cada linha de repositório mostra seu nome, a descrição (quando houver), **Atualizado** com a data, um campo de clone somente leitura com um botão de copiar e **Abrir**, que abre o repositório no Git. Os repositórios que você cria como privados ficam diretamente no Git, não nesta lista.

Se o Git não estiver configurado para seu espaço de trabalho ou não puder ser acessado, a guia **Git** mostra **Git is not available** com o motivo, e **Tentar novamente** verifica de novo.

## Clonar um Repositório

Copie o endereço de clone do repositório na linha dele. Na primeira vez que você copiar, aparece um cartão **Set up Git on your computer** com as etapas abaixo. Selecione **Dispensar** para ocultá-lo e **How to clone** no cabeçalho para exibi-lo novamente.

1. O Git precisa estar instalado no seu computador.
2. Crie um token em **Settings → Applications** com a permissão **write:repository**. O cartão tem um link para essa página.
3. Informe ao Git quem você é, usando os dois comandos `git config --global user.name` e `user.email` exibidos, que já contêm seu nome e seu e-mail.
4. Clone o repositório com o comando `git clone` exibido. Quando o Git pedir uma senha, cole esse token, não a senha do seu PlaidCloud.

Cada comando tem seu próprio botão de copiar. Consulte [Repositories](/pt-br/guides/git/repositories/) para ver o passo a passo completo. Copiar exige acesso de push e uma conta do Git ativada: se o botão de copiar estiver desabilitado, abra qualquer repositório uma vez para ativar sua conta ou, como **Visualizador**, peça acesso de push conforme descrito abaixo.

## Níveis de Acesso

Todos que têm acesso ao Git podem ler os repositórios compartilhados do espaço de trabalho. Mais dois níveis permitem fazer push.

| Função | O que você pode fazer | Concedido por |
|---|---|---|
| **Visualizador** | Ver e clonar os repositórios compartilhados. | Padrão para todos os membros. |
| **Colaborador** | Tudo o que o nível de leitura permite, e fazer push no repositório `apps`, onde fica o código dos aplicativos [Panel](/pt-br/guides/panel-apps/deploy-from-git/) e [Dash](/pt-br/guides/dash-apps/deploy-from-git/). | O grupo de segurança **Git Contributors**. |
| **Administrador** | Tudo o que o Colaborador pode fazer, e fazer push em todos os repositórios, incluindo `udfs`, e criar organizações. | O grupo de segurança **Git Administration**. |

O repositório `udfs` é limitado aos administradores porque as funções definidas pelo usuário são executadas sob a identidade do fluxo de trabalho que as chama.

Se você for um **Visualizador**, a guia **Git** indica até três administradores do espaço de trabalho a quem você pode pedir para adicioná-lo a **Git Contributors**.

## Git em Aplicativos e UDFs

A janela de um aplicativo Panel ou Dash tem uma seção **Repositório** que mostra seu repositório, o branch e o status da compilação, com **Edit in browser** e **Copy clone URL** para os membros que podem fazer push. Os aplicativos do Panel Studio e os aplicativos do App Runner na conexão gerenciada do PlaidCloud Git são pastas no repositório `apps`, portanto esse é o repositório que a janela deles mostra. Consulte [Onde Seu Aplicativo Fica](/pt-br/guides/panel-apps/studio/#onde-o-aplicativo-fica). A barra de ferramentas de uma UDF baseada em Git tem **Abrir**, que abre o repositório no respectivo branch no Git, e **Edit in browser** para administradores.

## Conceder Acesso ao Git

Os administradores do espaço de trabalho concedem acesso em **Identidade**, adicionando membros a um grupo de segurança ou adicionando a permissão a um grupo próprio.

1. Adicione o membro a **Git Contributors** para que ele possa fazer push do código de aplicativos, ou a **Git Administration** para torná-lo administrador do Git.
2. Para dar a todo novo membro acesso de push ao código de aplicativos, adicione **Git Contributors** aos seus grupos padrão. **Git Administration** não pode ser um grupo padrão.
3. Para verificar o que um membro pode fazer, abra o membro e selecione a guia **Git**. Ela mostra o nome de usuário do membro no Git, o nível dele e qual grupo o concede.

Uma alteração se aplica na próxima vez que o membro entrar no Git ou abrir a guia **Git**. A conta de um membro no Git acompanha a associação dele ao PlaidCloud. Desativar ou remover um membro bloqueia a conta dele no Git, incluindo seus tokens e chaves SSH, em cerca de uma hora, e reativá-lo a desbloqueia. Nada é excluído: os repositórios e o histórico dele permanecem. Entrar no Git com login único abre a conta do próprio membro. A equipe de suporte do PlaidCloud tem acesso de administrador automaticamente.

## O Que Há Nesta Seção

- [Repositories](/pt-br/guides/git/repositories/) — crie um repositório e depois clone, faça commit e push do seu trabalho
- [Issues](/pt-br/guides/git/issues/) — acompanhe tarefas, bugs e ideias com rótulos, marcos e responsáveis
- [Pull Requests](/pt-br/guides/git/pull-requests/) — proponha alterações em um branch e revise-as antes de mesclá-las
- [Project Boards](/pt-br/guides/git/projects/) — organize issues e pull requests em um quadro Kanban
- [Releases and Tags](/pt-br/guides/git/releases-and-tags/) — marque e publique instantâneos versionados de um repositório
- [Wikis](/pt-br/guides/git/wikis/) — mantenha a documentação longa junto do seu código
- [Packages](/pt-br/guides/git/packages/) — publique e instale artefatos de compilação a partir do registro do repositório
- [Searching Code](/pt-br/guides/git/searching-code/) — encontre código, issues e pull requests em todos os seus repositórios

## Relacionados

- [Deploy a Panel App From PlaidCloud Git](/pt-br/guides/panel-apps/deploy-from-git/) — sirva um aplicativo HoloViz Panel diretamente de um repositório, com uma conexão gerenciada sem credenciais
- [Deploy a Dash App From PlaidCloud Git](/pt-br/guides/dash-apps/deploy-from-git/) — sirva um aplicativo Plotly Dash da mesma forma
- [Access Management](/pt-br/administration/access/) — como a associação ao espaço de trabalho e os grupos de segurança controlam quem pode ver e editar repositórios
