---
title: Continuar em caso de erro
description: Configure as etapas de um fluxo de trabalho do PlaidCloud para continuar a execução em caso de erro, permitindo que as etapas seguintes sejam executadas apesar de falhas anteriores.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/continue-on-error.md
---

As etapas do fluxo de trabalho podem ser configuradas para continuar o processamento mesmo quando há um erro. Isso pode ser útil em condições de inicialização do fluxo de trabalho ou quando os dados ficam disponíveis de forma intermitente. Se a etapa apresentar erro, ele será registrado como erro, mas o fluxo de trabalho continuará a ser processado.



Para definir essa opção, abra o formulário da etapa na tabela do fluxo de trabalho — clique no ícone de engrenagem ou clique com o botão direito e escolha **Editar detalhes da etapa** — e vá para a guia **Geral**. Defina **Ação a executar em caso de erro** como **Continuar**. Depois de salvar a etapa atualizada, nenhum erro nela fará o fluxo de trabalho parar.



As etapas configuradas para continuar em caso de erro têm um indicador especial na tabela de hierarquia de etapas do fluxo de trabalho.
