---
title: Execução condicional de etapas
description: Configure a execução condicional das etapas de um fluxo de trabalho do PlaidCloud para controlar quais etapas são executadas com base em valores de variáveis e lógica.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/step-conditions.md
---

## Visão geral

As etapas de um fluxo de trabalho normalmente são executadas na ordem definida para o fluxo de trabalho. No entanto, muitas vezes é útil que certas etapas só sejam executadas se condições predefinidas forem atendidas. Com o recurso de condições de etapa, você pode controlar a execução com base nas seguintes opções:
 - Valores de variáveis
 - A tabela tem linhas ou está vazia
 - A tabela existe ou não existe
 - Um arquivo existe em Documentos
 - Um arquivo está ausente em Documentos
 - Resultado de consulta de tabela
 - Condições de data e hora são atendidas

Para comparações de variáveis ou de resultados de consulta de tabela, você pode usar as seguintes comparações:
 - Igual
 - Diferente
 - Contém
 - Não contém
 - Começa com
 - Termina com
 - Maior que
 - Menor que
 - Maior ou igual
 - Menor ou igual

Também é importante observar que você pode ter várias condições que precisam ser atendidas para que a etapa seja executada. Isso oferece uma ferramenta poderosa para controlar exatamente quando uma etapa deve ser executada.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 640 190" role="img" aria-label="Uma condição de etapa determina se uma etapa é executada. Quando a etapa anterior termina, a condição é verificada; se for atendida, a etapa é executada; caso contrário, a etapa é ignorada e o fluxo de trabalho continua para a próxima etapa." style="width:100%;max-width:640px;height:auto;">
  <defs><marker id="sc3-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="74" width="104" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="66" y="100" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">etapa anterior</text>
  <path d="M118 96 L150 96" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <rect x="152" y="66" width="150" height="60" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="227" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">condição atendida?</text>
  <text x="227" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">variável · linhas · doc existe</text>
  <path d="M302 82 C340 82 350 54 384 54" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="345" y="48" text-anchor="middle" font-size="10" fill="var(--sl-color-accent)">verdadeiro</text>
  <path d="M302 110 C340 110 350 138 384 138" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="5 4" marker-end="url(#sc3-arrow)" />
  <text x="345" y="132" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">falso</text>
  <rect x="386" y="34" width="128" height="40" rx="8" fill="var(--sl-color-accent)" fill-opacity="0.12" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="450" y="59" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-text)">etapa executada</text>
  <rect x="386" y="118" width="128" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="450" y="143" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">etapa ignorada</text>
  <path d="M514 54 C548 54 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <path d="M514 138 C548 138 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="606" y="100" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">próxima</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Uma condição controla a etapa: atendida → a etapa é executada; não atendida → ela é ignorada. De qualquer forma, o fluxo de trabalho segue para a próxima etapa. As condições testam variáveis, se uma tabela tem linhas ou se um documento existe.</figcaption>
</figure>

## Adicionar e controlar condições

Para ativar e adicionar condições em uma etapa:
1) Encontre a etapa na qual você quer adicionar uma condição
2) Clique com o botão direito na etapa e escolha **Editar detalhes da etapa**, ou clique no ícone de engrenagem e vá para a guia **Geral**
3) Role até a seção **Verificações de condição**, na parte inferior da guia **Geral**
4) Marque a caixa de seleção **Verificar condições antes de executar** para habilitar a caixa de diálogo e adicionar condições.
5) Na seção **Verificações de condição**, à esquerda, selecione o "+" para adicionar uma nova condição
6) Adicione uma condição na seção com guias à direita
7) Repita as etapas 5 e 6 conforme necessário para adicionar todas as suas condições

## Ver condições na tela visual

As condições de uma etapa ficam visíveis na tela visual sem abrir a etapa. O conector que leva a uma etapa condicional é **tracejado** e tem um pequeno **escudo** na ponta da seta. O tracejado é o que você lê quando está com um zoom afastado o bastante para que o escudo fique pequeno demais para ser distinguido.

