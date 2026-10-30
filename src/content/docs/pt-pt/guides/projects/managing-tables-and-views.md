---
title: Gerir tabelas e vistas
description: Gerir tabelas e vistas nos projetos do PlaidCloud, incluindo criação, configuração, permissões e organização dos objetos de dados.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

O PlaidCloud permite organizar e gerir tabelas, incluindo etiquetas. As tabelas estão disponíveis para todos os fluxos de trabalho de um projeto e têm muitas ferramentas e opções.


Além das tabelas, o PlaidCloud também oferece Vistas baseadas em dados de tabelas. Utilizar Vistas permite atualizações instantâneas quando ocorrem alterações nas tabelas subjacentes, além de poupar espaço de armazenamento de dados.



As opções incluem:


* A mesma tabela pode existir em vários caminhos da hierarquia (hierarquias alternativas)
* As tabelas podem ser etiquetadas para facilitar a pesquisa e a inclusão em processos do PlaidCloud
* As tabelas podem ter versões
* As tabelas podem ser publicadas para ficarem disponíveis para Visualizações em painéis de controlo

O PlaidCloud usa um sistema baseado em caminhos para organizar as tabelas, como o que se usa para navegar numa série de pastas, o que permite uma organização das tabelas mais flexível e lógica. Com este sistema, as tabelas podem ser movidas dentro de uma hierarquia, ou podem ser criadas várias referências a uma tabela a partir de diferentes locais da hierarquia (hierarquias alternativas). A capacidade de gerir tabelas por este método permite que a estrutura reflita as necessidades operacionais, de relatórios e de controlo.



## Encontrar tabelas


Use a caixa de filtro no canto inferior esquerdo da hierarquia para pesquisar nomes e etiquetas de tabelas. As correspondências aparecem na hierarquia acima.


### Por fluxo de trabalho

A pasta **Por fluxo de trabalho** no fim do separador **Tabelas** agrupa as tabelas sob cada fluxo de trabalho que as lê ou escreve. Abra um fluxo de trabalho para ver as respetivas tabelas. A pasta é uma vista das mesmas tabelas, pelo que não pode mover nem copiar nada a partir dela.


### Por coluna

Escreva o nome de uma coluna na caixa de pesquisa de colunas do separador **Tabelas** e prima Enter, ou selecione a lupa ao lado, para mostrar apenas as tabelas que têm uma coluna com esse nome. A pesquisa lê nomes de colunas, não os dados, pelo que é rápida. Selecione **Contém** para corresponder a parte do nome de uma coluna em vez do nome inteiro. Limpe a caixa para voltar a mostrar todas as tabelas. Uma pesquisa longa pode devolver resultados por páginas e a linha de estado indica quando ainda está a pesquisar ou pode estar incompleta.

Selecione **Árvore de colunas** para pesquisar a partir de uma janela própria. Cada tabela que tem a coluna abre-se com duas listas:

* **Alimentada por** — as tabelas que fornecem a coluna
* **Alimenta** — as tabelas que a coluna passa a alimentar

Um assistente de IA ligado por MCP encontra as mesmas tabelas com `table_find(column=...)`, fazendo corresponder o nome inteiro ou parte dele.


### Pesquisar valores

Para descobrir que tabelas contêm um valor, escolha **Pesquisar valores nos dados… (lento)** no menu **Ações** do separador **Tabelas**, ou clique com o botão direito numa tabela e escolha-o para procurar apenas nessa tabela. Introduza o valor, escolha **Contém** para corresponder a parte de um valor e selecione **Pesquisar**. Cada tabela que contém o valor é listada com as colunas em que aparece e alguns dos valores correspondentes. Faça duplo clique numa tabela, ou prima Enter sobre ela, para a abrir no Explorador de tabelas. Uma coluna abre a tabela filtrada pelas linhas correspondentes. Se a caixa de pesquisa de colunas contiver texto, este preenche o valor a procurar.

Antes de pesquisar, tenha em atenção que:

