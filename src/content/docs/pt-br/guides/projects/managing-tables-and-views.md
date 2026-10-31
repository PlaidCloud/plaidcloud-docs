---
title: Gerenciar tabelas e visões
description: Gerencie tabelas e visões em projetos do PlaidCloud, incluindo criação, configuração, permissões e organização dos objetos de dados.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

O PlaidCloud oferece a capacidade de organizar e gerenciar tabelas, incluindo rótulos. As tabelas estão disponíveis para todos os fluxos de trabalho de um projeto e têm muitas ferramentas e opções.


Além das tabelas, o PlaidCloud também oferece Visões baseadas nos dados das tabelas. O uso de Visões permite atualizações instantâneas quando ocorrem alterações nas tabelas subjacentes, além de economizar espaço de armazenamento de dados.



As opções incluem:


* A mesma tabela pode existir em vários caminhos da hierarquia (hierarquias alternativas)
* As tabelas podem receber tags para facilitar a pesquisa e a inclusão em processos do PlaidCloud
* As tabelas podem ter versões
* As tabelas podem ser publicadas para ficarem disponíveis para Visualizações de painel

O PlaidCloud usa um sistema baseado em caminhos para organizar as tabelas, como o que você usaria para navegar por uma série de pastas, permitindo uma organização das tabelas mais flexível e lógica. Com esse sistema, as tabelas podem ser movidas dentro de uma hierarquia, ou é possível criar várias referências a uma tabela a partir de locais diferentes da hierarquia (hierarquias alternativas). A capacidade de gerenciar tabelas por esse método permite que a estrutura reflita necessidades operacionais, de geração de relatórios e de controle.



## Localizar tabelas


Use a caixa de filtro no canto inferior esquerdo da hierarquia para pesquisar nomes e rótulos de tabelas. As correspondências aparecem na hierarquia acima.


### Por fluxo de trabalho

A pasta **Por fluxo de trabalho** no final da guia **Tabelas** agrupa as tabelas sob cada fluxo de trabalho que as lê ou grava. Abra um fluxo de trabalho para ver suas tabelas. A pasta é uma visão das mesmas tabelas, portanto você não pode mover nem copiar nada a partir dela.


### Por coluna

Digite o nome de uma coluna na caixa de pesquisa de colunas na guia **Tabelas** e pressione Enter, ou selecione a lupa ao lado dela, para mostrar apenas as tabelas que têm uma coluna com esse nome. A pesquisa lê nomes de colunas, não os dados, por isso é rápida. Selecione **Contém** para corresponder a parte do nome de uma coluna em vez do nome inteiro. Limpe a caixa para mostrar todas as tabelas novamente. Uma pesquisa longa pode retornar em páginas, e a linha de status informa quando ela ainda está pesquisando ou pode estar incompleta.

Selecione **Árvore de colunas** para pesquisar em uma janela própria. Cada tabela que tem a coluna se abre em duas listas:

* **Alimentada por** — as tabelas que fornecem a coluna
* **Alimenta** — as tabelas que a coluna passa a alimentar

Um assistente de IA conectado por MCP encontra as mesmas tabelas com `table_find(column=...)`, correspondendo ao nome inteiro ou a parte dele.


### Pesquisar valores

Para descobrir quais tabelas contêm um valor, escolha **Buscar valores nos dados… (lento)** no menu **Ações** da guia **Tabelas**, ou clique com o botão direito em uma tabela e escolha essa opção para pesquisar somente nessa tabela. Insira o valor, escolha **Contém** para corresponder a parte de um valor e selecione **Pesquisar**. Cada tabela que contém o valor é listada com as colunas em que ele aparece e alguns dos valores correspondentes. Clique duas vezes em uma tabela, ou pressione Enter sobre ela, para abri-la no Explorador de tabelas. Uma coluna abre a tabela filtrada pelas linhas correspondentes. Se a caixa de pesquisa de colunas contiver texto, ele preenche o valor a ser encontrado.

Antes de pesquisar, saiba que:

