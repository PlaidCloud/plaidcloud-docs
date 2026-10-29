---
title: Migrar flujos de trabajo de KNIME
description: Convierta un flujo de trabajo de KNIME (.knwf) o un grupo de flujos de trabajo (.knar) en flujos de trabajo avanzados de PlaidCloud desde la app Analyze, la API REST o un agente de IA conectado por MCP, vincule sus entradas y conexiones, y lea el informe de conversión.
sidebar:
  order: 31.7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/migrate-knime-workflows.md
---

PlaidCloud es un reemplazo directo de KNIME. El 98,5 % de las configuraciones de nodos de KNIME se convierte por completo, y 205 de los 207 tipos de nodos principales son Full: cada uno se convierte en pasos estándar del flujo de trabajo de PlaidCloud que realizan el trabajo del nodo. El convertidor transforma un archivo de flujo de trabajo de KNIME en flujos de trabajo avanzados ejecutables, conserva el grafo original y devuelve un informe de conversión que indica todo lo que usted debe configurar. La [matriz de conversión de KNIME](/es/reference/knime-conversion-matrix/) enumera todos los nodos.

La conversión solo lee el archivo que usted indica. Nunca se conecta al sistema del que un nodo de KNIME lee o en el que escribe.

La conversión es un paso único. Si convierte el mismo archivo de nuevo, se crean flujos de trabajo nuevos, y las modificaciones que haya hecho en PlaidCloud nunca se combinan con una exportación posterior.

## Qué crea PlaidCloud

- Un flujo de trabajo avanzado por cada flujo de trabajo de KNIME. Un `.knwf` genera un flujo de trabajo y un `.knar` genera uno por cada flujo de trabajo del grupo.
- Cada nodo de KNIME se convierte en el paso, la variable de proyecto o el objeto de lienzo equivalente, con las relaciones ascendentes y descendentes conservadas. Los metanodos y los componentes se aplanan dentro del flujo de trabajo, de modo que sus nodos se ejecutan como pasos normales.
- Las variables de flujo y los nodos Configuration y Widget se convierten en variables de proyecto que contienen sus valores predeterminados. Los conmutadores y los bucles cuyos valores se conocen al convertir se podan y se expanden en los pasos que ejecutan.
- Los lenguajes de expresiones de KNIME (Expression, String Manipulation, Math Formula, Column Expressions y Rule Engine) se convierten en expresiones de PlaidCloud.
- Los archivos de datos incluidos en el archivo comprimido se cargan en una carpeta `knime/` de la cuenta de documentos predeterminada del proyecto, una carpeta por flujo de trabajo, y los lectores convertidos los importan desde allí.
- Las vistas, los gráficos y los administradores de color no tienen efecto sobre los datos. Se descartan y se enumeran en el informe de conversión.

## Antes de empezar

