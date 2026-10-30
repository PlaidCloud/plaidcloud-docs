---
title: Conector REST Acumatica
description: Configure uma ligação à API REST baseada em contratos do Acumatica no PlaidCloud para importar dados mestre e transacionais e lançar transações de diário, faturas, faturas de fornecedor e pagamentos.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/acumatica.md
---

## Documentação da API

A [API REST baseada em contratos](https://help.acumatica.com/Help?ScreenId=ShowWiki&pageid=e0dea52d-0339-4f34-a6c0-9615ce6a25c2) do Acumatica documenta os pontos de acesso e as opções de consulta que este conector utiliza.

## Como funciona a autenticação

A ligação é **baseada em sessão**: o PlaidCloud inicia sessão uma vez por unidade de trabalho delimitada (`POST <instance>/entity/auth/login` com o seu nome de utilizador, palavra-passe, empresa e ramo opcional) e reutiliza o cookie de sessão resultante em todas as chamadas dessa unidade, terminando a sessão no fim. Não se trata de um fluxo com token de portador nem de OAuth — as sessões contam para o limite de sessões em simultâneo da sua licença Acumatica, que as instâncias de avaliação e de escalões inferiores podem limitar a apenas 2, pelo que deve evitar executar muitos passos Acumatica em paralelo numa única ligação.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de apresentação desta ligação. |
| URL base da instância | Texto | O URL da sua instância Acumatica, por exemplo `https://yourcompany.acumatica.com`. |
| Nome do ponto de acesso | Texto | O nome do ponto de acesso do contrato. `Default`, a menos que tenha sido publicado um ponto de acesso personalizado. |
| Versão do ponto de acesso | Texto | Opcional, por exemplo `25.200.001`. Deixe em branco para utilizar a versão mais recente publicada do ponto de acesso. |
| Empresa / Inquilino | Texto | O ID exato da empresa Acumatica em que esta ligação inicia sessão. |
| Ramo | Texto | Opcional. Deixe em branco para utilizar o ramo predefinido do utilizador de início de sessão. |
| Nome de utilizador | Texto | O início de sessão do utilizador de API do PlaidCloud. |
| Palavra-passe | Texto | A palavra-passe do utilizador de API do PlaidCloud. Guardada cifrada. |

## Entidades disponíveis para importação

O passo **Import Acumatica Entity** abrange 18 entidades baseadas em contratos:

**Dados mestre e de referência** — `account`, `subaccount`, `ledger`, `financial_period`, `branch`, `currency`, `currency_rate`, `customer`, `vendor`, `stock_item`, `warehouse`, `employee`, `tax_category`, `project`

**Dados transacionais** — `sales_invoice`, `bill`, `sales_order`, `shipment`

Cada extração suporta um comutador `Active Only`, um limite `Updated After` e filtros do lado do servidor por entidade. Consulte [Import Acumatica Entity](/pt-pt/reference/workflow-steps/acumatica/import-acumatica-entity/) para a referência completa dos campos.

## Lançamento de documentos

O passo **Acumatica Post** lança documentos **JournalTransaction**, **SalesInvoice**, **Bill** e **Payment** através do pipeline de escrita ERP partilhado do PlaidCloud: criar em retenção, libertar (uma ação assíncrona) e confirmar a libertação antes de comunicar que um documento foi lançado. Consulte [Acumatica: Post Documents](/pt-pt/reference/workflow-steps/acumatica/acumatica-post/) para a referência dos campos e [Ligar ao Acumatica](/pt-pt/guides/connections/acumatica/) para o passo a passo completo do lançamento.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| Leituras dependentes de GI não abrangidas | O balancete, o detalhe de transações do razão geral, o inventário disponível, os orçamentos e os dados intercompanhias residem nas Generic Inquiries (GI) do Acumatica, não nas 18 entidades baseadas em contratos acima. Crie a GI no Acumatica e extraia-a com uma [ligação REST genérica](/pt-pt/reference/connectors/rest/generic-rest/). |
| Sem chave de idempotência nativa na escrita | A API de escrita baseada em PUT do Acumatica não tem um campo de idempotência; o registo de reserva do próprio PlaidCloud é a única proteção contra um lançamento duplicado. |
| A reversão é manual | Nenhum tipo de documento tem uma ação de anulação/reversão documentada. Um documento lançado não pode ser revertido a partir do PlaidCloud — corrija-o diretamente no Acumatica. |
| Sem campo de correlação de pagamentos | O Acumatica não expõe nenhum campo documentado para correlacionar um pagamento com o pedido do PlaidCloud após um resultado ambíguo; um pagamento em dúvida é colocado em quarentena para resolução manual. |
| A filtragem de linhas de documento não é feita no servidor | Os filtros do estilo `$filter` chegam aos campos da entidade e do cabeçalho, não às dimensões das linhas de um documento (por exemplo, um centro de custo ao nível da linha). Delimite as linhas no seu fluxo de trabalho depois da extração. |
## Relacionado

- [Ligar ao Acumatica (guia)](/pt-pt/guides/connections/acumatica/) — passo a passo: criar a ligação, testá-la, importar uma entidade e lançar um lote.
- [Import Acumatica Entity](/pt-pt/reference/workflow-steps/acumatica/import-acumatica-entity/)
- [Acumatica: Post Documents](/pt-pt/reference/workflow-steps/acumatica/acumatica-post/)
- [Rever o histórico de lançamentos ERP](/pt-pt/guides/connections/erp-post-history/)
