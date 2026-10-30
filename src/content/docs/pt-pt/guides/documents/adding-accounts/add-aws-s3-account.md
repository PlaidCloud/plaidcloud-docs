---
title: Adicionar uma conta AWS S3
description: Adicione uma conta de armazenamento AWS S3 ao PlaidCloud para importar e exportar ficheiros de dados através do armazenamento de objetos na nuvem da Amazon.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-aws-s3-account.md
---

## Configuração do AWS S3

Estes passos têm de ser concluídos na consola da AWS.

1. Inicie sessão ou crie uma conta Amazon Web Services (AWS)
2. Aceda a `All services > Storage > S3` na consola
3. Crie um bucket predefinido ou de teste. Anote o nome do bucket e a região (p. ex. `us-east-1`).
4. Aceda a `All Services > Security Identity & Compliance > IAM > Users` na consola
5. Selecione o botão `Create User`
6. Quando lhe for pedido, introduza um nome de utilizador e selecione apenas `Access Key - Programmatic access`. Selecione o botão `Next: Permissions`.
7. Selecione a caixa de opção `Attach existing policies directly`
8. Na caixa de pesquisa do filtro, escreva `s3`. Quando a lista ficar reduzida aos itens relacionados com S3, selecione `AmazonS3FullAccess` marcando a caixa à esquerda. Selecione o botão `Next: Tags`.
9. Ignore este passo selecionando o botão `Next: Review`
10. Reveja as definições do utilizador e selecione `Create user`
11. Guarde as chaves geradas para o utilizador, transferindo o CSV ou copiando e colando as chaves num local para utilização posterior. Não será possível obter esta chave novamente, por isso guarde-a bem. Se precisar de voltar a gerar uma chave, volte simplesmente ao passo 5 acima.

Neste momento, deverá ter tudo o que precisa para adicionar a sua conta S3 ao Document do PlaidCloud.


## Configuração do Document do PlaidCloud

1. Inicie sessão no PlaidCloud
2. Selecione a área de trabalho em que a nova conta de documentos vai residir
3. Aceda a `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `Amazon S3` como Tipo de serviço
6. Preencha um nome e uma descrição
7. Introduza o nome do bucket e um prefixo de caminho opcional no campo **Caminho inicial** (p. ex. `my-bucket` ou `my-bucket/data`). O primeiro segmento do caminho é o nome do bucket.
8. Selecione um **Modelo de segurança** adequado ao seu caso de utilização. Se tiver dúvidas, deixe `Private`.
9. Cole a **Access Key** criada no passo 11 acima no campo ID da chave de acesso, em Credenciais de autenticação
10. Cole a **Secret Key** criada no passo 11 acima no campo Chave de acesso secreta, em Credenciais de autenticação
11. Introduza a **Região** do seu bucket (p. ex. `us-east-1`, `eu-west-1`). Se ficar em branco, a predefinição é `us-east-2`.
12. Selecione o botão Guardar e a sua nova conta de documentos fica ativa
