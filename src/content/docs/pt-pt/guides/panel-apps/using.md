---
title: Utilizar uma aplicação Panel
description: Acompanhe o estado da compilação, abra, recompile, bloqueie, consulte os registos e os indicadores de utilização, edite e remova aplicações HoloViz Panel publicadas a partir do ecrã As minhas aplicações Panel do PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Cada aplicação publicada aparece no ecrã **As minhas aplicações Panel** com o respetivo **Tempo de execução**, **Estado**, **Slug** e carimbos de data/hora. A coluna mais à esquerda abre a aplicação; os restantes ícones da linha permitem bloqueá-la contra alterações acidentais, editá-la, removê-la e — no caso das aplicações de servidor — recompilá-la, consultar os respetivos registos e consultar os indicadores de utilização. O ícone de abertura reflete o tempo de execução da aplicação, pelo que as aplicações WASM e de servidor são fáceis de distinguir num relance.

## Estado da compilação (aplicações de servidor)

A coluna **Estado** de uma aplicação de servidor acompanha a respetiva compilação, e a lista atualiza-se automaticamente enquanto uma compilação está em curso:

- **A compilar…** — o PlaidCloud está a compilar o repositório num contentor. A aplicação ainda não tem URL.
- **Pronta** — a compilação foi bem-sucedida. O URL da aplicação está ativo e o ícone **Abrir** aparece na respetiva linha.
- **Falhou** — a compilação não foi concluída. Verifique o ponto de entrada e o ramo e, em seguida, edite a aplicação para a voltar a publicar.

As aplicações WASM não têm fase de compilação e ficam disponíveis assim que são publicadas.

## Recompilar uma aplicação de servidor

Clique no ícone **Recompilar** na linha de uma aplicação de servidor para a recompilar e voltar a implementar sem alterar as respetivas definições. O estado da aplicação volta a **A compilar…** enquanto o PlaidCloud compila novamente o mesmo ramo e ponto de entrada, e passa de novo a **Pronta** quando a nova compilação estiver ativa.

Utilize **Recompilar** após alterações de dependências, atualizações da imagem base ou uma falha de compilação transitória. Editar e guardar uma aplicação de servidor também a recompila, mas uma recompilação não exige abrir o formulário de edição.

