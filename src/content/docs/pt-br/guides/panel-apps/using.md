---
title: Usar um aplicativo Panel
description: Acompanhe o status de compilação, abra, recompile, bloqueie, veja logs e métricas de uso, edite e remova aplicativos HoloViz Panel publicados na tela Meus aplicativos Panel do PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Todo aplicativo publicado aparece na tela **Meus aplicativos Panel** com seu **Tempo de execução**, **Status**, **Slug** e carimbos de data e hora. A coluna mais à esquerda abre o aplicativo; os demais ícones da linha permitem bloqueá-lo contra alterações acidentais, editá-lo, removê-lo e, no caso de aplicativos de servidor, recompilá-lo, ver seus logs e ver as métricas de uso. O ícone de abrir reflete o tempo de execução do aplicativo, de modo que aplicativos WASM e de servidor são fáceis de distinguir à primeira vista.

## Status de compilação (aplicativos de servidor)

A coluna **Status** de um aplicativo de servidor acompanha sua compilação, e a lista é atualizada sozinha enquanto uma compilação está em andamento:

- **Compilando…** — o PlaidCloud está compilando seu repositório em um contêiner. O aplicativo ainda não tem URL.
- **Pronto** — a compilação foi concluída com sucesso. A URL do aplicativo está ativa e o ícone **Abrir** aparece na linha dele.
- **Falhou** — a compilação não foi concluída. Verifique o ponto de entrada e o branch e, em seguida, edite o aplicativo para publicá-lo novamente.

Aplicativos WASM não têm etapa de compilação e ficam disponíveis assim que são publicados.

## Recompilar um aplicativo de servidor

Clique no ícone **Recompilar** na linha de um aplicativo de servidor para recompilá-lo e reimplantá-lo sem alterar suas configurações. O status do aplicativo volta para **Compilando…** enquanto o PlaidCloud compila novamente o mesmo branch e o mesmo ponto de entrada e, em seguida, retorna para **Pronto** quando a nova compilação estiver ativa.

Use **Recompilar** após alterações de dependências, atualizações da imagem base ou uma compilação que falhou por um problema transitório. Editar e salvar um aplicativo de servidor também o recompila, mas a recompilação não exige abrir o formulário de edição.

