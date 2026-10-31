---
title: Adicionar conta do Azure Data Lake Gen2
description: Adicione uma conta do Azure Data Lake Storage Gen2 ao PlaidCloud para importar e exportar arquivos de dados usando armazenamento com namespace hierárquico no Azure.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-data-lake-gen2-account.md
---

## Configuração do Azure Data Lake Gen2

O Azure Data Lake Storage Gen2 é construído sobre o Azure Blob Storage com um namespace hierárquico habilitado. Estas etapas precisam ser concluídas no portal do Azure.

1. Entre no [portal do Azure](https://portal.azure.com)
2. Navegue até **Storage accounts** e selecione ou crie uma conta de armazenamento com **Hierarchical namespace** habilitado
3. Na barra lateral esquerda, em **Security + networking**, selecione **Access keys**
4. Copie o **Storage account name** e um dos valores de **Key**. Salve os dois para a configuração do PlaidCloud Document abaixo.
5. Navegue até **Containers**, em **Data storage**, e crie um sistema de arquivos (contêiner) caso ainda não exista um. Anote o nome do sistema de arquivos.

Agora você deve ter tudo o que precisa para adicionar sua conta do Azure Data Lake Gen2 ao PlaidCloud Document.


## Configuração do PlaidCloud Document

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Vá para `Document > Manage Accounts`
4. Clique no botão `+ New Account`
5. Selecione `Azure Data Lake Gen2` como o Tipo de serviço
6. Preencha um nome e uma descrição
7. Informe o nome do sistema de arquivos e um prefixo de caminho opcional no campo **Caminho inicial** (por exemplo, `my-filesystem/data`). O primeiro segmento do caminho é o nome do sistema de arquivos.
8. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Se estiver em dúvida, deixe como `Private`.
9. Cole o **Storage account name** no campo Nome da conta, em Credenciais de autenticação
10. Cole a **Key** no campo Chave da conta, em Credenciais de autenticação
11. Clique no botão Salvar e sua nova conta de documentos estará ativa
