---
title: Gerir tabelas e vistas
description: Faça a gestão de tabelas e vistas nos projetos PlaidCloud, incluindo criação, configuração, permissões e organização dos objetos de dados.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

O PlaidCloud permite organizar e gerir tabelas, incluindo etiquetas. As tabelas estão disponíveis para todos os fluxos de trabalho de um projeto e têm muitas ferramentas e opções.


Para além das tabelas, o PlaidCloud oferece também Vistas baseadas nos dados das tabelas. A utilização de Vistas permite atualizações instantâneas quando ocorrem alterações nas tabelas subjacentes, bem como poupar espaço de armazenamento de dados.



As opções incluem:


* A mesma tabela pode existir em vários caminhos da hierarquia (hierarquias alternativas)
* As tabelas podem ser etiquetadas para facilitar a pesquisa e a inclusão nos processos do PlaidCloud
* As tabelas podem ter versões
* As tabelas podem ser publicadas para ficarem disponíveis para Visualizações de painéis de controlo

O PlaidCloud utiliza um sistema baseado em caminhos para organizar as tabelas, como o que se utiliza para navegar numa série de pastas, permitindo uma organização das tabelas mais flexível e lógica. Com este sistema, as tabelas podem ser movidas dentro de uma hierarquia, ou podem ser criadas várias referências a uma tabela a partir de diferentes locais da hierarquia (hierarquias alternativas). A capacidade de gerir tabelas por este método permite que a estrutura reflita as necessidades operacionais, de relatórios e de controlo.



## Encontrar tabelas


Utilize a caixa de filtro no canto inferior esquerdo da hierarquia para pesquisar nos nomes e nas etiquetas das tabelas. As correspondências são apresentadas na hierarquia acima.


### Por fluxo de trabalho

A pasta **By Workflow** no final do separador **Tabelas** agrupa as tabelas por cada fluxo de trabalho que as lê ou escreve. Abra um fluxo de trabalho para ver as suas tabelas. A pasta é uma vista das mesmas tabelas, pelo que não pode mover nem copiar nada a partir dela.


### Por coluna

Escreva o nome de uma coluna na caixa de pesquisa de colunas do separador **Tabelas** para mostrar apenas as tabelas que têm uma coluna com esse nome. Selecione **Contém** para corresponder a parte do nome da coluna em vez do nome completo. Limpe a caixa para voltar a mostrar todas as tabelas. Uma pesquisa longa pode devolver resultados em páginas e a linha de estado indica quando ainda está a pesquisar ou pode estar incompleta.

Selecione **Column Tree** para pesquisar numa janela própria. Cada tabela que tem a coluna abre-se em duas listas:

* **Fed by** — as tabelas que fornecem a coluna
* **Feeds** — as tabelas que a coluna passa a alimentar

Um assistente de IA ligado através de MCP encontra as mesmas tabelas com `table_find(column=...)`, correspondendo ao nome completo ou a parte dele.


### Pesquisar valores

Para descobrir que tabelas contêm um valor, selecione **Search Values** no separador **Tabelas**, ou clique com o botão direito do rato numa tabela e escolha **Search Value** para procurar apenas nessa tabela. Introduza o valor, escolha **Contém** para corresponder a parte de um valor e selecione **Pesquisar**. Cada tabela que contém o valor é listada com as colunas em que aparece e alguns dos valores correspondentes.

Antes de pesquisar, tenha em atenção que:

* Só vê as linhas que já poderia abrir. A segurança ao nível da linha aplica-se a todas as pesquisas.
* O histórico de consultas do seu armazém de dados regista os valores que pesquisa.
* A pesquisa abrange as colunas de texto das tabelas. As tabelas que não foram construídas são ignoradas e indicadas num aviso.
* Os resultados vêm em páginas. Quando a linha de estado indica que a pesquisa parou antecipadamente, escolha **Search more** para continuar com as tabelas ainda não pesquisadas.

Um assistente de IA ligado através de MCP utiliza `table_value_search`. Devolve as tabelas e as colunas que contêm o valor, nunca os próprios valores. Quando pede ao assistente de IA, num projeto, que encontre um valor, o Weave envia os nomes das tabelas e das colunas correspondentes ao fornecedor do modelo de linguagem.



## Importar um ficheiro CSV

**Para transformar um ficheiro CSV numa nova tabela neste projeto:**

