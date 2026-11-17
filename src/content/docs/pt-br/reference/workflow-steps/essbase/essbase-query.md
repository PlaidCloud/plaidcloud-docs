---
title: "Essbase: Consultar cubo"
description: Execute uma consulta MDX ao vivo em um cubo do Oracle Essbase e grave a grade de resultado em uma tabela do fluxo de trabalho, com colunas derivadas da grade e acesso a linhas aplicado ao resultado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-query.md
---

## Descrição

A etapa **Essbase: Consultar cubo** executa um `SELECT` MDX em um cubo do Oracle Essbase e grava a grade retornada em uma tabela de destino. É uma **consulta ao vivo de verdade**: a etapa envia o MDX e lê a grade resultante de forma síncrona, de modo que cada execução reflete os números atuais do cubo. Não é uma extração nem um polling: não há trabalho de preparação a aguardar nem instantâneo que fique desatualizado entre execuções.

Use-a para trazer uma fatia específica de um cubo (um conjunto de contas por período, uma comparação de cenários, um conjunto de direcionadores para uma alocação) para uma tabela do PlaidCloud que você pode então transformar, juntar ou usar em relatórios junto com o restante dos seus dados.

## Pré-requisitos

- Uma [conexão do Oracle Essbase](/pt-br/reference/connectors/erp/oracle-essbase/) apontando para o Essbase 21c+ ou o Oracle Analytics Cloud (OAC), com uma conta de serviço que possa ler o aplicativo e o cubo que você quer consultar.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 120" role="img" aria-label="Fluxo de uma conexão Essbase, passando pelo aplicativo e pelo cubo escolhidos, uma consulta MDX e a grade retornada, até uma tabela de destino." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="eq-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="70" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Conexão</text>
<rect x="176" y="42" width="130" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="241" y="63" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Aplicativo</text><text x="241" y="78" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">/ Cubo</text>
<rect x="352" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="412" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">MDX SELECT</text>
<rect x="518" y="42" width="80" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="558" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Grade</text>
<rect x="632" y="42" width="80" height="42" rx="8" fill="var(--sl-color-accent)" stroke="var(--sl-color-accent)" /><text x="672" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Tabela</text>
<path d="M130 63 L172 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M306 63 L348 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M472 63 L514 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M598 63 L628 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">O MDX é executado ao vivo no cubo; a grade retornada vai para a tabela de destino com colunas derivadas da própria grade.</figcaption>
</figure>

## Configuração

- **Conexão** — uma conexão do Oracle Essbase. O atalho de edição ao lado do seletor abre o editor de conexão para visualizar ou editar.
- **Aplicativo** — o aplicativo Essbase a consultar. O seletor lista os aplicativos que a conta de serviço da conexão consegue ver; se a conexão define um aplicativo padrão, ele já vem selecionado.
- **Cubo (banco de dados)** — o cubo, dentro do aplicativo escolhido, em que a consulta será executada.
- **MDX** — a instrução `SELECT` MDX a executar. Monte-a com a seleção guiada de membros ou escreva-a diretamente (veja abaixo).
- **Tabela de destino** — a tabela em que a grade retornada é gravada.

## Montando a consulta

Você pode produzir o MDX de duas maneiras:

- **Seleção guiada de membros.** Navegue pelas dimensões e membros do cubo e escolha o que vai nas colunas e nas linhas; a etapa monta o MDX para você. Os membros são carregados um nível por vez à medida que você os expande, para que um esboço grande continue responsivo.
- **MDX bruto.** Escreva ou cole um `SELECT` MDX diretamente: a saída para tudo o que o seletor guiado não cobre, como membros calculados, funções ou operadores de conjunto.

Os dois caminhos produzem o mesmo valor `MDX` que a etapa executa; o seletor guiado é um ponto de partida que você sempre pode editar manualmente.

## Opções

