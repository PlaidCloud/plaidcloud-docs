---
title: Adicionar conta do Backblaze B2
description: Adicione uma conta de armazenamento do Backblaze B2 ao PlaidCloud para importar e exportar arquivos de dados usando armazenamento de objetos em nuvem de baixo custo.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Configuração do Backblaze B2

Estas etapas precisam ser concluídas no console do Backblaze B2.

1. Entre no [console do Backblaze B2](https://secure.backblaze.com/b2_buckets.htm)
2. Navegue até **Buckets** e crie um bucket caso ainda não exista um. Anote o nome do bucket.
3. Navegue até **App Keys**
4. Selecione **Add a New Application Key**
5. Dê um nome à chave, selecione o bucket ao qual ela deve ter acesso e escolha as permissões adequadas (leitura e gravação)
6. Selecione **Create New Key**
7. Copie o **keyID** (que é a sua chave de acesso) e a **applicationKey** (que é a sua chave secreta). Salve os dois para a configuração do PlaidCloud Document abaixo. A application key é exibida apenas uma vez.
8. Anote o **S3 Endpoint** da região do seu bucket. Ele segue o padrão `https://s3.{region}.backblazeb2.com` (por exemplo, `https://s3.us-west-004.backblazeb2.com`). Ele pode ser encontrado na página de detalhes do bucket.

Agora você deve ter tudo o que precisa para adicionar sua conta do Backblaze B2 ao PlaidCloud Document.


## Configuração do PlaidCloud Document

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Vá para `Document > Manage Accounts`
4. Clique no botão `+ New Account`
5. Selecione `Backblaze B2` como o Tipo de serviço
6. Preencha um nome e uma descrição
7. Informe o **Caminho inicial** como o seu endpoint compatível com S3 seguido do nome do bucket: `https://s3.us-west-004.backblazeb2.com/my-bucket`
8. Informe a **Região** do seu bucket (por exemplo, `us-west-004`)
9. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Se estiver em dúvida, deixe como `Private`.
10. Cole o **keyID** no campo ID da chave de acesso, em Credenciais de autenticação
11. Cole a **applicationKey** no campo Chave de acesso secreta, em Credenciais de autenticação
12. Clique no botão Salvar e sua nova conta de documentos estará ativa
