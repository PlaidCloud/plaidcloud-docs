---
title: Adicionar conta do DigitalOcean Spaces
description: Adicione uma conta de armazenamento do DigitalOcean Spaces ao PlaidCloud para importar e exportar arquivos de dados usando o armazenamento de objetos compatível com S3 da DigitalOcean.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-digitalocean-spaces-account.md
---

## Configuração do DigitalOcean Spaces

Estas etapas precisam ser concluídas no painel de controle da DigitalOcean.

1. Entre no [painel de controle da DigitalOcean](https://cloud.digitalocean.com)
2. Navegue até **Spaces Object Storage** na barra lateral esquerda
3. Crie um Space caso ainda não exista um. Anote o nome do Space e a região (por exemplo, `nyc3`).
4. Navegue até **API > Spaces Keys** (na seção Tokens)
5. Selecione **Generate New Key**
6. Dê um nome à chave
7. Copie a **Key** (chave de acesso) e o **Secret**. Salve os dois para a configuração do PlaidCloud Document abaixo. O segredo é exibido apenas uma vez.
8. Anote a URL do endpoint da região do seu Space. Ela segue o padrão `https://{region}.digitaloceanspaces.com` (por exemplo, `https://nyc3.digitaloceanspaces.com`)

Agora você deve ter tudo o que precisa para adicionar sua conta do DigitalOcean Spaces ao PlaidCloud Document.


## Configuração do PlaidCloud Document

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Vá para `Document > Manage Accounts`
4. Clique no botão `+ New Account`
5. Selecione `DigitalOcean Spaces` como o Tipo de serviço
6. Preencha um nome e uma descrição
7. Informe o **Caminho inicial** como a URL do endpoint seguida do nome do Space: `https://nyc3.digitaloceanspaces.com/my-space`
8. Informe a **Região** (por exemplo, `nyc3`, `sfo3`, `ams3`)
9. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Se estiver em dúvida, deixe como `Private`.
10. Cole a **Key** no campo ID da chave de acesso, em Credenciais de autenticação
11. Cole o **Secret** no campo Chave de acesso secreta, em Credenciais de autenticação
12. Clique no botão Salvar e sua nova conta de documentos estará ativa