1. Arraste o ficheiro do seu computador para a lista de **Tabelas** do projeto, ou escolha **Novo** > **Tabela a partir de ficheiro CSV** na barra de ferramentas e largue o ficheiro na caixa ou clique em **Escolher um ficheiro CSV**.
2. O PlaidCloud carrega o ficheiro para a sua **Personal Temp Drive**, ou para a **Temp Drive** da área de trabalho se não tiver uma, e importa-o para uma nova tabela no nível superior da lista, com o nome do ficheiro: `Sales Data.csv` passa a `sales_data`. Se o projeto já tiver uma tabela com esse nome, a nova recebe um número, como `sales_data_2`.
3. A lista é atualizada com a nova tabela selecionada e **Os seus dados num relance** abre-se sobre ela. Consulte [Start With Your Own CSV](/pt-pt/get-started/quickstart/#comece-com-o-seu-próprio-csv) para ver o que o painel mostra.

Só são aceites ficheiros terminados em `.csv`. Precisa de permissão para criar tabelas e para escrever no armazenamento de documentos, e um projeto bloqueado não aceita um CSV até ser desbloqueado. Se a importação falhar, a janela indica o motivo e o projeto fica como estava. O PlaidCloud elimina o ficheiro carregado da unidade temporária assim que a importação termina, quer tenha tido êxito ou não; se tal não acontecer, a unidade temporária elimina-o ao fim de um dia.

## Mover


**Para mover uma tabela:**


1. Arraste-a para a pasta onde pretende que fique localizada

## Mudar o nome

**Para mudar o nome de uma tabela:**


1. Clique com o botão direito do rato na tabela
2. Selecione a opção de mudar o nome
3. Escreva o novo nome e guarde-o
4. A tabela tem agora um novo nome, mas conserva o seu identificador único original.

## Limpar


**Para limpar uma tabela:**


1. Selecione as tabelas na hierarquia ‘
2. Clique no botão de limpar na barra de ferramentas superior.

*Nota: Pode limpar uma única tabela ou várias tabelas*



## Eliminar


**Para eliminar uma tabela:**


1. Selecione as tabelas na hierarquia
2. Clique no botão de eliminar na barra de ferramentas superior
3. A operação de eliminação verifica se a tabela está a ser utilizada por passos de fluxo de trabalho ou por Vistas. Se estiver, ser-lhe-á pedido que remova essas associações antes de a eliminação poder ocorrer.

*Nota: Também pode forçar a eliminação das tabelas. A eliminação forçada das tabelas deixa referências quebradas, pelo que deve ser utilizada com moderação.*


### Última leitura

A janela de eliminação mostra quando a tabela foi lida pela última vez, por exemplo **Last read 3 days ago by** uma pessoa ou um passo, para que possa distinguir uma tabela que ninguém utiliza de uma que ainda está em uso. O PlaidCloud obtém esta informação a partir do próprio histórico de consultas do seu armazém de dados e exclui as leituras feitas pelas suas próprias tarefas de manutenção.

| Armazém de dados | O que é necessário |
| --- | --- |
| Snowflake | As leituras provêm do Access History, que o Snowflake regista com um atraso até cerca de 3 horas. A função da ligação precisa da função de base de dados `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` na base de dados `SNOWFLAKE` também funciona). A edição Standard do Snowflake não tem Access History. |
| Databricks | As leituras provêm da tabela de linhagem, que o Databricks também regista com atraso, pelo que uma leitura recente pode ainda não aparecer. A identidade da ligação precisa de `USE CATALOG` em `system`, `USE SCHEMA` em `system.access` e `SELECT` em `system.access.table_lineage`. |
| PlaidCloud Lakehouse | O histórico de leituras ainda não está disponível. A janela mostra **Read history incomplete**. |

