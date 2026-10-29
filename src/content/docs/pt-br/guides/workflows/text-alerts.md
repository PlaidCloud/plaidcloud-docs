---
title: Alertas por texto
description: Aceite receber alertas de fluxos de trabalho do PlaidCloud como mensagens de texto no seu número de celular dos EUA e desative-os novamente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/text-alerts.md
---

Os fluxos de trabalho podem enviar um texto quando precisam de atenção, com a etapa [Notify Via SMS](/pt-br/reference/workflow-steps/notifications/notify-via-sms/). Um fluxo de trabalho só pode enviar texto para você depois que você mesmo aceitar.

## Ativar os alertas por texto

1. Abra o menu do usuário no canto superior direito e escolha **Alertas por texto**.
2. Insira seu **Número de celular dos EUA**.
3. Marque **Concordo em receber alertas por mensagem de texto de fluxos de trabalho do PlaidCloud neste número.** Leia as divulgações acima dela e os links **SMS Terms** e **SMS Privacy Policy**.
4. Clique em **Enviar código**. O PlaidCloud envia por texto um código de 6 dígitos para o seu número. Os textos podem levar um ou dois minutos para chegar.
5. Insira o **Código de confirmação** em até 10 minutos e clique em **Confirmar**.

Depois de enviar um código, o botão faz uma contagem regressiva de 60 segundos e depois exibe **Reenviar código**. Reenviar enquanto seu código ainda é válido envia o mesmo código por texto, então qualquer texto que chegar funciona. Você pode solicitar 3 códigos por número de telefone por dia e 3 por pessoa por hora.

A janela então exibe **Os alertas por texto estão ativados para** o seu número mascarado. Somente números de celular dos EUA são aceitos. Podem ser aplicadas tarifas de mensagens e de dados, e a frequência das mensagens varia.

## Desativar os alertas por texto

Abra **Alertas por texto** e clique em **Parar alertas por texto**, ou responda **STOP** a qualquer texto. Responda **HELP** para obter ajuda.

## Reativá-los após um STOP

Responder STOP bloqueia todos os textos para o seu número. Envie **START** por texto para o número de alerta exibido na janela, depois envie um novo código e confirme-o.

## Se algo der errado

| Mensagem | O que fazer |
|---|---|
| Esse código não está correto | Confira o texto e insira o código novamente. |
| Esse código expirou | Clique em **Enviar código** para obter um novo. |
| Códigos incorretos demais | Após 5 códigos incorretos, clique em **Enviar código** para obter um novo. |
| Insira um número de celular dos EUA válido | Use um número de celular dos EUA de 10 dígitos. |
| Solicitações demais | Você atingiu um limite de códigos. Aguarde alguns minutos e tente novamente. |
| Os alertas por texto não estão disponíveis para o seu espaço de trabalho no momento | Tente novamente mais tarde. |

Não use alertas por texto para dados pessoais de saúde ou financeiros. Dúvidas: support@plaidcloud.com.
