---
title: Ver projetos
description: Veja e navegue pelos projetos PlaidCloud autorizados, incluindo detalhes do projeto, estado, membros e recursos de dados associados.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/viewing-projects.md
---

## Descrição


No **Analyze**, a função Projetos proporciona um nível de compartimentação que torna muito mais fácil controlar o acesso e modificar privilégios. Os projetos são o que proporciona a principal segregação de dados dentro de um separador da área de trabalho.



Embora os Projetos estejam sob o Analyze, os fluxos de trabalho estão sob os Projetos, o que significa que os Projetos contêm fluxos de trabalho. Os fluxos de trabalho, em termos simples, executam uma vasta gama de tarefas, incluindo pipelines de transformação de dados, análise de dados e até processos ETL. Pode encontrar mais informações sobre os fluxos de trabalho na secção “Fluxos de trabalho”.



## Aceder aos projetos


**Para aceder aos Projetos:**


1. Abra o Analyze
2. Selecione “Projetos” na barra de menus superior

Isto apresenta a Hierarquia de projetos. A partir daqui, verá uma hierarquia dos projetos a que tem acesso. Pode haver projetos adicionais na área de trabalho mas, se não for proprietário nem estiver atribuído ao projeto, não serão visíveis para si.


## O painel de atividade

O painel **Atividade**, à direita da janela Projetos, mostra o que foi executado nos seus projetos, se correu bem e quem alterou o quê. Lista a atividade de todos os projetos a que tem acesso, da mais recente para a mais antiga, sob um cabeçalho para cada dia. Verifica se há atividade nova aproximadamente a cada 15 segundos, enquanto a janela Projetos for a janela ativa e o separador do navegador estiver visível.

O cabeçalho de cada dia indica **Hoje**, **Ontem** ou a data, com um resumo das linhas desse dia, como "12 execuções · 1 falhou · 3 alterações". O cabeçalho do dia que está a percorrer permanece no topo da lista.

### Execuções

Uma execução de um fluxo de trabalho tem uma linha. Um ícone mostra como correu, e, ao passar o cursor sobre o ícone, é indicado o estado: Com êxito, Falhou, Aviso, Interrompido ou Iniciado. As linhas com uma falha ou um aviso têm também uma barra colorida ao longo da margem esquerda.

- **A primeira linha** indica o fluxo de trabalho e a hora: "agora", há minutos ou horas para hoje, ou a hora do relógio num dia anterior. Passe o cursor sobre a hora para ver a data completa.
- **A segunda linha** indica quem a executou e em que projeto, como "mike executou · CFO Services", "Execução agendada · CFO Services" ou "Execução do sensor · CFO Services". À direita está a duração da execução, ou **Falhou** ou **Interrompido** com a respetiva duração. Uma execução interrompida indica quem a interrompeu.
- **Uma terceira linha**, quando existe, mostra o que correu mal. Quando um passo falhou ou emitiu um aviso durante a execução, mostra o nome do passo e a sua mensagem, com "+2 mais" quando outros passos também tiveram problemas. Clique nessa linha para abrir o fluxo de trabalho nesse passo.

