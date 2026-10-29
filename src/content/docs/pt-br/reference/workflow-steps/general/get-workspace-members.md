---
title: Get Workspace Members (etapa)
description: Grave os membros do espaço de trabalho em uma tabela de projeto, escolhendo quais campos de identidade e de atividade incluir.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## Descrição

Grava os membros do espaço de trabalho em uma tabela de projeto. Use-a para gerar relatórios sobre acessos, conciliar uma lista de membros com um feed de RH ou conduzir uma etapa downstream com base em quem tem acesso no momento.

## Configuração

### Informações a incluir

Ativados por padrão: **Sobrenome**, **Nome**, **E-mail**, **Nome de usuário**, **Data de criação do membro** e **Carimbo de data/hora do último login**.

### Configurações adicionais

Desativadas por padrão:

- **Incluir membros desativados** — amplia a saída além dos membros ativos.
- **Modo de histórico de login** — retorna o histórico de logins em vez de apenas o último login.

## Relacionados

- [Etapas gerais](/pt-br/reference/workflow-steps/general/)
- [Deactivate Workspace Members (etapa)](/pt-br/reference/workflow-steps/general/deactivate-workspace-members/)
- [Gerenciamento de membros](/pt-br/administration/access/)
