---
title: Gerenciar erros de etapas
description: Trate e gerencie erros de etapas em fluxos de trabalho do PlaidCloud, incluindo notificações de erro, lógica de nova tentativa e opções de recuperação de falhas.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/managing-step-errors.md
---

Se um fluxo de trabalho tiver um erro durante o processamento, um indicador de erro é exibido tanto no fluxo de trabalho quanto na etapa que teve o erro. O PlaidCloud pode tentar novamente uma etapa com falha várias vezes. Isso costuma ser útil quando a etapa acessa sistemas remotos ou dados que podem não ter alta disponibilidade ou que falham de forma intermitente por motivos desconhecidos. A capacidade de nova tentativa pode ser configurada para muitas repetições, com um intervalo entre elas que vai de segundos a horas.



Uma etapa cujo servidor é perdido durante a execução é tratada separadamente das novas tentativas: uma etapa que pode ser repetida com segurança é executada novamente de forma automática, e uma que não pode falha uma única vez com uma mensagem de **interrompida**. Consulte [Etapas interrompidas](/pt-br/guides/workflows/run-a-workflow/#etapas-interrompidas).

Quando o PlaidCloud recusa uma etapa por um motivo que você pode corrigir, como uma permissão ausente ou uma configuração inválida, o log da etapa mostra essa mensagem em linguagem clara, em vez de um erro de servidor com um rastreamento de pilha. Em uma etapa Model Loop, Model Run ou Macro Run cujo fluxo de trabalho filho falha, é exibida a própria mensagem de erro do filho, como “Child workflow run failed:” seguida da mensagem.

Se nenhuma nova tentativa for selecionada ou o número máximo de tentativas for excedido, a etapa será marcada como erro. Nesse caso, o PlaidCloud oferece três níveis de tratamento de erros:


* Interromper o fluxo de trabalho quando ocorrer um erro
* Marcar a etapa como erro, mas continuar processando o fluxo de trabalho
* Marcar a etapa como erro e acionar um processo de fluxo de trabalho de correção em vez de continuar o fluxo de trabalho atual

## Interromper o fluxo de trabalho


Interromper o fluxo de trabalho quando uma etapa dá erro é a abordagem mais comum, já que os fluxos de trabalho em geral devem ser executados sem erros. Isso interrompe o fluxo de trabalho e exibe o indicador de erro tanto na etapa quanto no fluxo de trabalho. O erro também é exibido no monitor de atividades, mas nenhuma outra ação é tomada.



## Continuar o processamento


Cada etapa pode ser configurada para continuar em caso de erro no formulário da etapa. Se essa caixa de seleção estiver ativada, qualquer etapa será marcada com erro caso ele ocorra, mas o fluxo de trabalho tratará o erro como a conclusão da etapa e seguirá em frente. Isso costuma ser útil quando há etapas que executam tarefas que podem dar erro quando faltam dados, mas são inofensivas para os processos como um todo.



Como o fluxo de trabalho continua apesar do erro nesse cenário, ele não exibirá um indicador de erro e continuará mostrando um indicador de execução.



## Acionar fluxo de trabalho de correção


Com a possibilidade de definir um fluxo de trabalho de correção como parte da configuração do fluxo de trabalho, um erro no fluxo de trabalho interrompe imediatamente o processamento do fluxo de trabalho atual e inicia o processamento do fluxo de trabalho de correção. Observe que, se uma etapa estiver marcada para continuar em caso de erro, uma falha dela não acionará o fluxo de trabalho de correção. Somente as etapas que falham e que também fariam todo o fluxo de trabalho parar acionarão o processo de correção.



Um fluxo de trabalho de correção pode ser útil para simplesmente avisar as pessoas de que ocorreu uma falha, ou pode executar outros processamentos complexos para tentar corrigir automaticamente os motivos subjacentes pelos quais o fluxo de trabalho original falhou.
