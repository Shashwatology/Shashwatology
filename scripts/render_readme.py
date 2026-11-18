#!/usr/bin/env python3
"""
Generate the ultra-tight, zero-wasted-space Master Revision V3.3 GitHub Profile README.md
for Shashwat Upadhyay. Every <br><br> dead gap is eliminated and side-by-side image rows
use subpixel-safe percentage widths (19.8%, 33%, 49.6%) so they never orphan-wrap on GitHub.
"""

import os
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
README_PATH = os.path.join(ROOT, "README.md")
STATS_PATH = os.path.join(ROOT, "data", "github_stats.json")


def generate_readme():
    public_repos = 46
    if os.path.exists(STATS_PATH):
        with open(STATS_PATH, "r", encoding="utf-8") as sf:
            stats = json.load(sf)
            public_repos = stats.get("public_repos", 46)

    readme_content = f"""<!--
  SHASHWAT UPADHYAY — RESEARCH IN MOTION (Master Revision V3.3)
  Compact Swiss Editorial AI Research Portfolio & Automated Design System
  Ground Truth: Shashwat_Research_Resume_2026-10-28.pdf
-->

<div align="center">

<!-- 00 · COMPACT HERO CARD + ICON QUICK-LINK BAR -->
<a href="https://github.com/Shashwatology"><img src="./cards/hero.svg" width="100%" alt="Shashwat Upadhyay — Research in Motion. Independent AI Researcher." /></a><br><a href="https://github.com/Shashwatology"><img src="./cards/nav-github.svg" width="19.8%" alt="GitHub" /></a><a href="https://scholar.google.com/citations?user=ulC0-soAAAAJ"><img src="./cards/nav-scholar.svg" width="19.8%" alt="Google Scholar" /></a><a href="https://www.linkedin.com/in/shashwatupadhyay/"><img src="./cards/nav-linkedin.svg" width="19.8%" alt="LinkedIn" /></a><a href="https://www.researchgate.net/profile/Shashwat-Upadhyay-2"><img src="./cards/nav-researchgate.svg" width="19.8%" alt="ResearchGate" /></a><a href="mailto:shashwatology.s@gmail.com"><img src="./cards/nav-email.svg" width="19.8%" alt="Email" /></a>

<!-- 01 · 5 CORE RESEARCH DIRECTIONS (INDIVIDUALLY CLICKABLE) -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-research-dark.svg" />
  <img src="./cards/title-research-light.svg" width="100%" alt="01 Research Directions" />
</picture>
<a href="https://github.com/Shashwatology/PhysioFM"><img src="./cards/domain-01.svg" width="33%" alt="01 Multimodal AI & Physiological Computing" /></a><a href="https://github.com/Shashwatology/Guardian-Travel-Twin-"><img src="./cards/domain-02.svg" width="33%" alt="02 Intelligent Infrastructure & Digital Twins" /></a><a href="https://github.com/Shashwatology/semantic-drift-vlm-attacks"><img src="./cards/domain-03.svg" width="33%" alt="03 Trustworthy AI & ML Security" /></a><br><a href="https://github.com/Shashwatology/Semantic-Ctrl-F"><img src="./cards/domain-04.svg" width="49.6%" alt="04 Computer Vision & Document Intelligence" /></a><a href="https://github.com/Shashwatology?tab=repositories"><img src="./cards/domain-05.svg" width="49.6%" alt="05 Quantitative Research & Financial Modelling" /></a>

<!-- 02 · FEATURED RESEARCH PROJECTS (ROW OF 3 CLICKABLE CARDS) -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-projects-dark.svg" />
  <img src="./cards/title-projects-light.svg" width="100%" alt="02 Featured Research Projects" />
</picture>
<a href="https://github.com/Shashwatology/PhysioFM"><img src="./cards/project-physiofm.svg" width="33%" alt="PhysioFM: Foundation Models in rPPG" /></a><a href="https://github.com/Shashwatology/Guardian-Travel-Twin-"><img src="./cards/project-digital-twins.svg" width="33%" alt="Digital Twins in Urban Mobility" /></a><a href="https://github.com/Shashwatology/semantic-drift-vlm-attacks"><img src="./cards/project-vlm-security.svg" width="33%" alt="Semantic Drift in VLMs" /></a>
<p align="right"><sub><a href="https://github.com/Shashwatology?tab=repositories">Explore all {public_repos} public repositories &#8599;</a></sub></p>

<!-- 03 · PUBLICATIONS & SCHOLARLY MILESTONES -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-publications-dark.svg" />
  <img src="./cards/title-publications-light.svg" width="100%" alt="03 Publications and Milestones" />
</picture>

</div>

| Manuscript / Publication Title | Venue / Publisher | Year | Status | Verified Link |
| :-- | :-- | :-: | :-: | :-: |
| **Semantic Drift Before Inference: A Preprocessing Attack Surface in Vision–Language Models**<br><sub>S.A.K. Upadhyay, S.B. Sharma, R.A. Borgalli, R. Vairagade</sub> | *Adaptive Defense and Intelligent Security Architectures for AI-Driven Cybersecurity (IGI Global)*, Ch. 6, pp. 171–202 | 2026 | `Accepted / DOI` | [**DOI: 10.4018/979-8-2600-5116-0.ch006**](https://doi.org/10.4018/979-8-2600-5116-0.ch006) · [Code](https://github.com/Shashwatology/semantic-drift-vlm-attacks) |
| **Fake news detection using deep learning models: A novel approach**<br><sub>Sachin Kumar, Rohan Asthana, Shashwat Upadhyay, N. Upreti, M. Akbar</sub> | *Transactions on Emerging Telecommunications Technologies (Wiley)* | 2020 | `Published` | [**DOI: 10.1002/ett.3767**](https://doi.org/10.1002/ett.3767) |
| **Protocol-Driven Framework for Implementing an Integrated Multimodal Transportation System in Jaipur, India**<br><sub>S.A.K. Upadhyay (mentor: Prof. Nand Kumar)</sub> | *Proceedings of the 18th International Asian Urbanization Conference (IAUC 2026)*, p. 122 | 2026 | `Published` | [**JUMTA Framework**](https://github.com/Shashwatology/JUMTA) |
| **An IoMT-Based Wearable Prototype for Sustainable Remote Patient Monitoring**<br><sub>S.A.K. Upadhyay, A.K. Singh, A.A. Tiwari, R. Borgalli</sub> | *National Conference on Data-Centric AI (DASDA 2025)* | 2025 | `Best Paper` | [**ResearchGate**](https://www.researchgate.net/publication/397178065_An_IoMT-Based_Wearable_Prototype_Sustainable_Remote_Patient_Monitoring) |
| **Technology Intervention for an Efficient Judicial System**<br><sub>Y. Jain, S.A.K. Upadhyay</sub> | *Conference Proceedings (ResearchGate Verified)* | 2025 | `Published` | [**ResearchGate**](https://www.researchgate.net/publication/394205684_Technology_Intervention_for_an_Efficient_Judicial_System) |
| **SentinelAI: Adaptive Behavioral Risk Framework for Real-Time SSH Threat Detection**<br><sub>S.A.K. Upadhyay</sub> | *Cybersecurity Systems Venue* | 2026 | `Under Review` | [**SentinelAI Code**](https://github.com/Shashwatology/SentinelAI) |
| **PhysioFM: A Diagnostic Framework for Transformer-Based Remote Photoplethysmography**<br><sub>S.A.K. Upadhyay, S.B. Sharma, N. Kumar, S. Kumar, Bhoomika</sub> | *Int’l Conf. on Next-Gen Structural Health Monitoring Systems (SHMS-2026)*, Paper ID 123 | 2026 | `Presented` | [**PhysioFM Code**](https://github.com/Shashwatology/PhysioFM) |

<div align="center">

<!-- ACADEMIC & RESEARCH MILESTONES -->
<img src="./cards/research-timeline.svg" width="100%" alt="Academic and Research Milestones" />

<!-- 04 · TECHNOLOGY TOOLKIT -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-stack-dark.svg" />
  <img src="./cards/title-stack-light.svg" width="100%" alt="04 Technology Toolkit" />
</picture>

</div>

| Domain | Core Tools &amp; Frameworks |
| :-- | :-- |
| **Programming &amp; Core** | `Python 3.10+` · `C++ 17/20` · `TypeScript` · `JavaScript` · `SQL` · `Bash` |
| **AI &amp; Machine Learning** | `PyTorch` · `Hugging Face Transformers` · `Swin-V2` · `TimeSformer` · `Scikit-learn` · `TorchVision` |
| **Computer Vision &amp; OCR** | `OpenCV` · `YOLO (v8/v9)` · `CLIP Embeddings` · `Waveform Extraction (rPPG)` · `Spectral Analysis` · `Tesseract OCR` |
| **Cyber &amp; ML Security** | `VLM Preprocessing Auditing (SEV)` · `Isolation Forests (Zero-Label)` · `SSH Threat Modeling` · `CICIDS2017 Benchmark` |
| **Infrastructure &amp; Systems** | `SUMO Traffic Simulation` · `Unity 3D Engine` · `GIS Integration` · `Docker` · `Git &amp; GitHub Actions CI/CD` · `LaTeX` |

<div align="center">

<!-- 05 · GITHUB TELEMETRY & BLUE HEATMAP -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-activity-dark.svg" />
  <img src="./cards/title-activity-light.svg" width="100%" alt="05 GitHub Telemetry and Heatmap" />
</picture>
<img src="./cards/heatmap.svg" width="100%" alt="Shashwat's contribution calendar in electric cobalt blue, refreshed daily with integrated telemetry" /><br><img src="./cards/activity.svg" width="100%" alt="12-month GitHub activity chart, contribution streak metrics, repository metrics, and language distribution" />

<!-- 06 · FEATURED REPOSITORIES -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-repos-dark.svg" />
  <img src="./cards/title-repos-light.svg" width="100%" alt="06 Featured Repositories" />
</picture>

</div>

| Repository | Primary Focus | Language | Architecture / Stack |
| :-- | :-- | :-: | :-- |
| [**PhysioFM**](https://github.com/Shashwatology/PhysioFM) | Non-contact rPPG foundation model &amp; optimization diagnostics | `Python` | Swin-V2 · STDS · UBFC-rPPG · PyTorch |
| [**Guardian-Travel-Twin-**](https://github.com/Shashwatology/Guardian-Travel-Twin-) | 25 km multimodal corridor digital twin &amp; microscopic simulation | `JavaScript` | SUMO · Unity 3D · YOLOv8 · MoHUA IMPACT |
| [**semantic-drift-vlm-attacks**](https://github.com/Shashwatology/semantic-drift-vlm-attacks) | Preprocessing attack surfaces &amp; SEV defense in VLMs | `Python` | IGI Global 2026 Chapter · RGBA-to-RGB Auditing |
| [**SentinelAI**](https://github.com/Shashwatology/SentinelAI) | Zero-label behavioral anomaly detection engine for SSH streams | `Python` | Isolation Forest · CICIDS2017 · Real-Time Engine |
| [**JUMTA**](https://github.com/Shashwatology/JUMTA) | Jaipur integrated multimodal transit &amp; mobility architecture | `TypeScript` | IAUC 2026 · IMPACT Protocol · Public Transit |
| [**Semantic-Ctrl-F**](https://github.com/Shashwatology/Semantic-Ctrl-F) | Visual-semantic document retrieval &amp; contrastive indexing | `Python` | CLIP · Vector Indexing · Cross-Modal Retrieval |

<div align="center">

<!-- 07 · CONNECT & COLLABORATE FOOTER -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-connect-dark.svg" />
  <img src="./cards/title-connect-light.svg" width="100%" alt="07 Connect and Collaborate" />
</picture>

<a href="https://github.com/Shashwatology"><b>GitHub</b></a> &nbsp;·&nbsp; <a href="https://scholar.google.com/citations?user=ulC0-soAAAAJ"><b>Google Scholar</b></a> &nbsp;·&nbsp; <a href="https://www.linkedin.com/in/shashwatupadhyay/"><b>LinkedIn</b></a> &nbsp;·&nbsp; <a href="https://www.researchgate.net/profile/Shashwat-Upadhyay-2"><b>ResearchGate</b></a> &nbsp;·&nbsp; <a href="mailto:shashwatology.s@gmail.com"><b>Email</b></a><br><sub>RESEARCHING INTELLIGENCE. BUILDING SYSTEMS. &copy; 2026 SHASHWAT UPADHYAY.</sub>

</div>
"""

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Generated tight Master Revision V3.3 {README_PATH} ({len(readme_content)} bytes)")


if __name__ == "__main__":
    generate_readme()
