---
title: Porque são úteis as alocações
description: Compreenda porque são úteis as alocações de custos no PlaidCloud para a contabilidade de custos por atividade, a imputação interna e a análise de rentabilidade.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/why-are-allocations-useful.md
---

As alocações distribuem um conjunto de valores (normalmente custos, mas funcionam com qualquer agregado) pelos consumidores com base num indutor mensurável. Respondem à pergunta: *se incorrermos neste custo, como deve ser atribuído às entidades que o consomem?*

## Casos de utilização comuns

### Contabilidade de custos por atividade

Conhece o total da despesa de marketing de um trimestre. Pretende atribuí-lo a produtos específicos com base em algo mensurável: horas de campanha, contactos gerados, oportunidades qualificadas. Uma alocação distribui o conjunto de custos de marketing pelos produtos através do indutor escolhido, atribuindo a cada produto um custo totalmente imputado.

### Imputação de custos de TI

Gasta $X na operação de infraestrutura partilhada (computação, armazenamento, licenciamento). Cada unidade de negócio consome uma quantidade diferente. Uma alocação distribui o custo de TI pelas unidades com base em métricas de utilização (horas de VM, GB de armazenamento, licenças atribuídas), de modo que a demonstração de resultados de cada unidade reflita o que realmente consumiu.

### Distribuição de serviços partilhados

Finanças, recursos humanos, jurídico, instalações: funções centrais que servem toda a empresa. As alocações distribuem o respetivo custo pelas divisões servidas, normalmente com base no número de colaboradores, na receita ou numa combinação ponderada.

### Preços de transferência

Nas organizações com várias entidades, as alocações modelam a forma como os serviços internos são faturados entre entidades. O resultado alimenta os lançamentos de diário intragrupo.

### Análise de rentabilidade

Tem a receita ao nível do produto ou do cliente. Tem custos em vários conjuntos (vendas, suporte, infraestrutura, custo das mercadorias vendidas). As alocações reúnem tudo ao nível de granularidade do produto ou do cliente, para que possa ver a margem real.

### Custeio com lista de materiais

O custo flui por uma hierarquia de componentes. Cada passo da lista de materiais é uma alocação: os custos dos subconjuntos são distribuídos pelos conjuntos, os conjuntos pelos produtos acabados e os produtos acabados pelos SKU.

## O que as alocações lhe poupam

Sem um motor de alocação, estes modelos seriam criados em folhas de cálculo, que são frágeis, difíceis de auditar e difíceis de repetir com dados atualizados. As alocações do PlaidCloud oferecem:

- **Modelos reproduzíveis** que são executados novamente de forma automática à medida que os dados de origem são atualizados
- **Registo de auditoria** que mostra que linhas de origem contribuíram para que linhas de destino
- **Alocações em camadas** em que os resultados alimentam outras alocações
- **Integração dimensional**, para que as alocações respeitem as hierarquias existentes

## Passos seguintes

- [Início rápido das alocações](/pt-pt/guides/allocations/getting-started/allocations-quick-start/) — crie uma em 30 minutos
- [Etiquetagem baseada em regras](/pt-pt/guides/allocations/getting-started/rule-based-tagging/) — controle o comportamento da alocação por linha
- [Configurar uma alocação](/pt-pt/guides/allocations/setup/configure-an-allocation/) — referência completa de configuração
