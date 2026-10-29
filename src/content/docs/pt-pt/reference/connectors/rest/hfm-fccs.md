---
title: Conector HFM / FCCS
description: Configure uma ligação ao Oracle FCCS (Financial Consolidation and Close, EPM Cloud) no PlaidCloud para obter por autosserviço uma fatia de dados ad hoc com um seletor de ponto de vista, com colocação em cache opcional e uma carga recorrente agendada.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/hfm-fccs.md
---

Ligue o PlaidCloud ao Oracle **FCCS** — Financial Consolidation and Close, parte do Oracle EPM Cloud — para que um utilizador de finanças possa obter por autosserviço uma fatia de dados sem abrir um pedido de suporte junto da equipa HFM. O passo [HFM/FCCS: Ler dados (ad hoc)](/pt-pt/reference/workflow-steps/oracle-epm/hfm-fccs-read/) parece uma consulta em direto, mas, por baixo, é um pedido assíncrono → consulta periódica → obtenção sobre a API de tarefas de exportação de dados do FCCS.

O tipo de ligação aparece no seletor de ligações como **REST - HFM/FCCS**.

:::note[Delimite a dimensão de entidade]
Mantenha todos os pontos de vista delimitados — uma extração sem delimitação pode bloquear a aplicação FCCS durante muito tempo enquanto a tarefa de exportação é executada.
:::

## Documentação da API

O conector utiliza a [API REST](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/index.html) do Oracle EPM Cloud — os pontos de acesso de metadados da aplicação (para descobrir dimensões e membros) e os pontos de acesso das tarefas de exportação de dados (para pedir, consultar periodicamente e obter uma grelha).

## Como funciona a autenticação

A ligação utiliza **autenticação HTTP Basic com uma conta de serviço** num pod EPM Cloud clássico — não existe fluxo OAuth nem de tokens (os pods OCI / Gen 2 com token de portador estão fora do âmbito). Quando é definido um **Domínio de identidade**, o PlaidCloud compõe o início de sessão como `identitydomain.username` (o domínio, um ponto e o nome de utilizador); se deixar o Domínio de identidade em branco, ou se o seu nome de utilizador já contiver um ponto, o nome de utilizador é enviado tal como está. Aponte a ligação para uma conta de serviço de integração dedicada, com acesso de leitura às aplicações e às fatias de ponto de vista que os seus utilizadores de autosserviço vão extrair.

## Configuração

| Campo | Obrigatório | Descrição |
|---|---|---|
| Nome | Sim | Nome de apresentação desta ligação. |
| URL do EPM Cloud | Sim | O URL do pod/serviço EPM Cloud, por exemplo `https://planning-test-yourdomain.epm.us2.oraclecloud.com`. |
| Domínio de identidade | Não | O domínio de identidade do seu EPM Cloud. Quando definido, o PlaidCloud antepõe-no ao nome de utilizador como `identitydomain.username` no início de sessão. |
| Nome de utilizador | Sim | O nome de utilizador da conta de serviço de integração. |
| Palavra-passe | Sim | A palavra-passe da conta de serviço. Guardada cifrada. |
| Aplicação predefinida | Não | Uma aplicação FCCS predefinida para preencher previamente o seletor de ponto de vista do passo. Cada passo pode substituí-la. |

## O que pode fazer com a ligação

- **Obter por autosserviço uma fatia ad hoc.** Crie um ponto de vista (POV) — Aplicação mais as dimensões do FCCS — no formulário do passo, clique em Executar e uma tabela de resultados é carregada automaticamente. Consulte [HFM/FCCS: Ler dados (ad hoc)](/pt-pt/reference/workflow-steps/oracle-epm/hfm-fccs-read/).
- **Dispensar o pedido de suporte.** A fatia é executada com a conta de serviço da ligação, pelo que um utilizador de finanças obtém os dados por si próprio em vez de esperar por um administrador HFM.
- **Colocar em cache extrações repetidas.** O mesmo POV e data de referência servidos novamente devolve de imediato a cópia já carregada, em vez de consultar de novo o FCCS.
- **Controlar quem vê que entidades.** A tabela carregada está **pronta para segurança ao nível da linha**: um administrador pode declarar o Acesso a linhas na coluna `Entity` para que os utilizadores de autosserviço vejam apenas as entidades a que têm direito. Isto é controlado pelo administrador, não é automático — consulte a referência do passo.
- **Agendar uma carga recorrente.** Ative **Destino associado** para promover uma fatia ad hoc a uma tabela persistente que cresce de forma aditiva e é intercalada em vez de substituída, de modo que o mesmo passo colocado num fluxo de trabalho agendado se torna uma carga recorrente noturna.

## Descoberta de metadados

Nos pods FCCS suportados, o formulário do passo descobre em direto a lista de membros de cada dimensão a partir dos metadados da aplicação, assim que escolhe uma ligação e uma aplicação, de modo que o seletor de POV oferece membros reais para escolher (volta a descobrir sempre que um dos dois muda). Nos pods mais antigos que não expõem o ponto de acesso de metadados, a descoberta não devolve nada e o seletor recorre à introdução manual — escreve os nomes dos membros à mão, e um ponto de vista guardado é sempre preservado. A extração funciona da mesma forma nos dois casos.

## Limitações conhecidas

| Limitação | O que significa |
|---|---|
| Só de leitura | O conector extrai dados do FCCS. Não escreve dados de consolidação, não executa consolidações nem lança dados de volta. |
| Delimite a dimensão de entidade | Uma extração sem delimitação (sem seleção de `Entity`) pode bloquear a aplicação FCCS durante muito tempo enquanto a tarefa de exportação é executada. Mantenha a seleção de entidades delimitada. |
| Membros manuais em pods mais antigos | Quando um pod não expõe o ponto de acesso de metadados, as listas de membros não são preenchidas automaticamente — introduza os nomes dos membros à mão. |
| A segurança ao nível da linha é controlada pelo administrador, não é automática | A tabela carregada pode ser controlada com Acesso a linhas, mas um administrador tem de publicar, declarar a coluna `Entity`, aprovar a primeira escrita controlada e reconciliar. Até o fazer, a tabela não é filtrada. |

## Relacionado

- [Extrair do HFM / FCCS (guia)](/pt-pt/guides/connections/hfm-fccs/) — criar a ligação, criar um POV, executá-lo, colocar em cache, controlar e agendar.
- [HFM/FCCS: Ler dados (ad hoc)](/pt-pt/reference/workflow-steps/oracle-epm/hfm-fccs-read/) — a referência dos campos do passo.
- [Gerir grupos de segurança e atribuições](/pt-pt/administration/access/managing-security-groups-and-assignments/) — como o Acesso a linhas controla a tabela carregada.
- [Criar e gerir uma ligação](/pt-pt/guides/connections/create-connection/)
