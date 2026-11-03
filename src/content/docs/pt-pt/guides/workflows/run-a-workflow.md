---
title: Executar um fluxo de trabalho
description: Execute manualmente ou a pedido um fluxo de trabalho do PlaidCloud, acompanhe o estado de cada passo e pause, pare ou retome uma execução a partir do ponto onde ficou.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Pode iniciar uma execução completa de um fluxo de trabalho clicando no ícone de execução na hierarquia **Fluxos de trabalho** ou selecionando **Run All** no menu **Ações** de um fluxo de trabalho específico.



Também pode clicar no botão **Toggle Start/Stop** na parte superior da tabela de fluxos de trabalho. Este botão de alternância para um fluxo de trabalho em execução ou inicia um fluxo de trabalho.

Se clicar em **Executar** num fluxo de trabalho que já está em execução, o PlaidCloud informa-o disso em vez de iniciar uma segunda execução.

## Escolher um modo de lançamento

Cada execução tem um modo de lançamento ERP. Para escolher um no PlaidCloud, utilize **Executar com modo de lançamento** no menu de contexto de um fluxo de trabalho ou o botão de modo de execução na área de desenho do fluxo de trabalho; um simples **Iniciar fluxo de trabalho** ou **Executar fluxo de trabalho** pede o modo Real, sujeito ainda ao limite do projeto descrito abaixo. Também pode escolher o modo ao iniciar uma execução através da API de execução ou do assistente.

| Modo | O que acontece |
|---|---|
| Real | Os passos de lançamento fazem os lançamentos exatamente como sempre fizeram. É o modo predefinido. |
| Simular | Cada passo de lançamento ERP constrói e valida exatamente o que lançaria, não confirma nada e nunca contacta o ERP. Os lançamentos que seriam feitos ficam registados no [Histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/), marcados como simulados, para que possa revê-los antes de executar em modo real. |
| Desligado | Os passos de lançamento são ignorados por completo. |

Um projeto tem também o seu próprio limite de modo de lançamento, definido através da API de projetos ou do assistente por qualquer membro com acesso de escrita a um projeto desbloqueado. O limite só torna uma execução mais segura, nunca mais permissiva: o modo efetivo de uma execução é o mais restritivo entre o modo que escolheu e o limite do projeto, pelo que um projeto limitado a Simular continua simulado mesmo que inicie a execução em modo Real.

