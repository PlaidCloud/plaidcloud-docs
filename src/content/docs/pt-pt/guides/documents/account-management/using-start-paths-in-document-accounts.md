---
title: Utilizar caminhos iniciais nas contas de documentos
description: Configure caminhos iniciais nas contas de documentos do PlaidCloud para controlar a localização predefinida do diretório ao navegar no armazenamento de ficheiros.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/account-management/using-start-paths-in-document-accounts.md
---

O formulário de gestão de contas permite configurar as informações de ligação ao armazenamento e um caminho inicial. Um caminho inicial permite que quem utiliza a conta comece a navegar na estrutura de diretórios mais abaixo na árvore de diretórios. Esta opção é particularmente útil quando existem várias equipas que precisam de armazenamento de ficheiros segregado, mas pretende apenas uma conta de serviço de armazenamento subjacente.



A opção Caminho inicial nas contas de documentos é útil pelos seguintes motivos:


* Para controlar o acesso a subdiretórios para equipas e grupos específicos
* Para conceder acesso a apenas um bucket

Por exemplo, definir um caminho inicial *teams/team_1/* para a conta de documentos `Team 1` e *teams/team_2* para a conta de documentos `Team 2` oferece pontos de partida diferentes numa conta partilhada. Quando um membro abre a conta de documentos Team 1, começa a navegar nos ficheiros dentro de *team/team_1*. Não conseguirá subir na árvore nem ver nada acima de *teams/team_1*.



A Team 2 teria uma restrição semelhante, não podendo navegar para a área da Team 1.



Isto permite restringir equipas específicas a níveis inferiores da árvore, ao mesmo tempo que outras equipas têm acesso a níveis superiores, sem necessidade de complexidade adicional no armazenamento na nuvem, como buckets adicionais ou permissões especiais.



## Adicionar e atualizar o caminho inicial


1. Aceda a Document > Manage Accounts
2. Selecione a conta que pretende editar e entre no modo de edição
3. Adicione um Caminho inicial no campo de texto Caminho inicial
4. Selecione o botão Guardar

## Formato do caminho inicial


O caminho começa sempre pelo nome do bucket, seguido dos subdiretórios.



```text
<my-bucket>/folder1/folder2/
```
