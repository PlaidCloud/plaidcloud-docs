---
title: Get Workspace Members
description: Escreva os membros da área de trabalho numa tabela de projeto, escolhendo os campos de identidade e de atividade a incluir.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## Descrição

Escreve os membros da área de trabalho numa tabela de projeto. Utilize-o para elaborar relatórios sobre acessos, reconciliar uma lista de membros com um ficheiro de RH ou acionar um passo a jusante com base em quem tem acesso atualmente.

## Configuração

### Informação a incluir

Ativados por predefinição: **Apelido**, **Nome próprio**, **Correio eletrónico**, **Nome de utilizador**, **Data de criação do membro** e **Carimbo de data/hora do último início de sessão**.

### Definições adicionais

Desativadas por predefinição:

- **Incluir membros desativados** — alarga a saída para além dos membros ativos.
- **Modo de histórico de inícios de sessão** — devolve o histórico de inícios de sessão em vez de apenas o último início de sessão.

## Relacionados

- [Passos gerais](/pt-pt/reference/workflow-steps/general/)
- [Deactivate Workspace Members](/pt-pt/reference/workflow-steps/general/deactivate-workspace-members/)
- [Gestão de membros](/pt-pt/administration/access/)
