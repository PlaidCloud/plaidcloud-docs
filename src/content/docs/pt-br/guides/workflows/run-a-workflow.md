---
title: Executar um fluxo de trabalho
description: Execute um fluxo de trabalho do PlaidCloud manualmente ou sob demanda, acompanhe o status de cada etapa e pause, pare ou retome uma execução de onde ela parou.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Você pode disparar a execução completa de um fluxo de trabalho clicando no ícone de execução na hierarquia de **Fluxos de trabalho** ou selecionando **Run All** no menu **Ações** de um fluxo de trabalho específico.



Você também pode clicar no botão **Toggle Start/Stop** na parte superior da tabela de fluxos de trabalho. Esse botão alternado interrompe um fluxo de trabalho em execução ou inicia um fluxo de trabalho parado.

Se você clicar em **Executar** em um fluxo de trabalho que já está em execução, o PlaidCloud avisa isso em vez de iniciar uma segunda execução.

## Escolher um modo de lançamento

Toda execução tem um modo de lançamento no ERP. Para escolher um no PlaidCloud, use **Executar com modo de lançamento** no menu de contexto (clique com o botão direito) de um fluxo de trabalho ou o botão de modo de execução na tela do fluxo de trabalho; um simples **Iniciar fluxo de trabalho** ou **Executar fluxo de trabalho** solicita o modo Ao vivo, ainda sujeito ao limite do projeto descrito abaixo. Você também pode escolher o modo ao iniciar uma execução pela API de execução ou pelo assistente.

| Modo | O que acontece |
|---|---|
| Ao vivo | As etapas de lançamento fazem o lançamento exatamente como sempre fizeram. Este é o modo padrão. |
| Simular | Cada etapa de lançamento no ERP monta e valida exatamente o que lançaria, depois não confirma nada e nunca entra em contato com o ERP. Os lançamentos que seriam feitos são registrados no [Histórico de lançamentos no ERP](/pt-br/guides/connections/erp-post-history/), marcados como simulados, para que você possa revisá-los antes de executar ao vivo. |
| Desligado | As etapas de lançamento são ignoradas por completo. |

Um projeto também tem seu próprio limite de modo de lançamento, definido pela API do projeto ou pelo assistente por qualquer membro com acesso de gravação a um projeto desbloqueado. O limite só torna uma execução mais segura, nunca mais permissiva: o modo efetivo de uma execução é o mais restritivo entre o modo que você escolheu e o limite do projeto, de modo que um projeto limitado a Simular continua simulado mesmo que você inicie a execução como Ao vivo.

