---
title: Executar um fluxo de trabalho
description: Execute um fluxo de trabalho do PlaidCloud manualmente ou sob demanda, acompanhe o status de cada etapa e pause, pare ou retome uma execução do ponto em que parou.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Você pode disparar a execução completa de um fluxo de trabalho clicando no ícone de execução na hierarquia **Fluxos de trabalho** ou selecionando **Run All** no menu **Ações** de um fluxo de trabalho específico.



Você também pode clicar no botão **Toggle Start/Stop** na parte superior da tabela de fluxos de trabalho. Esse botão alternável interrompe um fluxo de trabalho em execução ou inicia um fluxo de trabalho.

Se você clicar em **Executar** em um fluxo de trabalho que já está em execução, o PlaidCloud avisa isso em vez de iniciar uma segunda execução.

## Escolher um modo de lançamento

Toda execução tem um modo de lançamento no ERP. Para escolher um no PlaidCloud, use **Executar com modo de lançamento** no menu de contexto (clique com o botão direito) de um fluxo de trabalho, ou o botão de modo de execução na tela do fluxo de trabalho; um simples **Iniciar fluxo de trabalho** ou **Executar fluxo de trabalho** solicita Live, ainda sujeito ao limite do projeto descrito abaixo. Você também pode escolher o modo ao iniciar uma execução pela API de execução ou pelo assistente.

| Modo | O que acontece |
|---|---|
| Live | As etapas de lançamento fazem o lançamento exatamente como sempre fizeram. Este é o padrão. |
| Simulate | Cada etapa de lançamento no ERP monta e valida exatamente o que lançaria, mas não confirma nada e nunca contata o ERP. Os lançamentos que seriam feitos ficam registrados no [Histórico de lançamentos no ERP](/pt-br/guides/connections/erp-post-history/), marcados como simulados, para que você possa revisá-los antes de executar em modo Live. |
| Off | As etapas de lançamento são ignoradas por completo. |

Um projeto também tem seu próprio limite de modo de lançamento, definido pela API de projetos ou pelo assistente por qualquer membro com acesso de gravação a um projeto desbloqueado. O limite só torna uma execução mais segura, nunca mais permissiva: o modo efetivo de uma execução é o mais restritivo entre o modo que você escolheu e o limite do projeto; portanto, um projeto limitado a Simulate continua simulado mesmo que você inicie a execução como Live.

