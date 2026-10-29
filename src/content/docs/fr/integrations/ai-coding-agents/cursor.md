---
title: Cursor
description: Configurez l'IDE Cursor pour appeler les outils MCP de PlaidCloud grâce à sa prise en charge intégrée de MCP.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

[Cursor](https://cursor.com) prend en charge les serveurs MCP via un fichier de configuration `mcp.json`. Sa structure est la même que celle du `.mcp.json` de Claude Code ; le même extrait avec jeton porteur fonctionne donc dans les deux.

La fenêtre **Connecter votre IA** de la barre d'outils de PlaidCloud propose un lien en un clic **Installer dans Cursor** qui ajoute le serveur via une connexion OAuth, sans fichier de configuration. Essayez-le d'abord. La configuration avec jeton porteur ci-dessous est celle que cette page documente en détail, et le repli si le lien en un clic n'ajoute pas le serveur ou si Cursor n'est pas installé.

## Configuration

1. Obtenez un jeton porteur en vous rendant sur `https://<your-workspace>.plaid.cloud/mcp/setup/token` dans un navigateur où vous êtes connecté à PlaidCloud.

2. Ouvrez la configuration MCP de Cursor :
   - **Au niveau du projet** : créez `.cursor/mcp.json` à la racine de votre projet.
   - **Au niveau de l'utilisateur (tous les projets)** : créez `~/.cursor/mcp.json` dans votre répertoire personnel.

3. Ajoutez le serveur PlaidCloud :

    ```json
    {
      "mcpServers": {
        "plaidcloud": {
          "url": "https://<your-workspace>.plaid.cloud/mcp",
          "headers": {
            "Authorization": "Bearer eyJhbGc…"
          }
        }
      }
    }
    ```

4. Ouvrez **Settings → MCP** dans Cursor pour vérifier que le serveur est connecté. S'il affiche une erreur, consultez [Dépannage](../troubleshooting/).

## Utiliser les outils

Dans Composer ou le panneau de conversation de Cursor, vous pouvez donner des instructions à l'agent en langage courant (« décris la structure du projet `Q4 Forecast` ») et il choisira l'outil `plaidcloud_*` approprié. Les appels d'outils et les réponses apparaissent en ligne ; examinez les opérations de modification avant d'approuver.

## Actualiser le jeton

Lorsque le jeton expire, rechargez `https://<your-workspace>.plaid.cloud/mcp/setup/token` et collez la nouvelle valeur dans `mcp.json`. Cursor prend en compte la modification sans redémarrage complet ; désactivez puis réactivez le serveur dans **Settings → MCP** si nécessaire.

## Plusieurs tenants

Répétez l'entrée sous un autre nom :

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
