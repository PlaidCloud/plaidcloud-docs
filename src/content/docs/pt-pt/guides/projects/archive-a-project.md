---
title: Arquivar um projeto
description: Arquive projetos do PlaidCloud para preservar o trabalho concluído, libertar recursos da área de trabalho e manter um ambiente de projetos organizado.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/archive-a-project.md
---

## Criar um arquivo


Os projetos contêm normalmente processos e lógica críticos, que é importante arquivar. Se alguma vez precisar de repor o projeto num determinado estado, é essencial dispor de arquivos. 



O PlaidCloud permite arquivar projetos em qualquer momento. A criação de arquivos complementa o rastreio pontual integrado do PlaidCloud, permitindo capturar momentos específicos. Isto pode ser particularmente útil antes de uma alteração importante ou para registar para a posteridade o estado exato de um ambiente de produção.



**Cópia de segurança completa**: inclui todas as tabelas de dados de um projeto. O arquivo pode ser bastante grande, consoante o volume de dados do projeto.


**Cópia de segurança parcial:** pode ser utilizada se todos os dados do projeto puderem ser obtidos a partir de outras origens. Nesse caso, não é necessário arquivar os dados do projeto e mantê-los noutro local. Os arquivos parciais poupam tempo e espaço de armazenamento na criação do arquivo.



Para arquivar um projeto:


1. Abra o Analyze
2. Selecione o separador “Projetos”
3. Selecione o projeto e, em seguida, escolha **Exportar arquivo do projeto** no menu **Ações** (ou clique com o botão direito do rato no projeto e escolha **Exportar arquivo do projeto**)

A janela indica na barra de título o projeto que vai arquivar, para que possa confirmar que escolheu o correto antes de começar.

### Enquanto o arquivo é executado

A janela de exportação fecha-se assim que o PlaidCloud aceita o pedido, e uma janela de progresso acompanha o arquivo a partir daí. Pode deixar essa janela de progresso aberta para acompanhar a operação, ou enviá-la para segundo plano e continuar a trabalhar — o arquivo é executado na plataforma de qualquer forma, e fechar a janela de progresso não o interrompe.

Uma notificação informa como terminou: que o arquivo foi gravado, que tabelas foram incluídas sem os respetivos dados ou, se falhou, o motivo. Não precisa de manter a janela aberta para a receber.

:::note
Arquivar um projeto grande pode demorar entre alguns segundos e uma hora, consoante a quantidade de dados de tabelas incluída. Um arquivo demorado é normal e não significa que algo correu mal — aguarde pela notificação em vez de iniciar uma segunda exportação, que arquivaria o projeto novamente de raiz.
:::

### Tabelas cujos dados não podem ser incluídos

Ocasionalmente, uma tabela listada num projeto deixou de ter dados — por exemplo, uma tabela que nunca foi criada, ou cujos dados foram removidos fora do projeto. O arquivo é gravado na mesma: essas tabelas ficam de fora dos dados de tabelas, e a exportação termina com uma mensagem que as identifica. Tudo o resto — a configuração do projeto, os fluxos de trabalho, as definições de tabelas e os dados de todas as outras tabelas — é arquivado normalmente.

O arquivo regista quais as tabelas incluídas sem os respetivos dados, e a restauração volta a identificá-las no final em vez de as apresentar como completas. Uma tabela cuja definição ainda era legível regressa com as suas colunas e sem linhas; uma cuja definição também já não existia regressa como uma entrada sem tabela associada. Execute novamente o fluxo de trabalho que cria uma tabela para a preencher.

:::note
Um arquivo agendado regista as tabelas ignoradas no registo do sistema em vez de lhe mostrar uma mensagem, uma vez que não há nenhum ecrã onde a apresentar. Verifique a mensagem de exportação quando for importante saber quais as tabelas incluídas.
:::

### Se não puder ler as tabelas do projeto

Ler as tabelas de um projeto é uma permissão distinta de ler o próprio projeto, e um arquivo depende de ambas. Se puder abrir um projeto mas não tiver acesso de leitura às tabelas, o arquivo é gravado na mesma — apenas não contém dados de tabelas nem definições de tabelas, uma vez que ambos dependem dessa mesma permissão. A exportação termina com uma mensagem que identifica as tabelas deixadas de fora, indicadas pelos respetivos identificadores internos e não pelos nomes, porque os nomes provêm das definições que o arquivo não incluiu.

Um arquivo obtido desta forma é uma cópia da configuração do projeto — os seus fluxos de trabalho, variáveis, dimensões, vistas e esquemas, na medida em que tem direito a ler cada um deles — e não dos respetivos dados. **Restaurá-lo não recria nenhuma tabela**, pelo que não é uma cópia de segurança a partir da qual possa reconstruir os dados do projeto. Verifique a mensagem de exportação antes de confiar num arquivo destes.

Ao contrário das tabelas descritas acima, isto não se corrige executando novamente um fluxo de trabalho — os dados nunca chegaram a ser lidos. Peça a um administrador da área de trabalho que lhe conceda acesso de leitura às tabelas do projeto e, em seguida, crie novamente o arquivo.

