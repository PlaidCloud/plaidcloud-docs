---
title: Conector SAP ECC e S/4HANA
description: Configure a conexão SAP ECC / S/4HANA no PlaidCloud para integrar dados financeiros, logísticos e operacionais do SAP aos seus fluxos de trabalho por RFC.
sidebar:
  order: 1
  label: SAP ECC / S/4HANA
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-ecc.md
---

Um único tipo de conexão atende ao SAP ECC e ao SAP S/4HANA. Os dois são acessados da mesma forma — Remote Function Calls no servidor de aplicativos — por isso o PlaidCloud não pergunta em qual geração você está. Na tela **Conexões**, escolha **Novo → Instância SAP ECC / S/4HANA**.

Todas as [etapas de fluxo de trabalho do SAP](/pt-br/reference/workflow-steps/sap/) são executadas em uma conexão deste tipo. Para pesquisar no SAP e extrair tabelas, transações, relatórios e SAP Queries salvas, consulte [Extrações Ad Hoc do SAP ECC / S/4HANA](/pt-br/guides/connections/sap-adhoc-extract/).

## Documentação do Fornecedor

A SAP removeu toda a documentação do ECC e atualmente só oferece documentação do [S/4HANA](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE). As interfaces RFC que o PlaidCloud usa são comuns às duas.

## Configuração

Estes campos aparecem ao criar ou editar a conexão.

### Descrição da conta

| Campo | Tipo | Descrição |
|---|---|---|
| Nome da conta | Texto | Nome de exibição desta conexão, mostrado sempre que uma etapa escolhe uma conexão. Obrigatório. |
| Memorando | Texto (várias linhas) | Observações opcionais sobre a conexão — para qual sistema ela aponta, quem é o responsável. |

### Ambiente SAP

| Campo | Tipo | Descrição |
|---|---|---|
| Cliente | Texto | Número do mandante SAP, por exemplo `100`. Obrigatório. |
| Idioma | Seleção | Idioma de logon, como um código SAP de duas letras. O padrão é `EN`. Obrigatório. |
| Nível de rastreamento | Seleção | Detalhamento do rastreamento de RFC — Desativado, Resumido, Detalhado ou Completo. Deixe em Desativado, a menos que esteja diagnosticando um problema de conexão. Obrigatório. |
| Tipo de conexão | Opções | **Usar conexão direta única** para acessar um servidor de aplicativos, ou **Usar conexão de vários sistemas com balanceamento de carga** para passar por um servidor de mensagens. Os campos abaixo são ativados de acordo com esta escolha. |

Escolher **Usar conexão direta única** habilita:

| Campo | Tipo | Descrição |
|---|---|---|
| Host | Texto | Nome do host ou endereço IP do servidor de aplicativos. |
| Número do sistema | Texto | Número do sistema SAP de dois dígitos, por exemplo `00`. |

Escolher **Usar conexão de vários sistemas com balanceamento de carga** habilita:

| Campo | Tipo | Descrição |
|---|---|---|
| Host MS | Texto | Nome do host ou endereço IP do servidor de mensagens. |
| Servidor MS | Texto | Porta ou nome do serviço do servidor de mensagens. |
| ID do sistema | Texto | ID do sistema SAP de três caracteres, por exemplo `PRD`. |
| Grupo | Texto | Grupo de logon entre os quais balancear, por exemplo `PUBLIC`. |

### Credenciais de autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| Usuário | Texto | Usuário de logon do SAP para as chamadas RFC. Obrigatório. |
| Senha | Senha | Senha desse usuário. Somente gravação — deixe em branco ao editar para manter a senha armazenada. |

### Uso

| Campo | Tipo | Descrição |
|---|---|---|
| Ativo (permitir acesso) | Alternância | Indica se a conexão pode ser usada. Desmarque para pausar a conexão sem excluí-la. |
| Somente leitura | Alternância | Restringe a conexão a operações de leitura. |

### Modelo de segurança

| Campo | Tipo | Descrição |
|---|---|---|
| Modelo de segurança | Seleção | Quem pode usar esta conexão — Privado (somente proprietários), Somente membros específicos, Somente grupos de segurança específicos ou Todos os membros do espaço de trabalho. |

## Testar a Conexão

**Testar conexão**, na janela da conexão, faz logon com os detalhes acima e informa o resultado. Ao editar uma conexão existente e alterar qualquer configuração, digite a senha novamente antes de testar — a senha armazenada não é enviada junto com os valores editados.
