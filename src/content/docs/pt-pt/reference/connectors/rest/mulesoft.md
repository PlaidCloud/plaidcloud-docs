---
title: Conector REST MuleSoft
description: Ligue o PlaidCloud a um gateway MuleSoft Anypoint e anexe a definição da API para que os passos do fluxo de trabalho possam listar os respetivos pontos de acesso.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/mulesoft.md
---

O MuleSoft Anypoint é um gateway de API: coloca-se à frente dos serviços que a sua organização publicou atrás dele, num endereço específico da sua implementação. Por isso, ao contrário de um conector criado para um único serviço, uma ligação MuleSoft não conhece os seus próprios pontos de acesso — é você quem indica onde estão a API e a respetiva definição.

## Documentação da API

A documentação da API desta ligação é a que documentar os serviços que o seu gateway disponibiliza.

## Configuração

O MuleSoft utiliza o mesmo formulário que a [ligação REST genérica](/pt-pt/reference/connectors/rest/generic-rest/) — os mesmos quatro separadores, os mesmos campos, o mesmo comportamento em todo o formulário. Dois são especialmente importantes aqui:

- **Anfitrião ou endereço IP** — o endereço do seu gateway Anypoint. Não existe valor predefinido, porque o endereço do MuleSoft é específico da sua implementação.
- **Tipo de autenticação** — qualquer um de `None`, `Basic`, `API Key`, `Bearer Token` ou `OAuth 2.0` que o seu gateway espere. Nada é assumido em seu nome.

## Listar pontos de acesso num fluxo de trabalho

Como o gateway não tem uma lista de pontos de acesso integrada, anexe a definição OpenAPI 3.x ou Swagger 2.0 da sua API à ligação em **Definição da API** — o endereço onde está publicada ou um ficheiro `.json` ou `.yaml` armazenado no Document. Consulte [Definição da API](/pt-pt/reference/connectors/rest/generic-rest/#definição-da-api) para os campos.

Um [passo Pedido REST](/pt-pt/guides/workflows/rest-request-step/) que utilize esta ligação pode então definir **Origem dos pontos finais** como **A partir da definição da API da ligação** e escolher **Carregar catálogo** para selecionar entre os pontos de acesso da API, em vez de escrever cada caminho manualmente.

## Relacionado

- [Ligação REST genérica](/pt-pt/reference/connectors/rest/generic-rest/) — a referência completa dos campos deste formulário.
- [Criar e gerir uma ligação](/pt-pt/guides/connections/create-connection/)
- [Passo de fluxo de trabalho Pedido REST](/pt-pt/guides/workflows/rest-request-step/)
