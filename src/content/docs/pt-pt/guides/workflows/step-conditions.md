---
title: Execução condicional de passos
description: Configure a execução condicional dos passos de um fluxo de trabalho do PlaidCloud para controlar quais os passos executados com base em valores de variáveis e em lógica.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/step-conditions.md
---

## Descrição geral

Os passos de um fluxo de trabalho são normalmente executados pela ordem definida para o fluxo de trabalho.  No entanto, é muitas vezes útil que determinados passos só sejam executados se forem cumpridas condições predefinidas.  Com a capacidade de condições de passos, pode controlar a execução com base nas seguintes opções:
 - Valores de variáveis
 - A tabela tem linhas ou está vazia
 - A tabela existe ou não existe
 - Existe um ficheiro em Document
 - Falta um ficheiro em Document
 - Resultado de consulta a uma tabela
 - São cumpridas condições de data e hora

Para comparações de variáveis ou de resultados de consultas a tabelas, pode utilizar as seguintes comparações:
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

É também importante notar que pode ter várias condições que têm de ser cumpridas para que o passo seja executado.  Isto proporciona uma ferramenta poderosa para controlar exatamente quando um passo deve ser executado.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 640 190" role="img" aria-label="Uma condição de passo determina se um passo é executado. Quando o passo anterior termina, a condição é verificada; se for cumprida, o passo é executado; caso contrário, o passo é ignorado e o fluxo de trabalho continua para o passo seguinte." style="width:100%;max-width:640px;height:auto;">
  <defs><marker id="sc3-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="74" width="104" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="66" y="100" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">passo anterior</text>
  <path d="M118 96 L150 96" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <rect x="152" y="66" width="150" height="60" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="227" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">condição cumprida?</text>
  <text x="227" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">variável · linhas · doc. existe</text>
  <path d="M302 82 C340 82 350 54 384 54" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="345" y="48" text-anchor="middle" font-size="10" fill="var(--sl-color-accent)">sim</text>
  <path d="M302 110 C340 110 350 138 384 138" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="5 4" marker-end="url(#sc3-arrow)" />
  <text x="345" y="132" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">não</text>
  <rect x="386" y="34" width="128" height="40" rx="8" fill="var(--sl-color-accent)" fill-opacity="0.12" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="450" y="59" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-text)">passo executado</text>
  <rect x="386" y="118" width="128" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="450" y="143" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">passo ignorado</text>
  <path d="M514 54 C548 54 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <path d="M514 138 C548 138 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="606" y="100" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">seguinte</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Uma condição controla o passo: cumprida → o passo é executado; não cumprida → é ignorado. Em qualquer dos casos, o fluxo de trabalho avança para o passo seguinte. As condições testam variáveis, se uma tabela tem linhas ou se um documento existe.</figcaption>
</figure>

## Adicionar e controlar condições

Para ativar e adicionar condições a um passo:
1) Localize o passo ao qual pretende adicionar uma condição
2) Clique com o botão direito do rato no passo e escolha **Editar detalhes do passo**, ou clique no ícone de engrenagem e mude para o separador **Geral**
3) Desloque-se até à secção **Verificações de condições**, na parte inferior do separador **Geral**
4) Assinale a caixa de verificação **Verificar condições antes de executar** para ativar a caixa de diálogo e adicionar condições.
5) Na secção **Verificações de condições** à esquerda, selecione o "+" para adicionar uma nova condição
6) Adicione uma condição a partir da secção com separadores à direita
7) Repita os passos 5 e 6 conforme necessário para adicionar todas as suas condições

## Ver condições na área de desenho visual

As condições de um passo são visíveis na área de desenho visual sem abrir o passo. O conector que leva a um passo condicional é **tracejado** e tem um pequeno **escudo** na ponta da seta. O tracejado é o que se lê quando o zoom está reduzido ao ponto de o escudo ser demasiado pequeno para se distinguir.

