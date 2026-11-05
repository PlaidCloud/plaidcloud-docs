---
title: Executar um fluxo de trabalho
description: Execute um fluxo de trabalho do PlaidCloud manualmente ou a pedido, acompanhe o estado de cada passo e pause, pare ou retome uma execução a partir do ponto em que ficou.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Pode iniciar uma execução completa de um fluxo de trabalho clicando no ícone de execução na hierarquia de **Fluxos de trabalho** ou selecionando **Run All** no menu **Ações** de um fluxo de trabalho específico.



Também pode clicar no botão **Toggle Start/Stop** na parte superior da tabela de fluxos de trabalho. Este botão alternável para um fluxo de trabalho em execução ou inicia um fluxo de trabalho.

Se clicar em **Executar** num fluxo de trabalho que já está em execução, o PlaidCloud informa-o disso em vez de iniciar uma segunda execução.

## Escolher um modo de lançamento

Cada execução tem um modo de lançamento no ERP. Para escolher um no PlaidCloud, utilize **Executar com modo de lançamento** no menu de contexto de um fluxo de trabalho ou o botão de modo de execução na área de desenho do fluxo de trabalho; **Iniciar fluxo de trabalho** ou **Executar fluxo de trabalho** simples pedem o modo Real, sujeito ainda ao limite do projeto descrito abaixo. Também pode escolher o modo ao iniciar uma execução através da API de execução ou do assistente.

| Modo | O que acontece |
|---|---|
| Real | Os passos de lançamento lançam exatamente como sempre fizeram. Este é o modo predefinido. |
| Simulação | Cada passo de lançamento no ERP constrói e valida exatamente o que lançaria, mas não confirma nada e nunca contacta o ERP. Os lançamentos que seriam efetuados ficam registados no [Histórico de lançamentos no ERP](/pt-pt/guides/connections/erp-post-history/), marcados como simulados, para que possa revê-los antes de executar em modo real. |
| Desligado | Os passos de lançamento são totalmente ignorados. |

Um projeto tem também o seu próprio limite de modo de lançamento, definido através da API de projetos ou do assistente por qualquer membro com acesso de escrita a um projeto desbloqueado. O limite só torna uma execução mais segura, nunca mais permissiva: o modo efetivo de uma execução é o mais restritivo entre o modo que escolheu e o limite do projeto, pelo que um projeto limitado a Simulação continua simulado mesmo que inicie a execução em modo Real.