:::caution
Isto aplica-se também aos arquivos agendados, que são executados como um membro específico. Se esse membro não tiver acesso de leitura às tabelas, todos os arquivos produzidos pelo agendamento contêm apenas a configuração, e a lacuna é registada no registo do sistema em vez de ser mostrada a alguém. Se mantiver arquivos agendados como cópias de segurança, confirme que o membro como o qual são executados consegue ler as tabelas do projeto.
:::

### Se o projeto utilizar o acesso a linhas

Criar um arquivo lê as tabelas do projeto, pelo que o [Acesso a linhas](/pt-pt/administration/access/managing-security-groups-and-assignments/#gerir-o-acesso-a-linhas) se aplica como em qualquer outra leitura. Em cada coluna de governação, o arquivo contém as linhas concedidas aos seus grupos. Quando não tem nenhuma concessão numa coluna, o resultado depende de como essa coluna foi declarada: uma configurada para negar por predefinição não lhe dá nenhuma linha, ao passo que uma declarada para permitir tudo por predefinição deixa essa coluna sem filtro. Uma tabela que não tenha nenhuma das colunas de governação é arquivada por inteiro, e um Arquiteto do projeto arquiva todas as linhas, independentemente das concessões. Um arquivo agendado é executado sob a identidade do próprio projeto e não a sua, pelo que arquiva todas as linhas.

Um arquivo criado por um membro que detém apenas algumas das concessões é uma cópia parcial dos dados do projeto, e uma coluna configurada para negar por predefinição significa que uma tabela pode regressar vazia e não apenas reduzida. Restaurar um arquivo destes reconstrói o projeto sem essas linhas, e nada na restauração o indica, porque, no que respeita ao arquivo, as linhas nunca existiram.

:::caution
Quando precisar de um arquivo a partir do qual possa reconstruir o projeto completo, crie-o como um membro que leia o projeto na íntegra.
:::

### Se a exportação falhar

Uma exportação que falha passa agora a comunicar a falha. Anteriormente, um arquivo podia indicar-se como concluído quando não tinha sido gravado, deixando-o descobrir o ficheiro em falta mais tarde — geralmente quando o ia restaurar. Uma exportação falhada di-lo agora, pelo que deve tratar um êxito comunicado como genuíno e verificar a mensagem em tudo o que comunique um erro. O mesmo se aplica aos outros tipos de exportação, não apenas aos arquivos de projeto.

## Restaurar um arquivo


Depois de ter um arquivo, pode querer restaurá-lo. Pode restaurar um arquivo para um novo projeto ou para um projeto existente.



Para restaurar um arquivo:


1. Abra o Analyze
2. Selecione o separador “Projetos”
3. Escolha **Importar arquivo de projeto** no menu **Ações** (ou na barra de ferramentas) e selecione o arquivo a restaurar
4. Escolha se pretende **Criar novo projeto** ou **Importar para projeto existente** e selecione na árvore de seleção o que pretende trazer
5. Clique em **Importar projeto**

A importação é executada em segundo plano. Uma janela de progresso mostra o andamento e uma mensagem informa quando termina, com um e-mail adicional se algo tiver ficado de fora. Se a importação não puder começar — por exemplo, porque o projeto escolhido está bloqueado —, a janela permanece aberta e indica o motivo.


Um arquivo é verificado quando é aberto. Um arquivo com conteúdo que um arquivo de projeto nunca contém — um ficheiro que ficaria fora da pasta do próprio arquivo, uma ligação que aponta para fora dela ou definições que tentam criar algo que não sejam dados simples — é recusado antes de qualquer elemento ser restaurado.


Não tem de trazer o arquivo todo. A árvore de seleção lista o que o arquivo contém por tipo — fluxos de trabalho, passos, tabelas, dimensões, editores de dados, funções definidas pelo utilizador — e tudo o que assinalar traz consigo as respetivas dependências.


### Quando parte de um arquivo não é importada


Uma importação continua quando parte do arquivo não pode ser restaurada. Desde que o arquivo possa ser lido e o próprio projeto possa ser configurado, o projeto é importado, e tudo o que não pôde ser restaurado é listado no respetivo resultado da importação. Se o arquivo não puder ser lido, ou o próprio projeto não puder ser configurado, a importação falha e indica o motivo, e um novo projeto é removido. Uma importação para um projeto existente também pode parar antes de terminar. Tudo o que já tinha sido restaurado permanece no projeto. A mensagem e o e-mail indicam que a importação parou, e o resultado da importação refere quando e porquê, e lista o que não conseguiu restaurar até esse momento.

Quando algo ficou de fora, a mensagem e o e-mail no final da importação indicam-no, e a mensagem inclui uma ligação para a janela **Resultado da importação**. A janela identifica cada item por tipo e nome, indica o motivo e agrupa os itens sob estes cabeçalhos:

- **Não importado** — o item não está no projeto.
- **Criadas sem dados** — a tabela, vista ou dimensão está no projeto mas não contém dados, porque os respetivos dados não puderam ser lidos ou carregados.
- **Avisos** — o item foi importado, mas há algo a verificar, como colunas que o armazém converteu para os tipos de coluna da tabela.
- **Variáveis que mantiveram o valor deste projeto** — o projeto já tinha uma variável com esse nome, pelo que manteve o seu próprio valor.

Os itens mais graves são listados primeiro, e a janela indica-o quando existem mais itens do que os listados. Para voltar a abrir a janela mais tarde, selecione o projeto no separador **Projetos** e escolha **Ver resultado da importação ou cópia** no menu **Ações**, ou clique com o botão direito do rato no projeto.

O resultado permanece no projeto até alguém o dispensar ou até uma importação posterior para o mesmo projeto o substituir. Clique em **Dispensar resultado** para o remover para todos os que podem abrir o projeto; nada no projeto é alterado. Dispensar exige acesso de edição ao projeto, e o projeto não pode estar bloqueado.


### Importar para um projeto existente


Importar para um projeto que já existe acrescenta-lhe conteúdo em vez de o substituir. Duas coisas determinam o que acontece quando o arquivo e o projeto contêm o mesmo item.


**Tem de poder alterar o projeto de destino.** Uma importação para um projeto em que não tem nenhuma função é recusada, tal como uma importação para um projeto bloqueado para impedir alterações — verificado antes de qualquer leitura ou escrita, pelo que uma importação recusada deixa o projeto intacto.


**O projeto mantém as suas próprias definições.** O nome, o identificador, o ambiente de ligação de dados, as predefinições de armazenamento, a conta de documentos, o tipo de acesso, as listas de acesso e as concessões de acesso a linhas permanecem como estão. Apenas o conteúdo que selecionou é trazido.

Um passo definido como **Project Default** transporta essa definição, e não uma conta — depois de restaurado, passa a corresponder à predefinição que o projeto tiver, e não à que tinha quando foi arquivado.


### Itens duplicados


Quando um item recebido é o mesmo item que já existe no projeto, escolhe o que lhe acontece:


- **Substituir itens duplicados pelos dados recebidos** — a versão do arquivo substitui a que está no projeto.
- **Criar nova cópia dos itens duplicados** — o projeto mantém o que tem, e o item recebido é adicionado a seguir com ` copy` acrescentado ao nome (e um contador, se esse nome também estiver ocupado). Aplica-se a fluxos de trabalho, passos, tabelas, dimensões, editores de dados, vistas e funções definidas pelo utilizador.


**As variáveis de projeto e de fluxo de trabalho são a exceção.** Uma variável é identificada pelo nome, pelo que não há forma de adicionar uma segunda cópia sem a mudar para um nome a que nada faz referência. Quando o projeto já define uma variável que o arquivo também contém, o valor do próprio projeto é mantido e o resultado da importação lista as variáveis que deixou intactas. Se quiser o valor do arquivo, defina-o depois na variável.


De notar: esta correspondência é feita por identidade e não por nome. Um item que se originou do mesmo projeto — qualquer coisa de onde o arquivo foi exportado, ou uma cópia desse projeto — é reconhecido como o mesmo item. Dois itens que apenas coincidem no nome são tratados como itens diferentes, e ambos estarão presentes após a importação.

### Se uma tabela regressar sem os respetivos dados


Restaurar os dados de uma tabela depende de as suas colunas coincidirem com as da tabela de destino — os mesmos nomes pela mesma ordem, porque é isso que um carregamento utiliza. Quando não coincidem, os dados dessa tabela ficam de fora e a tabela é listada no resultado da importação em **Criadas sem dados**, tal como uma tabela cujos dados não estavam no arquivo. Uma diferença apenas no tipo armazenado de uma coluna não retém os dados: os dados são carregados e a tabela é listada em **Avisos** com as colunas que o armazém converteu.


Uma importação em que todas as tabelas falharam o carregamento dos dados mantém, ainda assim, o projeto. A mensagem final indica que não foi possível carregar nenhum dos dados das tabelas, e o resultado da importação também. Se uma importação terminar com todos os fluxos de trabalho, tabelas e dimensões no lugar, leia a mensagem final antes de presumir que as linhas vieram também.


## Agendamento de arquivos


Os arquivos podem também servir de cópia de segurança periódica do projeto. O PlaidCloud permite gerir o agendamento das cópias de segurança e definir o período de retenção dos arquivos de cópia de segurança da forma que for mais conveniente ou pretendida.


Uma vez que todas as alterações a um projeto são rastreadas automaticamente, o arquivo não é necessário para reverter alterações. No entanto, fornece instantâneos específicos do estado do projeto, o que é frequentemente útil para efeitos de controlo e/ou para poder recuperar até um ponto conhecido.



Para definir um agendamento de arquivos:


1. Abra o Analyze
2. Selecione o separador “Projetos”
3. Clique no ícone de cópia de segurança
4. Escolha um diretório de destino numa conta **Documento**
5. Escolha a frequência e a retenção da cópia de segurança
6. Escolha os itens a incluir na cópia de segurança
7. Clique em “Update”
