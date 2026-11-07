---
title: Executar um fluxo de trabalho
description: Execute um fluxo de trabalho do PlaidCloud manualmente ou sob demanda, acompanhe o status de cada etapa e pause, pare ou retome uma execução do ponto em que parou.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Você pode iniciar a execução completa de um fluxo de trabalho clicando no ícone de execução na hierarquia de **Fluxos de trabalho** ou selecionando **Run All** no menu **Ações** de um fluxo de trabalho específico.



Você também pode clicar no botão **Toggle Start/Stop** na parte superior da tabela de fluxos de trabalho. Esse botão alternado interrompe um fluxo de trabalho em execução ou inicia um fluxo de trabalho.

Se você clicar em **Executar** em um fluxo de trabalho que já está em execução, o PlaidCloud avisa isso em vez de iniciar uma segunda execução.

## Escolher um modo de lançamento

Toda execução tem um modo de lançamento no ERP. Para escolher um no PlaidCloud, use **Executar com modo de lançamento** no menu de clique com o botão direito de um fluxo de trabalho ou o botão de modo de execução na tela do fluxo de trabalho; um simples **Iniciar fluxo de trabalho** ou **Executar fluxo de trabalho** solicita o modo Real, ainda sujeito ao limite do projeto descrito abaixo. Você também pode escolher o modo ao iniciar uma execução pela API de execução ou pelo assistente.

| Modo | O que acontece |
|---|---|
| Real | As etapas de lançamento lançam exatamente como sempre fizeram. Este é o padrão. |
| Simulação | Cada etapa de lançamento no ERP monta e valida exatamente o que lançaria, depois não confirma nada e nunca entra em contato com o ERP. Os lançamentos simulados são registrados no [Histórico de lançamentos no ERP](/pt-br/guides/connections/erp-post-history/), marcados como simulados, para que você possa revisá-los antes de executar em modo real. |
| Desativado | As etapas de lançamento são ignoradas por completo. |

Um projeto também tem seu próprio limite de modo de lançamento, definido pela API do projeto ou pelo assistente por qualquer membro com acesso de gravação a um projeto desbloqueado. O limite só torna uma execução mais segura, nunca mais permissiva: o modo efetivo de uma execução é o mais restritivo entre o modo que você escolheu e o limite do projeto, então um projeto limitado a Simulação continua simulado mesmo que você inicie a execução em modo Real.

