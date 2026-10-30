---
title: "HFM/FCCS: Ler dados (ad hoc)"
description: Obtenha por si um segmento de dados do Oracle FCCS construindo um ponto de vista no formulário do passo — a grelha devolvida é gravada automaticamente como tabela, as obtenções repetidas ficam em cache, a coluna Entity está pronta para segurança ao nível da linha e um destino associado opcional transforma-o num carregamento recorrente agendado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/hfm-fccs-read.md
---

## Descrição

Lê um segmento de dados ad hoc do **FCCS** da Oracle (Financial Consolidation and Close, EPM Cloud), através da sua [ligação HFM/FCCS](/pt-pt/guides/connections/hfm-fccs/), por **ponto de vista (POV)** em vez de escrever uma consulta. Um utilizador de finanças escolhe uma aplicação, constrói um POV a partir das dimensões do FCCS e executa o passo; a grelha devolvida é gravada automaticamente como tabela de projeto (esquema na leitura — a tabela é criada a partir das colunas da grelha). Parece uma consulta em direto, mas, nos bastidores, o passo submete uma tarefa de exportação ao FCCS, **consulta-a periodicamente** até estar concluída e depois obtém e grava o resultado — pelo que um segmento demorado não bloqueia e não é necessário nenhum pedido à equipa do HFM.

Este passo aparece no menu de passos em **Oracle EPM (HFM/FCCS)**.

:::note[Delimite a dimensão da entidade]
Mantenha a seleção de **Entidade** limitada — uma extração sem âmbito definido pode bloquear a aplicação FCCS durante muito tempo enquanto a tarefa de exportação decorre.
:::

## Configuração

### Origem e destino

| Campo | Obrigatório | Notas |
|---|---|---|
| Ligação HFM/FCCS | Sim | A [ligação HFM/FCCS](/pt-pt/guides/connections/hfm-fccs/) através da qual ler. |
| Ambiente | Sim | O ambiente da ligação. |
| Aplicação | Sim | A aplicação FCCS de onde ler. Assume por predefinição a Aplicação predefinida da ligação, se estiver definida. Escolher a aplicação ativa a descoberta de membros em direto para o POV. |
| Tabela de destino | Sim | A tabela de projeto onde a grelha devolvida é gravada. |

### Ponto de vista

Construa o segmento a partir das dimensões do FCCS. Nos pods suportados, as listas de membros são preenchidas automaticamente a partir da descoberta de metadados em direto, depois de escolhidas uma ligação e uma aplicação; nos pods mais antigos, escreve os nomes dos membros manualmente.

| Dimensão | Obrigatório | Notas |
|---|---|---|
| Cenário | Sim | |
| Ano | Sim | |
| Período | Sim | |
| Entidade | Delimitada | Tem de indicar um segmento delimitado — o formulário rejeita uma seleção vazia, "all" ou uma seleção com mais de 500 membros. Mantenha-a delimitada para que a exportação não bloqueie a aplicação. |
| Conta | Não | |
| Custom1–Custom4 | Não | As dimensões personalizadas da aplicação. |
| ICP | Não | Intercompanhia. |
| Vista | Não | |
| Valor | Não | |

Uma dimensão opcional por definir não aplica qualquer filtro nesse eixo (é utilizado o membro predefinido do FCCS).

### Destino associado

Desativado por predefinição — cada execução grava um segmento ad hoc que substitui a tabela de destino.

| Campo | Notas |
|---|---|
| Destino associado (carregamento recorrente agendado) | Quando assinalado, o destino passa a ser uma tabela **persistente**: o passo funde os dados nela com um upsert por conjunto de chaves em vez de a substituir, e o esquema cresce de forma aditiva quando uma grelha posterior traz novas colunas (uma nova coluna gera um aviso, nunca uma falha). Colocar o passo num fluxo de trabalho agendado dá então um carregamento recorrente que acumula em vez de apagar. |
| Colunas-chave | Ativado apenas com o Destino associado ligado. Colunas separadas por vírgulas que formam a chave de fusão (por exemplo `Entity, Account`). **Deixe-o vazio** para utilizar como chave de fusão as colunas de dimensões do POV presentes na grelha gravada. |

