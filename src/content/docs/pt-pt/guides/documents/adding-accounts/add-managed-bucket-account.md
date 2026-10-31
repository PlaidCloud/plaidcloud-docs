---
title: Adicionar uma conta de bucket gerido pelo PlaidCloud
description: Adicione armazenamento de ficheiros totalmente gerido ao Document do PlaidCloud num único passo — escolha um nome e o PlaidCloud configura tudo por si, sem nada para configurar.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-managed-bucket-account.md
---

Um **Bucket gerido pelo PlaidCloud** é a forma mais rápida de adicionar armazenamento de ficheiros ao Document. O PlaidCloud cria e gere o armazenamento por si — não há nada para configurar previamente nem credenciais para gerir. Basta atribuir-lhe um nome.

Utilize um Bucket gerido pelo PlaidCloud quando quiser um local novo e autónomo para guardar ficheiros do Document. Para ligar armazenamento que já possui e gere por si, escolha antes um dos outros fornecedores na página [Adicionar novas contas de documentos](/pt-pt/guides/documents/adding-accounts/).

## Configuração

1. Inicie sessão no PlaidCloud
2. Selecione a área de trabalho em que a nova conta de documentos vai residir
3. Aceda a `Document > Manage Accounts`
4. Selecione o botão `+ New Account`
5. Selecione `PlaidCloud Managed Bucket` como Tipo de serviço
6. Preencha um nome e uma descrição opcional
7. Introduza um **Nome do bucket**. Os nomes têm de ter entre 3 e 63 carateres, usar apenas letras minúsculas, dígitos, pontos ou hífenes, e começar e terminar com uma letra ou um dígito. O nome tem de ser **globalmente único** — se já estiver a ser utilizado, ser-lhe-á pedido que escolha outro
8. Selecione um **Modelo de segurança** adequado ao seu caso de utilização. Se tiver dúvidas, deixe `Private`
9. Selecione o botão Guardar

O PlaidCloud configura o armazenamento e torna-o proprietário do mesmo. A conta fica imediatamente pronta para navegar e carregar ficheiros — não há mais nada a configurar.

:::note
Os Buckets geridos pelo PlaidCloud estão disponíveis nos planos **Business** e **Enterprise**. Se o seu plano não os incluir, ou se tiver atingido o limite do seu plano, o formulário informa-o quando tentar criar um.
:::

## Depois da criação

- O nome do bucket fica fixo depois de criado — não pode ser alterado numa conta existente.
- Eliminar a conta **deixa os ficheiros armazenados no mesmo local**, pelo que uma eliminação nunca destrói os seus dados. Contacte o suporte se precisar que o próprio armazenamento seja removido.
- Um Bucket gerido pelo PlaidCloud comporta-se como qualquer outra conta de documentos no que respeita ao [controlo de acesso](/pt-pt/guides/documents/account-management/control-document-account-access/), à [propriedade](/pt-pt/guides/documents/account-management/managing-document-account-owners/) e à navegação.
