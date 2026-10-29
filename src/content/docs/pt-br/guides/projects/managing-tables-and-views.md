---
title: Gerenciar tabelas e visões
description: Gerencie tabelas e visões nos projetos do PlaidCloud, incluindo criação, configuração, permissões e organização dos objetos de dados.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-tables-and-views.md
---

O PlaidCloud permite organizar e gerenciar tabelas, inclusive com rótulos. As tabelas ficam disponíveis para todos os fluxos de trabalho de um projeto e têm muitas ferramentas e opções.


Além das tabelas, o PlaidCloud também oferece visões baseadas nos dados das tabelas. O uso de visões permite atualizações instantâneas quando ocorrem alterações nas tabelas subjacentes, além de economizar espaço de armazenamento de dados.



As opções incluem:


* A mesma tabela pode existir em vários caminhos da hierarquia (hierarquias alternativas)
* As tabelas podem receber marcas, para facilitar a pesquisa e a inclusão em processos do PlaidCloud
* As tabelas podem ter versões
* As tabelas podem ser publicadas para ficarem disponíveis nas visualizações de painel

O PlaidCloud usa um sistema baseado em caminhos para organizar as tabelas, como você usaria para navegar por uma série de pastas, o que permite uma organização mais flexível e lógica das tabelas. Com esse sistema, as tabelas podem ser movidas dentro de uma hierarquia, ou é possível criar várias referências a uma tabela a partir de locais diferentes da hierarquia (hierarquias alternativas). A capacidade de gerenciar tabelas dessa forma permite que a estrutura reflita as necessidades operacionais, de relatórios e de controle.



## Encontrar tabelas


Use a caixa de filtro no canto inferior esquerdo da hierarquia para pesquisar nomes e rótulos de tabelas. As correspondências aparecem na hierarquia acima.


### Por fluxo de trabalho

A pasta **By Workflow**, no fim da guia **Tabelas**, agrupa as tabelas sob cada fluxo de trabalho que as lê ou grava. Abra um fluxo de trabalho para ver suas tabelas. A pasta é uma visão das mesmas tabelas, então você não pode mover nem copiar nada a partir dela.


### Por coluna

Digite o nome de uma coluna na caixa de pesquisa de colunas da guia **Tabelas** para mostrar apenas as tabelas que têm uma coluna com esse nome. Selecione **Contém** para corresponder a parte do nome de uma coluna, em vez do nome inteiro. Limpe a caixa para mostrar todas as tabelas novamente. Uma pesquisa longa pode retornar em páginas, e a linha de status informa quando ela ainda está pesquisando ou pode estar incompleta.

Selecione **Column Tree** para pesquisar em uma janela própria. Cada tabela que tem a coluna abre com duas listas:

* **Fed by** — as tabelas que fornecem a coluna
* **Feeds** — as tabelas que a coluna passa a alimentar

Um assistente de IA conectado via MCP encontra as mesmas tabelas com `table_find(column=...)`, correspondendo ao nome inteiro ou a parte dele.


### Pesquisar valores

Para descobrir quais tabelas contêm um valor, selecione **Search Values** na guia **Tabelas** ou clique com o botão direito em uma tabela e escolha **Search Value** para procurar somente nessa tabela. Insira o valor, escolha **Contém** para corresponder a parte de um valor e selecione **Pesquisar**. Cada tabela que contém o valor é listada com as colunas em que ele aparece e alguns dos valores correspondentes.

Antes de pesquisar, saiba que:

* Você vê apenas as linhas que já poderia abrir. A segurança em nível de linha se aplica a toda pesquisa.
* O histórico de consultas do seu data warehouse registra os valores que você pesquisa.
* A pesquisa abrange as colunas de texto das tabelas. As tabelas que não foram construídas são ignoradas e citadas em um aviso.
* Os resultados vêm em páginas. Quando a linha de status informa que a pesquisa parou mais cedo, escolha **Search more** para continuar com as tabelas ainda não pesquisadas.

Um assistente de IA conectado via MCP usa `table_value_search`. Ele retorna as tabelas e colunas que contêm o valor, nunca os valores em si. Quando você pede ao assistente de IA em um projeto para encontrar um valor, o Weave envia os nomes das tabelas e colunas correspondentes ao provedor do modelo de linguagem.



## Importar um arquivo CSV

**Para transformar um arquivo CSV em uma nova tabela neste projeto:**

