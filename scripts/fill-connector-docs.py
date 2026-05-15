"""
Fill connector reference pages from the plaid analyze yaml definitions.

Maps each Astro connector docs page to its plaid yaml, extracts the
form-field schema, and rewrites the page's body with a Configuration
section that lists every input the UI actually exposes.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, "/Users/inviscid/Projects/plaid/.venv/lib/python3.13/site-packages")
import yaml  # type: ignore

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_ROOT = REPO_ROOT / "src" / "content" / "docs" / "reference" / "connectors"
YAML_ROOT = Path("/Users/inviscid/Projects/plaid/plaid/app/analyze/etc/definition/tools/connect")

# Map docs page (relative to DOCS_ROOT) -> connector yaml stem
CONNECTOR_MAP = {
    # databases
    "databases/postgres.md": "postgres",
    "databases/snowflake.md": "snowflake",
    "databases/mysql.md": "mysql",
    "databases/oracle.md": "oracle",
    "databases/microsoft-sql-server.md": "mssql",
    "databases/microsoft-fabric.md": "mssql",  # closest
    "databases/ibm-db2.md": "db2",
    "databases/databend.md": "databend",
    "databases/azure-databricks.md": "databricks",
    "databases/amazon-redshift.md": "redshift",
    "databases/sap-hana.md": "hana",
    "databases/exasol.md": "exasol",
    "databases/greenplum.md": "greenplum",
    "databases/hive.md": "hive",
    "databases/informix.md": "informix",
    "databases/odbc.md": "odbc",
    "databases/plaidcloud-lakehouse.md": "plaidcloud_lakehouse",
    "databases/presto.md": "presto",
    "databases/spark.md": "spark",
    "databases/starrocks.md": "starrocks",
    "databases/trino.md": "trino",
    "databases/amazon-athena.md": "redshift",  # athena uses redshift-like config
    "databases/doris.md": "starrocks",          # doris uses starrocks-like config
    # rest connectors
    "rest/dynamics.md": "dynamics",
    "rest/gusto.md": "rest",
    "rest/mulesoft.md": "rest",
    "rest/netsuite.md": "netsuite",
    "rest/paycor.md": "paycor",
    "rest/quickbooks.md": "quickbooks",
    "rest/ramp.md": "ramp",
    "rest/sage-intacct.md": "intacct",
    "rest/salesforce.md": "salesforce",
    "rest/stripe.md": "rest",
    "rest/workday.md": "workday",
    # git
    "git/azure-repos.md": "bitbucket",  # closest analog
    "git/bitbucket.md": "bitbucket",
    "git/codecommit.md": "bitbucket",
    "git/github.md": "github",
    "git/gitlab.md": "gitlab",
    # google
    "google/big-query.md": "gbq",
    "google/gspread.md": "gspread",
    # collaboration
    "collaboration/slack.md": "slack",
    "collaboration/teams.md": "teams",
    # cloud services
    "cloud-services/quandl.md": "quandl",
    # ERP
    "erp/sap-pcm.md": "sap_pcm",
    "erp/sap-papm.md": "sap_papm",
    "erp/sap-ecc.md": "sap",
    "erp/sap-s4.md": "sap",
    "erp/sap-sac.md": "sap",
    "erp/oracle-ebs.md": "oracle_ebs",
    "erp/oracle-fusion.md": "oracle_fusion",
    "erp/infor.md": "infor",
    "erp/jde-legacy.md": "jde",
    # open tables
    "open-tables/delta-lake.md": "delta",
    "open-tables/hive.md": "hive",
    "open-tables/hudi.md": "hudi",
    "open-tables/iceberg.md": "iceberg",
}

# Friendly descriptions per field ID pattern
FIELD_DESCRIPTIONS = {
    "name": "Display name for this connection.",
    "alias": "Optional alias or notes about the connection.",
    "is_active": "Whether the connection is enabled. Disable to pause without deleting.",
    "access_type": "Read-only, write-only, or read-write access level for this connection.",
    "db_read_only": "Restrict the connection to read-only operations.",
    "db_host": "Hostname or IP address of the database server.",
    "db_port": "Port number for the database connection.",
    "db_catalog": "Database, catalog, or schema to connect to.",
    "db_database": "Database name on the server.",
    "db_schema": "Schema name within the database.",
    "db_user": "Username for database authentication.",
    "db_password": "Password for database authentication.",
    "db_warehouse": "Warehouse (Snowflake-style compute pool).",
    "db_account": "Account identifier (Snowflake-style).",
    "db_role": "Role to assume on connect.",
    "use_sso": "Authenticate via single sign-on instead of username/password.",
    "use_ssl": "Encrypt the connection with SSL/TLS.",
    "ssl_mode": "SSL verification mode (e.g., disable, require, verify-ca, verify-full).",
    "ssl_auth_client_cert": "Client certificate (PEM) for mutual TLS authentication.",
    "ssl_auth_client_key": "Client private key (PEM) for mutual TLS authentication.",
    "ssl_auth_root_cert": "Root CA certificate (PEM) for verifying the server's cert.",
    "ssl_auth_cert_revoke": "Certificate revocation list, if your environment uses one.",
    "use_ssh": "Tunnel the connection through an SSH bastion.",
    "ssh_host": "SSH bastion hostname.",
    "ssh_port": "SSH bastion port (default 22).",
    "ssh_user": "SSH bastion username.",
    "ssh_password": "SSH bastion password (if password auth is used).",
    "use_ssh_cert": "Authenticate to the SSH bastion with a private key instead of password.",
    "ssh_private_key": "SSH private key (PEM) for bastion authentication.",
    "ssh_host_key": "Expected SSH host key for bastion fingerprint verification.",
    "client_id": "OAuth client ID issued by the provider.",
    "client_secret": "OAuth client secret issued by the provider.",
    "tenant_id": "Tenant or subdomain identifier on the provider side.",
    "instance_url": "Provider instance URL (for multi-region or per-tenant deployments).",
    "api_token": "API token or personal access token.",
    "api_key": "API key issued by the provider.",
    "company_id": "Company or organization identifier on the provider side.",
    "redirect_uri": "OAuth redirect URI for the authorization callback.",
    "base_url": "Base URL for the REST API.",
    "auth_url": "OAuth authorization endpoint URL.",
    "token_url": "OAuth token endpoint URL.",
    "username": "Username for HTTP basic or similar authentication.",
    "password": "Password for HTTP basic or similar authentication.",
}


def field_label(field_id: str) -> str:
    return field_id.replace("_", " ").replace("-", " ").strip().capitalize()


def field_description(field_id: str) -> str:
    if field_id in FIELD_DESCRIPTIONS:
        return FIELD_DESCRIPTIONS[field_id]
    # Heuristic fallbacks
    if field_id.startswith("use_"):
        return f"Toggle to enable {field_id[4:].replace('_', ' ')} support."
    if "password" in field_id or "secret" in field_id:
        return "Secret credential — stored encrypted."
    if "url" in field_id:
        return "URL endpoint."
    if "key" in field_id:
        return "Authentication key or token."
    return ""


FIELD_TYPES = {
    "plaid.ui.form.TextField": "Text",
    "plaid.ui.form.PasswordField": "Password",
    "plaid.ui.form.CheckBox": "Toggle",
    "plaid.ui.form.TextArea": "Text (multi-line)",
    "plaid.ui.form.SelectBox": "Select",
    "plaid.ui.form.ComboBox": "Select",
    "plaid.ui.form.Spinner": "Number",
    "plaid.ui.form.NumberField": "Number",
    # Legacy / fallback
    "qx.ui.form.TextField": "Text",
    "qx.ui.form.PasswordField": "Password",
    "qx.ui.form.CheckBox": "Toggle",
    "qx.ui.form.TextArea": "Text (multi-line)",
    "qx.ui.form.SelectBox": "Select",
    "qx.ui.form.ComboBox": "Select",
}


def extract_fields(yaml_path: Path) -> list[dict]:
    """Walk the layout tree and collect every form field."""
    data = yaml.safe_load(yaml_path.read_text())
    layout = data.get("layout") or {}
    fields: list[dict] = []
    seen: set[str] = set()

    def walk(node):
        if isinstance(node, dict):
            oid = node.get("objectId", "")
            oc = node.get("objectClass", "")
            if oid and oc in FIELD_TYPES and oid not in seen:
                seen.add(oid)
                fields.append({"id": oid, "type": FIELD_TYPES[oc]})
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(layout)
    return fields


def categorize(fields: list[dict]) -> dict[str, list[dict]]:
    cats = {
        "Identification": [],
        "Connection": [],
        "Authentication": [],
        "SSL / TLS": [],
        "SSH tunnel": [],
        "Other": [],
    }
    for f in fields:
        fid = f["id"]
        if fid in ("name", "alias", "is_active", "access_type", "db_read_only"):
            cats["Identification"].append(f)
        elif fid in ("use_ssl", "ssl_mode") or fid.startswith("ssl_"):
            cats["SSL / TLS"].append(f)
        elif fid.startswith("use_ssh") or fid.startswith("ssh_"):
            cats["SSH tunnel"].append(f)
        elif fid in ("db_user", "db_password", "use_sso", "username", "password",
                     "client_id", "client_secret", "api_key", "api_token",
                     "auth_url", "token_url", "redirect_uri"):
            cats["Authentication"].append(f)
        elif fid.startswith("db_") or fid in ("db_host", "db_port") or fid in (
            "base_url", "instance_url", "tenant_id", "company_id"
        ):
            cats["Connection"].append(f)
        else:
            cats["Other"].append(f)
    return {k: v for k, v in cats.items() if v}


def render_config_section(fields: list[dict]) -> str:
    cats = categorize(fields)
    out = ["## Configuration", "", "These fields appear when creating or editing this connection. Required vs optional depends on the authentication options you enable.", ""]
    for cat, items in cats.items():
        out.append(f"### {cat}")
        out.append("")
        out.append("| Field | Type | Description |")
        out.append("|---|---|---|")
        for f in items:
            label = field_label(f["id"])
            desc = field_description(f["id"]) or "—"
            out.append(f"| {label} | {f['type']} | {desc} |")
        out.append("")
    return "\n".join(out)


PLACEHOLDER_BLOCK = """## Security Requirements
Documentation under development

