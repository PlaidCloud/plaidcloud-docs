---
title: Adicionar conta do Cloudflare R2
description: Adicione uma conta de armazenamento do Cloudflare R2 ao PlaidCloud para importar e exportar arquivos de dados usando o armazenamento de objetos da Cloudflare, sem taxas de saída de dados.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-cloudflare-r2-account.md
---

## Configuração do Cloudflare R2

Estas etapas precisam ser concluídas no painel da Cloudflare.

1. Entre no [painel da Cloudflare](https://dash.cloudflare.com)
2. Selecione sua conta e, em seguida, navegue até **R2 Object Storage** na barra lateral esquerda
3. Crie um bucket caso ainda não exista um. Anote o nome do bucket.
4. Navegue até **R2 Object Storage > Manage R2 API Tokens**
5. Selecione **Create API Token**
6. Dê um nome ao token, selecione os buckets aos quais ele deve ter acesso e escolha as permissões **Object Read & Write**
7. Selecione **Create API Token**
8. Copie o **ID da chave de acesso** e a **Chave de acesso secreta**. Salve os dois para a configuração do PlaidCloud Document abaixo. O segredo é exibido apenas uma vez.
9. Anote o **S3 API endpoint** da sua conta. Ele segue o padrão `https://{account_id}.r2.cloudflarestorage.com` e é exibido na página de visão geral do R2.

Agora você deve ter tudo o que precisa para adicionar sua conta do Cloudflare R2 ao PlaidCloud Document.


## Configuração do PlaidCloud Document

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Vá para `Document > Manage Accounts`
4. Clique no botão `+ New Account`
5. Selecione `Cloudflare R2` como o Tipo de serviço
6. Preencha um nome e uma descrição
7. Informe o **Caminho inicial** como o seu endpoint do R2 seguido do nome do bucket: `https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. O campo **Região** pode ser definido como `auto` ou deixado em branco — o R2 seleciona automaticamente a região mais próxima
9. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Se estiver em dúvida, deixe como `Private`.
10. Cole o **ID da chave de acesso** no campo ID da chave de acesso, em Credenciais de autenticação
11. Cole a **Chave de acesso secreta** no campo Chave de acesso secreta, em Credenciais de autenticação
12. Clique no botão Salvar e sua nova conta de documentos estará ativa
