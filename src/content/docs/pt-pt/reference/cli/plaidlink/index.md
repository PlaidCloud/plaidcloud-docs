---
title: PlaidLink
description: Instale e configure agentes PlaidLink para um acesso seguro a sistemas protegidos por firewalls, permitindo consultas remotas e transferências de ficheiros.
sidebar:
  label: PlaidLink
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/index.md
---

O PlaidLink proporciona acesso indireto a sistemas e processos de clientes que estão protegidos por firewalls ou por outras restrições que dificultam as ligações diretas a partir do PlaidCloud. Com um Agente PlaidCloud instalado na área isolada, o PlaidCloud pode pedir ao agente que realize ações como executar consultas, transferir ou carregar ficheiros, verificar condições de sensores, interagir com o SAP e muito mais.

Como é o agente que inicia o contacto com o PlaidCloud e comunica através de protocolos de rede HTTPS padrão, normalmente pode funcionar com uma configuração mínima. Além disso, o agente pode ser executado como um utilizador sem privilégios, para controlar os direitos de acesso num ambiente restrito.

## Tópicos

- [Instalar](/pt-pt/reference/cli/plaidlink/install/) — colocar o PlaidLink em funcionamento no Windows, no Linux, no macOS ou num contentor
- [Configurar](/pt-pt/reference/cli/plaidlink/configure/) — definições de ligação, credenciais e opções de execução
- [Agentes](/pt-pt/reference/cli/plaidlink/agents/) — gerir vários agentes e as respetivas capacidades
- [Atualizar](/pt-pt/reference/cli/plaidlink/upgrade/) — passar para uma versão mais recente do PlaidLink
