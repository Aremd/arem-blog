"""
Generate SVG cover images for Arem blog articles.
Usage: python3 scripts/generate-covers.py <theme> <article-dir>
Example: python3 scripts/generate-covers.py governance content/en/post/my-article/

Themes: pharos, governance

To add cover to article front matter: image: cover.png
"""
import os, sys

TEMPLATES = {
    "pharos": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630"><defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#152540"/><stop offset="100%" style="stop-color:#1e3555"/></linearGradient></defs><rect width="1200" height="630" fill="url(#g)"/><circle cx="600" cy="300" r="200" fill="none" stroke="#6db0e8" stroke-width="2.5" opacity="0.45"/><circle cx="600" cy="300" r="140" fill="none" stroke="#6db0e8" stroke-width="2" opacity="0.55"/><circle cx="600" cy="300" r="80" fill="none" stroke="#6db0e8" stroke-width="1.5" opacity="0.65"/><circle cx="600" cy="300" r="280" fill="none" stroke="#4a90c9" stroke-width="1.5" opacity="0.3"/><circle cx="600" cy="300" r="14" fill="#7ec0f5" opacity="0.8"/><circle cx="600" cy="300" r="30" fill="#7ec0f5" opacity="0.15"/><circle cx="380" cy="200" r="10" fill="#7ec0f5" opacity="0.7"/><circle cx="820" cy="400" r="10" fill="#7ec0f5" opacity="0.7"/><circle cx="450" cy="450" r="8" fill="#7ec0f5" opacity="0.6"/><circle cx="780" cy="180" r="8" fill="#7ec0f5" opacity="0.6"/><circle cx="250" cy="350" r="6" fill="#7ec0f5" opacity="0.55"/><circle cx="950" cy="250" r="6" fill="#7ec0f5" opacity="0.55"/><circle cx="200" cy="150" r="5" fill="#7ec0f5" opacity="0.45"/><circle cx="1000" cy="480" r="5" fill="#7ec0f5" opacity="0.45"/><line x1="600" y1="300" x2="380" y2="200" stroke="#6db0e8" stroke-width="2" opacity="0.45"/><line x1="600" y1="300" x2="820" y2="400" stroke="#6db0e8" stroke-width="2" opacity="0.45"/><line x1="600" y1="300" x2="450" y2="450" stroke="#6db0e8" stroke-width="1.5" opacity="0.4"/><line x1="600" y1="300" x2="780" y2="180" stroke="#6db0e8" stroke-width="1.5" opacity="0.4"/><line x1="380" y1="200" x2="250" y2="350" stroke="#6db0e8" stroke-width="1" opacity="0.35"/><line x1="820" y1="400" x2="950" y2="250" stroke="#6db0e8" stroke-width="1" opacity="0.35"/><line x1="250" y1="350" x2="200" y2="150" stroke="#6db0e8" stroke-width="0.8" opacity="0.3"/><line x1="950" y1="250" x2="1000" y2="480" stroke="#6db0e8" stroke-width="0.8" opacity="0.3"/><line x1="450" y1="450" x2="250" y2="350" stroke="#6db0e8" stroke-width="0.8" opacity="0.3"/><line x1="780" y1="180" x2="950" y2="250" stroke="#6db0e8" stroke-width="0.8" opacity="0.3"/></svg>',

    "governance": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630"><defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#152540"/><stop offset="100%" style="stop-color:#1e3555"/></linearGradient></defs><rect width="1200" height="630" fill="url(#g)"/><path d="M0,400 Q200,150 500,300 Q800,450 1200,200" fill="none" stroke="#6db0e8" stroke-width="4" opacity="0.7"/><path d="M0,450 Q250,200 550,350 Q850,500 1200,250" fill="none" stroke="#6db0e8" stroke-width="3" opacity="0.5"/><path d="M0,350 Q150,180 450,280 Q750,400 1200,180" fill="none" stroke="#4a90c9" stroke-width="2" opacity="0.4"/><circle cx="250" cy="230" r="8" fill="#7ec0f5" opacity="0.8"/><circle cx="500" cy="300" r="14" fill="#7ec0f5" opacity="0.6"/><circle cx="500" cy="300" r="30" fill="#7ec0f5" opacity="0.12"/><circle cx="750" cy="420" r="8" fill="#7ec0f5" opacity="0.7"/><circle cx="1000" cy="230" r="7" fill="#7ec0f5" opacity="0.6"/><circle cx="150" cy="350" r="4" fill="#7ec0f5" opacity="0.5"/><circle cx="400" cy="200" r="4" fill="#7ec0f5" opacity="0.45"/><circle cx="650" cy="350" r="5" fill="#7ec0f5" opacity="0.5"/><circle cx="900" cy="300" r="4" fill="#7ec0f5" opacity="0.45"/><circle cx="1100" cy="280" r="4" fill="#7ec0f5" opacity="0.4"/></svg>',
}

def generate(theme, output_dir):
    if theme not in TEMPLATES:
        print(f"Unknown theme: {theme}. Available: {', '.join(TEMPLATES.keys())}")
        return
    svg_path = os.path.join(output_dir, "cover.svg")
    png_path = os.path.join(output_dir, "cover.png")
    with open(svg_path, "w") as f:
        f.write(TEMPLATES[theme])
    os.system(f'sips -s format png --resampleWidth 1200 "{svg_path}" --out "{png_path}" > /dev/null 2>&1')
    print(f"Generated: {svg_path} + {png_path}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        generate(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python3 scripts/generate-covers.py <theme> <article-dir>")
        print(f"Themes: {', '.join(TEMPLATES.keys())}")
