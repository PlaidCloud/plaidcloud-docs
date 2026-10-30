---
title: Arquivar um projeto
description: Arquive projetos do PlaidCloud para preservar o trabalho concluído, liberar recursos do espaço de trabalho e manter um ambiente de projetos organizado.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/archive-a-project.md
---

## Criar um arquivo

Os projetos normalmente contêm processos e lógica críticos, que é importante arquivar. Se você precisar restaurar o projeto para um estado específico, ter arquivos é essencial.

O PlaidCloud permite arquivar projetos a qualquer momento. A criação de arquivos complementa o acompanhamento pontual integrado do PlaidCloud, permitindo capturar momentos específicos. Isso pode ser particularmente útil antes de uma grande alteração ou para registrar o estado exato de um ambiente de produção para a posteridade.

**Backup completo**: inclui todas as tabelas de dados de um projeto. O arquivo pode ser bastante grande, dependendo do volume de dados do projeto.

**Backup parcial:** pode ser usado quando todos os dados do projeto podem ser derivados de outras fontes. Nesse caso, não é necessário arquivar os dados do projeto, pois eles permanecem em outro lugar. Arquivos parciais economizam tempo e espaço de armazenamento ao criar o arquivo.

Para arquivar um projeto:

1. Abra o Analyze
2. Selecione a guia “Projetos”
3. Selecione o projeto e escolha **Exportar arquivo do projeto** no menu **Ações** (ou clique com o botão direito no projeto e escolha **Exportar arquivo do projeto**)

A janela mostra o nome do projeto que será arquivado na barra de título, para que você confirme que escolheu o correto antes de começar.

### Enquanto o arquivamento é executado

A janela de exportação se fecha assim que o PlaidCloud aceita a solicitação, e uma janela de progresso acompanha o arquivamento a partir daí. Você pode deixar essa janela de progresso aberta para acompanhar, ou enviá-la para segundo plano e continuar trabalhando — o arquivamento é executado na plataforma de qualquer forma, e fechar a janela de progresso não o interrompe.

Uma notificação informa como ele terminou: que o arquivo foi gravado, quais tabelas entraram sem seus dados ou, se falhou, por quê. Você não precisa manter a janela aberta para recebê-la.

:::note
Um projeto grande pode levar de alguns segundos a uma hora para ser arquivado, dependendo de quantos dados de tabela ele inclui. Um arquivamento demorado é normal e não significa que algo deu errado — aguarde a notificação em vez de iniciar uma segunda exportação, que arquivaria o projeto novamente desde o início.
:::

### Tabelas cujos dados não podem ser incluídos

Ocasionalmente, uma tabela listada em um projeto não tem mais nenhum dado por trás — por exemplo, uma tabela que nunca foi criada ou cujos dados foram removidos fora do projeto. O arquivo ainda é gravado: essas tabelas ficam de fora dos dados de tabela, e a exportação termina com uma mensagem que as nomeia. Todo o resto — a configuração do projeto, os fluxos de trabalho, as definições de tabela e os dados de todas as outras tabelas — é arquivado normalmente.

O arquivo registra quais tabelas entraram sem seus dados, e restaurá-lo as nomeia novamente ao final da restauração, em vez de apresentá-las como completas. Uma tabela cuja definição ainda era legível volta com suas colunas e sem linhas; uma cuja definição também havia desaparecido volta como uma entrada sem tabela por trás. Execute novamente o fluxo de trabalho que cria uma tabela para preenchê-la.

:::note
Um arquivamento agendado registra as tabelas ignoradas no log do sistema em vez de mostrar uma mensagem, já que não há nada na tela para mostrá-la. Verifique a mensagem de exportação quando for importante saber quais tabelas foram incluídas.
:::

### Se você não puder ler as tabelas do projeto

Ler as tabelas de um projeto é uma permissão separada de ler o próprio projeto, e um arquivamento depende de ambas. Se você consegue abrir um projeto, mas não tem acesso de leitura às tabelas, o arquivo ainda é gravado — apenas não leva nenhum dado de tabela, nem definições de tabela, já que ambos dependem da mesma permissão. A exportação termina com uma mensagem que nomeia as tabelas que ficaram de fora, identificadas por seus ids internos em vez de seus nomes, porque os nomes vêm das definições que o arquivo não incluiu.

Um arquivo gerado dessa forma é uma cópia da configuração do projeto — seus fluxos de trabalho, variáveis, dimensões, visões e layouts, na medida em que você tem direito de ler cada um deles — e não de seus dados. **Restaurá-lo não recria nenhuma tabela**, portanto ele não é um backup a partir do qual você possa reconstruir os dados do projeto. Verifique a mensagem de exportação antes de confiar em um arquivo assim.

Diferentemente das tabelas descritas acima, isso não é algo que executar novamente um fluxo de trabalho corrija — os dados nunca foram lidos. Peça a um administrador do espaço de trabalho que conceda a você acesso de leitura às tabelas do projeto e, em seguida, gere o arquivo novamente.