Clique no escudo para abrir a etapa com as **Verificações de condição** já visíveis na rolagem — você também pode clicar com o botão direito no conector e escolher **Editar condições…**, que faz a mesma coisa. O escudo no bloco da própria etapa, no canto inferior esquerdo, continua marcando a etapa como condicional, como sempre fez.

Dois casos não mostram escudo em uma seta, por design:

- **Uma etapa sem conector de entrada.** Uma etapa controlada por uma data ou uma variável pode ficar no início de um fluxo de trabalho sem nada levando até ela. Não há seta para marcar, então só aparece o escudo do bloco.
- **Uma etapa dentro de um grupo recolhido.** O bloco dela é incorporado ao do grupo, e a seta se ancora no grupo e não na etapa, então marcá-la atribuiria a condição à coisa errada.

Uma etapa com vários conectores de entrada recebe um escudo, não um por seta.

:::note
Abrir as condições dessa forma leva às verificações de condição dos tipos de etapa que usam o formulário de etapa nativo. Um tipo de etapa que ainda abre a janela de configuração mais antiga a abre no topo — as condições estão lá, apenas sem rolagem até elas.
:::

### O que o escudo diz que verifica

A dica do escudo lista o que a etapa realmente verifica, em vez de apenas informar
que ela verifica alguma coisa:

```
Table Row Count (sales_2026) > 0 where region = 'EU'
Day of Week = Monday (UTC+2)
Project Variable (run_mode) = "full"
```

Até três verificações são listadas, seguidas de uma contagem das restantes — *…e mais 2 verificações* — para que
a lista continue legível em uma etapa com muitas condições. O mesmo resumo aparece no
escudo do bloco da própria etapa, que é o único que uma etapa sem conector de entrada tem.

Selecionar a etapa coloca a mesma lista na seção **Condições** do painel
Inspetor, que é o lugar mais fácil para ler uma lista longa.

Algumas coisas a esperar quanto à redação:

- **As verificações de dia e mês são lidas como nomes**, não como os números armazenados para elas — *Dia da
  semana = segunda-feira*, não *Dia da semana = 3*.
- **O fuso horário aparece somente quando não é UTC**, como em *(UTC+2)* acima.
- **Um filtro em uma verificação de tabela é exibido** depois de `where`, abreviado se for longo.
- **Uma comparação agregada informa isso** — *Valor da consulta (aggregated sales_2026.amount) >=
  100* compara um total da tabela, enquanto *Valor da consulta (sales_2026.amount) >= 100*
  compara o valor de uma única linha.
- **Uma verificação de documento mostra o caminho, mas não a conta.** Duas condições que verificam o
  mesmo caminho em contas de documentos diferentes são lidas de forma idêntica; abra a etapa para
  distingui-las.
- **Uma tabela escolhida no navegador em árvore mostra seu nome** quando o fluxo de trabalho lê ou
  grava essa tabela em algum lugar. Se isso não acontecer, a verificação é listada sem o nome da tabela
  em vez de com um identificador interno.


### Quanto a condição custaria a você

Passe o mouse sobre o escudo sem clicar, e a tela destaca com um contorno tracejado a etapa condicional e tudo o que vem depois dela — as etapas que não seriam executadas se essa condição bloqueasse. Nada muda; afaste o ponteiro e o destaque desaparece. As etapas *anteriores* nunca são destacadas: elas são executadas de qualquer forma.

Esta é a mesma pré-visualização que o indicador **desativado** de um grupo desativado oferece, com uma diferença de redação que importa. Um grupo desativado está realmente desligado, então seu indicador diz quantas etapas *serão* ignoradas. Uma condição só é avaliada quando a execução chega até ela, então o escudo diz quantas etapas *não seriam* executadas **se** a condição bloquear. Ela pode muito bem deixar tudo passar.

### O que o escudo diz sobre a última execução

O escudo também informa o que aconteceu na execução mais recente, para que você possa rastrear um fluxo concluído e ver onde ele parou:

| Escudo | Significado |
| --- | --- |
| Escudo simples | A etapa é condicional. Ela ainda não foi executada ou está sendo executada agora. |
| Escudo com um **+** | A etapa foi executada na última execução. |
| Escudo com um **−** | A etapa não foi executada na última execução. |

Os três se distinguem pela forma, não pela cor, e a dica do escudo descreve o estado em palavras. Ele é atualizado em tempo real enquanto um fluxo de trabalho está em execução, então você não precisa recarregar a tela para ver uma execução chegar a uma condição.

:::caution
Um escudo com um **−** informa que a etapa não foi executada. Ele não informa *por quê*, e você não deve interpretá-lo como "a condição a bloqueou". Uma etapa também é registrada como não executada quando está desativada, quando seu grupo está desativado, quando uma etapa anterior a ela falhou ou quando ficou fora do escopo de uma execução parcial. O botão **Ver logs** da barra de ferramentas abre o [log de execução](/pt-br/guides/workflows/viewing-workflow-log/), que informa o motivo de cada etapa que ele ignorou. Uma etapa retida em um ponto de interrupção é o único caso deliberadamente excluído — ela mantém o escudo simples, porque pausar ali foi uma decisão sua, e não um resultado da execução.
:::


## Gerenciar condições

Você pode adicionar quantas condições forem necessárias na seção **Verificações de condição**. Ao adicioná-las, é uma boa ideia dar a elas um nome útil para encontrá-las facilmente no futuro.

Depois de adicionar uma condição, selecione-a à esquerda e os critérios de avaliação da condição ficarão editáveis à direita.

Para renomear uma condição, selecione-a e edite o campo **Nome** na parte superior do painel Configuração à direita — ou clique duas vezes na condição na lista. Você também pode clicar com o botão direito em uma condição para **Renomear** e **Excluir**; **Excluir** também está disponível no botão "−" acima da lista.

Uma condição sem tipo de condição selecionado — uma herdada de um fluxo de trabalho mais antigo ou importado, por exemplo — não pode ser avaliada. Ela é tratada como não atendida, então a etapa é ignorada, e a mensagem da etapa diz que a condição não indica o que verificar. Abra a condição e escolha o que ela deve verificar.


## Condições de variável

Ao verificar condições de variável, a seção **Value Check Parameters** precisa ser preenchida para que uma comparação possa ser feita.

Em **Variable or Table Field**, preencha o nome da variável. Selecione um tipo de comparação e insira um valor de comparação.


## Condições básicas de tabela

Se a condição verifica se uma tabela tem linhas ou está vazia, você também precisará definir a tabela na guia **Seleção de dados da tabela**.


## Condições de existência de tabela

Uma condição de existência de tabela executa a etapa somente quando a tabela foi criada no warehouse, ou somente quando ela não foi. Ela nunca lê as linhas da tabela, e uma tabela gravada com zero linhas existe. Um nome de tabela que não corresponde a nenhuma tabela do projeto conta como ausente. Use-a para construir uma tabela na primeira execução e deixá-la como está depois, ou para ignorar uma etapa que lê uma tabela que uma etapa anterior pode não ter criado.

Os dois tipos de verificação são `radio_table_exists` e `radio_table_not_exists`. Escolha a tabela da mesma forma que em uma condição básica de tabela. Defina a condição com um assistente de IA ou com a API REST; a guia **Verificações de condição** ainda não a lista.

## Condições avançadas de tabela

Ao usar condições avançadas de tabela, a seção **Value Check Parameters** precisa ser preenchida para que uma comparação possa ser feita.

Em **Variable or Table Field**, preencha o nome do campo da seleção de tabela. Selecione um tipo de comparação e insira um valor de comparação.

Na guia **Seleção de dados da tabela**, selecione a tabela e preencha a seção de mapeamento de dados com pelo menos o campo referenciado na comparação da condição.

## Condições de caminho de documento

