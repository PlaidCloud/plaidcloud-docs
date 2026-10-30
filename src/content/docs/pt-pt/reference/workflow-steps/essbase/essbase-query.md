---
title: "Essbase: Consultar cubo"
description: Execute uma consulta MDX em direto sobre um cubo Oracle Essbase e coloque a grelha de resultados numa tabela do fluxo de trabalho, com colunas derivadas da grelha e acesso a linhas aplicado ao resultado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-query.md
---

## Descrição

O passo **Essbase: Consultar cubo** executa um `SELECT` MDX sobre um cubo Oracle Essbase e escreve a grelha devolvida numa tabela de destino. É uma **verdadeira consulta em direto** — o passo envia o MDX e lê a grelha resultante de forma síncrona, pelo que cada execução reflete os números atuais do cubo. Não é uma extração nem uma sondagem: não há nenhuma tarefa intermédia a aguardar nem instantâneo que fique desatualizado entre execuções.

Utilize-o para obter uma fatia específica de um cubo — um conjunto de contas por período, uma comparação de cenários, um conjunto de indutores para uma alocação — para uma tabela PlaidCloud que depois pode transformar, juntar ou usar em relatórios a par do restante conjunto de dados.

## Pré-requisitos

- Uma [ligação Oracle Essbase](/pt-pt/reference/connectors/erp/oracle-essbase/) que aponte para o Essbase 21c+ ou para o Oracle Analytics Cloud (OAC), com uma conta de serviço que consiga ler a aplicação e o cubo que pretende consultar.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 120" role="img" aria-label="Fluxo desde uma ligação Essbase, passando pela aplicação e cubo escolhidos, uma consulta MDX e a grelha devolvida, até uma tabela de destino." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="eq-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="70" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Ligação</text>
<rect x="176" y="42" width="130" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="241" y="63" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Aplicação</text><text x="241" y="78" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">/ Cubo</text>
<rect x="352" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="412" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">MDX SELECT</text>
<rect x="518" y="42" width="80" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="558" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Grelha</text>
<rect x="632" y="42" width="80" height="42" rx="8" fill="var(--sl-color-accent)" stroke="var(--sl-color-accent)" /><text x="672" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Tabela</text>
<path d="M130 63 L172 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M306 63 L348 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M472 63 L514 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M598 63 L628 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">O MDX é executado em direto sobre o cubo; a grelha devolvida é colocada na tabela de destino com colunas derivadas da própria grelha.</figcaption>
</figure>

## Configuração

- **Ligação** — uma ligação Oracle Essbase. O atalho de edição junto ao seletor abre o editor de ligações para consulta ou edição.
- **Aplicação** — a aplicação Essbase a consultar. O seletor lista as aplicações que a conta de serviço da ligação consegue ver; se a ligação definir uma aplicação predefinida, esta fica pré-selecionada.
- **Cubo (base de dados)** — o cubo, dentro da aplicação escolhida, sobre o qual consultar.
- **MDX** — a instrução `SELECT` MDX a executar. Crie-a com a seleção guiada de membros ou escreva-a diretamente (ver abaixo).
- **Tabela de destino** — a tabela para onde a grelha devolvida é escrita.

## Criar a consulta

Pode produzir o MDX de duas formas:

- **Seleção guiada de membros.** Navegue pelas dimensões e membros do cubo e escolha o que vai nas colunas e nas linhas; o passo monta o MDX por si. Os membros são carregados um nível de cada vez à medida que os expande, pelo que um esboço grande continua a responder bem.
- **MDX em bruto.** Escreva ou cole diretamente um `SELECT` MDX — a saída para tudo o que o seletor guiado não abrange, como membros calculados, funções ou operadores de conjuntos.

Ambos os caminhos produzem o mesmo valor `MDX` que o passo executa; o seletor guiado é um ponto de partida que pode sempre editar manualmente.

## Opções

