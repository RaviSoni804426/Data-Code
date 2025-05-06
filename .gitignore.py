# update_gitignore.py

custom_rules = [
    "venv/",
    "__pycache__/",
    "*.pyc",
    "*.pyd",
    "*.egg",
    "Revision/",
    "envs/"  # Ignore Conda environments stored in a folder like ./envs/
]

default_rules = [
    "# Byte-compiled / optimized / DLL files",
    "*$py.class",

    "# Distribution / packaging",
    "build/",
    "dist/",
    "*.egg-info/",
    ".eggs/",

    "# Environment files",
    ".env",
    ".venv/",
    "env/",
    ".envrc",

    "# Jupyter",
    ".ipynb_checkpoints/",

    "# Logs",
    "*.log",

    "# OS",
    ".DS_Store",
    "Thumbs.db",

    "# VS Code",
    ".vscode/"
]

# Combine and deduplicate
ignore_rules = list(dict.fromkeys(custom_rules + default_rules))

gitignore_path = ".gitignore"

try:
    with open(gitignore_path, "r") as f:
        existing = set(line.strip() for line in f.readlines())
except FileNotFoundError:
    existing = set()

# Add new rules, skipping duplicates
new_rules = [rule for rule in ignore_rules if rule not in existing]

# Write new rules to .gitignore
with open(gitignore_path, "a") as f:
    if new_rules:
        f.write("\n# --- Updated ignore rules ---\n")
        for rule in new_rules:
            f.write(rule + "\n")

print(".gitignore has been updated successfully.")
