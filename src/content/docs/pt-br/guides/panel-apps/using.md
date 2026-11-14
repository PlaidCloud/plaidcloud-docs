---
title: Como usar um aplicativo Panel
description: Acompanhe o status da compilação, abra, recompile, bloqueie, veja os logs e as métricas de uso, edite e remova aplicativos HoloViz Panel publicados na tela Aplicativos do PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Todo aplicativo publicado aparece na tela **Aplicativos** com seu **Tempo de execução**, **Status**, **Slug** e carimbos de data/hora. A coluna mais à esquerda abre o aplicativo; os demais ícones da linha permitem bloqueá-lo contra alterações acidentais, editá-lo, removê-lo e — para aplicativos de servidor — recompilá-lo, ver seus logs e ver as métricas de uso. O ícone de abertura reflete o tempo de execução do aplicativo, para que seja fácil distinguir rapidamente os aplicativos WASM dos de servidor.

## Status da compilação (aplicativos de servidor)

A coluna **Status** de um aplicativo de servidor acompanha sua compilação, e a lista é atualizada sozinha enquanto uma compilação está em andamento:

- **Compilando…** — o PlaidCloud está compilando seu repositório em um contêiner. O aplicativo ainda não tem URL.
- **Pronto** — a compilação foi concluída com sucesso. A URL do aplicativo está ativa e o ícone **Abrir** aparece na linha dele.
- **Falhou** — a compilação não foi concluída. Verifique o ponto de entrada e o branch e, em seguida, edite o aplicativo para publicá-lo novamente.

Os aplicativos WASM não têm etapa de compilação e ficam disponíveis assim que são publicados.

## Como recompilar um aplicativo de servidor

Clique no ícone **Recompilar** na linha de um aplicativo de servidor para recompilá-lo e reimplantá-lo sem alterar suas configurações. O status do aplicativo volta para **Compilando…** enquanto o PlaidCloud compila novamente o mesmo branch e ponto de entrada e, depois, muda de volta para **Pronto** quando a nova compilação estiver ativa.

Use **Recompilar** após alterações de dependências, atualizações da imagem base ou uma falha transitória de compilação. Editar e salvar um aplicativo de servidor também o recompila, mas a recompilação não exige abrir o formulário de edição.

