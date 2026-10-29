---
title: Adicionar novas contas de documentos
description: Conecte armazenamento de documentos em nuvem e local ao PlaidCloud, incluindo S3, GCS, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV e outros.
sidebar:
  label: Adicionar novas contas de documentos
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/index.md
---

Conecte armazenamento de documentos em nuvem e local ao PlaidCloud, incluindo S3, Google Cloud Storage, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV e outros. Cada provedor tem suas próprias credenciais e seu próprio fluxo de conexão.

A opção mais rápida é um **Bucket gerenciado pelo PlaidCloud**, em que o PlaidCloud configura e opera o armazenamento para você: você só escolhe um nome, sem mais nada a configurar. Para conectar um armazenamento que você já possui, escolha o provedor correspondente abaixo.

## Segredos salvos são somente de gravação

O segredo de uma conta, o campo rotulado **Chave privada / Senha** ou, dependendo do tipo de conta, **Chave de acesso secreta**, **Chave da conta**, **Segredo do cliente**, **Token de acesso**, **Senha**, **Chave JSON do usuário do sistema** ou **JSON de credenciais OAuth2**, é somente de gravação, assim como a **RSA Private Key** de uma conta SFTP. Depois de salvos, eles nunca são exibidos novamente, nem no formulário, nem na API, nem para um assistente de IA. Ao editar uma conta, o campo fica vazio com a dica *Paste the value; leave blank on edit to keep the saved one.* Deixe-o em branco para manter o segredo salvo ou cole um novo para substituí-lo.

Alterar o destino de conexão de uma conta exige informar o segredo novamente. Se você alterar a primeira parte do **Caminho inicial** (no armazenamento em nuvem, o bucket ou contêiner), o **Host ou endereço IP** ou a **Porta da conexão SSH** de uma conta SFTP, ou o **ID do tenant do OneDrive** de uma conta OneDrive, cole também o segredo; caso contrário, o salvamento é recusado com a mensagem *Changing where the account connects needs its secret entered again*. Isso impede que alguém que possa editar uma conta, mas nunca viu o segredo, envie esse segredo a um servidor de sua escolha.

Um assistente de IA conectado por meio do conector MCP do PlaidCloud também pode criar e atualizar contas, com um tipo de armazenamento, credenciais e caminho inicial. As credenciais são somente de gravação e ficam ocultas quando a conta é lida de volta. Para um exemplo prático, consulte [Adicionar conta OneDrive / SharePoint](/pt-br/guides/documents/adding-accounts/add-onedrive-account/#criar-a-conta-com-um-assistente-de-ia).
