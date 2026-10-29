---
title: TASK_HISTORY (Lakehouse v1)
description: TASK_HISTORY — affiche l'historique d'exécution des tâches selon les variables fournies.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/17-table-functions/task-history.md
---

Affiche l'historique d'exécution des tâches selon les variables fournies.

## Syntaxe SQL
```sql
TASK_HISTORY(
      [ SCHEDULED_TIME_RANGE_START => <constant_expr> ]
      [, SCHEDULED_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <integer> ]
      [, TASK_NAME => '<string>' ]
      [, ERROR_ONLY => { TRUE | FALSE } ]
      [, ROOT_TASK_ID => '<string>'] )
```



## Arguments

Tous les arguments sont facultatifs.

`SCHEDULED_TIME_RANGE_START => <constant_expr>`, `SCHEDULED_TIME_RANGE_END => <constant_expr>`

Plage de temps (au format TIMESTAMP_LTZ), au cours des 7 derniers jours, pendant laquelle l'exécution de la tâche était planifiée. Si la plage de temps ne se situe pas dans les 7 derniers jours, une erreur est renvoyée.

* Si `SCHEDULED_TIME_RANGE_END` n'est pas spécifié, la fonction renvoie les tâches déjà terminées, en cours d'exécution ou planifiées dans le futur.
* Si `SCHEDULED_TIME_RANGE_END` vaut CURRENT_TIMESTAMP, la fonction renvoie les tâches déjà terminées ou en cours d'exécution. Notez qu'une tâche exécutée juste avant l'heure actuelle peut encore être identifiée comme planifiée.
* Pour n'interroger que les tâches déjà terminées ou en cours d'exécution, ajoutez `WHERE query_id IS NOT NULL` comme filtre. La colonne QUERY_ID de la sortie de TASK_HISTORY n'est renseignée que lorsqu'une tâche a commencé à s'exécuter.

Si aucune heure de début ni de fin n'est spécifiée, les tâches les plus récentes sont renvoyées, dans la limite de la valeur RESULT_LIMIT spécifiée.

`RESULT_LIMIT => <integer>`

Un nombre qui spécifie le nombre maximal de lignes renvoyées par la fonction.

Si le nombre de lignes correspondantes dépasse cette limite, les exécutions de tâches dont l'horodatage est le plus récent sont renvoyées, dans la limite spécifiée.

Plage : `1` à `10000`

Par défaut : `100`.

`TASK_NAME => <string>`

Une chaîne, insensible à la casse, qui spécifie une tâche. Seuls les noms de tâches non qualifiés sont pris en charge. Seules les exécutions de la tâche spécifiée sont renvoyées. Notez que si plusieurs tâches portent le même nom, la fonction renvoie l'historique de chacune de ces tâches.

`ERROR_ONLY => { TRUE | FALSE }`

Lorsque cet argument vaut TRUE, la fonction ne renvoie que les exécutions de tâches qui ont échoué ou ont été annulées.

`ROOT_TASK_ID => <string>`

Identifiant unique de la tâche racine d'un graphe de tâches. Cet ID correspond à la valeur de la colonne ID dans la sortie de SHOW TASKS pour la même tâche. Spécifiez ROOT_TASK_ID pour afficher l'historique de la tâche racine et de toutes les tâches enfants qui font partie du graphe de tâches.

## Notes d'utilisation
* Cette fonction renvoie au maximum 10 000 lignes, définies par la valeur de l'argument RESULT_LIMIT. La valeur par défaut est 100.
* Cette fonction ne renvoie de résultats que pour le rôle ACCOUNTADMIN.


## Exemples SQL

```sql
SELECT
  *
FROM TASK_HISTORY() order by scheduled_time;
```
La requête SQL ci-dessus récupère tous les enregistrements d'historique de tâches de la fonction TASK_HISTORY, triés par la colonne scheduled_time (10 000 au maximum).



```sql
SELECT *
  FROM TASK_HISTORY(
    SCHEDULED_TIME_RANGE_START=>TO_TIMESTAMP('2022-01-02T01:12:00-07:00'),
    SCHEDULED_TIME_RANGE_END=>TO_TIMESTAMP('2022-01-02T01:12:30-07:00'))
```

La requête SQL ci-dessus récupère tous les enregistrements d'historique de tâches de la fonction TASK_HISTORY dont la plage de temps planifiée commence à '2022-01-02T01:12:00-07:00' et se termine à '2022-01-02T01:12:30-07:00'. Elle renvoie donc les tâches dont l'exécution était planifiée dans cette fenêtre précise de 30 secondes. Le résultat inclut les détails des tâches qui correspondent à ces critères.