* A pesquisa lê todas as linhas de todas as tabelas pesquisadas, portanto pode ser muito lenta e usar muitos recursos do data warehouse. A janela avisa você, e os botões de pesquisa ficam desativados até que uma pesquisa termine.
* Você vê apenas as linhas que já poderia abrir. A segurança em nível de linha se aplica a toda pesquisa.
* O histórico de consultas do seu data warehouse registra os valores que você pesquisa.
* A pesquisa abrange as colunas de texto das tabelas. As tabelas que não foram criadas são ignoradas e nomeadas em um aviso.
* Os resultados vêm em páginas. Quando a linha de status informa que a pesquisa parou antes do fim, escolha **Pesquisar mais** para continuar com as tabelas ainda não pesquisadas.

Um assistente de IA conectado por MCP usa `table_value_search`. Ele retorna as tabelas e colunas que contêm o valor, nunca os valores em si. Quando você pede ao assistente de IA em um projeto que encontre um valor, o Weave envia ao provedor do modelo de linguagem os nomes das tabelas e colunas correspondentes.



## Importar um arquivo CSV

**Para transformar um arquivo CSV em uma nova tabela neste projeto:**

1. Arraste o arquivo do seu computador para a lista **Tabelas** do projeto, ou escolha **Novo** > **Tabela a partir de arquivo CSV** na barra de ferramentas e solte o arquivo na caixa ou clique em **Escolher um arquivo CSV**.
2. O PlaidCloud carrega o arquivo para o seu **Personal Temp Drive**, ou para o **Temp Drive** do espaço de trabalho se você não tiver um, e o importa para uma nova tabela no nível superior da lista, com o nome do arquivo: `Sales Data.csv` se torna `sales_data`. Se o projeto já tiver uma tabela com esse nome, a nova recebe um número, como `sales_data_2`.
3. A lista é atualizada com a nova tabela selecionada, e **Seus dados em resumo** abre sobre ela. Consulte [Comece com seu próprio CSV](/pt-br/get-started/quickstart/#comece-com-seu-próprio-csv) para ver o que o painel mostra.

Somente arquivos terminados em `.csv` são aceitos. Você precisa de permissão para criar tabelas e gravar no armazenamento de documentos, e um projeto bloqueado não aceita um CSV até ser desbloqueado. Se a importação falhar, a janela informa o motivo e seu projeto permanece como estava. O PlaidCloud exclui o arquivo carregado da unidade temporária quando a importação termina, tenha ela sucesso ou não; caso isso não aconteça, a unidade temporária o exclui após um dia.

## Mover


**Para mover uma tabela:**


1. Arraste-a para a pasta em que você deseja que ela fique

## Renomear


**Para renomear uma tabela:**


1. Clique com o botão direito na tabela
2. Selecione a opção de renomear
3. Digite o novo nome e salve
4. A tabela agora está renomeada, mas mantém seu identificador exclusivo original.

## Limpar


**Para limpar uma tabela:**


1. Selecione as tabelas na hierarquia ‘
2. Clique no botão de limpar na barra de ferramentas superior.

*Observação: você pode limpar uma única tabela ou várias tabelas*



## Excluir


**Para excluir uma tabela:**


1. Selecione as tabelas na hierarquia
2. Clique no botão de excluir na barra de ferramentas superior
3. A operação de exclusão verifica se a tabela está em uso por etapas de fluxo de trabalho ou Visões. Se estiver, você será solicitado a remover essas associações antes que a exclusão possa ocorrer.

*Observação: você também pode forçar a exclusão das tabelas. A exclusão forçada das tabelas deixa referências quebradas, portanto deve ser usada com moderação.*


### Última leitura

A janela de exclusão mostra quando a tabela foi lida pela última vez, por exemplo **Last read 3 days ago by** uma pessoa ou etapa, para que você possa distinguir uma tabela que ninguém usa de uma que ainda está em uso. O PlaidCloud obtém isso do próprio histórico de consultas do seu data warehouse e exclui as leituras feitas por suas próprias tarefas de manutenção.

| Data warehouse | O que é necessário |
| --- | --- |
| Snowflake | As leituras vêm do Access History, que o Snowflake registra com até cerca de 3 horas de atraso. A função da conexão precisa da função de banco de dados `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` no banco de dados `SNOWFLAKE` também funciona). A edição Standard do Snowflake não tem Access History. |
| Databricks | As leituras vêm da tabela de linhagem, que o Databricks também registra com atraso, portanto uma leitura recente pode ainda não aparecer. A identidade da conexão precisa de `USE CATALOG` em `system`, `USE SCHEMA` em `system.access` e `SELECT` em `system.access.table_lineage`. |
| PlaidCloud Lakehouse | O histórico de leituras ainda não está disponível. A janela mostra **Read history incomplete**. |

