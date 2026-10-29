---
title: Adicionar uma conta Linode Object Storage
description: Adicione uma conta Linode (Akamai) Object Storage ao PlaidCloud para importar e exportar ficheiros de dados através do armazenamento na nuvem compatível com S3 da Linode.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-linode-object-storage-account.md
---

## Configuração do Linode Object Storage

Estes passos têm de ser concluídos no Linode Cloud Manager.

1. Inicie sessão no [Linode Cloud Manager](https://cloud.linode.com)
2. Navegue até **Object Storage** na barra lateral esquerda
3. Crie um bucket, se ainda não existir nenhum. Anote o nome do bucket (chamado **label**) e a região (p. ex. `us-east-1`).
4. Navegue até **Object Storage > Access Keys**
5. Selecione **Create Access Key**
6. Atribua uma etiqueta à chave e selecione o(s) bucket(s) a que deve ter acesso, com permissões de leitura/escrita
7. Selecione **Create Access Key**
8. Copie a **Access Key** e a **Secret Key**. Guarde ambas para a configuração do Document do PlaidCloud abaixo. O segredo só é apresentado uma vez.
9. Anote o URL do endpoint da região do seu bucket. Segue o padrão `https://{region}.linodeobjects.com` (p. ex. `https://us-east-1.linodeobjects.com`)

Neste momento, deverá ter tudo o que precisa para adicionar a sua conta Linode Object Storage ao Document do PlaidCloud.


## Configuração do Document do PlaidCloud

1. Inicie sessão no PlaidCloud
2. Selecione a área de trabalho em que a nova conta de documentos vai residir
3. Aceda a `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `Linode Object Storage` como Tipo de serviço
6. Preencha um nome e uma descrição
7. Introduza o **Caminho inicial** como o URL do endpoint seguido do nome do bucket: `https://us-east-1.linodeobjects.com/my-bucket`
8. Introduza a **Região** (p. ex. `us-east-1`)
9. Selecione um **Modelo de segurança** adequado ao seu caso de utilização. Se tiver dúvidas, deixe `Private`.
10. Cole a **Access Key** no campo ID da chave de acesso, em Credenciais de autenticação
11. Cole a **Secret Key** no campo Chave de acesso secreta, em Credenciais de autenticação
12. Selecione o botão Guardar e a sua nova conta de documentos fica ativa
