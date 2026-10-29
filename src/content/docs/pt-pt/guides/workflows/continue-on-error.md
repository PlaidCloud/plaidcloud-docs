---
title: Continuar em caso de erro
description: Configure os passos de um fluxo de trabalho do PlaidCloud para continuarem a execução em caso de erro, permitindo que os passos seguintes sejam executados apesar de falhas anteriores.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/continue-on-error.md
---

Os passos de um fluxo de trabalho podem ser configurados para continuar o processamento mesmo quando há um erro. Isto pode ser útil em condições de arranque do fluxo de trabalho ou quando os dados podem estar disponíveis de forma intermitente. Se o passo der erro, este é registado como erro, mas o fluxo de trabalho continua a processar.



Para definir esta opção, abra o formulário do passo a partir da tabela do fluxo de trabalho — clique no respetivo ícone de engrenagem, ou clique com o botão direito e escolha **Editar detalhes do passo** — e aceda ao separador **Geral**. Defina **Ação a executar em caso de erro** como **Continuar**. Depois de guardar o passo atualizado, quaisquer erros do passo não farão com que o fluxo de trabalho pare.



Os passos que foram definidos para continuar em caso de erro têm um indicador especial na tabela da hierarquia de passos do fluxo de trabalho.
