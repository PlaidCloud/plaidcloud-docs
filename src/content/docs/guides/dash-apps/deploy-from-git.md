---
title: Deploy a Dash App From PlaidCloud Git
description: The end-to-end path to serve a Plotly Dash app in PlaidCloud — put your code in a PlaidCloud Git repository, connect it with a managed no-credentials connection, and publish it live.
sidebar:
  order: 1
---

This is the complete path from Dash app code on your machine to a live URL, using **[PlaidCloud Git](/guides/git/)** — the managed Git service built into your workspace — as the source. Because PlaidCloud Git is managed, the connection your app deploys from needs **no server URL, username, or token**: PlaidCloud authenticates on your behalf.

There are five steps:

1. Write a minimal Dash app.
2. Put it in a PlaidCloud Git repository.
3. Create a managed PlaidCloud Git connection.
4. Publish a Dash app that points at the repository.
5. Open the served app — and read the build logs if it doesn't start.

This walkthrough is nearly identical to [Deploy a Panel App From PlaidCloud Git](/guides/panel-apps/deploy-from-git/) — both are server-side Python apps built from Git and served the same way. The difference is the app code itself and one field in the publish dialog.

## Before You Start

- Open **Git** from your workspace to confirm you can reach PlaidCloud Git. By default, your workspace's organization includes an **`apps`** repository — the natural home for Dash apps too.
- Have `git` installed locally if you want to push code from your machine (you can also add files in the Git web UI).

## 1. Write a Minimal Dash App

Your app needs an **entry point** — a Python file that builds a Dash app and exposes its Flask server — and, optionally, a **`requirements.txt`** for extra packages, either at the repository root or next to your entry point.

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Create `app.py`:

```python
import plaidcloud_dash as pcd
from dash import Dash, Input, Output, html

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you

app.layout = html.Div(
    [
        html.H1("Hello from PlaidCloud Git"),
        html.P(id="whoami"),
        html.Button("Who am I?", id="whoami-btn", n_clicks=0),
    ]
)


@app.callback(Output("whoami", "children"), Input("whoami-btn", "n_clicks"))
def _whoami(n_clicks):
    if not n_clicks:
        return ""
    return f"Signed in as {pcd.current_user()!r}"


if __name__ == "__main__":
    app.run(debug=True)
```

That's a complete app. `dash`, `plotly`, `dash-mantine-components`, `dash-ag-grid`, and the PlaidCloud client libraries (`plaidcloud-rpc`, `plaidcloud-utilities`) are pre-installed, so list only *extra* packages in `requirements.txt`. Don't pass `requests_pathname_prefix` or `url_base_pathname` to `Dash(__name__)` — the platform sets the URL prefix through `DASH_URL_BASE_PATHNAME` automatically, and setting both throws a configuration error at startup. For the full app contract and the data-access helpers, see [the App Contract](/guides/dash-apps/#app-contract) and [Reading Data and the Signed-In User in a Dash App](/guides/dash-apps/accessing-data/).

## 2. Put Your App in a PlaidCloud Git Repository

Use your workspace's existing **`apps`** repository, or [create a new one](/guides/git/repositories/#create-a-repository). Then get your code into it.

Because you sign in through PlaidCloud, your Git account has no separate password — [generate a personal access token](/guides/git/repositories/#generate-a-personal-access-token) (**your avatar → Settings → Applications**) with repository **read** and **write** scopes, and use it as the password when Git prompts. Copy the repository's **HTTPS** clone URL from its **Code** button, then:

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

Note the repository path — `<org>/apps` — where `<org>` is your workspace's organization name. You'll enter that path in the next step. Full clone, commit, and push details are in [Repositories](/guides/git/repositories/).

> **The token here is only for *you* to push code.** The connection you create next is managed and needs no token — don't confuse the two.

## 3. Create a Managed PlaidCloud Git Connection

A **connection** tells a Dash deployment where its code lives. For PlaidCloud Git the connection is *managed* — PlaidCloud supplies the host and credentials, so you enter only the repository target. This is the same connection type a server Panel app uses.

1. Open **Tools > Connections**, click **New Connection**, and choose **PlaidCloud Git**.
2. Give the connection an **Account Name** (for example, `Apps Repo`).
3. Set **Repository Path** to `<org>/apps` — the path you noted in step 2 — and **Default Branch** to `main`. Leave **Start Path** blank unless your apps live in a subdirectory.
4. Click **Create**.

There is no Server URL, User, Password, or SSL/SSH field — PlaidCloud Git is managed, so the platform handles the host and authentication. For the complete form, including the connection's **Usage** and **Security Model** (who in the workspace may use it), see [PlaidCloud Git Connection](/guides/connections/plaidcloud-git/).

## 4. Publish the Dash App

Now point a Dash deployment at that connection.

1. Open **My Panel Apps** and click **New Dash App**.
2. Under **Directory Settings**, set an **App Name** and a **URL Slug** — the slug is the app's URL and internal name, so use lowercase letters, digits, and hyphens, starting with a letter, 40 characters or fewer (for example, `hello-dash`). An optional **Memo** describes the app.
3. Under **Git Connection and Publish Watcher**:
   - **Git Connection** — the PlaidCloud Git connection you created in step 3.
   - **Branch** — `main`. Pushes to this branch rebuild and redeploy the app automatically.
   - **Entry Point** — `app.py`.
4. Under **Runtime**, choose the **CPU**, **Memory**, and **Idle (minutes)** window. Tick **Allow Public Access** only if the app should be reachable without signing in. There's no **Design** setting — that's a Panel-specific option.
5. Under **Advanced (Embedded Serving)** — optional. Leave it empty unless you're embedding the app in another site.
6. Click **Publish**.

## 5. Open the App — and Read Logs if It Doesn't Start

After you publish, the app **builds**: PlaidCloud clones the branch, installs your `requirements.txt`, and builds a container image from the `platform-dash-base` image. Its **Status** shows in the **My Panel Apps** list and updates automatically.

- When Status is **Ready**, open the app at `https://<your-tenant-host>/serve/<slug>/`. The first request after it has been idle spins it up, showing a brief PlaidCloud loading screen while it does.
- If the build fails, open the app and check its **Build** logs — a missing dependency or an import error shows up there. See [Using a Dash App](/guides/dash-apps/using/) for what each status means, how to read logs, and how to trigger a rebuild.

From here on, **every push to the connection's branch rebuilds and redeploys the app automatically** — edit `app.py`, `git push`, and your change goes live. (Unless the app is **locked**, in which case pushes are skipped until you unlock it — see [Using a Dash App](/guides/dash-apps/using/#locking-an-app).)

## Next Steps

- [Reading Data and the Signed-In User in a Dash App](/guides/dash-apps/accessing-data/) — query PlaidCloud data as the person viewing the app.
- [Using a Dash App](/guides/dash-apps/using/) — build status, logs, locking, and removing the app.
- [PlaidCloud Git Connection](/guides/connections/plaidcloud-git/) — the full connection form, usage, and security model.
- [Repositories](/guides/git/repositories/) — branches, tokens, and collaborating in PlaidCloud Git.
