---
title: Notify Via Email
description: Envie notificações por e-mail a partir de uma etapa de fluxo de trabalho do PlaidCloud, com assunto, corpo, destinatários e opções de anexo personalizáveis.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-email.md
---

## Descrição


Envie notificações por e-mail. As mensagens são enviadas a partir da conta de e-mail *[info@tartansolutions.com](mailto:info@tartansolutions.com)*. Nenhuma configuração de saída é necessária.



### Endereços de e-mail


Especifique qualquer número de destinatários de e-mail. Os delimitadores aceitos incluem ponto e vírgula (;) e vírgula (,).



### Cc, Cco e Responder para

**Cc** (`cc_address`), **Cco** (`bcc_address`) e **Responder para** (`reply_to`) recebem endereços formatados como os dos destinatários e aceitam variáveis do projeto e do fluxo de trabalho. Os destinatários em Cc e Cco recebem a mesma mensagem, e as respostas vão para o endereço de Responder para. Eles se aplicam a corpos de texto simples e de modelo Jinja. Defina-os em **Mais opções de e-mail**, na guia **Mensagem**.

### Um e-mail para cada linha

Em **Mais opções de e-mail**, defina **Enviar** (`request_source`) como **Um e-mail por linha de uma tabela** (`table`) e escolha uma **Tabela de direcionadores** (`driver_table`) para enviar um e-mail para cada linha de uma tabela, em vez de um único e-mail. **Máximo de linhas a enviar** (`row_limit`) limita as linhas usadas e tem padrão de 10.000. O direcionador deve ser uma tabela, não uma visão.

Use `{{row.column}}` nos endereços, no assunto, na mensagem e no caminho do anexo para preencher o valor de cada linha. Uma coluna que a tabela de direcionadores não tenha faz a etapa falhar. Uma linha sem endereço de destinatário não envia nada para essa linha, e a etapa termina com um aviso que a identifica.

Um caminho de anexo preenchido a partir de uma linha (`{{row.column}}`) deve ser um único arquivo existente, nunca uma pasta, para que uma linha cujo caminho saiu errado não envie arquivos de outra pessoa. Uma linha cujo valor para esse caminho esteja vazio, cujo caminho saia da pasta com `..` ou cujo arquivo não exista é enviada sem o anexo, com um aviso que identifica a linha. O envio por linha exige um corpo simples e não está disponível com um corpo de modelo Jinja.

### Mensagem


Especifique o **Assunto** e o **Corpo** como desejar.



Observação: as variáveis do projeto e as variáveis do fluxo de trabalho estão disponíveis para uso nesta transformação, tanto na linha de assunto quanto no corpo da mensagem.



Além disso, é permitido usar código HTML padrão no corpo para personalizar ainda mais a aparência das mensagens de e-mail.


### Anexos


Anexar arquivos a e-mails é muito simples. Selecione um arquivo ou uma pasta do Document para anexar. Se uma pasta for selecionada, o conteúdo da pasta será anexado como arquivos individuais. A substituição de variáveis funciona com os caminhos, para dar mais controle sobre os anexos ao enviar e-mails personalizados.



Para anexar vários documentos, marque **Adicionar anexo ao e-mail** e liste-os em **Mais anexos** (`attachments`), em **Mais opções de e-mail**, cada um com um **ID da conta** e um **Caminho do documento**; eles são enviados junto com o anexo que você selecionar, e um caminho pode usar variáveis e tokens de linha da mesma forma.

### Prioridade e texto simples

Em **Mais opções de e-mail**, **Prioridade** (`priority`) marca a mensagem como **Baixa**, **Normal** ou **Alta** (`low`, `normal`, `high`), e **Enviar como** (`content_type`) definido como **Texto simples** (`text`) envia o corpo como texto simples em vez de **HTML** (`html`, o padrão).

### Corpo (modelo Jinja)


O corpo da etapa é escrito como um **modelo Jinja** renderizado sobre um ou mais **frames**, produzindo um e-mail HTML rico. Cada frame é uma seleção nomeada de uma única tabela: um Nome do frame, uma tabela do fluxo de trabalho e, opcionalmente, seleção de colunas, um filtro where e agregação (sem junções). O editor abre diretamente neste modelo, com a lista de frames, o corpo do modelo, uma pré-visualização ao vivo e um botão **Enviar teste para mim**, sem alternância entre texto simples e modelo. Um botão **Embelezar** e uma paleta de inserção (`render_table(...)` para um frame, `{{ cloud }}`, um laço for e os filtros de moeda/milhares/porcentagem/data) ajudam a dar forma ao modelo.

Referencie cada frame no modelo como `frames['<Frame Name>'].rows` e `frames['<Frame Name>'].columns`; um modelo de um único frame pode usar `rows` / `columns` de nível superior, que são vinculados ao primeiro frame. O modelo é um mecanismo de renderização separado e isolado (sandbox): apenas `cloud` é resolvido como um valor do espaço de trabalho, e os tokens legados `{project}` / `{model}` / `{date}` não são resolvidos dentro dele. As etapas criadas antes da criação com Jinja abrem com o corpo antigo convertido automaticamente; um corpo que não pode ser convertido com segurança permanece em uma alternativa de texto simples e continua enviando com a substituição legada de `{token}`. Consulte [Enviar notificações por e-mail em HTML com modelos](/pt-br/guides/workflows/notify-email-templates/) para ver as variáveis de modelo disponíveis, o auxiliar `render_table`, as tags e os atributos HTML que sobrevivem ao sanitizador de e-mail e como os corpos existentes são migrados.



## Exemplos


Neste exemplo, todas as variáveis do sistema são usadas. Além disso, um pequeno trecho de HTML é usado para formatar a primeira linha do corpo. A execução desta transformação envia o seguinte e-mail:


* PARA: [info@tartansolutions.com](mailto:info%40tartansolutions.com)
* DE: [info@tartansolutions.com](mailto:info%40tartansolutions.com) (lembre-se de que todas as mensagens vêm deste endereço)
* Assunto: DEMO – Workflow Analyze Demo Running
