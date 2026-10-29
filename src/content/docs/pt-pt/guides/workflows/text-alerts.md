---
title: Alertas por mensagem de texto
description: Subscreva para receber alertas de fluxos de trabalho do PlaidCloud como mensagens de texto no seu número de telemóvel dos EUA e desative-os novamente.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/text-alerts.md
---

Os fluxos de trabalho podem enviar-lhe uma mensagem de texto quando precisam de atenção, com o passo [Notify Via SMS](/pt-pt/reference/workflow-steps/notifications/notify-via-sms/). Um fluxo de trabalho só pode enviar-lhe mensagens depois de ter dado o seu consentimento.

## Ativar os alertas por mensagem de texto

1. Abra o menu do utilizador no canto superior direito e escolha **Alertas por mensagem de texto**.
2. Introduza o seu **Número de telemóvel dos EUA**.
3. Assinale **Aceito receber alertas por mensagem de texto de fluxos de trabalho do PlaidCloud neste número.** Leia as divulgações acima da mesma e as ligações **SMS Terms** e **SMS Privacy Policy**.
4. Clique em **Enviar código**. O PlaidCloud envia por mensagem de texto um código de 6 dígitos para o seu número. As mensagens podem demorar um ou dois minutos a chegar.
5. Introduza o **Código de confirmação** no prazo de 10 minutos e clique em **Confirmar**.

Depois de enviar um código, o botão faz uma contagem decrescente de 60 segundos e passa a indicar **Reenviar código**. Reenviar enquanto o seu código ainda é válido envia o mesmo código, pelo que qualquer uma das mensagens que chegar funciona. Pode pedir 3 códigos por número de telefone por dia e 3 por pessoa por hora.

A janela passa então a indicar **Os alertas por mensagem de texto estão ativados para** o seu número mascarado. Só são suportados números de telemóvel dos EUA. Podem aplicar-se tarifas de mensagens e de dados, e a frequência das mensagens varia.

## Desativar os alertas por mensagem de texto

Abra **Alertas por mensagem de texto** e clique em **Parar alertas por mensagem de texto**, ou responda **STOP** a qualquer mensagem. Responda **HELP** para obter ajuda.

## Reativá-los após STOP

Responder STOP bloqueia todas as mensagens para o seu número. Envie **START** para o número de alertas apresentado na janela, depois envie um novo código e confirme-o.

## Se algo correr mal

| Mensagem | O que fazer |
|---|---|
| That code is not right | Verifique a mensagem e introduza o código novamente. |
| That code has expired | Clique em **Enviar código** para obter um novo. |
| Too many wrong codes | Após 5 códigos errados, clique em **Enviar código** para obter um novo. |
| Enter a valid US mobile number | Utilize um número de telemóvel dos EUA com 10 dígitos. |
| Too many requests | Atingiu um limite de códigos. Aguarde alguns minutos e tente novamente. |
| Text alerts are not available for your workspace right now | Tente novamente mais tarde. |

Não utilize alertas por mensagem de texto para dados pessoais de saúde ou financeiros. Questões: support@plaidcloud.com.