Um [evento agendado](/pt-pt/administration/scheduled-events/event-scheduler/#modo-de-lançamento-no-erp) mantém o seu próprio modo de lançamento, pelo que um agendamento definido para Simulação é executado em simulação sempre que é acionado.

O modo estende-se a tudo o que a execução toca. Um subfluxo de trabalho, uma macro e os passos **Run Model**, **Conditional Run Model** ou **Loop Model** herdam todos o modo da execução principal, tal como uma execução que [retome](#pausar-parar-e-retomar) após uma paragem: uma execução simulada não consegue lançar a sério em lado nenhum no seu interior.

:::caution
Os passos de lançamento SAP, de anexos SAP e de RFC SAP genéricas não fazem execução de teste. Em Simulação ou Desligado, são ignorados por completo, porque as próprias indicações de teste do SAP continuam a abrir uma ligação real ao SAP: ignorar o passo é a única forma de uma execução simulada nunca chegar ao SAP.
:::

:::note
Cada passo individual de lançamento no ERP tem também a sua própria definição Validate Only (com a etiqueta Preview ou Test Only Mode em alguns passos), independente do modo de lançamento da execução acima. O editor de passos guarda sempre esta definição de forma explícita. Uma configuração de passo escrita de outra forma — a API REST, o MCP ou uma importação de pacote de fluxo de trabalho — que omita totalmente a definição passa agora também a ter como predefinição uma pré-visualização em vez de um lançamento real.
:::

## Autorizar o projeto a lançar

Uma execução de fluxo de trabalho lança num ERP como o projeto, não como a pessoa que a iniciou. Antes de uma execução poder lançar, o projeto precisa de uma autorização para cada ligação e ambiente de ERP que os seus passos de lançamento utilizam. Sem ela, o passo falha com "Este projeto não está autorizado a lançar na ligação …", indicando a ligação e o ambiente. Os passos **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** e **Call SAP RFC** não precisam de uma.

Para autorizar um projeto, abra a sua página inicial e selecione **Autorizações de escrita no ERP** em **Lançamento ERP**. Cada linha corresponde a uma ligação num ambiente. Assinale **Autorizado** para permitir que o projeto lance aí, ou desassinale para impedir. **Autorizado por** e **Autorizado em** mostram quem autorizou por último e quando.

- O botão é apresentado aos Arquitetos do projeto e aos administradores da área de trabalho, mas só um Arquiteto pode alterar uma autorização, e apenas enquanto o projeto estiver desbloqueado. Um administrador da área de trabalho que não seja Arquiteto pode primeiro adicionar-se como tal.
- Selecionar uma linha para autorizar ou limpar uma autorização não recarrega a lista: a posição de deslocamento e qualquer ordenação de colunas que tenha escolhido mantêm-se. A janela pode ser redimensionada e a nota sobre projetos públicos é apresentada na íntegra.
- Para autorizar uma ligação, também precisa de ter acesso de escrita à mesma: é o proprietário, ou esta é partilhada consigo por nome ou através de um dos seus grupos de segurança. Uma ligação definida para **Todos os membros da área de trabalho** não conta.
- Um projeto definido para **Todos os membros da área de trabalho** é autorizado como qualquer outro. Todos os membros são Arquitetos do mesmo, pelo que qualquer membro com acesso de escrita a uma ligação pode autorizar o projeto para essa ligação. Depois de autorizado, qualquer membro pode lançar nessa ligação a partir dos fluxos de trabalho do projeto, e a janela di-lo acima da grelha.
- Uma nova cópia privada para si, feita com dados de tabelas ou membros de dimensões, mantém as autorizações da origem que poderia conceder a si próprio e fica em Simulação se a origem estava em modo Real — consulte [Autorizações de escrita no ERP na cópia](/pt-pt/guides/projects/managing-projects/#autorizações-de-escrita-no-erp-na-cópia). Qualquer outra cópia, ou um projeto criado a partir de um arquivo de projeto, começa sem autorizações. Autorize-o antes de lançar.

## Acompanhar o estado de um passo

Enquanto um fluxo de trabalho é executado, cada passo apresenta um ícone de estado que indica em que ponto se encontra, juntamente com o tempo que está em execução. Passe o cursor sobre o ícone para ver a mensagem associada.

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
| Abandonado | A execução do passo foi interrompida, pelo que nunca terminará. Retome a execução ou volte a executar o fluxo de trabalho. |

Uma vista de fluxo de trabalho aberta atualiza-se automaticamente à medida que uma execução avança, pelo que os estados que está a ver se mantêm atuais sem recarregar a página.

### Passos abandonados

Um passo é marcado como **abandonado** quando aquilo que o estava a executar desapareceu a meio da execução — o mais frequente é alguém ter premido **Parar**, ou uma manutenção da plataforma ter interrompido a execução. A duração do passo deixa de aumentar e a dica do estado explica o que aconteceu.

Um passo abandonado não foi concluído e não produziu qualquer resultado. Não é um passo lento, nem um problema com os seus dados ou com a sua configuração.

Para retomar o trabalho, [**Retome**](#pausar-parar-e-retomar) a execução — o passo abandonado é executado de novo — ou volte a executar o fluxo de trabalho completo. Ambas as opções são seguras.

### Passos interrompidos

Se o servidor que executa um passo se perder a meio da execução, o PlaidCloud volta a executar o passo automaticamente quando é seguro repeti-lo: um passo que substitui o seu resultado acaba com o mesmo resultado de uma única execução limpa, pelo que não tem nada a verificar.

Um passo que não pode ser repetido em segurança não é executado de novo. Falha uma vez com uma mensagem de **interrompido**, porque executá-lo uma segunda vez poderia duplicar o que a primeira tentativa já escreveu. Os passos que escrevem resultados com `{date}` no nome ou no caminho contam como não seguros de repetir, uma vez que uma nova execução poderia cair numa data diferente. Para recuperar, verifique no destino do passo o que a primeira tentativa escreveu, limpe-o se necessário e, em seguida, [volte a executar o passo](/pt-pt/guides/workflows/running-one-step-in-a-workflow/) ou **Retome** a execução.

### Passos que nunca arrancam

Enquanto um passo aguarda por um worker, a sua mensagem de estado indica "Waiting for a worker… N min. No import worker has picked this step up yet." (o tipo de worker corresponde ao passo, como importação ou exportação). A mensagem desaparece quando o trabalho começa.

Se o trabalho de um passo nunca puder arrancar, o passo falha com o motivo em vez de esperar indefinidamente:

| Causa | Falha ao fim de cerca de |
|---|---|
| Nenhum worker assume o trabalho de um passo de importação ou de dimensão | 40 minutos |
| O pod do passo fica preso em Pending | 20 minutos |
| Não é possível obter a imagem do passo | 5 minutos |
| Não é criado nenhum pod para o passo | 20 minutos |
| Nenhum runner assume uma sincronização de conector (Singer) | 30 minutos |

A mensagem de sincronização de conector indica a sincronização. Se um worker iniciou o trabalho e depois desapareceu, o passo também falha, com uma mensagem a indicar que o worker parou. As mensagens de importação e de dimensão dizem "Use Run from here to retry."

## Pausar, parar e retomar

Enquanto um fluxo de trabalho está em execução, pode **Pausar** o mesmo, para que os passos em curso terminem e os novos passos aguardem, ou **Parar** o mesmo, o que cancela os passos que estavam em fila e quaisquer trabalhos de importação ou exportação que ainda estejam em execução. Os passos de importação e de dimensão que ainda estavam em fila são cancelados de forma limpa, para não bloquearem as importações e os carregamentos de dimensões seguintes na área de trabalho. Parar também para as sincronizações de conector (Singer) do fluxo de trabalho que estejam em fila ou em execução, para que uma sincronização não continue a ser executada depois de o fluxo de trabalho ter parado.

**Retomar** recomeça uma execução em pausa, parada ou falhada a partir do ponto em que ficou, em vez de começar de novo. Está disponível sempre que a última execução de um fluxo de trabalho terminou num estado de pausa, paragem ou erro.

O que significa "o ponto em que ficou" depende da forma como o fluxo de trabalho é executado:

| Execução | Ao retomar |
|---|---|
| Série | Recomeça no passo que estava em execução quando a execução terminou e continua a partir daí. Se esse passo estiver dentro de um grupo, Retomar abrange todo o grupo de nível superior que o contém: os passos do grupo que já terminaram com êxito são deixados como estão, os restantes são executados e a execução continua após o grupo. |
| Paralelo | Volta a executar todos os passos que ainda não tinham terminado com êxito e deixa os passos concluídos como estão. |
| Avançado (grafo) | Volta a executar o nó que falhou e tudo o que ainda aguarda por ele, e deixa os nós concluídos como estão. |

Os passos que chamam outro fluxo de trabalho — **Run Model**, **Conditional Run Model** e **Loop Model** — retomam o fluxo de trabalho que chamam em vez de o reiniciarem, por muitos níveis de aninhamento que tenha. Um passo de ciclo retoma a iteração que foi interrompida e salta as iterações que já foram concluídas.

Quando retoma um fluxo de trabalho que foi executado como **filho aninhado** de outro — um invocado por um passo **Run Model** num fluxo principal — o PlaidCloud oferece **Retomar a partir do topo da cadeia**. Retomar o filho isoladamente não consegue continuar a orquestração do fluxo principal, pelo que esta opção retoma o fluxo principal de nível superior — a raiz da cadeia — e continua toda a cadeia a partir do ponto onde parou. Retomar um fluxo de trabalho de nível superior mantém-se inalterado. O topo da cadeia é resolvido dentro do mesmo projeto: uma cadeia que passa para outro projeto retoma a partir do topo da parte que se encontra no projeto.

Retomar continua sempre a execução **original**. Volta a executar todos os passos dessa execução que não terminaram com êxito — um passo que falhou ou foi abandonado é executado de novo, não é tratado como concluído — e voltar a executar um passo individual isoladamente entretanto não altera o que Retomar executa a seguir.

Uma execução retomada é registada como uma **nova execução** no histórico de execuções do fluxo de trabalho, contendo apenas os passos que voltou a executar. A execução original mantém a sua própria entrada no histórico.

:::note
Um passo de ciclo faz corresponder as iterações concluídas pelos valores das suas variáveis. Se os dados sobre os quais o ciclo itera mudaram entre a execução original e a retoma, as iterações que já não consegue fazer corresponder são executadas de novo em vez de saltadas.
:::