Um [evento agendado](/pt-br/administration/scheduled-events/event-scheduler/#modo-de-lançamento-no-erp) mantém seu próprio modo de lançamento; assim, um agendamento definido como Simulate executa de forma simulada toda vez que é disparado.

O modo se propaga a tudo o que a execução toca. Um subfluxo de trabalho, uma macro e uma etapa **Run Model**, **Conditional Run Model** ou **Loop Model** herdam o modo da execução pai, e o mesmo vale para uma execução que você [retoma](#pausar-parar-e-retomar) após uma parada: uma execução simulada não consegue fazer lançamentos reais em nenhum ponto dela.

:::caution
As etapas de lançamento SAP, de anexo SAP e de RFC SAP genérico não fazem simulação. Em Simulate ou Off, elas são ignoradas por completo, porque as próprias flags de teste do SAP ainda abrem uma conexão real com o SAP; ignorar a etapa é a única forma de garantir que uma execução simulada nunca chegue ao SAP.
:::

:::note
Cada etapa individual de lançamento no ERP também tem sua própria configuração Validate Only (chamada Preview ou Test Only Mode em algumas etapas), independente do modo de lançamento da execução descrito acima. O editor de etapas sempre a salva de forma explícita. Uma configuração de etapa escrita de outra forma (pela API REST, pelo MCP ou por uma importação de pacote de fluxo de trabalho) que omita totalmente essa configuração agora também assume como padrão uma pré-visualização, em vez de um lançamento real.
:::

## Autorizar o projeto a fazer lançamentos

Uma execução de fluxo de trabalho faz lançamentos em um ERP como o projeto, não como a pessoa que a iniciou. Antes que uma execução possa fazer lançamentos, o projeto precisa de uma autorização para cada conexão e ambiente de ERP que suas etapas de lançamento usam. Sem ela, a etapa falha com "This project isn't authorized to post to connection …", indicando a conexão e o ambiente. As etapas **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** e **Call SAP RFC** não precisam de autorização.

Para autorizar um projeto, abra a página inicial dele e selecione **Autorizações de gravação no ERP** em **Lançamento no ERP**. Cada linha corresponde a uma conexão em um ambiente. Marque **Autorizado** para permitir que o projeto faça lançamentos ali, ou desmarque para impedir. **Autorizado por** e **Autorizado em** mostram quem autorizou por último e quando.

- O botão é exibido para os Arquitetos do projeto e para os administradores do espaço de trabalho, mas somente um Arquiteto pode alterar uma autorização, e somente enquanto o projeto estiver desbloqueado. Um administrador do espaço de trabalho que não é Arquiteto pode primeiro se adicionar como Arquiteto.
- Selecionar uma linha para autorizar ou limpar a autorização não recarrega a lista: a posição de rolagem e qualquer ordenação de coluna que você escolheu permanecem como estão. A janela pode ser redimensionada, e a observação sobre projetos públicos é exibida por inteiro, com quebra de linha.
- Para autorizar uma conexão, você também precisa ter acesso de gravação a ela: você é o proprietário, ou ela é compartilhada com você pelo nome ou por meio de um dos seus grupos de segurança. Uma conexão definida como **Todos os membros do espaço de trabalho** não conta.
- Um projeto definido como **Todos os membros do espaço de trabalho** é autorizado como qualquer outro. Todo membro é Arquiteto dele; portanto, qualquer membro com acesso de gravação a uma conexão pode autorizar o projeto para ela. Depois de autorizado, qualquer membro pode fazer lançamentos naquela conexão a partir dos fluxos de trabalho do projeto, e a janela informa isso acima da grade.
- Uma nova cópia privada para você, feita com dados de tabela ou membros de dimensão, mantém as autorizações da origem que você mesmo poderia conceder e chega em Simulate se a origem estava em Live; veja [Autorizações de gravação no ERP na cópia](/pt-br/guides/projects/managing-projects/#autorizações-de-gravação-no-erp-na-cópia). Qualquer outra cópia, ou um projeto criado a partir de um arquivo de projeto, começa sem autorizações. Autorize-o antes de ele fazer lançamentos.

## Acompanhar o status de uma etapa

Enquanto um fluxo de trabalho é executado, cada etapa exibe um ícone de status mostrando em que ponto ela está, junto com o tempo que ela está em execução. Passe o mouse sobre o ícone para ver a mensagem por trás dele.

| Status | O que significa |
|---|---|
| Aguardando | A etapa está na fila e ainda não começou. |
| Em execução | A etapa está em andamento, e sua duração aumenta conforme ela avança. |
| Concluída | A etapa terminou com sucesso. |
| Aviso | A etapa terminou, mas sinalizou algo que vale a pena ler no [log do fluxo de trabalho](/pt-br/guides/workflows/viewing-workflow-log/). |
| Erro | A etapa falhou. Veja [Gerenciar erros de etapa](/pt-br/guides/workflows/managing-step-errors/). |
| Ignorada | A etapa foi pulada: está desativada ou suas condições de execução não foram atendidas. Veja [Pular etapas em um fluxo de trabalho](/pt-br/guides/workflows/skip-steps-in-a-workflow/). |
| Continuada | A etapa falhou, mas está configurada para continuar em caso de erro; por isso, o fluxo de trabalho prosseguiu. Veja [Continuar em caso de erro](/pt-br/guides/workflows/continue-on-error/). |
| Parada | A execução foi parada antes de a etapa terminar. |
| Abandonada | A execução da etapa foi interrompida, então ela nunca terminará. Retome a execução ou execute o fluxo de trabalho novamente. |

Uma visão aberta do fluxo de trabalho é atualizada automaticamente conforme a execução avança; assim, os status que você está vendo permanecem atuais sem recarregar a página.

### Etapas abandonadas

Uma etapa é marcada como **abandonada** quando o que a estava executando desapareceu no meio da execução, mais frequentemente porque alguém pressionou **Parar** ou porque uma manutenção da plataforma interrompeu a execução. A duração da etapa deixa de aumentar e a dica de status explica o que aconteceu.

Uma etapa abandonada não foi concluída e não gerou saída. Não é uma etapa lenta, nem um problema com seus dados ou sua configuração.

Para retomar o trabalho, [**Retome**](#pausar-parar-e-retomar) a execução (a etapa abandonada é executada novamente) ou execute o fluxo de trabalho inteiro de novo. Ambas as opções são seguras.

### Etapas interrompidas

Se o servidor que executa uma etapa for perdido no meio da execução, o PlaidCloud executa a etapa novamente de forma automática quando é seguro repeti-la: uma etapa que substitui sua saída termina com o mesmo resultado de uma única execução limpa, então você não precisa verificar nada.

Uma etapa que não pode ser repetida com segurança não é executada novamente. Ela falha uma vez com uma mensagem de **interrompida**, porque executá-la uma segunda vez poderia duplicar o que a primeira tentativa já gravou. Etapas que gravam saídas com `{date}` no nome ou no caminho contam como não seguras para repetir, pois uma nova execução poderia cair em uma data diferente. Para se recuperar, verifique no destino da etapa o que a primeira tentativa gravou, limpe-o se necessário e então [execute a etapa novamente](/pt-br/guides/workflows/running-one-step-in-a-workflow/) ou **Retome** a execução.

### Etapas que nunca começam

Enquanto uma etapa espera por um worker, a mensagem de status dela diz "Waiting for a worker… N min. No import worker has picked this step up yet." (o tipo de worker corresponde à etapa, como importação ou exportação). A mensagem desaparece quando o trabalho começa.

Se o job de uma etapa nunca puder começar, a etapa falha com o motivo em vez de esperar para sempre:

| Causa | Falha após cerca de |
|---|---|
| Nenhum worker assume o job de uma etapa de importação ou de dimensão | 40 minutos |
| O pod da etapa fica preso em Pending | 20 minutos |
| A imagem da etapa não pode ser baixada | 5 minutos |
| Nenhum pod é criado para a etapa | 20 minutos |
| Nenhum runner assume uma sincronização de conector (Singer) | 30 minutos |

A mensagem de sincronização de conector informa qual é a sincronização. Se um worker iniciou o job e depois desapareceu, a etapa também falha, com uma mensagem informando que o worker parou. As mensagens de importação e de dimensão dizem "Use Run from here to retry."

## Pausar, parar e retomar

Enquanto um fluxo de trabalho está em execução, você pode **Pausar** para que as etapas em andamento terminem e as novas aguardem, ou **Parar**, o que cancela as etapas que estavam na fila e quaisquer jobs de importação ou exportação ainda em execução. As etapas de importação e de dimensão que ainda estavam na fila são canceladas de forma limpa, para que não atrasem as importações e cargas de dimensão seguintes no espaço de trabalho. Parar também interrompe as sincronizações de conector (Singer) do fluxo de trabalho que estavam na fila ou em execução, para que uma sincronização não continue rodando depois que o fluxo de trabalho parou.

**Retomar** continua uma execução pausada, parada ou com falha do ponto em que ela parou, em vez de começar do zero. Está disponível sempre que a última execução de um fluxo de trabalho terminou em estado pausado, parado ou de erro.

O que significa "do ponto em que parou" depende de como o fluxo de trabalho é executado:

| Execução | Ao retomar |
|---|---|
| Serial | Reinicia na etapa que estava em execução quando a execução terminou e continua a partir dali. Se essa etapa estiver dentro de um grupo, Retomar assume o grupo de nível superior inteiro que a contém: as etapas do grupo que já terminaram com sucesso são deixadas como estão, as demais são executadas e a execução continua depois do grupo. |
| Paralela | Executa novamente todas as etapas que ainda não haviam terminado com sucesso e deixa as etapas concluídas como estão. |
| Avançada (grafo) | Executa novamente o nó que falhou e tudo o que ainda espera por ele, e deixa os nós concluídos como estão. |

As etapas que chamam outro fluxo de trabalho (**Run Model**, **Conditional Run Model** e **Loop Model**) retomam o fluxo de trabalho que chamam em vez de reiniciá-lo, por quantos níveis de aninhamento você tiver. Uma etapa de loop retoma a iteração que foi interrompida e pula as iterações que já foram concluídas.

Quando você usa Retomar em um fluxo de trabalho que foi executado como **filho aninhado** de outro (um chamado por uma etapa **Run Model** em um pai), o PlaidCloud oferece **Retomar do início da cadeia**. Retomar o filho isoladamente não consegue continuar a orquestração do pai; por isso, essa opção retoma o pai de nível superior, a raiz da cadeia, e continua toda a cadeia do ponto em que ela parou. Retomar um fluxo de trabalho de nível superior continua igual. O início da cadeia é resolvido dentro do mesmo projeto: uma cadeia que passa para outro projeto é retomada a partir do início da parte que está dentro do projeto.

Retomar sempre continua a execução **original**. Ele executa novamente todas as etapas dessa execução que não terminaram com sucesso (uma etapa que falhou ou foi abandonada é executada novamente, não tratada como concluída), e executar novamente uma etapa individual por conta própria nesse meio-tempo não altera o que Retomar assume em seguida.

Uma execução retomada é registrada como uma **nova execução** no histórico de execuções do fluxo de trabalho, contendo apenas as etapas que ela executou novamente. A execução original mantém sua própria entrada no histórico.

:::note
Uma etapa de loop associa suas iterações concluídas pelos valores das variáveis delas. Se os dados sobre os quais o loop itera mudaram entre a execução original e a retomada, as iterações que ele não consegue mais associar são executadas novamente em vez de puladas.
:::
