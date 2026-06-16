import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\sai\OneDrive\Desktop\Aptitude"

# Map of markdown filenames to HTML filenames
link_mappings = {
    "Aptitude_Placement_Mastery_Guide.md": "index.html",
    "averages_ratio_proportion_study_guide.md": "averages_ratio_proportion_study_guide.html",
    "mixtures_alligations_study_guide.md": "mixtures_alligations_study_guide.html",
    "number_systems_simplification_study_guide.md": "number_systems_simplification_study_guide.html",
    "percentages_study_guide.md": "percentages_study_guide.html",
    "probability_study_guide.md": "probability_study_guide.html",
    "profit_loss_discount_study_guide.md": "profit_loss_discount_study_guide.html",
    "simple_compound_interest_study_guide.md": "simple_compound_interest_study_guide.html",
    "time_speed_distance_study_guide.md": "time_speed_distance_study_guide.html",
    "time_work_study_guide.md": "time_work_study_guide.html",
    "permutations_combinations_study_guide.md": "permutations_combinations_study_guide.html",
    "ages_study_guide.md": "ages_study_guide.html",
    "coding_decoding_study_guide.md": "coding_decoding_study_guide.html",
    "blood_relations_study_guide.md": "blood_relations_study_guide.html",
    "clocks_calendar_study_guide.md": "clocks_calendar_study_guide.html",
    "data_interpretation_study_guide.md": "data_interpretation_study_guide.html"
}

