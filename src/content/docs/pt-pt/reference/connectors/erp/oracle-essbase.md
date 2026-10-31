---
title: Conector Oracle Essbase
description: Ligue o PlaidCloud ao Oracle Essbase 21c ou ao Oracle Analytics Cloud com uma conta de serviço para executar consultas MDX em direto a cubos Essbase a partir de um fluxo de trabalho.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-essbase.md
---

## Documentação da API

Este conector comunica com a [API REST do Oracle Essbase](https://docs.oracle.com/en/database/other-databases/essbase/), ou seja, os mesmos pontos finais `grid/mdx`, de aplicação, de base de dados e de estrutura que a Oracle documenta para o Essbase 21c e o Oracle Analytics Cloud (OAC).

## A que se liga

Oracle Essbase **21c ou posterior** e Essbase do Oracle Analytics Cloud (OAC). Estas versões expõem o Essbase através de uma API REST documentada, que é a que o PlaidCloud invoca. As versões locais do Essbase anteriores à API REST **não são suportadas**: não existe um caminho através da API Java legada nem de cliente de grelha.

Depois de a ligação existir, o passo [Essbase: Consultar cubo](/pt-pt/reference/workflow-steps/essbase/essbase-query/) executa MDX em direto num cubo e coloca a grelha de resultados numa tabela, e o passo [Essbase: Ler dimensão](/pt-pt/reference/workflow-steps/essbase/essbase-dimension-read/) carrega a estrutura de uma dimensão para uma dimensão do PlaidCloud.

## Como funciona a autenticação

A ligação autentica-se com o nome de utilizador e a palavra-passe de uma conta de serviço, através de HTTP Basic. O aprovisionamento dessa conta no Essbase controla as aplicações e os cubos que pode ver e consultar, pelo que deve conceder-lhe acesso de leitura apenas às aplicações que pretende consultar e a nada mais.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| URL base | Texto | A origem do servidor Essbase, por exemplo `https://your-host:9001`. Introduza apenas a origem, sem o caminho final `/essbase/...`. |
| Aplicação predefinida | Texto *(opcional)* | Pré-seleciona esta aplicação no formulário do passo Essbase: Consultar cubo. |
| Nome de utilizador | Texto | Utilizador da conta de serviço para a autenticação HTTP Basic. |
| Palavra-passe | Texto | Palavra-passe da conta de serviço. Guardada de forma encriptada. |
| Verificar SSL | Interruptor | Ativado por predefinição. Desative apenas para um anfitrião com um certificado autoassinado ou, de outra forma, não verificável. |

## Testar a ligação

Utilize **Testar ligação** no editor de ligações. Um teste bem-sucedido chega ao servidor Essbase, lista as aplicações que a conta de serviço consegue ver e indica quantas encontrou, confirmando o URL base e as credenciais antes de criar uma consulta.

## Relacionado

- [Essbase: Consultar cubo](/pt-pt/reference/workflow-steps/essbase/essbase-query/): execute uma consulta MDX em direto num cubo e coloque o resultado numa tabela.
- [Essbase: Ler dimensão](/pt-pt/reference/workflow-steps/essbase/essbase-dimension-read/): carregue a estrutura de uma dimensão para uma dimensão do PlaidCloud.
- [Passos Oracle Essbase](/pt-pt/reference/workflow-steps/essbase/)
- [Ligar ao Oracle Essbase (guia)](/pt-pt/guides/connections/essbase/)
- [Criar e gerir uma ligação](/pt-pt/guides/connections/create-connection/)
