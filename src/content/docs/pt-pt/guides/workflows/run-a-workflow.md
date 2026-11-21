---
title: Executar um fluxo de trabalho
description: Execute um fluxo de trabalho do PlaidCloud manualmente ou a pedido, acompanhe o estado de cada passo e pause, pare ou retome uma execução a partir do ponto onde ficou.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Pode iniciar uma execução completa de um fluxo de trabalho clicando no ícone de execução na hierarquia de **Fluxos de trabalho** ou selecionando **Run All** no menu **Ações** de um fluxo de trabalho específico.



Também pode clicar no botão **Toggle Start/Stop** na parte superior da tabela de fluxos de trabalho. Este botão de alternância para um fluxo de trabalho em execução ou inicia um fluxo de trabalho.

Se clicar em **Executar** num fluxo de trabalho que já está em execução, o PlaidCloud informa-o disso em vez de iniciar uma segunda execução.

## Escolher um modo de lançamento

Cada execução tem um modo de lançamento ERP. Para escolher um no PlaidCloud, utilize **Executar com modo de lançamento** no menu de contexto de um fluxo de trabalho, ou o botão de modo de execução na área de desenho do fluxo de trabalho; **Iniciar fluxo de trabalho** ou **Executar fluxo de trabalho** simples pedem Live, sujeito ainda ao limite do projeto descrito abaixo. Também pode escolher o modo ao iniciar uma execução através da API de execução ou do assistente.

| Modo | O que acontece |
|---|---|
| Live | Os passos de lançamento lançam exatamente como sempre o fizeram. É o valor predefinido. |
| Simulate | Cada passo de lançamento ERP constrói e valida exatamente o que lançaria, não confirma nada e nunca contacta o ERP. Os lançamentos que seriam efetuados ficam registados para que possa revê-los antes de executar em modo Live: os de um passo **Contabilizar documentos** no [Registo de lançamentos](/pt-pt/guides/connections/posting-register/) como **Seria lançado** (consulte [Contabilizar documentos em sistemas ERP](/pt-pt/guides/connections/post-documents/)), e os do passo de lançamento próprio de um sistema no [Histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/), marcados como simulados. |
| Off | Os passos de lançamento são ignorados por completo. |

Um projeto tem também o seu próprio limite de modo de lançamento, definido através da API do projeto ou do assistente por qualquer membro com acesso de escrita a um projeto desbloqueado. O limite só torna uma execução mais segura, nunca mais permissiva: o modo efetivo de uma execução é o mais restritivo entre o modo escolhido e o limite do projeto, pelo que um projeto limitado a Simulate permanece simulado mesmo que a execução seja iniciada em Live.