Em um aplicativo [App Runner](/pt-br/guides/workflows/use-converted-alteryx-apps/#manter-o-aplicativo-atualizado) — o formulário de entrada gerado para um aplicativo Alteryx convertido — **Recompilar** e salvar uma edição primeiro atualizam os arquivos gerados dele para a versão atual do App Runner e depois o compilam. O PlaidCloud também faz isso para todo aplicativo App Runner que não esteja bloqueado quando o próprio PlaidCloud é atualizado; um aplicativo bloqueado precisa de **Recompilar** depois que você o desbloquear.

## Bloquear um aplicativo

Clique no ícone de **bloqueio** na linha de um aplicativo para protegê-lo contra alterações acidentais. Enquanto um aplicativo está bloqueado:

- **Editar**, **Remover** e **Recompilar** se recusam a executar e informam que o aplicativo está bloqueado.
- Um **push no branch de um aplicativo de servidor não o recompila** — a recompilação automática é ignorada até você desbloquear o aplicativo. Nenhuma compilação é executada para um push ignorado, portanto nada de novo aparece nos logs de compilação do aplicativo; faça push novamente (ou use **Recompilar**) depois de desbloquear para aplicar a alteração.
- Abrir o aplicativo, ver seus logs e ver suas métricas de uso continuam funcionando — o bloqueio impede apenas alterações, nunca os visualizadores.

Clique no ícone novamente para desbloquear. O ícone mostra o estado atual do aplicativo: fechado quando bloqueado, aberto quando não.

O bloqueio é uma proteção contra acidentes — uma edição equivocada, uma exclusão não intencional ou um push de git que chega a um aplicativo que você está demonstrando — assim como o bloqueio em fluxos de trabalho e etapas de fluxo de trabalho. Ele **não** é um controle de segurança: qualquer pessoa que possa editar aplicativos Panel também pode desbloqueá-los.

> Duas coisas que o bloqueio não cobre: uma **compilação já em andamento** quando você bloqueia ainda termina e entra no ar, e os arquivos de um aplicativo **WASM** ficam na conta de documentos dele, portanto substituir esses arquivos altera o aplicativo em execução sem tocar no registro bloqueado.

## Abrir um aplicativo

Clique no ícone **Abrir** no início da linha de um aplicativo pronto para iniciá-lo em uma nova guia.

- Um aplicativo de servidor é servido em `https://<your-tenant-host>/serve/<slug>/`.
- O ícone **Abrir** só aparece quando um aplicativo de servidor está **Pronto**.

Um aplicativo de servidor reduz a zero quando está ocioso para economizar recursos, portanto a primeira abertura após um período de inatividade precisa iniciá-lo novamente. Enquanto isso acontece, você vê uma **tela de carregamento do PlaidCloud** — o nome do seu aplicativo, um indicador de progresso e os detalhes do seu espaço de trabalho — em vez de uma guia em branco. O aplicativo aparece sozinho assim que fica pronto (em geral em poucos segundos, até cerca de um minuto em uma partida a frio) e depois responde normalmente até ficar ocioso novamente.

> Se um aplicativo não conseguir iniciar, a tela de carregamento se transforma em uma mensagem **"Este aplicativo não foi iniciado"** com um botão **Tentar novamente**, em vez de girar para sempre. Se isso continuar acontecendo, edite o aplicativo para verificar o ponto de entrada e o branch e publique-o novamente, ou entre em contato com o administrador do PlaidCloud.

### Aparência

Os aplicativos Panel de servidor usam por padrão o design moderno **FAST** do PlaidCloud, mas a configuração **Design** do aplicativo pode alterná-lo de volta para o estilo **Padrão** do Panel quando um CSS existente depende dele. O tema — claro, escuro ou uma alternância entre claro e escuro que os visualizadores podem acionar — é algo que você define no modelo do seu aplicativo. Consulte [Definir o tema](/pt-br/guides/panel-apps/creating/#defina-o-tema-claro-escuro-ou-alternável) no guia de criação para ver os padrões. Se as tabelas ou o estilo personalizado do seu aplicativo foram criados para um fundo claro, mantenha-o fixado em claro.

## Ver logs (aplicativos de servidor)

Clique no ícone **Ver logs** na linha de um aplicativo de servidor para abrir o visualizador de logs. (Aplicativos WASM são executados inteiramente no navegador e não têm logs de servidor, por isso o ícone aparece apenas nas linhas de aplicativos de servidor.)

O visualizador tem duas guias:

- **Tempo de execução** (exibida primeiro) — a saída do próprio aplicativo em execução: tudo o que ele registra, tudo o que imprime e quaisquer erros não tratados. Eles são mantidos mesmo depois que o aplicativo reduz a zero, para que você possa revisar o que uma sessão anterior fez.
- **Compilação** — a saída da compilação do contêiner do aplicativo. Use-a para ver *por que* uma compilação mostra **Falhou** — por exemplo, uma dependência que não foi instalada.

Cada guia oferece filtros de **Informação / Aviso / Erro**, um intervalo de tempo de **Logs desde** (da última hora até 30 dias, ou todos), um botão **Atualizar** e **Atualização automática** para consultar novas entradas — útil enquanto você acompanha um aplicativo ao vivo ou uma compilação em andamento. As entradas mais recentes são listadas primeiro.

> Se a saída da compilação não puder ser capturada, a guia Compilação mostra uma breve observação explicando o motivo, em vez de aparecer vazia.

### Ler uma mensagem de log completa

A tabela de logs corta linhas longas para manter a lista legível. Selecione uma linha de log para abrir um **painel de detalhes** ao lado da tabela que mostra a mensagem completa da entrada. Essa é a maneira mais fácil de ler algo longo demais para a tabela — uma mensagem de erro extensa ou um rastreamento de pilha completo — sem que seja cortado.

### Copiar linhas de log

Você pode selecionar várias linhas de log de uma só vez e clicar em **Copiar** para colocá-las na área de transferência. Isso é útil para colar logs em uma conversa com um assistente de IA ao depurar seu aplicativo, ou em uma mensagem para sua equipe ou para o suporte do PlaidCloud.

### Quem gerou uma linha de log

Quando seu aplicativo autentica os visualizadores, cada linha de log é marcada com o **usuário** cuja sessão a produziu, para que você saiba qual visualizador encontrou determinado erro ou aviso. A marcação é feita em regime de melhor esforço — algumas linhas do framework e da inicialização são executadas antes de qualquer visualizador estar envolvido e podem não mostrar um usuário.

## Métricas de uso (aplicativos de servidor)

Clique no ícone **Usage Metrics** na linha de um aplicativo de servidor — ao lado de **Ver logs** — para ver como o aplicativo está sendo usado. A visualização resume:

- **Usuários únicos** — quantas pessoas distintas abriram o aplicativo.
- **Sessões** — quantas vezes ele foi aberto.
- **Duração média e mediana das sessões** — aproximadamente quanto dura uma visita.
- **Último uso** — quando o aplicativo foi aberto pela última vez.

Abaixo do resumo, você vê um detalhamento **por usuário** e **por dia**, para saber quem está usando o aplicativo e como o uso evolui ao longo do tempo.

> As durações são aproximadas. Aplicativos de servidor ficam ociosos e reduzem a escala quando ninguém os está usando, portanto o fim exato de uma sessão nem sempre é observado — leia os números de duração como uma referência, não como uma medição exata.

## Editar um aplicativo

Clique no ícone de **lápis** na linha de um aplicativo para editá-lo. O formulário de edição corresponde ao tempo de execução do aplicativo.

Em um aplicativo de **servidor**, você pode alterar o nome, o slug, o branch, o ponto de entrada, a CPU, a memória, o design, a janela de inatividade, o indicador de público, os domínios de exibição incorporada e o memorando. A **Conexão Git** é fixada quando o aplicativo é criado e é exibida somente para leitura. Salvar recompila o aplicativo — o status dele volta para **Compilando…** até a nova compilação ficar pronta.

## Remover um aplicativo

Clique no ícone de **menos** na linha de um aplicativo e confirme; excluir ou cancelar a publicação de um aplicativo sempre pede confirmação primeiro. Remover um aplicativo de servidor desfaz sua compilação e sua implantação; remover um aplicativo WASM cancela a publicação do arquivo estático. A URL do aplicativo deixa de funcionar imediatamente.

A ferramenta MCP `panel_deployment_manage` não oferece mais o cancelamento de publicação. Remova um aplicativo desta lista.
