import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\sai\OneDrive\Desktop\Aptitude"

# Map of markdown filenames to HTML filenames
link_mappings = {
    "Aptitude_Placement_Mastery_Guide.md": "aptitude_placement.html",
    "averages_ratio_proportion_study_guide.md": "averages_ratio_proportion_study_guide.html",
    "mixtures_alligations_study_guide.md": "mixtures_alligations_study_guide.html",
    "number_systems_simplification_study_guide.md": "number_systems_simplification_study_guide.html",
    "percentages_study_guide.md": "percentages_study_guide.html",
    "probability_study_guide.md": "probability_study_guide.html",
    "profit_loss_discount_study_guide.md": "profit_loss_discount_study_guide.html",
    "simple_compound_interest_study_guide.md": "simple_compound_interest_study_guide.html",
    "time_speed_distance_study_guide.md": "time_speed_distance_study_guide.html",
    "time_work_study_guide.md": "time_work_study_guide.html"
}

# Sidebar items configuration
study_guides = [
    {"name": "Home Dashboard", "link": "aptitude_placement.html", "emoji": "🏠"},
    {"name": "Number Systems", "link": "number_systems_simplification_study_guide.html", "emoji": "🔢"},
    {"name": "Percentages", "link": "percentages_study_guide.html", "emoji": "📈"},
    {"name": "Profit & Loss", "link": "profit_loss_discount_study_guide.html", "emoji": "💰"},
    {"name": "SI & CI", "link": "simple_compound_interest_study_guide.html", "emoji": "💸"},
    {"name": "Time & Work", "link": "time_work_study_guide.html", "emoji": "⚙️"},
    {"name": "Speed & Distance", "link": "time_speed_distance_study_guide.html", "emoji": "⏳"},
    {"name": "Averages & Ratio", "link": "averages_ratio_proportion_study_guide.html", "emoji": "📊"},
    {"name": "Mixtures & Alligation", "link": "mixtures_alligations_study_guide.html", "emoji": "⚖️"},
    {"name": "Probability", "link": "probability_study_guide.html", "emoji": "🎲"}
]

# Configurations for badges
file_metadata = {
    "averages_ratio_proportion_study_guide.md": {
        "rank": "7",
        "importance": "★★★★☆",
        "imp_color": "orange",
        "difficulty": "Easy--Medium",
        "diff_color": "yellowgreen"
    },
    "mixtures_alligations_study_guide.md": {
        "rank": "8",
        "importance": "★★★★☆",
        "imp_color": "orange",
        "difficulty": "Medium",
        "diff_color": "orange"
    },
    "number_systems_simplification_study_guide.md": {
        "rank": "1",
        "importance": "★★★★★",
        "imp_color": "red",
        "difficulty": "Medium",
        "diff_color": "orange"
    },
    "percentages_study_guide.md": {
        "rank": "2",
        "importance": "★★★★★",
        "imp_color": "red",
        "difficulty": "Easy--Medium",
        "diff_color": "yellowgreen"
    },
    "probability_study_guide.md": {
        "rank": "9",
        "importance": "★★★★☆",
        "imp_color": "orange",
        "difficulty": "Medium--Hard",
        "diff_color": "red"
    },
    "profit_loss_discount_study_guide.md": {
        "rank": "3",
        "importance": "★★★★☆",
        "imp_color": "orange",
        "difficulty": "Easy--Medium",
        "diff_color": "yellowgreen"
    },
    "simple_compound_interest_study_guide.md": {
        "rank": "4",
        "importance": "★★★★☆",
        "imp_color": "orange",
        "difficulty": "Medium",
        "diff_color": "orange"
    },
    "time_speed_distance_study_guide.md": {
        "rank": "6",
        "importance": "★★★★☆",
        "imp_color": "orange",
        "difficulty": "Medium",
        "diff_color": "orange"
    },
    "time_work_study_guide.md": {
        "rank": "5",
        "importance": "★★★★☆",
        "imp_color": "orange",
        "difficulty": "Medium",
        "diff_color": "orange"
    }
}

