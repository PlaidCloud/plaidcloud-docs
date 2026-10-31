---
title: Gerir erros de passos
description: Trate e gira erros de passos em fluxos de trabalho do PlaidCloud, incluindo notificações de erro, lógica de repetição e opções de recuperação de falhas.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/managing-step-errors.md
---

Se um fluxo de trabalho tiver um erro durante o processamento, é apresentado um indicador de erro tanto no fluxo de trabalho como no passo que teve o erro. O PlaidCloud pode repetir um passo falhado várias vezes. Isto é muitas vezes útil se o passo aceder a sistemas remotos ou a dados que possam não ter elevada disponibilidade ou que falhem de forma intermitente por motivos desconhecidos. A capacidade de repetição pode ser definida para repetir muitas vezes, bem como para acrescentar um atraso entre repetições, de segundos a horas.



Um passo cujo servidor é perdido a meio da execução é tratado separadamente das repetições: um passo que pode ser repetido em segurança é executado novamente de forma automática, e um que não pode falha uma só vez com uma mensagem de **interrompido**. Consulte [Passos interrompidos](/pt-pt/guides/workflows/run-a-workflow/#passos-interrompidos).

Quando o PlaidCloud recusa um passo por um motivo que pode corrigir, como uma permissão em falta ou uma definição que não é válida, o registo do passo mostra essa mensagem em linguagem simples, em vez de um erro de servidor com um rastreio de pilha. Num passo Model Loop, Model Run ou Macro Run cujo fluxo de trabalho subordinado falha, é apresentada a mensagem de erro do próprio fluxo subordinado, como "Child workflow run failed:" seguida da mensagem.

Se não for selecionada nenhuma repetição ou se o número máximo de repetições for excedido, o passo será marcado como erro. Nesse caso, o PlaidCloud oferece três níveis de tratamento de erros:


* Parar o fluxo de trabalho quando ocorre um erro
* Marcar o passo como erro, mas continuar a processar o fluxo de trabalho
* Marcar o passo como erro e acionar um processo de fluxo de trabalho de correção, em vez de continuar o fluxo de trabalho atual

## Parar o fluxo de trabalho


Parar o fluxo de trabalho quando um passo tem um erro é a abordagem mais comum, uma vez que os fluxos de trabalho devem, em geral, ser executados sem erros. Isto pára o fluxo de trabalho e apresenta o indicador de erro tanto no passo como no fluxo de trabalho. O erro também é apresentado no monitor de atividade, mas não é tomada mais nenhuma ação.



## Continuar o processamento


Cada passo pode ser definido para continuar em caso de erro no formulário do passo. Se esta caixa de verificação estiver ativada, qualquer passo será marcado com um erro caso este ocorra, mas o fluxo de trabalho tratará o erro como uma conclusão do passo e continuará. Isto é muitas vezes útil se existirem passos que executam tarefas que podem dar erro quando faltam dados, mas que são inofensivos para os processos globais.



Uma vez que, neste cenário, o fluxo de trabalho continua em caso de erro, não apresentará um indicador de erro e continuará a mostrar um indicador de execução.



## Acionar o fluxo de trabalho de correção


Com a possibilidade de definir um fluxo de trabalho de correção como parte da configuração do fluxo de trabalho, um erro no fluxo de trabalho interrompe de imediato o processamento do fluxo de trabalho atual e inicia o processamento do fluxo de trabalho de correção. Tenha em atenção que, se um passo estiver marcado para continuar em caso de erro, uma falha nesse passo não acionará o fluxo de trabalho de correção. Apenas os passos que falham e que fariam também parar todo o fluxo de trabalho acionarão o processo de correção.



Um fluxo de trabalho de correção pode ser útil simplesmente para notificar as pessoas de que ocorreu uma falha, ou pode realizar outro processamento complexo para tentar corrigir automaticamente quaisquer causas subjacentes da falha do fluxo de trabalho original.
