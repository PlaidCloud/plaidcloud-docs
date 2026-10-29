---
title: Carregando e descarregando dimensões
description: Carregue e descarregue dados de dimensão no PlaidCloud, incluindo importações em massa, atualização de dados e sincronização com fontes de dados externas.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/loading-unloading.md
---

As dimensões podem ser mantidas por operações de fluxo de trabalho por meio do carregamento de dados. Além disso, os dados dimensionais podem ser achatados em dados tabulares e armazenados em tabelas. Isso costuma ser útil para enriquecer dados de relatórios e análises.


## Carregando dimensões

Como as dimensões representam estruturas de dados hierárquicas, o processo de carga precisa transmitir as relações existentes nos dados. O PlaidCloud oferece suporte a duas estruturas de dados diferentes para carregar dimensões:
 * Pai-filho - Os dados são organizados na vertical, com uma coluna de *pai* e uma coluna de *filho* que definem o pai de cada filho em toda a estrutura
 * Níveis - Os dados são organizados na horizontal, com cada coluna representando um nível da hierarquia, da esquerda para a direita

 Além da estrutura, outras informações da dimensão podem ser incluídas no processo de carga, como valores, aliases e propriedades.

 Uma carga de níveis (plana) usa uma consolidação padrão, que todo nó intermediário criado pela carga recebe, e pode indicar uma coluna de folha: quando indica, essa coluna decide qual nó recebe os aliases, as propriedades e os valores da linha; caso contrário, o último nível preenchido é a folha.

 O tipo de consolidação padrão de uma carga pai-filho se aplica a qualquer linha cuja própria consolidação esteja em branco ou não seja reconhecida; por isso, ele deve ser um dos tipos válidos, mesmo quando a tabela também indica uma coluna de consolidação. A hierarquia de destino de uma carga não pode ter o mesmo nome de uma coluna que a carga mapeia: uma coluna com esse nome é lida como a hierarquia à qual cada linha pertence, então uma carga que indique ambas é recusada, em vez de seguir uma interpretação e ignorar a outra.

 Uma carga de aliases, propriedades ou valores verifica o membro de cada linha antes de gravar qualquer coisa. Se alguma linha indicar um membro que a dimensão não possui, a carga falha e informa esses nomes, e nada dessa carga é armazenado. Carregue primeiro a estrutura, ou inclua nela os membros ausentes, e só depois carregue os atributos.

 Consulte a etapa de fluxo de trabalho [Dimension Load](/pt-br/reference/workflow-steps/dimensions/dimension-load) para obter mais informações.


## Descarregando (exportando) dimensões

A exportação de dimensões para tabelas oferece suporte a duas abordagens estruturais:
 * Pai-filho - Os dados são organizados na vertical, com uma coluna de *pai* e uma coluna de *filho* que definem o pai de cada filho em toda a estrutura
 * Níveis - Os dados são organizados na horizontal, com cada coluna representando um nível da hierarquia, da esquerda para a direita

Propriedades e valores também podem ser incluídos nos dados tabulares achatados.

 Consulte a etapa de fluxo de trabalho [Dimension Export](/pt-br/reference/workflow-steps/dimensions/dimension-export) para obter mais informações.
