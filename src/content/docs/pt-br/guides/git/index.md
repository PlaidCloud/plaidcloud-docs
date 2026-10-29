---
title: PlaidCloud Git
description: Hospede, versione e colabore em repositórios Git dentro do PlaidCloud, com issues, pull requests, quadros de projeto, releases e wikis, além de logon único integrado.
sidebar:
  label: Visão geral
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

O PlaidCloud Git é um serviço Git privado integrado ao seu espaço de trabalho. Cada espaço de trabalho tem seu próprio servidor Git para armazenar código, configurações, notebooks e quaisquer outros arquivos versionados, junto com as issues, os pull requests e os quadros de projeto que sua equipe usa para colaborar neles.

Você entra com a sua conta do PlaidCloud, portanto não há nome de usuário nem senha separados para configurar. Abra o **Git** no seu espaço de trabalho e você já está conectado. Os novos repositórios são privados por padrão e ficam visíveis apenas para os membros aos quais você concede acesso.

## Administrar o Git

Qualquer membro pode criar repositórios, mas **criar organizações** (espaços compartilhados que agrupam repositórios e equipes) exige a permissão **Git Administration**. Conceda-a em **Identidade** adicionando a permissão a um grupo de segurança ou adicionando membros ao grupo integrado **Git Administration**. Qualquer pessoa em um grupo que tenha a permissão se torna administradora do Git na próxima vez que entrar no Git. A equipe de suporte do PlaidCloud a tem automaticamente.

Se um administrador recém-autorizado nunca abriu o Git antes, talvez ele precise entrar no Git **duas vezes** para que o acesso de administrador entre em vigor: o primeiro login cria a conta dele no Git, e a permissão é aplicada no seguinte.

## O que há nesta seção

- [Repositórios](/pt-br/guides/git/repositories/): crie um repositório e depois clone, faça commit e envie seu trabalho com push
- [Issues](/pt-br/guides/git/issues/): acompanhe tarefas, bugs e ideias com rótulos, marcos e responsáveis
- [Pull requests](/pt-br/guides/git/pull-requests/): proponha alterações em um branch e revise-as antes de mesclá-las
- [Quadros de projeto](/pt-br/guides/git/projects/): organize issues e pull requests em um quadro Kanban
- [Releases e tags](/pt-br/guides/git/releases-and-tags/): marque e publique instantâneos versionados de um repositório
- [Wikis](/pt-br/guides/git/wikis/): mantenha documentação longa ao lado do seu código
- [Pacotes](/pt-br/guides/git/packages/): publique e instale artefatos de build a partir do registro do repositório
- [Pesquisar código](/pt-br/guides/git/searching-code/): encontre código, issues e pull requests em todos os seus repositórios

## Relacionado

- [Implantar um aplicativo Panel a partir do PlaidCloud Git](/pt-br/guides/panel-apps/deploy-from-git/): sirva um aplicativo HoloViz Panel diretamente de um repositório, com uma conexão gerenciada sem credenciais
- [Implantar um aplicativo Dash a partir do PlaidCloud Git](/pt-br/guides/dash-apps/deploy-from-git/): sirva um aplicativo Plotly Dash da mesma forma
- [Gerenciamento de acesso](/pt-br/administration/access/): como a participação no espaço de trabalho e os grupos de segurança determinam quem pode ver e editar repositórios
