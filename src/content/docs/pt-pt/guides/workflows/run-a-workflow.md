---
title: Executar um fluxo de trabalho
description: Execute um fluxo de trabalho PlaidCloud manualmente ou a pedido, acompanhe o estado de cada passo e coloque em pausa, pare ou retome uma execução a partir do ponto onde ficou.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Pode iniciar uma execução completa de um fluxo de trabalho clicando no ícone de execução na hierarquia **Fluxos de trabalho** ou selecionando **Run All** no menu **Ações** de um fluxo de trabalho específico.



Também pode clicar no botão **Toggle Start/Stop** na parte superior da tabela de fluxos de trabalho. Este botão de alternância para um fluxo de trabalho em execução ou inicia um fluxo de trabalho.

Se clicar em **Executar** num fluxo de trabalho que já está em execução, o PlaidCloud informa-o disso em vez de iniciar uma segunda execução.

## Escolher um modo de lançamento

Cada execução tem um modo de lançamento ERP. Para escolher um no PlaidCloud, utilize **Executar com modo de lançamento** no menu de contexto de um fluxo de trabalho ou o botão do modo de execução na área de desenho do fluxo de trabalho; um simples **Iniciar fluxo de trabalho** ou **Executar fluxo de trabalho** pede Live, sempre sujeito ao limite do projeto descrito abaixo. Também pode escolher o modo ao iniciar uma execução através da API de execução ou do assistente.

| Modo | O que acontece |
|---|---|
| Live | Os passos de lançamento lançam exatamente como sempre. É a predefinição. |
| Simulate | Cada passo de lançamento ERP prepara e valida exatamente o que lançaria, mas não confirma nada e nunca contacta o ERP. Os lançamentos que seriam efetuados ficam registados no [Histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/), marcados como simulados, para que os possa rever antes de executar em modo real. |
| Off | Os passos de lançamento são totalmente ignorados. |

Um projeto também tem o seu próprio limite de modo de lançamento, definido através da API do projeto ou do assistente por qualquer membro com acesso de escrita a um projeto desbloqueado. O limite só torna uma execução mais segura, nunca mais permissiva: o modo efetivo de uma execução é o mais restritivo entre o modo escolhido e o limite do projeto, pelo que um projeto limitado a Simulate continua simulado mesmo que inicie a execução como Live.