# Topic details for dashboard
topics_info = [
    {
        "rank": "1",
        "title": "Number Systems & Simplifications",
        "stars": "★★★★★",
        "difficulty": "Medium",
        "diff_class": "diff-medium",
        "practice": "75–100 Qs",
        "link": "number_systems_simplification_study_guide.html",
        "emoji": "🥇",
        "desc": "Number Systems is the single most foundational topic. Master this and other topics become easier."
    },
    {
        "rank": "2",
        "title": "Percentages",
        "stars": "★★★★★",
        "difficulty": "Easy-Medium",
        "diff_class": "diff-easy",
        "practice": "60–80 Qs",
        "link": "percentages_study_guide.html",
        "emoji": "🥈",
        "desc": "Percentages are the connective tissue of quantitative reasoning, underlying Profit & Loss, SI/CI, and Data Interpretation."
    },
    {
        "rank": "3",
        "title": "Profit, Loss & Discount",
        "stars": "★★★★★",
        "difficulty": "Easy-Medium",
        "diff_class": "diff-easy",
        "practice": "60–80 Qs",
        "link": "profit_loss_discount_study_guide.html",
        "emoji": "🥉",
        "desc": "Highly tested in service Giants. Covers CP, SP, MP, successive discounts, and dishonest merchant false weights."
    },
    {
        "rank": "4",
        "title": "Simple & Compound Interest",
        "stars": "★★★★★",
        "difficulty": "Medium",
        "diff_class": "diff-medium",
        "practice": "50–70 Qs",
        "link": "simple_compound_interest_study_guide.html",
        "emoji": "🏅",
        "desc": "Tested heavily in banking and IT services. Focuses on compounding growth and EMI calculations."
    },
    {
        "rank": "5",
        "title": "Time & Work",
        "stars": "★★★★★",
        "difficulty": "Medium",
        "diff_class": "diff-medium",
        "practice": "60–80 Qs",
        "link": "time_work_study_guide.html",
        "emoji": "⚙️",
        "desc": "Covers efficiency ratios, alternating days, and pipes & cisterns fill/drain rate problems."
    },
    {
        "rank": "6",
        "title": "Time, Speed & Distance",
        "stars": "★★★★★",
        "difficulty": "Medium",
        "diff_class": "diff-medium",
        "practice": "60–80 Qs",
        "link": "time_speed_distance_study_guide.html",
        "emoji": "⏳",
        "desc": "Includes relative speeds, train crossings, circular tracks, and boat upstream/downstream problems."
    },
    {
        "rank": "7",
        "title": "Averages, Ratio & Proportion",
        "stars": "★★★★☆",
        "difficulty": "Easy-Medium",
        "diff_class": "diff-easy",
        "practice": "50–70 Qs",
        "link": "averages_ratio_proportion_study_guide.html",
        "emoji": "📊",
        "desc": "Master Central Tendency deviations, weighted averages, direct/inverse scaling, and ratios."
    },
    {
        "rank": "8",
        "title": "Mixtures & Alligations",
        "stars": "★★★★☆",
        "difficulty": "Easy-Medium",
        "diff_class": "diff-easy",
        "practice": "50–70 Qs",
        "link": "mixtures_alligations_study_guide.html",
        "emoji": "⚖️",
        "desc": "Features the Alligation Cross, a powerful visual tool for finding mixing ratios and replacement dilution."
    },
    {
        "rank": "9",
        "title": "Probability",
        "stars": "★★★★☆",
        "difficulty": "Medium-Hard",
        "diff_class": "diff-hard",
        "practice": "50–80 Qs",
        "link": "probability_study_guide.html",
        "emoji": "🎲",
        "desc": "A favorite for product companies (Amazon, Google). Covers conditional probability and Bayes' Theorem."
    },
    {
        "rank": "10",
        "title": "Permutations & Combinations",
        "stars": "★★★★☆",
        "difficulty": "Medium-Hard",
        "diff_class": "diff-hard",
        "practice": "60–80 Qs",
        "link": "#",
        "emoji": "🧩",
        "desc": "Core foundation for Probability and arrangement brain-teasers (circular arrangement, identical items)."
    },
    {
        "rank": "11",
        "title": "Ages",
        "stars": "★★★☆☆",
        "difficulty": "Easy-Medium",
        "diff_class": "diff-easy",
        "practice": "40–60 Qs",
        "link": "#",
        "emoji": "⏳",
        "desc": "Algebraic relationship equations tracking variables across time scales."
    },
    {
        "rank": "12",
        "title": "Coding & Decoding",
        "stars": "★★★☆☆",
        "difficulty": "Easy-Medium",
        "diff_class": "diff-easy",
        "practice": "60–80 Qs",
        "link": "#",
        "emoji": "🔤",
        "desc": "Alphabet-number logical reasoning series. High scoring speed multiplier."
    },
    {
        "rank": "13",
        "title": "Blood Relations",
        "stars": "★★★☆☆",
        "difficulty": "Easy-Medium",
        "diff_class": "diff-easy",
        "practice": "50–70 Qs",
        "link": "#",
        "emoji": "🌳",
        "desc": "Family tree analysis, coded generation tracking, and pointing-to puzzle relationships."
    },
    {
        "rank": "14",
        "title": "Clocks & Calendar",
        "stars": "★★★☆☆",
        "difficulty": "Medium",
        "diff_class": "diff-medium",
        "practice": "40–60 Qs",
        "link": "#",
        "emoji": "📅",
        "desc": "Hands alignment angle calculations, leap year calculations, and odd days tracking."
    },
    {
        "rank": "15",
        "title": "Data Interpretation",
        "stars": "★★★★☆",
        "difficulty": "Medium",
        "diff_class": "diff-medium",
        "practice": "150+ Qs",
        "link": "#",
        "emoji": "📈",
        "desc": "Chart analyses (pie charts, line graphs, bar graphs, tables) checking fast numerical calculation."
    }
]

