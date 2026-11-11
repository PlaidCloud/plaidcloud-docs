---
title: Deactivate Workspace Members (etapa)
description: Desative membros do espaço de trabalho listados em uma tabela de projeto, identificados pelo endereço de e-mail ou pelo nome de usuário.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/deactivate-workspace-members.md
---

import { Aside } from '@astrojs/starlight/components';

## Descrição

Desativa os membros do espaço de trabalho indicados em uma tabela de origem. Use-a para automatizar o desligamento a partir de uma lista oficial — uma extração de RH ou uma revisão de acessos — em vez de desativar pessoas manualmente.

Use-a em conjunto com [Get Workspace Members (etapa)](/pt-br/reference/workflow-steps/general/get-workspace-members/) para montar a lista de quem não deve mais ter acesso.

<Aside type="caution" title="Isto revoga o acesso">
  Todo membro correspondente perde o acesso quando a etapa é executada. Verifique se a tabela
  de origem contém apenas quem você pretende desativar antes de agendar esta etapa.
</Aside>

## Administradores do espaço de trabalho na lista

[Somente um administrador do espaço de trabalho pode desativar um administrador do espaço de trabalho](/pt-br/administration/access/member-management/#alteração-de-um-administrador-do-espaço-de-trabalho). Quando a etapa é executada sem direitos de administrador do espaço de trabalho e a lista inclui administradores, ela mantém esses administradores ativos, desativa todos os demais e termina com erro, com uma mensagem que informa quantos membros ela desativou e nomeia cada administrador que manteve ativo. Os membros que ela desativou continuam desativados. Para desativar um administrador, peça a um administrador do espaço de trabalho que faça isso no Identity.

## Configuração

### Parâmetro de pesquisa de membros

Como as linhas da tabela de origem são associadas aos membros. Escolha uma:

- **E-mail** (padrão)
- **Nome de usuário**

## Relacionados

- [Etapas gerais](/pt-br/reference/workflow-steps/general/)
- [Get Workspace Members (etapa)](/pt-br/reference/workflow-steps/general/get-workspace-members/)
- [Gerenciamento de membros](/pt-br/administration/access/)
