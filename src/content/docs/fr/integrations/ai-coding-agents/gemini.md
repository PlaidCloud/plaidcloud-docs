---
title: Google Gemini CLI
description: Configurez gemini-cli de Google pour appeler les outils MCP de PlaidCloud.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/gemini.md
---

[`gemini-cli`](https://github.com/google-gemini/gemini-cli) de Google prend en charge les serveurs MCP via `~/.gemini/settings.json` (au niveau de l'utilisateur) ou `.gemini/settings.json` à la racine d'un projet (au niveau du projet).

## Configuration

1. Obtenez un jeton porteur en vous rendant sur `https://<your-workspace>.plaid.cloud/mcp/setup/token` dans un navigateur où vous êtes connecté à PlaidCloud.

2. Modifiez `~/.gemini/settings.json` (créez-le s'il n'existe pas) :

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "httpUrl": "https://<your-workspace>.plaid.cloud/mcp",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

3. Redémarrez `gemini`. Dans une session, exécutez `/mcp` pour vérifier que le serveur est connecté et lister ses outils.

## Utilisation

Demandez à Gemini d'utiliser directement les outils PlaidCloud :

- « Utilise plaidcloud pour lister les workflows du projet `Sales Forecasting`. »
- « Décris les colonnes de la table `customers` et l'instantané le plus récent. »

Vous pouvez aussi appeler des outils explicitement avec la commande `/tools` si vous voulez inspecter le schéma d'entrée d'un outil précis avant de l'invoquer.

## Actualiser le jeton

Lorsque le jeton expire, rechargez `https://<your-workspace>.plaid.cloud/mcp/setup/token` et mettez à jour la valeur de `Authorization` dans `settings.json`. Redémarrez `gemini` pour prendre en compte la modification.

## Gemini Code Assist (IDE)

Gemini Code Assist dans VSCode/JetBrains accepte la même configuration `mcpServers` dans ses paramètres d'agent. Le schéma correspond à celui de la CLI : collez le même extrait dans le panneau des paramètres de serveurs MCP de l'IDE.
