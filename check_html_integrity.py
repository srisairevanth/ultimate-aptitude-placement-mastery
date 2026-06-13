import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\sai\OneDrive\Desktop\Aptitude"

expected_files = [
    "index.html",
    "averages_ratio_proportion_study_guide.html",
    "mixtures_alligations_study_guide.html",
    "number_systems_simplification_study_guide.html",
    "percentages_study_guide.html",
    "probability_study_guide.html",
    "profit_loss_discount_study_guide.html",
    "simple_compound_interest_study_guide.html",
    "time_speed_distance_study_guide.html",
    "time_work_study_guide.html"
]

all_passed = True

print("=== STARTING HTML PORTAL INTEGRITY CHECK ===")

for filename in expected_files:
    file_path = os.path.join(workspace_dir, filename)
    if not os.path.exists(file_path):
        print(f"❌ Missing file: {filename}")
        all_passed = False
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check basics
    if not content.strip().startswith("<!DOCTYPE html>"):
        print(f"❌ {filename}: Does not start with <!DOCTYPE html>")
        all_passed = False
        
    if "</html>" not in content:
        print(f"❌ {filename}: Missing closing </html> tag")
        all_passed = False

    # Check for unparsed markdown elements
    # 1. Unconverted header markers (e.g. ## or ### at the start of a line)
    unconverted_headers = re.findall(r"^#+\s+.*$", content, re.MULTILINE)
    if unconverted_headers:
        print(f"❌ {filename}: Contains unconverted markdown headers: {unconverted_headers}")
        all_passed = False

    # 2. Unconverted alerts (e.g. [!NOTE])
    unconverted_alerts = re.findall(r"\[!(NOTE|TIP|WARNING|IMPORTANT)\]", content)
    if unconverted_alerts:
        print(f"❌ {filename}: Contains unconverted alert markers: {unconverted_alerts}")
        all_passed = False

    # 3. Leftover .md links
    leftover_md_links = re.findall(r'href="[^"]+\.md"', content)
    if leftover_md_links:
        print(f"❌ {filename}: Contains links to markdown files: {leftover_md_links}")
        all_passed = False

    # 4. Check details elements
    details_count = content.count("<details>")
    summary_count = content.count("<summary>")
    if details_count != summary_count:
        print(f"❌ {filename}: details count ({details_count}) and summary count ({summary_count}) mismatch!")
        all_passed = False

    # Check sidebars and titles
    if "sidebar" not in content and filename != "index.html":
        print(f"❌ {filename}: Missing sidebar navigation structure")
        all_passed = False

if all_passed:
    print("✨ ALL CHECKS PASSED SUCCESSFULLY! The portal is structurally 100% sound.")
else:
    print("⚠️ Integrity check completed with errors. Please review the output above.")
