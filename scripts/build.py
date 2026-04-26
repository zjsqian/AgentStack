import json
import os
from datetime import datetime

def build_site():
    print("Building AgentStack site...")
    data_path = 'data/tools.json'
    template_path = 'docs/index.html'
    sitemap_path = 'docs/sitemap.xml'
    
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        return

    with open(data_path, 'r') as f:
        data = json.load(f)

    tools_html = ""
    for tool in data.get('tools', []):
        card = f"""
        <div class="tool-card">
            <div class="tool-title">{tool['name']}</div>
            <span class="tag">{tool['category']}</span>
            <span class="tag">Difficulty: {tool['integration_difficulty']}</span>
            <p>{tool['description']}</p>
            <a href="{tool['affiliate_link']}" class="btn" target="_blank">Get Integration</a>
        </div>
        """
        tools_html += card

    with open(template_path, 'r') as f:
        template = f.read()

    # Replace the placeholder
    placeholder = "<!-- Tools will be injected here via build script -->"
    if placeholder in template:
        new_content = template.replace(placeholder, tools_html)
    else:
        # Fallback if placeholder is missing
        new_content = template.replace("<p>Loading tools...</p>", tools_html)

    with open(template_path, 'w') as f:
        f.write(new_content)
    
    # Update sitemap date
    if os.path.exists(sitemap_path):
        print("Updating sitemap.xml date...")
        today = datetime.now().strftime("%Y-%m-%d")
        with open(sitemap_path, 'r') as f:
            lines = f.readlines()
        
        updated_lines = []
        for line in lines:
            if "<lastmod>" in line:
                updated_lines.append(f"    <lastmod>{today}</lastmod>\n")
            else:
                updated_lines.append(line)
        
        with open(sitemap_path, 'w') as f:
            f.writelines(updated_lines)

    print("Build complete. Output written to AgentStack/docs/index.html")

if __name__ == "__main__":
    build_site()
