---
title: "TM1: Ler dimensão"
description: Leia uma hierarquia do IBM TM1 / Planning Analytics — elementos, relações pai/filho e atributos de elementos — para uma dimensão do PlaidCloud, diretamente da nuvem via REST.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read.md
---

## Descrição

Lê uma hierarquia de uma dimensão do IBM **TM1 / Planning Analytics** por meio da sua [conexão TM1](/pt-br/guides/connections/tm1/) e a carrega em uma dimensão do PlaidCloud. Os elementos, as relações pai/filho e os atributos de elementos da hierarquia do TM1 são primeiro preparados como linhas pai/filho em uma tabela, e a dimensão do PlaidCloud é construída a partir dessa tabela de preparação — a mesma carga que a etapa Dimension Load do próprio PlaidCloud executa, de modo que uma hierarquia do TM1 chega exatamente como uma criada manualmente ou obtida de qualquer outra origem externa.

Esta etapa aparece no menu de etapas em **IBM TM1 / Planning Analytics**.

A etapa acessa o TM1 **diretamente da nuvem** por meio da API REST — nenhum agente local é envolvido. Consulte [TM1: Consultar cubo (agente)](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) para o caminho local.

## Configuração

### Origem TM1

| Campo | Obrigatório | Observações |
|---|---|---|
| Conexão TM1 | Sim | A [conexão TM1](/pt-br/guides/connections/tm1/) pela qual ler. |
| Ambiente | Sim | O ambiente da conexão. |
| Banco de dados | Sim | O banco de dados (instância) do TM1 do qual ler. Usa por padrão o Banco de dados padrão da conexão, se houver um definido. |
| Dimensão TM1 | Sim | A dimensão do TM1 a ser lida. Descoberta ao vivo a partir do banco de dados conectado, ou digitada manualmente. |
| Hierarquia TM1 | Não | A hierarquia dentro da dimensão. Descoberta ao vivo depois que uma dimensão é escolhida, ou digitada manualmente. Deixe em branco para ler a hierarquia própria (implícita) da dimensão, que o TM1 nomeia com o nome da dimensão. |
| Tabela de preparação | Sim | A tabela em que as linhas brutas de pai/filho/atributo são gravadas antes de a dimensão do PlaidCloud ser construída a partir dela. |

Depois que uma dimensão e uma hierarquia são escolhidas, o formulário mostra quais atributos de elementos do TM1 serão gravados como **aliases** do PlaidCloud e quais como **propriedades** — de acordo com o próprio tipo de atributo do TM1 (`Alias` vs. `Numeric`/`String`). O tipo TM1 de cada elemento (Numeric, String ou Consolidated) também é gravado como propriedade, com o nome `tm1_element_type`.

### Dimensão de destino do PlaidCloud

| Campo | Obrigatório | Observações |
|---|---|---|
| Especificar dimensão dinamicamente | Um dos dois | Nome da dimensão de destino, que pode conter tokens `{variable}` resolvidos em tempo de execução. Selecionado por padrão. |
| Usar dimensão específica | Um dos dois | Em vez disso, escolha na árvore uma dimensão já existente do PlaidCloud. |
| Hierarquia alternativa | Não | Uma chave de hierarquia alternativa do PlaidCloud na qual carregar. Deixe em branco para carregar a hierarquia principal. |

O carregamento em uma hierarquia alternativa é validado antes de qualquer gravação: uma hierarquia alternativa do PlaidCloud não pode alterar o pai de um nó que já existe na hierarquia principal da dimensão, e uma hierarquia alternativa do TM1 compartilha seus elementos com a hierarquia principal do próprio TM1 por definição, portanto esse é o formato normal para essa opção, não um caso extremo. Se o pai de qualquer linha analisada já existir na hierarquia principal da dimensão de destino, a etapa falha logo no início, antes de a tabela de preparação ser tocada, indicando os pais em conflito.

## O que esta etapa não consegue representar

| Limitação | O que significa |
|---|---|
| Elementos com vários pais são recusados | Um nó de dimensão do PlaidCloud tem exatamente um pai por hierarquia. Um elemento do TM1 que está sob duas consolidações na mesma hierarquia não pode ser carregado — a etapa falha com um erro nomeado que lista cada elemento problemático e seus pais, em vez de descartar silenciosamente o elemento da primeira consolidação. Leia a consolidação alternativa como uma dimensão própria do PlaidCloud, ou resolva antes no TM1 a duplicidade de parentesco. |
| Os pesos de consolidação carregam apenas um sinal | Uma aresta do PlaidCloud carrega um indicador de consolidação (`+`, `-` ou `~`), não um coeficiente. O peso `0` do TM1 vira `~` (o membro não é consolidado no pai); um peso negativo vira `-`; um peso positivo vira `+`; um peso ausente (o padrão do próprio TM1) é tratado como `+`. Um **peso fracionário ou multiplicador — 0,5, 2,0 — não pode ser representado**: ele é gravado como um simples `+` e o multiplicador se perde. Isso é contabilizado e informado, não ignorado — o aviso da etapa na execução informa quantas arestas foram afetadas e as lista como `parent -> child (weight)`, por exemplo `Total Revenue -> Product A (0.5)`, limitado a 10, com "(and N more)" além disso. Uma aresta raiz (sem pai) é nomeada `(root)` em vez de ficar em branco. Um peso presente porém não numérico é recusado de imediato, em vez de ser adivinhado. |
| Sem descoberta mediada por agente | Esta etapa funciona somente diretamente da nuvem — consulte [TM1: Consultar cubo (agente)](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) para ler um servidor TM1 que a nuvem não consegue alcançar. |

## Relacionados

- [Conectar ao TM1 (guia)](/pt-br/guides/connections/tm1/) — crie a conexão.
- [Conector TM1](/pt-br/reference/connectors/rest/tm1/) — referência dos campos de conexão, incluindo o caminho do agente local.
- [TM1: Consultar cubo](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — leia dados de cubo, diretamente da nuvem.
- [TM1: Consultar cubo (agente)](/pt-br/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — leia dados de cubo por meio de um agente PlaidLink local.
- [Dimension Load](/pt-br/reference/workflow-steps/dimensions/dimension-load/) — o mesmo mecanismo de carga de dimensão em que esta etapa se baseia.
- [Etapas do IBM TM1 / Planning Analytics](/pt-br/reference/workflow-steps/ibm-planning-analytics/)
