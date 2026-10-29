---
title: "Essbase: Ler dimensão"
description: Leia o esboço de uma dimensão do Oracle Essbase para a hierarquia principal de uma dimensão do PlaidCloud, diretamente na nuvem, recusando pelo nome qualquer membro compartilhado, somente rótulo, Dynamic Calc ou de atributo, e tudo o mais que o esboço não consiga representar.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-dimension-read.md
---

## Descrição

Lê o esboço de uma dimensão de um cubo do Oracle **Essbase** por meio da sua [conexão do Oracle Essbase](/pt-br/guides/connections/essbase/) e o carrega na **hierarquia principal** de uma dimensão do PlaidCloud.

Esta etapa aparece no menu de etapas em **Oracle Essbase**.

A etapa acessa o Essbase **diretamente na nuvem**, por sua API REST: não há caminho por agente local para esta etapa, nem uma variante remota dela.

## Configuração

### Origem Essbase

| Campo | Obrigatório | Observações |
|---|---|---|
| Conexão | Sim | A [conexão do Oracle Essbase](/pt-br/guides/connections/essbase/) por meio da qual ler. |
| Aplicativo | Sim | O aplicativo Essbase de onde ler. O seletor lista os aplicativos que a conta de serviço da conexão consegue ver; se a conexão define um aplicativo padrão, ele já vem selecionado. |
| Cubo (banco de dados) | Sim | O cubo, dentro do aplicativo escolhido, de onde ler o esboço. |
| Dimensão | Sim | A dimensão do Essbase cujo esboço será lido. |

### Dimensão de destino do PlaidCloud

| Campo | Obrigatório | Observações |
|---|---|---|
| Dimensão de destino | Sim | A dimensão do PlaidCloud em que o esboço é carregado. |

## O que esta etapa não consegue representar

| Limitação | O que significa |
|---|---|
| Membros compartilhados | Um membro compartilhado reutiliza os dados de outro membro sob um segundo pai. Um nó de dimensão do PlaidCloud tem exatamente um pai, então um membro compartilhado é recusado pelo nome, em vez de ser carregado como duplicata ou descartado silenciosamente. Leia a consolidação principal como uma dimensão própria do PlaidCloud: o segundo pai de um membro compartilhado não pode ser representado aqui. |
| Membros somente rótulo | Um membro somente rótulo existe para navegação e nunca guarda dados próprios. Ele é recusado pelo nome, em vez de ser carregado como um membro comum que nada adiante espera que esteja vazio. |
| Membros Dynamic Calc | O valor de um membro Dynamic Calc é calculado pelo Essbase na hora e nunca é armazenado. Esta etapa lê a estrutura do esboço, não dados calculados, então um membro Dynamic Calc é recusado pelo nome, em vez de ser carregado como se fosse um membro armazenado. |
| Dimensões de atributo | Uma dimensão de atributo classifica os membros de uma dimensão base; não é uma hierarquia de fatos por si só. Lê-la é recusado de imediato; leia a dimensão base. |
| Operadores de consolidação não representáveis | Uma aresta do PlaidCloud carrega um indicador de consolidação (`+`, `-` ou `~`). Os operadores `+` e `-` do Essbase têm correspondência direta. `*`, `/` e `%` não podem ser representados como um sinal simples de consolidação: um membro que usa um deles é recusado pelo nome, em vez de ser carregado com o sinal errado. |
| Esboços acima do limite de membros | Um esboço de dimensão com mais de **5.000 membros no total** é recusado em vez de carregado parcialmente, e o erro informa a contagem observada e o limite. Leia um nível menos profundo da hierarquia, ou uma subárvore menor, para ficar abaixo do limite. |

## Relacionados

- [Conectar-se ao Oracle Essbase (guia)](/pt-br/guides/connections/essbase/) — crie a conexão.
- [Conector do Oracle Essbase](/pt-br/reference/connectors/erp/oracle-essbase/) — referência dos campos da conexão.
- [Essbase: Consultar cubo](/pt-br/reference/workflow-steps/essbase/essbase-query/) — executa uma consulta MDX ao vivo em um cubo, diretamente na nuvem.
- [Etapas do Oracle Essbase](/pt-br/reference/workflow-steps/essbase/)