:::caution
Isso vale também para arquivamentos agendados, que são executados como um membro específico. Quando esse membro não tem acesso de leitura às tabelas, todo arquivo que o agendamento produz contém apenas a configuração, e a lacuna é registrada no log do sistema em vez de ser mostrada a alguém. Se você mantém arquivamentos agendados como backups, confirme que o membro com o qual eles são executados consegue ler as tabelas do projeto.
:::

### Se o projeto usa acesso a linhas

Gerar um arquivo lê as tabelas do projeto, portanto o [Acesso a linhas](/pt-br/administration/access/managing-security-groups-and-assignments/#gerenciar-o-acesso-a-linhas) se aplica a ele como a qualquer outra leitura. Em cada coluna de controle, o arquivo leva as linhas concedidas aos seus grupos. Quando você não tem nenhuma concessão em uma coluna, o resultado depende de como essa coluna foi declarada: uma configurada para negar por padrão não retorna nenhuma linha, e uma declarada para permitir tudo por padrão deixa essa coluna sem filtro. Uma tabela que não tem nenhuma das colunas de controle é arquivada por inteiro, e um Arquiteto do projeto arquiva todas as linhas, independentemente das concessões. Um arquivamento agendado é executado sob a identidade do próprio projeto, e não a sua, portanto arquiva todas as linhas.

Um arquivo gerado por um membro que tem apenas algumas das concessões é uma cópia parcial dos dados do projeto, e uma coluna configurada para negar por padrão significa que uma tabela pode voltar vazia, e não apenas reduzida. Restaurar esse arquivo reconstrói o projeto sem essas linhas, e nada na restauração informa isso, porque, no que diz respeito ao arquivo, as linhas nunca existiram.

:::caution
Quando você precisar de um arquivo a partir do qual seja possível reconstruir o projeto inteiro, gere-o como um membro que lê o projeto por completo.
:::

### Se a exportação falhar

Uma exportação que falha agora informa a falha. Anteriormente, um arquivamento podia ser relatado como concluído sem ter sido gravado, deixando você descobrir o arquivo ausente mais tarde — com mais frequência na hora de restaurá-lo. Agora, uma exportação com falha avisa, portanto trate um sucesso informado como genuíno e verifique a mensagem em tudo que relatar um erro. O mesmo vale para os outros tipos de exportação, não apenas para arquivos de projeto.

## Restaurar um arquivo

Depois de ter um arquivo, você pode querer restaurá-lo. Você pode restaurar um arquivo em um novo projeto ou em um projeto existente.

Para restaurar um arquivo:

1. Abra o Analyze
2. Selecione a guia “Projetos”
3. Escolha **Importar arquivo do projeto** no menu **Ações** (ou na barra de ferramentas) e selecione o arquivo a restaurar
4. Escolha entre **Criar novo projeto** ou **Importar para projeto existente** e selecione na árvore de seleção o que trazer
5. Clique em **Importar projeto**

A importação é executada em segundo plano. Uma janela de progresso mostra o andamento, e uma mensagem informa quando ela termina, com um e-mail também se algo tiver ficado de fora. Se a importação não puder começar — porque o projeto escolhido está bloqueado, por exemplo — a janela permanece aberta e informa o motivo.

Um arquivo é verificado ao ser aberto. Um arquivo com conteúdo que um arquivo de projeto nunca contém — um arquivo que cairia fora da pasta do próprio arquivo, um link que aponta para fora dela ou configurações que tentam criar algo diferente de dados simples — é recusado antes de qualquer coisa dele ser restaurada.

Você não precisa trazer o arquivo inteiro. A árvore de seleção lista o que o arquivo contém por tipo — fluxos de trabalho, etapas, tabelas, dimensões, editores de dados, funções definidas pelo usuário — e tudo o que você marcar traz consigo suas dependências.

### Quando parte de um arquivo não é importada

Uma importação continua quando parte do arquivo não pode ser restaurada. Desde que o arquivo possa ser lido e o próprio projeto possa ser configurado, o projeto é importado, e tudo o que não pôde ser restaurado é listado no resultado da importação. Se o arquivo não puder ser lido, ou se o próprio projeto não puder ser configurado, a importação falha e informa o motivo, e um novo projeto é removido. Uma importação para um projeto existente também pode parar antes de terminar. Tudo o que ela já havia restaurado permanece no projeto. A mensagem e o e-mail informam que a importação foi interrompida, e o resultado da importação informa quando e por quê, além de listar o que ela não conseguiu restaurar até então.

Quando algo ficou de fora, a mensagem e o e-mail ao final da importação informam isso, e a mensagem tem um link para a janela **Resultado da importação**. A janela nomeia cada item por tipo e nome, informa o motivo e agrupa os itens sob estes títulos:

- **Não importado** — o item não está no projeto.
- **Criadas sem dados** — a tabela, visão ou dimensão está no projeto, mas não contém dados, porque seus dados não puderam ser lidos ou carregados.
- **Avisos** — o item foi importado, mas há algo a verificar, como colunas que o data warehouse converteu para os tipos de coluna da tabela.
- **Variáveis que mantiveram o valor deste projeto** — o projeto já tinha uma variável com esse nome, portanto manteve o próprio valor.

Os itens mais graves são listados primeiro, e a janela informa quando há mais itens do que os listados. Para abrir a janela novamente mais tarde, selecione o projeto na guia **Projetos** e escolha **Ver resultado da importação ou cópia** no menu **Ações**, ou clique com o botão direito no projeto.

O resultado permanece no projeto até alguém dispensá-lo ou até uma importação posterior no mesmo projeto substituí-lo. Clique em **Dispensar resultado** para removê-lo para todos que podem abrir o projeto; nada no projeto é alterado. Dispensar exige acesso de edição ao projeto, e o projeto não pode estar bloqueado.

### Importar para um projeto existente

Importar para um projeto que já existe adiciona a ele em vez de substituí-lo. Duas coisas decidem o que acontece quando o arquivo e o projeto têm o mesmo item.

**Você precisa poder alterar o projeto de destino.** Uma importação para um projeto no qual você não tem nenhum papel é recusada, assim como uma importação para um projeto bloqueado contra alterações — verificado antes de qualquer coisa ser lida ou gravada, de modo que uma importação recusada deixa o projeto intocado.

**O projeto mantém as próprias configurações.** Seu nome, identificador, ambiente de conexão de dados, padrões de armazenamento, conta de documentos, tipo de acesso, listas de acesso e concessões de acesso a linhas permanecem como estão. Apenas o conteúdo que você selecionou é trazido.

Uma etapa definida como **Padrão do projeto** leva essa configuração, e não uma conta — depois de restaurada, ela passa a usar o padrão que o projeto tiver, e não o que tinha quando foi arquivada.

### Itens duplicados

Quando um item recebido é o mesmo item que já está no projeto, você escolhe o que acontece com ele:

- **Substituir itens duplicados pelos dados recebidos** — a versão do arquivo substitui a do projeto.
- **Criar nova cópia dos itens duplicados** — o projeto mantém o que tem, e o item recebido é adicionado ao lado dele com ` copy` anexado ao nome (e um contador, se esse nome também já existir). Isso se aplica a fluxos de trabalho, etapas, tabelas, dimensões, editores de dados, visões e funções definidas pelo usuário.

**Variáveis de projeto e de fluxo de trabalho são a exceção.** Uma variável é identificada pelo nome, portanto não há como adicionar uma segunda cópia dela sem renomeá-la para algo a que nada se refere. Quando o projeto já define uma variável que o arquivo também contém, o valor do próprio projeto é mantido e o resultado da importação lista as variáveis que foram deixadas como estavam. Se você quiser o valor do arquivo, defina-o na variável depois.

Um ponto a saber: essa correspondência é por identidade, não por nome. Um item que veio originalmente do mesmo projeto — qualquer coisa da qual o arquivo foi exportado, ou uma cópia dela — é reconhecido como o mesmo item. Dois itens que apenas têm o mesmo nome são tratados como itens diferentes, e ambos estarão presentes após a importação.

### Se uma tabela voltar sem seus dados

Restaurar os dados de uma tabela depende de suas colunas coincidirem com a tabela de destino — os mesmos nomes na mesma ordem, porque é isso que um carregamento considera. Quando não coincidem, os dados dessa tabela ficam de fora e a tabela é listada no resultado da importação em **Criadas sem dados**, da mesma forma que uma tabela cujos dados não estavam no arquivo. Uma diferença apenas no tipo armazenado de uma coluna não impede os dados: eles são carregados, e a tabela é listada em **Avisos** com as colunas que o data warehouse converteu.

Uma importação cujas tabelas falharam todas ao carregar seus dados ainda mantém o projeto. Sua mensagem final informa que nenhum dado de tabela pôde ser carregado, e o resultado da importação também. Se uma importação terminar com todos os fluxos de trabalho, tabelas e dimensões no lugar, leia a mensagem final antes de presumir que as linhas vieram junto.

## Agendamento de arquivamento

Os arquivos também podem servir como backup periódico do seu projeto. O PlaidCloud permite gerenciar o agendamento de backup e definir o período de retenção dos arquivos de backup da forma mais conveniente ou desejada.

Como todas as alterações em um projeto são rastreadas automaticamente, o arquivamento não é necessário para fins de reversão. No entanto, ele fornece instantâneos específicos do estado do projeto, o que costuma ser útil para fins de controle e/ou para poder recuperar um ponto conhecido.

Para definir um agendamento de arquivamento:

1. Abra o Analyze
2. Selecione a guia “Projetos”
3. Clique no ícone de backup
4. Escolha um diretório de destino em uma conta de **Documento**
5. Escolha a frequência e a retenção do backup
6. Escolha quais itens incluir no backup
7. Clique em “Atualizar”
