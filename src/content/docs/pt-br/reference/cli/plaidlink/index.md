---
title: PlaidLink
description: Instale e configure agentes PlaidLink para acessar com segurança sistemas protegidos por firewalls, permitindo consultas remotas e transferências de arquivos.
sidebar:
  label: PlaidLink
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/index.md
---

O PlaidLink fornece acesso indireto a sistemas e processos de clientes que são protegidos por firewalls ou estão atrás de outras restrições que dificultam conexões diretas a partir do PlaidCloud. Com um Agente PlaidCloud instalado dentro da área isolada, o PlaidCloud pode solicitar que o agente execute ações como rodar consultas, baixar ou enviar arquivos, verificar condições de sensores, interagir com o SAP e muito mais.

Como o agente inicia o contato com o PlaidCloud e se comunica por protocolos de rede HTTPS padrão, ele normalmente funciona com configuração mínima. Além disso, o agente pode ser executado como um usuário sem privilégios para controlar os direitos de acesso em um ambiente restrito.

## Tópicos

- [Instalar](/pt-br/reference/cli/plaidlink/install/) — colocar o PlaidLink em funcionamento no Windows, Linux, macOS ou em um contêiner
- [Configurar](/pt-br/reference/cli/plaidlink/configure/) — configurações de conexão, credenciais e opções de execução
- [Agentes](/pt-br/reference/cli/plaidlink/agents/) — gerenciamento de vários agentes e seus recursos
- [Atualizar](/pt-br/reference/cli/plaidlink/upgrade/) — migração para uma build mais recente do PlaidLink
