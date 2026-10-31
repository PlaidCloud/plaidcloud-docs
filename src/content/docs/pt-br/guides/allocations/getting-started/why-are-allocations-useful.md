---
title: Por que as alocações são úteis
description: Entenda por que as alocações de custos são úteis no PlaidCloud para custeio baseado em atividades, rateio de custos e análise de rentabilidade.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/why-are-allocations-useful.md
---

As alocações distribuem um conjunto de valores (normalmente custos, mas funciona para qualquer valor agregado) entre os consumidores com base em um direcionador mensurável. Elas respondem à pergunta: *se incorremos neste custo, como ele deve ser atribuído aos itens que o consomem?*

## Casos de uso comuns

### Custeio baseado em atividades

Você sabe o total gasto em marketing em um trimestre. Quer atribuí-lo a produtos específicos com base em algo mensurável, como horas de campanha, leads gerados ou oportunidades qualificadas. Uma alocação distribui o conjunto de marketing entre os produtos usando o direcionador escolhido, dando a cada produto um custo totalmente absorvido.

### Rateio de custos de TI

Você gasta $X para manter uma infraestrutura compartilhada (computação, armazenamento, licenciamento). Cada unidade de negócios consome uma quantidade diferente. Uma alocação distribui o custo de TI entre as unidades com base em métricas de uso, como horas de VM, GB de armazenamento ou licenças, para que a DRE de cada unidade reflita o que ela realmente consumiu.

### Distribuição de serviços compartilhados

Finanças, RH, jurídico, instalações: funções centrais que atendem a empresa inteira. As alocações distribuem o custo delas entre as divisões atendidas, normalmente por número de funcionários, receita ou uma combinação ponderada.

### Preço de transferência

Para organizações com várias entidades, as alocações modelam como os serviços internos são precificados entre as entidades. O resultado alimenta os lançamentos contábeis entre empresas do grupo.

### Análise de rentabilidade

Você tem a receita no nível de produto ou cliente. Tem custos em vários conjuntos (vendas, suporte, infraestrutura, CPV). As alocações reúnem tudo na granularidade de produto/cliente para que você veja a margem real.

### Custeio de lista de materiais

O custo desce por uma hierarquia de componentes. Cada etapa da lista de materiais é uma alocação: os custos dos subconjuntos são distribuídos para os conjuntos, os conjuntos para os produtos acabados e os produtos acabados para os SKUs.

## O que as alocações evitam

Sem um mecanismo de alocação, você construiria esses modelos em planilhas, que são frágeis, difíceis de auditar e difíceis de repetir com dados atualizados. As alocações do PlaidCloud oferecem:

- **Modelos reproduzíveis** que são executados novamente de forma automática à medida que os dados de origem são atualizados
- **Trilha de auditoria** que mostra quais linhas de origem contribuíram para quais linhas de destino
- **Alocações em camadas**, em que as saídas alimentam outras alocações
- **Integração dimensional**, para que as alocações respeitem suas hierarquias existentes

## Próximas etapas

- [Início rápido de alocações](/pt-br/guides/allocations/getting-started/allocations-quick-start/) — crie uma em 30 minutos
- [Marcação baseada em regras](/pt-br/guides/allocations/getting-started/rule-based-tagging/) — controle o comportamento da alocação por linha
- [Configurar uma alocação](/pt-br/guides/allocations/setup/configure-an-allocation/) — referência completa de configuração
