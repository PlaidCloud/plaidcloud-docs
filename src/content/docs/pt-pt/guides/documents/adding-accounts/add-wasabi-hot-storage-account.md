---
title: Adicionar conta Wasabi Hot Storage
description: Adicione uma conta Wasabi Hot Storage ao PlaidCloud para importar e exportar ficheiros de dados através de armazenamento na nuvem económico.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-wasabi-hot-storage-account.md
---

## Configuração do Wasabi Hot Storage


Estes passos têm de ser concluídos na consola do Wasabi Hot Storage


1. Inicie sessão ou crie uma conta Wasabi Hot Storage
2. Aceda a `Buckets` na consola
3. Crie um bucket predefinido ou de teste
4. Aceda a Users na consola
5. Selecione o botão `Create User`
6. Quando lhe for pedido, introduza um nome de utilizador e selecione o tipo de utilizador `Programmatic (create API key)`
7. Ignore a atribuição de grupo. Selecione o botão `Next`
8. Selecione o ícone de mais junto à política `WasabiFullAccess` para a associar ao utilizador. Selecione o botão `Next`.
9. Reveja as definições do utilizador e selecione `Create User`
10. Guarde as chaves geradas para o utilizador, transferindo o CSV ou copiando e colando as chaves num local para utilização posterior. Não será possível obter esta chave novamente, por isso guarde-a em segurança. Se precisar de gerar novamente uma chave, volte ao passo 5 acima.

Já deverá ter tudo o que é necessário para adicionar a sua conta Wasabi ao PlaidCloud Document.



## Configuração do PlaidCloud Document

1. Inicie sessão no PlaidCloud
2. Selecione a área de trabalho onde ficará a nova conta de documentos
3. Aceda a `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `Wasabi Hot Storage` como Tipo de serviço
6. Preencha um nome e uma descrição
7. Introduza o nome do bucket e um prefixo de caminho opcional no campo **Caminho inicial** (por exemplo, `my-bucket` ou `my-bucket/data`). O primeiro segmento do caminho é o nome do bucket.
8. Selecione um **Modelo de segurança** adequado ao seu caso de utilização. Em caso de dúvida, deixe `Private`.
9. Cole a **Access Key** criada no passo 10 acima no campo ID da chave de acesso, em Credenciais de autenticação
10. Cole a **Secret Key** criada no passo 10 acima no campo Chave de acesso secreta, em Credenciais de autenticação
11. Introduza a **Região** se a sua conta Wasabi utilizar uma região específica; caso contrário, deixe em branco
12. Selecione o botão Guardar e a sua nova conta de documentos fica ativa
