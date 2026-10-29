---
title: Adicionar conta MinIO
description: Adicione uma conta de armazenamento MinIO ao PlaidCloud para importar e exportar ficheiros de dados através de armazenamento de objetos autoalojado e compatível com S3.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-minio-account.md
---

## Configuração do MinIO

Estes passos têm de ser concluídos na consola MinIO ou através da CLI `mc`.

1. Inicie sessão na consola MinIO (por exemplo, `https://your-minio-host:9001`)
2. Aceda a **Buckets** e crie um bucket, caso ainda não exista nenhum. Anote o nome do bucket.
3. Aceda a **Identity > Users** (ou **Access Keys**)
4. Crie um novo utilizador ou conta de serviço com acesso de leitura/escrita ao bucket de destino
5. Copie a **Access Key** e a **Secret Key** geradas para o utilizador. Guarde ambas para a configuração do PlaidCloud Document abaixo.
6. Anote o URL do ponto final do MinIO (por exemplo, `https://play.min.io` ou `https://minio.yourcompany.com`)

Já deverá ter tudo o que é necessário para adicionar a sua conta MinIO ao PlaidCloud Document.


## Configuração do PlaidCloud Document

1. Inicie sessão no PlaidCloud
2. Selecione a área de trabalho onde ficará a nova conta de documentos
3. Aceda a `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `MinIO` como Tipo de serviço
6. Preencha um nome e uma descrição
7. Introduza o **Caminho inicial** como o URL do ponto final do MinIO seguido do nome do bucket e de um prefixo opcional: `https://minio.yourcompany.com/my-bucket/optional/prefix`
8. Introduza a **Região** se a sua implementação do MinIO utilizar regiões; caso contrário, deixe em branco
9. Selecione um **Modelo de segurança** adequado ao seu caso de utilização. Em caso de dúvida, deixe `Private`.
10. Cole a **Access Key** no campo ID da chave de acesso, em Credenciais de autenticação
11. Cole a **Secret Key** no campo Chave de acesso secreta, em Credenciais de autenticação
12. Selecione o botão Guardar e a sua nova conta de documentos fica ativa
