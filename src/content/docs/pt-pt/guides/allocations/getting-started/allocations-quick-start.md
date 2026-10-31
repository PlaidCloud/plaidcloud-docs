---
title: Início rápido das alocações
description: Configure rapidamente uma alocação de custos básica no PlaidCloud com este guia passo a passo, que abrange origens, indutores e mapeamento de destino.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/allocations-quick-start.md
---

Este guia leva-o dos dados de custos em bruto a um modelo de alocação funcional em cerca de 30 minutos.

## O que vai precisar

- Um projeto com pelo menos duas tabelas:
  - **Valores a alocar** — os custos (ou receitas, ou volumes) que pretende repartir. Uma linha por unidade de origem, uma coluna com o montante.
  - **Dados de indutores** — a base da repartição. Número de colaboradores, área em metros quadrados, número de transações, receitas — aquilo *por* que pretende alocar.
- Uma dimensão que una a origem e o destino (centros de custo, departamentos, produtos — a taxonomia que se adequar ao seu modelo).

Se ainda não tiver tudo isto, os guias [Tabelas e vistas](/pt-pt/guides/data/) e [Dimensões](/pt-pt/guides/dimensions/) explicam como carregar os dados de entrada.

## Passos

1. **Abra o projeto** que contém as tabelas de valores e de indutores.
2. **Crie um novo fluxo de trabalho.** As alocações são sempre executadas dentro de um fluxo de trabalho — não operam diretamente sobre tabelas fora de um.
3. **Adicione um passo de alocação.** Dentro do fluxo de trabalho, adicione um passo da categoria **Alocação**. O ponto de partida mais comum é **Allocation Rules**, para uma repartição simples baseada em indutores.
4. **Configure a origem.** Aponte o passo para a tabela de valores e escolha a coluna com o montante a alocar.
5. **Configure o indutor.** Aponte o passo para a tabela de indutores e escolha a coluna com os valores do indutor.
6. **Mapeie a dimensão.** Identifique que coluna de cada tabela representa os membros da dimensão. O passo de alocação utiliza-as para fazer corresponder as linhas de origem às linhas de indutores.
7. **Execute o passo.** O resultado é uma nova tabela com uma linha por montante repartido.
8. **Inspecione os resultados.** Verifique se os totais correspondem ao esperado — a soma dos montantes alocados deve ser igual à soma dos montantes de origem (dentro da tolerância de arredondamento).

## Seguimentos comuns

- **Repartição recursiva** — se um destino contiver, ele próprio, indutores para uma alocação adicional, consulte [Alocações recursivas](/pt-pt/guides/allocations/setup/recursive-allocations/).
- **Etiquetar linhas para alocação** — para determinar *que* linhas são alocadas a que destinos, consulte [Etiquetagem baseada em regras](/pt-pt/guides/allocations/getting-started/rule-based-tagging/).
- **Investigar resultados inesperados** — se os totais não reconciliam ou algumas linhas parecem erradas, consulte [Resolução de problemas das alocações](/pt-pt/guides/allocations/results/troubleshooting-allocations/).

## Passos seguintes

- [Para que servem as alocações?](/pt-pt/guides/allocations/getting-started/why-are-allocations-useful/) — quando as utilizar
- [Configurar uma alocação](/pt-pt/guides/allocations/setup/configure-an-allocation/) — referência de configuração mais detalhada
- [Tipos de passos de alocação](/pt-pt/reference/workflow-steps/allocation/) — todos os passos de fluxo de trabalho da categoria Alocação
