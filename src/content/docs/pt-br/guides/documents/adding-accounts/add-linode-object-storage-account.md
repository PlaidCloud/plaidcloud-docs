---
title: Adicionar conta do Linode Object Storage
description: Adicione uma conta do Linode Object Storage (Akamai) ao PlaidCloud para importar e exportar arquivos de dados usando o armazenamento em nuvem compatível com S3 da Linode.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-linode-object-storage-account.md
---

## Configuração do Linode Object Storage

Estas etapas precisam ser concluídas no Linode Cloud Manager.

1. Entre no [Linode Cloud Manager](https://cloud.linode.com)
2. Navegue até **Object Storage** na barra lateral esquerda
3. Crie um bucket caso ainda não exista um. Anote o nome do bucket (chamado de **label**) e a região (por exemplo, `us-east-1`).
4. Navegue até **Object Storage > Access Keys**
5. Selecione **Create Access Key**
6. Dê um rótulo à chave e selecione os buckets aos quais ela deve ter acesso, com permissões de leitura e gravação
7. Selecione **Create Access Key**
8. Copie a **chave de acesso** e a **chave secreta**. Salve as duas para a configuração do PlaidCloud Document abaixo. O segredo é exibido apenas uma vez.
9. Anote a URL do endpoint da região do seu bucket. Ela segue o padrão `https://{region}.linodeobjects.com` (por exemplo, `https://us-east-1.linodeobjects.com`)

Agora você deve ter tudo o que precisa para adicionar sua conta do Linode Object Storage ao PlaidCloud Document.


## Configuração do PlaidCloud Document

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Vá para `Document > Manage Accounts`
4. Clique no botão `+ New Account`
5. Selecione `Linode Object Storage` como o Tipo de serviço
6. Preencha um nome e uma descrição
7. Informe o **Caminho inicial** como a URL do endpoint seguida do nome do bucket: `https://us-east-1.linodeobjects.com/my-bucket`
8. Informe a **Região** (por exemplo, `us-east-1`)
9. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Se estiver em dúvida, deixe como `Private`.
10. Cole a **chave de acesso** no campo ID da chave de acesso, em Credenciais de autenticação
11. Cole a **chave secreta** no campo Chave de acesso secreta, em Credenciais de autenticação
12. Clique no botão Salvar e sua nova conta de documentos estará ativa