Quando você conecta seu data warehouse, [a verificação da conexão](/pt-br/guides/connections/external-lakehouse/#3-verificar-e-usar) recomenda qualquer uma dessas concessões que esteja faltando, cada uma com a instrução a ser executada. Elas são recomendadas, não obrigatórias: sem elas, o data warehouse se conecta e a janela mostra **Read history incomplete**.

Quando o PlaidCloud não consegue ler o histórico inteiro, a linha diz **Read history incomplete** e nunca informa "nenhuma leitura" no lugar. Qualquer pessoa com acesso direto por SQL ao seu data warehouse pode definir uma tag de sessão que altera como suas próprias leituras são rotuladas.

Um assistente de IA conectado por MCP obtém a mesma resposta com `table_describe(include=['last_read'])`.



## Ver as colunas de uma tabela


Ao selecionar uma tabela, seu painel de detalhes é aberto. A seção **Colunas** lista cada coluna com seu **Tipo** e sua **Descrição**, que vem de **Propriedades da coluna**. Aponte para uma linha para ler uma descrição longa por inteiro.

Uma tabela que não está no data warehouse no momento, porque seus dados expiraram ou nenhuma etapa a criou, não tem colunas para listar. A seção informa isso e mostra quantas colunas a tabela tem. Execute uma etapa que grave a tabela para listá-las.


## Ver onde uma tabela é usada


Ao selecionar uma tabela, seu painel de detalhes é aberto e lista as etapas de fluxo de trabalho que a utilizam:


* **Tabela criada por** — etapas que gravam na tabela
* **Tabela contribui para** — etapas que leem dela
* **Pode referenciar esta tabela** — etapas que alcançam uma tabela por meio de uma variável que não pode ser resolvida. Esta seção só aparece quando há essas etapas.


Uma etapa pode nomear uma tabela diretamente ou alcançá-la por meio de um caminho que contém uma variável, como `/Periods/{period}/Sales`. Quando essa variável tem um valor atual, a etapa aparece nas duas primeiras listas com um ícone de informação ao lado. Passe o mouse sobre a linha para ver o caminho como a etapa o armazena.


Trate essas linhas como a resposta mais fraca que elas são. Elas descrevem o que uma execução iniciada agora utilizaria — não tudo o que já utilizou a tabela. Altere a variável e uma tabela diferente será lida.


Algumas variáveis não podem ser resolvidas. Ou nada definiu a variável, ou o valor que uma execução usa não vem do que está armazenado — uma etapa Workflow Loop obtém suas variáveis dos dados à medida que itera, uma etapa Set Variable atribui durante a execução, uma macro recebe suas variáveis da etapa que a chama, e uma execução iniciada por um sensor carrega os detalhes do próprio sensor. Em cada caso, o que está armazenado entre execuções é o que sobrou da última, e não um valor confiável. Em vez de resolver essas variáveis para uma tabela que pode ser a errada, o PlaidCloud lista as etapas pelo nome em **Pode referenciar esta tabela**, com a variável que não pôde resolver, para que você as abra e verifique.


Uma etapa que sua função não pode ver ainda é listada, para que você saiba que a tabela está em uso, mas sem seu nome ou fluxo de trabalho, e você não pode abri-la. Ela continua contando quando você exclui a tabela. Uma etapa que você pode ver é listada sem qualquer fluxo de trabalho que sua função oculte. Nada é ocultado de um Arquiteto.


*Observação: quando você exclui tabelas da lista **Tabelas**, uma etapa que alcança uma tabela por meio de um caminho, com ou sem variável, conta como usando-a, mesmo quando sua variável não pode ser resolvida. A janela de exclusão lista a etapa, e a exclusão só prossegue se você forçá-la.*



## Criar uma nova estrutura de diretórios


**Para adicionar uma nova pasta:**


1. Clique no botão Nova pasta na barra de ferramentas

**Para adicionar uma pasta a uma pasta existente:**


1. Clique com o botão direito na pasta
2. Selecione Nova pasta


## Visualizar dados (Explorador de tabelas)


Os dados da tabela são visualizados usando o Explorador de dados. O Explorador de dados fornece uma visualização em grade dos dados, além de um resumo coluna por coluna de valores e estatísticas. A filtragem por apontar e clicar e a exportação para formatos de arquivo conhecidos estão disponíveis. As seleções de filtro também podem ser salvas como uma etapa de extração utilizável em um fluxo de trabalho.



## Publicar tabela para relatórios


As Visualizações de painel são intencionalmente limitadas a tabelas que foram publicadas. Ao publicar uma tabela, você pode fornecer um nome exclusivo que possa distinguir os dados. Isso pode ser útil quando a tabela tem um nome mais obscuro na parte do fluxo de trabalho que a gerou, mas precisa de um nome mais claro para quem cria painéis.


As tabelas publicadas não têm caminhos associados. Elas aparecem como uma lista de tabelas para uso na área de painéis.



## Marcar tabela para funções de visualização


A visualização de tabelas por diversas funções pode ser controlada clicando nas caixas de seleção Explorador ou Gerente. Se várias tabelas precisarem ser atualizadas, selecione as tabelas na hierarquia e escolha a função de visualização desejada no menu Ações da barra de ferramentas superior.



## Memorandos para descrever o conteúdo da tabela


Adicione um memorando a uma tabela para ajudar a entender os dados.



## Ver formato, tamanho e hora da última atualização da tabela


O número de linhas, colunas e o tamanho dos dados de cada tabela são mostrados na hierarquia de tabelas. Para tabelas muito grandes (com milhões de linhas), a contagem de linhas pode ser estimada e um indicador de contagem aproximada de linhas será exibido.



## Ver outros atributos da tabela


**Para ver e editar outros atributos da tabela:**


1. Selecione uma tabela
2. Clique para ver o formulário de contexto da tabela à direita.


## Duplicar uma tabela


**Para duplicar uma tabela:**


1. Selecione a tabela
2. Clique no botão de duplicar na barra de ferramentas superior.


## Criar um aplicativo Panel a partir de uma tabela


Selecione uma tabela ou visão e escolha **Criar aplicativo Panel** no menu **Novo** ou no menu de contexto. A caixa de diálogo **Novo aplicativo Studio** é aberta com o projeto e a tabela já escolhidos. O aplicativo recebe o nome da tabela; altere-o se quiser e depois escolha **Criar**, e o Panel Studio o abre com o Weave pronto para criar sua primeira página. O comando fica disponível quando você seleciona uma única tabela ou visão, tem acesso de edição ao projeto e o projeto não é somente leitura. Consulte [Criar um aplicativo Panel](/pt-br/guides/panel-apps/creating/#começar-a-partir-de-uma-tabela).


## Ver o que as tabelas armazenam


A lista **Tabelas** mostra as colunas **Dados atuais**, **Histórico**, **Dias de Time Travel** e **Observação** ao lado do tamanho de cada tabela. **Dias de Time Travel** é a configuração da própria tabela; **1** significa que ela usa o padrão do projeto. A barra de status abaixo da lista mostra o total do projeto: quanto ele armazena e quanto disso são dados atuais e quanto é histórico. Os tamanhos marcados como **Estimado** vêm do formato da tabela até que o PlaidCloud o meça.

Escolha **Armazenamento** na barra de ferramentas para abrir a janela **Armazenamento** do projeto, com sugestões para liberar espaço e as configurações de time travel. Consulte [Gerenciar o armazenamento](/pt-br/guides/projects/managing-storage/#a-janela-armazenamento-de-um-projeto).


## Criar um editor de dados a partir de uma tabela


Você pode transformar uma tabela em um editor de dados configurado em uma única etapa — selecione a tabela e escolha **Criar editor de dados a partir da tabela** no menu **Novo** ou no menu de contexto. O PlaidCloud examina as colunas da tabela e pré-configura os controles de entrada do editor. Consulte [Criar um editor de dados a partir de uma tabela](/pt-br/guides/projects/managing-data-editors/#criar-um-editor-de-dados-a-partir-de-uma-tabela) para obter detalhes.
