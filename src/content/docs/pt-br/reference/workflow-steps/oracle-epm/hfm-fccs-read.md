---
title: "HFM/FCCS: Ler dados (ad hoc)"
description: "Obtenha por conta própria uma fatia de dados do Oracle FCCS montando um ponto de vista no formulário da etapa: a grade retornada chega automaticamente como uma tabela, extrações repetidas ficam em cache, a coluna Entity está pronta para segurança em nível de linha e um destino vinculado opcional a transforma em uma carga recorrente agendada."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/hfm-fccs-read.md
---

## Descrição

Lê uma fatia de dados ad hoc do Oracle **FCCS** (Financial Consolidation and Close, EPM Cloud) por meio da sua [conexão HFM/FCCS](/pt-br/guides/connections/hfm-fccs/), por **ponto de vista (POV)** em vez de escrever uma consulta. Um usuário de finanças escolhe um aplicativo, monta um POV a partir das dimensões do FCCS e executa a etapa; a grade retornada chega automaticamente como uma tabela de projeto (schema-on-read: a tabela é criada a partir das colunas da grade). Parece uma consulta ao vivo, mas, por baixo, a etapa envia um job de exportação ao FCCS, **consulta** seu andamento até a conclusão e então busca e grava o resultado, de modo que uma fatia demorada não bloqueia nada e não exige um chamado para a equipe do HFM.

Esta etapa aparece no menu de etapas em **Oracle EPM (HFM/FCCS)**.

:::note[Delimite a dimensão de entidade]
Mantenha a seleção de **Entidade** limitada: uma extração sem delimitação pode bloquear o aplicativo FCCS por muito tempo enquanto o job de exportação é executado.
:::

## Configuração

### Origem e destino

| Campo | Obrigatório | Observações |
|---|---|---|
| Conexão HFM/FCCS | Sim | A [conexão HFM/FCCS](/pt-br/guides/connections/hfm-fccs/) pela qual ler. |
| Ambiente | Sim | O ambiente da conexão. |
| Aplicativo | Sim | O aplicativo FCCS do qual ler. Usa por padrão o Aplicativo padrão da conexão, se houver um definido. Escolher o aplicativo aciona a descoberta ao vivo de membros para o POV. |
| Tabela de destino | Sim | A tabela de projeto na qual a grade retornada chega. |

### Ponto de vista

Monte a fatia a partir das dimensões do FCCS. Nos pods compatíveis, as listas de membros são preenchidas automaticamente pela descoberta ao vivo de metadados depois que uma conexão e um aplicativo são escolhidos; em pods mais antigos, você digita os nomes dos membros manualmente.

| Dimensão | Obrigatória | Observações |
|---|---|---|
| Cenário | Sim | |
| Ano | Sim | |
| Período | Sim | |
| Entidade | Delimitada | Deve indicar uma fatia delimitada: o formulário rejeita uma seleção vazia, "all" ou uma seleção com mais de 500 membros. Mantenha-a delimitada para que a exportação não bloqueie o aplicativo. |
| Conta | Não | |
| Custom1–Custom4 | Não | As dimensões personalizadas do aplicativo. |
| ICP | Não | Intercompany. |
| Visão | Não | |
| Valor | Não | |

Uma dimensão opcional não definida não aplica nenhum filtro nesse eixo (o membro padrão do FCCS é usado).

### Destino vinculado

Desativado por padrão: cada execução traz uma fatia ad hoc que sobrescreve a tabela de destino.

| Campo | Observações |
|---|---|
| Destino vinculado (carga recorrente agendada) | Quando marcado, o destino passa a ser uma tabela **persistente**: a etapa mescla os dados nela com um upsert por conjunto de chaves em vez de sobrescrevê-la, e o esquema cresce de forma aditiva quando uma grade posterior traz novas colunas (uma nova coluna gera um aviso, nunca uma falha). Colocar a etapa em um fluxo de trabalho agendado gera então uma carga recorrente que acumula em vez de apagar. |
| Colunas-chave | Habilitado somente com o destino vinculado ativado. Colunas separadas por vírgula que formam a chave de mesclagem (por exemplo `Entity, Account`). **Deixe vazio** para usar como chave de mesclagem as colunas de dimensão do POV presentes na grade carregada. |

