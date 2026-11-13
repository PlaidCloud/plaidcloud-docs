---
title: Adicionar uma conta Google Drive
description: Adicione uma conta de armazenamento Google Drive ao PlaidCloud para importar e exportar ficheiros de dados através do armazenamento na nuvem Google Drive.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Configuração do Google Drive

Estes passos têm de ser concluídos na Google Cloud Console para criar uma conta de serviço que o PlaidCloud possa usar para aceder ao Google Drive.

### Criar um projeto Google Cloud

1. Inicie sessão na [Google Cloud Console](https://console.cloud.google.com)
2. Crie um novo projeto ou selecione um existente

### Ativar a API do Google Drive

1. Navegue até **APIs & Services > Library**
2. Pesquise **Google Drive API**
3. Selecione-a e clique em **Enable**

### Criar uma conta de serviço

1. Navegue até **APIs & Services > Credentials**
2. Selecione **+ Create Credentials > Service account**
3. Introduza um nome para a conta de serviço (p. ex. `plaidcloud-drive`)
4. Selecione **Create and Continue**
5. Opcionalmente, conceda funções (p. ex. **Viewer** para só de leitura ou **Editor** para leitura/escrita). Selecione **Continue**.
6. Selecione **Done**

### Gerar uma chave de conta de serviço

1. Na lista **Service Accounts**, selecione a conta de serviço que acabou de criar
2. Navegue até ao separador **Keys**
3. Selecione **Add Key > Create new key**
4. Escolha o formato **JSON** e selecione **Create**
5. Será transferido um ficheiro de chave JSON. Guarde este ficheiro em segurança — contém as credenciais que o PlaidCloud vai utilizar.

### Partilhar o conteúdo do Drive com a conta de serviço

1. Copie o endereço de correio eletrónico da conta de serviço (p. ex. `plaidcloud-drive@your-project.iam.gserviceaccount.com`)
2. No Google Drive, partilhe com este endereço de correio eletrónico a(s) pasta(s) a que pretende que o PlaidCloud aceda, concedendo acesso **Editor**. Para utilizar uma Drive partilhada, adicione antes a conta de serviço como membro da mesma.

Neste momento, deverá ter tudo o que precisa para adicionar a sua conta Google Drive ao Document do PlaidCloud.


## Configuração do Document do PlaidCloud

1. Inicie sessão no PlaidCloud
2. Selecione a área de trabalho em que a nova conta de documentos vai residir
3. Aceda a `Document > Manage`
4. Selecione o botão **Nova conta**
5. Selecione `Google Drive` como Tipo de serviço
6. Preencha um nome e uma descrição
7. Introduza o caminho da pasta partilhada no campo **Caminho inicial** ou deixe-o em branco para aceder a todo o conteúdo partilhado
8. Selecione um **Modelo de segurança** adequado ao seu caso de utilização. Se tiver dúvidas, deixe `Private`.
9. Cole todo o conteúdo do ficheiro de chave JSON no campo JSON de credenciais OAuth2, em Credenciais de autenticação
10. Selecione o botão Guardar e a sua nova conta de documentos fica ativa

## Utilizar a conta em fluxos de trabalho

Uma conta Google Drive funciona em fluxos de trabalho, bem como no navegador do Document. Os passos podem listar, importar, exportar, copiar, mover, mudar o nome e eliminar ficheiros e criar pastas.

- **Localizações.** As localizações de nível superior da conta são as pastas partilhadas com a conta de serviço e as Drives partilhadas de que esta é membro. Os caminhos são nomes de pastas, como `Finance/Reports/2026`. Se duas pastas partilhadas ou Drives partilhadas tiverem o mesmo nome, a conta recusa-se a abrir esse nome. Mude o nome ou anule a partilha de todas, exceto uma.
- **Google Sheets.** Uma Google Sheet é lida como uma exportação `.xlsx` e aparece como `Name.xlsx`. Os outros ficheiros do Google Workspace, como Docs e Slides, não podem ser lidos.
- **Novos ficheiros em My Drive.** Uma conta de serviço não tem armazenamento próprio, pelo que, numa pasta que se encontra no My Drive pessoal de alguém, pode substituir um ficheiro existente, mas não pode criar um novo. Crie primeiro o ficheiro nessa pasta ou utilize uma pasta numa Drive partilhada, que aceita novos ficheiros e pastas.
- **Pastas inexistentes.** Uma pasta que não existe é listada como vazia, em vez de provocar um erro.
- **Limitação de pedidos.** O PlaidCloud tenta novamente de forma automática quando a Google limita um pedido ou devolve um erro temporário.
