---
title: Carregar e descarregar dimensões
description: Carregue e descarregue dados de dimensões no PlaidCloud, incluindo importações em massa, atualização de dados e sincronização com origens de dados externas.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/loading-unloading.md
---

As dimensões podem ser mantidas a partir de operações de fluxo de trabalho através do carregamento de dados. Além disso, os dados dimensionais podem ser aplanados em dados tabulares e armazenados em tabelas. Isto é frequentemente útil para enriquecer dados de relatórios e de análise.


## Carregar dimensões

Como as dimensões representam estruturas de dados hierárquicas, o processo de carregamento tem de transmitir as relações existentes nos dados. O PlaidCloud suporta duas estruturas de dados diferentes para carregar dimensões:
 * Nó superior-nó inferior - Os dados estão organizados na vertical, com uma coluna *Nó superior* e uma coluna *Nó inferior* que definem o nó superior de cada nó inferior em toda a estrutura
 * Níveis - Os dados estão organizados na horizontal, com cada coluna a representar um nível da hierarquia, da esquerda para a direita

 Além da estrutura, é possível incluir no processo de carregamento outras informações da dimensão, como valores, aliases e propriedades.

 Um carregamento por níveis (plano) aceita uma consolidação predefinida, que é atribuída a todos os nós intermédios que o carregamento cria, e pode indicar uma coluna de folha: quando o faz, essa coluna decide qual o nó que fica com os aliases, as propriedades e os valores da linha; caso contrário, a folha é o último nível preenchido.

 O tipo de consolidação predefinido de um carregamento nó superior-nó inferior aplica-se a qualquer linha cuja consolidação própria esteja em branco ou não seja reconhecida, pelo que tem de ser um dos tipos válidos, mesmo quando a tabela também indica uma coluna de consolidação. A hierarquia visada por um carregamento não pode ter o mesmo nome que uma coluna mapeada pelo carregamento: uma coluna com esse nome é lida como a hierarquia a que cada linha pertence, pelo que um carregamento que indique ambas é recusado, em vez de seguir uma leitura e ignorar a outra.

 Um carregamento de aliases, propriedades ou valores verifica o membro de todas as linhas antes de escrever seja o que for. Se alguma linha indicar um membro que a dimensão não contém, o carregamento falha e comunica esses nomes, e nada desse carregamento é guardado. Carregue primeiro a estrutura, ou inclua nela os membros em falta, e só depois carregue os atributos.

 Consulte o passo de fluxo de trabalho [Dimension Load](/pt-pt/reference/workflow-steps/dimensions/dimension-load) para mais informações.


## Descarregar (exportar) dimensões

A exportação de dimensões para tabelas suporta duas abordagens estruturais:
 * Nó superior-nó inferior - Os dados estão organizados na vertical, com uma coluna *Nó superior* e uma coluna *Nó inferior* que definem o nó superior de cada nó inferior em toda a estrutura
 * Níveis - Os dados estão organizados na horizontal, com cada coluna a representar um nível da hierarquia, da esquerda para a direita

As propriedades e os valores também podem ser incluídos nos dados tabulares aplanados.

 Consulte o passo de fluxo de trabalho [Dimension Export](/pt-pt/reference/workflow-steps/dimensions/dimension-export) para mais informações.
