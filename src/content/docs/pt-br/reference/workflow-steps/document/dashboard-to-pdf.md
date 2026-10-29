---
title: Convert Dashboard to PDF
description: Renderize um painel do PlaidCloud em PDFs em uma conta de documentos, uma vez para cada linha de um conjunto de dados de filtros, aplicando os valores de cada linha como filtros do painel.
sidebar:
  order: 22
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/dashboard-to-pdf.md
---

## Descrição

Renderiza um painel em PDFs e os grava em uma conta de documentos. Use-a para colocar um painel em agendamento: um pacote de fechamento do mês, uma distribuição para pessoas que não fazem login ou um instantâneo arquivado de como os números estavam em determinado dia.

A etapa renderiza uma vez para cada linha de um conjunto de dados de filtros, aplicando os valores dessa linha como filtros do painel. Assim, uma única etapa pode gerar um conjunto de PDFs por região ou por entidade em uma só execução.

## Configuração

### Painel

O painel a ser renderizado.

### Conjunto de dados de filtros

A tabela cujas linhas controlam as renderizações: um PDF por linha.

### Caminho de saída

A conta de documentos e a pasta em que os PDFs são gravados.

### Opções

- **Geração simultânea de PDF** — quantas renderizações são executadas ao mesmo tempo. O padrão é 8; diminua esse valor se o painel for pesado a ponto de as renderizações paralelas expirarem por tempo limite.
- **Tempo de espera da renderização (segundos)** — presente na configuração da etapa, mas **não aplicado atualmente** pelo executor de fluxo de trabalho. Definir esse valor não tem efeito hoje.

### Filtros do painel

Os filtros do próprio painel, cada um com seu **ID do filtro do painel**. Eles são lidos do painel quando você preenche o mapeamento.

### Mapeamento de colunas de origem

As colunas do conjunto de dados de filtros e como cada uma é usada. Use **Inspecionar origem › Preencher tabela de mapeamento** para ler as colunas e os filtros do painel; uma coluna com o mesmo nome de um filtro do painel é marcada como filtro dele. Ao preencher novamente, o **Tipo** e a **Coluna de filtro mapeada** que você já definiu em uma coluna são mantidos.

Defina o **Tipo** de cada coluna:

- **Filtro de coluna** — o valor da coluna define o filtro do painel indicado em **Coluna de filtro mapeada**, que deve ser um dos filtros do painel.
- **Nome do arquivo** — a coluna fornece o nome de cada PDF. Apenas uma coluna pode ser o Nome do arquivo. Sem uma, a etapa emite um aviso e gera os nomes automaticamente.
- **Sem filtro** — a coluna não é usada.

Pelo menos uma coluna deve ser um **Filtro de coluna**.

## O que é verificado ao salvar

O salvamento da etapa é recusado, com o nome da coluna, quando:

- Nenhuma coluna é um Filtro de coluna com uma Coluna de filtro mapeada — *Marque pelo menos uma coluna de origem como Filtro de coluna, com a Coluna de filtro mapeada que ela define.*
- Um Filtro de coluna não tem Coluna de filtro mapeada, ou indica uma que não está entre os filtros do painel — *A Coluna de filtro mapeada 'Region' da coluna de origem 'region' não é um dos filtros do painel.*
- Mais de uma coluna é o Nome do arquivo — *Apenas uma coluna de origem pode ser o Nome do arquivo; region, entity são todas.*
- Uma coluna de Filtro de coluna ou de Nome do arquivo não tem tipo de dados — *A coluna de origem 'region' não tem tipo de dados; inspecione a origem novamente para atualizá-lo.* Algumas etapas salvas no formulário de etapa estão sem os tipos de suas colunas e falham em todas as execuções até recuperá-los. Execute **Inspecionar origem › Preencher tabela de mapeamento** para restaurá-los; as marcações de Filtro de coluna e Nome do arquivo são mantidas.

## Relacionados

- [Etapas de documento](/pt-br/reference/workflow-steps/document/)
- [Painéis (guia)](/pt-br/guides/dashboards/)
- [Etapas de relatório](/pt-br/reference/workflow-steps/reports/)
