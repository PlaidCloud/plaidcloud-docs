---
title: Gerenciar editores de dados
description: Gerencie as atribuições de editores de dados em projetos do PlaidCloud para controlar quem pode modificar os dados de tabela diretamente pela interface de dados.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-data-editors.md
---

O PlaidCloud oferece a capacidade de organizar e gerenciar editores de dados, incluindo rótulos. Os editores de dados permitem editar dados de tabela ou criar dados por meio da interação do usuário.

O PlaidCloud usa um sistema baseado em caminhos para organizar os editores de dados, como o que você usaria para navegar por uma série de pastas, permitindo uma organização mais flexível e lógica (hierarquia de controle) dos editores de dados. Com esse sistema, os editores de dados podem ser movidos dentro de uma hierarquia de controle. É possível criar várias referências a um editor de dados a partir de locais diferentes da hierarquia de controle (hierarquias alternativas). A capacidade de gerenciar editores de dados por esse método permite que a estrutura reflita necessidades operacionais, de relatórios e de controle.

## Criar um editor de dados a partir de uma tabela

Você pode criar um editor de dados pronto para uso diretamente a partir de uma tabela existente. O PlaidCloud examina as colunas da tabela e pré-configura o editor — escolhendo um controle de entrada para cada coluna e transformando em listas de seleção suspensas as colunas que contêm um pequeno conjunto de valores repetidos.

Para criar um editor de dados a partir de uma tabela:

1. Abra a visão **Tabelas** do projeto e selecione uma única tabela
2. Abra **Criar editor de dados a partir da tabela** — no menu **Novo** da barra de ferramentas ou clicando com o botão direito na tabela
3. O PlaidCloud faz o perfil da tabela e abre a janela **Configuração do editor de dados** com tudo preenchido: ele define a origem e o destino como a tabela selecionada, de modo que suas edições sejam salvas diretamente nela, e atribui a cada coluna na guia **Colunas do formulário** um controle compatível com o tipo e os valores dos dados
4. Revise as colunas e ajuste os controles conforme necessário
5. Clique em **Salvar** ou **Salvar e fechar**

Salvar cria o editor — clicar em **Cancelar** não adiciona nada.

Quando uma coluna corresponde a uma dimensão, escolha uma hierarquia para ela na guia Colunas do formulário antes de salvar. O PlaidCloud bloqueia o salvamento enquanto uma coluna de dimensão não tiver hierarquia.

## Como o PlaidCloud configura as colunas

Quando você cria um editor a partir de uma tabela — ou usa **Preencher a partir da origem** — o PlaidCloud configura cada coluna automaticamente:

- As colunas **Booleano** se tornam uma caixa de seleção, ou uma lista Verdadeiro/Falso quando a coluna permite valores vazios
- As colunas **Data** se tornam um seletor de data
- As colunas **Numérico** se tornam um campo numérico
- As colunas que correspondem a uma **dimensão** se tornam um seletor de dimensão, em que você escolhe a hierarquia — editar uma célula abre a mesma árvore de seleção de membros descrita em [Propriedades do tipo dimensão e o seletor de membros](/pt-br/guides/dimensions/dimensions/#propriedades-do-tipo-dimensão-e-o-seletor-de-membros), com **Expandir tudo**, **Recolher tudo**, **Aplicar**, **Limpar** e **Cancelar**
- As colunas cujos valores se repetem em um pequeno conjunto — por exemplo, um código de status ou de região — se tornam uma **lista suspensa** que relaciona os valores encontrados na coluna
- As demais colunas de **texto** se tornam um campo de texto, ou uma área de texto para valores longos
- O PlaidCloud inclui colunas do tipo chave, como IDs gerados automaticamente, mas as marca como somente leitura

Para tabelas muito grandes, o PlaidCloud estima a lista de valores a partir de uma amostra de linhas. Você pode alterar o controle de qualquer coluna depois.

Na guia **Colunas do formulário**, selecione uma coluna para ver uma breve explicação de por que o PlaidCloud escolheu o controle dela.

## Ajustar o limite da lista de seleção

O PlaidCloud transforma uma coluna em lista suspensa somente quando seus valores se repetem em um pequeno conjunto. Você pode alterar esse limite e derivar as colunas novamente:

1. Na guia **Colunas do formulário**, defina **Máximo de valores na lista de seleção** como o maior número de valores distintos que uma coluna pode ter e ainda se tornar uma lista suspensa
2. Clique em **Refazer perfil**

O PlaidCloud examina novamente a tabela de origem com a nova configuração e reconstrói as colunas. Se o editor já tiver colunas, refazer o perfil as substitui, então o PlaidCloud pede que você confirme.

## Preencher um editor existente a partir de uma tabela

Você pode aplicar a mesma configuração automática a um editor que já está editando:

1. Abra a configuração do editor de dados e vá para a guia **Origem e destino**
2. Defina a origem como uma tabela
3. Na guia **Colunas do formulário**, clique em **Preencher a partir da origem**

O PlaidCloud adiciona uma coluna configurada para cada coluna da tabela de origem. Ele mantém as colunas que você já personalizou e solicita que você remova as colunas que não estão mais na origem.

## Pesquisar

Para pesquisar editores de dados:

1. Use a caixa de filtro no canto inferior esquerdo da hierarquia de controle

O filtro de pesquisa procura correspondências nos nomes e rótulos dos editores de dados e mostra os resultados na hierarquia de controle acima.

## Mover

Para mover um editor de dados dentro da hierarquia de controle:

1. Arraste-o para a pasta em que deseja colocá-lo

## Renomear

Para renomear um editor de dados:

1. Clique com o botão direito no editor de dados
2. Selecione a opção de renomear
3. Digite o novo nome e salve

O editor de dados será renomeado, mas manterá seu identificador exclusivo original.

## Excluir

Você pode excluir um único editor de dados ou vários editores de dados.

Para excluir um editor de dados:

1. Selecione os editores de dados na hierarquia de controle
2. Clique no botão de excluir na barra de ferramentas superior

## Criar uma nova estrutura de diretórios

Para adicionar uma nova pasta à hierarquia de controle:

1. Clique no botão Nova pasta na barra de ferramentas

Para adicionar uma pasta a uma pasta existente:

1. Clique com o botão direito na pasta
2. Selecione Nova pasta

## Marcar a hierarquia para papéis de visualização

A visualização de editores de dados por diferentes papéis:

1. Clique nas caixas de seleção Explorador ou Gerente

Para atualizar vários editores de dados:

1. Selecione os editores de dados na hierarquia de controle
2. Selecione o papel de visualização desejado no menu Ações da barra de ferramentas superior

## Memorandos para descrever o conteúdo da tabela

Para adicionar um memorando a um editor de dados:

1. Selecione o editor de dados
2. Atualize o memorando no formulário de contexto à direita

## Ver atributos adicionais da hierarquia

Para ver e editar atributos adicionais do editor de dados:

1. Selecione o editor de dados e veja o formulário de contexto do editor de dados à direita

## Duplicar um editor de dados

Para duplicar um editor de dados:

1. Selecione o editor de dados
2. Clique no botão Duplicar na barra de ferramentas superior

## Gravar por meio do assistente de IA ou do MCP

Além das telas de configuração, `editor_upsert` pode definir a origem, o destino e os controles de um editor de dados e gravar linhas nele diretamente — `data` é uma lista de objetos de linha indexados pelo id de cada controle. Uma data inválida é recusada antes que qualquer coisa toque a tabela de destino, de modo que uma gravação incorreta nunca é aplicada parcialmente.
