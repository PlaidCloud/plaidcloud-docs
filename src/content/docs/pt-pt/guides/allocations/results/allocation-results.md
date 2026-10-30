---
title: Resultados da alocação
description: Analise os resultados de alocação do PlaidCloud, incluindo a revisão dos dados de saída, a verificação das distribuições e a validação da exatidão da alocação.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/allocation-results.md
---

Depois de executar um passo de alocação, o resultado é uma tabela de resultados que pode inspecionar, verificar e utilizar em passos seguintes.

## O que contém a tabela de resultados

Uma linha de resultado de alocação típica inclui:

- **Identificador de origem** — a linha da tabela de origem de onde provém esta alocação
- **Identificador de destino** — a linha da dimensão ou tabela de destino que recebeu a distribuição
- **Montante alocado** — a parte do montante de origem atribuída a este destino
- **Valor do driver** — o número do indutor que justificou a distribuição (por exemplo, o número de colaboradores, a receita, as horas)
- **Taxa de alocação** — a quota do indutor como proporção do total
- **Montante de origem** — o total original que está a ser distribuído (mantido para fins de auditoria)
- **Referência de conjunto / etiqueta / regra** — se foi utilizada a etiquetagem baseada em regras, a regra que produziu esta linha

As colunas exatas dependem do tipo de passo de alocação e da configuração.

## Lista de verificação

Antes de confiar nos resultados:

1. **Reconciliação** — a soma dos montantes alocados é igual à soma dos montantes de origem (dentro da tolerância de vírgula flutuante). Se não for, alguma parte não foi distribuída.
2. **Sem linhas de origem órfãs** — cada linha de origem produziu pelo menos uma linha de alocação. As linhas órfãs significam, normalmente, que nenhum dado de indutor correspondeu à etiqueta ou ao membro de dimensão da origem.
3. **Sem destinos órfãos** — se esperava que todos os destinos recebessem algum valor, confirme que todos os membros da dimensão de destino aparecem nos resultados.
4. **Taxas razoáveis** — as taxas de alocação devem somar 1,0 (100%) por conjunto de origem. Taxas muito afastadas do esperado indicam problemas nos dados dos indutores.
5. **Verificação por amostragem dos totais** — escolha uma linha de origem de valor elevado e confirme que a respetiva alocação corresponde ao que calcularia manualmente.

## Padrões comuns a procurar

- **Alocações nulas** — um destino que não recebeu nada significa, normalmente, que a linha do indutor não existia ou tinha valor zero
- **Concentração excessiva** — se a maior parte da distribuição recai sobre um único destino, normalmente a coluna do indutor tem um valor muito elevado (muitas vezes um problema de qualidade dos dados a montante)
- **Indutores negativos** — consoante o passo de alocação, os valores negativos dos indutores podem produzir distribuições invertidas. Confirme a intenção.

## Passos seguintes

- [Analisar alocações com um agente de IA](/pt-pt/guides/allocations/results/analyzing-allocations-with-ai/) — pergunte, através de MCP, por que motivo um resultado mudou, o que o determina e o que uma alteração provocaria
- [Resolução de problemas de alocações](/pt-pt/guides/allocations/results/troubleshooting-allocations/) — o que fazer quando a reconciliação falha
- [Publicar dados](/pt-pt/guides/data/publish/) — quando confiar nos resultados, publique-os para painéis de controlo e consumidores a jusante
