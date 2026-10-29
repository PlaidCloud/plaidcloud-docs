---
title: Conector REST do MuleSoft
description: Conecte o PlaidCloud a um gateway MuleSoft Anypoint e anexe a definição da API para que as etapas de fluxo de trabalho possam listar seus endpoints.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/mulesoft.md
---

O MuleSoft Anypoint é um gateway de API: ele fica na frente dos serviços que a sua organização publicou atrás dele, em um endereço específico da sua implantação. Por isso, ao contrário de um conector criado para um único serviço, uma conexão MuleSoft não conhece os próprios endpoints: você informa onde ficam a API e a sua definição.

## Documentação da API

A documentação da API desta conexão é a que documenta os serviços que o seu gateway expõe.

## Configuração

O MuleSoft usa o mesmo formulário da [conexão REST genérica](/pt-br/reference/connectors/rest/generic-rest/): as mesmas quatro guias, os mesmos campos e o mesmo comportamento em tudo. Dois deles são os mais importantes aqui:

- **Host ou endereço IP** — o endereço do seu gateway Anypoint. Não há valor padrão, porque um endereço MuleSoft é específico da sua implantação.
- **Tipo de autenticação** — qualquer um entre `None`, `Basic`, `API Key`, `Bearer Token` ou `OAuth 2.0` que o seu gateway espera. Nada é presumido em seu nome.

## Listar endpoints em um fluxo de trabalho

Como o gateway não tem uma lista de endpoints integrada, anexe à conexão a definição OpenAPI 3.x ou Swagger 2.0 da sua API em **Definição da API**, seja o endereço em que ela está publicada ou um arquivo `.json` ou `.yaml` armazenado em Documentos. Consulte [Definição da API](/pt-br/reference/connectors/rest/generic-rest/#definição-da-api) para ver os campos.

Uma [etapa Solicitação REST](/pt-br/guides/workflows/rest-request-step/) que use esta conexão pode então definir **Origem do endpoint** como **Da definição de API da conexão** e escolher **Carregar catálogo** para selecionar entre os endpoints da API, em vez de digitar cada caminho à mão.

## Relacionados

- [Conexão REST genérica](/pt-br/reference/connectors/rest/generic-rest/) — a referência completa de campos deste formulário.
- [Criar e gerenciar uma conexão](/pt-br/guides/connections/create-connection/)
- [Etapa de fluxo de trabalho Solicitação REST](/pt-br/guides/workflows/rest-request-step/)