No caso de uma aplicação [App Runner](/pt-pt/guides/workflows/use-converted-alteryx-apps/#manter-a-aplicação-atualizada) — o formulário de entrada gerado para uma aplicação Alteryx convertida —, **Recompilar** e guardar uma edição começam por atualizar os respetivos ficheiros gerados para a versão atual do App Runner e, em seguida, compilam-na. O PlaidCloud faz também isto para todas as aplicações App Runner que não estejam bloqueadas quando o próprio PlaidCloud é atualizado; uma aplicação bloqueada precisa de **Recompilar** depois de a desbloquear.

## Bloquear uma aplicação

Clique no ícone de **cadeado** na linha de uma aplicação para a proteger contra alterações acidentais. Enquanto uma aplicação estiver bloqueada:

- **Editar**, **Remover** e **Recompilar** recusam-se a ser executados e indicam que a aplicação está bloqueada.
- Um **push para o ramo de uma aplicação de servidor não a recompila** — a recompilação automática é ignorada até desbloquear a aplicação. Não é executada nenhuma compilação para um push ignorado, pelo que nada de novo aparece nos registos de Compilação da aplicação; faça push novamente (ou utilize **Recompilar**) depois de desbloquear para incorporar a alteração.
- Abrir a aplicação, consultar os respetivos registos e consultar os indicadores de utilização continuam a funcionar — o bloqueio impede apenas alterações, nunca o acesso de quem a visualiza.

Clique novamente no ícone para desbloquear. O ícone mostra o estado atual da aplicação: fechado quando está bloqueada, aberto quando não está.

O bloqueio é uma proteção contra acidentes — uma edição por engano, uma eliminação não intencional ou um git push que chega a uma aplicação que está a demonstrar —, tal como o bloqueio de fluxos de trabalho e de passos de fluxos de trabalho. **Não** é um controlo de segurança: qualquer pessoa que possa editar aplicações Panel também as pode desbloquear.

> Há duas situações que o bloqueio não abrange: uma **compilação já em curso** no momento do bloqueio termina e fica ativa na mesma, e os ficheiros de uma aplicação **WASM** residem na respetiva conta de documentos, pelo que substituir esses ficheiros altera a aplicação em execução sem tocar no registo bloqueado.

## Abrir uma aplicação

Clique no ícone **Abrir** no início da linha de uma aplicação pronta para a iniciar num novo separador. **Abrir** é também o primeiro item do menu **⋯** da linha. Consulte [O menu de ações da linha](/pt-pt/guides/dashboards/using-dashboards/#o-menu-de-ações-da-linha).

- Uma aplicação de servidor é disponibilizada em `https://<your-tenant-host>/serve/<slug>/`.
- O ícone **Abrir** só aparece quando uma aplicação de servidor está **Pronta**.

Uma aplicação de servidor é reduzida a zero quando está inativa para poupar recursos, pelo que a primeira abertura após um período de inatividade tem de a iniciar. Enquanto isso acontece, é apresentado um **ecrã de carregamento do PlaidCloud** em vez de um separador em branco: o nome da aplicação, o respetivo progresso pelas fases **A iniciar**, **A preparar** e **A carregar a aplicação**, e o ID da área de trabalho, no tema claro ou escuro. A aplicação aparece automaticamente assim que estiver pronta (normalmente em poucos segundos, até cerca de um minuto num arranque a frio) e, a partir daí, responde normalmente até voltar a ficar inativa.

> Se uma aplicação não conseguir iniciar, o ecrã de carregamento passa a apresentar uma mensagem a indicar que a aplicação não iniciou e em que passo parou, com um botão **Tentar novamente**, em vez de ficar a carregar indefinidamente. Se isso continuar a acontecer, edite a aplicação para verificar o ponto de entrada e o ramo e volte a publicá-la, ou contacte o administrador do PlaidCloud.

### Aspeto

As aplicações Panel de servidor utilizam por predefinição o design moderno **Fast** do PlaidCloud, mas a definição **Design** da aplicação pode repor o estilo **Predefinição** do Panel quando o CSS existente depende dele. O tema — claro, escuro ou um seletor claro/escuro que os visitantes podem alternar — é definido no modelo da aplicação. Consulte [Definir o tema](/pt-pt/guides/panel-apps/creating/#definir-o-tema-claro-escuro-ou-um-comutador) no guia de criação para conhecer os padrões. Se as tabelas ou o estilo personalizado da aplicação forem concebidos para um fundo claro, mantenha-a fixa no tema claro.

## Consultar registos (aplicações de servidor)

Clique no ícone **Ver registos** na linha de uma aplicação de servidor para abrir o respetivo visualizador de registos. (As aplicações WASM são executadas inteiramente no browser e não têm registos de servidor, pelo que o ícone só aparece nas linhas de aplicações de servidor.)

O visualizador tem dois separadores:

- **Tempo de execução** (apresentado primeiro) — a saída da própria aplicação em execução: tudo o que regista, tudo o que imprime e quaisquer erros não capturados. Estes registos são mantidos mesmo depois de a aplicação ser reduzida a zero, para que possa rever o que uma sessão anterior fez.
- **Compilação** — a saída da compilação do contentor da aplicação. Utilize-o para perceber *porque* uma compilação apresenta **Falhou** — por exemplo, uma dependência que não foi possível instalar.

Cada separador disponibiliza os filtros **Informação / Aviso / Erro**, um intervalo de tempo **Registos desde** (desde a última hora até 30 dias, ou todos), um botão **Atualizar** e **Atualização automática** para consultar periodicamente novas entradas — útil enquanto acompanha uma aplicação ativa ou uma compilação em curso. As entradas mais recentes são apresentadas primeiro.

> Se não tiver sido possível capturar a saída da compilação, o separador Compilação apresenta uma breve nota a explicar o motivo, em vez de aparecer vazio.

### Ler uma mensagem de registo completa

A tabela de registos encurta as linhas longas para manter a lista legível. Selecione uma linha de registo para abrir um **painel de detalhes** junto à tabela que mostra a mensagem completa da entrada. É a forma mais fácil de ler algo demasiado longo para a tabela — uma mensagem de erro longa ou um rastreio de pilha completo — sem que fique cortado.

### Copiar linhas de registo

Pode selecionar várias linhas de registo de uma só vez e clicar em **Copiar** para as colocar na área de transferência. É útil para colar registos numa conversa com um assistente de IA quando está a depurar a aplicação, ou numa mensagem para a equipa ou para o suporte do PlaidCloud.

### Quem originou uma linha de registo

Quando a aplicação autentica os visitantes, cada linha de registo é etiquetada com o **utilizador** cuja sessão a produziu, para que possa saber que visitante encontrou um determinado erro ou aviso. A etiquetagem é feita na medida do possível — algumas linhas da framework e de arranque são executadas antes de qualquer visitante estar envolvido e podem não mostrar um utilizador.

## Usage Metrics (aplicações de servidor)

Clique no ícone **Usage Metrics** na linha de uma aplicação de servidor — junto a **Ver registos** — para ver como a aplicação está a ser utilizada. A vista resume:

- **Utilizadores únicos** — quantas pessoas distintas abriram a aplicação.
- **Sessões** — quantas vezes foi aberta.
- **Duração média e mediana da sessão** — aproximadamente quanto tempo dura uma visita.
- **Última utilização** — quando a aplicação foi aberta pela última vez.

Abaixo do resumo, é apresentada uma discriminação **por utilizador** e **por dia**, para que possa ver quem está a utilizar a aplicação e como a utilização evolui ao longo do tempo.

> As durações são aproximadas. As aplicações de servidor ficam inativas e são reduzidas quando ninguém as está a utilizar, pelo que o fim exato de uma sessão nem sempre é observado — interprete os valores de duração como uma orientação e não como uma medição exata.

## Editar uma aplicação

Clique no ícone de **lápis** na linha de uma aplicação para a editar. O formulário de edição corresponde ao tempo de execução da aplicação.

No caso de uma aplicação de **servidor**, pode alterar o nome, o slug, o ramo, o ponto de entrada, a CPU, a memória, o design, o período de inatividade, a opção pública, os domínios de publicação incorporada e o memorando. A **Ligação Git** fica fixa depois de a aplicação ser criada e é apresentada apenas para leitura. Guardar recompila a aplicação — o respetivo estado volta a **A compilar…** até a nova compilação estar pronta.

## Remover uma aplicação

Clique no ícone de **menos** na linha de uma aplicação e confirme; eliminar ou anular a publicação de uma aplicação pede sempre confirmação primeiro. Remover uma aplicação de servidor desmantela a respetiva compilação e implementação; remover uma aplicação WASM anula a publicação do ficheiro estático. O URL da aplicação deixa de funcionar imediatamente.

A ferramenta MCP `panel_deployment_manage` já não oferece a anulação da publicação. Remova antes a aplicação desta lista.
