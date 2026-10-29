---
title: Usando caminhos iniciais em contas de documentos
description: Configure caminhos iniciais em contas de documentos do PlaidCloud para controlar o local padrão do diretório ao navegar pelo armazenamento de arquivos.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/account-management/using-start-paths-in-document-accounts.md
---

O formulário de gerenciamento da conta permite configurar as informações de conexão do armazenamento e um caminho inicial. Um caminho inicial permite que quem usa a conta comece a navegar pela estrutura de diretórios em um ponto mais abaixo na árvore de diretórios. Essa opção é útil quando você tem várias equipes que precisam de armazenamento de arquivos segregado, mas quer apenas uma conta de serviço de armazenamento subjacente.



A opção Caminho inicial nas contas de documentos é útil pelos seguintes motivos:


* Para controlar o acesso a subdiretórios para equipes e grupos específicos
* Para conceder acesso a apenas um bucket

Por exemplo, definir um caminho inicial *teams/team_1/* para a conta de documentos `Team 1` e *teams/team_2* para a conta de documentos `Team 2` fornece pontos de partida diferentes em uma conta compartilhada. Quando um membro abre a conta de documentos Team 1, ele começa a navegar pelos arquivos dentro de *team/team_1*. Ele não poderá subir na árvore e ver nada acima de *teams/team_1*.



A Team 2 teria uma restrição semelhante, não podendo navegar para a área da Team 1.



Isso permite restringir equipes específicas a níveis mais baixos da árvore, enquanto outras equipes têm acesso a níveis mais altos, sem exigir nenhuma complexidade adicional de armazenamento em nuvem, como buckets extras ou permissões especiais.



## Adicionando e atualizando o caminho inicial


1. Vá para Document > Manage Accounts
2. Selecione a conta que deseja editar e entre no modo de edição
3. Adicione um caminho inicial no campo de texto Caminho inicial
4. Clique no botão Salvar

## Formato do caminho inicial


O caminho sempre começa com o nome do bucket, seguido dos subdiretórios.



```text
<my-bucket>/folder1/folder2/
```