Enquanto uma execução está em curso, aparece em [Em execução agora](#em-execução-agora). Quando termina, a sua linha mostra o resultado. Um fluxo de trabalho executado por outro fluxo de trabalho, através de um passo Fluxo de trabalho: Executar ou como macro, não tem linha própria, e um problema de passo no seu interior aparece na linha da execução que o chamou. Um problema de passo cuja execução não consta da lista tem uma linha própria, como "Falha no passo · CRM Pipeline · CFO Services".

As alterações, como as de fluxos de trabalho, passos, tabelas, dimensões e projetos, têm uma linha cada, como "mike modificou o passo · CFO Services" sob o nome do passo.

A maioria das linhas abre o que nomeiam quando clica nelas ou prime Enter nelas. Uma execução, ou um fluxo de trabalho que foi criado, modificado, importado ou exportado, abre o seu projeto no separador **Fluxos de trabalho** com o fluxo de trabalho selecionado. Um problema de passo, ou um passo que foi criado, modificado, eliminado, copiado ou movido, abre o fluxo de trabalho nesse passo. Uma tabela que foi criada, renomeada, publicada ou despublicada abre-se no Explorador de tabelas, uma dimensão que foi criada ou modificada abre para edição, e um projeto que foi criado, modificado, importado, exportado ou copiado para segurança, ou cuja segurança foi alterada, abre o projeto.

### Linhas repetidas

As edições consecutivas do mesmo tipo, feitas pela mesma pessoa ao mesmo objeto, reúnem-se numa única linha, tal como as execuções bem-sucedidas consecutivas do mesmo fluxo de trabalho, iniciadas da mesma forma pela mesma pessoa ou agendamento. Clique em **3 edições** ou **4 execuções** na linha para ver cada uma delas, e clique novamente para as recolher.

### Em execução agora

Os fluxos de trabalho que estão em execução agora aparecem em **Em execução agora**, acima da lista, com quem os iniciou e há quanto tempo estão em execução. Uma execução em pausa indica **Em pausa**. Clique no nome de um fluxo de trabalho para o selecionar na lista **Fluxos de trabalho** do respetivo projeto, ou clique em **Parar** para parar essa execução.

### Ações ao passar o cursor

Passe o cursor sobre a linha de uma execução, ou desloque-se até ela com o teclado, para mostrar dois botões de ícone, cujas descrições indicam **Abrir registo** e **Executar fluxo de trabalho**:

- **Abrir registo** abre o registo do projeto, filtrado por esse fluxo de trabalho. A linha de um problema de passo também tem este botão.
- **Executar fluxo de trabalho** executa novamente o fluxo de trabalho.

**Parar** e **Executar fluxo de trabalho** são permitidos aos mesmos membros que podem parar e executar o fluxo de trabalho a partir dos seus próprios ecrãs. **Executar fluxo de trabalho** executa o fluxo de trabalho completo com as respetivas definições predefinidas, mesmo quando a execução da linha foi um único passo, um intervalo de passos ou uma simulação.

### Problemas e filtros

Quando a atividade carregada tem execuções ou passos que falharam ou emitiram um aviso, o cabeçalho do painel mostra uma contagem como **2 problemas**, assinalada como erro quando algum deles falhou. Clique nela para mostrar apenas essas linhas.

A faixa na parte inferior do painel escolhe o que a lista mostra:

| Opção | Mostra |
|---|---|
| **Todos** | Tudo |
| **Execuções** | Execuções de fluxos de trabalho |
| **Alterações** | Alterações a fluxos de trabalho, passos, tabelas, dimensões, projetos e mais |
| **Problemas** | Execuções e passos que falharam ou emitiram um aviso |
| **Minhas** | As suas próprias execuções e alterações |

Escreva em **Filtro** para mostrar apenas as linhas cujo nome de fluxo de trabalho, projeto, passo, tabela, dimensão ou membro contenha o seu texto. A faixa termina com o número de eventos que correspondem, como **12 eventos**. O painel memoriza a opção que escolheu, neste navegador.

### Novidades desde a última visita

Uma linha **Novidades desde a sua última visita** separa o que chegou desde a sua visita anterior do que já tinha visto. Aparece quando **Todos** está escolhido e não há nada escrito em **Filtro**. Uma visita termina quando muda para outra janela ou fecha a janela Projetos, e a linha avança na próxima vez que abrir a janela Projetos ou recarregar a página.

### Mostrar anteriores

A lista começa com os últimos 7 dias. Clique em **Mostrar anteriores** no fim da lista para carregar até 500 eventos adicionais dos 30 dias anteriores ao mais antigo carregado, e clique novamente para recuar mais. Desaparece quando um período de 30 dias não tem atividade.

### Teclado

Prima Tab para se deslocar até uma linha e use as teclas de seta para cima e para baixo para se deslocar entre linhas e Enter para abrir aquela em que está. A tecla Tab também desloca para as ações da linha ao passar o cursor.

### Limites

- **A sua última visita é memorizada por navegador.** Noutro navegador ou dispositivo, a linha **Novidades desde a sua última visita** reflete a sua última visita aí.
- **As contagens descrevem a atividade carregada no painel.** A contagem de problemas, **Problemas** e os resumos diários abrangem inicialmente os 500 eventos mais recentes dos últimos 7 dias, e mais à medida que usa **Mostrar anteriores**. Não são totais dos seus projetos.
- **Uma execução em fila aparece como Iniciado** e passa a aparecer em **Em execução agora** quando realmente começa. A sua duração conta desde que foi colocada em fila.
- **Os problemas de passo de uma macro dentro de uma macro** não aparecem na linha da execução de nível superior.
- **Um fluxo de trabalho que é executado com frequência** tem muitas linhas. As execuções bem-sucedidas lado a lado reúnem-se, mas as de dois fluxos de trabalho que são executados à vez não.
- **As execuções anteriores à disponibilização deste painel** aparecem como Iniciado, sem resultado, e as paragens anteriores a essa data não aparecem.
- **Um evento registado com atraso**, depois de já terem aparecido outros mais recentes, aparece quando recarrega a página.
- **Uma janela Projetos deixada aberta e sem utilização durante mais de 30 dias** retoma a partir de 30 dias atrás.
- **Sem atividade nos últimos 7 dias**, o painel indica "Nenhuma atividade nos últimos 7 dias." e **Mostrar anteriores** não aparece, pelo que não é possível carregar a atividade anterior.