def markdown_to_html(md_text):
    # Rewrite local file links in markdown to point to HTML pages
    for md_name, html_name in link_mappings.items():
        # Replace matches like [percentages](file:///.../percentages_study_guide.md) or similar
        md_text = re.sub(r'\[([^\]]+)\]\([^)]*?' + re.escape(md_name) + r'[^)]*?\)', r'<a href="' + html_name + r'">\1</a>', md_text)
        # Also replace absolute markdown file scheme links
        md_text = md_text.replace(md_name, html_name)

    html = md_text

    # 1. Parse Code Blocks
    # Math blocks
    html = re.sub(
        r"```math\n(.*?)\n```", 
        r'<div class="math-block">\1</div>', 
        html, 
        flags=re.DOTALL
    )
    # Standard code blocks
    html = re.sub(
        r"```(.*?)\n(.*?)\n```", 
        r'<pre><code class="language-\1">\2</code></pre>', 
        html, 
        flags=re.DOTALL
    )
    # 2. Parse Alerts (including inside blockquotes)
    def alert_repl(match):
        alert_type = match.group(1).lower()
        content = match.group(2)
        cleaned_content = re.sub(r'^\s*>\s*', '', content, flags=re.MULTILINE)
        icons = {
            "note": "ℹ️",
            "tip": "💡",
            "warning": "⚠️",
            "important": "📢"
        }
        icon = icons.get(alert_type, "ℹ️")
        return f'<div class="alert alert-{alert_type}"><span class="alert-icon">{icon}</span><div class="alert-content">{cleaned_content}</div></div>'

    html = re.sub(
        r"> \[!(NOTE|TIP|WARNING|IMPORTANT)\]\s*\n(.*?)(?=\n\n|\n[^>])",
        alert_repl,
        html,
        flags=re.DOTALL | re.IGNORECASE
    )
    
    # 3. Parse Tables
    def table_repl(match):
        lines = match.group(0).strip().split('\n')
        table_html = '<table><thead><tr>'
        headers = [c.strip() for c in lines[0].split('|')[1:-1]]
        for h in headers:
            table_html += f'<th>{h}</th>'
        table_html += '</tr></thead><tbody>'
        
        for line in lines[2:]:
            cols = [c.strip() for c in line.split('|')[1:-1]]
            table_html += '<tr>'
            for c in cols:
                c_formatted = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", c)
                c_formatted = re.sub(r"\*(.*?)\*", r"<em>\1</em>", c_formatted)
                table_html += f'<td>{c_formatted}</td>'
            table_html += '</tr>'
        table_html += '</tbody></table>'
        return table_html

    html = re.sub(r'(\|.*\|)\n(\|[-:\s|]*\|)\n((\|.*\|\n?)+)', table_repl, html)

    # 4. Parse Headers
    html = re.sub(r'^#\s+(.*)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^##\s+(.*)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^###\s+(.*)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^####\s+(.*)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    
    # 5. Parse Details Accordions content (to format markdown inside accordion)
    def details_repl(match):
        content = match.group(1)
        # We recursively parse formatting inside details
        content_html = markdown_to_html(content)
        # Wrap summary in a strong or keep it clean
        return f'<details>{content_html}</details>'
        
    html = re.compile(r'<details>(.*?)</details>', re.DOTALL).sub(details_repl, html)
    
    # 6. Parse Lists
    html = re.sub(r'^\s*-\s+(.*)$', r'<ul><li>\1</li></ul>', html, flags=re.MULTILINE)
    html = re.sub(r'</ul>\s*<ul>', '', html)
    
    html = re.sub(r'^\s*(\d+)\.\s+(.*)$', r'<ol><li>\2</li></ol>', html, flags=re.MULTILINE)
    html = re.sub(r'</ol>\s*<ol>', '', html)
    
    # 7. Convert horizontal rules
    html = re.sub(r'^---$', r'<hr />', html, flags=re.MULTILINE)
    
    # 8. Parse Inline markdown (strong, em, inline code, links)
    html = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.*?)\*", r"<em>\1</em>", html)
    html = re.sub(r"`(.*?)`", r"<code>\1</code>", html)
    
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    return html

