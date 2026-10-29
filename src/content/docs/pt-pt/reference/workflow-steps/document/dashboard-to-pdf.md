---
title: Convert Dashboard to PDF (passo)
description: Renderiza um painel de controlo PlaidCloud em PDF numa conta de documentos, uma vez por linha de um conjunto de dados de filtros, aplicando os valores de cada linha como filtros do painel.
sidebar:
  order: 22
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/dashboard-to-pdf.md
---

## Descrição

Renderiza um painel de controlo em PDF e guarda-os numa conta de documentos. Utilize-o para colocar um painel de controlo num agendamento — um pacote de fim de mês, uma distribuição a pessoas que não iniciam sessão ou um instantâneo arquivado do aspeto dos números num determinado dia.

O passo renderiza uma vez por linha de um conjunto de dados de filtros, aplicando os valores dessa linha como filtros do painel de controlo, pelo que um único passo pode produzir um conjunto de PDF por região ou por entidade numa só execução.

## Configuração

### Painel de controlo

O painel de controlo a renderizar.

### Conjunto de dados de filtros

A tabela cujas linhas determinam as renderizações: um PDF por linha.

### Caminho de saída

A conta de documentos e a pasta onde os PDF são escritos.

### Opções

- **Geração de PDF em simultâneo** — quantas renderizações são executadas em simultâneo. O valor predefinido é 8; reduza-o se o painel de controlo for pesado ao ponto de as renderizações em paralelo excederem o tempo limite.
- **Tempo de espera da renderização (segundos)** — presente na configuração do passo, mas **atualmente não aplicado** pelo executor de fluxos de trabalho. Definir este valor não tem qualquer efeito atualmente.

### Filtros do painel de controlo

Os filtros do próprio painel de controlo, cada um com o respetivo **ID do filtro do painel de controlo**. São lidos a partir do painel quando preenche o mapeamento.

### Mapeamento de colunas de origem

As colunas do conjunto de dados de filtros e a forma como cada uma é utilizada. Utilize **Inspecionar origem › Preencher tabela de mapeamento** para ler as colunas e os filtros do painel; uma coluna com o mesmo nome de um filtro do painel é marcada como filtro dessa coluna. Se preencher novamente, os valores de **Tipo** e **Coluna de filtro mapeada** que já definiu numa coluna são mantidos.

Defina o **Tipo** de cada coluna:

- **Filtro de coluna** — o valor da coluna define o filtro do painel indicado em **Coluna de filtro mapeada**, que tem de ser um dos filtros do painel.
- **Nome do ficheiro** — a coluna fornece o nome do ficheiro de cada PDF. Apenas uma coluna pode ser o Nome do ficheiro. Sem uma, o passo emite um aviso e gera os nomes automaticamente.
- **Sem filtro** — a coluna não é utilizada.

Pelo menos uma coluna tem de ser um **Filtro de coluna**.

## O que é verificado ao guardar

A gravação do passo é recusada, indicando a coluna, quando:

- Nenhuma coluna é um Filtro de coluna com uma Coluna de filtro mapeada — *Marque pelo menos uma coluna de origem como Filtro de coluna, com a Coluna de filtro mapeada que define.*
- Um Filtro de coluna não tem Coluna de filtro mapeada, ou indica uma que não está entre os filtros do painel — *A Coluna de filtro mapeada 'Region' para a coluna de origem 'region' não é um dos filtros do painel.*
- Mais do que uma coluna é o Nome do ficheiro — *Apenas uma coluna de origem pode ser o Nome do ficheiro; region e entity são-no ambas.*
- Uma coluna de Filtro de coluna ou de Nome do ficheiro não tem tipo de dados — *A coluna de origem 'region' não tem tipo de dados; inspecione novamente a origem para o atualizar.* Alguns passos guardados no formulário do passo não têm os tipos das respetivas colunas e falham todas as execuções até que os recuperem. Execute **Inspecionar origem › Preencher tabela de mapeamento** para os repor; as suas marcações de Filtro de coluna e de Nome do ficheiro são mantidas.

## Relacionado

- [Passos de documentos](/pt-pt/reference/workflow-steps/document/)
- [Painéis de controlo (guia)](/pt-pt/guides/dashboards/)
- [Passos de relatórios](/pt-pt/reference/workflow-steps/reports/)