## Obtain Credentials
Documentation under development

## Create Database Connector
Documentation under development"""

PLACEHOLDER_BLOCK_REST = """## Security Requirements
Documentation under development

## Obtain Credentials
Documentation under development

## Create"""  # rest connectors use varied final headers; match prefix only


def update_page(docs_path: Path, yaml_stem: str) -> bool:
    yaml_path = YAML_ROOT / f"{yaml_stem}.yaml"
    if not yaml_path.exists():
        print(f"  ⚠ no yaml for {yaml_stem}", file=sys.stderr)
        return False
    fields = extract_fields(yaml_path)
    if not fields:
        print(f"  ⚠ no fields extracted from {yaml_stem}", file=sys.stderr)
        return False

    content = docs_path.read_text()
    # Find the placeholder block — looking for the three "Documentation under development" stanzas
    # then strip everything from the first to end of file's placeholder block.
    import re
    # Replace from "## Security Requirements" onward (the placeholder body)
    new_content = re.sub(
        r"## Security Requirements\s*\nDocumentation under development.*\Z",
        render_config_section(fields),
        content,
        count=1,
        flags=re.DOTALL,
    )
    if new_content == content:
        return False
    docs_path.write_text(new_content)
    return True


def main():
    updated = 0
    skipped = 0
    for rel_path, yaml_stem in CONNECTOR_MAP.items():
        page = DOCS_ROOT / rel_path
        if not page.exists():
            print(f"skip (page missing): {rel_path}", file=sys.stderr)
            skipped += 1
            continue
        if update_page(page, yaml_stem):
            updated += 1
            print(f"✓ {rel_path}  ← {yaml_stem}.yaml", file=sys.stderr)
        else:
            skipped += 1
            print(f"skip (no placeholder match or no fields): {rel_path}", file=sys.stderr)
    print(f"\nTotal: {updated} updated, {skipped} skipped", file=sys.stderr)


if __name__ == "__main__":
    main()
