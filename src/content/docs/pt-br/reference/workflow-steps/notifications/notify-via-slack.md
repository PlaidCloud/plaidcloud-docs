---
title: Notify via Slack
description: Envie notificações do Slack a partir de uma etapa de fluxo de trabalho do PlaidCloud para alertar canais ou usuários sobre eventos, erros e o status do fluxo de trabalho.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-slack.md
---

Adicionar notificações do Slack a partir de um fluxo de trabalho é um processo em duas partes. As duas partes são:


1. Criar uma conexão externa de webhook do Slack
2. Adicionar etapas de notificação do Slack aos seus fluxos de trabalho

## Adicionar a etapa de notificação do Slack ao fluxo de trabalho


Adicionar etapas de notificação do Slack ao fluxo de trabalho é igual a adicionar outras etapas a um fluxo de trabalho. Ao adicionar a etapa, abra a configuração da etapa, preencha o formulário e salve. Agora você pode testar sua notificação do Slack.



## Anexar um arquivo

Escolha um documento em **Arquivo a carregar** para enviá-lo ao canal com a mensagem como seu comentário. Um webhook não pode transportar um arquivo, então um anexo passa por um token de bot na conexão do Slack:

- Adicione um **Token de bot** à conexão. É o token `xoxb-` de um aplicativo do Slack com o escopo `files:write`, e o aplicativo precisa ser convidado para o canal.
- Informe o **ID do canal** na etapa, como `C0123ABCD`, e não o nome do canal. O carregamento de arquivos do Slack aceita apenas IDs, e a etapa falha sem um. Para encontrar um ID, abra os detalhes do canal no Slack e role até o final.
- Se o documento não for encontrado, a mensagem é enviada pelo webhook sem ele, e a etapa emite um aviso com o caminho do documento.

## Formatar a mensagem do Slack


O Slack tem muitas opções de formatação, incluindo adicionar imagens e mencionar usuários. Consulte a documentação [Formatação de texto do Slack](https://api.slack.com/reference/surfaces/formatting) para obter detalhes.



## Criar a conexão externa de webhook do Slack


Esta é uma configuração única que permite ao PlaidCloud enviar notificações do Slack em seu nome. O Slack permite criar um aplicativo de webhook (uma forma genérica de enviar uma notificação pela internet). Depois de criar o aplicativo de webhook no Slack, adicione as credenciais fornecidas ao PlaidCloud para permitir seu uso.



### Criação do aplicativo de webhook do Slack


Estas etapas precisam ser realizadas por um administrador do Slack. Siga estas etapas para criar um aplicativo de webhook do Slack:


1. No Slack, abra o menu de controle do espaço de trabalho e selecione `Settings & administration > Manage Apps`
2. Selecione `Custom Integrations` na lista de categorias de aplicativos
3. Selecione `Incoming Webhooks` na lista de aplicativos
4. Selecione o botão `Add to Slack`
5. Na tela seguinte, selecione o canal do Slack no qual deseja publicar as mensagens e continue. Esse é o canal padrão que será usado, mas pode ser substituído em cada notificação, inclusive para enviar mensagens diretas a pessoas específicas.
6. Copie a URL do webhook exibida. Ela será usada mais tarde, então guarde-a em um local seguro. Ela terá uma aparência semelhante a esta: `https://hooks.slack.com/services/T04QZ1435/G02TGBFTOP8/K9GZrR2ThdJz1uSiL9YeZxoR`
7. Você pode personalizar a aparência, o nome e o emoji antes de salvar. Essas personalizações são apenas os padrões e podem ser substituídas em cada etapa de notificação dentro de um fluxo de trabalho do PlaidCloud.

### Configuração da conexão externa do PlaidCloud


Estas etapas precisam ser realizadas por um administrador do espaço de trabalho do PlaidCloud com permissão para criar Conexões de dados externas. Siga estas etapas para criar a conexão:


1. Acesse `Analyze > Tools > External Data Connections`
2. Em `+ New Connection`, escolha Webhook do Slack
3. Preencha o nome, a descrição e cole a URL do webhook fornecida na etapa 6 acima. O nome informado aqui será exibido como a opção de seleção na etapa do fluxo de trabalho, portanto, se possível, deve ser descritivo. Qualquer pessoa que tenha a URL pode publicar no seu canal, por isso o campo **URL do webhook** a mascara quando você a cola e aparece em branco quando você reabre a conexão; deixe-o em branco para manter a URL salva.
4. Para enviar anexos, cole também o token de bot do aplicativo do Slack no campo **Token de bot (para carregar arquivos)**. Uma conexão pode conter a URL do webhook, o token de bot ou ambos. O token de bot é mascarado como a URL do webhook e aparece em branco quando você reabre a conexão.
5. Selecione o botão `+ Create`


## Exemplos

Ainda não há exemplos...
