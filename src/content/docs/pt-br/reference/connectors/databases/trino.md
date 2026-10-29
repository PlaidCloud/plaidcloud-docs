---
title: Trino
description: Configure uma conexão com o mecanismo de consulta distribuído Trino no PlaidCloud para executar consultas federadas em várias fontes de dados.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/trino.md
---

**Trino** (anteriormente PrestoSQL) é o mecanismo de consulta SQL distribuído comumente usado em data lakes. Use este conector para consultar implantações do Trino a partir de fluxos de trabalho do PlaidCloud. A autenticação usa HTTP Basic Auth ou JWT; o catálogo e o esquema de destino determinam qual fonte de dados subjacente a consulta acessa.

## Documentação do Fornecedor
[A documentação do Trino](https://trino.io/docs/current/index.html).

## Configuração Inicial

Este conector usa um fluxo de autenticação específico do fornecedor e é configurado diretamente na tela **Conexões** do seu espaço de trabalho. Os campos de configuração exibidos dependem das credenciais que o administrador do seu tenant provisionou para a integração.

Consulte a [documentação do trino](https://trino.io/docs/current/) do fornecedor para ver os detalhes mais recentes da configuração.

Se precisar de ajuda para configurar este conector no seu tenant, entre em contato com a sua equipe de conta — as credenciais específicas do conector, as URLs de ambiente e qualquer provisionamento prévio necessário normalmente precisam ser coordenados com o suporte do PlaidCloud.
