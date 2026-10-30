---
title: Conector REST do Acumatica
description: Configure uma conexão com a API REST baseada em contrato do Acumatica no PlaidCloud para importar dados mestres e transacionais e lançar transações contábeis, faturas, contas a pagar e pagamentos.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/acumatica.md
---

## Documentação da API

A [API REST baseada em contrato](https://help.acumatica.com/Help?ScreenId=ShowWiki&pageid=e0dea52d-0339-4f34-a6c0-9615ce6a25c2) do Acumatica documenta os endpoints e as opções de consulta usados por este conector.

## Como funciona a autenticação

A conexão é **baseada em sessão**: o PlaidCloud faz login uma vez por unidade de trabalho delimitada (`POST <instance>/entity/auth/login` com seu nome de usuário, senha, empresa e filial opcional) e reutiliza o cookie de sessão resultante em todas as chamadas dessa unidade, fazendo logout ao terminar. Não é um fluxo de token de portador nem OAuth: as sessões contam para o limite de sessões simultâneas da sua licença do Acumatica, que instâncias de avaliação e de níveis inferiores podem limitar a apenas 2. Por isso, evite executar muitas etapas do Acumatica em paralelo em uma mesma conexão.

## Configuração

| Campo | Tipo | Descrição |
|---|---|---|
| Nome | Texto | Nome de exibição desta conexão. |
| URL base da instância | Texto | A URL da sua instância do Acumatica, por exemplo `https://yourcompany.acumatica.com`. |
| Nome do endpoint | Texto | O nome do endpoint de contrato. `Default`, a menos que um endpoint personalizado tenha sido publicado. |
| Versão do endpoint | Texto | Opcional, por exemplo `25.200.001`. Deixe em branco para usar a última versão publicada do endpoint. |
| Empresa / Tenant | Texto | O ID exato da empresa do Acumatica no qual esta conexão faz login. |
| Filial | Texto | Opcional. Deixe em branco para usar a filial padrão do usuário de login. |
| Nome de usuário | Texto | O login do usuário de API do PlaidCloud. |
| Senha | Texto | A senha do usuário de API do PlaidCloud. Armazenada de forma criptografada. |

## Entidades disponíveis para importação

A etapa **Import Acumatica Entity** cobre 18 entidades baseadas em contrato:

**Dados mestres e de referência** — `account`, `subaccount`, `ledger`, `financial_period`, `branch`, `currency`, `currency_rate`, `customer`, `vendor`, `stock_item`, `warehouse`, `employee`, `tax_category`, `project`

**Dados transacionais** — `sales_invoice`, `bill`, `sales_order`, `shipment`

Cada extração oferece uma opção `Active Only`, um corte `Updated After` e filtros do lado do servidor por entidade. Consulte a etapa [Import Acumatica Entity](/pt-br/reference/workflow-steps/acumatica/import-acumatica-entity/) para a referência completa dos campos.

## Lançamento de documentos

A etapa **Acumatica Post** lança documentos **JournalTransaction**, **SalesInvoice**, **Bill** e **Payment** pelo pipeline de gravação de ERP compartilhado do PlaidCloud: cria em Hold, libera (uma ação assíncrona) e confirma a liberação antes de informar que um documento foi lançado. Consulte a etapa [Acumatica: Post Documents](/pt-br/reference/workflow-steps/acumatica/acumatica-post/) para a referência dos campos e [Conectar ao Acumatica](/pt-br/guides/connections/acumatica/) para o passo a passo completo de lançamento.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| Leituras dependentes de GI não cobertas | Balancete, detalhes de transações do razão geral, estoque disponível, orçamentos e dados intercompany ficam em Generic Inquiries (GI) do Acumatica, não nas 18 entidades baseadas em contrato acima. Crie o GI no Acumatica e extraia-o com uma [conexão REST genérica](/pt-br/reference/connectors/rest/generic-rest/). |
| Sem chave de idempotência nativa na gravação | A API de gravação do Acumatica, baseada em PUT, não tem campo de idempotência; a reserva no livro de controle do próprio PlaidCloud é a única proteção contra lançamento duplicado. |
| Estorno manual | Nenhum tipo de documento tem uma ação documentada de cancelamento ou estorno. Um documento lançado não pode ser estornado pelo PlaidCloud; corrija-o diretamente no Acumatica. |
| Sem campo de correlação de pagamento | O Acumatica não expõe nenhum campo documentado para correlacionar um pagamento à solicitação do PlaidCloud após um resultado ambíguo; um pagamento em dúvida fica em quarentena para resolução manual. |
| A filtragem de itens de linha não é feita no servidor | Filtros no estilo `$filter` alcançam campos da entidade e do cabeçalho, não as dimensões dos itens de linha de um documento (por exemplo, um centro de custo no nível da linha). Delimite as linhas no seu fluxo de trabalho depois da extração. |
## Relacionados

- [Conectar ao Acumatica (guia)](/pt-br/guides/connections/acumatica/) — passo a passo: criar a conexão, testá-la, importar uma entidade e lançar um lote.
- [Import Acumatica Entity](/pt-br/reference/workflow-steps/acumatica/import-acumatica-entity/)
- [Acumatica: Post Documents](/pt-br/reference/workflow-steps/acumatica/acumatica-post/)
- [Revisar o histórico de lançamentos de ERP](/pt-br/guides/connections/erp-post-history/)
