---
title: Ferramentas CLI
description: Referência das ferramentas de linha de comandos do PlaidCloud — agente PlaidLink, suplemento PlaidXL para Excel e a CLI do Jupyter para integração com blocos de notas.
sidebar:
  label: CLI
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/index.md
---

O PlaidCloud disponibiliza três ferramentas de linha de comandos e locais para trabalhar com áreas de trabalho fora da interface web:

## PlaidLink

O [PlaidLink](/pt-pt/reference/cli/plaidlink/) é um agente que é executado na sua rede para ligar os fluxos de trabalho do PlaidCloud a recursos protegidos por firewall — bases de dados, partilhas de ficheiros e outros sistemas que o PlaidCloud não consegue alcançar diretamente. Instala-se como serviço do Windows, daemon Unix/Linux/Mac, contentor ou pod do Kubernetes.

- [Instalar](/pt-pt/reference/cli/plaidlink/install/)
- [Configurar](/pt-pt/reference/cli/plaidlink/configure/)
- [Agentes](/pt-pt/reference/cli/plaidlink/agents/)
- [Atualizar](/pt-pt/reference/cli/plaidlink/upgrade/)

## PlaidXL

O [PlaidXL](/pt-pt/reference/cli/plaidxl/) é o suplemento do PlaidCloud para o Microsoft Excel. Obtém tabelas e dimensões do projeto para folhas de cálculo, atualiza-as a pedido, acrescenta fórmulas `PLAIDXL` que calculam valores agregados e indicadores governados a partir dos dados do PlaidCloud, e escreve de volta os valores planeados.

- [Instalar](/pt-pt/reference/cli/plaidxl/install/)
- [Iniciar sessão](/pt-pt/reference/cli/plaidxl/connect/)
- [Trabalhar com tabelas e dimensões](/pt-pt/reference/cli/plaidxl/retrieve/)
- [Funções personalizadas](/pt-pt/reference/cli/plaidxl/functions/)
- [Criar um relatório](/pt-pt/reference/cli/plaidxl/build-a-report/)
- [Detalhar, escolher membros e explicar números](/pt-pt/reference/cli/plaidxl/drill/)
- [Introduzir valores no PlaidCloud](/pt-pt/reference/cli/plaidxl/write-values/)
- [Perguntar ao Weave no Excel](/pt-pt/reference/cli/plaidxl/weave/)
- [A faixa de opções do PlaidCloud](/pt-pt/reference/cli/plaidxl/ribbon/)
- [Resolução de problemas](/pt-pt/reference/cli/plaidxl/troubleshooting/)

## CLI do Jupyter

A [CLI do Jupyter](/pt-pt/reference/cli/jupyter/) permite aos cientistas de dados trabalhar com os dados de projeto do PlaidCloud a partir de blocos de notas Jupyter, através de uma CLI com conhecimento do PlaidCloud e de auxiliares Python.

- [Linha de comandos](/pt-pt/reference/cli/jupyter/command-line/)
- [Bloco de notas Jupyter](/pt-pt/reference/cli/jupyter/jupyter-notebook/)
- [Configuração do OAuth](/pt-pt/reference/cli/jupyter/oauth-setup/)