## Como funciona

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 130" role="img" aria-label="O passo submete uma tarefa de exportação ao FCCS, consulta-a periodicamente até estar concluída, obtém a grelha e grava-a como tabela; um ponto de vista repetido é servido a partir da tabela em cache." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="hf-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="58" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Submeter tarefa</text>
<rect x="150" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="198" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Consultar</text>
<rect x="290" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="338" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Obter grelha</text>
<rect x="430" y="46" width="120" height="40" rx="7" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" /><text x="490" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Gravar tabela</text>
<path d="M106 66 L150 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M246 66 L290 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M386 66 L430 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<text x="198" y="34" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">enquanto decorre…</text>
<rect x="590" y="46" width="120" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="650" y="64" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">POV repetido</text><text x="650" y="78" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">servido a partir da cache</text>
<path d="M550 82 C570 100 630 100 650 88" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="4 3" marker-end="url(#hf-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Uma execução submete uma tarefa de exportação, consulta-a periodicamente, obtém a grelha e grava uma tabela. O mesmo ponto de vista pedido novamente é servido a partir da cópia já gravada.</figcaption>
</figure>

Enquanto a tarefa decorre, o passo mostra um estado de consulta periódica. Quando é gravada, a tabela é criada a partir das colunas da grelha — sem esquema para definir previamente.

## Cache

O mesmo POV pedido novamente é **servido a partir da tabela já gravada**, de imediato, em vez de voltar a submeter a exportação ao FCCS. Uma execução é identificada pela aplicação, pela tabela de destino, pelo ponto de vista e por uma etiqueta **as-of** (predefinição `latest`); uma repetição que resulte num segmento já gravado indica que a tabela foi deixada como estava em vez de ser reescrita. Altere a etiqueta as-of quando quiser forçar uma nova extração do mesmo POV.

## Segurança ao nível da linha

O eixo de entidade da grelha gravada é normalizado para uma coluna com o nome exato **`Entity`**, pelo que a tabela fica **pronta para segurança ao nível da linha** — um administrador pode geri-la com [Acesso a linhas](/pt-pt/administration/access/managing-security-groups-and-assignments/), para que os utilizadores autónomos vejam apenas as entidades a que têm direito.

Isto é **governado sob controlo do administrador, não é automático**. Como a extração é executada sob a conta de serviço da ligação, o PlaidCloud não deixa o passo declarar a sua própria segurança. Um administrador segue o fluxo normal de Acesso a linhas:

1. **Publicar** a tabela gravada para relatórios.
2. **Declarar** a coluna `Entity` como atributo de governação (recusa por predefinição).
3. **Aprovar** a primeira escrita governada.
4. **Reconciliar** para que as concessões entrem em vigor.

Até um administrador o fazer, a tabela não é filtrada. Consulte [Gerir grupos de segurança e atribuições](/pt-pt/administration/access/managing-security-groups-and-assignments/).

## Limites de capacidade

| Limitação | O que significa |
|---|---|
| Só de leitura | Extrai um segmento do FCCS. Não escreve dados de consolidação, não executa consolidações nem lança de volta. |
| Entidade delimitada obrigatória | O formulário rejeita uma seleção de entidades vazia, "all" ou com mais de 500 membros, e um único membro agregado ainda pode expandir-se no servidor — mantenha o segmento delimitado. |
| Membros manuais em pods mais antigos | Quando um pod não expõe o ponto de acesso de metadados, as listas de membros não são preenchidas automaticamente; introduza os nomes dos membros à mão. |
| A segurança ao nível da linha é governada pelo administrador | A coluna `Entity` está pronta para segurança ao nível da linha, mas um administrador tem de publicar, declarar, aprovar a primeira escrita e reconciliar antes de a tabela ser filtrada. |

## Relacionado

- [Extrair do HFM / FCCS (guia)](/pt-pt/guides/connections/hfm-fccs/): o tutorial completo.
- [Conector HFM / FCCS](/pt-pt/reference/connectors/rest/hfm-fccs/): referência dos campos da ligação.
- [Passos do Oracle EPM (HFM / FCCS)](/pt-pt/reference/workflow-steps/oracle-epm/)
- [Gerir grupos de segurança e atribuições](/pt-pt/administration/access/managing-security-groups-and-assignments/)