| Campo | Predefinição | Notas |
|---|---|---|
| Suprimir células #Missing | Desativado | No servidor: descarta células `#Missing` e outras estruturalmente irrelevantes antes de atravessarem a rede. Seguro — nunca descarta um zero lançado. |
| Suprimir também células com zero (com perdas) | Desativado | Um filtro separado e opcional que descarta também qualquer célula cujo valor já seja exatamente `0`, depois de obtida. **Com perdas**: um zero lançado é um facto real num cubo de planeamento, não ausência de dados — ative-o apenas se pretender especificamente excluir os zeros do resultado. |
| Limite de linhas | 250 000 | Limita o número de linhas devolvidas. Deixe em branco para usar o limite predefinido de 250 000; aumente-o ou reduza-o explicitamente. Uma consulta que exceda o limite é recusada em vez de truncada em silêncio — restrinja a consulta (adicione um segmentador, `NON EMPTY` ou um conjunto de membros mais restrito) ou aumente o Limite de linhas e tente novamente. |

## Pré-visualização

Antes de guardar, **Pré-visualização** executa o MDX atual sobre o cubo e mostra as colunas devolvidas e as primeiras linhas — uma verificação rápida de que a consulta tem a forma esperada, independentemente do Limite de linhas com que o próprio passo está configurado.

## Resultados e esquema na leitura

A grelha devolvida pelo Essbase é escrita na tabela de destino com as suas **colunas derivadas da grelha devolvida** — esquema na leitura. Não é preciso declarar previamente uma lista de colunas:

- Os nomes das colunas provêm das linhas de cabeçalho da grelha. Uma célula de cabeçalho que não abrange nada (o canto acima das etiquetas das linhas) passa a `column_1`, `column_2`, e assim sucessivamente; os nomes duplicados são tornados únicos com um sufixo numérico.
- Uma coluna cujas células de dados são todas numéricas é tipificada como numérica; qualquer outra é tipificada como texto. As células vazias do Essbase ficam como nulos.
- As etiquetas de membros e de alias na grelha provêm da tabela de alias configurada na ligação, aplicada de forma consistente em todas as execuções — e não da predefinição por sessão do próprio Essbase, que poderia mostrar texto de etiqueta diferente consoante quem tinha sessão iniciada quando a consulta foi executada.

Como a forma acompanha a consulta, alterar o que o MDX coloca nas colunas altera as colunas da tabela na execução seguinte — tenha isto em conta nos passos a jusante que referenciam nomes de colunas específicos.

## Acesso a linhas

A [segurança ao nível da linha](/pt-pt/administration/access/managing-security-groups-and-assignments/#gerir-o-acesso-a-linhas) aplica-se à tabela criada exatamente como a qualquer outra tabela PlaidCloud. A governação é imposta sobre o resultado que o passo escreve, pelo que um leitor com uma restrição de linhas vê apenas as linhas que o seu grupo de segurança permite — a consulta é executada com a conta de serviço da ligação, mas a tabela que produz é governada como o resto dos seus dados.

## Exemplo

Este MDX coloca duas medidas nas colunas e dois produtos nas linhas:

```mdx
SELECT
  {Sales, COGS} ON COLUMNS,
  {[100-10], [200-10]} ON ROWS
FROM Sample.Basic
```

Executá-lo sobre um cubo que devolva esses quatro números cria uma tabela como:

| column_1 | Sales | COGS |
|---|---|---|
| 100-10 | 678.0 | 271.0 |
| 200-10 | 551.0 | 235.0 |

A coluna das etiquetas das linhas não tem cabeçalho na grelha, pelo que passa a `column_1` (texto); `Sales` e `COGS` são totalmente numéricas e ficam como colunas numéricas.

## Relacionado

- [Ligar ao Oracle Essbase (guia)](/pt-pt/guides/connections/essbase/) — crie a ligação e construa uma consulta.
- [Conector Oracle Essbase](/pt-pt/reference/connectors/erp/oracle-essbase/) — referência dos campos da ligação.
- [Essbase: Ler dimensão](/pt-pt/reference/workflow-steps/essbase/essbase-dimension-read/) — carrega o esboço de uma dimensão Essbase numa dimensão PlaidCloud, diretamente na nuvem.
- [Passos Oracle Essbase](/pt-pt/reference/workflow-steps/essbase/)
- [Pedido REST](/pt-pt/reference/workflow-steps/general/rest-request/) — o passo de uso geral para outros pedidos HTTP em direto.
