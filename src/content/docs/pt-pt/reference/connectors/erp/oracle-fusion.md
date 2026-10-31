---
title: Conector Oracle Fusion
description: Configure uma ligação ao Oracle Fusion Cloud no PlaidCloud com credenciais OAuth2 para importar saldos do razão geral e lotes de lançamentos de diário através de OData/BIP, e registar lançamentos de diário através de FBDI.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-fusion.md
---

## Documentação da API

As referências da [API REST (OData)](https://docs.oracle.com/en/cloud/saas/financials/) e do [BI Publisher (BIP) e File-Based Data Import (FBDI)](https://docs.oracle.com/en/cloud/saas/applications-common/) do Oracle Fusion Cloud documentam os pontos finais e o caminho de extração/carregamento em massa que este conector utiliza.

## Como funciona a autenticação

A ligação autentica-se com credenciais de cliente OAuth2 (ou com as credenciais de API de autenticação básica que a configuração de segurança do seu Fusion Cloud emite para utilizadores de integração) num utilizador de API dedicado. A função do utilizador de API controla quer as entidades do razão geral que este pode ler, quer as funções FBDI/GL Interface através das quais pode registar lançamentos.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| URL da instância | Texto | O URL da sua instância do Fusion Cloud, por exemplo `https://yourorg.fa.us2.oraclecloud.com`. |
| ID do cliente | Texto | O ID de cliente OAuth2 do utilizador de API (ou o nome de utilizador, na autenticação básica). |
| Segredo do cliente | Texto | O segredo de cliente OAuth2 do utilizador de API (ou a palavra-passe, na autenticação básica). Guardado de forma encriptada. |

## Entidades disponíveis para importação

Dois passos de importação cobrem dimensões de extração diferentes, ambos sobre `gl_balances` e `journal_batches`:

- **Import Fusion Entity**: uma chamada OData/BIP direta, para uma extração de rotina e limitada.
- **Import Fusion Bulk Extract**: uma tarefa de exportação FBDI/BIP assíncrona, para uma extração de grande dimensão.

Ambos suportam filtros de intervalo (`ge`/`le`) em campos de data, de período contabilístico e de saldo/montante numérico, bem como filtros de igualdade em campos discretos como o razão ou a moeda. Consulte [Import Fusion Entity](/pt-pt/reference/workflow-steps/oracle-fusion/import-fusion-entity/) e [Import Fusion Bulk Extract](/pt-pt/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) para obter a referência completa dos campos.

## Registo de lançamentos de diário

O passo **Oracle Fusion: Post Journal Entry** regista lotes de lançamentos de diário do razão geral através do pipeline de escrita ERP partilhado do PlaidCloud: escreve o lote na tabela de preparação GL_INTERFACE da Oracle como um ficheiro FBDI, submete e consulta a tarefa ESS Journal Import Launcher até um estado terminal, e confirma antes de comunicar que um lote foi registado. Uma correção regista um novo lançamento de estorno, com débito/crédito trocados, em vez de editar o original. Consulte [Oracle Fusion: Post Journal Entry](/pt-pt/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) para obter a referência dos campos e [Ligar ao Oracle Fusion](/pt-pt/guides/connections/oracle-fusion/) para o guia completo de registo.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| Latência da tarefa ESS | O Journal Import Launcher é executado como uma tarefa agendada, não como uma chamada síncrona: uma execução de registo demora bastante mais do que uma escrita direta pela API. |
| Latência da extração em massa | O `import_fusion_bulk_extract` aguarda por uma tarefa de exportação FBDI/BIP: reserve-o para extrações demasiado grandes para o caminho direto do `import_fusion_entity`. |
## Relacionado

- [Ligar ao Oracle Fusion (guia)](/pt-pt/guides/connections/oracle-fusion/): passo a passo para criar a ligação, testá-la, importar uma entidade e registar um lançamento de diário.
- [Import Fusion Entity](/pt-pt/reference/workflow-steps/oracle-fusion/import-fusion-entity/)
- [Import Fusion Bulk Extract](/pt-pt/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/)
- [Oracle Fusion: Post Journal Entry](/pt-pt/reference/workflow-steps/oracle-fusion/oracle-fusion-post/)
- [Rever o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
