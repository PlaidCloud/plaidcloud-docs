---
title: Etapa Macro Concurrent
description: Execute uma invocação isolada de Macro por linha da tabela de direcionadores, com um limite de simultaneidade configurável.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/macro-concurrent.md
---

## Descrição

Executa uma [Macro](/pt-br/guides/workflows/create-a-macro/) uma vez para cada linha selecionada em uma tabela de direcionadores do lado do chamador. Cada invocação filha se comporta como uma etapa [Macro Run](/pt-br/reference/workflow-steps/workflow-control/run-macro/):

- Recebe um `run_id` novo.
- É executada em seu próprio esquema temporário (`macrorun_<run_id>`).
- Recebe do chamador vinculações de tabelas, escalares e dimensões.
- Copia as tabelas de saída declaradas de volta para os destinos do lado do chamador quando a invocação filha termina com `done` ou `warn`.
- Descarta o esquema temporário quando a invocação filha termina, falha ou é interrompida.

Use a etapa Macro Concurrent quando o mesmo processo reutilizável deve ser executado para muitas linhas, como um período, entidade, cliente, lote de arquivos ou região por linha da tabela de direcionadores.

## Direcionador

- **Tabela** — a tabela do lado do chamador que contém uma linha por invocação da Macro.
- **Execuções simultâneas** — o número máximo de invocações filhas da Macro mantidas ativas ao mesmo tempo.

## Seleção de dados da tabela

Selecione as colunas da tabela de direcionadores de que cada invocação filha precisa. Essas colunas podem ser usadas pelas vinculações da Macro e pelo filtro do direcionador.

## Filtro do direcionador

Opcionalmente, adicione regras de filtro para a tabela de direcionadores. Somente as linhas correspondentes iniciam invocações filhas da Macro.

## Macro

- **Projeto** — o projeto que contém a Macro. Deve ser o mesmo projeto do chamador na v1.
- **Macro** — o fluxo de trabalho Macro a invocar para cada linha de direcionador selecionada.

## Vínculos de entrada

Os vínculos de entrada conectam os dados do lado do chamador às entradas declaradas da Macro.

**Vínculos de entrada de tabela:**

- **Tabela de origem do chamador** — a tabela copiada para o esquema temporário da invocação filha.
- **Porta de destino da macro** — o nome da tabela de entrada ou a porta da Macro que receberá a tabela copiada.
- **Filtro de entrada da cópia** — cláusula `WHERE` opcional aplicada durante a cópia de entrada.
- **JSON de colunas** — projeção JSON de colunas opcional, para quando somente colunas selecionadas devem ser copiadas.

**Vínculos de entrada escalares e de dimensão:**

- **Variável da macro** — a variável do lado da Macro a definir para a invocação filha.
- **Valor** — o valor literal, a referência a uma variável do chamador ou o valor da coluna do direcionador a vincular.

As entradas escalares e de dimensão são definidas antes da cópia de entrada das tabelas, de modo que os filtros de tabela podem referenciar essas variáveis.

## Vínculos de saída

Os vínculos de saída copiam as tabelas de resultado da Macro de volta para os destinos do lado do chamador.

- **Porta de origem da macro** — o nome da tabela de saída ou a porta da Macro de onde copiar.
- **Tabela de destino do chamador** — a tabela do lado do chamador para a qual copiar.
- **JSON de colunas** — projeção JSON de colunas opcional para a cópia de saída.

Cada linha de direcionador deve resolver para uma tabela de destino diferente, portanto inclua uma coluna do direcionador no nome do destino — por exemplo, `results_{region}`. A cópia de saída substitui o destino em vez de acrescentar a ele; assim, duas linhas que resolvessem para o mesmo destino deixariam apenas o resultado da segunda linha. A etapa recusa essa configuração antes de iniciar qualquer coisa. Para combinar os resultados em uma única tabela, adicione uma etapa posterior que una as tabelas de cada linha.

A cópia de saída é ignorada para uma invocação filha interrompida, de modo que resultados parciais não sejam gravados em tabelas duráveis do chamador.

## Quando uma invocação filha para de responder

Uma invocação filha informa seu próprio resultado ao terminar; portanto, uma invocação filha cuja máquina para sem aviso nunca informa nada. Em vez de esperar indefinidamente por ela, a etapa verifica se cada invocação filha que ainda aguarda está ativa.

- Uma invocação filha que já começou é verificada aproximadamente uma vez por minuto, e somente enquanto não mostra sinal de progresso. Uma invocação filha que executa uma única etapa demorada não mostra progresso durante todo o tempo que essa etapa levar, e é deixada em paz enquanto estiver realmente em execução.
- Uma invocação filha que foi aceita mas não começou em 15 minutos é tratada como se nunca tivesse começado. Essa janela cobre o agendamento e o download da imagem, não o trabalho da própria Macro.

Uma invocação filha tratada de qualquer uma dessas formas é interrompida, seu esquema temporário é descartado e a etapa falha no final, citando essa invocação, o último estado que ela informou e quando o informou.

**As demais invocações filhas não são afetadas.** Elas são executadas até o fim e suas tabelas de saída são gravadas normalmente, de modo que uma invocação filha sem resposta entre muitas não descarta as outras. Somente as invocações que não puderam ser concluídas são citadas na falha.

Se a própria verificação não puder ser respondida — por exemplo, enquanto a plataforma está brevemente inacessível —, a invocação filha é tratada como ainda em execução e verificada novamente na próxima passagem.

## Comportamento de interrupção

Interromper a etapa Macro Concurrent pai interrompe todas as invocações filhas ativas da Macro e descarta o esquema de cada execução ativa. As invocações filhas que ainda não começaram não são iniciadas depois que o pai é interrompido.

## Relacionados

- [Criar uma Macro](/pt-br/guides/workflows/create-a-macro/) — declare um fluxo de trabalho como Macro e defina seu contrato de portas.
- [Macro Run](/pt-br/reference/workflow-steps/workflow-control/run-macro/) — invoque uma Macro uma única vez.
