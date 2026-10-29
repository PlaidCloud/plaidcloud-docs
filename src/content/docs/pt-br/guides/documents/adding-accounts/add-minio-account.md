---
title: Adicionar conta MinIO
description: Adicione uma conta de armazenamento MinIO ao PlaidCloud para importar e exportar arquivos de dados usando armazenamento de objetos autogerenciado compatível com S3.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-minio-account.md
---

## Configuração do MinIO

Estas etapas devem ser concluídas no MinIO Console ou pela CLI `mc`.

1. Entre no MinIO Console (por exemplo, `https://your-minio-host:9001`)
2. Acesse **Buckets** e crie um bucket, caso ainda não exista. Anote o nome do bucket.
3. Acesse **Identity > Users** (ou **Access Keys**)
4. Crie um novo usuário ou conta de serviço com acesso de leitura e gravação ao bucket de destino
5. Copie a **Access Key** e a **Secret Key** geradas para o usuário. Salve ambas para a configuração do PlaidCloud Document abaixo.
6. Anote a URL do endpoint do MinIO (por exemplo, `https://play.min.io` ou `https://minio.yourcompany.com`)

Agora você tem tudo de que precisa para adicionar sua conta MinIO ao PlaidCloud Document.


## Configuração do PlaidCloud Document

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Acesse `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `MinIO` como **Tipo de serviço**
6. Preencha um nome e uma descrição
7. Informe o **Caminho inicial** como a URL do endpoint do MinIO seguida do nome do bucket e de um prefixo opcional: `https://minio.yourcompany.com/my-bucket/optional/prefix`
8. Informe a **Região** se sua implantação do MinIO usar regiões; caso contrário, deixe em branco
9. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Deixe `Private` se tiver dúvida.
10. Cole a **Access Key** no campo ID da chave de acesso em Credenciais de autenticação
11. Cole a **Secret Key** no campo Chave de acesso secreta em Credenciais de autenticação
12. Selecione o botão Salvar e sua nova conta de documentos estará ativa
