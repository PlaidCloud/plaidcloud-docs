---
title: Grok
description: Connectez Grok de xAI au serveur MCP de PlaidCloud grâce à ses connecteurs personnalisés.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/grok.md
---

[Grok](https://grok.com) prend en charge les serveurs MCP via des connecteurs personnalisés, configurés sur grok.com.

## Configuration

1. Rendez-vous sur [grok.com/connectors](https://grok.com/connectors) et cliquez sur **New Connector → Custom**.
2. Collez l'URL du serveur MCP : `https://<your-workspace>.plaid.cloud/mcp`.
3. Terminez la connexion lorsque Grok vous redirige vers PlaidCloud. Une page **Application Access Request** s'affiche, qui nomme l'application demandeuse et l'URI de redirection vers laquelle elle enverra les identifiants ; vérifiez que les deux correspondent à Grok avant d'approuver.

## Offres pour les entreprises

Les espaces de travail Business et Enterprise passent par un administrateur d'équipe pour configurer les connecteurs : un administrateur de l'espace de travail provisionne le connecteur sur grok.com/connectors, puis les membres y connectent leur propre compte.

## Actualiser l'accès

Si Grok indique que la connexion doit être réautorisée, répétez l'étape de connexion : le connecteur conserve son URL, vous n'avez donc pas besoin de le rajouter depuis le début.