Para um aplicativo [App Runner](/pt-br/guides/workflows/use-converted-alteryx-apps/#manter-o-aplicativo-atualizado) — o formulário de entrada gerado para um aplicativo Alteryx convertido —, **Recompilar** e salvar uma edição primeiro atualizam os arquivos gerados dele para a versão atual do App Runner e depois o compilam. O PlaidCloud também faz isso para todo aplicativo App Runner que não esteja bloqueado quando o próprio PlaidCloud é atualizado; um aplicativo bloqueado precisa de um **Recompilar** depois que você o desbloquear.

## Como bloquear um aplicativo

Clique no ícone de **cadeado** na linha de um aplicativo para protegê-lo contra alterações acidentais. Enquanto um aplicativo está bloqueado:

- **Editar**, **Remover** e **Recompilar** não são executados e informam que o aplicativo está bloqueado.
- Um **push no branch de um aplicativo de servidor não o recompila** — a recompilação automática é ignorada até você desbloquear o aplicativo. Nenhuma compilação é executada para um push ignorado, então nada novo aparece nos logs de Compilação do aplicativo; faça um novo push (ou use **Recompilar**) após o desbloqueio para incorporar a alteração.
- Abrir o aplicativo, ver seus logs e ver suas métricas de uso continuam funcionando — o bloqueio impede apenas alterações, nunca quem o visualiza.

Clique no ícone novamente para desbloquear. O ícone mostra o estado atual do aplicativo: fechado quando bloqueado, aberto quando não.

O bloqueio é uma proteção contra acidentes — uma edição equivocada, uma exclusão não intencional ou um git push que chega a um aplicativo que você está demonstrando —, assim como o bloqueio em fluxos de trabalho e etapas de fluxo de trabalho. Ele **não** é um controle de segurança: qualquer pessoa que pode editar aplicativos Panel também pode desbloqueá-los.

> Duas situações que o bloqueio não cobre: uma **compilação já em andamento** quando você bloqueia ainda é concluída e entra no ar, e os arquivos de um aplicativo **WASM** ficam na conta de documentos dele, portanto substituir esses arquivos altera o aplicativo em execução sem mexer no registro bloqueado.

## Como abrir um aplicativo

Clique no ícone **Abrir** no início da linha de um aplicativo pronto para iniciá-lo em uma nova guia. **Abrir** também é o primeiro item do menu **⋯** da linha. Consulte [O menu de ações da linha](/pt-br/guides/dashboards/using-dashboards/#o-menu-de-ações-da-linha).

- Um aplicativo de servidor é disponibilizado em `https://<your-tenant-host>/serve/<slug>/`.
- O ícone **Abrir** só aparece quando um aplicativo de servidor está **Pronto**.

Um aplicativo de servidor é reduzido a zero quando ocioso para economizar recursos, então a primeira abertura após um período de inatividade precisa iniciá-lo. Enquanto isso acontece, você vê uma **tela de carregamento do PlaidCloud** em vez de uma guia em branco: o nome do seu aplicativo, o progresso dele pelas etapas **Iniciando**, **Preparando** e **Carregando aplicativo**, e o ID do seu espaço de trabalho, no seu tema claro ou escuro. O aplicativo aparece sozinho assim que estiver pronto (geralmente em alguns segundos, até cerca de um minuto em uma inicialização a frio) e, depois, responde normalmente até ficar ocioso novamente.

> Se um aplicativo não conseguir iniciar, a tela de carregamento passa a exibir uma mensagem informando que o aplicativo não foi iniciado e em qual etapa ele parou, com um botão **Tentar novamente**, em vez de ficar carregando indefinidamente. Se isso continuar acontecendo, edite o aplicativo para verificar o ponto de entrada e o branch e publique-o novamente, ou entre em contato com o administrador do PlaidCloud.

### Aparência

Os aplicativos Panel de servidor usam por padrão o design moderno **Fast** do PlaidCloud, mas a configuração **Design** do aplicativo pode voltar ao estilo **Padrão** do Panel quando um CSS existente depender dele. O tema — claro, escuro ou uma alternância claro/escuro que os visualizadores podem acionar — é definido no modelo do seu aplicativo. Consulte [Definir o tema](/pt-br/guides/panel-apps/creating/#defina-o-tema-claro-escuro-ou-alternável) no guia de criação para ver os padrões. Se as tabelas ou o estilo personalizado do seu aplicativo foram feitos para um fundo claro, mantenha-o fixado no tema claro.

## Como ver os logs (aplicativos de servidor)

Clique no ícone **Ver logs** na linha de um aplicativo de servidor para abrir o visualizador de logs dele. (Os aplicativos WASM são executados inteiramente no navegador e não têm logs de servidor, por isso o ícone aparece apenas nas linhas de aplicativos de servidor.)

O visualizador tem duas guias:

- **Tempo de execução** (exibida primeiro) — a saída do próprio aplicativo em execução: tudo o que ele registra em log, tudo o que ele imprime e quaisquer erros não tratados. Essas entradas são mantidas mesmo depois que o aplicativo é reduzido a zero, para que você possa revisar o que uma sessão anterior fez.
- **Compilação** — a saída da compilação do contêiner do aplicativo. Use-a para entender *por que* uma compilação mostra **Falhou** — por exemplo, uma dependência que não foi instalada.

Cada guia oferece os filtros **Informação / Aviso / Erro**, um intervalo de tempo **Logs desde** (da última hora até 30 dias, ou tudo), um botão **Atualizar** e **Atualização automática** para buscar novas entradas periodicamente — prático enquanto você acompanha um aplicativo ativo ou uma compilação em andamento. As entradas mais recentes são listadas primeiro.

> Se não for possível capturar a saída da compilação, a guia Compilação exibe uma breve observação explicando o motivo, em vez de aparecer vazia.

### Como ler uma mensagem de log completa

A tabela de logs corta linhas longas para manter a lista legível. Selecione uma linha de log para abrir um **painel de detalhes** ao lado da tabela, que mostra a mensagem completa da entrada. Essa é a maneira mais fácil de ler algo longo demais para a tabela — uma mensagem de erro longa ou um stack trace completo — sem que seja cortado.

### Como copiar linhas de log

Você pode selecionar várias linhas de log de uma vez e clicar em **Copiar** para colocá-las na área de transferência. Isso é prático para colar logs em uma conversa com um assistente de IA ao depurar seu aplicativo, ou em uma mensagem para sua equipe ou para o suporte do PlaidCloud.

### Quem gerou uma linha de log

Quando seu aplicativo autentica os visualizadores, cada linha de log é marcada com o **usuário** cuja sessão a gerou, para que você saiba qual visualizador encontrou determinado erro ou aviso. A marcação é feita na medida do possível — algumas linhas do framework e da inicialização são executadas antes de qualquer visualizador estar envolvido e podem não mostrar um usuário.

## Métricas de uso (aplicativos de servidor)

Clique no ícone **Usage Metrics** na linha de um aplicativo de servidor — ao lado de **Ver logs** — para ver como o aplicativo está sendo usado. A visão resume:

- **Usuários únicos** — quantas pessoas distintas abriram o aplicativo.
- **Sessões** — quantas vezes ele foi aberto.
- **Duração média e mediana da sessão** — aproximadamente quanto tempo dura uma visita.
- **Último uso** — quando o aplicativo foi aberto mais recentemente.

Abaixo do resumo, você tem um detalhamento **por usuário** e **por dia**, para ver quem está usando o aplicativo e como o uso evolui ao longo do tempo.

> As durações são aproximadas. Os aplicativos de servidor ficam ociosos e são reduzidos quando ninguém os está usando, portanto o término exato de uma sessão nem sempre é observado — leia os valores de duração como uma referência, não como uma medição exata.

## Como editar um aplicativo

Clique no ícone de **lápis** na linha de um aplicativo para editá-lo. O formulário de edição corresponde ao tempo de execução do aplicativo.

Para um aplicativo de **servidor**, você pode alterar o nome, o slug, o branch, o ponto de entrada, a CPU, a memória, o design, o período de inatividade, a opção pública, os domínios de exibição incorporada e o memorando. A **Conexão Git** é fixada quando o aplicativo é criado e é exibida como somente leitura. Salvar recompila o aplicativo — o status dele volta para **Compilando…** até que a nova compilação esteja pronta.

## Como remover um aplicativo

Clique no ícone de **menos** na linha de um aplicativo e confirme; excluir ou cancelar a publicação de um aplicativo sempre pede sua confirmação antes. A remoção de um aplicativo de servidor desfaz sua compilação e implantação; a remoção de um aplicativo WASM cancela a publicação do arquivo estático. A URL do aplicativo para de funcionar imediatamente.

A ferramenta MCP `panel_deployment_manage` não oferece mais o cancelamento da publicação. Em vez disso, remova o aplicativo desta lista.
