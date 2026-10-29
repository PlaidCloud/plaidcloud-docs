---
title: Adicionar conta do Azure Blob Storage
description: Adicione uma conta do Azure Blob Storage ao PlaidCloud para importar e exportar arquivos de dados usando o armazenamento de objetos em nuvem do Microsoft Azure.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-blob-storage-account.md
---

## Configuração do Azure Blob Storage

Estas etapas precisam ser concluídas no portal do Azure.

1. Entre no [portal do Azure](https://portal.azure.com)
2. Navegue até **Storage accounts** e selecione ou crie uma conta de armazenamento
3. Na barra lateral esquerda, em **Security + networking**, selecione **Access keys**
4. Copie o **Storage account name** e um dos valores de **Key**. Salve os dois para a configuração do PlaidCloud Document abaixo.
5. Navegue até **Containers**, em **Data storage**, e crie um contêiner caso ainda não exista um. Anote o nome do contêiner.

Agora você deve ter tudo o que precisa para adicionar sua conta do Azure Blob Storage ao PlaidCloud Document.


## Configuração do PlaidCloud Document

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Vá para `Document > Manage Accounts`
4. Clique no botão `+ New Account`
5. Selecione `Azure Blob Storage` como o Tipo de serviço
6. Preencha um nome e uma descrição
7. Informe o nome do contêiner e um prefixo de caminho opcional no campo **Caminho inicial** (por exemplo, `my-container/data`). O primeiro segmento do caminho é o nome do contêiner.
8. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Se estiver em dúvida, deixe como `Private`.
9. Cole o **Storage account name** no campo Nome da conta, em Credenciais de autenticação
10. Cole a **Key** no campo Chave da conta, em Credenciais de autenticação
11. Clique no botão Salvar e sua nova conta de documentos estará ativa