Clique no escudo para abrir o passo com as suas **Verificações de condições** já visíveis. Também pode clicar com o botão direito do rato no conector e escolher **Editar condições…**, o que faz o mesmo. O escudo no próprio mosaico do passo, no canto inferior esquerdo, continua a marcar o passo como condicional, como sempre fez.

Há dois casos em que não aparece escudo numa seta, por conceção:

- **Um passo sem conector de entrada.** Um passo condicionado por uma data ou uma variável pode estar no início de um fluxo de trabalho sem nada que conduza até ele. Não há seta para marcar, pelo que só aparece o escudo do mosaico.
- **Um passo dentro de um grupo recolhido.** O seu mosaico está integrado no do grupo e a seta fixa-se no grupo e não no passo, pelo que marcá-lo atribuiria a condição à coisa errada.

Um passo com vários conectores de entrada tem um escudo, e não um por seta.

:::note
Abrir as condições desta forma leva às verificações de condições para os tipos de passo que utilizam o formulário de passo nativo. Um tipo de passo que ainda abre a janela de configuração mais antiga abre-a no topo: as condições lá estão, apenas não estão visíveis de imediato.
:::

### O que o escudo diz que verifica

A descrição do escudo lista o que o passo realmente verifica, em vez de apenas indicar
que verifica alguma coisa:

```
Table Row Count (sales_2026) > 0 where region = 'EU'
Day of Week = Monday (UTC+2)
Project Variable (run_mode) = "full"
```

São listadas até três verificações, seguidas de uma contagem das restantes (*…and 2 more checks*), para
que a lista se mantenha legível num passo com muitas condições. O mesmo resumo aparece no
escudo do próprio mosaico do passo, que é o único que um passo sem conector de entrada tem.

Ao selecionar o passo, a mesma lista surge na secção **Condições** do painel
Inspetor, que é o local mais fácil para ler uma lista longa.

Algumas coisas a esperar quanto à redação:

- **As verificações de dia e de mês aparecem como nomes**, e não como os números guardados para eles:
  *Dia da semana = Monday*, e não *Dia da semana = 3*.
- **O fuso horário só aparece quando não é UTC**, como em *(UTC+2)* acima.
- **É apresentado um filtro numa verificação de tabela** após `where`, abreviado se for longo.
- **Uma comparação agregada di-lo** — *Valor da consulta (aggregated sales_2026.amount) >=
  100* compara um total na tabela, enquanto *Valor da consulta (sales_2026.amount) >= 100*
  compara o valor de uma única linha.
- **Uma verificação de documento mostra o caminho mas não a conta.** Duas condições que verificam o
  mesmo caminho em contas de Document diferentes aparecem de forma idêntica; abra o passo para as
  distinguir.
- **Uma tabela escolhida no navegador em árvore mostra o seu nome** quando o fluxo de trabalho lê ou
  escreve essa tabela nalgum ponto. Se não o fizer, a verificação é listada sem o nome da tabela
  em vez de com um identificador interno.


### O que a condição lhe custaria

Passe o rato sobre o escudo sem clicar e a área de desenho contorna o passo condicional e tudo o que lhe é posterior com um realce tracejado: os passos que não seriam executados se essa condição bloqueasse. Nada muda; afaste o ponteiro e o realce desaparece. Os passos *anteriores* nunca são realçados: são executados em qualquer dos casos.

Esta é a mesma pré-visualização que o indicador **desativado** de um grupo desativado lhe dá, com uma diferença de redação que importa. Um grupo desativado está realmente desligado, pelo que o seu indicador diz quantos passos *serão* ignorados. Uma condição só é avaliada quando a execução lá chega, pelo que o escudo diz quantos passos *não seriam* executados **se** a condição bloquear. Pode muito bem deixar passar tudo.

### O que o escudo diz sobre a última execução

O escudo também indica o que aconteceu na execução mais recente, para que possa seguir um fluxo já terminado e ver onde parou:

