---
title: Alocações recursivas e recíprocas
description: Modele a distribuição de custos em várias passagens e recíproca no PlaidCloud encadeando passos de alocação em passagens explícitas e faseadas.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/recursive-allocations.md
---

Alguns modelos de custos precisam que o destino de uma alocação passe a ser uma *origem* da seguinte — por exemplo, serviços partilhados que se consomem mutuamente (as TI servem os RH, mas os RH também servem as TI). O PlaidCloud modela isto **encadeando passos de alocação em passagens explícitas e faseadas**, e não através de um único solucionador automático.

## Quando precisa de várias passagens

- **Serviços recíprocos** — dois conjuntos de custos que se consomem mutuamente.
- **Repartições em camadas** — os custos divisionais descem em cascata por uma hierarquia, e os níveis inferiores têm de absorver os superiores antes de voltar a alocar.
- **Equilíbrio iterativo** — o modelo aproxima-se de um resultado estável ao fim de várias passagens (o conjunto A aloca uma parte a B, B devolve uma parte, e assim sucessivamente).

## Como o modelar

O PlaidCloud **não tem "modo de recursividade" incorporado nem solucionador automático de convergência**. Constrói a recursividade por si, adicionando um [passo de divisão de alocação](/pt-pt/reference/workflow-steps/allocation/allocation-split/) separado para cada passagem e ligando-os em sequência:

1. Execute a primeira passagem como uma divisão de alocação normal.
2. Para a passagem seguinte, construa uma origem que inclua a saída da passagem anterior — normalmente unindo ou juntando o resultado anterior de volta ao conjunto — e volte a alocar.
3. Repita para tantas passagens quantas o seu modelo precisar.

Como cada passagem é um passo explícito, **é você quem decide quantas passagens são executadas**. O motor não resolve a relação recíproca como uma única equação simultânea, e não existe nenhuma definição de tolerância que interrompa o ciclo automaticamente. Adicione passagens até o resíduo que falta voltar a alocar ser suficientemente pequeno para os seus fins.

## Sugestões

- Comece com uma alocação de **passagem única** e confirme que o modelo simples se comporta como esperado antes de adicionar passagens.
- Após cada passagem, verifique o resíduo não alocado restante. Se não estiver a diminuir de passagem para passagem, reveja as relações dos drivers — uma verdadeira dependência circular não estabiliza por mais passagens que adicione.
- Cada passagem reprocessa a sua origem, pelo que a recursividade é dispendiosa em grandes conjuntos de dados. Teste numa amostra antes de executar sobre toda a origem.

## Relacionado

- [Configurar uma alocação](/pt-pt/guides/allocations/setup/configure-an-allocation/) — configuração base
- [Passo Allocation Split](/pt-pt/reference/workflow-steps/allocation/allocation-split/) — o passo de fluxo de trabalho que encadeia para cada passagem
- [Resolução de problemas de alocações](/pt-pt/guides/allocations/results/troubleshooting-allocations/) — quando os resíduos não fazem sentido
