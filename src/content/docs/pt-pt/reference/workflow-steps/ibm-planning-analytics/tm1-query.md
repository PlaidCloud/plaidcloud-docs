---
title: "TM1: Consultar cubo"
description: Leia dados de cubo de um servidor IBM TM1 / Planning Analytics por vista guardada ou MDX, aplique opcionalmente um corte de ponto de vista e coloque o resultado numa tabela — diretamente na cloud através de REST, com pré-visualização antes de guardar.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query.md
---

## Descrição

Lê dados de um cubo IBM **TM1 / Planning Analytics** através da sua [ligação TM1](/pt-pt/guides/connections/tm1/), executando uma **vista** guardada ou escrevendo uma consulta **MDX**. Um ponto de vista (POV) pode fixar membros de dimensão adicionais para além dos que a vista ou o MDX já fixam. O conjunto de células devolvido é colocado numa tabela do projeto — com esquema na leitura, com colunas de dimensão e uma coluna de medida `Value`, criada a partir dos eixos da própria consulta.

Este passo aparece no menu de passos em **IBM TM1 / Planning Analytics**.

O passo acede ao TM1 **diretamente na cloud** através da respetiva API REST — não há nenhum agente local envolvido e, para já, nenhum está disponível para este passo.

## Configuração

### Origem e destino

| Campo | Obrigatório | Notas |
|---|---|---|
| Ligação TM1 | Sim | A [ligação TM1](/pt-pt/guides/connections/tm1/) através da qual se faz a leitura. |
| Ambiente | Sim | O ambiente da ligação. |
| Base de dados | Sim | A base de dados (instância) TM1 a consultar. Assume por predefinição a Base de dados predefinida da ligação, caso esta esteja definida. |
| Cubo | Sim | O cubo TM1 a consultar. É detetado em direto a partir da base de dados ligada ou escrito manualmente. |
| Tabela de destino | Sim | A tabela do projeto onde o conjunto de células devolvido é colocado. |

### Corte

| Campo | Obrigatório | Notas |
|---|---|---|
| Modo de origem | Sim | `By View` (predefinido) executa uma vista TM1 guardada. `By MDX` executa uma consulta MDX em bruto que o utilizador escreve. |
| Vista | Com By View | A vista de cubo TM1 guardada a executar. É detetada em direto depois de escolhido um cubo ou escrita manualmente. |
| MDX | Com By MDX | A consulta MDX a executar no cubo. |

### Ponto de vista

Fixe um membro por dimensão para limitar o corte para além do que a vista ou o MDX já fixam — útil para uma extração incremental (veja abaixo). Adicione uma linha de dimensão, escolha a dimensão e escreva o membro. O valor de um membro pode ser um literal (`Jan-2026`) ou um token `{variable}` resolvido na execução a partir das variáveis do próprio fluxo de trabalho, a mesma substituição que o próprio campo MDX recebe. Deixe o ponto de vista vazio para uma leitura simples de vista ou MDX. Aplicar um ponto de vista em conjunto com `By View` não é suportado — utilize `By MDX` se precisar de um.

### Opções

| Campo | Predefinição | Notas |
|---|---|---|
| Suprimir células com zero/vazias | Desativado | Elimina as células cujo valor é exatamente o numérico `0` **depois** de terem sido obtidas. Não poupa largura de banda e, num cubo de planeamento em que um `0` lançado é um facto real, descarta-o. Prefira suprimir os zeros na própria consulta — `NON EMPTY` no MDX ou a definição de supressão da própria vista guardada — para que o TM1 nunca os calcule. |
| Limite de linhas | 250,000 | Limita o número de células devolvidas. Deixe em branco para utilizar o limite predefinido de 250,000; aumente-o ou reduza-o explicitamente — um Limite de linhas não definido não é ilimitado. Uma consulta que exceda o limite efetivo é recusada em vez de ser truncada silenciosamente. |

## Extrações incrementais

O TM1 não tem controlo de alterações integrado, pelo que não existe uma chamada do tipo "devolve apenas o que mudou desde a última vez". O padrão é, em vez disso, **cortar por período (ou versão)** em cada execução: fixe `Period` no ponto de vista a uma variável de fluxo de trabalho `{period}` em vez de um nome de membro literal, de modo que cada execução substitua o período de destino da própria execução e obtenha os dados de um período em vez de todo o cubo. Combine isto com um fluxo de trabalho agendado e uma variável que avança a cada execução para construir um histórico incremental, um período de cada vez.

## Pré-visualização

Antes de guardar, a **Pré-visualização** executa o corte atual no TM1 e mostra as primeiras linhas e uma contagem de células, limitada a um pequeno número de linhas, independente do Limite de linhas com que o próprio passo está configurado.

## Quando o valor é colocado como texto

Uma dimensão de medidas do TM1 contém habitualmente elementos numéricos (`Sales`, `Cost`) a par de elementos String (`Comment`, `Status`) na mesma dimensão. Um corte que abranja ambos coloca a coluna `Value` como texto — uma coluna tem um único tipo físico e basta uma célula não numérica no corte para o decidir.

Este é o tratamento correto: definir as células de texto como nulas faria perder dados, falhar a consulta bloquearia um cubo legítimo e dividir em duas colunas faria o esquema depender dos dados devolvidos. O que o passo faz, em vez disso, é avisar. Emite um aviso que indica a coluna, a escala e os elementos responsáveis, por exemplo:

> Column Value landed as text: 3 of 4,812 cells are non-numeric (text or boolean), and a column can only have one type. The non-numeric cells come from element Comment. Exclude that element from the slice, or query it separately, to keep this column numeric.

A **Pré-visualização** mostra o mesmo detalhe antes de guardar, e o seletor de membros do ponto de vista assinala o tipo TM1 de cada elemento (Numeric, String ou Consolidated), para que um elemento String seja visível antes de o fixar. Fixar um elemento String no ponto de vista não é bloqueado — é uma forma legítima de ler uma medida de texto —, mas fazê-lo coloca toda a coluna `Value` como texto, uma vez que a medida está no POV e não num eixo; nesse caso, o aviso indica as contagens sem nomear um elemento, porque todos os membros nos eixos são igualmente não numéricos e nenhum deles distingue o corte.

Para manter `Value` numérico, exclua o elemento String do corte ou consulte separadamente as medidas de texto e as numéricas.

## Limitações de capacidade

| Limitação | O que significa |
|---|---|
| Só de leitura | Lê dados de cubo do TM1. Sem escrita de retorno nem execução de processos TI. |
| Apenas diretamente na cloud | Ainda não existe caminho através de um agente PlaidLink local para este passo — o servidor TM1 precisa de um caminho de rede que o PlaidCloud consiga alcançar diretamente. |
| Sem controlo de alterações | O TM1 não expõe nenhuma API de deltas/alterações desde. Em alternativa, corte por período ou versão em cada execução (veja Extrações incrementais acima). |
| Sem importação de dimensões/hierarquias | Este passo lê dados de cubo. Importar hierarquias de dimensões do TM1 como dimensões do PlaidCloud ainda não está disponível. |

## Relacionado

- [Ligar ao TM1 (guia)](/pt-pt/guides/connections/tm1/) — crie a ligação e construa uma consulta.
- [Conector TM1](/pt-pt/reference/connectors/rest/tm1/) — referência dos campos da ligação.
- [Passos do IBM TM1 / Planning Analytics](/pt-pt/reference/workflow-steps/ibm-planning-analytics/)