Se a condição verifica se um arquivo existe, é preciso escolher a **Conta de documentos** e especificar o caminho do documento a verificar na guia **Caminho do documento**. Uma pasta nesse caminho conta como ausente, porque a verificação é de um arquivo.

## Condições de data e hora

Para seleções de data ou hora, você pode adicionar várias condições se for necessária uma combinação delas. Por exemplo, se você quisesse que uma etapa fosse executada somente às segundas-feiras às 2h05, criaria três condições:
 - Condição de dia da semana definida como segunda-feira (1)
 - Hora do dia definida como 2
 - Minuto da hora definido como 5

### Deslocamento de fuso horário

Cada condição de data e hora tem seu próprio **Deslocamento de fuso horário**, listado como um deslocamento de horas inteiras com o nome de um fuso representativo — por exemplo, *Eastern Time (US & Canada) (UTC -5)* ou *Asia/Tokyo (UTC +9)*. Os horários que você insere são comparados com o relógio desse fuso.

Uma nova condição começa com o deslocamento informado pelo seu navegador, então na maioria dos casos você pode deixá-lo como está. Defina-o deliberadamente quando o agendamento pertencer a um lugar diferente de onde você está — um fechamento que roda no relógio da equipe financeira, por exemplo. Somente horas inteiras estão disponíveis, então um fuso de meia hora, como a Índia (UTC +5:30), precisa ser arredondado para a hora inteira mais próxima.

Uma condição salva antes de essa configuração entrar em vigor continua sendo avaliada em UTC até que você escolha um fuso para ela, então as condições existentes continuam se comportando exatamente como antes.

:::caution
As condições de **Dia da semana** atualmente comparam com UTC, qualquer que seja o deslocamento escolhido. Se você precisa que uma condição de dia da semana caia em um dia específico em um fuso distante do UTC, saiba que ela pode diferir do seu dia local por várias horas antes e depois da meia-noite.
:::

### Fechamento financeiro Workday

Para **Use Financial Close Workday**, a contagem começa em **0 para o dia 1º do mês** — como a dica ao lado do campo informa. Então um fechamento que acontece no 5º dia do mês é `4`, não `5`.

:::caution
Esta condição atualmente nunca é atendida, então uma etapa protegida por ela não será executada. Use uma condição **Day of the month** até que isso seja resolvido. Valores negativos, destinados a contar de trás para frente a partir do fim do mês, também não funcionam.
:::

## Definir condições com um assistente de IA

Um assistente de IA conectado ao seu espaço de trabalho pode adicionar e alterar as condições de uma etapa para você, seja ao criar a etapa ou ao editar uma que você já tem. Todos os tipos de condição descritos anteriormente estão disponíveis para ele, exceto **Verificar fechamento financeiro do Workday**: um assistente pode escrevê-la, mas ela nunca é atendida, então o assistente avisa você em vez de deixá-la passar despercebida. Defina essa na guia **Condições** por conta própria.

Três coisas funcionam de forma diferente da edição manual de condições:

- **A lista inteira é substituída a cada vez.** Peça para adicionar ou alterar uma condição e o assistente envia a lista completa, então qualquer condição que ele deixar de fora é removida. Se você não tem certeza de que ele incluiu todas, peça que liste as condições atuais da etapa antes de gravar.
- **Uma condição que não pode ser avaliada é recusada.** Uma condição que não indica o que verifica é rejeitada em vez de salva, e a etapa mantém as condições que já tinha. Corrija a solicitação e peça novamente.
- **Uma condição incompleta é salva, com um aviso.** Uma condição sem o valor de comparação, ou condições adicionadas sem **Verificar condições antes de executar** marcado, são armazenadas e informadas de volta como um aviso. Abra a guia **Condições** e conclua-as, ou a etapa não se comportará como você pediu.

Um assistente também pode definir o bloqueio da etapa, sua visibilidade nas visões do Gerente e do Explorador, suas configurações de nova tentativa e a etapa para a qual ir em caso de erro.
