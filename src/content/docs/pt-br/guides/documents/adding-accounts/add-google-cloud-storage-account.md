---
title: Adicionar conta do Google Cloud Storage
description: Adicione uma conta do Google Cloud Storage ao PlaidCloud para importar e exportar arquivos de dados usando o armazenamento de objetos em nuvem do Google.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-cloud-storage-account.md
---

## Configuração do Google Cloud


Estas etapas precisam ser concluídas no Google Cloud Platform


1. Entre ou crie uma conta do Google Cloud Platform
2. Selecione ou crie um projeto em que a conta do Google Cloud Storage ficará
3. Vá para `Cloud Storage > Browser` no console do Google Cloud Platform
4. Crie um bucket padrão ou de teste
5. Vá para `IAM & Admin > Service Accounts` no console do Google Cloud Platform
6. Clique no botão `+ Create Service Account`
7. Preencha as informações da conta de serviço e crie a conta
8. Encontre a conta de serviço que acabou de criar na lista de contas de serviço e selecione `Manage Keys` no menu de contexto à direita
9. No menu `Add Key`, selecione `Create a Key`
10. Quando solicitado, selecione o formato JSON para a chave. Isso gerará a chave e a baixará automaticamente para a sua área de trabalho. Não será possível recuperar essa chave novamente, então guarde-a. Se precisar gerar uma chave novamente, basta voltar à etapa 8 acima.
11. Vá para `IAM & Admin > IAM` no console do Google Cloud Platform
12. Encontre a conta de serviço que você acabou de criar e clique no ícone de edição de permissões
13. Adicione os direitos `Storage Admin` e `Storage Transfer Admin` à conta de serviço e salve. Observe que é possível atribuir direitos menos permissivos, mas isso afetará a funcionalidade disponível no Document.

Agora você deve ter tudo o que precisa para adicionar sua conta do GCS ao PlaidCloud Document.



## Configuração do PlaidCloud Document

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Vá para `Document > Manage Accounts`
4. Clique no botão `+ New Account`
5. Selecione `Google Cloud Storage` como o Tipo de serviço
6. Preencha um nome e uma descrição
7. Informe o nome do bucket e um prefixo de caminho opcional no campo **Caminho inicial** (por exemplo, `my-bucket` ou `my-bucket/data`). O primeiro segmento do caminho é o nome do bucket.
8. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Se estiver em dúvida, deixe como `Private`.
9. Abra o arquivo de chave JSON da conta de serviço que você baixou na etapa 10 acima e copie todo o conteúdo
10. Cole o conteúdo no campo **Chave JSON do usuário do sistema**, em Credenciais de autenticação
11. Clique no botão Salvar e sua nova conta de documentos estará ativa

É necessária uma chave de conta de serviço válida. Salvar a conta sem uma chave, ou com algo que não seja uma chave de conta de serviço do Google, é recusado com "GCS document accounts require a valid service-account key." Uma conta existente salva sem uma chave válida deixa de funcionar até que você cole uma no campo **Chave JSON do usuário do sistema**.