Um [evento agendado](/pt-pt/administration/scheduled-events/event-scheduler/#modo-de-lançamento-no-erp) mantém o seu próprio modo de lançamento, pelo que um agendamento definido como Simulate é executado em modo simulado sempre que é acionado.

O modo aplica-se a tudo aquilo em que a execução toca. Um subfluxo de trabalho, uma macro e um passo **Run Model**, **Conditional Run Model** ou **Loop Model** herdam todos o modo da execução principal, tal como uma execução que [retome](#pausar-parar-e-retomar) após uma paragem — uma execução simulada não pode efetuar lançamentos reais em nenhum ponto do seu interior.

:::caution
Os passos de lançamento SAP, de anexos SAP e de RFC SAP genérica não fazem execuções de teste. Em Simulate ou Off são simplesmente ignorados, porque os próprios indicadores de teste do SAP continuam a abrir uma ligação real ao SAP — ignorar o passo é a única forma de garantir que uma execução simulada nunca chega ao SAP.
:::

:::note
Cada passo de lançamento ERP tem também a sua própria definição Validate Only (designada Preview ou Test Only Mode em alguns passos), independente do modo de lançamento da execução acima. O editor de passos guarda sempre esta definição de forma explícita. Uma configuração de passo escrita de outra forma — a API REST, o MCP ou a importação de um pacote de fluxo de trabalho — que omita totalmente a definição passa também a assumir por predefinição uma pré-visualização em vez de um lançamento real.
:::

## Autorizar o projeto a efetuar lançamentos

Uma execução de fluxo de trabalho efetua lançamentos num ERP em nome do projeto, e não da pessoa que a iniciou. Antes de uma execução poder efetuar lançamentos, o projeto precisa de uma autorização para cada ligação e ambiente ERP utilizados pelos seus passos de lançamento. Sem ela, o passo falha com "Este projeto não está autorizado a efetuar lançamentos na ligação …", indicando a ligação e o ambiente. Os passos **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** e **Call SAP RFC** não precisam de autorização.

Para autorizar um projeto, abra a respetiva página inicial e selecione **Autorizações de escrita no ERP** em **Lançamento ERP**. Cada linha corresponde a uma ligação num ambiente. Marque **Autorizado** para permitir que o projeto efetue lançamentos aí, ou desmarque para o impedir. **Autorizado por** e **Autorizado em** mostram quem autorizou pela última vez e quando.

- O botão é apresentado aos Arquitetos do projeto e aos administradores da área de trabalho, mas apenas um Arquiteto pode alterar uma autorização, e apenas enquanto o projeto estiver desbloqueado. Um administrador da área de trabalho que não seja Arquiteto pode primeiro adicionar-se como tal.
- Selecionar uma linha para a autorizar ou desmarcar não recarrega a lista: a posição de deslocamento e qualquer ordenação de colunas escolhida mantêm-se. A janela pode ser redimensionada e a nota sobre projetos públicos é apresentada na íntegra.
- Para autorizar uma ligação, também precisa de ter acesso de escrita a ela: é o proprietário ou foi partilhada consigo pelo nome ou através de um dos seus grupos de segurança. Uma ligação definida como **Todos os membros da área de trabalho** não conta.
- Um projeto definido como **Todos os membros da área de trabalho** é autorizado como qualquer outro. Todos os membros são Arquitetos do projeto, pelo que qualquer membro com acesso de escrita a uma ligação pode autorizar o projeto para essa ligação. Depois de autorizado, qualquer membro pode efetuar lançamentos nessa ligação a partir dos fluxos de trabalho do projeto, e a janela indica-o acima da grelha.
- Uma nova cópia privada, feita com dados de tabelas ou membros de dimensões, mantém as autorizações da origem que poderia conceder pessoalmente e chega em Simulate se a origem estava em Live — consulte [Autorizações de escrita no ERP na cópia](/pt-pt/guides/projects/managing-projects/#autorizações-de-escrita-no-erp-na-cópia). Qualquer outra cópia, ou um projeto criado a partir de um arquivo de projeto, começa sem autorizações. Autorize-o antes de efetuar lançamentos.

## Acompanhar o estado de um passo

Enquanto um fluxo de trabalho é executado, cada passo apresenta um ícone de estado que mostra a situação em que se encontra, juntamente com o tempo de execução decorrido. Passe o cursor sobre o ícone para ver a mensagem associada.

| Estado | Significado |
|---|---|
| Em espera | O passo está em fila e ainda não começou. |
| Em execução | O passo está a ser processado e a sua duração vai aumentando. |
| Concluído | O passo terminou com êxito. |
| Aviso | O passo terminou, mas assinalou algo que vale a pena ler no [registo do fluxo de trabalho](/pt-pt/guides/workflows/viewing-workflow-log/). |
| Erro | O passo falhou. Consulte [Gerir erros de passos](/pt-pt/guides/workflows/managing-step-errors/). |
| Ignorado | O passo foi ignorado — está desativado ou as suas condições de execução não foram cumpridas. Consulte [Ignorar passos num fluxo de trabalho](/pt-pt/guides/workflows/skip-steps-in-a-workflow/). |
| Continuado | O passo falhou, mas está configurado para continuar em caso de erro, pelo que o fluxo de trabalho prosseguiu. Consulte [Continuar em caso de erro](/pt-pt/guides/workflows/continue-on-error/). |
| Parado | A execução foi parada antes de o passo poder terminar. |
| Abandonado | A execução do passo foi interrompida, pelo que nunca terminará. Retome a execução ou volte a executar o fluxo de trabalho. |

Uma vista de fluxo de trabalho aberta atualiza-se automaticamente à medida que a execução avança, pelo que os estados apresentados se mantêm atuais sem ter de recarregar a página.

### Passos abandonados

Um passo é marcado como **abandonado** quando o que o estava a executar desapareceu a meio da execução — na maioria dos casos porque alguém premiu **Parar** ou porque uma manutenção da plataforma interrompeu a execução. A duração do passo deixa de aumentar e a descrição do estado explica o que aconteceu.

Um passo abandonado não foi concluído e não produziu resultados. Não é um passo lento nem um problema com os seus dados ou a sua configuração.

Para retomar o trabalho, pode [**Retomar**](#pausar-parar-e-retomar) a execução — o passo abandonado é executado novamente — ou voltar a executar todo o fluxo de trabalho. Ambas as opções são seguras.

### Passos interrompidos

Se o servidor que executa um passo se perder a meio da execução, o PlaidCloud volta a executar o passo automaticamente quando é seguro repeti-lo: um passo que substitui o seu resultado acaba com o mesmo resultado de uma única execução limpa, pelo que não há nada a verificar.

Um passo que não pode ser repetido com segurança não é executado novamente. Falha uma vez com uma mensagem **Interrompido**, porque executá-lo uma segunda vez poderia duplicar o que a primeira tentativa já escreveu. Os passos que escrevem resultados com `{date}` no nome ou no caminho são considerados não seguros para repetir, pois uma nova execução poderia corresponder a uma data diferente. Para recuperar, verifique no destino do passo o que a primeira tentativa escreveu, limpe-o se necessário e, em seguida, [volte a executar o passo](/pt-pt/guides/workflows/running-one-step-in-a-workflow/) ou **Retome** a execução.

### Passos que nunca começam

Se nenhum worker aceitar a tarefa de um passo de importação ou de dimensão em cerca de 40 minutos, o passo falha em vez de apresentar **Em execução** até ao tempo limite de 24 horas. Se um worker iniciou a tarefa e depois desapareceu, o passo também falha, com uma mensagem a indicar que o worker parou. Ambas as mensagens indicam "Utilize Executar a partir daqui para tentar novamente."

## Pausar, parar e retomar

Enquanto um fluxo de trabalho está em execução, pode **Pausar**, para que os passos em curso terminem e os novos passos aguardem, ou **Parar**, o que cancela os passos em fila e quaisquer tarefas de importação ou exportação ainda em execução. Os passos de importação e de dimensão que ainda estavam em fila são cancelados de forma limpa, para que não atrasem importações e carregamentos de dimensões posteriores na área de trabalho.

**Retomar** recupera uma execução em pausa, parada ou com falha a partir do ponto onde ficou, em vez de recomeçar. Está disponível sempre que a última execução de um fluxo de trabalho terminou num estado de pausa, paragem ou erro.

O significado de "a partir do ponto onde ficou" depende da forma como o fluxo de trabalho é executado:

| Execução | Ao retomar |
|---|---|
| Em série | Recomeça no passo que estava em execução quando a execução terminou e continua a partir daí. Se esse passo estiver dentro de um grupo, Retomar recupera todo o grupo de nível superior que o contém: os passos do grupo que já terminaram com êxito ficam inalterados, os restantes são executados e a execução continua após o grupo. |
| Em paralelo | Volta a executar todos os passos que ainda não tinham terminado com êxito e deixa inalterados os passos concluídos. |
| Avançado (grafo) | Volta a executar o nó que falhou e tudo o que ainda está à espera dele, e deixa inalterados os nós concluídos. |

Os passos que chamam outro fluxo de trabalho — **Run Model**, **Conditional Run Model** e **Loop Model** — retomam o fluxo de trabalho que chamam em vez de o reiniciar, por muitos níveis de aninhamento que existam. Um passo de ciclo retoma a iteração que foi interrompida e ignora as iterações já concluídas.

Quando retoma um fluxo de trabalho que foi executado como **filho aninhado** de outro — um invocado por um passo **Run Model** num fluxo de trabalho principal — o PlaidCloud disponibiliza **Retomar a partir do topo da cadeia**. Retomar o filho isoladamente não permite continuar a orquestração do fluxo principal, pelo que esta opção retoma antes o fluxo principal de nível superior — a raiz da cadeia — e continua toda a cadeia a partir do ponto onde parou. Retomar um fluxo de trabalho de nível superior não sofre alterações. O topo da cadeia é determinado dentro do mesmo projeto: uma cadeia que passa para outro projeto é retomada a partir do topo da parte que está no projeto.

Retomar continua sempre a execução **original**. Volta a executar todos os passos dessa execução que não terminaram com êxito — um passo que falhou ou foi abandonado é executado novamente, e não tratado como concluído — e voltar a executar um passo individual entretanto não altera o que Retomar recupera a seguir.

Uma execução retomada é registada como uma **nova execução** no histórico de execuções do fluxo de trabalho, contendo apenas os passos que voltou a executar. A execução original mantém a sua própria entrada no histórico.

:::note
Um passo de ciclo faz corresponder as iterações concluídas pelos valores das respetivas variáveis. Se os dados sobre os quais o ciclo itera tiverem mudado entre a execução original e a retoma, as iterações que já não consegue fazer corresponder são executadas novamente em vez de ignoradas.
:::