1. Arraste o arquivo do seu computador para a lista **Tabelas** do projeto ou escolha **Novo** > **Tabela a partir de arquivo CSV** na barra de ferramentas e solte o arquivo na caixa ou clique em **Escolher um arquivo CSV**.
2. O PlaidCloud envia o arquivo para o seu **Personal Temp Drive**, ou para o **Temp Drive** do espaço de trabalho se você não tiver um, e o importa para uma nova tabela no nível superior da lista, com o nome do arquivo: `Sales Data.csv` se torna `sales_data`. Se o projeto já tiver uma tabela com esse nome, a nova recebe um número, como `sales_data_2`.
3. A lista é atualizada com a nova tabela selecionada, e **Seus dados em resumo** abre nela. Consulte [Comece com seu próprio CSV](/pt-br/get-started/quickstart/#comece-com-seu-próprio-csv) para ver o que o painel mostra.

Somente arquivos terminados em `.csv` são aceitos. Você precisa de permissão para criar tabelas e gravar no armazenamento de documentos, e um projeto bloqueado não aceita um CSV até ser desbloqueado. Se a importação falhar, a janela informa o motivo e o seu projeto permanece como estava. O PlaidCloud exclui o arquivo enviado do drive temporário assim que a importação termina, com sucesso ou não; caso contrário, o drive temporário o exclui após um dia.

## Mover


**Para mover uma tabela:**


1. Arraste-a para a pasta onde você quer que ela fique

## Renomear


**Para renomear uma tabela:**


1. Clique com o botão direito na tabela
2. Selecione a opção de renomear
3. Digite o novo nome e salve
4. A tabela agora está renomeada, mas mantém o identificador exclusivo original.

## Limpar


**Para limpar uma tabela:**


1. Selecione as tabelas na hierarquia
2. Clique no botão de limpar na barra de ferramentas superior.

*Observação: você pode limpar uma única tabela ou várias tabelas*



## Excluir


**Para excluir uma tabela:**


1. Selecione as tabelas na hierarquia
2. Clique no botão de excluir na barra de ferramentas superior
3. A operação de exclusão verifica se a tabela está em uso por etapas de fluxo de trabalho ou visões. Se estiver, será solicitado que você remova essas associações antes que a exclusão possa ocorrer.

*Observação: você também pode forçar a exclusão da(s) tabela(s). A exclusão forçada deixa as referências quebradas, portanto deve ser usada com moderação.*


### Última leitura

A janela de exclusão mostra quando a tabela foi lida pela última vez, por exemplo **Last read 3 days ago by** uma pessoa ou etapa, para que você distinga uma tabela que ninguém usa de uma que ainda está em uso. O PlaidCloud obtém isso do próprio histórico de consultas do seu data warehouse e deixa de fora as leituras feitas por suas próprias rotinas internas.

| Data warehouse | O que é necessário |
| --- | --- |
| Snowflake | As leituras vêm do Access History, que o Snowflake registra com até cerca de 3 horas de atraso. A função da conexão precisa da função de banco de dados `SNOWFLAKE.GOVERNANCE_VIEWER` (`IMPORTED PRIVILEGES` no banco de dados `SNOWFLAKE` também funciona). A edição Standard do Snowflake não tem Access History. |
| Databricks | As leituras vêm da tabela de linhagem, que o Databricks também registra com atraso, então uma leitura recente pode ainda não aparecer. A identidade da conexão precisa de `USE CATALOG` em `system`, `USE SCHEMA` em `system.access` e `SELECT` em `system.access.table_lineage`. |
| PlaidCloud Lakehouse | O histórico de leituras ainda não está disponível. A janela mostra **Read history incomplete**. |

Quando você conecta seu data warehouse, [a verificação da conexão](/pt-br/guides/connections/external-lakehouse/#3-verificar-e-usar) recomenda qualquer uma dessas concessões que esteja ausente, cada uma com a instrução a executar. Elas são recomendadas, não obrigatórias: sem elas, o data warehouse se conecta e a janela mostra **Read history incomplete**.

Quando o PlaidCloud não consegue ler o histórico inteiro, a linha diz **Read history incomplete** e nunca informa "nenhuma leitura" no lugar. Qualquer pessoa com acesso SQL direto ao seu data warehouse pode definir uma marca de sessão que altera como as próprias leituras dela são rotuladas.

Um assistente de IA conectado via MCP obtém a mesma resposta em `table_describe(include=['last_read'])`.



## Ver onde uma tabela é usada


Selecionar uma tabela abre seu painel de detalhes, que lista as etapas de fluxo de trabalho que a utilizam:


* **Tabela criada por** — etapas que gravam na tabela
* **Tabela contribui para** — etapas que leem dela
* **Pode referenciar esta tabela** — etapas que chegam a uma tabela por meio de uma variável que não pode ser resolvida. Esta seção só aparece quando há etapas assim.


Uma etapa pode nomear uma tabela diretamente ou chegar a ela por um caminho que contém uma variável, como `/Periods/{period}/Sales`. Quando essa variável tem um valor atual, a etapa aparece nas duas primeiras listas com um ícone de informação ao lado. Passe o ponteiro sobre a linha para ver o caminho como a etapa o armazena.


Trate essas linhas como a resposta mais fraca que são. Elas descrevem o que uma execução iniciada agora tocaria, não tudo o que já tocou a tabela. Mude a variável e uma tabela diferente é lida.


Algumas variáveis não podem ser resolvidas. Ou nada definiu a variável, ou o valor que uma execução usa não vem do que está armazenado: um Workflow Loop obtém suas variáveis dos dados à medida que itera, uma etapa Set Variable atribui durante a execução, uma macro recebe suas variáveis da etapa que a chama, e uma execução iniciada por um sensor carrega os próprios detalhes desse sensor. Em cada caso, o que fica armazenado entre as execuções é o resto da última, e não um valor confiável. Em vez de resolver essas variáveis para uma tabela que pode ser a errada, o PlaidCloud lista as etapas pelo nome em **Pode referenciar esta tabela**, com a variável que não conseguiu resolver, para que você possa abri-las e conferir.


Uma etapa que a sua função não pode ver ainda é listada, para que você saiba que a tabela está em uso, mas sem o nome ou o fluxo de trabalho dela, e você não pode abri-la. Ela ainda conta quando você exclui a tabela. Uma etapa que você pode ver é listada sem nenhum fluxo de trabalho que a sua função oculte. Nada é ocultado de um Arquiteto.


*Observação: quando você exclui tabelas da lista **Tabelas**, uma etapa que chega a uma tabela por um caminho, com ou sem variável, conta como a utilizando, mesmo quando sua variável não pode ser resolvida. A janela de exclusão lista a etapa, e a exclusão só prossegue se você a forçar.*



## Criar uma nova estrutura de diretórios


**Para adicionar uma nova pasta:**


1. Clique no botão Nova pasta na barra de ferramentas

**Para adicionar uma pasta a uma pasta existente:**


1. Clique com o botão direito na pasta
2. Selecione Nova pasta


## Visualizar dados (Explorador de tabelas)


Os dados da tabela são visualizados no Data Explorer. O Data Explorer oferece uma visualização em grade dos dados, além de um resumo coluna a coluna de valores e estatísticas. Estão disponíveis a filtragem por apontar e clicar e a exportação para formatos de arquivo conhecidos. As seleções de filtro também podem ser salvas como uma etapa Extract utilizável em um fluxo de trabalho.



## Publicar tabela para relatórios


As visualizações de painel são limitadas, de propósito, a tabelas que foram publicadas. Ao publicar uma tabela, você pode fornecer um nome exclusivo que distinga os dados. Isso pode ser útil quando a tabela tem um nome mais obscuro na parte do fluxo de trabalho que a gerou, mas precisa de um nome mais claro para quem cria painéis.


As tabelas publicadas não têm caminhos associados. Elas aparecem como uma lista de tabelas para uso na área de painéis.



## Marcar tabela para funções de visualização


A visualização de tabelas por diversas funções pode ser controlada clicando nas caixas de seleção Explorador ou Gerente. Se várias tabelas precisarem ser atualizadas, selecione as tabelas na hierarquia e selecione a função de visualização desejada no menu Ações da barra de ferramentas superior.



## Memorandos para descrever o conteúdo da tabela


Adicione um memorando a uma tabela para ajudar a entender os dados.



## Ver formato, tamanho e hora da última atualização da tabela


O número de linhas, colunas e o tamanho dos dados de cada tabela são mostrados na hierarquia de tabelas. Para tabelas muito grandes (vários milhões de linhas), a contagem de linhas pode ser estimada e um indicador de contagem aproximada de linhas será exibido.



## Ver atributos adicionais da tabela


**Para ver e editar outros atributos da tabela:**


1. Selecione uma tabela
2. Clique para ver o formulário de contexto da tabela à direita.


## Duplicar uma tabela


**Para duplicar uma tabela:**


1. Selecione a tabela
2. Clique no botão de duplicar na barra de ferramentas superior.


## Criar um editor de dados a partir de uma tabela


Você pode transformar uma tabela em um editor de dados configurado em uma única etapa: selecione a tabela e escolha **Criar editor de dados a partir da tabela** no menu **Novo** ou no menu do botão direito. O PlaidCloud examina as colunas da tabela e pré-constrói os controles de entrada do editor. Consulte [Criar um editor de dados a partir de uma tabela](/pt-br/guides/projects/managing-data-editors/#criar-um-editor-de-dados-a-partir-de-uma-tabela) para ver os detalhes.
