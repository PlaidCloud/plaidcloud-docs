---
title: Adicionar uma conta de bucket gerenciado pelo PlaidCloud
description: Adicione armazenamento de arquivos totalmente gerenciado ao PlaidCloud Document em uma única etapa — escolha um nome e o PlaidCloud configura tudo para você, sem nada a configurar.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-managed-bucket-account.md
---

Um **Bucket gerenciado pelo PlaidCloud** é a maneira mais rápida de adicionar armazenamento de arquivos ao Document. O PlaidCloud cria e opera o armazenamento para você — não há nada para configurar antes e nenhuma credencial para gerenciar. Basta dar um nome.

Use um Bucket gerenciado pelo PlaidCloud quando quiser um local novo e independente para guardar arquivos do Document. Para conectar um armazenamento que você já possui e gerencia por conta própria, escolha um dos outros provedores na página [Adicionando novas contas de documentos](/pt-br/guides/documents/adding-accounts/).

## Configuração

1. Entre no PlaidCloud
2. Selecione o espaço de trabalho em que a nova conta de documentos ficará
3. Vá para `Document > Manage Accounts`
4. Clique no botão `+ New Account`
5. Selecione `PlaidCloud Managed Bucket` como o Tipo de serviço
6. Preencha um nome e uma descrição opcional
7. Informe um **Nome do bucket**. Os nomes devem ter de 3 a 63 caracteres, usar apenas letras minúsculas, dígitos, pontos ou hifens, e começar e terminar com uma letra ou um dígito. O nome deve ser **globalmente exclusivo** — se já estiver em uso, você será solicitado a escolher outro
8. Selecione um **Modelo de segurança** adequado ao seu caso de uso. Se estiver em dúvida, deixe como `Private`
9. Clique no botão Salvar

O PlaidCloud configura o armazenamento e torna você o proprietário. A conta fica pronta imediatamente para navegar e enviar arquivos — não há mais nada a configurar.

:::note
Os Buckets gerenciados pelo PlaidCloud estão disponíveis nos planos **Business** e **Enterprise**. Se o seu plano não os inclui, ou se você atingiu o limite do plano, o formulário informará isso quando você tentar criar um.
:::

## Após a criação

- O nome do bucket é fixo depois de criado — não pode ser alterado em uma conta existente.
- Excluir a conta **mantém os arquivos armazenados no lugar**, de modo que uma exclusão nunca destrói seus dados. Entre em contato com o suporte se precisar que o próprio armazenamento seja removido.
- Um Bucket gerenciado pelo PlaidCloud se comporta como qualquer outra conta de documentos no que se refere a [controle de acesso](/pt-br/guides/documents/account-management/control-document-account-access/), [propriedade](/pt-br/guides/documents/account-management/managing-document-account-owners/) e navegação.
