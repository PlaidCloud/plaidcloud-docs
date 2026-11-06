---
title: Get Workspace Members
description: Grava os membros do espaço de trabalho em uma tabela de projeto, com a escolha dos campos de identidade e de atividade a incluir.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-members.md
---

## Descrição

Grava os membros do espaço de trabalho em uma tabela de projeto. Use-a para gerar relatórios de acesso, conciliar uma lista de membros com um feed de RH ou acionar uma etapa seguinte com base em quem tem acesso no momento.

## Configuração

### Informações a incluir

Ativados por padrão: **Sobrenome**, **Nome**, **E-mail**, **Nome de usuário**, **Data de criação do membro** e **Carimbo de data/hora do último login**.

### Configurações adicionais

Desativadas por padrão:

- **Incluir membros desativados** — amplia a saída para além dos membros ativos.
- **Modo de histórico de login** — retorna o histórico de logins em vez de apenas o último login.

## Log de segurança

Cada execução grava uma entrada no Log de segurança registrando as colunas gravadas, a tabela de destino, o fluxo de trabalho, a etapa e a execução.

## Relacionados

- [Etapas gerais](/pt-br/reference/workflow-steps/general/)
- [Deactivate Workspace Members](/pt-br/reference/workflow-steps/general/deactivate-workspace-members/)
- [Get Workspace Usage](/pt-br/reference/workflow-steps/general/get-workspace-usage/)
- [Gerenciamento de membros](/pt-br/administration/access/)
