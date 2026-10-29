---
title: Conector Oracle Fusion
description: Configure uma conexão com o Oracle Fusion Cloud no PlaidCloud com credenciais OAuth2 para importar saldos do razão geral e lotes de lançamentos por OData/BIP e lançar lançamentos contábeis por FBDI.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-fusion.md
---

## Documentação da API

As referências da [API REST (OData)](https://docs.oracle.com/en/cloud/saas/financials/) e do [BI Publisher (BIP) e File-Based Data Import (FBDI)](https://docs.oracle.com/en/cloud/saas/applications-common/) do Oracle Fusion Cloud documentam os endpoints e o caminho de extração e carga em massa que este conector usa.

## Como Funciona a Autenticação

A conexão se autentica com credenciais de cliente OAuth2 (ou com as credenciais de API de autenticação básica que a configuração de segurança do seu Fusion Cloud emite para usuários de integração) em um usuário de API dedicado. A função do usuário de API controla tanto quais entidades do razão geral ele pode ler quanto por quais funções de FBDI/GL Interface ele pode lançar.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| URL da instância | Texto | A URL da sua instância do Fusion Cloud, por exemplo `https://yourorg.fa.us2.oraclecloud.com`. |
| ID do cliente | Texto | O ID de cliente OAuth2 do usuário de API (ou o nome de usuário, na autenticação básica). |
| Segredo do cliente | Texto | O segredo de cliente OAuth2 do usuário de API (ou a senha, na autenticação básica). Armazenado de forma criptografada. |

## Entidades Disponíveis para Importação

Duas etapas de importação cobrem volumes de extração diferentes, ambas em `gl_balances` e `journal_batches`:

- **Import Fusion Entity** — uma chamada direta de OData/BIP, para uma extração rotineira e limitada.
- **Import Fusion Bulk Extract** — um job assíncrono de exportação FBDI/BIP, para uma extração grande.

As duas oferecem suporte a filtros de intervalo (`ge`/`le`) em campos de data, de período contábil e de saldo/valor numérico, além de filtros de igualdade em campos discretos como razão ou moeda. Consulte [Import Fusion Entity](/pt-br/reference/workflow-steps/oracle-fusion/import-fusion-entity/) e [Import Fusion Bulk Extract](/pt-br/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) para a referência completa dos campos.

## Lançar Lançamentos Contábeis

A etapa **Oracle Fusion: Post Journal Entry** lança lotes de lançamentos do razão geral pelo pipeline compartilhado de gravação em ERP do PlaidCloud: grava o lote na tabela de preparação GL_INTERFACE da Oracle como um arquivo FBDI, envia o job ESS Journal Import Launcher e o acompanha até um estado final, e confirma antes de informar que um lote foi lançado. Uma correção lança um novo lançamento de estorno, com débito e crédito invertidos, em vez de editar o original. Consulte [Oracle Fusion: Post Journal Entry](/pt-br/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) para a referência dos campos e [Conectar ao Oracle Fusion](/pt-br/guides/connections/oracle-fusion/) para o passo a passo completo do lançamento.

## Limitações Conhecidas

| Limitação | O que significa |
|---|---|
| Latência do job ESS | O Journal Import Launcher é executado como um job agendado, não como uma chamada síncrona — uma execução de lançamento leva bem mais tempo do que uma gravação direta pela API. |
| Latência da extração em massa | `import_fusion_bulk_extract` aguarda um job de exportação FBDI/BIP — reserve-o para extrações grandes demais para o caminho direto de `import_fusion_entity`. |
## Relacionados

- [Conectar ao Oracle Fusion (guia)](/pt-br/guides/connections/oracle-fusion/) — passo a passo: criar a conexão, testá-la, importar uma entidade e lançar um lançamento contábil.
- [Import Fusion Entity](/pt-br/reference/workflow-steps/oracle-fusion/import-fusion-entity/)
- [Import Fusion Bulk Extract](/pt-br/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/)
- [Oracle Fusion: Post Journal Entry](/pt-br/reference/workflow-steps/oracle-fusion/oracle-fusion-post/)
- [Revisar o Histórico de Lançamentos em ERP](/pt-br/guides/connections/erp-post-history/)
