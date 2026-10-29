---
title: Macro Concurrent (passo)
description: Execute uma invocação isolada de macro por cada linha da tabela de indutores, com um limite de simultaneidade configurável.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/macro-concurrent.md
---

## Descrição

Executa uma [macro](/pt-pt/guides/workflows/create-a-macro/) uma vez por cada linha selecionada numa tabela de indutores do lado do chamador. Cada invocação filha comporta-se como um passo [Macro Run](/pt-pt/reference/workflow-steps/workflow-control/run-macro/):

- Recebe um `run_id` novo.
- É executada no seu próprio esquema temporário (`macrorun_<run_id>`).
- Recebe do chamador associações de tabelas, valores escalares e dimensões.
- Copia as tabelas de saída declaradas para os destinos do lado do chamador quando a invocação filha termina com `done` ou `warn`.
- Elimina o esquema temporário quando a invocação filha termina, falha ou é parada.

Utilize o passo Macro Concurrent quando o mesmo processo reutilizável deva ser executado para muitas linhas, como um período, entidade, cliente, lote de ficheiros ou região por cada linha da tabela de indutores.

## Indutor

- **Tabela** — a tabela do lado do chamador que contém uma linha por cada invocação da macro.
- **Execuções em simultâneo** — o número máximo de invocações filhas da macro a manter ativas ao mesmo tempo.

## Seleção de dados da tabela

Selecione as colunas da tabela de indutores de que cada invocação filha necessita. Estas colunas podem ser utilizadas pelas associações da macro e pelo filtro do driver.

## Filtro do driver

Pode adicionar regras de filtro para a tabela de indutores. Apenas as linhas correspondentes iniciam invocações filhas da macro.

## Macro

- **Projeto** — o projeto que contém a macro. Na v1, tem de ser o mesmo projeto do chamador.
- **Macro** — o fluxo de trabalho de macro a invocar por cada linha de indutor selecionada.

## Associações de entrada

As associações de entrada ligam os dados do lado do chamador às entradas declaradas da macro.

**Associações de entrada de tabelas:**

- **Tabela de origem do chamador** — a tabela copiada para o esquema temporário da invocação filha.
- **Porta de destino da macro** — o nome da tabela de entrada ou a porta da macro que recebe a tabela copiada.
- **Filtro de cópia de entrada** — cláusula `WHERE` opcional aplicada durante a cópia de entrada.
- **JSON das colunas** — projeção opcional de colunas em JSON, quando apenas determinadas colunas devem ser copiadas.

**Associações de entrada escalares e de dimensões:**

- **Variável da macro** — a variável do lado da macro a definir para a invocação filha.
- **Valor** — o valor literal, a referência a uma variável do chamador ou o valor de uma coluna do indutor a associar.

As entradas escalares e de dimensões são definidas antes da cópia de entrada das tabelas, pelo que os filtros das tabelas podem referenciar essas variáveis.

## Associações de saída

As associações de saída copiam as tabelas de resultados da macro para destinos do lado do chamador.

- **Porta de origem da macro** — o nome da tabela de saída ou a porta da macro a partir da qual copiar.
- **Tabela de destino do chamador** — a tabela do lado do chamador para a qual copiar.
- **JSON das colunas** — projeção opcional de colunas em JSON para a cópia de saída.

Cada linha do indutor tem de resolver para uma tabela de destino diferente, pelo que deve incluir uma coluna do indutor no nome do destino — por exemplo, `results_{region}`. A cópia de saída substitui o destino em vez de lhe acrescentar dados, pelo que duas linhas que resolvessem para o mesmo destino deixariam apenas o resultado da segunda; o passo recusa essa configuração antes de iniciar o que quer que seja. Para combinar os resultados numa única tabela, adicione a jusante um passo que una as tabelas de cada linha.

A cópia de saída é ignorada numa invocação filha parada, para que os resultados parciais não sejam escritos em tabelas duradouras do chamador.

## Quando uma invocação filha deixa de responder

Uma invocação filha comunica o seu próprio resultado quando termina, pelo que uma invocação filha cuja máquina pare sem aviso nunca comunica nada. Em vez de esperar indefinidamente por ela, o passo verifica se cada invocação filha por que ainda aguarda está ativa.

- Uma invocação filha que já iniciou é verificada aproximadamente uma vez por minuto, e apenas enquanto não mostrar sinais de progresso. Uma invocação filha que esteja a executar um único passo demorado não mostra progresso durante todo o tempo que esse passo demorar, e é deixada em paz enquanto estiver realmente em execução.
- Uma invocação filha que foi aceite mas não iniciou em 15 minutos é tratada como nunca tendo iniciado. Esse intervalo abrange o agendamento e a obtenção da imagem, não o trabalho da própria macro.

Uma invocação filha tratada de qualquer das formas é parada, o respetivo esquema temporário é eliminado, e o passo falha no final, indicando essa invocação, o último estado que comunicou e quando o comunicou pela última vez.

**As restantes invocações filhas não são afetadas.** Executam-se até ao fim e as suas tabelas de saída são escritas normalmente, pelo que uma invocação sem resposta entre muitas não descarta as restantes. Apenas as invocações que não puderam ser concluídas são indicadas na falha.

Se a própria verificação não puder ser respondida — por exemplo, enquanto a plataforma está brevemente inacessível — a invocação filha é tratada como ainda em execução e verificada novamente na passagem seguinte.

## Comportamento ao parar

Parar o passo Macro Concurrent principal para todas as invocações filhas ativas da macro e elimina cada esquema de execução ativo. As invocações filhas que ainda não iniciaram não são lançadas depois de o passo principal ser parado.

## Ver também

- [Criar uma macro](/pt-pt/guides/workflows/create-a-macro/) — declare um fluxo de trabalho como macro e defina o seu contrato de portas.
- [Macro Run](/pt-pt/reference/workflow-steps/workflow-control/run-macro/) — invoque uma macro uma única vez.
