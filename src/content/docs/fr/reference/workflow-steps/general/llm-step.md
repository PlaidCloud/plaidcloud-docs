---
title: Étape LLM
description: Exécutez une invite sur un LLM avec un accès délimité en lecture et/ou en écriture aux données du projet, le modèle écrivant directement ses résultats via le serveur MCP.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/llm-step.md
---

## Description

L'**Étape LLM** envoie une invite à un grand modèle de langage. Avec une connexion LLM Anthropic, le modèle obtient un accès délimité aux tables, dimensions et documents du projet que vous liez — **Lecture**, **Écriture** ou les deux pour chaque objet — et écrit ses résultats directement dans les liaisons dotées de l'accès en écriture. Une liaison en écriture constitue la sortie de l'étape ; il n'existe pas de format de sortie distinct.

Pour une présentation complète, consultez le [guide de l'Étape LLM](/fr/guides/workflows/llm-step/).

## Configuration

* **Connexion LLM** *(obligatoire)* — une connexion de type LLM (par exemple, Anthropic). Son **Accès de l'agent** doit être **Lecture et écriture** pour toute liaison en écriture. **Complet** autorise aussi les écritures jusqu'à sa suppression le 15 janvier 2027, et une étape qui l'utilise consigne un avertissement à la fin de son exécution. Avec **Lecture et écriture**, une étape n'écrit que dans les liaisons dont **Écriture** est coché, et ne peut ni exécuter de SQL qui écrit ni créer de tables.
* **Modèle** *(facultatif)* — par défaut, le modèle par défaut de la connexion. Tout modèle Claude fonctionne avec une connexion Anthropic, y compris les modèles plus anciens tels que Claude Sonnet 4.5.
* **Invite** *(obligatoire)* — prend en charge les références `{{tables.NAME}}`, `{{dimensions.NAME}}` et `{{documents.NAME}}` aux objets liés.
* **Result schema** *(facultatif pour Anthropic ; obligatoire pour les autres fournisseurs)* — un **Schéma JSON** (racine `"type": "object"`) pour un résumé structuré capturé ; avec Anthropic, laissez vide lorsque le travail du modèle consiste en ses écritures MCP. Les fournisseurs autres qu'Anthropic n'ont pas d'accès MCP : un schéma est donc obligatoire.
* **Bindings** — les tables, dimensions et documents auxquels le modèle peut accéder, chacun choisi avec un sélecteur et doté de **Lecture** et/ou d'**Écriture**. Les tables en écriture reçoivent des lignes insérées, les dimensions en écriture reçoivent des nœuds, les documents en écriture reçoivent des fichiers téléversés.
* **Limites** — Nombre maximal de jetons de sortie (de 1 024 à 128 000) et Credential TTL (de 60 à 3 600 secondes).

## Comportement

* L'appel au modèle s'exécute dans sa propre tâche. Un identifiant éphémère à portée limitée est généré pour l'exécution et révoqué à sa fin.
* L'accès est contrôlé par objet et par case à cocher : le modèle ne lit que les objets liés en lecture et n'écrit que dans ceux liés en écriture — jamais dans un objet que vous n'avez pas lié. L'écriture exige un objet de destination existant ; l'étape n'en crée pas.
* Chaque exécution effectue un appel facturable au fournisseur et écrit dans vos objets liés.

## Contrôles à l'enregistrement

* **Result schema** — lorsque vous en fournissez un, il doit être du JSON valide, un objet JSON, et déclarer `"type": "object"` à sa racine. Sinon, l'enregistrement est refusé, par exemple avec *The result schema must declare "type": "object" at its root.*
* **Bindings et connexion** — seule une connexion Anthropic donne au modèle l'accès aux liaisons. L'enregistrement d'une étape dont les liaisons reposent sur la connexion d'un autre fournisseur est refusé, avec un message qui nomme le fournisseur et vous invite à *Remove the bindings or choose an Anthropic connection.* Une liaison dont **Écriture** est coché exige une connexion dont l'**Accès de l'agent** autorise les écritures. Sur une connexion en lecture seule, l'enregistrement est refusé avec *The selected LLM connection has Read-only Agent Access, so a binding with Write checked could not write. Set the connection to 'Read & write' or uncheck Write on the bindings.* Une étape enregistrée via l'API sans connexion est vérifiée par rapport à la connexion LLM par défaut de l'espace de travail, sur laquelle elle s'exécute aussi : celle qu'un administrateur a marquée comme connexion par défaut, sinon la plus récemment mise à jour. En l'absence de connexion par défaut marquée par un administrateur, la modification d'une autre connexion LLM en fait la connexion par défaut et peut faire refuser le prochain enregistrement de l'étape.
