---
title: "TM1: Consultar cubo"
description: Leia dados de cubo de um servidor IBM TM1 / Planning Analytics por visão salva ou MDX, aplique um recorte opcional de ponto de vista e grave o resultado como tabela — diretamente da nuvem via REST, com pré-visualização antes de salvar.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query.md
---

## Descrição

Lê dados de um cubo do IBM **TM1 / Planning Analytics** por meio da sua [conexão TM1](/pt-br/guides/connections/tm1/), executando uma **visão** salva ou uma consulta **MDX** que você escreve. Um ponto de vista (POV) pode fixar membros de dimensões adicionais além do que a visão ou o MDX já fixa. O cellset retornado é gravado como uma tabela do projeto — schema-on-read, com colunas de dimensão e uma coluna de medida `Value`, criada a partir dos próprios eixos da consulta.

Esta etapa aparece no menu de etapas em **IBM TM1 / Planning Analytics**.

A etapa acessa o TM1 **diretamente da nuvem** por meio da API REST — não há agente local envolvido, e ainda não há nenhum disponível para esta etapa.

## Configuração

### Origem e destino

| Campo | Obrigatório | Observações |
|---|---|---|
| Conexão TM1 | Sim | A [conexão TM1](/pt-br/guides/connections/tm1/) pela qual ler. |
| Ambiente | Sim | O ambiente da conexão. |
| Banco de dados | Sim | O banco de dados (instância) do TM1 a consultar. Usa por padrão o Banco de dados padrão da conexão, se houver um definido. |
| Cubo | Sim | O cubo do TM1 a consultar. Descoberto ao vivo a partir do banco de dados conectado, ou digitado manualmente. |
| Tabela de destino | Sim | A tabela do projeto em que o cellset retornado é gravado. |

### Recorte

| Campo | Obrigatório | Observações |
|---|---|---|
| Modo de origem | Sim | `By View` (padrão) executa uma visão salva do TM1. `By MDX` executa uma consulta MDX bruta que você escreve. |
| Visão | Com By View | A visão salva do cubo do TM1 a executar. Descoberta ao vivo depois que um cubo é escolhido, ou digitada manualmente. |
| MDX | Com By MDX | A consulta MDX a executar no cubo. |

### Ponto de vista

Fixe um membro por dimensão para delimitar o recorte além do que a visão ou o MDX já fixa — útil para uma extração incremental (veja abaixo). Adicione uma linha de dimensão, escolha a dimensão e digite o membro. O valor de um membro pode ser um literal (`Jan-2026`) ou um token `{variable}` resolvido em tempo de execução a partir das variáveis do próprio fluxo de trabalho, a mesma substituição que o próprio campo MDX recebe. Deixe o ponto de vista vazio para uma leitura simples de visão ou MDX. Aplicar um ponto de vista junto com `By View` não é compatível — use `By MDX` se precisar de um.

### Opções

| Campo | Padrão | Observações |
|---|---|---|
| Suprimir células zeradas/vazias | Desativado | Descarta as células cujo valor é exatamente o numérico `0` **depois** de buscadas. Não economiza largura de banda e, em um cubo de planejamento em que um `0` lançado é um fato real, o descarta. Prefira suprimir os zeros na própria consulta — `NON EMPTY` no MDX, ou a configuração de supressão da própria visão salva — para que o TM1 nunca os calcule. |
| Limite de linhas | 250.000 | Limita o número de células retornadas. Deixe em branco para usar o limite padrão de 250.000; aumente ou diminua explicitamente — um Limite de linhas não definido não significa ilimitado. Uma consulta que excede o limite efetivo é recusada em vez de ser truncada silenciosamente. |

## Extrações incrementais

O TM1 não tem rastreamento de alterações nativo, então não existe uma chamada "traga só o que mudou desde a última vez". O padrão, em vez disso, é **recortar por período (ou versão)** a cada execução: fixe `Period` no ponto de vista em uma variável de fluxo de trabalho `{period}` em vez de um nome de membro literal, de modo que cada execução substitua o próprio período de destino e traga os dados de um período em vez do cubo inteiro. Combine isso com um fluxo de trabalho agendado e uma variável que avança a cada execução para construir um histórico incremental, um período por vez.

## Pré-visualização

Antes de salvar, **Pré-visualização** executa o recorte atual no TM1 e mostra as primeiras linhas e a contagem de células, limitadas a um pequeno número de linhas, independentemente do Limite de linhas configurado na própria etapa.

## Quando Value é gravado como texto

Uma dimensão de medidas do TM1 costuma conter elementos numéricos (`Sales`, `Cost`) junto com elementos String (`Comment`, `Status`) na mesma dimensão. Um recorte que abrange ambos grava a coluna `Value` como texto — uma coluna tem um único tipo físico, e uma única célula não numérica no recorte basta para defini-lo.

Esse é o tratamento correto: definir as células de texto como nulas perderia dados, fazer a consulta falhar bloquearia um cubo legítimo, e dividir em duas colunas faria o esquema depender dos dados retornados. O que a etapa faz, em vez disso, é avisar. Ela emite um aviso que informa a coluna, a escala e os elementos responsáveis, por exemplo:

> Column Value landed as text: 3 of 4,812 cells are non-numeric (text or boolean), and a column can only have one type. The non-numeric cells come from element Comment. Exclude that element from the slice, or query it separately, to keep this column numeric.

A **Pré-visualização** mostra o mesmo detalhe antes de você salvar, e o seletor de membros do ponto de vista marca o tipo TM1 de cada elemento (Numeric, String ou Consolidated) para que um elemento String fique visível antes de você fixá-lo. Fixar um elemento String no ponto de vista não é bloqueado — é uma forma legítima de ler uma medida de texto —, mas isso grava toda a coluna `Value` como texto, já que a medida fica no POV e não em um eixo; nesse caso, o aviso informa as contagens sem nomear um elemento, porque todos os membros nos eixos são igualmente não numéricos e nenhum deles distingue o recorte.

Para manter `Value` numérica, exclua o elemento String do recorte ou consulte separadamente as medidas de texto e as numéricas.

## Limites de capacidade

| Limitação | O que significa |
|---|---|
| Somente leitura | Lê dados de cubo do TM1. Sem write-back e sem execução de processos TI. |
| Somente direto da nuvem | Ainda não há caminho por agente PlaidLink local para esta etapa — o servidor TM1 precisa de um caminho de rede que o PlaidCloud alcance diretamente. |
| Sem rastreamento de alterações | O TM1 não expõe API de delta/alterações desde a última vez. Recorte por período ou versão a cada execução (veja Extrações incrementais acima). |
| Sem importação de dimensão/hierarquia | Esta etapa lê dados de cubo. A importação de hierarquias de dimensão do TM1 como dimensões do PlaidCloud ainda não está disponível. |

## Relacionados

- [Conectar ao TM1 (guia)](/pt-br/guides/connections/tm1/) — crie a conexão e monte uma consulta.
- [Conector TM1](/pt-br/reference/connectors/rest/tm1/) — referência dos campos de conexão.
- [Etapas do IBM TM1 / Planning Analytics](/pt-br/reference/workflow-steps/ibm-planning-analytics/)
