---
title: PlaidCloud Git
description: Aloje, versione e colabore em repositórios Git dentro do PlaidCloud — com issues, pull requests, quadros de projeto, lançamentos e wikis, e início de sessão único integrado.
sidebar:
  label: Descrição geral
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/git/index.md
---

O PlaidCloud Git é um serviço Git privado integrado na sua área de trabalho. Cada área de trabalho tem o seu próprio servidor Git para armazenar código, configuração, notebooks e quaisquer outros ficheiros versionados — juntamente com as issues, os pull requests e os quadros de projeto que a sua equipa utiliza para colaborar neles.

Inicia sessão com a sua conta PlaidCloud, por isso não há nenhum nome de utilizador ou palavra-passe separado para configurar. Abra o **Git** a partir da sua área de trabalho e a sessão já está iniciada. Os novos repositórios são privados por predefinição e só são visíveis para os membros a quem conceder acesso.

## Administrar o Git

Qualquer membro pode criar repositórios, mas **criar organizações** — espaços partilhados que agrupam repositórios e equipas — exige a permissão **Git Administration**. Conceda-a em **Identidade**, adicionando a permissão a um grupo de segurança ou adicionando membros ao grupo incorporado **Git Administration**. Quem pertencer a um grupo que tenha a permissão passa a ser administrador do Git no próximo início de sessão no Git. O pessoal de suporte do PlaidCloud tem-na automaticamente.

Se um administrador recém-autorizado nunca tiver aberto o Git, pode ter de iniciar sessão no Git **duas vezes** para que o acesso de administrador produza efeito — o primeiro início de sessão cria a sua conta Git e a permissão é aplicada no seguinte.

## O que contém esta secção

- [Repositórios](/pt-pt/guides/git/repositories/) — crie um repositório e depois clone, faça commit e push do seu trabalho
- [Issues](/pt-pt/guides/git/issues/) — acompanhe tarefas, erros e ideias com etiquetas, marcos e responsáveis
- [Pull requests](/pt-pt/guides/git/pull-requests/) — proponha alterações num ramo e reveja-as antes de serem integradas
- [Quadros de projeto](/pt-pt/guides/git/projects/) — organize issues e pull requests num quadro Kanban
- [Lançamentos e etiquetas](/pt-pt/guides/git/releases-and-tags/) — marque e publique instantâneos versionados de um repositório
- [Wikis](/pt-pt/guides/git/wikis/) — mantenha documentação extensa junto ao seu código
- [Pacotes](/pt-pt/guides/git/packages/) — publique e instale artefactos de compilação a partir do registo do repositório
- [Pesquisar código](/pt-pt/guides/git/searching-code/) — encontre código, issues e pull requests nos seus repositórios

## Relacionado

- [Implementar uma aplicação Panel a partir do PlaidCloud Git](/pt-pt/guides/panel-apps/deploy-from-git/) — disponibilize uma aplicação HoloViz Panel diretamente a partir de um repositório, com uma ligação gerida sem credenciais
- [Implementar uma aplicação Dash a partir do PlaidCloud Git](/pt-pt/guides/dash-apps/deploy-from-git/) — disponibilize uma aplicação Plotly Dash da mesma forma
- [Gestão de acessos](/pt-pt/administration/access/) — como a pertença à área de trabalho e os grupos de segurança determinam quem pode ver e editar repositórios
