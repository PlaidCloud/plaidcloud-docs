---
title: "TM1: Ler dimensão"
description: Leia uma hierarquia do IBM TM1 / Planning Analytics — elementos, relações pai/filho e atributos dos elementos — para uma dimensão do PlaidCloud, diretamente na nuvem através de REST.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read.md
---

## Descrição

Lê uma hierarquia de uma dimensão do IBM **TM1 / Planning Analytics** através da sua [ligação TM1](/pt-pt/guides/connections/tm1/) e carrega-a numa dimensão do PlaidCloud. Os elementos, as relações pai/filho e os atributos dos elementos da hierarquia do TM1 são primeiro preparados como linhas pai/filho numa tabela, e a dimensão do PlaidCloud é construída a partir dessa tabela de preparação — o mesmo carregamento que o próprio passo Dimension Load do PlaidCloud executa, pelo que uma hierarquia do TM1 chega exatamente como uma construída manualmente ou originária de qualquer outra fonte externa.

Este passo aparece no menu de passos em **IBM TM1 / Planning Analytics**.

O passo acede ao TM1 **diretamente na nuvem** através da sua API REST — sem intervenção de qualquer agente local. Consulte [TM1: Consultar cubo (agente)](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) para o caminho local.

## Configuração

### Origem TM1

| Campo | Obrigatório | Notas |
|---|---|---|
| Ligação TM1 | Sim | A [ligação TM1](/pt-pt/guides/connections/tm1/) através da qual ler. |
| Ambiente | Sim | O ambiente da ligação. |
| Base de dados | Sim | A base de dados (instância) do TM1 de onde ler. Assume por predefinição a Base de dados predefinida da ligação, se estiver definida. |
| Dimensão TM1 | Sim | A dimensão do TM1 a ler. Descoberta em direto a partir da base de dados ligada, ou escrita manualmente. |
| Hierarquia TM1 | Não | A hierarquia dentro da dimensão. Descoberta em direto depois de escolhida uma dimensão, ou escrita manualmente. Deixe em branco para ler a hierarquia própria (implícita) da dimensão, que o TM1 designa com o nome da dimensão. |
| Tabela de preparação | Sim | A tabela onde as linhas brutas de pai/filho/atributo são colocadas antes de a dimensão do PlaidCloud ser construída a partir dela. |

Depois de escolhidas uma dimensão e uma hierarquia, o formulário mostra quais atributos de elementos do TM1 passarão a **Aliases** do PlaidCloud e quais a **Propriedades** — conforme o tipo de atributo do próprio TM1 (`Alias` vs. `Numeric`/`String`). O tipo TM1 de cada elemento (Numeric, String ou Consolidated) também passa a propriedade, com o nome `tm1_element_type`.

### Dimensão PlaidCloud de destino

| Campo | Obrigatório | Notas |
|---|---|---|
| Especificar dimensão dinamicamente | Um dos dois | Nome da dimensão de destino, que pode conter tokens `{variable}` resolvidos no momento da execução. Selecionado por predefinição. |
| Utilizar dimensão específica | Um dos dois | Escolha antes, na árvore, uma dimensão do PlaidCloud já existente. |
| Hierarquia alternativa | Não | Uma chave de hierarquia alternativa do PlaidCloud para onde carregar. Deixe em branco para carregar a hierarquia principal. |

O carregamento numa hierarquia alternativa é validado antes de qualquer coisa ser escrita: uma hierarquia alternativa do PlaidCloud não pode alterar o pai de um nó que já existe na hierarquia principal da dimensão, e uma hierarquia alternativa do TM1 partilha por definição os seus elementos com a hierarquia principal do próprio TM1, pelo que esta é a forma normal dessa opção, não um caso extremo. Se o pai de alguma linha analisada já existir na hierarquia principal da dimensão de destino, o passo falha logo de início, antes de a tabela de preparação ser tocada, nomeando os pais em conflito.

## O que este passo não consegue representar

| Limitação | O que significa |
|---|---|
| Os elementos com vários pais são recusados | Um nó de dimensão do PlaidCloud tem exatamente um pai por hierarquia. Um elemento do TM1 que se encontre sob duas consolidações na mesma hierarquia não pode ser carregado — o passo falha com um erro nomeado que lista todos os elementos em causa e os seus pais, em vez de descartar silenciosamente o elemento da primeira consolidação. Leia a agregação alternativa como uma dimensão própria do PlaidCloud, ou resolva primeiro a duplicação de paternidade no TM1. |
| As ponderações de consolidação transportam apenas um sinal | Uma relação do PlaidCloud tem um indicador de consolidação (`+`, `-` ou `~`), não um coeficiente. A ponderação `0` do TM1 passa a `~` (o membro não se agrega no seu pai); uma ponderação negativa passa a `-`; uma ponderação positiva passa a `+`; uma ponderação ausente (a predefinição do próprio TM1) é tratada como `+`. Uma **ponderação fracionária ou multiplicadora — 0.5, 2.0 — não pode ser representada**: passa a um simples `+` e o multiplicador perde-se. Isto é contabilizado e nomeado, não engolido — o aviso do passo na execução indica quantas relações foram afetadas e lista-as como `parent -> child (weight)`, por exemplo `Total Revenue -> Product A (0.5)`, limitado a 10 com "(and N more)" para além disso. Uma relação de raiz (sem pai) é designada `(root)` em vez de ficar em branco. Uma ponderação presente mas não numérica é recusada de imediato em vez de adivinhada. |
| Sem descoberta intermediada por agente | Este passo funciona apenas diretamente na nuvem — consulte [TM1: Consultar cubo (agente)](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) para ler um servidor TM1 que a nuvem não consegue alcançar. |

## Relacionados

- [Ligar ao TM1 (guia)](/pt-pt/guides/connections/tm1/) — criar a ligação.
- [Conector TM1](/pt-pt/reference/connectors/rest/tm1/) — referência dos campos da ligação, incluindo o caminho do agente local.
- [TM1: Consultar cubo](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — ler dados de cubos, diretamente na nuvem.
- [TM1: Consultar cubo (agente)](/pt-pt/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — ler dados de cubos através de um agente PlaidLink local.
- [Dimension Load](/pt-pt/reference/workflow-steps/dimensions/dimension-load/) — o mesmo mecanismo de carregamento de dimensões em que este passo se baseia.
- [Passos do IBM TM1 / Planning Analytics](/pt-pt/reference/workflow-steps/ibm-planning-analytics/)
