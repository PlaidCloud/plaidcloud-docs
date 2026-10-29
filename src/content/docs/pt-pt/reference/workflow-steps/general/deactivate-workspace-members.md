---
title: Deactivate Workspace Members
description: Desative os membros da área de trabalho listados numa tabela de projeto, identificados por endereço de correio eletrónico ou nome de utilizador.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/deactivate-workspace-members.md
---

import { Aside } from '@astrojs/starlight/components';

## Descrição

Desativa os membros da área de trabalho indicados numa tabela de origem. Utilize-o para automatizar a saída de pessoas a partir de uma lista de referência — uma extração de RH ou uma revisão de acessos — em vez de desativar as pessoas manualmente.

Combine-o com [Get Workspace Members](/pt-pt/reference/workflow-steps/general/get-workspace-members/) para construir a lista de quem deixa de ter acesso.

<Aside type="caution" title="Isto revoga o acesso">
  Todos os membros correspondentes perdem o acesso quando o passo é executado. Verifique se a tabela
  de origem contém apenas quem pretende antes de agendar este passo.
</Aside>

## Administradores da área de trabalho na lista

[Só um administrador da área de trabalho pode desativar um administrador da área de trabalho](/pt-pt/administration/access/member-management/#alterar-um-administrador-da-área-de-trabalho). Quando o passo é executado sem direitos de administrador da área de trabalho e a sua lista inclui administradores, deixa esses administradores ativos, desativa todos os outros e termina depois com um erro, com uma mensagem que indica quantos membros desativou e nomeia cada administrador que deixou ativo. Os membros que desativou permanecem desativados. Para desativar um administrador, peça a um administrador da área de trabalho que o faça no Identity.

## Configuração

### Parâmetro de pesquisa de membros

Como as linhas da tabela de origem são associadas aos membros. Escolha uma opção:

- **Correio eletrónico** (predefinição)
- **Nome de utilizador**

## Relacionados

- [Passos gerais](/pt-pt/reference/workflow-steps/general/)
- [Get Workspace Members](/pt-pt/reference/workflow-steps/general/get-workspace-members/)
- [Gestão de membros](/pt-pt/administration/access/)