Um [evento agendado](/pt-br/administration/scheduled-events/event-scheduler/#modo-de-lançamento-no-erp) mantém seu próprio modo de lançamento, então um agendamento definido como Simular é executado de forma simulada toda vez que dispara.

O modo se propaga por tudo o que a execução toca. Um subfluxo de trabalho, uma macro e uma etapa **Run Model**, **Conditional Run Model** ou **Loop Model** herdam o modo da execução pai, assim como uma execução que você [retoma](#pausar-parar-e-retomar) após uma parada — uma execução simulada não consegue lançar de verdade em nenhum ponto dentro dela mesma.

:::caution
As etapas de lançamento no SAP, de anexo no SAP e de RFC genérica do SAP não fazem simulação. Em Simular ou Desligado, elas são ignoradas por completo, porque os próprios indicadores de teste do SAP ainda abrem uma conexão real com o SAP — ignorar a etapa é a única forma de uma execução simulada nunca chegar ao SAP.
:::

:::note
Uma etapa individual de lançamento no ERP também tem sua própria configuração Validate Only (chamada de Preview ou Test Only Mode em algumas etapas), independente do modo de lançamento da execução descrito acima. O editor de etapas sempre a salva de forma explícita. Uma configuração de etapa gravada de outra forma — pela API REST, pelo MCP ou por uma importação de pacote de fluxo de trabalho — que omita totalmente essa configuração agora também assume por padrão uma pré-visualização em vez de um lançamento real.
:::

## Autorizar o projeto a lançar

Uma execução de fluxo de trabalho lança em um ERP como o projeto, não como a pessoa que a iniciou. Antes que uma execução possa lançar, o projeto precisa de uma autorização para cada conexão e ambiente de ERP que suas etapas de lançamento usam. Sem ela, a etapa falha com "This project isn't authorized to post to connection …", informando a conexão e o ambiente. As etapas **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** e **Call SAP RFC** não precisam de autorização.

Para autorizar um projeto, abra a página inicial dele e selecione **Autorizações de gravação no ERP** em **Lançamento no ERP**. Cada linha é uma conexão em um ambiente. Marque **Autorizado** para permitir que o projeto lance ali, ou desmarque para impedir. **Autorizado por** e **Autorizado em** mostram quem autorizou por último e quando.

- O botão é exibido para os Arquitetos do projeto e para os administradores do espaço de trabalho, mas somente um Arquiteto pode alterar uma autorização, e somente enquanto o projeto estiver desbloqueado. Um administrador do espaço de trabalho que não é Arquiteto pode se adicionar como Arquiteto antes.
- Selecionar uma linha para autorizar ou limpar a autorização não recarrega a lista: a posição de rolagem e qualquer ordenação de coluna que você escolheu permanecem como estão. A janela pode ser redimensionada, e a observação sobre projetos públicos é quebrada em linhas para aparecer por inteiro.
- Para autorizar uma conexão, você também precisa de acesso de gravação a ela: você é o proprietário, ou ela é compartilhada com você pelo nome ou por meio de um dos seus grupos de segurança. Uma conexão definida como **Todos os membros do espaço de trabalho** não conta.
- Um projeto definido como **Todos os membros do espaço de trabalho** é autorizado como qualquer outro. Todo membro é Arquiteto dele, então qualquer membro com acesso de gravação a uma conexão pode autorizar o projeto para ela. Depois de autorizado, qualquer membro pode lançar nessa conexão a partir dos fluxos de trabalho do projeto, e a janela informa isso acima da grade.
- Um projeto copiado, ou criado a partir de um arquivo de projeto, começa sem autorizações. Autorize a cópia antes que ela lance.

## Acompanhar o status de uma etapa

Enquanto um fluxo de trabalho é executado, cada etapa tem um ícone de status que mostra em que ponto ela está, junto com há quanto tempo está em execução. Passe o mouse sobre o ícone para ver a mensagem por trás dele.

| Status | O que significa |
|---|---|
| Aguardando | A etapa está na fila e ainda não começou. |
| Em execução | A etapa está trabalhando, e a duração dela aumenta conforme avança. |
| Concluída | A etapa terminou com sucesso. |
| Aviso | A etapa terminou, mas sinalizou algo que vale a pena ler no [log do fluxo de trabalho](/pt-br/guides/workflows/viewing-workflow-log/). |
| Erro | A etapa falhou. Consulte [Gerenciar erros de etapa](/pt-br/guides/workflows/managing-step-errors/). |
| Ignorada | A etapa foi pulada — está desativada ou suas condições de execução não foram atendidas. Consulte [Ignorar etapas em um fluxo de trabalho](/pt-br/guides/workflows/skip-steps-in-a-workflow/). |
| Continuada | A etapa falhou, mas está configurada para continuar em caso de erro, então o fluxo de trabalho prosseguiu. Consulte [Continuar em caso de erro](/pt-br/guides/workflows/continue-on-error/). |
| Parada | A execução foi parada antes que a etapa pudesse terminar. |
| Abandonada | A execução da etapa foi interrompida, então ela nunca terminará. Retome a execução ou execute o fluxo de trabalho novamente. |

Uma visão de fluxo de trabalho aberta é atualizada sozinha à medida que uma execução avança, então os status que você está vendo permanecem atuais sem recarregar a página.

### Etapas abandonadas

Uma etapa é marcada como **abandonada** quando o que a estava executando desapareceu no meio da execução — na maioria das vezes porque alguém pressionou **Parar** ou porque uma manutenção da plataforma interrompeu a execução. A duração da etapa deixa de aumentar e a dica do status explica o que aconteceu.

Uma etapa abandonada não foi concluída e não produziu saída. Ela não é uma etapa lenta, e não é um problema com seus dados ou com sua configuração.

Para retomar o trabalho, [**Retome**](#pausar-parar-e-retomar) a execução — a etapa abandonada é executada novamente — ou execute o fluxo de trabalho inteiro de novo. As duas opções são seguras.

### Etapas interrompidas

Se o servidor que executa uma etapa for perdido no meio da execução, o PlaidCloud executa a etapa novamente de forma automática quando é seguro repeti-la: uma etapa que substitui sua saída termina com o mesmo resultado de uma única execução limpa, então você não precisa verificar nada.

Uma etapa que não pode ser repetida com segurança não é executada novamente. Ela falha uma vez com uma mensagem de **interrompida**, porque executá-la uma segunda vez poderia duplicar o que a primeira tentativa já gravou. Etapas que gravam saídas com `{date}` no nome ou no caminho contam como não seguras para repetir, já que uma nova execução poderia cair em uma data diferente. Para se recuperar, verifique no destino da etapa o que a primeira tentativa gravou, limpe se necessário e então [execute a etapa novamente](/pt-br/guides/workflows/running-one-step-in-a-workflow/) ou **Retome** a execução.

### Etapas que nunca começam

Se nenhum worker pegar o trabalho de uma etapa de importação ou de dimensão em cerca de 40 minutos, a etapa falha em vez de mostrar **Em execução** até o tempo limite de 24 horas. Se um worker iniciou o trabalho e depois desapareceu, a etapa também falha, com uma mensagem informando que o worker parou. Ambas as mensagens dizem "Use Run from here to retry."

## Pausar, parar e retomar

Enquanto um fluxo de trabalho está em execução, você pode **Pausar** para que as etapas em andamento terminem e as novas etapas aguardem, ou **Parar**, o que cancela as etapas que estavam na fila e quaisquer trabalhos de importação ou exportação que ainda estejam em execução. As etapas de importação e de dimensão que ainda estavam na fila são canceladas de forma limpa, para que não atrasem importações e cargas de dimensão posteriores no espaço de trabalho.

**Retomar** continua uma execução pausada, parada ou com falha de onde ela parou, em vez de recomeçar. Está disponível sempre que a última execução de um fluxo de trabalho terminou em estado pausado, parado ou de erro.

O que "de onde parou" significa depende de como o fluxo de trabalho é executado:

| Execução | Ao retomar |
|---|---|
| Serial | Reinicia na etapa que estava em execução quando a execução terminou e continua a partir dali. Se essa etapa estiver dentro de um grupo, Retomar continua todo o grupo de nível superior que a contém: as etapas do grupo que já terminaram com sucesso são deixadas como estão, as demais são executadas e a execução continua após o grupo. |
| Paralela | Executa novamente todas as etapas que ainda não haviam terminado com sucesso e deixa as etapas concluídas como estão. |
| Avançada (grafo) | Executa novamente o nó que falhou e tudo o que ainda aguarda por ele, e deixa os nós concluídos como estão. |

As etapas que chamam outro fluxo de trabalho — **Run Model**, **Conditional Run Model** e **Loop Model** — retomam o fluxo de trabalho que chamam em vez de reiniciá-lo, por quantos níveis de aninhamento você tiver. Uma etapa de loop retoma a iteração que foi interrompida e pula as iterações que já foram concluídas.

Quando você retoma um fluxo de trabalho que foi executado como **filho aninhado** de outro — um invocado por uma etapa **Run Model** em um pai — o PlaidCloud oferece **Retomar do início da cadeia**. Retomar o filho isoladamente não consegue continuar a orquestração do pai, então essa opção retoma o pai de nível superior — a raiz da cadeia — e continua toda a cadeia de onde ela parou. Retomar um fluxo de trabalho de nível superior continua como antes. O início da cadeia é resolvido dentro do mesmo projeto: uma cadeia que passa para outro projeto é retomada a partir do início da parte que está dentro do projeto.

Retomar sempre continua a execução **original**. Ela executa novamente todas as etapas dessa execução que não terminaram com sucesso — uma etapa que falhou ou foi abandonada é executada de novo, não tratada como concluída — e executar novamente uma etapa individual por conta própria nesse meio-tempo não muda o que Retomar vai continuar em seguida.

Uma execução retomada é registrada como uma **nova execução** no histórico de execuções do fluxo de trabalho, contendo apenas as etapas que ela executou novamente. A execução original mantém sua própria entrada no histórico.

:::note
Uma etapa de loop associa suas iterações concluídas pelos valores das variáveis delas. Se os dados sobre os quais o loop itera mudaram entre a execução original e a retomada, as iterações que ele não consegue mais associar são executadas novamente em vez de ignoradas.
:::
