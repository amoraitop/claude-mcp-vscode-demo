# Claude MCP + VS Code Demo 🚀

Ένα απλό demo MCP project που δείχνει:
- πώς να ορίσεις MCP εργαλεία
- πώς να τα καλέσει ο Claude μέσα από το Visual Studio Code

## 🧰 Απαιτούμενα
- Python >= 3.10
- VS Code με extension **Claude Code** (publisher: `anthropic`)
- Εγκατάσταση: `pip install mcp`

## ▶️ Τρέξιμο
```bash
python tools/server.py
```

## 💬 Παράδειγμα Prompt
Μπορείς να γράψεις στον Claude (μέσα από VS Code):
> Use the `echo` tool to say "Γειά σου Claude!"
> Count how many lines are in the resource called `sample`

Αυτό καλεί το tool `count_lines` στο `test.txt` μέσω MCP.
