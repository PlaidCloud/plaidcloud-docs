---
title: Visualizar projetos
description: Visualize e navegue pelos projetos autorizados do PlaidCloud, incluindo detalhes do projeto, status, membros e recursos de dados associados.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/viewing-projects.md
---

## Descrição


Dentro do **Analyze**, a função Projetos oferece um nível de compartimentalização que facilita muito o controle de acesso e a alteração de privilégios. Os projetos são o que fornece a segregação primária dos dados dentro de uma guia do espaço de trabalho.



Embora os projetos fiquem no Analyze, os fluxos de trabalho ficam nos projetos, ou seja, os projetos contêm fluxos de trabalho. Em termos simples, os fluxos de trabalho executam uma ampla gama de tarefas, incluindo pipelines de transformação de dados, análise de dados e até processos de ETL. Você encontra mais informações sobre fluxos de trabalho na seção "Fluxos de trabalho".



## Acessar projetos


**Para acessar os projetos:**


1. Abra o Analyze
2. Selecione "Projetos" na barra de menus superior

Isso exibe a hierarquia de projetos. Nela, você vê uma hierarquia dos projetos aos quais tem acesso. Pode haver outros projetos no espaço de trabalho, mas, se você não for proprietário nem estiver atribuído ao projeto, eles não ficam visíveis para você.


## O painel de atividade

O painel **Atividade**, à direita da janela Projetos, mostra o que foi executado nos seus projetos, se funcionou e quem alterou o quê. Ele lista a atividade de todos os projetos aos quais você tem acesso, da mais recente para a mais antiga, sob um cabeçalho para cada dia. Ele verifica se há atividade nova a cada 15 segundos, aproximadamente, enquanto a janela Projetos é a janela ativa e a guia do navegador está visível.

O cabeçalho de cada dia mostra **Hoje**, **Ontem** ou a data, com um resumo das linhas desse dia, como "12 execuções · 1 falhou · 3 alterações". O cabeçalho do dia pelo qual você está rolando permanece no topo da lista.

### Execuções

Cada execução de fluxo de trabalho tem uma linha. Um ícone mostra como ela terminou, e passar o ponteiro sobre o ícone informa o estado: Com sucesso, Falhou, Aviso, Interrompido ou Iniciado. As linhas com falha ou aviso também têm uma barra colorida ao longo da borda esquerda.

- **A primeira linha** traz o nome do fluxo de trabalho e a hora: "agora", minutos ou horas atrás para hoje, ou o horário em um dia anterior. Passe o ponteiro sobre a hora para ver a data completa.
- **A segunda linha** diz quem a executou e em qual projeto, como "mike executou · CFO Services", "Execução agendada · CFO Services" ou "Execução do sensor · CFO Services". À direita fica quanto tempo a execução levou, ou **Falhou** ou **Interrompido** com a duração. Uma execução interrompida cita quem a interrompeu.
- **Uma terceira linha**, quando existe, mostra o que deu errado. Quando uma etapa falhou ou emitiu aviso durante a execução, ela mostra o nome da etapa e a mensagem, com "+2 mais" quando outras etapas também tiveram problemas. Clique nessa linha para abrir o fluxo de trabalho nessa etapa.

