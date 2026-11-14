---
title: Cursor
description: Configurez l’IDE Cursor pour appeler les outils MCP de PlaidCloud via sa prise en charge MCP intégrée.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/cursor.md
---

[Cursor](https://cursor.com) prend en charge les serveurs MCP via un fichier de configuration `mcp.json`. Sa forme est la même que celle du `.mcp.json` de Claude Code ; le même extrait avec jeton porteur fonctionne donc dans les deux.

La fenêtre **Connecter votre IA**, ouverte depuis le menu de l’avatar (utilisateur) de PlaidCloud, propose un lien en un clic **Installer dans Cursor** qui ajoute le serveur via une connexion OAuth, sans fichier de configuration. Essayez-le en premier. La configuration par jeton porteur ci-dessous est celle que cette page documente en détail, et la solution de repli si le lien en un clic n’ajoute pas le serveur ou si Cursor n’est pas installé.

## Configuration

1. Obtenez un jeton porteur en visitant `https://<your-workspace>.plaid.cloud/mcp/setup/token` dans un navigateur où vous êtes connecté à PlaidCloud.

2. Ouvrez la configuration MCP de Cursor :
   - **Portée projet** : créez `.cursor/mcp.json` à la racine de votre projet.
   - **Portée utilisateur (tous les projets)** : créez `~/.cursor/mcp.json` dans votre répertoire personnel.

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

4. Ouvrez **Settings → MCP** dans Cursor pour vérifier que le serveur est connecté. S’il affiche une erreur, consultez [Dépannage](../troubleshooting/).

## Utiliser les outils

Dans Composer ou le panneau de discussion de Cursor, vous pouvez donner des instructions à l’agent en langage courant (« décris la structure du projet `Q4 Forecast` ») et il choisira l’outil `plaidcloud_*` approprié. Les appels d’outils et les réponses s’affichent en ligne : examinez les opérations qui modifient des données avant de les approuver.

## Actualiser le jeton

Lorsque le jeton expire, rechargez `https://<your-workspace>.plaid.cloud/mcp/setup/token` et collez la nouvelle valeur dans `mcp.json`. Cursor prend en compte la modification sans redémarrage complet ; au besoin, désactivez puis réactivez le serveur dans **Settings → MCP**.

## Plusieurs tenants

Répétez l’entrée sous un autre nom :

```json
{
  "mcpServers": {
    "plaidcloud-prod": { "url": "https://prod.plaid.cloud/mcp", "headers": { "Authorization": "Bearer …" } },
    "plaidcloud-dev":  { "url": "https://dev.plaid.cloud/mcp",  "headers": { "Authorization": "Bearer …" } }
  }
}
```
