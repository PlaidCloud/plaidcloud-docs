---
title: Adicionar conta do Google Drive
description: Adicione uma conta de armazenamento do Google Drive ao PlaidCloud para importar e exportar arquivos de dados usando o armazenamento em nuvem do Google Drive.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Configuração do Google Drive

Estas etapas precisam ser concluídas no Google Cloud Console para criar uma conta de serviço que o PlaidCloud possa usar para acessar o Google Drive.

### Crie um projeto do Google Cloud

1. Entre no [Google Cloud Console](https://console.cloud.google.com)
2. Crie um novo projeto ou selecione um existente

### Ative a API do Google Drive

1. Navegue até **APIs & Services > Library**
2. Pesquise por **Google Drive API**
3. Selecione-a e clique em **Ativar**

### Crie uma conta de serviço

1. Navegue até **APIs & Services > Credentials**
2. Selecione **+ Create Credentials > Service account**
3. Informe um nome para a conta de serviço (por exemplo, `plaidcloud-drive`)
4. Selecione **Create and Continue**
5. Se quiser, conceda funções (por exemplo, **Visualizador** para somente leitura ou **Editor** para leitura e gravação). Selecione **Continuar**.
6. Selecione **Concluído**

### Gere uma chave da conta de serviço

1. Na lista **Service Accounts**, selecione a conta de serviço que você acabou de criar
2. Navegue até a guia **Keys**
3. Selecione **Adicionar chave > Criar novo**
4. Escolha o formato **JSON** e selecione **Criar**
5. Um arquivo de chave JSON será baixado. Guarde esse arquivo com segurança — ele contém as credenciais que o PlaidCloud usará.

### Compartilhe o conteúdo do Drive com a conta de serviço

1. Copie o endereço de e-mail da conta de serviço (por exemplo, `plaidcloud-drive@your-project.iam.gserviceaccount.com`)
2. No Google Drive, compartilhe com esse endereço de e-mail as pastas que você quer que o PlaidCloud acesse, concedendo acesso de **Editor**

Agora você deve ter tudo o que precisa para adicionar sua conta do Google Drive ao PlaidCloud Document.


## Configuração do PlaidCloud Document

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Vá para `Document > Manage Accounts`
4. Clique no botão `+ New Account`
5. Selecione `Google Drive` como o Tipo de serviço
6. Preencha um nome e uma descrição
7. Informe o caminho da pasta compartilhada no campo **Caminho inicial** ou deixe-o em branco para acessar todo o conteúdo compartilhado
8. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Se estiver em dúvida, deixe como `Private`.
9. Cole todo o conteúdo do arquivo de chave JSON no campo JSON de credenciais OAuth2, em Credenciais de autenticação
10. Clique no botão Salvar e sua nova conta de documentos estará ativa
