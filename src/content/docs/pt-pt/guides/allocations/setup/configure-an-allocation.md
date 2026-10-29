---
title: Configurar uma alocação
description: Configure uma alocação do PlaidCloud, incluindo dados de origem, dados de driver, mapeamento de destinos, métodos de alocação e opções de processamento.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/configure-an-allocation.md
---

## Finalidade

As alocações permitem repartir valores (normalmente custos) por um nível mais granular através da aplicação de um driver. As alocações são usadas para uma multiplicidade de fins, incluindo, entre outros, **Activity-Based Costing**, **IT & Shared Service Chargeback**, o cálculo do custo totalmente imputado para produzir e fornecer um bem ou serviço a clientes, etc. São uma ferramenta fundamental da análise financeira e uma pedra angular das operações de relato de gestão, como a **Customer & Product Profitability**. São também uma construção útil para estabelecer e gerir preços de transferência intragrupo globais para bens e serviços.

## Configurar a transformação de alocação

Do ponto de vista prático, as alocações são configuradas no PlaidCloud de forma semelhante a outras transformações de dados, como junções e pesquisas. Têm de ser definidos quatro parâmetros de configuração para que uma transformação de alocação tenha êxito.

1. **Especificar os dados pré-alocados**: especifique a tabela de dados pré-alocados na secção **Tabela de valores a alocar** da transformação de alocação.
2. **Especificar os dados de driver**: os dados de driver servirão de base para os rácios usados na alocação. Escolha a tabela de dados de driver na secção **Tabela de dados de driver** da transformação de alocação.
3. **Especificar a tabela de resultados**: os dados pós-alocação têm de ser armazenados numa tabela. Especifique a tabela na secção **Tabela de resultados da alocação** da secção de resultados da alocação da transformação.
4. **Especificar a dimensão de atribuição**: as alocações exigem uma dimensão de atribuição, cuja finalidade é fornecer a prescrição de como cada registo ou conjunto de registos dos dados pré-alocados será atribuído. Especifique a dimensão de atribuição na secção **Hierarquia da dimensão de atribuição** da transformação de alocação.

Para além destes quatro, os dois separadores de mapeamento precisam que as **Funções** das colunas estejam definidas antes de o passo poder ser guardado: uma coluna **Valor a alocar** no **Mapa de origem da alocação** e colunas **Valor de divisão**, **Relação de origem (denominador)** e **Destino da alocação (numerador)** no **Mapa de dados de driver**. O PlaidCloud verifica-as quando guarda e indica o que está em falta — consulte [Resolução de problemas de alocações](/pt-pt/guides/allocations/results/troubleshooting-allocations/#porque-é-que-um-passo-de-alocação-não-é-guardado).

## Conceitos-chave

A soma dos valores de um conjunto de dados alocado deve coincidir com a dos dados de origem pré-alocados.

As alocações estão acessíveis no PlaidCloud como uma opção de transformação. Para configurar uma alocação, defina primeiro as atribuições e depois configure uma transformação de alocação para usar as atribuições na alocação dos registos de entrada através de uma tabela de drivers especificada.

As atribuições são dimensões especiais. São acedidas na secção Dimensões de um projeto do PlaidCloud.

Para configurar uma dimensão de atribuição, execute os seguintes passos:

1. No ecrã do projeto, navegue até ao separador Dimensões
2. Crie uma nova dimensão
