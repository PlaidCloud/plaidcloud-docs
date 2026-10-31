---
title: Adicionar conta do AWS S3
description: Adicione uma conta de armazenamento do AWS S3 ao PlaidCloud para importar e exportar arquivos de dados usando o armazenamento de objetos em nuvem da Amazon.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-aws-s3-account.md
---

## Configuração do AWS S3

Estas etapas precisam ser concluídas no console da AWS.

1. Entre ou crie uma conta da Amazon Web Services (AWS)
2. Vá para `All services > Storage > S3` no console
3. Crie um bucket padrão ou de teste. Anote o nome do bucket e a região (por exemplo, `us-east-1`).
4. Vá para `All Services > Security Identity & Compliance > IAM > Users` no console
5. Clique no botão `Create User`
6. Quando solicitado, informe um nome de usuário e selecione apenas `Access Key - Programmatic access`. Clique no botão `Next: Permissions`.
7. Marque a opção chamada `Attach existing policies directly`
8. Na caixa de pesquisa de filtro, digite `s3`. Quando a lista for filtrada para itens relacionados ao S3, selecione `AmazonS3FullAccess` marcando a caixa à esquerda. Clique no botão `Next: Tags`.
9. Ignore esta etapa clicando no botão `Next: Review`
10. Revise as configurações do usuário e clique em `Create user`
11. Capture as chaves geradas para o usuário baixando o CSV ou copiando e colando as chaves em algum lugar para uso posterior. Não será possível recuperar essa chave novamente, então guarde-a. Se precisar gerar uma chave novamente, basta voltar à etapa 5 acima.

Agora você deve ter tudo o que precisa para adicionar sua conta do S3 ao PlaidCloud Document.


## Configuração do PlaidCloud Document

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Vá para `Document > Manage Accounts`
4. Clique no botão `+ New Account`
5. Selecione `Amazon S3` como o Tipo de serviço
6. Preencha um nome e uma descrição
7. Informe o nome do bucket e um prefixo de caminho opcional no campo **Caminho inicial** (por exemplo, `my-bucket` ou `my-bucket/data`). O primeiro segmento do caminho é o nome do bucket.
8. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Se estiver em dúvida, deixe como `Private`.
9. Cole a **chave de acesso** criada na etapa 11 acima no campo ID da chave de acesso, em Credenciais de autenticação
10. Cole a **chave secreta** criada na etapa 11 acima no campo Chave de acesso secreta, em Credenciais de autenticação
11. Informe a **Região** do seu bucket (por exemplo, `us-east-1`, `eu-west-1`). Se for deixada em branco, o padrão é `us-east-2`.
12. Clique no botão Salvar e sua nova conta de documentos estará ativa
