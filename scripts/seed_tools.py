import json

# Adding high-quality SaaS tools with strong affiliate programs
new_tools = [
    {
        "id": "make-com",
        "name": "Make (Integromat)",
        "category": "automation",
        "description": "Visual platform to design, build, and automate anything. Connects 1000+ apps.",
        "integration_difficulty": "Medium",
        "affiliate_link": "https://www.make.com/en/register?pc=agentstack"
    },
    {
        "id": "gorgias",
        "name": "Gorgias",
        "category": "support",
        "description": "E-commerce helpdesk that turns customer service into a profit center.",
        "integration_difficulty": "Low",
        "affiliate_link": "https://gorgias.grsm.io/agentstack"
    },
    {
        "id": "retool",
        "name": "Retool",
        "category": "internal",
        "description": "Build internal tools remarkably fast. Connects to any database or API.",
        "integration_difficulty": "High",
        "affiliate_link": "https://retool.com/?ref=agentstack"
    },
    {
        "id": "clay-run",
        "name": "Clay",
        "category": "sales",
        "description": "Automate outbound campaigns and enrich leads combining 50+ data providers.",
        "integration_difficulty": "Medium",
        "affiliate_link": "https://clay.com/?via=agentstack"
    },
    {
        "id": "jasper-ai",
        "name": "Jasper",
        "category": "marketing",
        "description": "AI copilot for enterprise marketing teams.",
        "integration_difficulty": "Low",
        "affiliate_link": "https://jasper.ai?fpr=agentstack"
    }
]

def update_tools_db():
    print("Updating AgentStack tools database...")
    data_path = 'AgentStack/data/tools.json'
    
    with open(data_path, 'r') as f:
        data = json.load(f)
    
    # Check for duplicates before appending
    existing_ids = {t['id'] for t in data.get('tools', [])}
    added_count = 0
    
    for tool in new_tools:
        if tool['id'] not in existing_ids:
            data['tools'].append(tool)
            added_count += 1
            
    with open(data_path, 'w') as f:
        json.dump(data, f, indent=2)
        
    print(f"Successfully added {added_count} new tools to the database.")

if __name__ == "__main__":
    update_tools_db()
