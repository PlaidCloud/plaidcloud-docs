"""Convert all H2/H3/H4/H5/H6 headings to Title Case.

Rules:
- Capitalize first and last word always.
- Capitalize all words 4+ letters.
- Keep these short words lowercase (unless first/last):
    a, an, the, and, but, or, nor, for, so, yet,
    a, at, by, in, of, on, to, up, via, off, out, per, vs
- Preserve hard-coded capitalization for acronyms/products.
- Don't touch headings inside code fences (```).
- Front matter is preserved as-is.
"""
import re
from pathlib import Path

SMALL_WORDS = {
    "a", "an", "the",
    "and", "but", "or", "nor", "for", "so", "yet",
    "at", "by", "in", "of", "on", "to", "up", "via", "off", "out", "per", "vs", "v",
    "is", "as", "if",  # debatable but commonly lowercase in title case
}

# Words/acronyms with locked capitalization — these override the title-case logic.
LOCKED = {
    # acronyms
    "sql": "SQL", "api": "API", "rest": "REST", "json": "JSON", "xml": "XML",
    "html": "HTML", "css": "CSS", "js": "JS", "csv": "CSV", "tsv": "TSV",
    "yaml": "YAML", "yml": "YML", "hdf": "HDF", "pdf": "PDF",
    "oauth": "OAuth", "oauth2": "OAuth2", "ssl": "SSL", "tls": "TLS",
    "ssh": "SSH", "sso": "SSO", "iam": "IAM", "saml": "SAML", "mfa": "MFA",
    "rpc": "RPC", "ipc": "IPC", "cli": "CLI", "ui": "UI", "ux": "UX",
    "ip": "IP", "dns": "DNS", "url": "URL", "uri": "URI",
    "vpn": "VPN", "tcp": "TCP", "udp": "UDP", "http": "HTTP", "https": "HTTPS",
    "io": "IO", "id": "ID", "ids": "IDs",
    "aws": "AWS", "gcp": "GCP", "gcs": "GCS", "s3": "S3", "rds": "RDS",
    "ec2": "EC2", "iam": "IAM",
    "mcp": "MCP", "etl": "ETL", "elt": "ELT", "olap": "OLAP", "oltp": "OLTP",
    # product/brand names
    "plaidcloud": "PlaidCloud", "plaidlink": "PlaidLink", "plaidxl": "PlaidXL",
    "github": "GitHub", "gitlab": "GitLab", "bitbucket": "Bitbucket",
    "github's": "GitHub's",
    "postgres": "PostgreSQL", "postgresql": "PostgreSQL",
    "mysql": "MySQL", "mariadb": "MariaDB",
    "snowflake": "Snowflake", "databricks": "Databricks",
    "databend": "Databend", "starrocks": "StarRocks", "presto": "Presto", "trino": "Trino",
    "redshift": "Redshift", "bigquery": "BigQuery", "athena": "Athena",
    "ibm": "IBM", "db2": "DB2",
    "sap": "SAP", "hana": "HANA",
    "oracle": "Oracle", "salesforce": "Salesforce", "stripe": "Stripe",
    "slack": "Slack", "teams": "Teams", "microsoft": "Microsoft",
    "google": "Google", "amazon": "Amazon", "azure": "Azure",
    "ai": "AI",  # title-case-ify but uppercase
    "macos": "macOS", "ios": "iOS",
    "kubernetes": "Kubernetes", "docker": "Docker",
    "python": "Python", "pyspark": "PySpark", "javascript": "JavaScript",
    "node.js": "Node.js", "react": "React",
    "saas": "SaaS", "paas": "PaaS", "iaas": "IaaS",
    # special
    "i": "I",
    "i'm": "I'm", "i'll": "I'll", "i've": "I've",
    "you'll": "You'll", "you're": "You're", "you've": "You've",
    "won't": "Won't", "can't": "Can't", "don't": "Don't",
    "let's": "Let's",
    "what's": "What's", "where's": "Where's", "when's": "When's",
    "it's": "It's", "that's": "That's",
}


def cap_word(word: str, is_first_or_last: bool) -> str:
    if not word:
        return word
    low = word.lower()
    # Locked words
    if low in LOCKED:
        return LOCKED[low]
    # Small words stay lowercase unless first/last
    if low in SMALL_WORDS and not is_first_or_last:
        return low
    # Preserve all-caps acronyms already in the original (e.g., 'SSH' in source)
    if word.isupper() and len(word) >= 2:
        return word
    # Standard title-case
    # Handle hyphens (Title-Cased)
    if "-" in word:
        parts = word.split("-")
        return "-".join(cap_word(p, is_first_or_last) if i == 0 else cap_word(p, False)
                        for i, p in enumerate(parts))
    return word[0].upper() + word[1:].lower() if len(word) > 1 else word.upper()


def title_case(text: str) -> str:
    # Split on whitespace; preserve original whitespace
    tokens = re.findall(r"\S+|\s+", text)
    word_indices = [i for i, t in enumerate(tokens) if not t.isspace()]
    if not word_indices:
        return text
    first_word = word_indices[0]
    last_word = word_indices[-1]
    out = []
    for i, t in enumerate(tokens):
        if t.isspace():
            out.append(t)
        else:
            is_first_or_last = (i == first_word) or (i == last_word)
            out.append(cap_word(t, is_first_or_last))
    return "".join(out)


HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$", re.MULTILINE)


def convert_file(path: Path) -> int:
    text = path.read_text()
    # Don't touch headings inside fenced code blocks
    lines = text.split("\n")
    in_fence = False
    fixes = 0
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{2,6})\s+(.+?)\s*$", line)
        if not m:
            continue
        hashes, heading = m.group(1), m.group(2)
        new_heading = title_case(heading)
        if new_heading != heading:
            lines[i] = f"{hashes} {new_heading}"
            fixes += 1
    if fixes:
        path.write_text("\n".join(lines))
    return fixes


def main():
    docs = Path("src/content/docs")
    total_files = 0
    total_fixes = 0
    for f in list(docs.rglob("*.md")) + list(docs.rglob("*.mdx")):
        n = convert_file(f)
        if n:
            total_files += 1
            total_fixes += n
    print(f"Files touched: {total_files}")
    print(f"Headings rewritten: {total_fixes}")


if __name__ == "__main__":
    main()
