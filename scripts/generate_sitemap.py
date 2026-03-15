
import os
from datetime import datetime

def generate_sitemap(base_url="https://www.example.com"):
    sitemap_path = os.path.join(os.path.dirname(__file__), "..", "docs", "sitemap.xml")
    
    # Get current date in YYYY-MM-DD format
    lastmod = datetime.now().strftime("%Y-%m-%d")
    
    urls = [
        "index.html",
        "webhook.html"
    ]

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    for url in urls:
        full_url = f"{base_url}/{url}"
        sitemap_content += f"""  <url>
    <loc>{full_url}</loc>
    <lastmod>{lastmod}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""
    sitemap_content += "</urlset>"

    with open(sitemap_path, "w") as f:
        f.write(sitemap_content)
    
    print(f"Sitemap generated at {sitemap_path}")

if __name__ == "__main__":
    generate_sitemap()
