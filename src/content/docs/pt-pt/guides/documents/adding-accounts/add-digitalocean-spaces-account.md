---
title: Adicionar uma conta DigitalOcean Spaces
description: Adicione uma conta de armazenamento DigitalOcean Spaces ao PlaidCloud para importar e exportar ficheiros de dados através do armazenamento de objetos compatível com S3 da DigitalOcean.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-digitalocean-spaces-account.md
---

## Configuração do DigitalOcean Spaces

Estes passos têm de ser concluídos no painel de controlo da DigitalOcean.

1. Inicie sessão no [DigitalOcean Control Panel](https://cloud.digitalocean.com)
2. Navegue até **Spaces Object Storage** na barra lateral esquerda
3. Crie um Space, se ainda não existir nenhum. Anote o nome do Space e a região (p. ex. `nyc3`).
4. Navegue até **API > Spaces Keys** (na secção Tokens)
5. Selecione **Generate New Key**
6. Dê um nome à chave
7. Copie a **Key** (Access Key) e o **Secret**. Guarde ambos para a configuração do Document do PlaidCloud abaixo. O segredo só é apresentado uma vez.
8. Anote o URL do endpoint da região do seu Space. Segue o padrão `https://{region}.digitaloceanspaces.com` (p. ex. `https://nyc3.digitaloceanspaces.com`)

Neste momento, deverá ter tudo o que precisa para adicionar a sua conta DigitalOcean Spaces ao Document do PlaidCloud.


## Configuração do Document do PlaidCloud

1. Inicie sessão no PlaidCloud
2. Selecione a área de trabalho em que a nova conta de documentos vai residir
3. Aceda a `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `DigitalOcean Spaces` como Tipo de serviço
6. Preencha um nome e uma descrição
7. Introduza o **Caminho inicial** como o URL do endpoint seguido do nome do Space: `https://nyc3.digitaloceanspaces.com/my-space`
8. Introduza a **Região** (p. ex. `nyc3`, `sfo3`, `ams3`)
9. Selecione um **Modelo de segurança** adequado ao seu caso de utilização. Se tiver dúvidas, deixe `Private`.
10. Cole a **Key** no campo ID da chave de acesso, em Credenciais de autenticação
11. Cole o **Secret** no campo Chave de acesso secreta, em Credenciais de autenticação
12. Selecione o botão Guardar e a sua nova conta de documentos fica ativa