Enquanto uma execução está em andamento, ela fica listada em [Em execução agora](#em-execução-agora). Quando termina, a linha dela mostra o resultado. Um fluxo de trabalho executado por outro fluxo de trabalho, por meio de uma etapa Fluxo de trabalho: Executar ou como macro, não tem linha própria, e um problema de etapa dentro dele aparece na linha da execução que o chamou. Um problema de etapa cuja execução não está na lista tem uma linha própria, como "Falha na etapa · CRM Pipeline · CFO Services".

As alterações, como em fluxos de trabalho, etapas, tabelas, dimensões e projetos, têm uma linha cada, como "mike modificou a etapa · CFO Services" sob o nome da etapa.

A maioria das linhas abre o que nomeia quando você clica nela ou pressiona Enter sobre ela. Uma execução, ou um fluxo de trabalho que foi criado, modificado, importado ou exportado, abre o projeto na guia **Fluxos de trabalho** com o fluxo de trabalho selecionado. Um problema de etapa, ou uma etapa que foi criada, modificada, excluída, copiada ou movida, abre o fluxo de trabalho nessa etapa. Uma tabela que foi criada, renomeada, publicada ou despublicada abre no Explorador de tabelas, uma dimensão que foi criada ou modificada abre para edição, e um projeto que foi criado, modificado, importado, exportado ou copiado em backup, ou cuja segurança mudou, abre o projeto.

### Linhas repetidas

Edições consecutivas do mesmo tipo feitas pela mesma pessoa no mesmo objeto se recolhem em uma só linha, assim como execuções bem-sucedidas consecutivas do mesmo fluxo de trabalho, iniciadas da mesma forma pela mesma pessoa ou pelo mesmo agendamento. Clique em **3 edições** ou **4 execuções** na linha para ver cada uma delas e clique de novo para recolhê-las.

### Em execução agora

Os fluxos de trabalho que estão em execução agora ficam listados em **Em execução agora**, acima da lista, com quem os iniciou e há quanto tempo estão em execução. Uma execução pausada mostra **Pausado**. Clique no nome de um fluxo de trabalho para selecioná-lo na lista **Fluxos de trabalho** do projeto dele ou clique em **Parar** para interromper essa execução.

### Ações ao passar o ponteiro

Passe o ponteiro sobre a linha de uma execução, ou vá até ela pelo teclado, para mostrar dois botões de ícone, cujas dicas de ferramenta são **Abrir log** e **Executar fluxo de trabalho**:

- **Abrir log** abre o log do projeto, filtrado por esse fluxo de trabalho. A linha de um problema de etapa também tem esse botão.
- **Executar fluxo de trabalho** executa o fluxo de trabalho novamente.

**Parar** e **Executar fluxo de trabalho** são permitidos para os mesmos membros que podem parar e executar o fluxo de trabalho a partir das próprias telas dele. **Executar fluxo de trabalho** executa o fluxo de trabalho inteiro com as configurações padrão, mesmo quando a execução da linha foi uma única etapa, um intervalo de etapas ou uma simulação.

### Problemas e filtros

Quando a atividade carregada tem execuções ou etapas que falharam ou emitiram aviso, o cabeçalho do painel mostra uma contagem como **2 problemas**, marcada como erro quando algum deles falhou. Clique nela para mostrar apenas essas linhas.

A faixa na parte inferior do painel escolhe o que a lista mostra:

| Opção | Mostra |
|---|---|
| **Todos** | Tudo |
| **Execuções** | Execuções de fluxos de trabalho |
| **Alterações** | Alterações em fluxos de trabalho, etapas, tabelas, dimensões, projetos e mais |
| **Problemas** | Execuções e etapas que falharam ou emitiram aviso |
| **Minhas** | Suas próprias execuções e alterações |

Digite em **Filtro** para mostrar apenas as linhas cujo nome de fluxo de trabalho, projeto, etapa, tabela, dimensão ou membro contenha o seu texto. A faixa termina com quantos eventos correspondem, como **12 eventos**. O painel lembra, neste navegador, qual opção você escolheu.

### Novidades desde a sua última visita

Uma linha **Novidades desde a sua última visita** separa o que chegou desde a sua visita anterior do que você já tinha visto. Ela aparece quando **Todos** está escolhido e nada está digitado em **Filtro**. Uma visita termina quando você muda para outra janela ou fecha a janela Projetos, e a linha se move na próxima vez que você abrir a janela Projetos ou recarregar a página.

### Mostrar anteriores

A lista começa com os últimos 7 dias. Clique em **Mostrar anteriores** no fim da lista para carregar até 500 eventos a mais dos 30 dias anteriores ao mais antigo carregado e clique de novo para voltar ainda mais. O botão desaparece quando um período de 30 dias não tem atividade.

### Teclado

Pressione Tab para ir até uma linha e use as teclas de seta para cima e para baixo para se mover entre as linhas e Enter para abrir a que você está. Tab também leva às ações da linha ao passar o ponteiro.

### Limites

- **Sua última visita é lembrada por navegador.** Em outro navegador ou dispositivo, a linha **Novidades desde a sua última visita** reflete a sua última visita lá.
- **As contagens descrevem a atividade carregada no painel.** A contagem de problemas, **Problemas** e os resumos dos dias cobrem, no início, os 500 eventos mais recentes dos últimos 7 dias e, depois, mais, conforme você usa **Mostrar anteriores**. Elas não são totais dos seus projetos.
- **Uma execução na fila aparece como Iniciado** e passa a aparecer em **Em execução agora** quando realmente começa. A duração dela é contada a partir do momento em que entrou na fila.
- **Os problemas de etapa de uma macro dentro de uma macro** não aparecem na linha da execução de nível superior.
- **Um fluxo de trabalho executado com frequência** tem muitas linhas. As execuções bem-sucedidas consecutivas se recolhem, mas as de dois fluxos de trabalho que são executados em alternância não.
- **As execuções anteriores ao lançamento deste painel** aparecem como Iniciado, sem resultado, e as interrupções anteriores a essa data não aparecem.
- **Um evento registrado com atraso**, depois que outros mais novos já apareceram, aparece quando você recarrega a página.
- **Uma janela Projetos deixada aberta e sem uso por mais de 30 dias** retoma a partir de 30 dias atrás.
- **Sem atividade nos últimos 7 dias**, o painel mostra "Nenhuma atividade nos últimos 7 dias." e **Mostrar anteriores** não aparece, então não é possível carregar atividades anteriores.
