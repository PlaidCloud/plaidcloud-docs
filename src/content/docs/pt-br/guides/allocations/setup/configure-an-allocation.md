---
title: Configurar uma alocação
description: Configure uma alocação do PlaidCloud, incluindo dados de origem, dados do direcionador, mapeamento de destino, métodos de alocação e opções de processamento.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/configure-an-allocation.md
---

## Finalidade

As alocações permitem que valores (normalmente custos) sejam desmembrados em um nível mais granular pela aplicação de um direcionador. As alocações são usadas para uma infinidade de finalidades, incluindo, entre outras, **Custeio baseado em atividades**, **Rateio de TI e serviços compartilhados**, cálculo do custo totalmente carregado para produzir e fornecer um bem ou serviço aos clientes, etc. Elas são uma ferramenta fundamental para a análise financeira e uma pedra angular das operações de relatórios gerenciais, como **Rentabilidade de clientes e produtos**. Também são uma construção útil para estabelecer e gerenciar preços de transferência globais entre empresas do mesmo grupo para bens e serviços.

## Configurando a transformação de alocação

Do ponto de vista prático, as alocações são configuradas no PlaidCloud de maneira semelhante a outras transformações de dados, como junções e consultas. Quatro parâmetros de configuração precisam ser definidos para que uma transformação de alocação tenha sucesso.

1. **Especifique os dados pré-alocados**: especifique a tabela de dados pré-alocados na seção **Tabela de valores a alocar** da transformação de alocação.
2. **Especifique os dados do direcionador**: os dados do direcionador servirão de base para as proporções usadas na alocação. Escolha a tabela de dados do direcionador na seção **Tabela de dados do direcionador** da transformação de alocação.
3. **Especifique a tabela de resultados**: os dados pós-alocação precisam ser armazenados em uma tabela. Especifique a tabela na seção **Tabela de resultado da alocação** da seção de resultado da alocação da transformação.
4. **Especifique a dimensão de atribuição**: as alocações exigem uma dimensão de atribuição, cuja finalidade é fornecer a prescrição de como cada registro ou conjunto de registros pré-alocados será atribuído. Especifique a dimensão de atribuição na seção **Hierarquia da dimensão de atribuição** da transformação de alocação.

Além dessas quatro, as duas guias de mapeamento precisam ter as **Funções** das colunas definidas antes que a etapa seja salva: uma coluna **Valor a alocar** no **Mapa de origem da alocação** e colunas **Dividir valor**, **Relação de origem (denominador)** e **Destino da alocação (numerador)** no **Mapa de dados do direcionador**. O PlaidCloud verifica isso quando você salva e informa o que está faltando — consulte [Solução de problemas de alocações](/pt-br/guides/allocations/results/troubleshooting-allocations/#por-que-uma-etapa-de-alocação-não-é-salva).

## Conceitos-chave

A soma dos valores em um conjunto de dados alocado deve fechar com a dos dados de origem pré-alocados

As alocações são acessíveis no PlaidCloud como uma opção de transformação. Para configurar uma alocação, primeiro configure as atribuições e, em seguida, configure uma transformação de alocação para usar as atribuições na alocação dos registros de entrada usando uma tabela de direcionadores especificada.

As atribuições são dimensões especiais. Elas são acessadas na seção Dimensões de um projeto do PlaidCloud.

Para configurar uma dimensão de atribuição, execute as etapas a seguir:

1. Na tela do projeto, navegue até a guia Dimensões
2. Crie uma nova dimensão
