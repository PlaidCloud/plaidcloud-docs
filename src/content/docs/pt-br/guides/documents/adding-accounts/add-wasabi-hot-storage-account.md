---
title: Adicionar conta Wasabi Hot Storage
description: Adicione uma conta Wasabi Hot Storage ao PlaidCloud para importar e exportar arquivos de dados usando armazenamento em nuvem de baixo custo.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-wasabi-hot-storage-account.md
---

## Configuração do Wasabi Hot Storage


Estas etapas devem ser concluídas no console do Wasabi Hot Storage


1. Entre em uma conta Wasabi Hot Storage ou crie uma
2. Acesse `Buckets` no console
3. Crie um bucket padrão ou de teste
4. Acesse Users no console
5. Selecione o botão `Create User`
6. Quando solicitado, informe um nome de usuário e selecione o usuário `Programmatic (create API key)`
7. Ignore a atribuição de grupo. Selecione o botão `Next`
8. Selecione o ícone de mais ao lado da política `WasabiFullAccess` para anexá-la ao usuário. Selecione o botão `Next`.
9. Revise as configurações do usuário e selecione `Create User`
10. Capture as chaves geradas para o usuário baixando o CSV ou copiando e colando as chaves em algum lugar para uso posterior. Não será possível recuperar essa chave novamente, portanto guarde-a. Se precisar gerar uma chave novamente, volte à etapa 5 acima.

Agora você tem tudo de que precisa para adicionar sua conta Wasabi ao PlaidCloud Document.



## Configuração do PlaidCloud Document

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Acesse `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `Wasabi Hot Storage` como **Tipo de serviço**
6. Preencha um nome e uma descrição
7. Informe o nome do bucket e um prefixo de caminho opcional no campo **Caminho inicial** (por exemplo, `my-bucket` ou `my-bucket/data`). O primeiro segmento do caminho é o nome do bucket.
8. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Deixe `Private` se tiver dúvida.
9. Cole a **Access Key** criada na etapa 10 acima no campo ID da chave de acesso em Credenciais de autenticação
10. Cole a **Secret Key** criada na etapa 10 acima no campo Chave de acesso secreta em Credenciais de autenticação
11. Informe a **Região** se sua conta Wasabi usar uma região específica; caso contrário, deixe em branco
12. Selecione o botão Salvar e sua nova conta de documentos estará ativa
