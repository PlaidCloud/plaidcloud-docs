---
title: Conector SAP ECC e S/4HANA
description: Configure a ligação SAP ECC / S/4HANA no PlaidCloud para integrar nos seus fluxos de trabalho dados financeiros, logísticos e operacionais do SAP através de RFC.
sidebar:
  order: 1
  label: SAP ECC / S/4HANA
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-ecc.md
---

Um único tipo de ligação abrange o SAP ECC e o SAP S/4HANA. Ambos são acedidos da mesma forma (Remote Function Calls ao servidor de aplicações), pelo que o PlaidCloud não lhe pergunta em que geração se encontra. No ecrã **Ligações**, escolha **New → Instância SAP ECC / S/4HANA**.

Todos os [passos SAP do fluxo de trabalho](/pt-pt/reference/workflow-steps/sap/) são executados com uma ligação deste tipo. Para pesquisar no SAP e extrair tabelas, transações, relatórios e consultas SAP Query guardadas, consulte [Extrações ad hoc do SAP ECC / S/4HANA](/pt-pt/guides/connections/sap-adhoc-extract/).

## Documentação do fabricante

A SAP removeu toda a documentação do ECC e disponibiliza atualmente apenas documentação do [S/4HANA](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE). As interfaces RFC que o PlaidCloud utiliza são comuns a ambos.

## Configuração

Estes campos aparecem ao criar ou editar a ligação.

### Descrição da conta

| Campo | Tipo | Descrição |
|---|---|---|
| Nome da conta | Texto | Nome de apresentação desta ligação, mostrado sempre que um passo escolhe uma ligação. Obrigatório. |
| Nota | Texto (várias linhas) | Notas opcionais sobre a ligação: para que sistema aponta e quem é o responsável. |

### Ambiente SAP

| Campo | Tipo | Descrição |
|---|---|---|
| Cliente | Texto | Número do cliente SAP, por exemplo `100`. Obrigatório. |
| Idioma | Seleção | Idioma de início de sessão como código SAP de duas letras. A predefinição é `EN`. Obrigatório. |
| Nível de rastreio | Seleção | Nível de detalhe do rastreio RFC: Desligado, Breve, Detalhado ou Completo. Deixe em Desligado, a menos que esteja a diagnosticar um problema de ligação. Obrigatório. |
| Tipo de ligação | Opção | **Usar ligação direta única** para aceder a um servidor de aplicações, ou **Usar ligação multissistema com balanceamento de carga** para passar por um servidor de mensagens. Os campos abaixo são ativados consoante esta escolha. |

Ao escolher **Usar ligação direta única**, ficam ativados:

| Campo | Tipo | Descrição |
|---|---|---|
| Anfitrião | Texto | Nome do anfitrião ou endereço IP do servidor de aplicações. |
| Número do sistema | Texto | Número do sistema SAP de dois dígitos, por exemplo `00`. |

Ao escolher **Usar ligação multissistema com balanceamento de carga**, ficam ativados:

| Campo | Tipo | Descrição |
|---|---|---|
| Anfitrião MS | Texto | Nome do anfitrião ou endereço IP do servidor de mensagens. |
| Servidor MS | Texto | Porta ou nome do serviço do servidor de mensagens. |
| ID do sistema | Texto | ID do sistema SAP de três carateres, por exemplo `PRD`. |
| Grupo | Texto | Grupo de início de sessão pelo qual distribuir a carga, por exemplo `PUBLIC`. |

### Credenciais de autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| Utilizador | Texto | Utilizador de início de sessão SAP para as chamadas RFC. Obrigatório. |
| Palavra-passe | Palavra-passe | Palavra-passe desse utilizador. Só de escrita: deixe em branco ao editar para manter a palavra-passe guardada. |

### Utilização

| Campo | Tipo | Descrição |
|---|---|---|
| Ativa (permitir acesso) | Interruptor | Indica se a ligação pode ser utilizada. Desmarque-a para suspender a ligação sem a eliminar. |
| Só de leitura | Interruptor | Restringe a ligação a operações de leitura. |

### Modelo de segurança

| Campo | Tipo | Descrição |
|---|---|---|
| Modelo de segurança | Seleção | Quem pode utilizar esta ligação: Privado (apenas proprietários), Apenas membros específicos, Apenas grupos de segurança específicos ou Todos os membros da área de trabalho. |

## Testar a ligação

**Testar ligação** na janela da ligação inicia sessão com os detalhes acima e comunica o resultado. Ao editar uma ligação existente e alterar qualquer definição, volte a escrever a palavra-passe antes de testar: a guardada não é enviada juntamente com os valores editados.
