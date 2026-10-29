---
title: Notify Via Email
description: Envie notificações por correio eletrónico a partir de um passo de fluxo de trabalho do PlaidCloud, com assunto, corpo, destinatários e opções de anexos personalizáveis.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-email.md
---

## Descrição


Envie notificações por correio eletrónico. As mensagens são enviadas a partir da conta de correio eletrónico *[info@tartansolutions.com](mailto:info@tartansolutions.com)*. Não é necessária qualquer configuração de envio.



### Endereços de correio eletrónico


Indique qualquer número de destinatários. Os delimitadores aceites incluem o ponto e vírgula (;) e a vírgula (,).



### Cc, Bcc e Responder para

**Cc** (`cc_address`), **Bcc** (`bcc_address`) e **Responder para** (`reply_to`) recebem endereços com o mesmo formato dos destinatários e aceitam variáveis do projeto e do fluxo de trabalho. Os destinatários em Cc e Bcc recebem a mesma mensagem, e as respostas seguem para o endereço de Responder para. Aplicam-se a corpos de texto simples e a corpos de modelo Jinja. Defina-os em **Mais opções de e-mail**, no separador **Mensagem**.

### Um e-mail para cada linha

Em **Mais opções de e-mail**, defina **Enviar** (`request_source`) como **Um e-mail por linha de uma tabela** (`table`) e escolha uma **Tabela de indutores** (`driver_table`) para enviar um e-mail por cada linha de uma tabela em vez de um único e-mail. **Máximo de linhas a enviar** (`row_limit`) limita as linhas utilizadas e é, por predefinição, 10 000. O indutor tem de ser uma tabela, não uma vista.

Utilize `{{row.column}}` nos endereços, no assunto, na mensagem e no caminho do anexo para preencher o valor de cada linha. Uma coluna que a tabela de indutores não tenha faz o passo falhar. Uma linha sem endereço de destino não envia nada para essa linha e o passo termina com um aviso que a identifica.

Um caminho de anexo preenchido a partir de uma linha (`{{row.column}}`) tem de ser um único ficheiro existente, nunca uma pasta, para que uma linha cujo caminho tenha ficado errado não consiga enviar os ficheiros de outra pessoa. Uma linha cujo valor para esse caminho esteja vazio, cujo caminho saia da respetiva pasta com `..` ou cujo ficheiro não exista é enviada sem o anexo, com um aviso que identifica a linha. O envio por linha requer um corpo simples e não está disponível com um corpo de modelo Jinja.

### Mensagem


Indique o **Assunto** e o **Corpo** como pretender.



Tenha em atenção que as Variáveis do projeto e as variáveis do fluxo de trabalho estão ambas disponíveis para utilização com esta transformação, tanto na linha de assunto como no corpo da mensagem.



Além disso, é permitido código HTML normal no corpo para personalizar ainda mais o aspeto das mensagens de correio eletrónico.


### Anexos


Anexar ficheiros a mensagens de correio eletrónico é muito simples. Selecione um ficheiro ou uma pasta de Documento para anexar. Se selecionar uma pasta, o conteúdo da pasta é anexado como ficheiros individuais. A substituição de variáveis funciona com os caminhos, para um melhor controlo dos anexos ao enviar mensagens personalizadas.



Para anexar vários documentos, assinale **Adicionar anexo ao correio eletrónico** e liste-os em **Mais anexos** (`attachments`), em **Mais opções de e-mail**, cada um com um **ID da conta** e um **Caminho do documento**; são enviados juntamente com o anexo que selecionar, e um caminho pode utilizar variáveis e tokens de linha da mesma forma.

### Prioridade e texto simples

Em **Mais opções de e-mail**, **Prioridade** (`priority`) marca a mensagem como **Baixa**, **Normal** ou **Alta** (`low`, `normal`, `high`), e **Enviar como** (`content_type`) definido como **Texto simples** (`text`) envia o corpo como texto simples em vez de **HTML** (`html`, o valor predefinido).

### Corpo (modelo Jinja)


O corpo do passo é criado como um **modelo Jinja** renderizado sobre um ou mais **frames**, produzindo um e-mail HTML rico. Cada frame é uma seleção nomeada de uma única tabela — um Nome do frame, uma tabela do fluxo de trabalho e, opcionalmente, uma seleção de colunas, um filtro where e agregação (sem junções). O editor abre diretamente neste modelo — a lista de frames, o corpo do modelo, uma pré-visualização em direto e um botão **Enviar teste para mim** —, sem alternância entre texto simples e modelo. Um botão **Embelezar** e uma paleta de inserção (`render_table(...)` para um frame, `{{ cloud }}`, um ciclo for e os filtros de moeda/milhares/percentagem/data) ajudam a dar forma ao modelo.

Referencie cada frame no modelo como `frames['<Frame Name>'].rows` e `frames['<Frame Name>'].columns`; um modelo de um só frame pode utilizar `rows` / `columns` de nível superior, que estão associados ao primeiro frame. O modelo é um motor de renderização separado e isolado (sandbox): apenas `cloud` é resolvido como valor da área de trabalho, e os tokens antigos `{project}` / `{model}` / `{date}` não são resolvidos no seu interior. Os passos criados antes da edição em Jinja abrem com o corpo antigo convertido automaticamente; um corpo que não possa ser convertido em segurança permanece num modo alternativo de texto simples e continua a enviar com a substituição antiga de `{token}`. Consulte [Enviar notificações por e-mail HTML com modelos](/pt-pt/guides/workflows/notify-email-templates/) para ver as variáveis de modelo disponíveis, o auxiliar `render_table`, as etiquetas e os atributos HTML que sobrevivem ao sanitizador de e-mail e como os corpos existentes são migrados.



## Exemplos


Neste exemplo, são utilizadas todas as variáveis de sistema. Além disso, é utilizado um pouco de HTML para formatar a primeira linha do corpo. A execução desta transformação envia o seguinte correio eletrónico:


* PARA: [info@tartansolutions.com](mailto:info%40tartansolutions.com)
* DE: [info@tartansolutions.com](mailto:info%40tartansolutions.com) (lembre-se de que todas as mensagens são enviadas deste endereço)
* Assunto: DEMO – Workflow Analyze Demo Running
