---
title: Conector Oracle Essbase
description: Conecte o PlaidCloud ao Oracle Essbase 21c ou ao Oracle Analytics Cloud com uma conta de serviço para executar consultas MDX em tempo real em cubos do Essbase a partir de um fluxo de trabalho.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-essbase.md
---

## Documentação da API

Este conector se comunica com a [API REST do Oracle Essbase](https://docs.oracle.com/en/database/other-databases/essbase/) — os mesmos endpoints `grid/mdx`, de aplicativo, de banco de dados e de estrutura que a Oracle documenta para o Essbase 21c e o Oracle Analytics Cloud (OAC).

## A Que Ele Se Conecta

Oracle Essbase **21c ou posterior** e o Essbase do Oracle Analytics Cloud (OAC). Essas versões expõem o Essbase por uma API REST documentada, que é o que o PlaidCloud chama. As versões locais do Essbase anteriores à API REST **não têm suporte** — não existe um caminho por API Java legada nem por cliente de grade.

Depois que a conexão existe, a etapa [Essbase: Consultar cubo](/pt-br/reference/workflow-steps/essbase/essbase-query/) executa MDX em tempo real em um cubo e grava a grade de resultados em uma tabela, e a etapa [Essbase: Ler dimensão](/pt-br/reference/workflow-steps/essbase/essbase-dimension-read/) carrega a estrutura de uma dimensão em uma dimensão do PlaidCloud.

## Como Funciona a Autenticação

A conexão se autentica com o usuário e a senha de uma conta de serviço por HTTP Basic. O provisionamento dessa conta no Essbase controla quais aplicativos e cubos ela pode ver e consultar, portanto conceda a ela acesso de leitura exatamente aos aplicativos que você pretende consultar e a nada além disso.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| URL base | Texto | A origem do servidor Essbase, por exemplo `https://your-host:9001`. Informe somente a origem — sem o caminho `/essbase/...` no final. |
| Aplicativo padrão | Texto *(opcional)* | Pré-seleciona este aplicativo no formulário da etapa Essbase: Consultar cubo. |
| Nome de usuário | Texto | Usuário da conta de serviço para a autenticação HTTP Basic. |
| Senha | Texto | Senha da conta de serviço. Armazenada de forma criptografada. |
| Verificar SSL | Alternância | Ativada por padrão. Desative somente para um host com certificado autoassinado ou que não possa ser verificado de outra forma. |

## Testar a Conexão

Use **Testar conexão** no editor de conexões. Um teste bem-sucedido alcança o servidor Essbase, lista os aplicativos que a conta de serviço pode ver e informa quantos encontrou — confirmando a URL base e as credenciais antes de você criar uma consulta.

## Relacionados

- [Essbase: Consultar cubo](/pt-br/reference/workflow-steps/essbase/essbase-query/) — execute uma consulta MDX em tempo real em um cubo e grave o resultado em uma tabela.
- [Essbase: Ler dimensão](/pt-br/reference/workflow-steps/essbase/essbase-dimension-read/) — carregue a estrutura de uma dimensão em uma dimensão do PlaidCloud.
- [Etapas do Oracle Essbase](/pt-br/reference/workflow-steps/essbase/)
- [Conectar ao Oracle Essbase (guia)](/pt-br/guides/connections/essbase/)
- [Criar e Gerenciar uma Conexão](/pt-br/guides/connections/create-connection/)