| Campo | Padrão | Observações |
|---|---|---|
| Suprimir células #Missing | Desativado | No servidor: descarta `#Missing` e outras células estruturalmente irrelevantes antes que trafeguem pela rede. É seguro: nunca descarta um zero lançado. |
| Suprimir também células zero (com perdas) | Desativado | Um filtro separado e opcional que também descarta qualquer célula cujo valor já seja exatamente `0`, depois que ela é buscada. **Com perdas**: um zero lançado é um fato real em um cubo de planejamento, não ausência de dados; ative somente se quiser especificamente excluir zeros do resultado. |
| Limite de linhas | 250.000 | Limita o número de linhas retornadas. Deixe em branco para usar o limite padrão de 250.000; aumente ou diminua explicitamente. Uma consulta que excede o limite é recusada em vez de truncada silenciosamente: restrinja a consulta (adicione um slicer, `NON EMPTY` ou um conjunto de membros mais restrito) ou aumente o Limite de linhas e tente novamente. |

## Pré-visualização

Antes de salvar, **Pré-visualização** executa o MDX atual no cubo e mostra as colunas retornadas e as primeiras linhas, uma verificação rápida de que a consulta tem o formato esperado, independentemente do Limite de linhas configurado na própria etapa.

## Resultados e esquema na leitura

A grade que o Essbase retorna é gravada na tabela de destino com suas **colunas derivadas da grade retornada** (schema-on-read). Você não declara uma lista de colunas antecipadamente:

- Os nomes das colunas vêm das linhas de cabeçalho da grade. Uma célula de cabeçalho que não abrange nada (o canto acima dos rótulos de linha) vira `column_1`, `column_2` e assim por diante; nomes duplicados se tornam exclusivos com um sufixo numérico.
- Uma coluna cujas células de dados são todas numéricas recebe tipo numérico; qualquer outra recebe tipo texto. Células vazias do Essbase chegam como nulos.
- Os rótulos de membros e de aliases na grade vêm da tabela de aliases configurada na conexão, aplicada de forma consistente em toda execução, e não do padrão por sessão do próprio Essbase, que poderia mostrar rótulos diferentes dependendo de quem estava conectado quando a consulta foi executada.

Como o formato acompanha a consulta, alterar o que o MDX coloca nas colunas muda as colunas da tabela na próxima execução; tenha isso em mente para as etapas seguintes que referenciam nomes de colunas específicos.

## Acesso a linhas

A [segurança em nível de linha](/pt-br/administration/access/managing-security-groups-and-assignments/#gerenciar-o-acesso-a-linhas) se aplica à tabela gravada exatamente como a qualquer outra tabela do PlaidCloud. A governança é imposta sobre o resultado que a etapa grava, de modo que um leitor com restrição de linhas vê apenas as linhas que seu grupo de segurança permite: a consulta é executada com a conta de serviço da conexão, mas a tabela que ela produz é governada como o restante dos seus dados.

## Exemplo

Este MDX coloca duas medidas nas colunas e dois produtos nas linhas:

```mdx
SELECT
  {Sales, COGS} ON COLUMNS,
  {[100-10], [200-10]} ON ROWS
FROM Sample.Basic
```

Executá-lo em um cubo que retorna esses quatro números grava uma tabela como esta:

| column_1 | Sales | COGS |
|---|---|---|
| 100-10 | 678.0 | 271.0 |
| 200-10 | 551.0 | 235.0 |

A coluna de rótulos de linha não tem cabeçalho na grade, então vira `column_1` (texto); `Sales` e `COGS` são totalmente numéricas e chegam como colunas numéricas.

## Relacionados

- [Conectar-se ao Oracle Essbase (guia)](/pt-br/guides/connections/essbase/) — crie a conexão e monte uma consulta.
- [Conector do Oracle Essbase](/pt-br/reference/connectors/erp/oracle-essbase/) — referência dos campos da conexão.
- [Essbase: Ler dimensão](/pt-br/reference/workflow-steps/essbase/essbase-dimension-read/) — carrega o esboço de uma dimensão do Essbase em uma dimensão do PlaidCloud, diretamente na nuvem.
- [Etapas do Oracle Essbase](/pt-br/reference/workflow-steps/essbase/)
- [Solicitação REST](/pt-br/reference/workflow-steps/general/rest-request/) — a etapa de uso geral para outras solicitações HTTP ao vivo.