Quando liga o seu armazém de dados, [a verificação da ligação](/pt-pt/guides/connections/external-lakehouse/#3-verificar-e-depois-utilizar) recomenda qualquer uma destas concessões que esteja em falta, cada uma com a instrução a executar. São recomendadas, não obrigatórias: sem elas, o armazém de dados liga-se e a janela mostra **Read history incomplete**.

Quando o PlaidCloud não consegue ler todo o histórico, a linha indica **Read history incomplete** e nunca comunica “sem leituras” em seu lugar. Qualquer pessoa com acesso SQL direto ao seu armazém de dados pode definir uma etiqueta de sessão que altera a forma como as suas próprias leituras são rotuladas.

Um assistente de IA ligado através de MCP obtém a mesma resposta a partir de `table_describe(include=['last_read'])`.



## Ver onde uma tabela é utilizada


Ao selecionar uma tabela, abre-se o respetivo painel de detalhes, que lista os passos de fluxo de trabalho que a tocam:


* **Tabela criada por** — passos que escrevem na tabela
* **A tabela contribui para** — passos que leem a partir dela
* **Pode referenciar esta tabela** — passos que chegam a uma tabela através de uma variável que não pode ser resolvida. Esta secção só aparece quando existem tais passos.


Um passo pode indicar uma tabela diretamente ou chegar a ela através de um caminho que contém uma variável, como `/Periods/{period}/Sales`. Quando essa variável tem um valor atual, o passo aparece nas duas primeiras listas com um ícone de informação ao lado. Passe o rato sobre a linha para ver o caminho tal como o passo o guarda.


Trate essas linhas como a resposta mais fraca que são. Descrevem o que uma execução iniciada agora tocaria — não tudo o que alguma vez tocou na tabela. Altere a variável e é lida uma tabela diferente.


Algumas variáveis não podem ser resolvidas. Ou nada definiu a variável, ou o valor que uma execução utiliza não provém do que está guardado — um Workflow Loop obtém as suas variáveis a partir dos dados à medida que itera, um passo Set Variable atribui durante a execução, uma macro recebe as suas variáveis do passo que a chama e uma execução iniciada por um sensor transporta os detalhes do próprio sensor. Em cada caso, o que fica guardado entre execuções é o que sobrou da última, e não um valor em que confiar. Em vez de resolver esses casos para uma tabela que pode ser a errada, o PlaidCloud lista os passos pelo nome em **Pode referenciar esta tabela**, com a variável que não conseguiu resolver, para que possa abri-los e verificar.


Um passo que a sua função não pode ver continua a ser listado, para que saiba que a tabela está em uso, mas sem o seu nome ou fluxo de trabalho, e não pode abri-lo. Continua a contar quando elimina a tabela. Um passo que pode ver é listado sem qualquer fluxo de trabalho que a sua função oculte. Nada fica oculto a um Arquiteto.


*Nota: Quando elimina tabelas da lista de **Tabelas**, um passo que chega a uma tabela através de um caminho, com ou sem variável, conta como a utilizando, mesmo quando a sua variável não pode ser resolvida. A janela de eliminação lista o passo e a eliminação só avança se a forçar.*



## Criar uma nova estrutura de diretórios


**Para adicionar uma nova pasta:**


1. Clique no botão Nova pasta na barra de ferramentas

**Para adicionar uma pasta a uma pasta existente:**


1. Clique com o botão direito do rato na pasta
2. Selecione Nova pasta


## Ver dados (Explorador de tabelas)


Os dados das tabelas são vistos através do Data Explorer. O Data Explorer fornece uma vista em grelha dos dados, bem como um resumo coluna a coluna dos valores e das estatísticas. Estão disponíveis a filtragem por apontar e clicar e a exportação para formatos de ficheiro conhecidos. As seleções de filtro também podem ser guardadas como um passo Extract utilizável num fluxo de trabalho.



## Publicar a tabela para relatórios


As Visualizações de painéis de controlo estão intencionalmente limitadas às tabelas que foram publicadas. Ao publicar uma tabela, pode indicar um nome único que possa distinguir os dados. Isto pode ser útil quando a tabela tem um nome mais obscuro na parte do fluxo de trabalho que a gerou, mas precisa de um nome mais claro para quem cria painéis de controlo.


As tabelas publicadas não têm caminhos associados. Aparecem como uma lista de tabelas para utilização na área de painéis de controlo.



## Marcar a tabela para funções de visualização


A visualização das tabelas pelas várias funções pode ser controlada ao clicar nas caixas de verificação Explorador ou Gestor. Se for necessário atualizar várias tabelas, selecione as tabelas na hierarquia e selecione a função de visualização pretendida no menu Ações da barra de ferramentas superior.



## Memorandos para descrever o conteúdo das tabelas


Adicione um memorando a uma tabela para ajudar a compreender os dados.



## Ver a forma, o tamanho e a hora da última atualização da tabela


O número de linhas, de colunas e o tamanho dos dados de cada tabela são mostrados na hierarquia de tabelas. Para tabelas muito grandes (vários milhões de linhas), a contagem de linhas pode ser estimada e é apresentado um indicador de contagem aproximada de linhas.



## Ver atributos adicionais da tabela


**Para ver e editar outros atributos da tabela:**


1. Selecione uma tabela
2. Clique para ver o formulário de contexto da tabela à direita.


## Duplicar uma tabela


**Para duplicar uma tabela:**


1. Selecione a tabela
2. Clique no botão de duplicar na barra de ferramentas superior.


## Criar um editor de dados a partir de uma tabela


Pode transformar uma tabela num editor de dados configurado num só passo — selecione a tabela e escolha **Criar editor de dados a partir da tabela** no menu **Novo** ou no menu de contexto. O PlaidCloud examina as colunas da tabela e pré-constrói os controlos de entrada do editor. Consulte [Create a Data Editor from a Table](/pt-pt/guides/projects/managing-data-editors/#criar-um-editor-de-dados-a-partir-de-uma-tabela) para mais detalhes.
