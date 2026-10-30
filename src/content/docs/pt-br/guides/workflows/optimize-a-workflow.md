---
title: Otimizar um fluxo de trabalho
description: Faça um fluxo de trabalho avançado ser executado mais rápido reconstruindo suas dependências a partir da linhagem de dados e mesclando cadeias de etapas de extração, com cada mesclagem verificada nos seus dados antes de ser aplicada.
sidebar:
  order: 19.6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/optimize-a-workflow.md
---

**Otimizar** analisa um fluxo de trabalho avançado e propõe alterações que o fazem ser executado mais rápido. Você vê cada alteração antes que qualquer coisa aconteça, escolhe as que deseja e pode desfazer o resultado depois.

A otimização funciona em fluxos de trabalho avançados (DAG). Para um fluxo de trabalho padrão, escolha primeiro **Converter em avançado...**; consulte [Fluxos de trabalho avançados](/pt-br/guides/workflows/advanced-workflows/#escolher-o-tipo-de-fluxo-de-trabalho).

## Otimizar um fluxo de trabalho

1. Na lista **Fluxos de trabalho**, clique com o botão direito em um fluxo de trabalho avançado e escolha **Otimizar...**. O fluxo de trabalho não pode estar em execução nem pausado, e você precisa de acesso de gravação a ele.
2. A janela **Otimizar fluxo de trabalho** mostra um resumo como *34 etapas → 30 etapas · 12 etapas podem ser executadas em paralelo*. Quando o fluxo de trabalho tem histórico de execuções, ela acrescenta *~11 s mais rápido por execução*.
3. Abaixo do resumo há uma linha por alteração, cada uma com uma caixa de seleção, as etapas que ela afeta, o que ela significa para o fluxo de trabalho e o tempo que economiza, medido como a variação no tempo real de execução. Todas vêm marcadas; desmarque as que você não quiser.
4. Uma lista **Não é possível otimizar** nomeia as etapas que a otimização deixou de lado e o motivo específico de cada uma; consulte [Por que uma etapa não pode ser otimizada](#por-que-uma-etapa-não-pode-ser-otimizada).
5. Escolha **Aplicar N alterações**.

Se o fluxo de trabalho não tiver mais nada a melhorar, a janela informa isso.

## Os dois tipos de alteração

### Reconstruir dependências a partir da linhagem de dados

A otimização lê quais tabelas cada etapa lê e grava e redesenha as conexões para que uma etapa espere apenas pelas etapas cujas tabelas ela usa. Etapas que não compartilham tabelas são executadas em paralelo.

- Uma etapa deixa de esperar por etapas não relacionadas e, portanto, não para mais quando uma etapa não relacionada falha. Uma falha se propaga ao longo das novas dependências.
- Uma execução parcial por intervalo de etapas, como **Executar a partir daqui**, segue as novas dependências.
- O servidor continua limitando quantas etapas são executadas ao mesmo tempo.
- Etapas que indicam suas tabelas por nome ou caminho são entendidas da mesma forma que etapas que usam IDs de tabela. Um nome deve corresponder a exatamente uma tabela no projeto; um nome que corresponde a várias tabelas, uma referência que usa uma variável e uma tabela de outro projeto não podem ser rastreados.
- Uma etapa desabilitada nunca carrega uma ordenação e não conta para as etapas que podem ser executadas em paralelo.
- A otimização deixa de fora essa alteração enquanto um agendamento ou outro fluxo de trabalho executa um intervalo das etapas deste fluxo de trabalho.

### Mesclar uma cadeia de etapas de extração em uma só

Uma cadeia de etapas de extração de dados, cada uma lendo a tabela gravada pela anterior, torna-se uma única etapa que lê a primeira origem e grava o último resultado.

Cada mesclagem é verificada antes de ser aplicada. A otimização executa as etapas originais e a etapa mesclada nos seus dados atuais em tabelas temporárias e compara os dois resultados linha por linha. Ela aplica a mesclagem somente quando são idênticos. Seu fluxo de trabalho e suas tabelas não são tocados durante a verificação.

- Uma renomeação seguida de um filtro, como uma etapa de seleção seguida de um filtro, pode ser mesclada em uma única etapa.
- Quando uma cadeia inteira não pode ser mesclada, a otimização oferece a maior parte dela que pode.
- As tabelas no meio de uma cadeia mesclada deixam de ser gravadas pelo fluxo de trabalho. Elas são mantidas, não excluídas, e a alteração as nomeia.
- Uma mesclagem cujos resultados diferem, ou que não pode ser verificada, não é aplicada, e os resultados informam o motivo. As mesclagens exigem uma tabela de origem com dados.

## Por que uma etapa não pode ser otimizada

Cada linha em **Não é possível otimizar** nomeia sua própria causa:

| Causa | O que significa |
|---|---|
| Agregações | A etapa resume linhas, então não pode ser incorporada a uma vizinha. |
| Dois filtros | Uma cadeia com dois filtros não pode se tornar uma única etapa. |
| Filtro em um float que pode arredondar | A mesclagem poderia mudar quais linhas passam, então o filtro permanece onde está. |
| Uma etapa que executa código do usuário | Expressões, scripts e etapas semelhantes não podem ter sua equivalência verificada. |
| Uma tabela lida por mais de uma etapa | A tabela no meio da cadeia é necessária em outro lugar. |
| Etapa desabilitada | Uma etapa desabilitada não é mesclada e não carrega uma ordenação. |
| Membro de um contêiner de execução | As etapas em um contêiner de execução são executadas como uma unidade. |
| Contagem de linhas indisponível | A contagem de linhas da tabela de origem não pode ser lida, nem mesmo ao vivo, então a mesclagem não pode ser dimensionada para verificação. |
| A tabela não pode ser identificada | O nome da tabela da etapa não corresponde a nenhuma tabela ou corresponde a mais de uma, usa uma variável ou aponta para outro projeto. |
| Segurança em nível de linha ou grande demais | A tabela é regida por segurança em nível de linha ou é grande demais para ser verificada automaticamente. |

Contêineres visuais, que apenas agrupam etapas na tela, não impedem uma mesclagem. Quando uma mesclagem remove etapas de um deles, a etapa mesclada toma o lugar delas, e um contêiner que fica vazio é descartado. Desfazer restaura o layout exatamente.

## Acompanhar o progresso

Depois de aplicar, **Otimizando fluxo de trabalho** mostra a fase: *Verificando (3 de 6 execuções)...*, *Comparando resultados...* e *Aplicando...*. Ao terminar, os resultados listam o que foi **Aplicado**, incluindo em quantas linhas cada mesclagem foi verificada, e o que **Não aplicado**, com um motivo para cada item.

Se o fluxo de trabalho mudou enquanto a otimização estava verificando, as alterações afetadas são ignoradas e a janela informa quantas. Se uma aplicação falhar, o fluxo de trabalho é restaurado ao estado em que estava antes.

Uma execução que começa enquanto as alterações estão sendo confirmadas é adiada por um instante, não descartada.

## Desfazer uma otimização

Clique com o botão direito no fluxo de trabalho e escolha **Desfazer otimização...**, ou use **Desfazer otimização** nos resultados. Confirme, e as etapas, as configurações e o layout do fluxo de trabalho voltam ao estado anterior à otimização. As alterações feitas no fluxo de trabalho desde então são perdidas.

Desfazer exige pontos de restauração, que não estão disponíveis em todos os tenants. Um tenant sem eles não pode aplicar uma otimização.

## Otimizar pela API e por assistentes de IA

A otimização também está disponível pela API REST e pela ferramenta `workflow_optimize` para assistentes de IA, com as mesmas etapas de pré-visualização, aplicação e desfazer.

## Próximos passos

- [Fluxos de trabalho avançados](/pt-br/guides/workflows/advanced-workflows/) — a tela, as conexões e os controles de execução
- [Controlar a execução paralela](/pt-br/guides/workflows/controlling-parallel-execution/) — execute etapas ao mesmo tempo
- [Executar um fluxo de trabalho](/pt-br/guides/workflows/run-a-workflow/) — executar um fluxo de trabalho de ponta a ponta
