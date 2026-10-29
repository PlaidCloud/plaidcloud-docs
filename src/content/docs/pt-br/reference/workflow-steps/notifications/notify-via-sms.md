---
title: Notify Via SMS
description: Envie uma mensagem de texto a partir de uma etapa de fluxo de trabalho para membros do espaço de trabalho que aceitaram receber alertas por texto, com confirmação de entrega, e-mail de contingência, agrupamento de repetições e horário silencioso.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-sms.md
---

## Descrição

Envie mensagens de texto a membros do espaço de trabalho quando um fluxo de trabalho precisar da atenção deles. Um texto só vai para um membro que aceitou receber por conta própria, em **Alertas por texto** no menu do usuário, com um número de celular dos EUA que ele confirmou. Você escolhe membros ou uma lista de distribuição; nunca digita um número de telefone na etapa. Para aceitar receber, consulte [Alertas por texto](/pt-br/guides/workflows/text-alerts/).

Os textos funcionam apenas com números dos EUA. Não inclua dados pessoais de saúde ou financeiros em um texto.

Os textos vêm de um único número de alerta do PlaidCloud e começam com `PlaidCloud [your workspace name]: ` seguido da sua mensagem. Consulte os [Termos de SMS](https://plaidcloud.com/sms-terms/) e a [Política de privacidade de SMS](https://plaidcloud.com/sms-privacy/).

## Destinatários

Escolha **Membros** ou **Lista de distribuição**.

- **Membros** lista os membros do seu espaço de trabalho. Cada um mostra **Aceitou receber**, **Não aceitou receber** ou **Inscrição cancelada - Envie START por mensagem de texto para o número de alerta**.
- **Lista de distribuição** envia texto a todos os membros da lista que aceitaram receber.

Um membro que não aceitou receber não recebe texto. Ele é um problema para a etapa (veja **Se um texto não puder ser entregue**) e, por padrão, recebe a mensagem por e-mail.

## Mensagem

Escreva a **Mensagem**. As variáveis do projeto e as variáveis do fluxo de trabalho funcionam, e **Inserir variável** adiciona qualquer uma destas:

| Variável | Valor |
|---|---|
| `{workflow_name}` | O nome do fluxo de trabalho em execução |
| `{project_name}` | O nome do projeto |
| `{run_url}` | Um link para a execução no PlaidCloud |
| `{project}`, `{model}`, `{cloud}`, `{date}` | As variáveis existentes |

O contador abaixo da mensagem mostra aproximadamente quantos caracteres e segmentos o texto ocupa, incluindo o prefixo `PlaidCloud [workspace]:` e o link da execução. Um texto é cortado após 3 segmentos. Links de encurtadores de links públicos são rejeitados.

## Entrega

| Configuração | O que faz |
|---|---|
| **Se um texto não puder ser entregue** | **Falhar a etapa** (padrão) ou **Avisar e continuar**. Um texto que não é entregue nunca passa em silêncio: ele é sempre informado na etapa. |
| **Enviar e-mail aos destinatários cujo texto não puder ser entregue** | Ativado por padrão. Um membro cujo texto falha, que não aceitou receber ou que cancelou o recebimento recebe a mensagem por e-mail. |
| **Agrupar repetições por (minutos)** | Padrão: 60. Uma repetição da mesma mensagem para o mesmo membro dentro desse intervalo não é enviada, e o próximo texto enviado termina com `(+N similar since HH:MM)`. |
| **Reter textos durante o horário silencioso** | Escolha os horários **De** e **até** e um fuso horário. Um texto que seria enviado dentro da janela fica retido até que ela termine. |

Cada membro recebe no máximo 20 textos por dia, um espaço de trabalho envia no máximo 500 textos e e-mails de contingência por dia, e uma etapa envia texto a no máximo 50 membros por vez.

## Enviar teste para mim

**Enviar teste para mim** envia um texto de teste para o seu próprio número e mostra o resultado ao lado do botão. Se você não aceitou receber, a janela **Alertas por texto** é aberta para que você possa aceitar.

## O que os destinatários veem

Todo texto vem do número de alerta. Responder **STOP** interrompe todos os textos do PlaidCloud para esse número, e **HELP** retorna informações de contato. Depois de STOP, o membro envia **START** por texto ao número de alerta para retomar e, em seguida, ativa novamente os alertas por texto em **Alertas por texto**. O formulário da etapa mostra **Inscrição cancelada - Envie START por mensagem de texto para o número de alerta** ao lado desse membro até que isso aconteça.

Os administradores do espaço de trabalho podem ver o status de alerta por texto de cada membro, com o número mascarado, na guia **Informações do membro** da janela do membro. Os membros aceitam e cancelam o recebimento por conta própria; um administrador não pode fazer isso por eles.

## Etapas que usavam um número digitado

Uma versão anterior desta etapa recebia um provedor de celular e um número de telefone digitado. Uma etapa que ainda esteja salva dessa forma não faz o fluxo de trabalho falhar e não envia nenhum texto ao número digitado.

- **Nenhum destinatário escolhido:** a etapa é concluída com um aviso, *Nenhum texto foi enviado: esta etapa ainda usa o provedor e o número de celular descontinuados. Abra a etapa, escolha membros que aceitaram receber alertas por texto e salve.* Nada é enviado.
- **Membros ou uma lista de distribuição escolhidos:** a etapa envia texto a esses destinatários e ignora a operadora e o número remanescentes.

Para corrigir uma etapa, abra-a, escolha membros ou uma lista de distribuição e salve.

## Exemplos

Ainda não há exemplos...
