---
title: Gerir editores de dados
description: Gira as atribuições de editores de dados nos projetos do PlaidCloud para controlar quem pode modificar os dados das tabelas diretamente através da interface de dados.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-data-editors.md
---

O PlaidCloud permite organizar e gerir editores de dados, incluindo etiquetas. Os editores de dados permitem editar dados de tabelas ou criar dados através da interação do utilizador.



O PlaidCloud utiliza um sistema baseado em caminhos para organizar os editores de dados, tal como se navega numa série de pastas, o que permite uma organização mais flexível e lógica (hierarquia de controlo) dos editores de dados. Com este sistema, os editores de dados podem ser movidos dentro de uma hierarquia de controlo. É possível criar várias referências a um editor de dados a partir de diferentes locais da hierarquia de controlo (hierarquias alternativas). A capacidade de gerir editores de dados com este método permite que a estrutura reflita as necessidades operacionais, de relatórios e de controlo.




## Criar um editor de dados a partir de uma tabela


Pode criar um editor de dados pronto a utilizar diretamente a partir de uma tabela existente. O PlaidCloud examina as colunas da tabela e pré-configura o editor — escolhendo um controlo de entrada para cada coluna e transformando as colunas que contêm um pequeno conjunto de valores repetidos em listas de escolha pendentes.


Para criar um editor de dados a partir de uma tabela:


1. Abra a vista **Tabelas** do projeto e selecione uma única tabela
2. Abra **Criar editor de dados a partir da tabela** — no menu **Novo** da barra de ferramentas ou clicando com o botão direito do rato na tabela
3. O PlaidCloud cria o perfil da tabela e abre a janela **Configuração do editor de dados** com tudo preenchido: define a origem e o destino como a tabela selecionada, para que as suas edições sejam guardadas diretamente nela, e atribui a cada coluna do separador **Colunas do formulário** um controlo que corresponde ao respetivo tipo de dados e valores
4. Reveja as colunas e ajuste os controlos conforme necessário
5. Clique em **Guardar** ou **Guardar e fechar**

Guardar cria o editor — clicar em **Cancelar** não adiciona nada.

Quando uma coluna corresponde a uma dimensão, escolha uma hierarquia para ela no separador Colunas do formulário antes de guardar. O PlaidCloud impede a gravação enquanto uma coluna de dimensão não tiver hierarquia.


## Como o PlaidCloud configura as colunas


Quando cria um editor a partir de uma tabela — ou utiliza **Preencher a partir da origem** —, o PlaidCloud configura cada coluna automaticamente:


- As colunas **Booleano** tornam-se uma caixa de seleção, ou uma lista Verdadeiro/Falso quando a coluna permite valores vazios
- As colunas **Data** tornam-se um seletor de datas
- As colunas **Numérico** tornam-se um campo numérico
- As colunas que correspondem a uma **dimensão** tornam-se um seletor de dimensão, onde escolhe a hierarquia — editar uma célula abre a mesma árvore de seleção de membros descrita em [Propriedades do tipo dimensão e seletor de membros](/pt-pt/guides/dimensions/dimensions/#propriedades-do-tipo-dimensão-e-o-seletor-de-membros), com **Expandir tudo**, **Recolher tudo**, **Aplicar**, **Limpar** e **Cancelar**
- As colunas cujos valores se repetem num pequeno conjunto — por exemplo, um código de estado ou de região — tornam-se uma **lista pendente** com os valores encontrados na coluna
- As outras colunas de **texto** tornam-se um campo de texto, ou uma área de texto para valores longos
- O PlaidCloud inclui colunas semelhantes a chaves, como IDs gerados automaticamente, mas marca-as como só de leitura

Para tabelas muito grandes, o PlaidCloud estima a lista de valores a partir de uma amostra de linhas. Pode alterar depois o controlo de qualquer coluna.

No separador **Colunas do formulário**, selecione uma coluna para ver uma breve explicação do motivo pelo qual o PlaidCloud escolheu o respetivo controlo.


## Ajustar o limite da lista de escolha


O PlaidCloud só transforma uma coluna numa lista pendente quando os seus valores se repetem num pequeno conjunto. Pode alterar esse limite e voltar a derivar as colunas:


1. No separador **Colunas do formulário**, defina **Máx. de valores da lista de escolha** como o maior número de valores distintos que uma coluna pode ter e ainda assim tornar-se uma lista pendente
2. Clique em **Refazer perfil**

O PlaidCloud volta a examinar a tabela de origem com a nova definição e reconstrói as colunas. Se o editor já tiver colunas, refazer o perfil substitui-as, pelo que o PlaidCloud pede confirmação.


## Preencher um editor existente a partir de uma tabela


Pode aplicar a mesma configuração automática a um editor que já está a editar:


1. Abra a configuração do editor de dados e aceda ao separador **Origem e destino**
2. Defina a origem como uma tabela
3. No separador **Colunas do formulário**, clique em **Preencher a partir da origem**

O PlaidCloud adiciona uma coluna configurada por cada coluna da tabela de origem. Mantém as colunas que já personalizou e pede-lhe que remova as colunas que já não existem na origem.


## Pesquisar


Para pesquisar editores de dados:


1. Utilize a caixa de filtro no canto inferior esquerdo da hierarquia de controlo

O filtro de pesquisa procura correspondências nos nomes e nas etiquetas dos editores de dados e mostra os resultados na hierarquia de controlo acima.




## Mover


Para mover um editor de dados dentro da hierarquia de controlo:


1. Arraste-o para a pasta onde pretende colocá-lo

## Mudar o nome


Para mudar o nome de um editor de dados:


1. Clique com o botão direito do rato no editor de dados
2. Selecione a opção de mudar o nome
3. Escreva o novo nome e guarde-o

O editor de dados passa a ter o novo nome, mas mantém o identificador único original.




## Eliminar


Pode eliminar um único editor de dados ou vários.


Para eliminar um editor de dados:


1. Selecione os editores de dados na hierarquia de controlo
2. Clique no botão de eliminar na barra de ferramentas superior


## Criar uma nova estrutura de diretórios


Para adicionar uma nova pasta à hierarquia de controlo:


1. Clique no botão Nova pasta na barra de ferramentas

Para adicionar uma pasta a uma pasta existente:


1. Clique com o botão direito do rato na pasta
2. Selecione Nova pasta


## Marcar a hierarquia para funções de visualização


A visualização dos editores de dados por várias funções:


1. Clique nas caixas de seleção Explorador ou Gestor

Para atualizar vários editores de dados:


1. Selecione os editores de dados na hierarquia de controlo
2. Selecione a função de visualização pretendida no menu Ações da barra de ferramentas superior


## Memorandos para descrever o conteúdo das tabelas


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


## Escrever através do assistente de IA ou do MCP

Para além dos ecrãs de configuração, `editor_upsert` pode definir a origem, o destino e os controlos de um editor de dados e escrever-lhe linhas diretamente — `data` é uma lista de objetos de linha indexados pelo id de cada controlo. Uma data inválida é recusada antes de qualquer alteração à tabela de destino, pelo que uma escrita incorreta nunca é aplicada parcialmente.
