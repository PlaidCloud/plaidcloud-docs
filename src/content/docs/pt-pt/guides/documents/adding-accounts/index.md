---
title: Adicionar novas contas de documentos
description: Ligue o armazenamento de documentos na nuvem e local ao PlaidCloud — S3, GCS, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV e muito mais.
sidebar:
  label: Adicionar novas contas de documentos
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/index.md
---

Ligue o armazenamento de documentos na nuvem e local ao PlaidCloud — S3, Google Cloud Storage, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV e muito mais. Cada fornecedor tem as suas próprias credenciais e o seu próprio fluxo de ligação.

A opção mais rápida é um **Bucket gerido pelo PlaidCloud**, em que o PlaidCloud configura e gere o armazenamento por si — só tem de escolher um nome, sem mais nada para configurar. Para ligar armazenamento que já possui, escolha o fornecedor correspondente abaixo.

## Os segredos guardados são apenas de escrita

O segredo de uma conta, o campo com a etiqueta **Chave privada / Palavra-passe** ou, consoante o tipo de conta, **Chave de acesso secreta**, **Chave da conta**, **Segredo do cliente**, **Token de acesso**, **Palavra-passe**, **Chave JSON do utilizador do sistema** ou **JSON de credenciais OAuth2**, é apenas de escrita, tal como a **chave privada RSA** de uma conta SFTP. Depois de guardados, nunca voltam a ser apresentados, nem no formulário, nem na API, nem a um assistente de IA. Quando edita uma conta, o campo fica vazio com a sugestão *Cole o valor; deixe em branco na edição para manter o valor guardado.* Deixe-o em branco para manter o segredo guardado ou cole um novo para o substituir.

Alterar o destino de ligação de uma conta exige que o respetivo segredo seja introduzido novamente. Se alterar a primeira parte do **Caminho inicial** (no armazenamento na nuvem, o bucket ou contentor), o **Anfitrião ou endereço IP** ou a **Porta da ligação SSH** de uma conta SFTP, ou o **ID do inquilino do OneDrive** de uma conta OneDrive, cole também o segredo, caso contrário a gravação é recusada com a mensagem *Changing where the account connects needs its secret entered again*. Isto impede que alguém que possa editar uma conta, mas nunca tenha visto o respetivo segredo, o envie para um servidor à sua escolha.

Um assistente de IA ligado através do conector MCP do PlaidCloud também pode criar e atualizar contas, com um tipo de armazenamento, credenciais e caminho inicial. As credenciais são apenas de escrita e ficam ocultas quando a conta é lida novamente. Para um exemplo prático, consulte [Adicionar conta OneDrive / SharePoint](/pt-pt/guides/documents/adding-accounts/add-onedrive-account/#criar-a-conta-com-um-assistente-de-ia).