Um [evento agendado](/pt-pt/administration/scheduled-events/event-scheduler/#modo-de-lançamento-no-erp) mantém o seu próprio modo de lançamento, pelo que um agendamento definido para Simular é executado em simulação de cada vez que é disparado.

O modo propaga-se a tudo o que a execução toca. Um subfluxo de trabalho, uma macro e um passo **Run Model**, **Conditional Run Model** ou **Loop Model** herdam todos o modo da execução principal, tal como uma execução que [retome](#pausar-parar-e-retomar) após uma paragem — uma execução simulada não pode lançar realmente em lado nenhum no seu interior.

:::caution
Os passos de lançamento SAP, de anexos SAP e de RFC SAP genéricos não fazem simulação. Em Simular ou Desligado, são ignorados por completo, porque as próprias sinalizações de teste do SAP continuam a abrir uma ligação real ao SAP — ignorar o passo é a única forma de uma execução simulada nunca chegar ao SAP.
:::

:::note
Um passo individual de lançamento ERP tem também a sua própria definição Validate Only (designada Preview ou Test Only Mode em alguns passos), independente do modo de lançamento da execução acima. O editor de passos guarda-a sempre de forma explícita. Uma configuração de passo escrita de outra forma — a API REST, o MCP ou uma importação de pacote de fluxo de trabalho — que omita totalmente a definição passa agora também a assumir por predefinição uma pré-visualização em vez de um lançamento real.
:::

## Autorizar o projeto a lançar

Uma execução de fluxo de trabalho lança no ERP como o projeto, não como a pessoa que a iniciou. Antes de uma execução poder lançar, o projeto precisa de uma autorização para cada ligação e ambiente ERP que os seus passos de lançamento utilizam. Sem ela, o passo falha com "This project isn't authorized to post to connection …", indicando a ligação e o ambiente. Os passos **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** e **Call SAP RFC** não precisam de uma.

Para autorizar um projeto, abra a respetiva página inicial e selecione **Autorizações de escrita no ERP** em **Lançamento ERP**. Cada linha é uma ligação num ambiente. Marque **Autorizado** para permitir que o projeto lance aí, ou desmarque para impedir. **Autorizado por** e **Autorizado em** mostram quem autorizou por último e quando.

- O botão é apresentado aos Arquitetos do projeto e aos administradores da área de trabalho, mas apenas um Arquiteto pode alterar uma autorização, e só enquanto o projeto estiver desbloqueado. Um administrador da área de trabalho que não seja Arquiteto pode primeiro adicionar-se como tal.
- Selecionar uma linha para autorizar ou limpar não recarrega a lista: a posição de deslocamento e qualquer ordenação de colunas que tenha escolhido mantêm-se. A janela pode ser redimensionada e a nota sobre projetos públicos é apresentada na íntegra.
- Para autorizar uma ligação, também precisa de acesso de escrita à mesma: é o proprietário ou a ligação é partilhada consigo pelo nome ou através de um dos seus grupos de segurança. Uma ligação definida para **Todos os membros da área de trabalho** não conta.
- Um projeto definido para **Todos os membros da área de trabalho** é autorizado como qualquer outro. Todos os membros são Arquitetos do mesmo, pelo que qualquer membro com acesso de escrita a uma ligação pode autorizar o projeto para essa ligação. Depois de autorizado, qualquer membro pode lançar nessa ligação a partir dos fluxos de trabalho do projeto, e a janela indica-o acima da grelha.
- Um projeto copiado, ou criado a partir de um arquivo de projeto, começa sem autorizações. Autorize a cópia antes de esta lançar.

## Acompanhar o estado de um passo

Enquanto um fluxo de trabalho é executado, cada passo apresenta um ícone de estado que mostra em que ponto se encontra, juntamente com há quanto tempo está em execução. Passe o rato sobre o ícone para ver a mensagem associada.

| Estado | O que significa |
|---|---|
| Em espera | O passo está em fila e ainda não começou. |
| Em execução | O passo está a trabalhar e a sua duração vai aumentando. |
| Concluído | O passo terminou com êxito. |
| Aviso | O passo terminou, mas assinalou algo que vale a pena ler no [registo do fluxo de trabalho](/pt-pt/guides/workflows/viewing-workflow-log/). |
| Erro | O passo falhou. Consulte [Gerir erros de passos](/pt-pt/guides/workflows/managing-step-errors/). |
| Ignorado | O passo foi saltado — está desativado ou as suas condições de execução não foram cumpridas. Consulte [Ignorar passos num fluxo de trabalho](/pt-pt/guides/workflows/skip-steps-in-a-workflow/). |
| Continuado | O passo falhou, mas está definido para continuar em caso de erro, pelo que o fluxo de trabalho prosseguiu. Consulte [Continuar em caso de erro](/pt-pt/guides/workflows/continue-on-error/). |
| Parado | A execução foi parada antes de o passo poder terminar. |
| Abandonado | A execução do passo foi interrompida, pelo que nunca terminará. Retome a execução ou volte a executar o fluxo de trabalho. |

Uma vista de fluxo de trabalho aberta é atualizada automaticamente à medida que uma execução progride, pelo que os estados que está a ver se mantêm atuais sem recarregar a página.

### Passos abandonados

Um passo é marcado como **abandonado** quando o que o estava a executar desapareceu a meio da execução — mais frequentemente porque alguém premiu **Parar** ou porque uma manutenção da plataforma interrompeu a execução. A duração do passo deixa de aumentar e a descrição do estado explica o que aconteceu.

Um passo abandonado não foi concluído e não produziu qualquer resultado. Não é um passo lento, nem um problema com os seus dados ou com a sua configuração.

Para retomar o trabalho, [**Retome**](#pausar-parar-e-retomar) a execução — o passo abandonado é executado novamente — ou volte a executar o fluxo de trabalho completo. Ambas as opções são seguras.

### Passos interrompidos

Se o servidor que executa um passo se perder a meio da execução, o PlaidCloud volta a executar o passo automaticamente quando é seguro repeti-lo: um passo que substitui o seu resultado acaba com o mesmo resultado que uma única execução limpa, pelo que não tem nada a verificar.

Um passo que não pode ser repetido em segurança não é executado novamente. Falha uma vez com uma mensagem de **interrompido**, porque executá-lo uma segunda vez poderia duplicar o que a primeira tentativa já escreveu. Os passos que escrevem resultados com `{date}` no nome ou no caminho contam como não seguros para repetir, uma vez que uma nova execução poderia cair numa data diferente. Para recuperar, verifique no destino do passo o que a primeira tentativa escreveu, limpe-o se necessário e depois [volte a executar o passo](/pt-pt/guides/workflows/running-one-step-in-a-workflow/) ou **Retome** a execução.

### Passos que nunca arrancam

Se nenhum worker aceitar a tarefa de um passo de importação ou de dimensão em cerca de 40 minutos, o passo falha em vez de mostrar **Em execução** até ao limite de 24 horas. Se um worker iniciou a tarefa e depois desapareceu, o passo também falha, com uma mensagem a indicar que o worker parou. Ambas as mensagens dizem "Use Run from here to retry."

## Pausar, parar e retomar

Enquanto um fluxo de trabalho está em execução, pode **Pausar**, para que os passos em curso terminem e os novos passos aguardem, ou **Parar**, o que cancela os passos que estavam em fila e quaisquer tarefas de importação ou exportação que ainda estejam em execução. Os passos de importação e de dimensão que ainda estavam em fila são cancelados de forma limpa, para não atrasarem as importações e os carregamentos de dimensões seguintes na área de trabalho.

**Retomar** recomeça uma execução pausada, parada ou falhada a partir do ponto onde ficou, em vez de começar de novo. Está disponível sempre que a última execução de um fluxo de trabalho terminou num estado de pausa, paragem ou erro.

O que significa "a partir do ponto onde ficou" depende da forma como o fluxo de trabalho é executado:

| Execução | Ao retomar |
|---|---|
| Em série | Recomeça no passo que estava em execução quando a execução terminou e continua a partir daí. Se esse passo estiver dentro de um grupo, Retomar recomeça todo o grupo de nível superior que o contém: os passos do grupo que já terminaram com êxito são deixados como estão, os restantes são executados e a execução continua após o grupo. |
| Em paralelo | Volta a executar todos os passos que ainda não tinham terminado com êxito e deixa os passos concluídos como estão. |
| Avançada (grafo) | Volta a executar o nó que falhou e tudo o que ainda aguarda por ele, e deixa os nós concluídos como estão. |

Os passos que chamam outro fluxo de trabalho — **Run Model**, **Conditional Run Model** e **Loop Model** — retomam o fluxo de trabalho que chamam em vez de o reiniciar, por mais níveis de aninhamento que existam. Um passo de ciclo retoma a iteração que foi interrompida e salta as iterações que já foram concluídas.

Quando retoma um fluxo de trabalho que foi executado como **filho aninhado** de outro — um que um passo **Run Model** de um fluxo principal invocou — o PlaidCloud oferece **Retomar a partir do topo da cadeia**. Retomar o filho isoladamente não consegue continuar a orquestração do fluxo principal, pelo que esta opção retoma o fluxo principal de nível superior — a raiz da cadeia — e continua toda a cadeia a partir de onde parou. Retomar um fluxo de trabalho de nível superior não se altera. O topo da cadeia é resolvido dentro do mesmo projeto: uma cadeia que atravessa outro projeto é retomada a partir do topo da parte que está dentro do projeto.

Retomar continua sempre a execução **original**. Volta a executar todos os passos dessa execução que não terminaram com êxito — um passo que falhou ou foi abandonado é executado novamente, não tratado como concluído — e voltar a executar um passo individual isoladamente entretanto não altera o que Retomar recolhe a seguir.

Uma execução retomada é registada como uma **nova execução** no histórico de execuções do fluxo de trabalho, contendo apenas os passos que voltou a executar. A execução original mantém a sua própria entrada no histórico.

:::note
Um passo de ciclo faz corresponder as iterações concluídas pelos valores das suas variáveis. Se os dados sobre os quais o ciclo itera mudaram entre a execução original e a retoma, as iterações que já não consegue fazer corresponder são executadas novamente em vez de saltadas.
:::
