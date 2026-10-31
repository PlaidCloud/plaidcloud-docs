---
title: Alocações recursivas e recíprocas
description: Modele a distribuição de custos em várias passagens e recíproca no PlaidCloud encadeando etapas de alocação em passagens explícitas e em estágios.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/recursive-allocations.md
---

Alguns modelos de custo precisam que o destino de uma alocação se torne a *origem* da próxima — por exemplo, serviços compartilhados que consomem um ao outro (a TI atende o RH, mas o RH também atende a TI). O PlaidCloud modela isso **encadeando etapas de alocação em passagens explícitas e em estágios**, e não por meio de um único solucionador automático.

## Quando você precisa de várias passagens

- **Serviços recíprocos** — dois pools de custo que consomem um ao outro.
- **Rateios em camadas** — os custos divisionais descem em cascata por uma hierarquia, e os níveis inferiores precisam absorver os superiores antes de realocar.
- **Equilíbrio iterativo** — o modelo se aproxima de um resultado estável após várias passagens (o pool A aloca uma parte para B, B devolve uma parte, e assim por diante).

## Como modelar

O PlaidCloud **não tem um "modo de recursão" nativo nem um solucionador de convergência automático**. Você mesmo constrói a recursão, adicionando uma [etapa de divisão de alocação](/pt-br/reference/workflow-steps/allocation/allocation-split/) separada para cada passagem e ligando-as em sequência:

1. Execute a primeira passagem como uma divisão de alocação normal.
2. Para a passagem seguinte, construa uma origem que inclua a saída da passagem anterior — normalmente unindo ou juntando o resultado anterior de volta ao pool — e aloque novamente.
3. Repita quantas passagens o seu modelo precisar.

Como cada passagem é uma etapa explícita, **você decide quantas passagens são executadas**. O mecanismo não resolve a relação recíproca como uma única equação simultânea, e não há configuração de tolerância que interrompa o ciclo automaticamente. Adicione passagens até que o resíduo ainda a ser realocado seja pequeno o bastante para os seus propósitos.

## Dicas

- Comece com uma alocação de **passagem única** e confirme que o modelo simples se comporta como esperado antes de adicionar passagens.
- Após cada passagem, verifique o resíduo não alocado restante. Se ele não estiver diminuindo a cada passagem, revise as relações do direcionador — uma dependência circular genuína não se estabiliza por mais passagens que você adicione.
- Cada passagem reprocessa sua origem, então a recursão é cara em grandes conjuntos de dados. Teste em uma fatia antes de executar sobre toda a origem.

## Relacionado

- [Configurar uma alocação](/pt-br/guides/allocations/setup/configure-an-allocation/) — configuração básica
- [Etapa Allocation Split](/pt-br/reference/workflow-steps/allocation/allocation-split/) — a etapa de fluxo de trabalho que você encadeia para cada passagem
- [Solução de problemas de alocações](/pt-br/guides/allocations/results/troubleshooting-allocations/) — quando os resíduos não fazem sentido
