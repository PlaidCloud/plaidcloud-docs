---
title: Agents IA (MCP)
description: Connectez Claude, Cursor, GitHub Copilot, Gemini et d'autres agents IA à votre locataire PlaidCloud grâce au serveur Model Context Protocol (MCP).
sidebar:
  label: Agents IA (MCP)
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

PlaidCloud expose un serveur [Model Context Protocol](https://modelcontextprotocol.io) (MCP) sélectionné à l'adresse `/mcp` sur chaque espace de travail. Les agents IA s'y connectent comme à n'importe quel autre serveur MCP, puis appellent les outils pour lire des projets, exécuter des workflows, interroger des tables, gérer des dimensions, et plus encore.

Les pages de cette section décrivent ce que le serveur expose, comment s'authentifier et comment configurer pas à pas les clients IA les plus courants. Pour l'architecture qui les sous-tend (le chemin gouverné emprunté par chaque requête IA, le fonctionnement de la recherche d'information et la manière d'exécuter votre propre modèle), consultez [Architecture IA et LLM](/fr/integrations/ai-architecture/).

## Ce qui distingue l'analyse IA de PlaidCloud

- **[Des réponses fiables](./honest-answers/)** : chaque réponse s'accompagne d'un indicateur de confiance et de réserves en langage clair, et PlaidCloud n'invente jamais de chiffre. Cette honnêteté vous permet d'agir sur une réponse de l'IA sans la revérifier à la main.
- **[Retracer les allocations](./tracing-allocations/)** : demandez *pourquoi* un résultat alloué a changé, ce qui l'alimente et ce qu'aurait pour effet une modification hypothétique, en langage naturel.
- **[Chemins d'analyse](./analysis-paths/)** : donnez à vos tables clés des noms parlants et une valeur par défaut, pour pouvoir simplement demander « pourquoi cela a-t-il augmenté le trimestre dernier ? »
- **[Créer des tableaux de bord](./build-dashboards/)** : demandez des graphiques et des tableaux de bord à partir de vos tables et vues publiées, via la même connexion PlaidCloud.
- **[Définitions de métriques](./metric-definitions/)** : convenez une fois pour toutes de la façon dont un chiffre d'activité est calculé, pour que toutes les réponses qui l'utilisent le calculent de la même manière.

## Connecter votre assistant

Le moyen le plus rapide est le bouton **Connecter votre IA** de la barre d'outils de l'en-tête de PlaidCloud : choisissez votre client et suivez les étapes affichées, URL du serveur MCP comprise.

- [Premiers pas](./getting-started/) : ce que le serveur MCP expose et comment s'authentifier.
- [Microsoft 365 Copilot](/fr/integrations/microsoft-365-copilot/) : mettez PlaidCloud à la disposition de toute votre équipe dans Teams et Outlook.
- Configuration par client : [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/), [Grok](./grok/).
