---
title: Trino
description: Configure uma ligação ao motor de consultas distribuído Trino no PlaidCloud para executar consultas federadas em várias origens de dados.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/trino.md
---

O **Trino** (anteriormente PrestoSQL) é o motor de consultas SQL distribuído habitualmente utilizado sobre data lakes. Utilize este conector para consultar implementações Trino a partir de fluxos de trabalho do PlaidCloud. A autenticação utiliza HTTP Basic Auth ou JWT; o catálogo e o esquema que indicar determinam a origem de dados subjacente consultada.

## Documentação do fabricante
[A documentação do Trino](https://trino.io/docs/current/index.html).

## Configuração

Este conector utiliza um fluxo de autenticação específico do fornecedor e é configurado diretamente a partir do ecrã **Ligações** da sua área de trabalho. Os campos de configuração apresentados dependem das credenciais que o administrador do seu inquilino aprovisionou para a integração.

Consulte a [documentação do trino](https://trino.io/docs/current/) do fabricante para obter os detalhes de configuração mais recentes.

Se precisar de ajuda para configurar este conector para o seu inquilino, contacte a sua equipa de conta: as credenciais específicas do conector, os URL de ambiente e qualquer pré-aprovisionamento necessário têm normalmente de ser coordenados com o suporte do PlaidCloud.
