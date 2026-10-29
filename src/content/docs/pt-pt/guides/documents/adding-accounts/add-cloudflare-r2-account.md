---
title: Adicionar uma conta Cloudflare R2
description: Adicione uma conta de armazenamento Cloudflare R2 ao PlaidCloud para importar e exportar ficheiros de dados através do armazenamento de objetos da Cloudflare, sem custos de saída de dados.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-cloudflare-r2-account.md
---

## Configuração do Cloudflare R2

Estes passos têm de ser concluídos no painel da Cloudflare.

1. Inicie sessão no [painel da Cloudflare](https://dash.cloudflare.com)
2. Selecione a sua conta e, depois, navegue até **R2 Object Storage** na barra lateral esquerda
3. Crie um bucket, se ainda não existir nenhum. Anote o nome do bucket.
4. Navegue até **R2 Object Storage > Manage R2 API Tokens**
5. Selecione **Create API Token**
6. Dê um nome ao token, selecione o(s) bucket(s) a que deve ter acesso e escolha as permissões **Object Read & Write**
7. Selecione **Create API Token**
8. Copie o **Access Key ID** e o **Secret Access Key**. Guarde ambos para a configuração do Document do PlaidCloud abaixo. O segredo só é apresentado uma vez.
9. Anote o **S3 API endpoint** da sua conta. Segue o padrão `https://{account_id}.r2.cloudflarestorage.com` e é apresentado na página de descrição geral do R2.

Neste momento, deverá ter tudo o que precisa para adicionar a sua conta Cloudflare R2 ao Document do PlaidCloud.


## Configuração do Document do PlaidCloud

1. Inicie sessão no PlaidCloud
2. Selecione a área de trabalho em que a nova conta de documentos vai residir
3. Aceda a `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `Cloudflare R2` como Tipo de serviço
6. Preencha um nome e uma descrição
7. Introduza o **Caminho inicial** como o seu endpoint R2 seguido do nome do bucket: `https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. O campo **Região** pode ser definido como `auto` ou deixado em branco — o R2 seleciona automaticamente a região mais próxima
9. Selecione um **Modelo de segurança** adequado ao seu caso de utilização. Se tiver dúvidas, deixe `Private`.
10. Cole o **Access Key ID** no campo ID da chave de acesso, em Credenciais de autenticação
11. Cole o **Secret Access Key** no campo Chave de acesso secreta, em Credenciais de autenticação
12. Selecione o botão Guardar e a sua nova conta de documentos fica ativa