1. Exporte el flujo de trabajo desde KNIME Analytics Platform como un archivo `.knwf`. Para convertir varios flujos de trabajo a la vez, exporte su grupo de flujos de trabajo como un archivo `.knar`. Guarde los archivos que usan sus lectores en la carpeta `data` del flujo de trabajo para que viajen dentro del archivo comprimido.
2. Cargue el archivo comprimido en una [cuenta de documentos](/es/guides/documents/adding-accounts/) que usted pueda leer. En la app Analyze, **Examinar** en la ventana de importación lo carga desde su computadora.
3. Elija el proyecto de PlaidCloud que recibirá los flujos de trabajo. Debe ser Arquitecto o Gerente del proyecto, y el proyecto debe tener una cuenta de documentos predeterminada.
4. Anote las tablas, los archivos y las conexiones de PlaidCloud que desea que usen los lectores y los nodos conectores del flujo de trabajo. Consulte [Vincular orígenes](#vincular-orígenes).

## Convertir un flujo de trabajo

Convierta desde la app Analyze, la API REST o un agente de IA conectado por MCP. La API REST y la herramienta MCP aceptan los mismos campos; la ventana acepta los que muestra.

### App Analyze

1. Abra **Analyze** y elija **Tools → Importar flujo de trabajo de KNIME**.
2. En **Importar origen y destino**, elija el **Proyecto de destino** y el **Archivo KNIME (.knwf o .knar)** en una cuenta de documentos. Seleccione **Examinar** para cargar el archivo desde su computadora.
3. En **Prefijos de objetos**, puede definir el **Prefijo del flujo de trabajo**, el **Prefijo del paso** y el **Prefijo de tabla**. El prefijo de tabla es, de forma predeterminada, el nombre del flujo de trabajo.
4. En **Vínculos de origen (opcional)**, puede vincular un lector a una tabla existente del proyecto de destino: seleccione **Agregar** e introduzca el **Lector de KNIME** (su id de nodo, como `12:3`, el nombre del nodo o el nombre del archivo) y el **ID de la tabla**. Para vincular conexiones, documentos o tablas de otros proyectos, use la API REST o la herramienta MCP. Consulte [Vincular orígenes](#vincular-orígenes).
5. Seleccione **Importar**.

La ventana muestra el progreso mientras convierte el archivo comprimido y, después, el informe de conversión: los recuentos de pasos (**Pasos**, **Confianza alta**, **Media**, **Baja** y **No convertidos**), los nodos que no se pudieron convertir y los pasos posteriores a ellos, las conversiones parciales, las advertencias, los archivos de origen que se deben cargar y los nodos sin paso. Si una conversión no tiene nada que revisar, la ventana lo indica y se cierra sola.

### Campos

| Campo | Obligatorio | Qué hace |
| --- | --- | --- |
| `source_account_id` | Sí | Cuenta de documentos que contiene el archivo de KNIME. |
| `source_file_path` | Sí | Ruta del archivo `.knwf` o `.knar` dentro de esa cuenta. |
| `project_id` | Sí | Proyecto en el que se crean los flujos de trabajo. |
| `workflow_prefix` | No | Prefijo que se agrega a los nombres de los flujos de trabajo. |
| `step_prefix` | No | Prefijo que se agrega a los nombres de los pasos. |
| `table_prefix` | No | Prefijo que se agrega a los nombres de las tablas. De forma predeterminada es el nombre del propio flujo de trabajo. Un prefijo que reutilizaría el nombre de una tabla existente se rechaza antes de crear nada. En un `.knar`, el prefijo de cada flujo de trabajo va seguido del nombre de ese flujo de trabajo. |
| `source_bindings` | No | Vincula lectores y nodos conectores a datos y conexiones que usted ya tiene, hasta 500 entradas. Consulte [Vincular orígenes](#vincular-orígenes). |

### REST

Envíe los campos como cuerpo JSON a:

```text
POST /rest/v1/analyze/knime/convert
```

```json
{
  "source_account_id": "<document account id>",
  "source_file_path": "/knime/monthly-close.knwf",
  "project_id": "<project id>"
}
```

### MCP

Un agente de IA conectado por MCP llama a la herramienta `knime_convert` con los mismos campos. Consulte [Agentes de IA (MCP)](/es/integrations/ai-coding-agents/) para conectar un agente. La herramienta modifica su proyecto, por lo que debe revisar la llamada antes de aprobarla.

## Vincular orígenes

Use `source_bindings` para que un lector de KNIME apunte a datos que ya existen en PlaidCloud en lugar de a la copia incluida en el archivo comprimido. Una clave es un id de nodo (como `12:3`), un nombre de nodo, una ruta de archivo incluido (como `data/sales.csv`) o un nombre de archivo; gana la primera coincidencia en ese orden. Un valor es uno de los siguientes:

- Un id `analyzetable_` de una tabla del proyecto de destino. La tabla reemplaza al lector.
- `{"project": "<project id>", "table": "<table id>"}` para una tabla de otro proyecto que usted pueda leer. El lector se convierte en un paso [Import Project Table](/es/reference/workflow-steps/import/import-project-table/) que la copia. El proyecto de origen debe compartir Lectura con el proyecto de destino; de lo contrario, el paso muestra una advertencia. Una tabla regida por acceso a filas se rechaza.
- `{"account": "<document account id>", "path": "/finance/budget.xlsx"}` para un documento que usted pueda leer. El lector lo importa.
- `{"connection": "<connection id>"}` para un nodo conector de base de datos o REST. Los pasos convertidos se ejecutan en esa conexión.

La ventana de la app Analyze vincula lectores a tablas del proyecto de destino mediante el id de tabla. Vincule conexiones, documentos y tablas de otros proyectos mediante la API REST o la herramienta MCP.

```json
"source_bindings": {
  "Sales": "analyzetable_1234",
  "data/budget.xlsx": { "account": "<document account id>", "path": "/finance/budget.xlsx" }
}
```

Una tabla vinculada que no existe, o una clave que no coincide con ningún lector, genera una advertencia. Los vínculos aplicados, con los nombres de su proyecto y de su tabla, se enumeran en el informe de conversión bajo `bindings`.

### Entradas sin vincular

Un lector cuyo archivo no está en el archivo comprimido lee desde `inputs/<file name>` en la carpeta del flujo de trabajo de la cuenta de documentos predeterminada, y el informe de conversión enumera la ruta bajo `missing_inputs` con una advertencia. Cargue el archivo allí y ejecute el flujo de trabajo. Mientras el archivo no esté allí, la importación termina con una advertencia y crea una tabla vacía, y el flujo de trabajo continúa.

## Credenciales y conexiones

Las credenciales de KNIME nunca se migran. Cada paso que inicia sesión en otro sistema lee sus credenciales de una conexión de PlaidCloud o de una variable de proyecto que usted configura, y la advertencia del paso en el informe de conversión indica cuál.

| KNIME | Qué debe configurar |
| --- | --- |
| Conectores de base de datos | Una conexión de base de datos: vincúlela con `{"connection": "<id>"}` o selecciónela en el paso. |
| Nodos REST y de servicios web que inician sesión | Una [conexión REST](/es/reference/connectors/rest/generic-rest/): vincúlela con `{"connection": "<id>"}` o selecciónela en el paso. |
| Speech Recognizer (IBM Watson) | Una conexión REST cuya URL base es la URL del servicio Watson que indica la advertencia, con el usuario `apikey` y su clave de API como inicio de sesión básico. Vincúlela al nodo. |
| Email Connector, con Email Reader o Email Mover | Una variable de proyecto que contenga la contraseña del servidor de correo, con el nombre que indica la advertencia. El host y el usuario provienen de Email Connector. |
| Excel Reader o Excel Writer con contraseña de libro | Una variable de proyecto que contenga la contraseña, con el nombre que indica la advertencia. |
| Conectores y autenticadores de LLM | Una conexión de LLM en el paso de IA. |

Consulte [Administrar variables del flujo de trabajo](/es/guides/workflows/manage-workflow-variables/) para configurar variables de proyecto.

## Leer el informe de conversión

La ventana de la app Analyze muestra el informe de conversión cuando termina la importación, y las respuestas de REST y MCP lo incluyen. Léalo antes de ejecutar los flujos de trabajo.

- `summary` cuenta los pasos creados y cuántos se asignaron con confianza alta, media o baja.
- `warnings` enumera cada advertencia con su nodo, su paso y la acción que se debe realizar, incluidas todas las credenciales o conexiones que se deben configurar.
- `missing_inputs` enumera las rutas de Documentos en las que se deben cargar los archivos de las entradas sin vincular.
- `bindings` enumera los vínculos aplicados.
- `table_prefix` es el prefijo utilizado. En un `.knar`, `workflows` enumera cada flujo de trabajo con su propio prefijo.
- `uploaded_files`, junto al informe, enumera los archivos incluidos que se cargaron en la cuenta de documentos predeterminada.
- `dropped_tools` enumera las vistas y los gráficos que se descartaron.

## Marcadores de posición

Un nodo sin ruta de conversión permanece en el lienzo como un marcador de posición con nombre. El marcador de posición transmite sus datos sin cambios y emite una advertencia con el nombre del nodo de KNIME, y todos los pasos posteriores a él se marcan en el informe, de modo que un resultado ausente nunca pasa inadvertido. Reconstruya la capacidad con un paso estándar cuando su resultado importe.

## Ejecutar el flujo de trabajo convertido

1. Abra el nuevo flujo de trabajo en el proyecto.
2. Configure las variables de proyecto y las conexiones que indican las advertencias.
3. Cargue los archivos de las entradas sin vincular en las rutas indicadas en **Archivos de origen que se deben cargar** en la ventana, o en `missing_inputs`.
4. [Ejecute el flujo de trabajo](/es/guides/workflows/run-a-workflow/) y revise la tabla de salida de cada paso.

## Casos límite

Estas son las únicas diferencias conocidas respecto de KNIME.

- **Crosstab.** Se convierte en el paso [Table: Pivot](/es/reference/workflow-steps/tables/table-pivot/). Algunas combinaciones de configuración dan resultados que difieren de los de KNIME.
- **Loop End (Column Append).** Se convierte en el paso [Table: Inner Join](/es/reference/workflow-steps/tables/table-inner-join/). Algunas combinaciones de configuración dan resultados que difieren de los de KNIME.
- **Selecciones aleatorias.** Row Sampler, Table Partitioner y Equal Size Sampling realizan la selección aleatoria propia de KNIME con el paso [Table: KNIME Random Sample](/es/reference/workflow-steps/tables/table-knime-random-sample/), de modo que un nodo con una semilla selecciona las mismas filas que en KNIME. La selección admite una tabla de como máximo 10 000 000 de filas; una tabla más grande hace fallar el paso.

## Guías relacionadas

- [Matriz de conversión de KNIME](/es/reference/knime-conversion-matrix/)
- [Conexión REST](/es/reference/connectors/rest/generic-rest/)
- [Agregar cuentas de documentos](/es/guides/documents/adding-accounts/)
- [Administrar variables del flujo de trabajo](/es/guides/workflows/manage-workflow-variables/)
- [Ejecutar un flujo de trabajo](/es/guides/workflows/run-a-workflow/)
