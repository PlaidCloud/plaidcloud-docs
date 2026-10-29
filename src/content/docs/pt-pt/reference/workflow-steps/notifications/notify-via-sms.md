---
title: Notify Via SMS
description: Envie uma mensagem de texto a partir de um passo de fluxo de trabalho a membros da área de trabalho que aderiram aos alertas por mensagem de texto, com confirmação de entrega, alternativa por correio eletrónico, agrupamento de repetições e horas de silêncio.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-sms.md
---

## Descrição

Envie uma mensagem de texto aos membros da área de trabalho quando um fluxo de trabalho precisar da sua atenção. Uma mensagem de texto só é enviada a um membro que tenha aderido por si próprio, em **Alertas por mensagem de texto** no menu do utilizador, com um número de telemóvel dos EUA que confirmou. Escolhe membros ou uma lista de distribuição; nunca escreve um número de telefone no passo. Para aderir, consulte [Alertas por mensagem de texto](/pt-pt/guides/workflows/text-alerts/).

As mensagens de texto destinam-se apenas a números dos EUA. Não inclua dados pessoais de saúde ou financeiros numa mensagem de texto.

As mensagens de texto provêm de um único número de alertas do PlaidCloud e começam por `PlaidCloud [your workspace name]: ` seguido da sua mensagem. Consulte os [Termos de SMS](https://plaidcloud.com/sms-terms/) e a [Política de privacidade de SMS](https://plaidcloud.com/sms-privacy/).

## Destinatários

Escolha **Membros** ou **Lista de distribuição**.

- **Membros** lista os membros da sua área de trabalho. Cada um mostra **Subscrito**, **Não subscrito** ou **Optou por sair - Envie START por SMS para o número de alertas**.
- **Lista de distribuição** envia uma mensagem de texto a todos os membros da lista que tenham aderido.

Um membro que não tenha aderido não recebe qualquer mensagem de texto. Constitui um problema para o passo (consulte **Se não for possível entregar uma mensagem de texto**) e, por predefinição, recebe a mensagem por correio eletrónico.

## Mensagem

Escreva a **Mensagem**. As variáveis do projeto e as variáveis do fluxo de trabalho funcionam, e **Inserir variável** adiciona qualquer uma das seguintes:

| Variável | Valor |
|---|---|
| `{workflow_name}` | O nome do fluxo de trabalho em execução |
| `{project_name}` | O nome do projeto |
| `{run_url}` | Uma ligação para a execução no PlaidCloud |
| `{project}`, `{model}`, `{cloud}`, `{date}` | As variáveis existentes |

O contador sob a mensagem mostra aproximadamente quantos carateres e segmentos a mensagem de texto ocupa, incluindo o prefixo `PlaidCloud [workspace]:` e a ligação da execução. Uma mensagem de texto é truncada para além de 3 segmentos. As ligações de encurtadores de ligações públicos são rejeitadas.

## Entrega

| Definição | O que faz |
|---|---|
| **Se não for possível entregar uma mensagem de texto** | **Falhar o passo** (predefinição) ou **Avisar e continuar**. Uma mensagem de texto que não é entregue nunca passa em silêncio: é sempre comunicada no passo. |
| **Enviar correio eletrónico aos destinatários cuja mensagem de texto não possa ser entregue** | Ativado por predefinição. Um membro cuja mensagem de texto falhe, que não tenha aderido ou que tenha optado por sair recebe a mensagem por correio eletrónico. |
| **Agrupar repetições durante (minutos)** | Predefinição 60. Uma repetição da mesma mensagem ao mesmo membro dentro deste período não é enviada, e a mensagem de texto seguinte a ser enviada termina com `(+N similar since HH:MM)`. |
| **Reter mensagens de texto durante as horas de silêncio** | Escolha as horas **De** e **a** e um fuso horário. Uma mensagem de texto que seria enviada dentro da janela é retida até esta terminar. |

Cada membro recebe no máximo 20 mensagens de texto por dia, uma área de trabalho envia no máximo 500 mensagens de texto e correios eletrónicos alternativos por dia, e um passo envia mensagens de texto a no máximo 50 membros de cada vez.

## Enviar Teste para Mim

**Enviar teste para mim** envia uma mensagem de texto de teste para o seu próprio número e mostra o resultado junto ao botão. Se não tiver aderido, a janela **Alertas por mensagem de texto** abre-se para que o possa fazer.

## O que os Destinatários Veem

Todas as mensagens de texto provêm do número de alertas. Responder **STOP** pára todas as mensagens de texto do PlaidCloud para esse número, e **HELP** devolve as informações de contacto. Depois de STOP, um membro envia **START** por mensagem de texto para o número de alertas para retomar e, em seguida, volta a ativar os alertas por mensagem de texto em **Alertas por mensagem de texto**. O formulário do passo mostra **Optou por sair - Envie START por SMS para o número de alertas** junto a esse membro até que o faça.

Os administradores da área de trabalho podem ver o estado dos alertas por mensagem de texto de cada membro, com o número mascarado, no separador **Informações do membro** da janela do membro. Os membros aderem e saem por si próprios; um administrador não o pode fazer por eles.

## Passos que Tinham um Número Escrito

Uma versão anterior deste passo aceitava um fornecedor móvel e um número de telefone escrito. Um passo ainda guardado dessa forma não faz falhar o fluxo de trabalho e não envia qualquer mensagem de texto para o número escrito.

- **Nenhum destinatário escolhido:** o passo termina com um aviso, *No text was sent: this step still uses the retired mobile provider and number. Open the step, choose members who've opted in to text alerts, and save it.* Nada é enviado.
- **Membros ou uma lista de distribuição escolhidos:** o passo envia mensagens de texto a esses destinatários e ignora o operador e o número que sobraram.

Para corrigir um passo, abra-o, escolha membros ou uma lista de distribuição e guarde.

## Exemplos

Ainda sem exemplos...