* A pesquisa lê todas as linhas de todas as tabelas pesquisadas, pelo que pode ser muito lenta e usar muitos recursos do armazém. A janela avisa-o e os botões de pesquisa ficam desativados até a pesquisa terminar.
* Vê apenas as linhas que já poderia abrir. A segurança ao nível da linha aplica-se a todas as pesquisas.
* O histórico de consultas do seu armazém regista os valores que pesquisa.
* A pesquisa abrange as colunas de texto das tabelas. As tabelas que ainda não foram criadas são ignoradas e nomeadas num aviso.
* Os resultados vêm por páginas. Quando a linha de estado indica que a pesquisa parou mais cedo, escolha **Pesquisar mais** para continuar com as tabelas ainda não pesquisadas.

Um assistente de IA ligado por MCP usa `table_value_search`. Devolve as tabelas e colunas que contêm o valor, nunca os valores em si. Quando pede ao assistente de IA num projeto que encontre um valor, o Weave envia os nomes das tabelas e colunas correspondentes ao fornecedor do modelo de linguagem.



## Importar um ficheiro CSV

**Para transformar um ficheiro CSV numa nova tabela neste projeto:**

1. Arraste o ficheiro do seu computador para a lista **Tabelas** do projeto, ou escolha **Novo** > **Tabela a partir de ficheiro CSV** na barra de ferramentas e largue o ficheiro na caixa ou clique em **Escolher um ficheiro CSV**.
2. O PlaidCloud carrega o ficheiro para a sua **Personal Temp Drive**, ou para a **Temp Drive** da área de trabalho se não tiver uma, e importa-o para uma nova tabela no nível superior da lista, com o nome do ficheiro: `Sales Data.csv` passa a `sales_data`. Se o projeto já tiver uma tabela com esse nome, a nova recebe um número, como `sales_data_2`.
3. A lista é atualizada com a nova tabela selecionada, e **Os seus dados num relance** abre-se sobre ela. Consulte [Comece com o seu próprio CSV](/pt-pt/get-started/quickstart/#comece-com-o-seu-próprio-csv) para ver o que o painel mostra.

Só são aceites ficheiros terminados em `.csv`. É necessária permissão para criar tabelas e para escrever no armazenamento de documentos, e um projeto bloqueado não aceita um CSV até ser desbloqueado. Se a importação falhar, a janela indica o motivo e o seu projeto fica como estava. O PlaidCloud elimina o ficheiro carregado da unidade temporária quando a importação termina, quer tenha tido êxito ou não; se não o fizer, a unidade temporária elimina-o ao fim de um dia.

## Mover


**Para mover uma tabela:**


1. Arraste-a para a pasta onde pretende que fique

## Mudar o nome


**Para mudar o nome de uma tabela:**


1. Clique com o botão direito na tabela
2. Selecione a opção de mudar o nome
3. Escreva o novo nome e guarde-o
4. A tabela fica com o novo nome, mas mantém o seu identificador único original.

## Limpar


**Para limpar uma tabela:**


1. Selecione as tabelas na hierarquia ‘
2. Clique no botão de limpar na barra de ferramentas superior.

*Nota: pode limpar uma única tabela ou várias tabelas*



## Eliminar


**Para eliminar uma tabela:**


1. Selecione as tabelas na hierarquia
2. Clique no botão de eliminar na barra de ferramentas superior
3. A operação de eliminação verifica se a tabela está a ser usada por passos de fluxos de trabalho ou por Vistas. Se estiver, ser-lhe-á pedido que remova essas associações antes de a eliminação poder ocorrer.

*Nota: também pode forçar a eliminação da(s) tabela(s). A eliminação forçada da(s) tabela(s) deixa as referências quebradas, pelo que deve ser usada com moderação.*


### Última leitura

A janela de eliminação mostra quando a tabela foi lida pela última vez, por exemplo **Last read 3 days ago by** uma pessoa ou um passo, para que possa distinguir uma tabela que ninguém usa de uma que ainda está em uso. O PlaidCloud obtém esta informação do próprio histórico de consultas do seu armazém e exclui as leituras feitas pelas suas próprias tarefas de manutenção.

| Armazém | O que é necessário |
| --- | --- |
| Snowflake | As leituras provêm do Access History, que o Snowflake regista com um atraso até cerca de 3 horas. A função da ligação precisa da função de base de dados `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` na base de dados `SNOWFLAKE` também funciona). A edição Standard do Snowflake não tem Access History. |
| Databricks | As leituras provêm da tabela de linhagem, que o Databricks também regista com atraso, pelo que uma leitura recente pode ainda não aparecer. A identidade da ligação precisa de `USE CATALOG` em `system`, `USE SCHEMA` em `system.access` e `SELECT` em `system.access.table_lineage`. |
| PlaidCloud Lakehouse | O histórico de leituras ainda não está disponível. A janela mostra **Read history incomplete**. |

