#!/usr/bin/env python3
"""
Generate a standalone, high-fidelity local HTML preview of the GitHub Profile README
with GitHub dark/light mode toggle, typography, and live SVG rendering.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
README_PATH = os.path.join(ROOT, "README.md")
PREVIEW_PATH = os.path.join(ROOT, "preview.html")

def md_to_html(md_text):
    # Process markdown headings, blockquotes, tables, links, and pictures
    html = md_text

    # Replace alert blocks
    html = re.sub(
        r"> \[!NOTE\]\s*(.*?)(?=\n\n|\n<|$)",
        r'<div class="markdown-alert markdown-alert-note"><p class="markdown-alert-title">Note</p><p>\1</p></div>',
        html,
        flags=re.DOTALL
    )

    # Convert markdown tables to HTML tables
    def replace_table(match):
        lines = match.group(0).strip().split("\n")
        if len(lines) < 2:
            return match.group(0)
        headers = [c.strip() for c in lines[0].strip("|").split("|")]
        rows = [lines[i] for i in range(2, len(lines))]
        
        table_html = ['<table class="rendered-table"><thead><tr>']
        for h in headers:
            table_html.append(f'<th>{h}</th>')
        table_html.append('</tr></thead><tbody>')
        for r in rows:
            cols = [c.strip() for c in r.strip("|").split("|")]
            table_html.append('<tr>')
            for c in cols:
                # Handle basic inline markdown in cells
                c_html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', c)
                c_html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', c_html)
                c_html = re.sub(r'`(.*?)`', r'<code>\1</code>', c_html)
                c_html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', c_html)
                table_html.append(f'<td>{c_html}</td>')
            table_html.append('</tr>')
        table_html.append('</tbody></table>')
        return "\n".join(table_html)

    html = re.sub(r'(\|[^\n]+\|\n\|[-:| ]+\|\n(?:\|[^\n]+\|\n?)+)', replace_table, html)

    # Basic markdown formatting
    html = re.sub(r'### (.*?)\n', r'<h3>\1</h3>\n', html)
    html = re.sub(r'#### (.*?)\n', r'<h4>\1</h4>\n', html)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)

    return html

def build_preview():
    with open(README_PATH, "r", encoding="utf-8") as f:
        md = f.read()

    rendered_body = md_to_html(md)

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Preview: Shashwat Upadhyay — Research in Motion</title>
  <style>
    :root {{
      --bg-color: #0d1117;
      --card-bg: #161b22;
      --text-color: #e6edf3;
      --text-muted: #8b949e;
      --border-color: #30363d;
      --link-color: #58a6ff;
    }}
    body.light {{
      --bg-color: #f6f8fa;
      --card-bg: #ffffff;
      --text-color: #1f2328;
      --text-muted: #656d76;
      --border-color: #d0d7de;
      --link-color: #0969da;
    }}
    body {{
      background-color: var(--bg-color);
      color: var(--text-color);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans", Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 32px 16px;
      line-height: 1.6;
      transition: background-color 0.2s, color 0.2s;
    }}
    .container {{
      max-width: 880px;
      margin: 0 auto;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 40px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.15);
    }}
    .theme-switch {{
      position: fixed;
      top: 16px;
      right: 16px;
      background: var(--card-bg);
      border: 1px solid var(--border-color);
      color: var(--text-color);
      padding: 8px 14px;
      border-radius: 20px;
      cursor: pointer;
      font-size: 13px;
      font-weight: 600;
      z-index: 1000;
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }}
    a {{ color: var(--link-color); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    code {{
      font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
      font-size: 85%;
      background: rgba(127,127,127,0.15);
      padding: 2px 5px;
      border-radius: 4px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 16px 0;
    }}
    th, td {{
      padding: 10px 14px;
      border: 1px solid var(--border-color);
    }}
    th {{
      background: rgba(127,127,127,0.08);
      text-align: left;
    }}
    img {{
      max-width: 100%;
      height: auto;
      display: inline-block;
      vertical-align: middle;
    }}
    .markdown-alert {{
      padding: 12px 16px;
      border-left: 4px solid #1f6feb;
      background: rgba(56, 139, 253, 0.1);
      border-radius: 4px;
      margin: 16px 0;
    }}
    .markdown-alert-title {{
      font-weight: 600;
      color: #58a6ff;
      margin: 0 0 6px 0;
    }}
    hr {{
      border: 0;
      border-top: 1px solid var(--border-color);
      margin: 24px 0;
    }}
  </style>
</head>
<body>
  <button class="theme-switch" onclick="document.body.classList.toggle('light')">🌓 Toggle Light / Dark</button>
  <div class="container">
    {rendered_body}
  </div>
</body>
</html>
"""

    with open(PREVIEW_PATH, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Generated standalone preview HTML: {PREVIEW_PATH}")

if __name__ == "__main__":
    build_preview()