# Generate dynamic table of contents for sidebars
def generate_toc(md_content):
    headers = re.findall(r"^##\s+(.*)$", md_content, re.MULTILINE)
    toc_html = '<ul class="toc-list">'
    for h in headers:
        # Generate clean ID
        clean_id = re.sub(r"[^\w\s-]", "", h).strip().lower().replace(" ", "-")
        # Strip emoji from text if present
        clean_text = re.sub(r"[^\w\s&,·]", "", h).strip()
        toc_html += f'<li><a href="#{clean_id}">{clean_text}</a></li>'
    toc_html += '</ul>'
    return toc_html

# Add IDs to headers in the HTML content dynamically matching the TOC
def add_header_ids(html_content):
    def repl_h2(match):
        h_text = match.group(1)
        clean_id = re.sub(r"[^\w\s-]", "", h_text).strip().lower().replace(" ", "-")
        # We keep any nested tags like strong, but ID applies to h2
        return f'<h2 id="{clean_id}">{h_text}</h2>'
    return re.sub(r'<h2>(.*?)</h2>', repl_h2, html_content)

def compile_study_guide(filename):
    print(f"Compiling study guide HTML: {filename}")
    md_path = os.path.join(workspace_dir, filename)
    html_name = link_mappings[filename]
    html_path = os.path.join(workspace_dir, html_name)
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    toc_html = generate_toc(md_content)
    body_content = add_header_ids(markdown_to_html(md_content))
    
    # Generate Quick Navigation sidebar list
    quick_nav = '<ul class="quick-nav-list">'
    for guide in study_guides:
        active_class = 'class="active"' if guide['link'] == html_name else ''
        quick_nav += f'<li><a href="{guide["link"]}" {active_class}><span class="nav-emoji">{guide["emoji"]}</span> {guide["name"]}</a></li>'
    quick_nav += '</ul>'
    
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{filename.replace('_', ' ').replace('.md', '').title()} | Learning Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #f8fafc;
            --text-color: #1e293b;
            --sidebar-bg: #ffffff;
            --border-color: #e2e8f0;
            --primary-color: #2563eb;
            --primary-light: #eff6ff;
            --code-bg: #f1f5f9;
            --details-bg: #ffffff;
            
            --note-border: #3b82f6;
            --note-bg: rgba(59, 130, 246, 0.05);
            --tip-border: #10b981;
            --tip-bg: rgba(16, 185, 129, 0.05);
            --warning-border: #f59e0b;
            --warning-bg: rgba(245, 158, 11, 0.05);
            --important-border: #8b5cf6;
            --important-bg: rgba(139, 92, 246, 0.05);
        }}
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        
        body {{
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            display: flex;
        }}
        
        /* Sticky Sidebar Layout */
        .sidebar {{
            width: 280px;
            background-color: var(--sidebar-bg);
            border-right: 1px solid var(--border-color);
            height: 100vh;
            position: sticky;
            top: 0;
            padding: 24px;
            overflow-y: auto;
            display: flex;
            flex-direction: flex-start;
            flex-flow: column;
            gap: 24px;
        }}
        
        .sidebar-brand {{
            font-weight: 700;
            font-size: 1.25rem;
            color: var(--primary-color);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 8px;
            text-decoration: none;
            transition: opacity 0.2s ease;
        }}
        
        .sidebar-brand:hover {{
            opacity: 0.85;
            text-decoration: none;
        }}
        
        .sidebar-section-title {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #64748b;
            font-weight: 600;
            margin-bottom: 8px;
        }}
        
        .quick-nav-list, .toc-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}
        
        .quick-nav-list a, .toc-list a {{
            color: #475569;
            text-decoration: none;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 12px;
            border-radius: 6px;
            transition: all 0.2s ease;
        }}
        
        .quick-nav-list a:hover, .toc-list a:hover {{
            background-color: #f1f5f9;
            color: var(--primary-color);
        }}
        
        .quick-nav-list a.active {{
            background-color: var(--primary-light);
            color: var(--primary-color);
            font-weight: 500;
        }}
        
        .toc-list a {{
            font-size: 0.85rem;
            padding: 4px 8px;
            border-left: 2px solid transparent;
            border-radius: 0;
        }}
        
        .toc-list a:hover {{
            background-color: transparent;
            border-left-color: var(--primary-color);
            padding-left: 12px;
        }}
        
        /* Main Container */
        .container {{
            flex: 1;
            max-width: 900px;
            margin: 40px auto;
            padding: 0 40px;
        }}
        
        h1, h2, h3, h4 {{
            color: #0f172a;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            font-weight: 600;
        }}
        
        h1 {{
            font-size: 2.25rem;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 12px;
        }}
        
        h2 {{
            font-size: 1.6rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 8px;
            margin-top: 2em;
        }}
        
        h3 {{
            font-size: 1.25rem;
        }}
        
        a {{
            color: var(--primary-color);
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        hr {{
            border: 0;
            height: 1px;
            background: var(--border-color);
            margin: 30px 0;
        }}
        
        img {{
            border-radius: 4px;
        }}
        
        /* Shields badges top */
        div[align="left"] {{
            display: flex;
            gap: 8px;
            margin: 20px 0;
            flex-wrap: wrap;
        }}
        
        /* Alerts styling */
        .alert {{
            display: flex;
            border-left: 4px solid;
            padding: 16px;
            border-radius: 6px;
            margin: 20px 0;
        }}
        
        .alert-icon {{
            font-size: 1.25rem;
            margin-right: 12px;
            display: flex;
            align-items: center;
        }}
        
        .alert-content {{
            flex: 1;
        }}
        
        .alert-note {{
            border-left-color: var(--note-border);
            background-color: var(--note-bg);
        }}
        
        .alert-tip {{
            border-left-color: var(--tip-border);
            background-color: var(--tip-bg);
        }}
        
        .alert-warning {{
            border-left-color: var(--warning-border);
            background-color: var(--warning-bg);
        }}
        
        .alert-important {{
            border-left-color: var(--important-border);
            background-color: var(--important-bg);
        }}
        
        /* Tables styling */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.9rem;
        }}
        
        th, td {{
            padding: 12px 16px;
            border: 1px solid var(--border-color);
            text-align: left;
        }}
        
        th {{
            background-color: #f1f5f9;
            color: #0f172a;
            font-weight: 500;
        }}
        
        tr:nth-child(even) {{
            background-color: rgba(0, 0, 0, 0.01);
        }}
        
        /* Code blocks */
        pre {{
            background-color: var(--code-bg);
            padding: 16px;
            border-radius: 8px;
            overflow-x: auto;
            border: 1px solid var(--border-color);
            margin: 20px 0;
        }}
        
        code {{
            font-family: 'JetBrains Mono', monospace;
            background-color: var(--code-bg);
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.85rem;
            color: #0f172a;
        }}
        
        pre code {{
            padding: 0;
            background-color: transparent;
            font-size: 0.8rem;
        }}
        
        /* details / summary styling */
        details {{
            background-color: var(--details-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            margin: 12px 0;
            padding: 14px 18px;
            transition: all 0.3s ease;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
        }}
        
        details[open] {{
            border-color: var(--primary-color);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }}
        
        summary {{
            font-weight: 500;
            cursor: pointer;
            outline: none;
            color: #0f172a;
            user-select: none;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        summary:hover {{
            color: var(--primary-color);
        }}
        
        details > div, details > ul, details > p, details > pre {{
            margin-top: 12px;
            padding-top: 12px;
            border-top: 1px solid var(--border-color);
        }}
        
        ul, ol {{
            padding-left: 20px;
            margin: 12px 0;
        }}
        
        li {{
            margin-bottom: 6px;
        }}
        
        /* Responsive design */
        @media (max-width: 1024px) {{
            body {{
                flex-direction: column;
            }}
            .sidebar {{
                width: 100%;
                height: auto;
                position: relative;
                border-right: none;
                border-bottom: 1px solid var(--border-color);
                padding: 16px;
            }}
            .container {{
                padding: 0 20px;
                margin: 20px auto;
            }}
        }}
    </style>
</head>
<body>
    <aside class="sidebar">
        <a href="aptitude_placement.html" class="sidebar-brand">
            🎓 Aptitude Mastery
        </a>
        <hr style="margin: 12px 0;" />
        <div class="sidebar-section-title">Table of Contents</div>
        {toc_html}
        <hr style="margin: 12px 0;" />
        <div class="sidebar-section-title">Topic Guides</div>
        {quick_nav}
    </aside>
    <main class="container">
        {body_content}
    </main>
</body>
</html>
"""
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"  Successfully compiled: {html_name}")


def compile_flagship_dashboard():
    filename = "Aptitude_Placement_Mastery_Guide.md"
    print(f"Compiling flagship dashboard: {filename}")
    md_path = os.path.join(workspace_dir, filename)
    html_name = "aptitude_placement.html"
    html_path = os.path.join(workspace_dir, html_name)
    
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    # Split content by H2 sections to extract executive summary, roadmap, resources, and practice questions
    # Let's extract the header, executive summary, etc.
    sections = re.split(r"^##\s+", md_content, flags=re.MULTILINE)
    
    header_content = markdown_to_html(sections[0])
    exec_summary = markdown_to_html("## " + sections[1]) if len(sections) > 1 else ""
    
    # We will replace the Ranked Topics section with our interactive visual cards!
    # Let's build the topics cards HTML
    cards_html = '<div class="topic-grid">'
    for topic in topics_info:
        guide_status = ""
        btn_class = "btn-start"
        btn_text = "Start Topic Guide"
        
        if topic['link'] == "#":
            guide_status = '<span class="status-badge status-lr-di">LR/DI Module</span>'
            btn_class = "btn-disabled"
            btn_text = "Core Syllabus Only"
        else:
            guide_status = '<span class="status-badge status-quant">Quant Guide</span>'
            
        cards_html += f"""
        <div class="topic-card">
            <div class="card-header">
                <span class="card-emoji">{topic['emoji']}</span>
                <span class="card-rank">Rank {topic['rank']}</span>
                {guide_status}
            </div>
            <h3 class="card-title">{topic['title']}</h3>
            <p class="card-desc">{topic['desc']}</p>
            <div class="card-meta">
                <div class="meta-item">
                    <span class="meta-label">Importance</span>
                    <span class="meta-stars">{topic['stars']}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Difficulty</span>
                    <span class="meta-badge {topic['diff_class']}">{topic['difficulty']}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Syllabus</span>
                    <span class="meta-practice">{topic['practice']}</span>
                </div>
            </div>
            <a href="{topic['link']}" class="card-btn {btn_class}">{btn_text}</a>
        </div>
        """
    cards_html += '</div>'
    
    # Rest of the sections
    roadmap_section = markdown_to_html("## " + sections[3]) if len(sections) > 3 else ""
    resources_section = markdown_to_html("## " + sections[4]) if len(sections) > 4 else ""
    practice_section = markdown_to_html("## " + sections[5]) if len(sections) > 5 else ""
    
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Aptitude Placement Mastery Guide</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #f8fafc;
            --text-color: #1e293b;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
            --primary-color: #2563eb;
            --primary-light: #eff6ff;
            --primary-dark: #1e40af;
            
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --danger-color: #ef4444;
        }}
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        
        body {{
            font-family: 'Outfit', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            background-image: radial-gradient(circle at 10% 20%, rgba(59, 130, 246, 0.03) 0%, transparent 40%),
                              radial-gradient(circle at 90% 80%, rgba(79, 70, 229, 0.03) 0%, transparent 40%);
            background-attachment: fixed;
        }}
        
        /* Navigation header */
        .navbar {{
            background-color: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(8px);
            border-bottom: 1px solid var(--border-color);
            padding: 16px 40px;
            position: sticky;
            top: 0;
            z-index: 100;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .navbar-brand {{
            font-weight: 700;
            font-size: 1.25rem;
            color: var(--primary-color);
            display: flex;
            align-items: center;
            gap: 8px;
            text-decoration: none;
            transition: opacity 0.2s ease;
        }}
        
        .navbar-brand:hover {{
            opacity: 0.85;
            text-decoration: none;
        }}
        
        /* Hero Section styling */
        .hero {{
            padding: 80px 40px 60px 40px;
            text-align: center;
            max-width: 1000px;
            margin: 0 auto;
        }}
        
        .hero h1 {{
            font-size: 3rem;
            color: #0f172a;
            margin-bottom: 16px;
            font-weight: 800;
            letter-spacing: -0.02em;
            line-height: 1.2;
            background: linear-gradient(to right, #2563eb, #4f46e5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .hero p {{
            font-size: 1.25rem;
            color: #64748b;
            max-width: 600px;
            margin: 0 auto 30px auto;
        }}
        
        .hero-stats {{
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 20px;
            flex-wrap: wrap;
        }}
        
        .stat-item {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        
        .stat-val {{
            font-size: 2rem;
            font-weight: 700;
            color: #0f172a;
        }}
        
        .stat-label {{
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #64748b;
            font-weight: 600;
        }}
        
        /* Main Layout */
        .main-content {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 40px 80px 40px;
        }}
        
        .section-header {{
            font-size: 2rem;
            color: #0f172a;
            margin: 60px 0 24px 0;
            font-weight: 700;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 12px;
        }}
        
        /* Live Search Section */
        .search-container {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 12px;
            padding: 16px 24px;
            margin-bottom: 30px;
            display: flex;
            gap: 16px;
            align-items: center;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
        }}
        
        .search-icon {{
            font-size: 1.25rem;
        }}
        
        .search-input {{
            flex: 1;
            border: none;
            outline: none;
            font-family: inherit;
            font-size: 1rem;
            color: var(--text-color);
        }}
        
        /* Topics Grid System */
        .topic-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
            gap: 24px;
            margin-top: 20px;
        }}
        
        .topic-card {{
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 16px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02);
            position: relative;
            overflow: hidden;
        }}
        
        .topic-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.05),
                        0 4px 6px -2px rgba(0, 0, 0, 0.03);
            border-color: var(--primary-light);
        }}
        
        .card-header {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .card-emoji {{
            font-size: 1.25rem;
        }}
        
        .card-rank {{
            font-size: 0.8rem;
            font-weight: 600;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        
        .status-badge {{
            font-size: 0.7rem;
            font-weight: 600;
            padding: 2px 8px;
            border-radius: 9999px;
            margin-left: auto;
        }}
        
        .status-quant {{
            background-color: var(--primary-light);
            color: var(--primary-color);
        }}
        
        .status-lr-di {{
            background-color: #f3e8ff;
            color: #7c3aed;
        }}
        
        .card-title {{
            font-size: 1.25rem;
            font-weight: 700;
            color: #0f172a;
        }}
        
        .card-desc {{
            font-size: 0.9rem;
            color: #64748b;
            flex: 1;
        }}
        
        .card-meta {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            border-top: 1px solid var(--border-color);
            padding-top: 16px;
        }}
        
        .meta-item {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        
        .meta-label {{
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #94a3b8;
            font-weight: 600;
        }}
        
        .meta-stars {{
            font-size: 0.85rem;
            color: var(--warning-color);
        }}
        
        .meta-badge {{
            font-size: 0.75rem;
            font-weight: 600;
            padding: 2px 6px;
            border-radius: 4px;
            text-align: center;
            width: fit-content;
        }}
        
        .diff-easy {{
            background-color: #d1fae5;
            color: #065f46;
        }}
        
        .diff-medium {{
            background-color: #fef3c7;
            color: #92400e;
        }}
        
        .diff-hard {{
            background-color: #fee2e2;
            color: #991b1b;
        }}
        
        .meta-practice {{
            font-size: 0.85rem;
            font-weight: 600;
            color: #334155;
        }}
        
        .card-btn {{
            display: block;
            text-align: center;
            padding: 12px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.9rem;
            text-decoration: none;
            transition: all 0.2s ease;
        }}
        
        .btn-start {{
            background-color: var(--primary-color);
            color: #ffffff;
        }}
        
        .btn-start:hover {{
            background-color: var(--primary-dark);
        }}
        
        .btn-disabled {{
            background-color: #f1f5f9;
            color: #94a3b8;
            cursor: not-allowed;
            pointer-events: none;
        }}
        
        /* Tables styling */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background-color: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
        }}
        
        th, td {{
            padding: 14px 18px;
            border: 1px solid var(--border-color);
            text-align: left;
        }}
        
        th {{
            background-color: #f8fafc;
            color: #0f172a;
            font-weight: 600;
        }}
        
        tr:nth-child(even) {{
            background-color: #f8fafc;
        }}
        
        /* Alerts styling */
        .alert {{
            display: flex;
            border-left: 4px solid;
            padding: 16px;
            border-radius: 6px;
            margin: 20px 0;
            background: #ffffff;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
        }}
        
        .alert-icon {{
            font-size: 1.25rem;
            margin-right: 12px;
            display: flex;
            align-items: center;
        }}
        
        .alert-content {{
            flex: 1;
        }}
        
        .alert-important {{
            border-left-color: var(--important-border, #8b5cf6);
            background-color: rgba(139, 92, 246, 0.05);
        }}
        
        .alert-note {{
            border-left-color: #3b82f6;
            background-color: rgba(59, 130, 246, 0.05);
        }}
        
        .alert-tip {{
            border-left-color: #10b981;
            background-color: rgba(16, 185, 129, 0.05);
        }}
        
        ul, ol {{
            padding-left: 20px;
            margin: 12px 0;
        }}
        
        li {{
            margin-bottom: 6px;
        }}
        
        /* Responsive Grid fixes */
        @media (max-width: 768px) {{
            .navbar {{
                padding: 16px 20px;
            }}
            .hero h1 {{
                font-size: 2.25rem;
            }}
            .hero-stats {{
                gap: 20px;
            }}
            .main-content {{
                padding: 0 20px 60px 20px;
            }}
            .topic-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <header class="navbar">
        <a href="aptitude_placement.html" class="navbar-brand">
            🎓 Aptitude Placement Mastery Portal
        </a>
    </header>
    
    <section class="hero">
        <h1>Ultimate Aptitude Placement Mastery Guide</h1>
        <p>A structured, high-ROI quantitative syllabus design to take you from zero to placement-ready in 15 days.</p>
        <div class="hero-stats">
            <div class="stat-item">
                <span class="stat-val">15</span>
                <span class="stat-label">Syllabus Ranks</span>
            </div>
            <div class="stat-item">
                <span class="stat-val">9</span>
                <span class="stat-label">Quant Guides</span>
            </div>
            <div class="stat-item">
                <span class="stat-val">15 Days</span>
                <span class="stat-label">Sprint Plan</span>
            </div>
        </div>
    </section>
    
    <main class="main-content">
        <h2 class="section-header">Executive Summary</h2>
        {exec_summary}
        
        <h2 class="section-header" id="ranked-topics">Top 15 Aptitude Syllabus Topics (Ranked by ROI)</h2>
        <div class="search-container">
            <span class="search-icon">🔍</span>
            <input type="text" id="topicSearch" class="search-input" placeholder="Search topics by rank, name, difficulty..." onkeyup="filterTopics()" />
        </div>
        {cards_html}
        
        <h2 class="section-header">The 15-Day Sprint Roadmap</h2>
        {roadmap_section}
        
        <h2 class="section-header">Best Free Learning Resources</h2>
        {resources_section}
        
        <h2 class="section-header">Top 50 Practice Questions Per Topic</h2>
        {practice_section}
    </main>
    
    <script>
        function filterTopics() {{
            let input = document.getElementById('topicSearch');
            let filter = input.value.toLowerCase();
            let cards = document.getElementsByClassName('topic-card');
            
            for (let i = 0; i < cards.length; i++) {{
                let title = cards[i].getElementsByClassName('card-title')[0].innerText.toLowerCase();
                let rank = cards[i].getElementsByClassName('card-rank')[0].innerText.toLowerCase();
                let desc = cards[i].getElementsByClassName('card-desc')[0].innerText.toLowerCase();
                let diff = cards[i].getElementsByClassName('meta-badge')[0].innerText.toLowerCase();
                
                if (title.includes(filter) || rank.includes(filter) || desc.includes(filter) || diff.includes(filter)) {{
                    cards[i].style.display = "";
                }} else {{
                    cards[i].style.display = "none";
                }}
            }}
        }}
    </script>
</body>
</html>
"""
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"  Successfully compiled flagship homepage: {html_name}")


# Compile all study guides
for md_file in file_metadata.keys():
    compile_study_guide(md_file)

# Compile the flagship dashboard
compile_flagship_dashboard()

print("HTML compilation portal successfully completed!")
