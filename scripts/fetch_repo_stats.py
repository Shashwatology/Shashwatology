#!/usr/bin/env python3
import json
import urllib.request

url = 'https://api.github.com/users/shashwatology/repos?per_page=100'
req = urllib.request.Request(url, headers={'User-Agent': 'ResearchPortfolio/1.0 (mailto:shashwatology.s@gmail.com)'})

try:
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read().decode('utf-8'))
        print(f"Total public repos: {len(repos)}")
        total_stars = sum(r.get('stargazers_count', 0) for r in repos)
        total_forks = sum(r.get('forks_count', 0) for r in repos)
        
        lang_counts = {}
        for r in repos:
            l = r.get('language')
            if l:
                lang_counts[l] = lang_counts.get(l, 0) + 1
                
        # Calculate language percentages
        tot_langs = sum(lang_counts.values()) or 1
        lang_dist = [
            {"name": k, "count": v, "pct": round((v / tot_langs) * 100, 1)}
            for k, v in sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)
        ]
        
        top_repos = []
        # Key repos mentioned in resume
        featured_names = [
            "PhysioFM", "SentinelAI", "semantic-drift-vlm-attacks",
            "Guardian-Travel-Twin-", "IMPACT-Multimodal-Transit", "WardOS-BreatheSync"
        ]
        for r in repos:
            top_repos.append({
                "name": r.get("name"),
                "desc": r.get("description") or "",
                "stars": r.get("stargazers_count", 0),
                "forks": r.get("forks_count", 0),
                "lang": r.get("language") or "Python",
                "url": r.get("html_url")
            })
            
        stats = {
            "username": "shashwatology",
            "public_repos": len(repos),
            "total_stars": total_stars,
            "total_forks": total_forks,
            "languages": lang_dist,
            "top_repos": top_repos[:6]
        }
        
        with open("data/github_stats.json", "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)
        print("Saved data/github_stats.json successfully!")
        print(f"Total stars: {total_stars}, Forks: {total_forks}")
        print("Languages:", lang_dist)
except Exception as e:
    print("Error fetching repos:", e)