Um [evento agendado](/pt-pt/administration/scheduled-events/event-scheduler/#modo-de-lançamento-erp) mantém o seu próprio modo de lançamento, pelo que um agendamento definido como Simulate é executado em modo simulado sempre que é acionado.

O modo estende-se a tudo o que a execução toca. Um subfluxo de trabalho, uma macro e um passo **Run Model**, **Conditional Run Model** ou **Loop Model** herdam todos o modo da execução principal, tal como uma execução que [retome](#pausar-parar-e-retomar) após uma paragem — uma execução simulada não pode lançar a sério em lado nenhum do seu interior.

:::caution
Os passos de lançamento SAP, de anexos SAP e de RFC SAP genéricas não fazem simulação. Em Simulate ou Off são ignorados por completo, porque os indicadores de teste do próprio SAP continuam a abrir uma ligação real ao SAP — ignorar o passo é a única forma de uma execução simulada nunca chegar ao SAP.
:::

:::note
Um passo individual de lançamento ERP tem também a sua própria definição Validate Only (designada Preview ou Test Only Mode em alguns passos), independente do modo de lançamento da execução acima. O editor de passos guarda sempre esta definição de forma explícita. Uma configuração de passo escrita por outra via — a API REST, o MCP ou a importação de um pacote de fluxo de trabalho — que omita totalmente a definição passa agora também a ter por predefinição uma pré-visualização em vez de um lançamento real. O passo **Contabilizar documentos** não tem uma definição deste tipo: o modo da execução e o modo do próprio sistema decidem se lança — consulte [Contabilizar documentos em sistemas ERP](/pt-pt/guides/connections/post-documents/).
:::

## Autorizar o projeto a lançar

Uma execução de fluxo de trabalho lança num ERP como o projeto, e não como a pessoa que a iniciou. Antes de uma execução poder lançar, o projeto precisa de uma autorização para cada ligação e ambiente ERP que os seus passos de lançamento utilizam. Sem ela, o passo falha com "This project isn't authorized to post to connection …", indicando a ligação e o ambiente. Os passos **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** e **Call SAP RFC** não precisam de uma.

Para autorizar um projeto, abra a respetiva página inicial e selecione **Autorizações de escrita no ERP** em **Lançamento ERP**. Cada linha corresponde a uma ligação num ambiente. Marque **Autorizado** para permitir que o projeto lance aí, ou desmarque para impedir. **Autorizado por** e **Autorizado em** mostram quem autorizou por último e quando.

- O botão é apresentado aos Arquitetos do projeto e aos administradores da área de trabalho, mas só um Arquiteto pode alterar uma autorização, e apenas enquanto o projeto estiver desbloqueado. Um administrador da área de trabalho que não seja Arquiteto pode primeiro adicionar-se a si próprio como Arquiteto.
- Selecionar uma linha para autorizar ou limpar não recarrega a lista: a posição de deslocação e qualquer ordenação de colunas que tenha escolhido mantêm-se. A janela pode ser redimensionada e a nota sobre projetos públicos é apresentada na íntegra.
- Para autorizar uma ligação, também precisa de acesso de escrita a ela: é o proprietário, ou esta é partilhada consigo pelo nome ou através de um dos seus grupos de segurança. Uma ligação definida como **Todos os membros da área de trabalho** não conta.
- Um projeto definido como **Todos os membros da área de trabalho** é autorizado como qualquer outro. Todos os membros são Arquitetos do mesmo, pelo que qualquer membro com acesso de escrita a uma ligação pode autorizar o projeto para essa ligação. Depois de autorizado, qualquer membro pode lançar nessa ligação a partir dos fluxos de trabalho do projeto, e a janela indica-o acima da grelha.
- Uma nova cópia privada, feita com dados de tabela ou membros de dimensão, mantém as autorizações da origem que pudesse conceder a si próprio e chega em Simulate se a origem estava em Live — consulte [Autorizações de escrita no ERP na cópia](/pt-pt/guides/projects/managing-projects/#autorizações-de-escrita-no-erp-na-cópia). Qualquer outra cópia, ou um projeto criado a partir de um arquivo de projeto, começa sem autorizações. Autorize-o antes de lançar.

## Acompanhar o estado de um passo

Enquanto um fluxo de trabalho é executado, cada passo apresenta um ícone de estado que mostra em que ponto se encontra, juntamente com o tempo que está em execução. Passe o rato sobre o ícone para ver a mensagem correspondente.

| Estado | O que significa |
|---|---|
| Em espera | O passo está em fila e ainda não começou. |
| Em execução | O passo está a trabalhar e a sua duração aumenta à medida que avança. |
| Concluído | O passo terminou com êxito. |
| Aviso | O passo terminou, mas assinalou algo que vale a pena ler no [registo do fluxo de trabalho](/pt-pt/guides/workflows/viewing-workflow-log/). |
| Erro | O passo falhou. Consulte [Gerir erros de passos](/pt-pt/guides/workflows/managing-step-errors/). |
| Ignorado | O passo foi saltado — está desativado ou as suas condições de execução não foram cumpridas. Consulte [Ignorar passos num fluxo de trabalho](/pt-pt/guides/workflows/skip-steps-in-a-workflow/). |
| Continuado | O passo falhou, mas está definido para continuar em caso de erro, pelo que o fluxo de trabalho prosseguiu. Consulte [Continuar em caso de erro](/pt-pt/guides/workflows/continue-on-error/). |
| Parado | A execução foi parada antes de o passo poder terminar. |
| Abandonado | A execução do passo foi interrompida, pelo que nunca terminará. Retome a execução ou execute novamente o fluxo de trabalho. |

Uma vista de fluxo de trabalho aberta é atualizada automaticamente à medida que uma execução progride, pelo que os estados que está a ver se mantêm atuais sem recarregar a página.

### Passos abandonados

Um passo é marcado como **abandonado** quando o que o estava a executar desapareceu a meio da execução — mais frequentemente porque alguém premiu **Parar**, ou porque uma manutenção da plataforma interrompeu a execução. A duração do passo deixa de aumentar e a descrição do estado explica o que aconteceu.

Um passo abandonado não foi concluído e não produziu qualquer resultado. Não é um passo lento, nem um problema com os seus dados ou com a sua configuração.

Para retomar o trabalho, [**Retome**](#pausar-parar-e-retomar) a execução — o passo abandonado é executado novamente — ou execute novamente todo o fluxo de trabalho. Ambas as opções são seguras.

### Passos interrompidos

Se o servidor que executa um passo for perdido a meio da execução, o PlaidCloud executa o passo novamente de forma automática quando é seguro repeti-lo: um passo que substitui o seu resultado acaba com o mesmo resultado que uma única execução limpa, pelo que não tem nada a verificar. O registo do passo mostra um aviso no ponto onde começa a segunda tentativa: "Restarted: the server running this step stopped before it finished (e.g. out of memory or a restart); running it again from the start."

Um passo que não pode ser repetido em segurança não é executado novamente. Falha uma vez com uma mensagem de **interrompido**, porque executá-lo uma segunda vez poderia duplicar o que a primeira tentativa já escreveu. Os passos que escrevem resultados com `{date}` ou `{date_iso}` no nome ou no caminho contam como não seguros para repetição, uma vez que uma nova execução poderia cair numa data diferente. Para recuperar, verifique no destino do passo o que a primeira tentativa escreveu, limpe-o se necessário e depois [volte a executar o passo](/pt-pt/guides/workflows/running-one-step-in-a-workflow/) ou **Retome** a execução.

### Passos que nunca começam

Enquanto um passo aguarda por um trabalhador, a sua mensagem de estado indica "Waiting for a worker… N min. No import worker has picked this step up yet." (o tipo de trabalhador corresponde ao passo, como importação ou exportação). A mensagem desaparece quando o trabalho começa.

Se o trabalho de um passo nunca puder começar, o passo falha com o motivo em vez de esperar indefinidamente:

| Causa | Falha após cerca de |
|---|---|
| Nenhum trabalhador recolhe o trabalho de um passo de importação ou de dimensão | 40 minutos |
| O pod do passo fica preso em Pending | 20 minutos |
| Não é possível obter a imagem do passo | 5 minutos |
| Não é criado nenhum pod para o passo | 20 minutos |
| Nenhum executor recolhe uma sincronização de conector (Singer) | 30 minutos |

A mensagem da sincronização de conector indica o nome da sincronização. Se um trabalhador iniciou o trabalho e depois desapareceu, o passo também falha, com uma mensagem a indicar que o trabalhador parou. As mensagens de importação e de dimensão indicam "Use Run from here to retry."

### Execuções que deixam de responder

Uma execução nunca fica **Em execução** depois de o trabalho por trás dela ter desaparecido. Se o servidor que executa o fluxo de trabalho for perdido, a execução termina como falhada. Uma execução pode durar no máximo 12 horas: uma que ainda esteja em execução nesse momento falha com "Run failed: still running at the 12-hour limit. Re-run the workflow."

## Run Insight

O Run Insight mostra onde uma execução de um fluxo de trabalho gastou o seu tempo e que passos demoraram mais ou menos tempo do que é habitual. Avalia cada passo em relação às execuções recentes desse mesmo passo, pelo que um passo que é sempre lento não é destacado.

### Abrir o Run Insight

- Na área de desenho, clique em **Histórico** na barra de ferramentas. Consulte [Estruturador visual de fluxos de trabalho](/pt-pt/guides/workflows/advanced-workflows/).
- No separador **Fluxos de trabalho**, selecione um fluxo de trabalho e escolha **Run Insight** no menu **Ações** ou no menu de clique com o botão direito.
- No Início, escolha **Abrir a última execução** num cartão de fluxo de trabalho.
- Na caixa de diálogo do histórico de execuções, escolha uma execução na tabela **Execuções** com **Abrir na Análise** ou abra a respetiva linha.
- Numa mensagem do Weave na aplicação sobre uma execução lenta, clique em **Abrir a execução**. Consulte [Ser avisado quando uma execução termina](/pt-pt/guides/ai-assistant/weave-findings/#ser-avisado-quando-uma-execução-termina).

A caixa de diálogo tem o título **Histórico de execuções** — nome do fluxo de trabalho. Os botões **Análise** e **Execuções** alternam entre esta vista e a tabela de execuções anteriores. O histórico de execuções de um passo, aberto a partir do Inspetor, mostra apenas a tabela.

### Ler o cabeçalho e a lista de atenção

O cabeçalho indica o resultado da execução numa linha: **Demorou** *tempo*, **Em execução há** *tempo* enquanto decorre, **Parado após** *tempo* para a última execução que foi parada, ou **Falhou em** o fluxo de trabalho em que falhou. Uma frase por baixo diz o que se destaca, como os passos que foram mais lentos do que o habitual, o tempo passado em espera, ou que todos os passos com histórico se mantiveram dentro do intervalo habitual. Seguem-se a hora de início e o número de fluxos de trabalho e de passos e, quando alguns passos têm histórico insuficiente para serem avaliados, quantos são. Quando algo precisa de ser visto, uma contagem assinalada com **para rever** aparece junto ao cabeçalho.

Uma faixa de execuções recentes fica ao lado do cabeçalho. Clique numa execução na faixa para a abrir. Uma execução que falhou é assinalada, tal como uma execução que executou menos passos do que a maioria das execuções recentes, porque não pode ser comparada com uma execução completa.

**O que requer atenção** lista, por esta ordem, as falhas primeiro, depois o tempo acima do habitual e depois a espera. Clique num item para o selecionar na vista.

### Fluxo, cronologia e tabela

Escolha uma vista no menu **Vista**.

| Vista | O que mostra |
|---|---|
| **Fluxo** | Blocos cuja altura é o tempo. O âmbar é o tempo acima do habitual de um passo. Onde um passo chamou outros fluxos de trabalho, uma fatia **Sobrecarga de chamada** é o tempo do próprio passo fora desses fluxos de trabalho. Onde nenhum passo estava em execução, uma fatia **Em espera** mostra a lacuna; um fluxo de trabalho executado em paralelo não desenha nenhuma. |
| **Cronologia** | Tempo de relógio desde o início da execução. Um contorno tracejado indica quanto tempo o bloco demorou na execução comparada. |
| **Tabela** | Tudo pela ordem das chamadas, com as colunas **Nome**, **Esta execução**, **Habitualmente**, **Extra**, **Execução comparada** e **Estado**. |

Um fluxo de trabalho que chamou outros fluxos de trabalho mostra-os no seu interior. Faça duplo clique num bloco de fluxo de trabalho, ou escolha **Ampliar**, para trabalhar no seu interior, e utilize o caminho acima da vista ou **Reduzir** no menu **Ações** para voltar. Quando vários blocos que seguiram o ritmo habitual estão juntos, o **Fluxo** recolhe-os num único bloco **N no ritmo habitual**; clique num deles, ou escolha **Mostrar todos os blocos** no menu **Ações**, para os abrir. **Recolher blocos no ritmo habitual** volta a recolhê-los.

Selecione um bloco para ver o respetivo painel de detalhes, com o que se aplicar entre **Esta execução**, **Habitualmente**, **Histórico**, **Acima do habitual** e **Execução comparada**, e com **Mostrar no respetivo fluxo de trabalho**, **Mostrar os respetivos passos** ou **Ampliar**, **Abrir fluxo de trabalho** e **Ver registo da execução**. **Abrir fluxo de trabalho** abre o fluxo de trabalho na área de desenho e **Ver registo da execução** abre o respetivo [registo](/pt-pt/guides/workflows/viewing-workflow-log/).

### O que significam as marcas

| Marca | Significado |
|---|---|
| **Falhou** | Um passo terminou com um erro. O painel mostra a respetiva mensagem, a menos que o seu perfil não possa ver o nome do passo. |
| **Mais lento do que o habitual** | O passo demorou mais do que o seu intervalo habitual. |
| **Mais lento em toda a execução** | Todos os passos do fluxo de trabalho ficaram mais lentos aproximadamente na mesma medida, o que aponta para algo que o fluxo de trabalho inteiro partilha e não para um único passo. Os seus passos mostram **Parte de uma lentidão generalizada**. |
| **Tem passos lentos** | Um fluxo de trabalho com **Passos lentos no interior**. |
| **No ritmo habitual** | O passo executou-se dentro do seu intervalo habitual. |
| **Mais rápido** | O passo foi mais rápido do que o seu intervalo habitual. |
| **Histórico insuficiente** | O passo não foi executado vezes suficientes para ter um intervalo habitual, por isso não é avaliado. |
| **Erro, continuou** | O passo falhou, mas está configurado para [continuar em caso de erro](/pt-pt/guides/workflows/continue-on-error/). |
| **Ignorado** | O passo foi saltado. |
| **Em execução** | O passo ainda não terminou. |

Um passo cujas execuções recentes já eram lentas ou variam muito pode não ser assinalado. Uma execução no fim de um período, comparada com dias normais, pode aparecer como mais lenta em toda a execução. Uma execução parada mais antiga aparece como uma execução curta, não como parada.

O painel também pode explicar uma marca. **Em espera** é o tempo em que nenhum passo estava em execução, pelo que nenhum passo é responsável por ele. Num passo que foi mais lento do que o habitual, **Linhas escritas** compara a saída do passo com a sua contagem habitual, e é omitida quando a segurança ao nível da linha filtra o que pode ler, e **Guardado desde a sua última execução** indica que o passo foi guardado depois da sua execução anterior e antes de esta começar; o registo mostra um guardar, não o que mudou. **Trabalho diferente** conta os passos que não foram executados e os passos que foram executados sem histórico, medidos em relação ao histórico de cada passo ou, quando compara com outra execução, em relação a essa execução. **Executado em paralelo** significa que as partes do fluxo de trabalho foram executadas ao mesmo tempo, pelo que os seus tempos somam mais do que o relógio. **Chamador incerto** significa que o histórico não consegue mostrar que passo chamou um fluxo de trabalho. **Nome oculto** assinala um passo ou um fluxo de trabalho cujo nome o seu perfil não pode ver, apresentado como **Passo oculto** ou **Fluxo de trabalho oculto**.

### Comparar com

**Comparar com** define em relação a que é medida uma execução, e o respetivo botão mostra **Comparar com: Habitual**, **Comparar com: Execução anterior** ou **Comparar com: Execução escolhida**. **Habitual** usa as execuções recentes de cada passo. **Habitual + execução anterior** e **Habitual + uma execução escolhida** acrescentam também o tempo dessa execução para cada passo, que a **Cronologia** contorna e a **Tabela** mostra em **Execução comparada**. A execução escolhida é selecionada entre as execuções recentes.

### Um fluxo de trabalho dentro de uma execução maior

Quando abre um fluxo de trabalho que outro fluxo de trabalho chamou, a Análise mostra apenas a parte desse fluxo de trabalho na execução. **Abrir a execução completa** passa a mesma caixa de diálogo para o fluxo de trabalho que iniciou a execução.

### Execuções em direto

Uma execução que ainda está em curso é lida de novo a cada 30 segundos enquanto a caixa de diálogo estiver visível. O seu zoom, a seleção e a vista mantêm-se como estão. Sair da Análise para **Execuções** interrompe as atualizações, e voltar à Análise lê a execução de novo e retoma-as. O botão Atualizar, as setas circulares à direita da barra de ferramentas, volta a carregar a execução de raiz, repõe o zoom e a seleção e volta a recolher os blocos que seguiram o ritmo habitual.

### Para assistentes de IA e a API REST

O mesmo perfil está disponível fora da caixa de diálogo:

- REST: `GET /rest/v1/analyze/workflow/run-insight` com `project_id` e `workflow_id`. `run_id` escolhe a execução (a mais recente quando omitido), e `baseline` é `typical`, `previous` ou `run:<id>`.
- MCP: `workflow_describe` com `include=['run_insight']`, e `run_id` e `baseline` opcionais.

Cada fluxo de trabalho e cada passo devolve o seu tempo, o seu lugar na execução, um veredicto em relação ao seu próprio histórico e os motivos. Uma execução que não existe, ou que não tem linhas de passos, não devolve nenhum perfil, mas sim um aviso, em vez de um erro.

## Pausar, parar e retomar

Enquanto um fluxo de trabalho está em execução, pode **Pausar** — os passos em curso terminam e os novos passos aguardam — ou **Parar**, o que cancela os passos que estavam em fila e quaisquer trabalhos de importação ou exportação ainda em execução, juntamente com a consulta ao warehouse que uma exportação estava a ler. Os passos de importação e de dimensão que ainda estavam em fila são cancelados de forma limpa, para não atrasarem importações e cargas de dimensão posteriores na área de trabalho. Parar também interrompe as sincronizações de conector (Singer) em fila ou em execução do fluxo de trabalho, para que uma sincronização não continue a ser executada depois de o fluxo de trabalho ter parado.

Uma macro pode estar em execução em vários sítios ao mesmo tempo, chamada por outros fluxos de trabalho ou por um passo **Macro: Execução em simultâneo**. Parar a macro interrompe todas as cópias dela que estão em execução. Parar uma cópia interrompe apenas essa cópia e o que ela iniciou, e deixa em execução o fluxo de trabalho que a chamou, tal como acontece quando um passo **Macro Concurrent** desiste de uma cópia que deixou de responder. Uma macro que está em execução apenas dentro de outros fluxos de trabalho aparece como **Em execução** na lista de fluxos de trabalho, com **Parar** disponível, e abri-la mostra o estado, a hora de início e a hora de fim de cada passo na sua execução mais recente.

**Retomar** recomeça uma execução pausada, parada ou falhada a partir do ponto onde ficou, em vez de começar de novo. Está disponível sempre que a última execução de um fluxo de trabalho terminou num estado de pausa, paragem ou erro.

O que significa "o ponto onde ficou" depende da forma como o fluxo de trabalho é executado:

| Execução | Ao retomar |
|---|---|
| Série | Recomeça no passo que estava em execução quando a execução terminou e continua a partir daí. Se esse passo estiver dentro de um grupo, Retomar recomeça todo o grupo de nível superior que o contém: os passos do grupo que já terminaram com êxito são deixados como estão, os restantes são executados e a execução continua depois do grupo. |
| Paralela | Volta a executar todos os passos que ainda não tinham terminado com êxito e deixa os passos concluídos como estão. |
| Avançada (grafo) | Volta a executar o nó que falhou e tudo o que ainda aguarda por ele, e deixa os nós concluídos como estão. |

Os passos que chamam outro fluxo de trabalho — **Run Model**, **Conditional Run Model** e **Loop Model** — retomam o fluxo de trabalho que chamam em vez de o reiniciarem, por muitos níveis de aninhamento que existam. Um passo de ciclo retoma a iteração que foi interrompida e ignora as iterações que já foram concluídas.

Quando retoma um fluxo de trabalho que foi executado como **filho aninhado** de outro — um invocado por um passo **Run Model** num fluxo principal — o PlaidCloud oferece **Retomar a partir do topo da cadeia**. Retomar o filho isoladamente não consegue continuar a orquestração do fluxo principal, pelo que esta opção retoma o fluxo principal de nível superior — a raiz da cadeia — e continua toda a cadeia a partir do ponto onde parou. Retomar um fluxo de trabalho de nível superior mantém-se inalterado. O topo da cadeia é resolvido dentro do mesmo projeto: uma cadeia que passa para outro projeto retoma a partir do topo da parte dentro do projeto.

Retomar continua sempre a execução **original**. Volta a executar todos os passos dessa execução que não terminaram com êxito — um passo que falhou ou foi abandonado é executado novamente, não é tratado como concluído — e voltar a executar um passo individual isoladamente entretanto não altera o que Retomar recolhe a seguir. O mesmo se aplica a um fluxo de trabalho filho: se voltou a executar um dos seus passos isoladamente, retomar o fluxo principal continua a executar tudo o que faltava ao filho, e não apenas esse passo.

Uma execução retomada é registada como uma **nova execução** no histórico de execuções do fluxo de trabalho, contendo apenas os passos que voltou a executar. A execução original mantém a sua própria entrada no histórico. Quando uma execução chama o mesmo fluxo de trabalho filho mais do que uma vez, cada chamada tem a sua própria entrada no histórico de execuções do filho. As iterações de um passo de ciclo contam como uma única chamada.

:::note
Um passo de ciclo faz corresponder as iterações concluídas pelos valores das respetivas variáveis. Se os dados sobre os quais o ciclo itera mudaram entre a execução original e a retoma, as iterações que já não consegue fazer corresponder são executadas novamente em vez de ignoradas.
:::
