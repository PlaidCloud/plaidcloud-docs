---
title: Utilizar uma aplicação Panel
description: Acompanhe o estado de compilação, abra, recompile, bloqueie, veja os registos e as métricas de utilização, edite e remova aplicações HoloViz Panel publicadas a partir do ecrã As minhas aplicações Panel no PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/using.md
---

Todas as aplicações publicadas aparecem no ecrã **As minhas aplicações Panel** com o respetivo **Tempo de execução**, **Estado**, **Slug** e datas e horas. A coluna mais à esquerda abre a aplicação; os restantes ícones da linha permitem bloqueá-la contra alterações acidentais, editá-la, removê-la e, no caso das aplicações de servidor, recompilá-la, ver os respetivos registos e consultar as métricas de utilização. O ícone de abertura reflete o tempo de execução da aplicação, pelo que é fácil distinguir à primeira vista as aplicações WASM das de servidor.

## Estado de compilação (aplicações de servidor)

A coluna **Estado** de uma aplicação de servidor acompanha a respetiva compilação, e a lista é atualizada automaticamente enquanto uma compilação está em curso:

- **A compilar…** — o PlaidCloud está a compilar o seu repositório num contentor. A aplicação ainda não tem URL.
- **Pronta** — a compilação foi concluída com êxito. O URL da aplicação está ativo e o ícone **Abrir** aparece na respetiva linha.
- **Falhou** — a compilação não foi concluída. Verifique o ponto de entrada e o ramo e, em seguida, edite a aplicação para a publicar novamente.

As aplicações WASM não têm passo de compilação e ficam disponíveis assim que são publicadas.

## Recompilar uma aplicação de servidor

Clique no ícone **Recompilar** na linha de uma aplicação de servidor para a recompilar e voltar a implementar sem alterar as respetivas definições. O estado da aplicação regressa a **A compilar…** enquanto o PlaidCloud compila novamente o mesmo ramo e ponto de entrada e, quando a nova compilação estiver ativa, volta a **Pronta**.

Utilize **Recompilar** após alterações de dependências, atualizações da imagem de base ou uma compilação que tenha falhado por motivos transitórios. Editar e guardar uma aplicação de servidor também a recompila, mas a recompilação não exige abrir o formulário de edição.

