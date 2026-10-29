---
title: Resultados da alocação
description: Analise os resultados de alocação do PlaidCloud, incluindo a revisão dos dados de saída, a verificação das distribuições e a validação da precisão da alocação.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/allocation-results.md
---

Depois de executar uma etapa de alocação, a saída é uma tabela de resultado que você pode inspecionar, verificar e usar em etapas posteriores.

## O que a tabela de resultado contém

Uma linha de resultado de alocação típica inclui:

- **Identificador de origem** — a linha da tabela de origem de onde esta alocação veio
- **Identificador de destino** — a linha da dimensão ou tabela de destino que recebeu a distribuição
- **Valor alocado** — a parcela do valor de origem atribuída a este destino
- **Valor do direcionador** — o número do direcionador que justificou a distribuição (por exemplo, o número de funcionários, a receita, as horas)
- **Taxa de alocação** — a participação do direcionador como proporção do total
- **Valor de origem** — o total original que está sendo distribuído (mantido para fins de auditoria)
- **Referência de conjunto / marcação / regra** — se a marcação baseada em regras foi usada, qual regra produziu esta linha

As colunas exatas dependem do tipo de etapa de alocação e da sua configuração.

## Lista de verificação

Antes de confiar nos resultados:

1. **Reconciliação** — a soma dos valores alocados é igual à soma dos valores de origem (dentro da tolerância de ponto flutuante). Se não for, algo não foi distribuído.
2. **Nenhuma linha de origem órfã** — toda linha de origem gerou pelo menos uma linha de alocação. Linhas órfãs geralmente significam que nenhum dado de direcionador correspondeu à marcação ou ao membro de dimensão da origem.
3. **Nenhum destino órfão** — se você esperava que todo destino recebesse algo, verifique se todos os membros da dimensão de destino aparecem nos resultados.
4. **Taxas razoáveis** — as taxas de alocação devem somar 1,0 (100%) por conjunto de origem. Taxas muito fora do esperado indicam problemas nos dados dos direcionadores.
5. **Conferência por amostragem dos totais** — escolha uma linha de origem de alto valor e verifique se a alocação corresponde ao que você calcularia manualmente.

## Padrões comuns a observar

- **Alocações zeradas** — um destino que não recebeu nada geralmente significa que a linha do direcionador estava ausente ou tinha valor zero
- **Concentração excessiva** — se a maior parte da distribuição vai para um único destino, geralmente a coluna do direcionador tem um valor muito grande (muitas vezes um problema de qualidade de dados a montante)
- **Direcionadores negativos** — dependendo da etapa de alocação, valores negativos de direcionadores podem produzir distribuições invertidas. Confirme se essa é a intenção.

## Próximas etapas

- [Analisar alocações com um agente de IA](/pt-br/guides/allocations/results/analyzing-allocations-with-ai/) — pergunte, via MCP, por que um resultado mudou, o que o determina e o que uma mudança causaria
- [Solução de problemas de alocações](/pt-br/guides/allocations/results/troubleshooting-allocations/) — o que fazer quando a reconciliação falha
- [Publicação de dados](/pt-br/guides/data/publish/) — quando confiar nos resultados, publique-os para painéis e consumidores posteriores