Um [evento agendado](/pt-br/administration/scheduled-events/event-scheduler/#modo-de-lançamento-no-erp) mantém seu próprio modo de lançamento, então um agendamento definido como Simulação é executado de forma simulada toda vez que dispara.

O modo se estende a tudo o que a execução toca. Um subfluxo de trabalho, uma macro e uma etapa **Run Model**, **Conditional Run Model** ou **Loop Model** herdam o modo da execução pai, assim como uma execução que você [retoma](#pausar-parar-e-retomar) após uma parada — uma execução simulada não consegue lançar de verdade em nenhum ponto dela.

:::caution
As etapas de lançamento SAP, de anexo SAP e de RFC SAP genérico não fazem execução de teste. Em Simulação ou Desativado, elas são ignoradas por completo, porque as próprias flags de teste do SAP ainda abrem uma conexão real com o SAP — ignorar a etapa é a única forma de uma execução simulada nunca chegar ao SAP.
:::

:::note
Uma etapa individual de lançamento no ERP também tem sua própria configuração Validate Only (chamada de Pré-visualização ou Test Only Mode em algumas etapas), independente do modo de lançamento da execução acima. O editor de etapas sempre a salva explicitamente. Uma configuração de etapa gravada de outra forma — a API REST, o MCP ou uma importação de pacote de fluxo de trabalho — que omita totalmente essa configuração agora também assume como padrão uma pré-visualização em vez de um lançamento real.
:::

## Autorizar o projeto a lançar

Uma execução de fluxo de trabalho lança em um ERP como o projeto, não como a pessoa que a iniciou. Antes que uma execução possa lançar, o projeto precisa de uma autorização para cada conexão e ambiente de ERP que suas etapas de lançamento usam. Sem ela, a etapa falha com "This project isn't authorized to post to connection …", informando a conexão e o ambiente. As etapas **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** e **Call SAP RFC** não precisam de uma.

Para autorizar um projeto, abra a página inicial dele e selecione **Autorizações de gravação no ERP** em **Lançamento no ERP**. Cada linha é uma conexão em um ambiente. Marque **Autorizado** para permitir que o projeto lance ali, ou desmarque para impedir. **Autorizado por** e **Autorizado em** mostram quem autorizou por último e quando.

- O botão é exibido para os Arquitetos do projeto e para os administradores do espaço de trabalho, mas somente um Arquiteto pode alterar uma autorização, e somente enquanto o projeto estiver desbloqueado. Um administrador do espaço de trabalho que não seja Arquiteto pode primeiro se adicionar como Arquiteto.
- Selecionar uma linha para autorizar ou desmarcar não recarrega a lista: a posição de rolagem e qualquer ordenação de coluna que você escolheu permanecem onde estão. A janela pode ser redimensionada, e a observação sobre projetos públicos é quebrada por completo.
- Para autorizar uma conexão, você também precisa de acesso de gravação a ela: você é o proprietário, ou ela é compartilhada com você pelo nome ou por meio de um dos seus grupos de segurança. Uma conexão definida como **Todos os membros do espaço de trabalho** não conta.
- Um projeto definido como **Todos os membros do espaço de trabalho** é autorizado como qualquer outro. Todo membro é Arquiteto dele, então qualquer membro com acesso de gravação a uma conexão pode autorizar o projeto para ela. Depois de autorizado, qualquer membro pode lançar nessa conexão a partir dos fluxos de trabalho do projeto, e a janela informa isso acima da grade.
- Uma nova cópia privada para você, feita com dados de tabela ou membros de dimensão, mantém as autorizações da origem que você mesmo poderia conceder e chega em Simulação se a origem estava em modo Real — veja [Autorizações de gravação no ERP na cópia](/pt-br/guides/projects/managing-projects/#autorizações-de-gravação-no-erp-na-cópia). Qualquer outra cópia, ou um projeto criado a partir de um arquivo de projeto, começa sem autorizações. Autorize-o antes que ele lance.

## Acompanhar o status de uma etapa

Enquanto um fluxo de trabalho é executado, cada etapa exibe um ícone de status mostrando em que ponto ela está, ao lado do tempo em que está em execução. Passe o mouse sobre o ícone para ver a mensagem por trás dele.

| Status | O que significa |
|---|---|
| Aguardando | A etapa está na fila e ainda não começou. |
| Em execução | A etapa está trabalhando, e sua duração aumenta conforme ela avança. |
| Concluído | A etapa terminou com sucesso. |
| Aviso | A etapa terminou, mas sinalizou algo que vale a pena ler no [log do fluxo de trabalho](/pt-br/guides/workflows/viewing-workflow-log/). |
| Erro | A etapa falhou. Veja [Gerenciar erros de etapa](/pt-br/guides/workflows/managing-step-errors/). |
| Ignorado | A etapa foi deixada de lado — ela está desativada ou suas condições de execução não foram atendidas. Veja [Ignorar etapas em um fluxo de trabalho](/pt-br/guides/workflows/skip-steps-in-a-workflow/). |
| Continuado | A etapa falhou, mas está configurada para continuar em caso de erro, então o fluxo de trabalho prosseguiu. Veja [Continuar em caso de erro](/pt-br/guides/workflows/continue-on-error/). |
| Parado | A execução foi parada antes que a etapa pudesse terminar. |
| Abandonado | A execução da etapa foi interrompida, então ela nunca terminará. Retome a execução ou execute o fluxo de trabalho novamente. |

Uma visão de fluxo de trabalho aberta é atualizada sozinha conforme uma execução avança, então os status que você está vendo permanecem atuais sem recarregar a página.

### Etapas abandonadas

Uma etapa é marcada como **abandonada** quando o que a estava executando desapareceu no meio da execução — na maioria das vezes porque alguém pressionou **Parar**, ou porque uma manutenção da plataforma interrompeu a execução. A duração da etapa deixa de aumentar e a dica do status explica o que aconteceu.

Uma etapa abandonada não foi concluída e não produziu saída. Ela não é uma etapa lenta, e não é um problema com seus dados ou sua configuração.

Para retomar o trabalho, [**Retome**](#pausar-parar-e-retomar) a execução — a etapa abandonada é executada novamente — ou execute o fluxo de trabalho inteiro de novo. Ambas as opções são seguras.

### Etapas interrompidas

Se o servidor que executa uma etapa for perdido no meio da execução, o PlaidCloud executa a etapa novamente de forma automática quando é seguro repeti-la: uma etapa que substitui sua saída termina com o mesmo resultado de uma única execução limpa, então não há nada para verificar. O log da etapa mostra um aviso no ponto em que a segunda tentativa começa: "Restarted: the server running this step stopped before it finished (e.g. out of memory or a restart); running it again from the start."

Uma etapa que não pode ser repetida com segurança não é executada de novo. Ela falha uma vez com uma mensagem de **interrompida**, porque executá-la uma segunda vez poderia duplicar o que a primeira tentativa já gravou. Etapas que gravam saídas com `{date}` no nome ou no caminho contam como não seguras para repetir, já que uma nova execução poderia cair em outra data. Para se recuperar, verifique no destino da etapa o que a primeira tentativa gravou, limpe-o se necessário e então [execute a etapa novamente](/pt-br/guides/workflows/running-one-step-in-a-workflow/) ou **Retome** a execução.

### Etapas que nunca começam

Enquanto uma etapa espera por um worker, sua mensagem de status diz "Waiting for a worker… N min. No import worker has picked this step up yet." (o tipo de worker corresponde à etapa, como importação ou exportação). A mensagem some quando o trabalho começa.

Se o job de uma etapa nunca puder começar, a etapa falha com o motivo em vez de esperar para sempre:

| Causa | Falha após cerca de |
|---|---|
| Nenhum worker pega o job de uma etapa de importação ou de dimensão | 40 minutos |
| O pod da etapa fica preso em Pending | 20 minutos |
| A imagem da etapa não pode ser baixada | 5 minutos |
| Nenhum pod é criado para a etapa | 20 minutos |
| Nenhum executor pega uma sincronização de conector (Singer) | 30 minutos |

A mensagem de sincronização de conector informa a sincronização. Se um worker iniciou o job e depois desapareceu, a etapa também falha, com uma mensagem dizendo que o worker parou. As mensagens de importação e de dimensão dizem "Use Run from here to retry."

### Execuções que param de responder

Uma execução nunca permanece **Em execução** depois que o trabalho por trás dela deixou de existir. Se o servidor que executa o fluxo de trabalho for perdido, a execução termina como falha. Uma execução pode durar no máximo 12 horas: uma que ainda estiver em execução nesse momento falha com "Run failed: still running at the 12-hour limit. Re-run the workflow."

## Pausar, parar e retomar

Enquanto um fluxo de trabalho está em execução, você pode **Pausar** para que as etapas em andamento terminem e as novas etapas aguardem, ou **Parar**, o que cancela as etapas que estavam na fila e quaisquer jobs de importação ou exportação ainda em execução, junto com a consulta ao warehouse que uma exportação estava lendo. As etapas de importação e de dimensão que ainda estavam na fila são canceladas de forma limpa, para que não atrasem importações e cargas de dimensão posteriores no espaço de trabalho. Parar também interrompe as sincronizações de conector (Singer) do fluxo de trabalho que estavam na fila ou em execução, de modo que uma sincronização não continue rodando depois que o fluxo de trabalho parou.

Uma macro pode estar em execução em vários lugares ao mesmo tempo, chamada por outros fluxos de trabalho ou por uma etapa **Macro: Execução simultânea**. Parar a macro interrompe todas as cópias dela em execução. Parar uma cópia interrompe somente essa cópia e o que ela iniciou, e deixa em execução o fluxo de trabalho que a chamou, assim como acontece quando uma etapa **Macro Concurrent** desiste de uma cópia que parou de responder. Uma macro que está em execução apenas dentro de outros fluxos de trabalho aparece como **Em execução** na lista de fluxos de trabalho, com **Parar** disponível, e abri-la mostra o status, o horário de início e o de término de cada etapa na execução mais recente.

**Retomar** recomeça uma execução pausada, parada ou com falha do ponto em que parou, em vez de começar do zero. Está disponível sempre que a última execução de um fluxo de trabalho terminou em estado pausado, parado ou de erro.

O que "do ponto em que parou" significa depende de como o fluxo de trabalho é executado:

| Execução | Ao retomar |
|---|---|
| Serial | Reinicia na etapa que estava em execução quando a execução terminou e continua a partir dela. Se essa etapa estiver dentro de um grupo, Retomar pega o grupo de nível superior inteiro que a contém: as etapas do grupo que já terminaram com sucesso são deixadas como estão, as outras são executadas, e a execução continua depois do grupo. |
| Paralela | Executa novamente todas as etapas que ainda não haviam terminado com sucesso e deixa as etapas concluídas como estão. |
| Avançada (grafo) | Executa novamente o nó que falhou e tudo o que ainda aguarda por ele, e deixa os nós concluídos como estão. |

As etapas que chamam outro fluxo de trabalho — **Run Model**, **Conditional Run Model** e **Loop Model** — retomam o fluxo de trabalho que chamam em vez de reiniciá-lo, por quantos níveis de aninhamento você tiver. Uma etapa de loop retoma a iteração que foi interrompida e ignora as iterações que já foram concluídas.

Quando você retoma um fluxo de trabalho que foi executado como **filho aninhado** de outro — um que uma etapa **Run Model** em um pai invocou —, o PlaidCloud oferece **Retomar do início da cadeia**. Retomar o filho isoladamente não consegue continuar a orquestração do pai, então essa opção retoma o pai de nível superior — a raiz da cadeia — e continua a cadeia inteira do ponto em que parou. Retomar um fluxo de trabalho de nível superior permanece inalterado. O início da cadeia é resolvido dentro do mesmo projeto: uma cadeia que cruza para outro projeto é retomada a partir do início da parte dentro do projeto.

Retomar sempre continua a execução **original**. Ele executa novamente todas as etapas dessa execução que não terminaram com sucesso — uma etapa que falhou ou foi abandonada é executada de novo, não tratada como concluída — e executar novamente uma etapa individual por conta própria nesse meio-tempo não muda o que Retomar pegará em seguida. Isso também vale para um fluxo de trabalho filho: se você executou novamente uma das etapas dele por conta própria, retomar o pai ainda executa tudo o que restava no filho, não apenas essa etapa.

Uma execução retomada é registrada como uma **nova execução** no histórico de execuções do fluxo de trabalho, contendo apenas as etapas que ela executou novamente. A execução original mantém sua própria entrada no histórico. Quando uma execução chama o mesmo fluxo de trabalho filho mais de uma vez, cada chamada tem sua própria entrada no histórico de execuções do filho. As iterações de uma etapa de loop contam como uma única chamada.

:::note
Uma etapa de loop associa suas iterações concluídas pelos valores de variável delas. Se os dados sobre os quais o loop itera mudaram entre a execução original e a retomada, as iterações que ele não consegue mais associar são executadas novamente em vez de ignoradas.
:::