# Sidebar items configuration
study_guides = [
    {"name": "Home Dashboard", "link": "index.html", "emoji": "🏠"},
    {"name": "Number Systems", "link": "number_systems_simplification_study_guide.html", "emoji": "🔢"},
    {"name": "Percentages", "link": "percentages_study_guide.html", "emoji": "📈"},
    {"name": "Profit & Loss", "link": "profit_loss_discount_study_guide.html", "emoji": "💰"},
    {"name": "SI & CI", "link": "simple_compound_interest_study_guide.html", "emoji": "💸"},
    {"name": "Time & Work", "link": "time_work_study_guide.html", "emoji": "⚙️"},
    {"name": "Speed & Distance", "link": "time_speed_distance_study_guide.html", "emoji": "⏳"},
    {"name": "Averages & Ratio", "link": "averages_ratio_proportion_study_guide.html", "emoji": "📊"},
    {"name": "Mixtures & Alligation", "link": "mixtures_alligations_study_guide.html", "emoji": "⚖️"},
    {"name": "Probability", "link": "probability_study_guide.html", "emoji": "🎲"},
    {"name": "P & C", "link": "permutations_combinations_study_guide.html", "emoji": "🧩"},
    {"name": "Ages", "link": "ages_study_guide.html", "emoji": "⏳"},
    {"name": "Coding Decoding", "link": "coding_decoding_study_guide.html", "emoji": "🔤"},
    {"name": "Blood Relations", "link": "blood_relations_study_guide.html", "emoji": "🌳"},
    {"name": "Clocks & Calendar", "link": "clocks_calendar_study_guide.html", "emoji": "📅"},
    {"name": "Data Interpretation", "link": "data_interpretation_study_guide.html", "emoji": "📈"}
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
    },
    "permutations_combinations_study_guide.md": {
        "rank": "10",
        "importance": "★★★★☆",
        "imp_color": "orange",
        "difficulty": "Medium--Hard",
        "diff_color": "red"
    },
    "ages_study_guide.md": {
        "rank": "11",
        "importance": "★★★☆☆",
        "imp_color": "orange",
        "difficulty": "Easy--Medium",
        "diff_color": "yellowgreen"
    },
    "coding_decoding_study_guide.md": {
        "rank": "12",
        "importance": "★★★☆☆",
        "imp_color": "orange",
        "difficulty": "Easy--Medium",
        "diff_color": "yellowgreen"
    },
    "blood_relations_study_guide.md": {
        "rank": "13",
        "importance": "★★★☆☆",
        "imp_color": "orange",
        "difficulty": "Easy--Medium",
        "diff_color": "yellowgreen"
    },
    "clocks_calendar_study_guide.md": {
        "rank": "14",
        "importance": "★★★☆☆",
        "imp_color": "orange",
        "difficulty": "Medium",
        "diff_color": "orange"
    },
    "data_interpretation_study_guide.md": {
        "rank": "15",
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
        "link": "permutations_combinations_study_guide.html",
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
        "link": "ages_study_guide.html",
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
        "link": "coding_decoding_study_guide.html",
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
        "link": "blood_relations_study_guide.html",
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
        "link": "clocks_calendar_study_guide.html",
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
        "link": "data_interpretation_study_guide.html",
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
    
    # Wrap standard text paragraphs in <p> tags
    html = wrap_paragraphs(html)
    
    return html

def wrap_paragraphs(html):
    placeholders = []
    
    def repl_placeholder(match):
        placeholder = f"<!--__BLOCK_PLACEHOLDER_{len(placeholders)}__-->"
        placeholders.append((placeholder, match.group(0)))
        return placeholder

    protected_patterns = [
        r'<pre\b[^>]*>.*?</pre>',
        r'<details\b[^>]*>.*?</details>',
        r'<blockquote\b[^>]*>.*?</blockquote>',
        r'<div\b[^>]*>.*?</div>',
        r'<table\b[^>]*>.*?</table>'
    ]
    
    protected_regex = '|'.join(protected_patterns)
    html_with_placeholders = re.sub(protected_regex, repl_placeholder, html, flags=re.DOTALL | re.IGNORECASE)
    
    blocks = re.split(r'\n\n+', html_with_placeholders)
    new_blocks = []
    
    for block in blocks:
        block_stripped = block.strip()
        if not block_stripped:
            continue
        
        is_placeholder = block_stripped.startswith("<!--__BLOCK_PLACEHOLDER_")
        is_block_tag = re.match(r'^\s*<(h[1-6]|hr|ul|ol|p)\b', block_stripped, re.IGNORECASE)
        
        if not is_placeholder and not is_block_tag:
            new_blocks.append(f"<p>{block_stripped}</p>")
        else:
            new_blocks.append(block_stripped)
            
    reassembled_html = '\n\n'.join(new_blocks)
    
    for placeholder, original in reversed(placeholders):
        reassembled_html = reassembled_html.replace(placeholder, original)
        
    return reassembled_html


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
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{filename.replace('_', ' ').replace('.md', '').title()} | Learning Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <script>
        // Sync theme immediately to prevent flashing
        (function() {{
            const savedTheme = localStorage.getItem('theme') || 'light';
            document.documentElement.setAttribute('data-theme', savedTheme);
        }})();
    </script>
    <style>
        :root {{
            --bg-color: #f8fafc;
            --text-color: #0f172a;
            --text-muted: #64748b;
            --sidebar-bg: #ffffff;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
            --primary-color: #2563eb;
            --primary-hover: #1d4ed8;
            --primary-light: #eff6ff;
            --accent-color: #8b5cf6;
            --accent-light: #f5f3ff;
            --code-bg: #f8fafc;
            --details-bg: #ffffff;
            
            --note-border: #3b82f6;
            --note-bg: rgba(59, 130, 246, 0.05);
            --tip-border: #10b981;
            --tip-bg: rgba(16, 185, 129, 0.05);
            --warning-border: #f59e0b;
            --warning-bg: rgba(245, 158, 11, 0.05);
            --important-border: #8b5cf6;
            --important-bg: rgba(139, 92, 246, 0.05);
            
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
            --sidebar-width: 320px;
            --transition-speed: 0.3s;
        }}
        
        [data-theme="dark"] {{
            --bg-color: #090d16;
            --text-color: #f1f5f9;
            --text-muted: #94a3b8;
            --sidebar-bg: #111827;
            --card-bg: #1f293d;
            --border-color: #1f293d;
            --primary-color: #3b82f6;
            --primary-hover: #60a5fa;
            --primary-light: rgba(59, 130, 246, 0.15);
            --accent-color: #a78bfa;
            --accent-light: rgba(139, 92, 246, 0.15);
            --code-bg: #111827;
            --details-bg: #111827;
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.5);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
            
            --note-border: #3b82f6;
            --note-bg: rgba(59, 130, 246, 0.1);
            --tip-border: #10b981;
            --tip-bg: rgba(16, 185, 129, 0.1);
            --warning-border: #f59e0b;
            --warning-bg: rgba(245, 158, 11, 0.1);
            --important-border: #8b5cf6;
            --important-bg: rgba(139, 92, 246, 0.1);
        }}
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            transition: background-color var(--transition-speed) ease, border-color var(--transition-speed) ease;
        }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            display: flex;
            min-height: 100vh;
        }}
        
        /* Sticky Sidebar Layout */
        .sidebar {{
            width: var(--sidebar-width);
            background-color: var(--sidebar-bg);
            border-right: 1px solid var(--border-color);
            height: 100vh;
            position: sticky;
            top: 0;
            padding: 30px 24px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 28px;
            flex-shrink: 0;
            z-index: 90;
            box-shadow: var(--shadow-sm);
        }}
        
        .sidebar.collapsed {{
            width: 0;
            padding: 0;
            overflow: hidden;
            border-right: none;
        }}
        
        .sidebar-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .sidebar-brand {{
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 1.35rem;
            color: var(--primary-color);
            display: flex;
            align-items: center;
            gap: 8px;
            text-decoration: none;
        }}
        
        .theme-toggle-btn {{
            background: none;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            width: 38px;
            height: 38px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: var(--bg-color);
            border: 1px solid var(--border-color);
            transition: all 0.2s ease;
        }}
        
        .theme-toggle-btn:hover {{
            color: var(--primary-color);
            transform: scale(1.05);
        }}
        
        .sun-icon {{ display: block; }}
        .moon-icon {{ display: none; }}
        
        [data-theme="dark"] .sun-icon {{ display: none; }}
        [data-theme="dark"] .moon-icon {{ display: block; }}
        
        .sidebar-progress-card {{
            background-color: var(--bg-color);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 16px;
        }}
        
        .sidebar-progress-label {{
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            font-weight: 700;
            margin-bottom: 8px;
            display: block;
        }}
        
        .sidebar-progress-wrapper {{
            background-color: var(--border-color);
            border-radius: 99px;
            height: 8px;
            overflow: hidden;
            margin-bottom: 6px;
        }}
        
        .sidebar-progress-bar {{
            background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
            height: 100%;
            width: 0%;
            border-radius: 99px;
            transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        .sidebar-progress-stats {{
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--text-color);
        }}
        
        .sidebar-section-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: var(--text-muted);
            font-weight: 700;
            margin-bottom: 10px;
        }}
        
        .quick-nav-list, .toc-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        
        .quick-nav-list a, .toc-list a {{
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.88rem;
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 10px 14px;
            border-radius: var(--radius-sm);
            transition: all 0.2s ease;
            font-weight: 500;
        }}
        
        .quick-nav-list a:hover, .toc-list a:hover {{
            background-color: var(--bg-color);
            color: var(--primary-color);
            transform: translateX(4px);
        }}
        
        .quick-nav-list a.active {{
            background-color: var(--primary-light);
            color: var(--primary-color);
            font-weight: 600;
            box-shadow: inset 3px 0 0 var(--primary-color);
        }}
        
        .toc-list a {{
            font-size: 0.84rem;
            padding: 6px 12px;
            border-left: 2px solid var(--border-color);
            border-radius: 0;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        
        .toc-list a:hover {{
            background-color: transparent;
            border-left-color: var(--primary-color);
            padding-left: 16px;
            color: var(--text-color);
        }}
        
        /* Main Container */
        .container {{
            flex: 1;
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 60px;
            width: 100%;
        }}
        
        /* Floating layout controls */
        .header-controls {{
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 24px;
        }}
        
        .collapse-btn {{
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            color: var(--text-color);
            cursor: pointer;
            padding: 10px 14px;
            border-radius: var(--radius-sm);
            font-size: 0.88rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 6px;
            box-shadow: var(--shadow-sm);
            transition: all 0.2s ease;
        }}
        
        .collapse-btn:hover {{
            background-color: var(--primary-light);
            color: var(--primary-color);
            border-color: var(--primary-color);
        }}
        
        h1, h2, h3, h4 {{
            font-family: 'Outfit', sans-serif;
            color: var(--text-color);
            margin-top: 1.8em;
            margin-bottom: 0.6em;
            font-weight: 700;
            letter-spacing: -0.01em;
        }}
        
        h1 {{
            font-size: 2.5rem;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 16px;
            margin-top: 0;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        h2 {{
            font-size: 1.75rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 10px;
            margin-top: 2.2em;
        }}
        
        h3 {{
            font-size: 1.35rem;
        }}
        
        p {{
            color: var(--text-color);
            opacity: 0.9;
            margin-bottom: 16px;
            line-height: 1.7;
        }}
        
        a {{
            color: var(--primary-color);
            text-decoration: none;
            font-weight: 500;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        hr {{
            border: 0;
            height: 1px;
            background: var(--border-color);
            margin: 40px 0;
        }}
        
        img {{
            border-radius: var(--radius-md);
            max-width: 100%;
        }}
        
        /* Badge styling */
        div[align="left"] {{
            display: flex;
            gap: 10px;
            margin: 24px 0;
            flex-wrap: wrap;
        }}
        
        /* Alerts styling */
        .alert {{
            display: flex;
            border-left: 4px solid;
            padding: 20px;
            border-radius: var(--radius-md);
            margin: 28px 0;
            box-shadow: var(--shadow-sm);
        }}
        
        .alert-icon {{
            font-size: 1.4rem;
            margin-right: 16px;
            display: flex;
            align-items: center;
        }}
        
        .alert-content {{
            flex: 1;
        }}
        
        .alert-content p:last-child {{
            margin-bottom: 0;
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
            margin: 28px 0;
            font-size: 0.9rem;
            background-color: var(--card-bg);
            border-radius: var(--radius-md);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
        }}
        
        th, td {{
            padding: 14px 20px;
            border: 1px solid var(--border-color);
            text-align: left;
        }}
        
        th {{
            background-color: var(--primary-light);
            color: var(--primary-color);
            font-weight: 700;
        }}
        
        tr:nth-child(even) {{
            background-color: rgba(59, 130, 246, 0.02);
        }}
        
        /* Code blocks */
        pre {{
            background-color: var(--code-bg);
            padding: 20px;
            border-radius: var(--radius-md);
            overflow-x: auto;
            border: 1px solid var(--border-color);
            margin: 28px 0;
            box-shadow: inset 0 1px 3px rgba(0,0,0,0.02);
        }}
        
        code {{
            font-family: 'JetBrains Mono', monospace;
            background-color: var(--code-bg);
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.86rem;
            color: var(--primary-color);
            font-weight: 600;
        }}
        
        pre code {{
            padding: 0;
            background-color: transparent;
            font-size: 0.82rem;
            color: var(--text-color);
            font-weight: 400;
        }}
        
        /* Interactive details / summary styling */
        details {{
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            margin: 16px 0;
            padding: 0;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
        }}
        
        details[open] {{
            border-color: var(--primary-color);
            box-shadow: var(--shadow-md);
        }}
        
        summary {{
            font-weight: 600;
            cursor: pointer;
            outline: none;
            color: var(--text-color);
            user-select: none;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 16px 20px;
            list-style: none;
        }}
        
        summary::-webkit-details-marker {{
            display: none;
        }}
        
        summary::after {{
            content: "→";
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--primary-color);
            transition: transform 0.3s ease;
        }}
        
        details[open] summary::after {{
            transform: rotate(90deg);
        }}
        
        summary:hover {{
            background-color: var(--primary-light);
            color: var(--primary-color);
        }}
        
        .solution-wrapper {{
            padding: 20px;
            border-top: 1px solid var(--border-color);
            background-color: var(--bg-color);
        }}
        
        ul, ol {{
            padding-left: 24px;
            margin: 16px 0;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        /* Dynamic Question Cards Style */
        .question-card {{
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 24px;
            margin: 20px 0;
            box-shadow: var(--shadow-sm);
            position: relative;
            display: flex;
            flex-direction: column;
            gap: 12px;
            border-left: 4px solid var(--border-color);
            transition: all var(--transition-speed) ease;
        }}
        
        .question-card.completed {{
            border-left-color: var(--success-color);
            background-color: rgba(16, 185, 129, 0.01);
        }}
        
        .question-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 16px;
        }}
        
        .question-meta-group {{
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }}
        
        .question-checkbox-label {{
            display: flex;
            align-items: center;
            gap: 8px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.9rem;
            color: var(--text-muted);
            user-select: none;
        }}
        
        .question-checkbox-label input {{
            display: none;
        }}
        
        .checkbox-box {{
            width: 20px;
            height: 20px;
            border: 2px solid var(--text-muted);
            border-radius: 6px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
        }}
        
        .question-checkbox-label input:checked + .checkbox-box {{
            background-color: var(--success-color);
            border-color: var(--success-color);
            color: white;
        }}
        
        .question-checkbox-label input:checked + .checkbox-box::after {{
            content: "✓";
            font-size: 0.78rem;
            font-weight: 900;
        }}
        
        .company-tag {{
            font-size: 0.74rem;
            background-color: var(--primary-light);
            color: var(--primary-color);
            padding: 2px 8px;
            border-radius: 99px;
            font-weight: 700;
            text-transform: uppercase;
        }}
        
        .question-text {{
            font-size: 1.05rem;
            font-weight: 500;
            line-height: 1.6;
        }}
        
        /* Practice progress & tabs widget styles */
        .practice-progress-widget {{
            background: linear-gradient(135deg, var(--card-bg), var(--bg-color));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 28px;
            margin: 32px 0;
            box-shadow: var(--shadow-md);
        }}
        
        .practice-progress-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            margin: 0 0 16px 0;
            border-bottom: none;
            padding-bottom: 0;
        }}
        
        .practice-progress-bar-container {{
            background-color: var(--border-color);
            height: 12px;
            border-radius: 99px;
            overflow: hidden;
            margin-bottom: 12px;
        }}
        
        .practice-progress-bar {{
            background: linear-gradient(90deg, #10b981, #3b82f6);
            height: 100%;
            width: 0%;
            border-radius: 99px;
            transition: width 0.5s ease;
        }}
        
        .practice-progress-stats {{
            display: flex;
            justify-content: space-between;
            font-size: 0.9rem;
            color: var(--text-muted);
            font-weight: 600;
        }}
        
        .tab-menu {{
            display: flex;
            gap: 8px;
            margin: 24px 0 8px 0;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 12px;
            flex-wrap: wrap;
        }}
        
        .tab-btn {{
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 8px 16px;
            border-radius: 99px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.85rem;
            transition: all 0.2s ease;
        }}
        
        .tab-btn:hover {{
            background-color: var(--primary-light);
            color: var(--primary-color);
            border-color: var(--primary-color);
        }}
        
        .tab-btn.active {{
            background-color: var(--primary-color);
            color: white;
            border-color: var(--primary-color);
            box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2);
        }}
        
        /* Math block styling */
        .math-block {{
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            padding: 16px;
            border-radius: var(--radius-md);
            margin: 16px 0;
            font-family: 'JetBrains Mono', monospace;
            overflow-x: auto;
            text-align: center;
            font-weight: 600;
            color: var(--accent-color);
        }}
        
        /* Floating Action Button (Back to Top) */
        .floating-action-btn {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--shadow-lg);
            z-index: 100;
            opacity: 0;
            pointer-events: none;
            transition: all 0.3s ease;
        }}
        
        .floating-action-btn.visible {{
            opacity: 1;
            pointer-events: auto;
        }}
        
        .floating-action-btn:hover {{
            background-color: var(--primary-hover);
            transform: translateY(-4px);
        }}
        
        /* Mobile Hamburger & Controls */
        .mobile-header {{
            display: none;
            background-color: var(--sidebar-bg);
            border-bottom: 1px solid var(--border-color);
            padding: 14px 20px;
            position: sticky;
            top: 0;
            z-index: 100;
            align-items: center;
            justify-content: space-between;
            box-shadow: var(--shadow-sm);
        }}
        
        .mobile-hamburger {{
            background: none;
            border: none;
            color: var(--text-color);
            font-size: 1.5rem;
            cursor: pointer;
        }}
        
        /* Responsive Design */
        @media (max-width: 1024px) {{
            body {{
                flex-direction: column;
            }}
            .sidebar {{
                position: fixed;
                left: 0;
                top: 0;
                bottom: 0;
                transform: translateX(-100%);
                transition: transform 0.3s ease;
                z-index: 200;
                height: 100vh;
                box-shadow: var(--shadow-lg);
            }}
            .sidebar.mobile-open {{
                transform: translateX(0);
            }}
            .mobile-header {{
                display: flex;
            }}
            .container {{
                padding: 30px 24px;
            }}
            .sidebar-overlay {{
                display: none;
                position: fixed;
                inset: 0;
                background-color: rgba(0,0,0,0.5);
                z-index: 150;
            }}
            .sidebar-overlay.visible {{
                display: block;
            }}
            .header-controls {{
                display: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="sidebar-overlay" id="sidebarOverlay"></div>
    <div class="mobile-header">
        <button class="mobile-hamburger" id="mobileHamburger">☰</button>
        <a href="index.html" class="sidebar-brand">🎓 Aptitude Mastery</a>
        <button class="theme-toggle-btn" id="themeToggleMobile">
            <svg class="sun-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
            <svg class="moon-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>
    </div>

    <aside class="sidebar" id="sidebar">
        <div class="sidebar-header">
            <a href="index.html" class="sidebar-brand">
                🎓 Aptitude Mastery
            </a>
            <button class="theme-toggle-btn" id="themeToggleSidebar">
                <svg class="sun-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                <svg class="moon-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
            </button>
        </div>
        
        <div class="sidebar-progress-card">
            <span class="sidebar-progress-label">Guide Progress</span>
            <div class="sidebar-progress-wrapper">
                <div class="sidebar-progress-bar" id="sidebarProgressBar"></div>
            </div>
            <div class="sidebar-progress-stats" id="sidebarProgressStats">0% Completed (0/0 Qs)</div>
        </div>
        
        <hr style="margin: 0; opacity: 0.5;" />
        <div class="sidebar-section-title">Table of Contents</div>
        {toc_html}
        <hr style="margin: 0; opacity: 0.5;" />
        <div class="sidebar-section-title">Topic Guides</div>
        {quick_nav}
    </aside>

    <main class="container">
        <div class="header-controls">
            <button class="collapse-btn" id="collapseSidebarBtn">
                <span>◀ Collapse Sidebar</span>
            </button>
        </div>
        {body_content}
    </main>
    
    <button class="floating-action-btn" id="backToTopBtn" aria-label="Back to Top">▲</button>

    <script>
        // Collapsible Sidebar
        const sidebar = document.getElementById('sidebar');
        const collapseSidebarBtn = document.getElementById('collapseSidebarBtn');
        const mobileHamburger = document.getElementById('mobileHamburger');
        const sidebarOverlay = document.getElementById('sidebarOverlay');

        if (collapseSidebarBtn) {{
            collapseSidebarBtn.addEventListener('click', () => {{
                sidebar.classList.toggle('collapsed');
                if (sidebar.classList.contains('collapsed')) {{
                    collapseSidebarBtn.querySelector('span').innerText = '▶ Expand Sidebar';
                }} else {{
                    collapseSidebarBtn.querySelector('span').innerText = '◀ Collapse Sidebar';
                }}
            }});
        }}

        if (mobileHamburger) {{
            mobileHamburger.addEventListener('click', () => {{
                sidebar.classList.add('mobile-open');
                sidebarOverlay.classList.add('visible');
            }});
        }}

        if (sidebarOverlay) {{
            sidebarOverlay.addEventListener('click', () => {{
                sidebar.classList.remove('mobile-open');
                sidebarOverlay.classList.remove('visible');
            }});
        }}

        // Theme Toggle Functionality
        const themeToggles = [
            document.getElementById('themeToggleSidebar'),
            document.getElementById('themeToggleMobile')
        ];

        themeToggles.forEach(toggle => {{
            if (toggle) {{
                toggle.addEventListener('click', () => {{
                    const currentTheme = document.documentElement.getAttribute('data-theme');
                    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                    document.documentElement.setAttribute('data-theme', newTheme);
                    localStorage.setItem('theme', newTheme);
                }});
            }}
        }});

        // Floating Action Button
        const backToTopBtn = document.getElementById('backToTopBtn');
        window.addEventListener('scroll', () => {{
            if (window.scrollY > 400) {{
                backToTopBtn.classList.add('visible');
            }} else {{
                backToTopBtn.classList.remove('visible');
            }}
        }});
        backToTopBtn.addEventListener('click', () => {{
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }});

        // Dynamic Interactive Quiz / Practice Engine
        document.addEventListener('DOMContentLoaded', () => {{
            const currentFilename = "{filename}";
            const topicKey = "aptitude_progress_" + currentFilename.replace('_study_guide.md', '');

            // 1. Locate Practice Section and Detailed Solutions
            // We search for Practice Section headers by IDs or emojis
            const practiceHeaders = Array.from(document.querySelectorAll('h2')).filter(h => 
                h.textContent.includes('Practice') || h.textContent.includes('PRACTICE')
            );
            
            const solutionsHeaders = Array.from(document.querySelectorAll('h2')).filter(h => 
                h.textContent.includes('Solutions') || h.textContent.includes('SOLUTIONS')
            );

            if (practiceHeaders.length === 0) return;
            const practiceHeader = practiceHeaders[0];

            // 2. Parse separated solutions if they are at the bottom (like ages_study_guide)
            const solutionsMap = new Map();
            let hasSeparatedSolutions = solutionsHeaders.length > 0;
            let solutionsContainer = null;

            if (hasSeparatedSolutions) {{
                solutionsContainer = solutionsHeaders[0];
                let currentEl = solutionsContainer.nextElementSibling;
                let foundSolutionsCount = 0;
                
                while (currentEl && currentEl.tagName !== 'H2') {{
                    // Scan children of solutions block to extract Q1, Q2, etc.
                    const text = currentEl.textContent.trim();
                    const qMatch = text.match(/^\\s*\\*?\\*?Q(?:uestion\\s*)?(\\d+[a-z]?)\\.?\\*?\\*?/i);
                    
                    if (qMatch) {{
                        const qNum = qMatch[1].toLowerCase();
                        // Clean up the Q1. tag from solution html
                        let innerHTML = currentEl.innerHTML;
                        solutionsMap.set(qNum, innerHTML);
                        foundSolutionsCount++;
                    }} else {{
                        // Check if it's a list container containing solutions
                        const listItems = currentEl.querySelectorAll('li');
                        listItems.forEach(li => {{
                            const liText = li.textContent.trim();
                            const liMatch = liText.match(/^\\s*\\*?\\*?Q(?:uestion\\s*)?(\\d+[a-z]?)\\.?\\*?\\*?/i);
                            if (liMatch) {{
                                const qNum = liMatch[1].toLowerCase();
                                solutionsMap.set(qNum, li.innerHTML);
                                foundSolutionsCount++;
                            }}
                        }});
                    }}
                    currentEl = currentEl.nextElementSibling;
                }}
                
                // If we extracted a reasonable number of solutions, we'll inline them dynamically and hide the bottom solutions section!
                if (foundSolutionsCount > 0) {{
                    solutionsContainer.style.display = 'none';
                    let hideEl = solutionsContainer.nextElementSibling;
                    while (hideEl && hideEl.tagName !== 'H2' && !hideEl.textContent.includes('Verdict') && !hideEl.textContent.includes('Verdicts')) {{
                        hideEl.style.display = 'none';
                        hideEl = hideEl.nextElementSibling;
                    }}
                }}
            }}

            // 3. Scan and rewrite Practice Questions into Cards
            // Questions can be in sub-sections (Easy, Medium, Hard, etc.) under the practice header
            let nextEl = practiceHeader.nextElementSibling;
            let questionNumberIndex = 1;
            let currentDifficulty = 'easy'; // default fallback
            
            // Layout widget insertion
            const progressWidget = document.createElement('div');
            progressWidget.className = 'practice-progress-widget';
            progressWidget.innerHTML = `
                <h3 class="practice-progress-title">🎯 Track Your Practice</h3>
                <div class="practice-progress-bar-container">
                    <div class="practice-progress-bar" id="practiceProgressBar"></div>
                </div>
                <div class="practice-progress-stats">
                    <span id="practiceProgressPercent">0% Completed</span>
                    <span id="practiceProgressStatsText">0/0 Solved</span>
                </div>
                <div class="tab-menu" id="difficultyTabMenu">
                    <button class="tab-btn active" data-difficulty="all">All Levels</button>
                    <button class="tab-btn" data-difficulty="easy">🟢 Easy</button>
                    <button class="tab-btn" data-difficulty="medium">🟡 Medium</button>
                    <button class="tab-btn" data-difficulty="hard">🟠 Hard</button>
                    <button class="tab-btn" data-difficulty="product">🔴 Product Co.</button>
                </div>
            `;
            practiceHeader.after(progressWidget);

            const qCards = [];
            let activeCard = null;

            function createQuestionCard(el, isListItem, parentListEl) {{
                const text = el.textContent.trim();
                
                // Parse question number (either explicit e.g. Q12 or implicit from index)
                const explicitMatch = text.match(/^\\s*\\*?\\*?Q(?:uestion\\s*)?(\\d+[a-z]?)\\.?\\*?\\*?/i);
                const qIdRaw = explicitMatch ? explicitMatch[1] : String(questionNumberIndex);
                
                // Parse company tag e.g. [TCS], [Amazon]
                const companyMatch = text.match(/\\[([^\\]]+)\\]\\s*$/);
                const companyName = companyMatch ? companyMatch[1] : '';
                
                // Create card element
                const card = document.createElement('div');
                card.className = `question-card diff-${{currentDifficulty}}`;
                card.setAttribute('data-difficulty', currentDifficulty);
                card.setAttribute('data-qnum', qIdRaw);

                // Check if solution exists (either pre-existing inside details, or extracted from bottom)
                let solutionHTML = '';
                const existingDetails = el.querySelector('details');
                if (existingDetails) {{
                    solutionHTML = existingDetails.querySelector('div, p, ul, ol, pre')?.outerHTML || existingDetails.innerHTML.replace(/<s[u]mmary>.*?<\\/s[u]mmary>/i, '');
                }} else {{
                    const key = qIdRaw.toLowerCase();
                    if (solutionsMap.has(key)) {{
                        solutionHTML = solutionsMap.get(key);
                    }} else {{
                        const keyInt = parseInt(key, 10);
                        if (!isNaN(keyInt) && solutionsMap.has(keyInt)) {{
                            solutionHTML = solutionsMap.get(keyInt);
                        }}
                    }}
                }}

                // Build clean question content text (stripping company tags and solution details if present)
                let questionCleanText = el.innerHTML;
                if (existingDetails) {{
                    questionCleanText = questionCleanText.replace(existingDetails.outerHTML, '');
                }}
                // Strip the trailing company tag from question representation
                if (companyMatch) {{
                    questionCleanText = questionCleanText.replace(companyMatch[0], '');
                }}

                // Check localStorage for completion state
                const isCompleted = localStorage.getItem(`${{topicKey}}_q${{qIdRaw}}`) === 'true';
                if (isCompleted) {{
                    card.classList.add('completed');
                }}

                card.innerHTML = `
                    <div class="question-header">
                        <div class="question-meta-group">
                            <span class="company-tag" style="background-color: var(--primary-light); color: var(--primary-color);">Q${{qIdRaw}}</span>
                            ${{companyName ? `<span class="company-tag" style="background-color: var(--accent-light); color: var(--accent-color);">${{companyName}}</span>` : ''}}
                        </div>
                        <label class="question-checkbox-label">
                            <input type="checkbox" class="q-checkbox" data-qnum="${{qIdRaw}}" ${{isCompleted ? 'checked' : ''}}>
                            <span class="checkbox-box"></span>
                            Done
                        </label>
                    </div>
                    <div class="question-text">${{questionCleanText}}</div>
                `;

                // Append Solution if exists
                if (solutionHTML) {{
                    const detailsEl = document.createElement('details');
                    const summaryEl = document.createElement('summary');
                    summaryEl.innerHTML = "🔍 View Detailed Solution";
                    detailsEl.appendChild(summaryEl);
                    
                    const wrapperEl = document.createElement('div');
                    wrapperEl.className = "solution-wrapper";
                    wrapperEl.innerHTML = solutionHTML;
                    detailsEl.appendChild(wrapperEl);
                    
                    card.appendChild(detailsEl);
                }}

                // Insert card
                if (isListItem && parentListEl) {{
                    parentListEl.parentNode.insertBefore(card, parentListEl);
                }} else {{
                    el.parentNode.insertBefore(card, el);
                }}

                qCards.push(card);
                questionNumberIndex++;
                return card;
            }}

            while (nextEl && nextEl.tagName !== 'H2' && nextEl !== solutionsContainer) {{
                // Detect difficulty section change
                const textVal = nextEl.textContent.toLowerCase();
                if (nextEl.tagName === 'H3') {{
                    if (textVal.includes('easy')) currentDifficulty = 'easy';
                    else if (textVal.includes('medium')) currentDifficulty = 'medium';
                    else if (textVal.includes('hard')) currentDifficulty = 'hard';
                    else if (textVal.includes('product') || textVal.includes('advanced')) currentDifficulty = 'product';
                    
                    nextEl = nextEl.nextElementSibling;
                    continue;
                }}

                // Check if it is a list
                const isList = nextEl.tagName === 'OL' || nextEl.tagName === 'UL';
                // A list is a question list if it is OL, or if it is a UL where the first item starts with a question marker
                const isQuestionList = nextEl.tagName === 'OL' || (nextEl.tagName === 'UL' && nextEl.children.length > 0 && /^\\s*(\\d+|Q\\d+|Question\\s*\\d+)\\b/i.test(nextEl.children[0].textContent.trim()));

                if (isList && isQuestionList) {{
                    const listItems = Array.from(nextEl.children);
                    const listEl = nextEl;
                    nextEl = nextEl.nextElementSibling; // save sibling before removing list
                    
                    listItems.forEach(li => {{
                        activeCard = createQuestionCard(li, true, listEl);
                    }});
                    listEl.remove();
                }} else if (nextEl.tagName === 'P' && (textVal.startsWith('**q') || textVal.startsWith('q') || textVal.startsWith('**question'))) {{
                    const el = nextEl;
                    nextEl = nextEl.nextElementSibling; // save sibling before removing paragraph
                    
                    activeCard = createQuestionCard(el, false, null);
                    el.remove();
                }} else {{
                    const el = nextEl;
                    nextEl = nextEl.nextElementSibling; // save sibling before moving element
                    
                    if (activeCard) {{
                        activeCard.querySelector('.question-text').appendChild(el);
                    }}
                }}
            }}

            // 4. Implement event listeners for checklists and tabs
            const updateProgress = () => {{
                const checkedCount = qCards.filter(card => card.querySelector('.q-checkbox').checked).length;
                const totalCount = qCards.length;
                const percent = totalCount > 0 ? Math.round((checkedCount / totalCount) * 100) : 0;
                
                // Update practice section widgets
                document.getElementById('practiceProgressBar').style.width = `${{percent}}%`;
                document.getElementById('practiceProgressPercent').innerText = `${{percent}}% Completed`;
                document.getElementById('practiceProgressStatsText').innerText = `${{checkedCount}}/${{totalCount}} Solved`;
                
                // Update sidebar progress widgets
                document.getElementById('sidebarProgressBar').style.width = `${{percent}}%`;
                document.getElementById('sidebarProgressStats').innerText = `${{percent}}% Completed (${{checkedCount}}/${{totalCount}} Qs)`;
                
                // Update localStorage topic overall percentage for main dashboard
                localStorage.setItem(`aptitude_topic_percent_${{currentFilename.replace('_study_guide.md', '')}}`, percent);
                localStorage.setItem(`aptitude_topic_solved_${{currentFilename.replace('_study_guide.md', '')}}`, checkedCount);
                localStorage.setItem(`aptitude_topic_total_${{currentFilename.replace('_study_guide.md', '')}}`, totalCount);
            }};

            qCards.forEach(card => {{
                const cb = card.querySelector('.q-checkbox');
                cb.addEventListener('change', (e) => {{
                    const checked = e.target.checked;
                    const qnum = e.target.getAttribute('data-qnum');
                    localStorage.setItem(`${{topicKey}}_q${{qnum}}`, checked);
                    
                    if (checked) {{
                        card.classList.add('completed');
                    }} else {{
                        card.classList.remove('completed');
                    }}
                    updateProgress();
                }});
            }});

            // Tabs Filtering Logic
            const tabButtons = document.querySelectorAll('#difficultyTabMenu .tab-btn');
            tabButtons.forEach(btn => {{
                btn.addEventListener('click', (e) => {{
                    tabButtons.forEach(b => b.classList.remove('active'));
                    e.target.classList.add('active');
                    
                    const selectedDiff = e.target.getAttribute('data-difficulty');
                    
                    qCards.forEach(card => {{
                        if (selectedDiff === 'all' || card.getAttribute('data-difficulty') === selectedDiff) {{
                            card.style.display = 'flex';
                        }} else {{
                            card.style.display = 'none';
                        }}
                    }});
                }});
            }});

            // Initial progress calculations
            updateProgress();
        }});
    </script>
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
    html_name = "index.html"
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
<html lang="en" data-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Aptitude Placement Mastery Guide</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <script>
        // Sync theme immediately to prevent flashing
        (function() {{
            const savedTheme = localStorage.getItem('theme') || 'light';
            document.documentElement.setAttribute('data-theme', savedTheme);
        }})();
    </script>
    <style>
        :root {{
            --bg-color: #f8fafc;
            --text-color: #0f172a;
            --text-muted: #64748b;
            --card-bg: #ffffff;
            --border-color: #e2e8f0;
            --primary-color: #2563eb;
            --primary-hover: #1d4ed8;
            --primary-light: #eff6ff;
            --primary-dark: #1e40af;
            --accent-color: #8b5cf6;
            --accent-light: #f5f3ff;
            
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --danger-color: #ef4444;
            
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08), 0 2px 4px -1px rgba(0, 0, 0, 0.04);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
            --radius-md: 12px;
            --radius-lg: 16px;
            --transition-speed: 0.3s;
        }}
        
        [data-theme="dark"] {{
            --bg-color: #090d16;
            --text-color: #f1f5f9;
            --text-muted: #94a3b8;
            --card-bg: #1f293d;
            --border-color: #1f293d;
            --primary-color: #3b82f6;
            --primary-hover: #60a5fa;
            --primary-light: rgba(59, 130, 246, 0.15);
            --primary-dark: #2563eb;
            --accent-color: #a78bfa;
            --accent-light: rgba(139, 92, 246, 0.15);
            --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.5);
            --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
            --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.4);
        }}
        
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            transition: background-color var(--transition-speed) ease, border-color var(--transition-speed) ease;
        }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
            background-image: radial-gradient(circle at 10% 20%, rgba(59, 130, 246, 0.02) 0%, transparent 40%),
                              radial-gradient(circle at 90% 80%, rgba(79, 70, 229, 0.02) 0%, transparent 40%);
            background-attachment: fixed;
            min-height: 100vh;
        }}
        
        /* Navigation header */
        .navbar {{
            background-color: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            padding: 16px 40px;
            position: sticky;
            top: 0;
            z-index: 100;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: var(--shadow-sm);
        }}
        
        [data-theme="dark"] .navbar {{
            background-color: rgba(17, 24, 39, 0.85);
        }}
        
        .navbar-brand {{
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 1.35rem;
            color: var(--primary-color);
            display: flex;
            align-items: center;
            gap: 8px;
            text-decoration: none;
            transition: opacity 0.2s ease;
        }}
        
        .navbar-brand:hover {{
            opacity: 0.85;
        }}
        
        .theme-toggle-btn {{
            background: none;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: var(--bg-color);
            border: 1px solid var(--border-color);
            transition: all 0.2s ease;
        }}
        
        .theme-toggle-btn:hover {{
            color: var(--primary-color);
            transform: scale(1.05);
        }}
        
        .sun-icon {{ display: block; }}
        .moon-icon {{ display: none; }}
        
        [data-theme="dark"] .sun-icon {{ display: none; }}
        [data-theme="dark"] .moon-icon {{ display: block; }}
        
        /* Hero Section styling */
        .hero {{
            padding: 80px 40px 40px 40px;
            text-align: center;
            max-width: 1000px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 16px;
        }}
        
        .hero h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 3.25rem;
            color: var(--text-color);
            font-weight: 800;
            letter-spacing: -0.02em;
            line-height: 1.25;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .hero p {{
            font-size: 1.2rem;
            color: var(--text-muted);
            max-width: 650px;
            line-height: 1.7;
        }}
        
        .hero-stats {{
            display: flex;
            justify-content: center;
            gap: 32px;
            margin-top: 24px;
            flex-wrap: wrap;
        }}
        
        .stat-item {{
            display: flex;
            flex-direction: column;
            gap: 4px;
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            padding: 16px 28px;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
            min-width: 160px;
        }}
        
        .stat-val {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.25rem;
            font-weight: 800;
            color: var(--primary-color);
        }}
        
        .stat-label {{
            font-size: 0.76rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            font-weight: 700;
        }}
        
        /* Overall Progress Hero Card */
        .overall-progress-hero {{
            background: linear-gradient(135deg, var(--card-bg), var(--bg-color));
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 30px;
            margin: 20px 0 40px 0;
            box-shadow: var(--shadow-md);
        }}
        
        /* Main Layout */
        .main-content {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 40px 80px 40px;
        }}
        
        .section-header {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.85rem;
            color: var(--text-color);
            margin: 60px 0 24px 0;
            font-weight: 700;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 12px;
            letter-spacing: -0.01em;
        }}
        
        /* Live Search Section */
        .search-container {{
            background: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 16px 24px;
            margin-bottom: 30px;
            display: flex;
            gap: 16px;
            align-items: center;
            box-shadow: var(--shadow-sm);
        }}
        
        .search-icon {{
            font-size: 1.25rem;
            color: var(--text-muted);
        }}
        
        .search-input {{
            flex: 1;
            border: none;
            outline: none;
            background: transparent;
            font-family: inherit;
            font-size: 1.05rem;
            color: var(--text-color);
        }}
        
        .search-input::placeholder {{
            color: var(--text-muted);
            opacity: 0.75;
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
            border-radius: var(--radius-lg);
            padding: 28px;
            display: flex;
            flex-direction: column;
            gap: 16px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: var(--shadow-sm);
            position: relative;
            overflow: hidden;
        }}
        
        .topic-card:hover {{
            transform: translateY(-6px);
            box-shadow: var(--shadow-lg);
            border-color: var(--primary-light);
        }}
        
        .card-header {{
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .card-emoji {{
            font-size: 1.35rem;
        }}
        
        .card-rank {{
            font-size: 0.78rem;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        
        .status-badge {{
            font-size: 0.72rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 99px;
            margin-left: auto;
            text-transform: uppercase;
            letter-spacing: 0.02em;
        }}
        
        .status-quant {{
            background-color: var(--primary-light);
            color: var(--primary-color);
        }}
        
        .status-lr-di {{
            background-color: var(--accent-light);
            color: var(--accent-color);
        }}
        
        .card-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--text-color);
        }}
        
        .card-desc {{
            font-size: 0.92rem;
            color: var(--text-muted);
            line-height: 1.6;
            flex: 1;
        }}
        
        .card-meta {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
            border-top: 1px solid var(--border-color);
            padding-top: 18px;
        }}
        
        .meta-item {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        
        .meta-label {{
            font-size: 0.68rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            font-weight: 700;
        }}
        
        .meta-stars {{
            font-size: 0.88rem;
            color: var(--warning-color);
        }}
        
        .meta-badge {{
            font-size: 0.74rem;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 6px;
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
            font-weight: 700;
            color: var(--text-color);
        }}
        
        .card-btn {{
            display: block;
            text-align: center;
            padding: 12px 18px;
            border-radius: var(--radius-sm);
            font-weight: 700;
            font-size: 0.92rem;
            text-decoration: none;
            transition: all 0.2s ease;
        }}
        
        .btn-start {{
            background-color: var(--primary-color);
            color: #ffffff;
            box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.15);
        }}
        
        .btn-start:hover {{
            background-color: var(--primary-hover);
            transform: translateY(-2px);
            box-shadow: 0 6px 8px -1px rgba(37, 99, 235, 0.2);
        }}
        
        .btn-disabled {{
            background-color: var(--border-color);
            color: var(--text-muted);
            cursor: not-allowed;
            pointer-events: none;
            opacity: 0.65;
        }}
        
        /* Tables styling */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 24px 0;
            background-color: var(--card-bg);
            border-radius: var(--radius-md);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
        }}
        
        th, td {{
            padding: 14px 20px;
            border: 1px solid var(--border-color);
            text-align: left;
        }}
        
        th {{
            background-color: var(--primary-light);
            color: var(--primary-color);
            font-weight: 700;
        }}
        
        tr:nth-child(even) {{
            background-color: rgba(59, 130, 246, 0.01);
        }}
        
        /* Alerts styling */
        .alert {{
            display: flex;
            border-left: 4px solid;
            padding: 18px;
            border-radius: var(--radius-md);
            margin: 24px 0;
            background: var(--card-bg);
            box-shadow: var(--shadow-sm);
        }}
        
        .alert-icon {{
            font-size: 1.35rem;
            margin-right: 14px;
            display: flex;
            align-items: center;
        }}
        
        .alert-content {{
            flex: 1;
        }}
        
        .alert-important {{
            border-left-color: var(--accent-color);
            background-color: var(--accent-light);
        }}
        
        .alert-note {{
            border-left-color: var(--primary-color);
            background-color: var(--primary-light);
        }}
        
        .alert-tip {{
            border-left-color: #10b981;
            background-color: rgba(16, 185, 129, 0.05);
        }}
        
        ul, ol {{
            padding-left: 24px;
            margin: 16px 0;
        }}
        
        li {{
            margin-bottom: 8px;
        }}
        
        /* Responsive Grid fixes */
        @media (max-width: 768px) {{
            .navbar {{
                padding: 16px 24px;
            }}
            .hero h1 {{
                font-size: 2.25rem;
            }}
            .hero-stats {{
                gap: 16px;
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
        <a href="index.html" class="navbar-brand">
            🎓 Aptitude Placement Mastery Portal
        </a>
        <button class="theme-toggle-btn" id="themeToggle">
            <svg class="sun-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
            <svg class="moon-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </button>
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
        // Theme Toggle Functionality
        const themeToggle = document.getElementById('themeToggle');
        if (themeToggle) {{
            themeToggle.addEventListener('click', () => {{
                const currentTheme = document.documentElement.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);
            }});
        }}

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

        // Dynamic Card Progress Tracking Aggregator
        document.addEventListener('DOMContentLoaded', () => {{
            const topics = [
                "number_systems_simplification", "percentages", "profit_loss_discount", 
                "simple_compound_interest", "time_work", "time_speed_distance", 
                "averages_ratio_proportion", "mixtures_alligations", "probability",
                "permutations_combinations", "ages", "coding_decoding", 
                "blood_relations", "clocks_calendar", "data_interpretation"
            ];
            
            let totalSolved = 0;
            let totalQuestions = 0;
            
            topics.forEach(t => {{
                // Read metrics calculated by individual study guide pages
                const percent = parseInt(localStorage.getItem(`aptitude_topic_percent_${{t}}`) || 0, 10);
                const solved = parseInt(localStorage.getItem(`aptitude_topic_solved_${{t}}`) || 0, 10);
                const total = parseInt(localStorage.getItem(`aptitude_topic_total_${{t}}`) || 0, 10);
                
                totalSolved += solved;
                totalQuestions += total;
                
                // Find matching card and inject its mini progress widget
                const cards = Array.from(document.querySelectorAll('.topic-card'));
                const matchedCard = cards.find(c => {{
                    const href = c.querySelector('.card-btn')?.getAttribute('href');
                    return href && href.includes(t);
                }});
                
                if (matchedCard && total > 0) {{
                    const progressDiv = document.createElement('div');
                    progressDiv.className = 'card-progress-section';
                    progressDiv.style.marginTop = '12px';
                    progressDiv.style.paddingTop = '12px';
                    progressDiv.style.borderTop = '1px solid var(--border-color)';
                    
                    progressDiv.innerHTML = `
                        <div style="display:flex; justify-content:space-between; font-size:0.72rem; font-weight:700; margin-bottom:4px; color:var(--text-muted);">
                            <span>TOPIC PROGRESS</span>
                            <span>${{percent}}% (${{solved}}/${{total}} Qs)</span>
                        </div>
                        <div style="background-color:var(--border-color); height:6px; border-radius:99px; overflow:hidden;">
                            <div style="background:linear-gradient(90deg, var(--primary-color), var(--accent-color)); height:100%; width:${{percent}}%; border-radius:99px;"></div>
                        </div>
                    `;
                    // Insert before the button
                    const btn = matchedCard.querySelector('.card-btn');
                    matchedCard.insertBefore(progressDiv, btn);
                }}
            }});
            
            // Insert Overall progress aggregator card at the top of Ranked Topics section
            if (totalQuestions > 0) {{
                const overallPercent = Math.round((totalSolved / totalQuestions) * 100);
                const progressHeroCard = document.createElement('div');
                progressHeroCard.className = 'overall-progress-hero';
                progressHeroCard.innerHTML = `
                    <div style="display:flex; flex-direction:column; gap:12px;">
                        <h3 style="margin:0; font-family:'Outfit',sans-serif; font-size:1.3rem; font-weight:800; color:var(--text-color);">📈 Overall Syllabus Completion</h3>
                        <div style="display:flex; justify-content:space-between; align-items:center; font-weight:700; font-size:0.95rem;">
                            <span style="color:var(--success-color);">${{overallPercent}}% Solved</span>
                            <span style="color:var(--text-muted);">${{totalSolved}} / ${{totalQuestions}} Questions Practiced</span>
                        </div>
                        <div style="background-color:var(--border-color); height:12px; border-radius:99px; overflow:hidden; box-shadow:inset 0 1px 2px rgba(0,0,0,0.05);">
                            <div style="background:linear-gradient(90deg, #10b981, #2563eb, #8b5cf6); height:100%; width:${{overallPercent}}%; border-radius:99px; transition:width 0.5s ease;"></div>
                        </div>
                    </div>
                `;
                
                const searchContainer = document.querySelector('.search-container');
                if (searchContainer) {{
                    searchContainer.parentNode.insertBefore(progressHeroCard, searchContainer);
                }}
            }}
        }});
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
