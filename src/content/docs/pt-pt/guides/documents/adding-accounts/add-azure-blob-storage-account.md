---
title: Adicionar uma conta Azure Blob Storage
description: Adicione uma conta Azure Blob Storage ao PlaidCloud para importar e exportar ficheiros de dados através do armazenamento de objetos na nuvem da Microsoft Azure.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-blob-storage-account.md
---

## Configuração do Azure Blob Storage

Estes passos têm de ser concluídos no portal do Azure.

1. Inicie sessão no [portal do Azure](https://portal.azure.com)
2. Navegue até **Storage accounts** e selecione ou crie uma conta de armazenamento
3. Na barra lateral esquerda, em **Security + networking**, selecione **Access keys**
4. Copie o **Storage account name** e um dos valores de **Key**. Guarde ambos para a configuração do Document do PlaidCloud abaixo.
5. Navegue até **Containers**, em **Data storage**, e crie um contentor, se ainda não existir nenhum. Anote o nome do contentor.

Neste momento, deverá ter tudo o que precisa para adicionar a sua conta Azure Blob Storage ao Document do PlaidCloud.


## Configuração do Document do PlaidCloud

1. Inicie sessão no PlaidCloud
2. Selecione a área de trabalho em que a nova conta de documentos vai residir
3. Aceda a `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `Azure Blob Storage` como Tipo de serviço
6. Preencha um nome e uma descrição
7. Introduza o nome do contentor e um prefixo de caminho opcional no campo **Caminho inicial** (p. ex. `my-container/data`). O primeiro segmento do caminho é o nome do contentor.
8. Selecione um **Modelo de segurança** adequado ao seu caso de utilização. Se tiver dúvidas, deixe `Private`.
9. Cole o **Storage account name** no campo Nome da conta, em Credenciais de autenticação
10. Cole a **Key** no campo Chave da conta, em Credenciais de autenticação
11. Selecione o botão Guardar e a sua nova conta de documentos fica ativa
