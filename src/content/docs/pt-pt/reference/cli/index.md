---
title: Ferramentas CLI
description: "Referência das ferramentas de linha de comandos do PlaidCloud: agente PlaidLink, suplemento PlaidXL para Excel e CLI Jupyter para integração com blocos de notas."
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

O PlaidCloud disponibiliza três ferramentas de linha de comandos e instaladas localmente para trabalhar com áreas de trabalho fora da interface web:

## PlaidLink

O [PlaidLink](/pt-pt/reference/cli/plaidlink/) é um agente que é executado na sua rede para ligar os fluxos de trabalho do PlaidCloud a recursos protegidos por firewall, como bases de dados, partilhas de ficheiros e outros sistemas que o PlaidCloud não consegue alcançar diretamente. Instala-se como serviço do Windows, daemon Unix/Linux/Mac, contentor ou pod do Kubernetes.

- [Instalar](/pt-pt/reference/cli/plaidlink/install/)
- [Configurar](/pt-pt/reference/cli/plaidlink/configure/)
- [Agentes](/pt-pt/reference/cli/plaidlink/agents/)
- [Atualizar](/pt-pt/reference/cli/plaidlink/upgrade/)

## PlaidXL

O [PlaidXL](/pt-pt/reference/cli/plaidxl/) é o suplemento do PlaidCloud para Microsoft Excel. Obtém tabelas e dimensões de projetos para folhas de cálculo, atualiza-as a pedido e adiciona fórmulas `PLAIDXL` que calculam valores agregados a partir dos dados do PlaidCloud.

- [Instalar](/pt-pt/reference/cli/plaidxl/install/)
- [Iniciar sessão](/pt-pt/reference/cli/plaidxl/connect/)
- [Trabalhar com tabelas e dimensões](/pt-pt/reference/cli/plaidxl/retrieve/)
- [Funções personalizadas](/pt-pt/reference/cli/plaidxl/functions/)
- [Criar um relatório com funções personalizadas](/pt-pt/reference/cli/plaidxl/build-a-report/)
- [O friso do PlaidCloud](/pt-pt/reference/cli/plaidxl/ribbon/)
- [Resolução de problemas](/pt-pt/reference/cli/plaidxl/troubleshooting/)

## CLI Jupyter

A [CLI Jupyter](/pt-pt/reference/cli/jupyter/) permite que os cientistas de dados trabalhem com dados de projetos do PlaidCloud a partir de blocos de notas Jupyter, através de uma CLI que reconhece o PlaidCloud e de auxiliares em Python.

- [Linha de comandos](/pt-pt/reference/cli/jupyter/command-line/)
- [Bloco de notas Jupyter](/pt-pt/reference/cli/jupyter/jupyter-notebook/)
- [Configuração de OAuth](/pt-pt/reference/cli/jupyter/oauth-setup/)
