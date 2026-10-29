---
title: Otimizar um fluxo de trabalho
description: Faça com que um fluxo de trabalho avançado seja executado mais depressa, reconstruindo as suas dependências a partir da linhagem de dados e fundindo cadeias de passos de extração, com cada fusão verificada nos seus dados antes de ser aplicada.
sidebar:
  order: 19.6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/optimize-a-workflow.md
---

A opção **Otimizar** analisa um fluxo de trabalho avançado e propõe alterações que o fazem executar mais depressa. Vê cada alteração antes de acontecer seja o que for, escolhe as que pretende e pode anular o resultado mais tarde.

A otimização funciona em fluxos de trabalho avançados (DAG). Para um fluxo de trabalho padrão, escolha primeiro **Converter para avançado...**; consulte [Fluxos de trabalho avançados](/pt-pt/guides/workflows/advanced-workflows/#escolher-o-tipo-de-fluxo-de-trabalho).

## Otimizar um fluxo de trabalho

1. Na lista **Fluxos de trabalho**, clique com o botão direito do rato num fluxo de trabalho avançado e escolha **Otimizar...**. O fluxo de trabalho não pode estar em execução nem em pausa, e é necessário ter acesso de escrita.
2. A janela **Otimizar fluxo de trabalho** mostra um resumo como *34 passos → 30 passos · 12 passos podem ser executados em paralelo*. Quando o fluxo de trabalho tem histórico de execuções, acrescenta *~11 s mais rápido por execução*.
3. Por baixo do resumo há uma linha por alteração, cada uma com uma caixa de seleção, os passos que afeta, o que significa para o fluxo de trabalho e o tempo que poupa, medido como a variação do tempo real de execução. Todas estão assinaladas; desmarque as que não pretende.
4. Uma lista **Não é possível otimizar** indica os passos que a otimização deixou intactos e o motivo específico de cada um; consulte [Porque é que um passo não pode ser otimizado](#porque-é-que-um-passo-não-pode-ser-otimizado).
5. Escolha **Aplicar N alterações**.

Se o fluxo de trabalho já não tiver nada a melhorar, a janela indica-o.

## Os dois tipos de alteração

### Reconstruir as dependências a partir da linhagem de dados

A otimização lê as tabelas que cada passo lê e escreve, e redesenha as ligações para que um passo aguarde apenas pelos passos cujas tabelas utiliza. Os passos que não partilham tabelas são executados em paralelo.

- Um passo deixa de aguardar por passos não relacionados, pelo que deixa de parar quando um passo não relacionado falha. Uma falha propaga-se ao longo das novas dependências.
- Uma execução parcial por intervalo de passos, como **Executar a partir daqui**, segue as novas dependências.
- O servidor continua a limitar quantos passos são executados em simultâneo.
- Os passos que indicam as suas tabelas por nome ou caminho são interpretados da mesma forma que os passos que utilizam ids de tabela. Um nome tem de corresponder exatamente a uma tabela do projeto; um nome que corresponda a várias tabelas, uma referência que utilize uma variável e uma tabela de outro projeto não podem ser rastreados.
- Um passo desativado nunca impõe uma ordem e não conta para os passos que podem ser executados em paralelo.
- A otimização deixa esta alteração de fora enquanto um agendamento ou outro fluxo de trabalho executa um intervalo de passos deste fluxo de trabalho.

### Fundir uma cadeia de passos de extração num só

Uma cadeia de passos Extract Data, em que cada um lê a tabela escrita pelo anterior, passa a ser um único passo que lê a primeira origem e escreve o último resultado.

Cada fusão é verificada antes de ser aplicada. A otimização executa os passos originais e o passo fundido sobre os seus dados atuais em tabelas temporárias de trabalho e compara os dois resultados linha a linha. Só aplica a fusão quando são idênticos. O seu fluxo de trabalho e as suas tabelas não são tocados durante a verificação.

- Uma mudança de nome seguida de um filtro, como um passo Select seguido de um filtro, pode fundir-se num só passo.
- Quando uma cadeia inteira não pode ser fundida, a otimização propõe a maior parte dela que o pode ser.
- As tabelas a meio de uma cadeia fundida deixam de ser escritas pelo fluxo de trabalho. São mantidas, não eliminadas, e a alteração indica-as.
- Uma fusão cujos resultados difiram, ou que não possa ser verificada, não é aplicada, e os resultados explicam porquê. As fusões requerem uma tabela de origem com dados.

## Porque é que um passo não pode ser otimizado

Cada linha em **Não é possível otimizar** indica a sua própria causa:

| Causa | O que significa |
|---|---|
| Agrega | O passo resume linhas, pelo que não pode ser integrado num vizinho. |
| Dois filtros | Uma cadeia com dois filtros não pode tornar-se num só passo. |
| Filtro sobre um valor de vírgula flutuante que pode ser arredondado | A fusão poderia alterar as linhas que passam, pelo que o filtro fica onde está. |
| Um passo que executa código do utilizador | As expressões, os scripts e passos semelhantes não podem ser verificados como equivalentes. |
| Uma tabela lida por mais de um passo | A tabela a meio da cadeia é necessária noutro local. |
| Passo desativado | Um passo desativado não é fundido e não impõe uma ordem. |
| Membro de um contentor de execução | Os passos de um contentor de execução são executados como uma unidade. |
| Contagem de linhas indisponível | A contagem de linhas da tabela de origem não pode ser lida, nem sequer em direto, pelo que a fusão não pode ser dimensionada para verificação. |
| Não é possível identificar a tabela | O nome da tabela do passo não corresponde a nenhuma tabela ou corresponde a mais de uma, utiliza uma variável ou aponta para outro projeto. |
| Segurança ao nível da linha ou demasiado grande | A tabela é regida por segurança ao nível da linha ou é demasiado grande para ser verificada automaticamente. |

Os contentores visuais, que apenas agrupam passos na área de desenho, não impedem uma fusão. Quando uma fusão remove passos de um deles, o passo fundido ocupa o seu lugar e um contentor que fique vazio é descartado. Anular restaura exatamente a disposição.

## Acompanhar o progresso

Depois de aplicar, **A otimizar fluxo de trabalho** mostra a fase: *A verificar (3 de 6 execuções)...*, *A comparar resultados...* e *A aplicar...*. Quando termina, os resultados listam o que foi **Aplicado**, incluindo em quantas linhas cada fusão foi verificada, e o que ficou **Não aplicado**, com um motivo para cada caso.

Se o fluxo de trabalho tiver mudado enquanto a otimização estava a verificar, as alterações afetadas são ignoradas e a janela indica quantas. Se uma aplicação falhar, o fluxo de trabalho é restaurado para o estado anterior.

Uma execução que comece enquanto as alterações estão a ser confirmadas é adiada por momentos, não descartada.

## Anular uma otimização

Clique com o botão direito do rato no fluxo de trabalho e escolha **Anular otimização...**, ou utilize **Anular otimização** nos resultados. Confirme, e os passos, as definições e a disposição do fluxo de trabalho regressam ao estado anterior à otimização. As alterações que fez ao fluxo de trabalho desde então perdem-se.

Anular requer pontos de restauro, que não estão disponíveis em todos os tenants. Um tenant sem eles não pode aplicar uma otimização.

## Otimizar através da API e dos assistentes de IA

A otimização também está disponível através da API REST e da ferramenta `workflow_optimize` para assistentes de IA, com os mesmos passos de pré-visualização, aplicação e anulação.

## Passos seguintes

- [Fluxos de trabalho avançados](/pt-pt/guides/workflows/advanced-workflows/) — a área de desenho, as ligações e os controlos de execução
- [Controlar a execução em paralelo](/pt-pt/guides/workflows/controlling-parallel-execution/) — execute passos ao mesmo tempo
- [Executar um fluxo de trabalho](/pt-pt/guides/workflows/run-a-workflow/) — executar um fluxo de trabalho do princípio ao fim
