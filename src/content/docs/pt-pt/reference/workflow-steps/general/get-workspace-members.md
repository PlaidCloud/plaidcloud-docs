---
title: Get Workspace Members
description: Escreva os membros da área de trabalho numa tabela do projeto, escolhendo os campos de identidade e de atividade a incluir.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## Descrição

Escreve os membros da área de trabalho numa tabela do projeto. Utilize-o para elaborar relatórios sobre o acesso, reconciliar uma lista de membros com um ficheiro de recursos humanos ou controlar um passo seguinte consoante quem tem atualmente acesso.

## Configuração

### Informação a incluir

Ativados por predefinição: **Apelido**, **Nome próprio**, **Correio eletrónico**, **Nome de utilizador**, **Data de criação do membro** e **Carimbo de data/hora do último início de sessão**.

### Definições adicionais

Desativadas por predefinição:

- **Incluir membros desativados** — alargar o resultado para além dos membros ativos.
- **Modo de histórico de inícios de sessão** — devolver o histórico de inícios de sessão em vez de apenas o último início de sessão.

## Registo de segurança

Cada execução grava uma entrada no Registo de segurança com as colunas escritas, a tabela de destino, o fluxo de trabalho, o passo e a execução.

## Relacionados

- [Passos gerais](/pt-pt/reference/workflow-steps/general/)
- [Deactivate Workspace Members](/pt-pt/reference/workflow-steps/general/deactivate-workspace-members/)
- [Get Workspace Usage](/pt-pt/reference/workflow-steps/general/get-workspace-usage/)
- [Gestão de membros](/pt-pt/administration/access/)
