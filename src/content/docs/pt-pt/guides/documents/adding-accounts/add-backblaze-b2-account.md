---
title: Adicionar uma conta Backblaze B2
description: Adicione uma conta de armazenamento Backblaze B2 ao PlaidCloud para importar e exportar ficheiros de dados através de armazenamento de objetos na nuvem económico.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Configuração do Backblaze B2

Estes passos têm de ser concluídos na consola do Backblaze B2.

1. Inicie sessão na [consola do Backblaze B2](https://secure.backblaze.com/b2_buckets.htm)
2. Navegue até **Buckets** e crie um bucket, se ainda não existir nenhum. Anote o nome do bucket.
3. Navegue até **App Keys**
4. Selecione **Add a New Application Key**
5. Dê um nome à chave, selecione o bucket a que deve ter acesso e escolha as permissões adequadas (leitura e escrita)
6. Selecione **Create New Key**
7. Copie o **keyID** (a sua Access Key) e a **applicationKey** (a sua Secret Key). Guarde ambos para a configuração do Document do PlaidCloud abaixo. A chave de aplicação só é apresentada uma vez.
8. Anote o **S3 Endpoint** da região do seu bucket. Segue o padrão `https://s3.{region}.backblazeb2.com` (p. ex. `https://s3.us-west-004.backblazeb2.com`). Pode encontrá-lo na página de detalhes do bucket.

Neste momento, deverá ter tudo o que precisa para adicionar a sua conta Backblaze B2 ao Document do PlaidCloud.


## Configuração do Document do PlaidCloud

1. Inicie sessão no PlaidCloud
2. Selecione a área de trabalho em que a nova conta de documentos vai residir
3. Aceda a `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `Backblaze B2` como Tipo de serviço
6. Preencha um nome e uma descrição
7. Introduza o **Caminho inicial** como o seu endpoint compatível com S3 seguido do nome do bucket: `https://s3.us-west-004.backblazeb2.com/my-bucket`
8. Introduza a **Região** do seu bucket (p. ex. `us-west-004`)
9. Selecione um **Modelo de segurança** adequado ao seu caso de utilização. Se tiver dúvidas, deixe `Private`.
10. Cole o **keyID** no campo ID da chave de acesso, em Credenciais de autenticação
11. Cole a **applicationKey** no campo Chave de acesso secreta, em Credenciais de autenticação
12. Selecione o botão Guardar e a sua nova conta de documentos fica ativa
