---
title: Adicionar uma conta Google Cloud Storage
description: Adicione uma conta Google Cloud Storage ao PlaidCloud para importar e exportar ficheiros de dados através do armazenamento de objetos na nuvem da Google.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-cloud-storage-account.md
---

## Configuração do Google Cloud


Estes passos têm de ser concluídos na Google Cloud Platform


1. Inicie sessão ou crie uma conta Google Cloud Platform
2. Selecione ou crie um projeto em que a conta Google Cloud Storage vai residir
3. Aceda a `Cloud Storage > Browser` na consola da Google Cloud Platform
4. Crie um bucket predefinido ou de teste
5. Ir para `IAM & Admin > Service Accounts` na consola da Google Cloud Platform
6. Selecione o botão `+ Create Service Account`
7. Preencha as informações da conta de serviço e crie a conta
8. Encontre a conta de serviço que acabou de criar na lista de contas de serviço e selecione `Manage Keys` no menu de contexto à direita
9. No menu `Add Key`, selecione `Create a Key`
10. Quando lhe for pedido, selecione o formato JSON para a chave. Isto vai gerar a chave e transferi-la automaticamente para o seu ambiente de trabalho. Não será possível obter esta chave novamente, por isso guarde-a bem. Se precisar de voltar a gerar uma chave, volte simplesmente ao passo 8 acima.
11. Aceda a `IAM & Admin > IAM` na consola da Google Cloud Platform
12. Encontre a conta de serviço que acabou de criar e clique no ícone de edição de permissões
13. Adicione os direitos `Storage Admin` e `Storage Transfer Admin` à conta de serviço e guarde. Tenha em conta que é possível atribuir direitos menos permissivos, mas isso afetará a funcionalidade disponível através do Document.

Neste momento, deverá ter tudo o que precisa para adicionar a sua conta GCS ao Document do PlaidCloud.



## Configuração do Document do PlaidCloud

1. Inicie sessão no PlaidCloud
2. Selecione a área de trabalho em que a nova conta de documentos vai residir
3. Aceda a `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `Google Cloud Storage` como Tipo de serviço
6. Preencha um nome e uma descrição
7. Introduza o nome do bucket e um prefixo de caminho opcional no campo **Caminho inicial** (p. ex. `my-bucket` ou `my-bucket/data`). O primeiro segmento do caminho é o nome do bucket.
8. Selecione um **Modelo de segurança** adequado ao seu caso de utilização. Se tiver dúvidas, deixe `Private`.
9. Abra o ficheiro de chave JSON da conta de serviço que transferiu no passo 10 acima e copie todo o conteúdo
10. Cole o conteúdo no campo **Chave JSON do utilizador do sistema**, em Credenciais de autenticação
11. Selecione o botão Guardar e a sua nova conta de documentos fica ativa

É necessária uma chave de conta de serviço válida. Guardar a conta sem uma, ou com algo que não seja uma chave de conta de serviço da Google, é recusado com a mensagem «GCS document accounts require a valid service-account key.» Uma conta existente guardada sem uma chave válida deixa de funcionar até colar uma no campo **Chave JSON do utilizador do sistema**.