## Como funciona

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 130" role="img" aria-label="A etapa envia um job de exportação ao FCCS, consulta seu andamento até a conclusão, busca a grade e a grava como uma tabela; um ponto de vista repetido é atendido a partir da tabela em cache." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="hf-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="58" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Enviar job</text>
<rect x="150" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="198" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Consultar</text>
<rect x="290" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="338" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Buscar grade</text>
<rect x="430" y="46" width="120" height="40" rx="7" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" /><text x="490" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Gravar tabela</text>
<path d="M106 66 L150 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M246 66 L290 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M386 66 L430 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<text x="198" y="34" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">enquanto executa…</text>
<rect x="590" y="46" width="120" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="650" y="64" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">POV repetido</text><text x="650" y="78" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">atendido pelo cache</text>
<path d="M550 82 C570 100 630 100 650 88" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="4 3" marker-end="url(#hf-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Uma execução envia um job de exportação, consulta seu andamento, busca a grade e grava uma tabela. O mesmo ponto de vista solicitado novamente é atendido a partir da cópia já gravada.</figcaption>
</figure>

Enquanto o job é executado, a etapa mostra um status de consulta. Quando os dados chegam, a tabela é criada a partir das colunas da grade, sem esquema para definir antes.

## Cache

O mesmo POV solicitado novamente é **atendido a partir da tabela já gravada**, instantaneamente, em vez de reenviar a exportação ao FCCS. Uma execução é identificada pelo aplicativo, pela tabela de destino, pelo ponto de vista e por uma marca **as-of** (padrão `latest`); uma repetição que corresponda a uma fatia já gravada informa que a tabela foi mantida como estava, em vez de regravá-la. Altere a marca as-of quando quiser forçar uma nova extração do mesmo POV.

## Segurança em nível de linha

O eixo de entidade da grade gravada é normalizado para uma coluna chamada exatamente **`Entity`**, de modo que a tabela fica **pronta para segurança em nível de linha**: um administrador pode governá-la com o [Acesso a linhas](/pt-br/administration/access/managing-security-groups-and-assignments/) para que os usuários de autoatendimento vejam apenas as entidades às quais têm direito.

Isso é **governado sob controle do administrador, não é automático**. Como a extração é executada sob a conta de serviço da conexão, o PlaidCloud não permite que a etapa declare sua própria segurança. Um administrador segue o fluxo padrão de Acesso a linhas:

1. **Publicar** a tabela gravada para relatórios.
2. **Declarar** a coluna `Entity` como um atributo de governança (negação por padrão).
3. **Aprovar** a primeira gravação governada.
4. **Reconciliar** para que as concessões entrem em vigor.

Até que um administrador faça isso, a tabela não é filtrada. Consulte [Gerenciar grupos de segurança e atribuições](/pt-br/administration/access/managing-security-groups-and-assignments/).

## Limites de capacidade

| Limitação | O que significa |
|---|---|
| Somente leitura | Extrai uma fatia do FCCS. Não grava dados de consolidação, não executa consolidações nem lança de volta. |
| Entidade delimitada obrigatória | O formulário rejeita uma seleção de entidade vazia, "all" ou com mais de 500 membros, e um único membro agregado ainda pode se expandir no lado do servidor; mantenha a fatia delimitada. |
| Membros manuais em pods mais antigos | Quando um pod não expõe o endpoint de metadados, as listas de membros não são preenchidas automaticamente; digite os nomes dos membros manualmente. |
| A segurança em nível de linha é governada pelo administrador | A coluna `Entity` está pronta para RLS, mas um administrador precisa publicar, declarar, aprovar a primeira gravação e reconciliar antes que a tabela seja filtrada. |

## Relacionados

- [Extrair do HFM / FCCS (guia)](/pt-br/guides/connections/hfm-fccs/): o passo a passo completo.
- [Conector HFM / FCCS](/pt-br/reference/connectors/rest/hfm-fccs/): referência dos campos da conexão.
- [Etapas do Oracle EPM (HFM / FCCS)](/pt-br/reference/workflow-steps/oracle-epm/)
- [Gerenciar grupos de segurança e atribuições](/pt-br/administration/access/managing-security-groups-and-assignments/)