| Escudo | Significado |
| --- | --- |
| Escudo simples | O passo é condicional. Ou ainda não foi executado, ou está a ser executado agora. |
| Escudo com um **+** | O passo foi executado na última execução. |
| Escudo com um **−** | O passo não foi executado na última execução. |

Os três distinguem-se pela forma e não pela cor, e a descrição do escudo explica o estado por palavras. É atualizado em direto enquanto um fluxo de trabalho está em execução, pelo que não precisa de recarregar a área de desenho para ver uma execução chegar a uma condição.

:::caution
Um escudo com um **−** diz-lhe que o passo não foi executado. Não lhe diz *porquê*, e não deve lê-lo como "a condição bloqueou-o". Um passo também é registado como não executado quando está desativado, quando o seu grupo está desativado, quando um passo anterior falhou ou quando ficou fora do âmbito de uma execução parcial. O botão **Ver registos** da barra de ferramentas abre o [registo de execução](/pt-pt/guides/workflows/viewing-workflow-log/), que indica o motivo de cada passo que ignorou. Um passo retido num ponto de interrupção é o único caso deliberadamente excluído: mantém o escudo simples, porque a pausa aí foi uma decisão sua e não um resultado da execução.
:::


## Gerir condições

Pode adicionar tantas condições quantas as necessárias na secção **Verificações de condições**.  À medida que as adiciona, convém dar-lhes um nome útil para as poder encontrar facilmente no futuro.

Depois de adicionar uma condição, selecione-a à esquerda e os critérios de avaliação da condição ficam editáveis à direita.

Para mudar o nome de uma condição, selecione-a e edite o campo **Nome** na parte superior do painel Configuração à direita, ou faça duplo clique na condição na lista. Também pode clicar com o botão direito do rato numa condição para **Mudar o nome** e **Eliminar**; **Eliminar** também está disponível no botão "−" acima da lista.

Uma condição sem tipo de condição selecionado (uma herdada de um fluxo de trabalho mais antigo ou importado, por exemplo) não pode ser avaliada. É tratada como não cumprida, pelo que o passo é ignorado, e a mensagem do passo indica que a condição não diz o que verificar. Abra a condição e escolha o que deve verificar.


## Condições de variáveis

Ao verificar condições de variáveis, a secção **Value Check Parameters** tem de ser preenchida para que possa ser feita uma comparação.

Em **Variable or Table Field**, preencha o nome da variável.  Selecione um tipo de comparação e introduza um valor de comparação.


## Condições básicas de tabelas

Se a condição verifica se uma tabela tem linhas ou está vazia, também terá de definir a tabela no separador **Seleção de dados da tabela**.


## Condições de existência de tabelas

Uma condição de existência de tabela executa o passo apenas quando a tabela foi criada no warehouse, ou apenas quando não foi. Nunca lê as linhas da tabela, e uma tabela escrita com zero linhas existe. Um nome de tabela que não corresponda a nenhuma tabela do projeto conta como inexistente. Utilize-a para construir uma tabela na primeira execução e deixá-la em paz depois, ou para ignorar um passo que lê uma tabela que um passo anterior pode não ter criado.

Os dois tipos de verificação são `radio_table_exists` e `radio_table_not_exists`. Escolha a tabela da mesma forma que numa condição básica de tabela. Defina a condição com um assistente de IA ou com a API REST; o separador **Verificações de condições** ainda não a lista.

## Condições avançadas de tabelas

Ao utilizar condições avançadas de tabelas, a secção **Value Check Parameters** tem de ser preenchida para que possa ser feita uma comparação.

Em **Variable or Table Field**, preencha o nome do campo a partir da seleção da tabela.  Selecione um tipo de comparação e introduza um valor de comparação.

No separador **Seleção de dados da tabela**, selecione a tabela e preencha a secção de mapeamento de dados com, pelo menos, o campo referenciado para a comparação da condição.

## Condições de caminho de documento

