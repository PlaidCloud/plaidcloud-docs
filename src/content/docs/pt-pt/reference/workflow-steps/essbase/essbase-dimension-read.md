---
title: "Essbase: Ler dimensão"
description: Leia o esboço de uma dimensão Oracle Essbase para a hierarquia principal de uma dimensão PlaidCloud, em ligação direta à nuvem — recusando, pelo nome, qualquer membro partilhado, apenas de etiqueta, Dynamic Calc ou de atributo, e tudo o resto que o esboço não consiga representar.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-dimension-read.md
---

## Descrição

Lê o esboço de uma dimensão de um cubo Oracle **Essbase** através da sua [ligação Oracle Essbase](/pt-pt/guides/connections/essbase/) e carrega-o na **hierarquia principal** de uma dimensão PlaidCloud.

Este passo aparece no menu de passos em **Oracle Essbase**.

O passo acede ao Essbase **diretamente na nuvem** através da respetiva API REST — não existe um caminho por agente local para este passo, nem uma variante remota do mesmo.

## Configuração

### Origem Essbase

| Campo | Obrigatório | Notas |
|---|---|---|
| Ligação | Sim | A [ligação Oracle Essbase](/pt-pt/guides/connections/essbase/) através da qual ler. |
| Aplicação | Sim | A aplicação Essbase de onde ler. O seletor lista as aplicações que a conta de serviço da ligação consegue ver; se a ligação definir uma aplicação predefinida, esta fica pré-selecionada. |
| Cubo (base de dados) | Sim | O cubo, dentro da aplicação escolhida, de onde ler o esboço. |
| Dimensão | Sim | A dimensão Essbase cujo esboço ler. |

### Dimensão PlaidCloud de destino

| Campo | Obrigatório | Notas |
|---|---|---|
| Dimensão de destino | Sim | A dimensão PlaidCloud para onde o esboço é carregado. |

## O que este passo não consegue representar

| Limitação | O que significa |
|---|---|
| Membros partilhados | Um membro partilhado reutiliza os dados de outro membro sob um segundo elemento superior. Um nó de dimensão PlaidCloud tem exatamente um elemento superior, pelo que um membro partilhado é recusado pelo nome, em vez de ser carregado como duplicado ou descartado em silêncio. Leia a consolidação principal como uma dimensão PlaidCloud própria — o segundo elemento superior de um membro partilhado não é representável aqui. |
| Membros apenas de etiqueta | Um membro apenas de etiqueta existe para navegação e nunca contém dados próprios. É recusado pelo nome, em vez de ser carregado como um membro normal que nada a jusante espera que esteja vazio. |
| Membros Dynamic Calc | O valor de um membro Dynamic Calc é calculado pelo Essbase em tempo real e nunca é armazenado. Este passo lê a estrutura do esboço, não dados calculados, pelo que um membro Dynamic Calc é recusado pelo nome, em vez de ser carregado como se fosse um membro armazenado. |
| Dimensões de atributo | Uma dimensão de atributo classifica membros de uma dimensão base — não é uma hierarquia de factos por direito próprio. A sua leitura é recusada de imediato; leia antes a dimensão base. |
| Operadores de consolidação não representáveis | Uma aresta PlaidCloud tem um indicador de consolidação (`+`, `-` ou `~`). Os operadores `+` e `-` do Essbase correspondem diretamente. `*`, `/` e `%` não podem ser representados como um simples sinal de consolidação — um membro que utilize um deles é recusado pelo nome, em vez de ser carregado com o sinal errado. |
| Esboços acima do limite de membros | Um esboço de dimensão com mais de **5000 membros de esboço no total** é recusado em vez de ser carregado parcialmente, com a contagem observada e o limite indicados no erro. Leia um nível menos profundo da hierarquia, ou uma subárvore mais pequena, para ficar abaixo do limite. |

## Relacionado

- [Ligar ao Oracle Essbase (guia)](/pt-pt/guides/connections/essbase/) — crie a ligação.
- [Conector Oracle Essbase](/pt-pt/reference/connectors/erp/oracle-essbase/) — referência dos campos da ligação.
- [Essbase: Consultar cubo](/pt-pt/reference/workflow-steps/essbase/essbase-query/) — executa uma consulta MDX em direto sobre um cubo, diretamente na nuvem.
- [Passos Oracle Essbase](/pt-pt/reference/workflow-steps/essbase/)