No caso de uma aplicação [App Runner](/pt-pt/guides/workflows/use-converted-alteryx-apps/#manter-a-aplicação-atualizada) — o formulário de entrada gerado para uma aplicação Alteryx convertida —, **Recompilar** e guardar uma edição atualizam primeiro os ficheiros gerados para a versão atual do App Runner e só depois a compilam. O PlaidCloud faz o mesmo para todas as aplicações App Runner que não estejam bloqueadas quando o próprio PlaidCloud é atualizado; uma aplicação bloqueada precisa de ser recompilada com **Recompilar** depois de a desbloquear.

## Bloquear uma aplicação

Clique no ícone de **cadeado** na linha de uma aplicação para a proteger contra alterações acidentais. Enquanto uma aplicação estiver bloqueada:

- **Editar**, **Remover** e **Recompilar** recusam-se a executar e informam que a aplicação está bloqueada.
- Um **push para o ramo de uma aplicação de servidor não a recompila** — a recompilação automática é ignorada até desbloquear a aplicação. Não é executada nenhuma compilação para um push ignorado, pelo que não aparece nada de novo nos registos de compilação da aplicação; faça novamente push (ou utilize **Recompilar**) depois de desbloquear para aplicar a alteração.
- Abrir a aplicação, ver os respetivos registos e consultar as métricas de utilização continuam a funcionar — o bloqueio impede apenas alterações, nunca os visualizadores.

Clique novamente no ícone para desbloquear. O ícone mostra o estado atual da aplicação: fechado quando bloqueada, aberto quando não.

O bloqueio é uma proteção contra acidentes — uma edição por engano, uma eliminação não intencional ou um push git que chega a uma aplicação que está a demonstrar —, tal como o bloqueio dos fluxos de trabalho e dos passos de fluxo de trabalho. **Não** é um controlo de segurança: qualquer pessoa que possa editar aplicações Panel pode também desbloqueá-las.

> Duas situações que o bloqueio não abrange: uma **compilação já em curso** quando bloqueia a aplicação termina na mesma e fica ativa, e os ficheiros de uma aplicação **WASM** encontram-se na respetiva conta de documentos, pelo que substituir esses ficheiros altera a aplicação em execução sem tocar no registo bloqueado.

## Abrir uma aplicação

Clique no ícone **Abrir** no início da linha de uma aplicação pronta para a iniciar num novo separador.

- Uma aplicação de servidor é disponibilizada em `https://<your-tenant-host>/serve/<slug>/`.
- O ícone **Abrir** só aparece quando uma aplicação de servidor está **Pronta**.

Uma aplicação de servidor reduz para zero quando está inativa, para poupar recursos, pelo que a primeira abertura após um período de inatividade tem de a arrancar. Enquanto isso acontece, vê um **ecrã de carregamento do PlaidCloud** — com o nome da aplicação, um indicador de progresso e os dados da sua área de trabalho — em vez de um separador em branco. A aplicação aparece automaticamente assim que estiver pronta (normalmente em alguns segundos, até cerca de um minuto num arranque a frio) e depois responde normalmente até voltar a ficar inativa.

> Se uma aplicação não conseguir arrancar, o ecrã de carregamento transforma-se numa mensagem **"This app didn't start"** com um botão **Tentar novamente**, em vez de ficar a rodar indefinidamente. Se a situação persistir, edite a aplicação para verificar o ponto de entrada e o ramo, publique-a novamente ou contacte o administrador do PlaidCloud.

### Aspeto

As aplicações Panel de servidor utilizam por predefinição o design moderno **FAST** do PlaidCloud, mas a definição **Design** da aplicação pode repô-las no estilo **Predefinição** do Panel quando o CSS existente depende dele. O tema — claro, escuro ou um comutador claro/escuro que os visualizadores podem alternar — é definido no modelo da sua aplicação. Consulte [Definir o tema](/pt-pt/guides/panel-apps/creating/#definir-o-tema-claro-escuro-ou-alternável) no guia de criação para ver os padrões. Se as tabelas ou o estilo personalizado da sua aplicação foram concebidos para um fundo claro, mantenha-a fixa no tema claro.

## Ver registos (aplicações de servidor)

Clique no ícone **Ver registos** na linha de uma aplicação de servidor para abrir o respetivo visualizador de registos. (As aplicações WASM são executadas inteiramente no browser e não têm registos de servidor, pelo que o ícone só aparece nas linhas de aplicações de servidor.)

O visualizador tem dois separadores:

- **Tempo de execução** (apresentado em primeiro lugar) — a saída da própria aplicação em execução: tudo o que regista, tudo o que imprime e quaisquer erros não tratados. Estes dados são conservados mesmo depois de a aplicação reduzir para zero, pelo que pode rever o que uma sessão anterior fez.
- **Compilação** — a saída da compilação do contentor da aplicação. Utilize-a para ver *porque* é que uma compilação mostra **Falhou** — por exemplo, uma dependência que não foi instalada.

Cada separador oferece filtros **Informação / Aviso / Erro**, um intervalo de tempo **Registos desde** (da última hora até 30 dias, ou todos), um botão **Atualizar** e **Atualização automática** para consultar novas entradas — útil enquanto acompanha uma aplicação em execução ou uma compilação em curso. As entradas mais recentes são listadas primeiro.

> Se não for possível capturar a saída da compilação, o separador Compilação mostra uma breve nota a explicar o motivo, em vez de aparecer vazio.

### Ler uma mensagem de registo completa

A tabela de registos corta as linhas longas para manter a lista legível. Selecione uma linha de registo para abrir um **painel de detalhe** junto à tabela que mostra a mensagem completa da entrada. Esta é a forma mais simples de ler algo demasiado longo para a tabela — uma mensagem de erro extensa ou um rastreio de pilha completo — sem que seja cortado.

### Copiar linhas de registo

Pode selecionar várias linhas de registo em simultâneo e clicar em **Copiar** para as colocar na área de transferência. É útil para colar registos numa conversa com um assistente de IA enquanto depura a sua aplicação, ou numa mensagem para a sua equipa ou para o suporte do PlaidCloud.

### Quem originou uma linha de registo

Quando a sua aplicação autentica os visualizadores, cada linha de registo é etiquetada com o **utilizador** cuja sessão a produziu, para que possa saber que visualizador encontrou determinado erro ou aviso. A etiquetagem é feita com o melhor esforço — algumas linhas da framework e do arranque são executadas antes de existir qualquer visualizador e podem não mostrar um utilizador.

## Métricas de utilização (aplicações de servidor)

Clique no ícone **Usage Metrics** na linha de uma aplicação de servidor — junto a **Ver registos** — para ver como a aplicação está a ser utilizada. A vista resume:

- **Utilizadores únicos** — quantas pessoas distintas abriram a aplicação.
- **Sessões** — quantas vezes foi aberta.
- **Duração média e mediana das sessões** — aproximadamente quanto tempo dura uma visita.
- **Última utilização** — quando a aplicação foi aberta pela última vez.

Abaixo do resumo, encontra uma decomposição **por utilizador** e **por dia**, para ver quem está a utilizar a aplicação e como a utilização evolui ao longo do tempo.

> As durações são aproximadas. As aplicações de servidor ficam inativas e reduzem a escala quando ninguém as utiliza, pelo que o fim exato de uma sessão nem sempre é observado — considere os valores de duração como uma indicação, não como uma medição exata.

## Editar uma aplicação

Clique no ícone de **lápis** na linha de uma aplicação para a editar. O formulário de edição corresponde ao tempo de execução da aplicação.

Numa aplicação de **servidor**, pode alterar o nome, o slug, o ramo, o ponto de entrada, o CPU, a memória, o design, o período de inatividade, a opção de acesso público, os domínios de disponibilização incorporada e a memória descritiva. A **Ligação Git** é fixada quando a aplicação é criada e é apresentada só de leitura. Guardar recompila a aplicação — o respetivo estado regressa a **A compilar…** até a nova compilação estar pronta.

## Remover uma aplicação

Clique no ícone de **menos** na linha de uma aplicação e confirme; eliminar ou anular a publicação de uma aplicação pede sempre confirmação primeiro. Remover uma aplicação de servidor desfaz a respetiva compilação e implementação; remover uma aplicação WASM anula a publicação do ficheiro estático. O URL da aplicação deixa de funcionar de imediato.

A ferramenta MCP `panel_deployment_manage` já não oferece a anulação da publicação. Remova antes uma aplicação a partir desta lista.