Se a condição verifica se um ficheiro existe, é necessário escolher a conta de documentos e especificar o caminho do documento a verificar no separador **Caminho do documento**. Uma pasta nesse caminho conta como inexistente, porque a verificação é de um ficheiro.

## Condições de data e hora

Para seleções de data ou hora, pode adicionar várias condições se for necessária uma combinação de condições.  Por exemplo, se pretendesse que um passo só fosse executado às segundas-feiras às 2:05, criaria três condições:
 - Condição de dia da semana definida como segunda-feira (1)
 - Hora do dia definida como 2
 - Minuto da hora definido como 5

### Desvio do fuso horário

Cada condição de data e hora tem o seu próprio **Desvio do fuso horário**, listado como um desvio de horas inteiras com o nome de uma zona representativa, por exemplo *Eastern Time (US & Canada) (UTC -5)* ou *Asia/Tokyo (UTC +9)*. As horas que introduzir são comparadas com o relógio dessa zona.

Uma nova condição começa com o desvio que o seu navegador indica, pelo que na maioria dos casos pode deixá-lo como está. Defina-o deliberadamente quando o horário pertencer a um local diferente de onde se encontra, por exemplo um fecho que decorre segundo o relógio da equipa financeira. Só estão disponíveis horas inteiras, pelo que um fuso de meia hora, como a Índia (UTC +5:30), tem de ser arredondado para a hora inteira mais próxima.

Uma condição guardada antes de esta definição entrar em vigor continua a ser avaliada em UTC até escolher uma zona para ela, pelo que as condições existentes continuam a comportar-se exatamente como antes.

:::caution
As condições de **Day of the week** comparam atualmente com UTC, qualquer que seja o desvio escolhido. Se precisar de que uma condição de dia da semana coincida com um dia específico num fuso muito afastado de UTC, tenha em atenção que pode diferir do seu dia local durante várias horas de cada lado da meia-noite.
:::

### Dia útil do fecho financeiro

Para **Utilizar dia útil do fecho financeiro**, a contagem começa em **0 para o dia 1 do mês**, tal como indica a sugestão junto ao campo. Assim, um fecho que ocorre no 5.º dia do mês é `4`, e não `5`.

:::caution
Esta condição nunca corresponde atualmente, pelo que um passo protegido por uma não será executado. Utilize uma condição **Day of the month** até isto ser resolvido. Os valores negativos, destinados a contar a partir do fim do mês, também não funcionam.
:::

## Definir condições com um assistente de IA

Um assistente de IA ligado à sua área de trabalho pode adicionar e alterar as condições de um passo por si, quer esteja a criar o passo quer a editar um que já tenha. Todos os tipos de condição descritos anteriormente estão disponíveis, exceto **Verificar fecho financeiro do Workday**: um assistente pode escrever essa, mas nunca corresponde, pelo que o assistente avisa-o em vez de a deixar passar despercebida. Defina essa no separador **Condições** por si.

Há três aspetos que funcionam de forma diferente da edição manual de condições:

- **A lista inteira é substituída de cada vez.** Peça para adicionar ou alterar uma condição e o assistente envia a lista completa, pelo que qualquer condição que omita é removida. Se não tiver a certeza de que as tem todas, peça-lhe que liste as condições atuais do passo antes de escrever.
- **Uma condição que não pode ser avaliada é recusada.** Uma condição que não diz o que verifica é rejeitada em vez de guardada, e o passo mantém as condições que já tinha. Corrija o pedido e peça novamente.
- **Uma condição incompleta é guardada, com um aviso.** Uma condição sem o valor com que comparar, ou condições adicionadas sem **Verificar condições antes de executar** assinalado, são armazenadas e comunicadas de volta como aviso. Abra o separador **Condições** e conclua-as, ou o passo não se comporta como pediu.

Um assistente também pode definir o bloqueio do passo, a sua visibilidade nas vistas Gestor e Explorador, as suas definições de repetição e o passo para onde ir em caso de erro.