Quando liga o seu armazém, [a verificação da ligação](/pt-pt/guides/connections/external-lakehouse/#3-verificar-e-depois-utilizar) recomenda qualquer uma destas concessões que esteja em falta, cada uma com a instrução a executar. São recomendadas, não obrigatórias: sem elas o armazém liga-se na mesma e a janela mostra **Read history incomplete**.

Quando o PlaidCloud não consegue ler o histórico completo, a linha diz **Read history incomplete** e nunca comunica "no reads" em seu lugar. Qualquer pessoa com acesso SQL direto ao seu armazém pode definir uma etiqueta de sessão que altera a forma como as suas próprias leituras são rotuladas.

Um assistente de IA ligado por MCP obtém a mesma resposta com `table_describe(include=['last_read'])`.



## Ver as colunas de uma tabela


Selecionar uma tabela abre o respetivo painel de detalhes. A secção **Colunas** lista cada coluna com o seu **Tipo** e **Descrição**, vindo a descrição de **Propriedades da coluna**. Aponte para uma linha para ler uma descrição longa na íntegra.

Uma tabela que neste momento não está no armazém, porque os seus dados expiraram ou nenhum passo a criou, não tem colunas para listar. A secção di-lo e mostra quantas colunas a tabela tem. Execute um passo que escreva a tabela para as listar.


## Ver onde uma tabela é usada


Selecionar uma tabela abre o respetivo painel de detalhes, que lista os passos de fluxos de trabalho que lhe tocam:


* **Tabela criada por** — passos que escrevem na tabela
* **A tabela contribui para** — passos que leem a partir dela
* **Pode referenciar esta tabela** — passos que chegam a uma tabela através de uma variável que não pode ser resolvida. Esta secção só aparece quando existem esses passos.


Um passo pode indicar uma tabela diretamente ou chegar a ela através de um caminho que contém uma variável, como `/Periods/{period}/Sales`. Quando essa variável tem um valor atual, o passo aparece nas duas primeiras listas com um ícone de informação ao lado. Passe o cursor sobre a linha para ver o caminho tal como o passo o armazena.


Trate essas linhas como a resposta mais fraca que são. Descrevem o que uma execução iniciada agora tocaria — não tudo o que alguma vez tocou na tabela. Altere a variável e é lida uma tabela diferente.


Algumas variáveis não podem ser resolvidas. Ou nada definiu a variável, ou o valor que uma execução usa não provém do que está armazenado — um Workflow Loop obtém as suas variáveis de dados à medida que itera, um passo Set Variable atribui durante a execução, uma macro recebe as suas variáveis do passo que a chama, e uma execução iniciada por um sensor transporta os detalhes desse sensor. Em cada caso, o que fica armazenado entre execuções é o que sobrou da última, e não um valor em que confiar. Em vez de resolver essas variáveis para uma tabela que pode ser a errada, o PlaidCloud lista os passos pelo nome em **Pode referenciar esta tabela**, com a variável que não conseguiu resolver, para que os possa abrir e verificar.


Um passo que a sua função não pode ver continua listado, para que saiba que a tabela está em uso, mas sem o seu nome ou fluxo de trabalho, e não o pode abrir. Continua a contar quando elimina a tabela. Um passo que pode ver é listado sem qualquer fluxo de trabalho que a sua função oculte. Nada é ocultado de um Arquiteto.


*Nota: quando elimina tabelas da lista **Tabelas**, um passo que chega a uma tabela através de um caminho, com ou sem variável, conta como a usando, mesmo quando a respetiva variável não pode ser resolvida. A janela de eliminação lista o passo, e a eliminação só avança se a forçar.*



## Criar uma nova estrutura de diretórios


**Para acrescentar uma nova pasta:**


1. Clique no botão Nova pasta na barra de ferramentas

**Para acrescentar uma pasta a uma pasta existente:**


1. Clique com o botão direito na pasta
2. Selecione Nova pasta


## Ver dados (Explorador de tabelas)


Os dados das tabelas são vistos através do Explorador de dados. O Explorador de dados oferece uma vista em grelha dos dados, bem como um resumo coluna a coluna de valores e estatísticas. Estão disponíveis a filtragem por apontar e clicar e a exportação para formatos de ficheiro familiares. As seleções de filtros também podem ser guardadas como um passo Extract utilizável num fluxo de trabalho.



## Publicar uma tabela para relatórios


As Visualizações em painéis de controlo estão propositadamente limitadas a tabelas que foram publicadas. Ao publicar uma tabela, pode indicar um nome único que distinga os dados. Isto pode ser útil quando a tabela tem um nome mais obscuro na parte do fluxo de trabalho que a gerou, mas precisa de um nome mais claro para quem cria painéis de controlo.


As tabelas publicadas não têm caminhos associados. Aparecem como uma lista de tabelas para utilização na área de painéis de controlo.



## Marcar uma tabela para funções de visualização


A visualização de tabelas por várias funções pode ser controlada clicando nas caixas de seleção Explorador ou Gestor. Se for necessário atualizar várias tabelas, selecione as tabelas na hierarquia e selecione a função de visualização pretendida no menu Ações da barra de ferramentas superior.



## Memorandos para descrever o conteúdo das tabelas


Acrescente um memorando a uma tabela para ajudar a compreender os dados.



## Ver a forma, o tamanho e a hora da última atualização de uma tabela


O número de linhas, colunas e o tamanho dos dados de cada tabela são apresentados na hierarquia de tabelas. Para tabelas muito grandes (vários milhões de linhas), a contagem de linhas pode ser estimada e é apresentado um indicador de contagem aproximada de linhas.



## Ver atributos adicionais de uma tabela


**Para ver e editar outros atributos de uma tabela:**


1. Selecione uma tabela
2. Clique em ver o formulário de contexto da tabela à direita.


## Duplicar uma tabela


**Para duplicar uma tabela:**


1. Selecione a tabela
2. Clique no botão de duplicar na barra de ferramentas superior.


## Criar uma aplicação Panel a partir de uma tabela


Selecione uma tabela ou vista e escolha **Criar aplicação Panel** no menu **Novo** ou no menu de contexto. A caixa de diálogo **Nova aplicação Studio** abre-se com o projeto e a tabela já escolhidos. Dê um nome à aplicação e escolha **Criar**, e o Panel Studio abre-a com o Weave pronto a criar a primeira página. O comando está disponível quando seleciona uma única tabela ou vista, tem acesso de edição ao projeto e o projeto não é só de leitura. Consulte [Criar uma aplicação Panel](/pt-pt/guides/panel-apps/creating/#começar-a-partir-de-uma-tabela).


## Ver o que as tabelas armazenam


A lista **Tabelas** mostra as colunas **Dados atuais**, **Histórico** e **Nota** ao lado do tamanho de cada tabela, e **Dias de viagem no tempo** depois delas. Acima da lista, uma linha indica o total do projeto: quanto armazena e quanto disso são dados atuais e quanto é histórico. Uma tabela que o PlaidCloud ainda não mediu não tem tamanhos.

Escolha **Armazenamento** na barra de ferramentas para abrir a janela **Armazenamento** do projeto, com sugestões para libertar espaço e as definições de time travel. Consulte [Gerir o armazenamento](/pt-pt/guides/projects/managing-storage/#a-janela-armazenamento-de-um-projeto).


## Criar um editor de dados a partir de uma tabela


Pode transformar uma tabela num editor de dados configurado num só passo — selecione a tabela e escolha **Criar editor de dados a partir da tabela** no menu **Novo** ou no menu de contexto. O PlaidCloud examina as colunas da tabela e pré-constrói os controlos de entrada do editor. Consulte [Criar um editor de dados a partir de uma tabela](/pt-pt/guides/projects/managing-data-editors/#criar-um-editor-de-dados-a-partir-de-uma-tabela) para mais detalhes.
