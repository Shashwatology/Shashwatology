#!/usr/bin/env python3
"""
Generate the complete GitHub Profile README.md for Shashwat Upadhyay.
Theme: "RESEARCH IN MOTION — Intelligence across modalities."
"""

import os
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
README_PATH = os.path.join(ROOT, "README.md")

def generate_readme():
    readme_content = """<!--
  SHASHWAT UPADHYAY — RESEARCH IN MOTION
  Automated GitHub Research Portfolio & Scientific Profile
  Maintained via Python SVG Engine & GitHub Actions Automation
-->

<div align="center">

<!-- ========================================== -->
<!-- 01 · HERO & EDITORIAL IDENTITY             -->
<!-- ========================================== -->
<a href="https://github.com/shashwatology">
  <img src="./cards/hero.svg" width="100%" alt="Shashwat Upadhyay — Research in Motion. Independent AI Researcher, Multimodal Learning, Computer Vision, Digital Twins." />
</a>

<br>

<!-- 16:9 MASTER EDITORIAL VISUAL -->
<a href="https://github.com/shashwatology/PhysioFM">
  <img src="./assets/research-visual.svg" width="100%" alt="Research in Motion: Intelligence Across Modalities — Abstract Scientific Environment & Cross-Modal Systems" />
</a>

<br><br>

<!-- ========================================== -->
<!-- 02 · RESEARCH DIRECTIONS                   -->
<!-- ========================================== -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-research-dark.svg" />
  <img src="./cards/title-research-light.svg" width="100%" alt="Research Directions" />
</picture>

<a href="#-selected-research--projects">
  <img src="./cards/research-map.svg" width="100%" alt="Research Map: Multimodal AI, Digital Twins, ML Security, Document Intelligence" />
</a>

</div>

<br>

### 🔬 Core Scientific Pillars

<table>
  <tr>
    <td width="50%" valign="top">
      <h4>01 · Multimodal AI &amp; Physiological Computing</h4>
      <p>Investigating non-contact physiological signal extraction (heart rate, respiration, BVP) from standard video feeds. Bridging spatial hierarchical vision transformers (Swin-V2) with spatio-temporal difference stems (STDS) to overcome gradient starvation in continuous regression tasks.</p>
      <p><b>Keywords:</b> <code>rPPG</code> · <code>UBFC-rPPG</code> · <code>Swin-V2</code> · <code>Temporal Transformers</code> · <code>RGB+Thermal Fusion</code></p>
      <p>🔗 <b>Primary Repository:</b> <a href="https://github.com/Shashwatology/PhysioFM"><b>Shashwatology/PhysioFM</b></a></p>
    </td>
    <td width="50%" valign="top">
      <h4>02 · Digital Twins &amp; Intelligent Mobility</h4>
      <p>Authoring synchronous digital twin environments coupling microscopic traffic simulation with real-time edge computer vision inference. Integrating synthetic sensor streams for dynamic signal phase optimization and urban congestion mitigation.</p>
      <p><b>Keywords:</b> <code>SUMO Simulation</code> · <code>Unity 3D Engine</code> · <code>YOLO Object Detection</code> · <code>Traffic Telemetry</code></p>
      <p>🔗 <b>Primary Repository:</b> <a href="https://github.com/Shashwatology/Guardian-Travel-Twin-"><b>Shashwatology/Guardian-Travel-Twin-</b></a></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h4>03 · Machine Learning Security &amp; Robustness</h4>
      <p>Auditing silent vulnerability surfaces in machine learning pipelines. Discovered pre-inference semantic drift across Vision-Language Models (VLMs) via alpha-channel transparency exploitation, coupled with zero-label unsupervised anomaly detection platforms.</p>
      <p><b>Keywords:</b> <code>VLM Preprocessing Attacks</code> · <code>Semantic Drift</code> · <code>Isolation Forests</code> · <code>SSH Threat Intelligence</code></p>
      <p>🔗 <b>Primary Repositories:</b> <a href="https://github.com/Shashwatology/semantic-drift-vlm-attacks"><b>semantic-drift-vlm-attacks</b></a> · <a href="https://github.com/Shashwatology/SentinelAI"><b>SentinelAI</b></a></p>
    </td>
    <td width="50%" valign="top">
      <h4>04 · Document Intelligence &amp; Visual Search</h4>
      <p>Decomposing complex visual documents into discrete semantic "visual atoms" vectorized via contrastive vision-language pretraining (CLIP). Enhancing localized image querying and model interpretability with localized explainability frameworks.</p>
      <p><b>Keywords:</b> <code>Visual Atoms</code> · <code>Contrastive Learning</code> · <code>CLIP Search</code> · <code>SLICE / LIME Interpretability</code></p>
      <p>🔗 <b>Primary Repository:</b> <a href="https://github.com/Shashwatology/Semantic-Ctrl-F"><b>Semantic-Ctrl-F</b></a></p>
    </td>
  </tr>
</table>

<br>

<div align="center">

<!-- ========================================== -->
<!-- 03 · SELECTED RESEARCH & PROJECTS          -->
<!-- ========================================== -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-projects-dark.svg" />
  <img src="./cards/title-projects-light.svg" width="100%" alt="Selected Research and Projects" />
</picture>

<a href="https://github.com/Shashwatology/PhysioFM">
  <img src="./cards/project-physiofm.svg" width="100%" alt="PhysioFM — Optimization Diagnostics and Failure Analysis of Hierarchical Foundation Models in rPPG" />
</a>

<a href="https://github.com/Shashwatology/semantic-drift-vlm-attacks">
  <img src="./cards/project-vlm-security.svg" width="100%" alt="Semantic Drift in VLMs — A Preprocessing Attack Surface in Vision-Language Models" />
</a>

<a href="https://github.com/Shashwatology/Guardian-Travel-Twin-">
  <img src="./cards/project-digital-twins.svg" width="100%" alt="Digital Twins in Urban Mobility — Microscopic Traffic Simulation with SUMO and Unity" />
</a>

<a href="https://github.com/Shashwatology/SentinelAI">
  <img src="./cards/project-sentinel-ai.svg" width="100%" alt="SentinelAI — Adaptive SSH Threat Intelligence & Unsupervised Anomaly Platform" />
</a>

<a href="https://github.com/Shashwatology/BreatheSync">
  <img src="./cards/project-breathesync.svg" width="100%" alt="BreatheSync — AI-Powered Respiratory Health Platform & Predictive Digital Twin" />
</a>

</div>

<br>

<!-- ========================================== -->
<!-- 04 · PUBLICATIONS & RESEARCH OUTPUT        -->
<!-- ========================================== -->
<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-publications-dark.svg" />
  <img src="./cards/title-publications-light.svg" width="100%" alt="Publications and Research Output" />
</picture>
</div>

| # | Manuscript / Research Title | Venue / Framework | Year | Status | Verified Link |
| :-: | :-- | :-- | :-: | :-: | :-: |
| **01** | **Fake news detection using deep learning models: A novel approach**<br><sub>Sachin Kumar, Rohan Asthana, Shashwat Upadhyay, N. Upreti, M. Akbar</sub> | *Transactions on Emerging Telecommunications Technologies (Wiley)* | 2020 | `Published` | [**DOI: 10.1002/ett.3967**](https://doi.org/10.1002/ett.3967) |
| **02** | **Semantic Drift Before Inference: A Preprocessing Attack Surface in Vision–Language Models**<br><sub>Shashwat Upadhyay</sub> | *Research Working Paper &amp; Reproducible Testbed* | 2026 | `In Progress` | [**Codebase &amp; Paper**](https://github.com/Shashwatology/semantic-drift-vlm-attacks) |
| **03** | **PhysioFM: Optimization Diagnostics and Failure Analysis of Hierarchical Foundation Models in rPPG**<br><sub>Shashwat Anil Kumar Upadhyay</sub> | *Master Research Dossier &amp; PyTorch Framework* | 2026 | `In Progress` | [**Research Dossier**](https://github.com/Shashwatology/PhysioFM) |

> [!NOTE]  
> All publications, working papers, and associated experimental artifacts are backed by reproducible code repositories and strictly verified data points. No citations or acceptance statuses are simulated.

<br>

<div align="center">

<!-- ========================================== -->
<!-- 05 · ACADEMIC & RESEARCH JOURNEY           -->
<!-- ========================================== -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-journey-dark.svg" />
  <img src="./cards/title-journey-light.svg" width="100%" alt="Academic and Research Journey" />
</picture>

<img src="./cards/research-timeline.svg" width="100%" alt="Academic and Research Milestones Timeline" />

</div>

<br>

<!-- ========================================== -->
<!-- 06 · TECHNOLOGY TOOLKIT                    -->
<!-- ========================================== -->
<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-stack-dark.svg" />
  <img src="./cards/title-stack-light.svg" width="100%" alt="Technology Toolkit" />
</picture>
</div>

<table>
  <tr>
    <td width="33%" valign="top">
      <b>⚡ Core Languages</b><br>
      • Python <code>3.10+</code><br>
      • C++ <code>17/20</code><br>
      • TypeScript / JavaScript<br>
      • SQL &amp; Dataform<br>
      • Java &amp; Bash
    </td>
    <td width="33%" valign="top">
      <b>🧠 Machine Learning &amp; AI</b><br>
      • PyTorch &amp; TorchVision<br>
      • Hugging Face Transformers<br>
      • Swin-V2 &amp; TimeSformer<br>
      • Scikit-learn &amp; NumPy<br>
      • SciPy &amp; Pandas
    </td>
    <td width="33%" valign="top">
      <b>👁️ Computer Vision &amp; rPPG</b><br>
      • OpenCV &amp; ImageIO<br>
      • YOLO (v8 / v9)<br>
      • CLIP &amp; BLIP Foundations<br>
      • Waveform Extraction (BVP)<br>
      • Spectral Analysis (FFT)
    </td>
  </tr>
  <tr>
    <td width="33%" valign="top">
      <b>🚦 Digital Twins &amp; Mobility</b><br>
      • SUMO (Simulation of Urban MObility)<br>
      • Unity 3D Engine<br>
      • TraCI Protocol<br>
      • Microscopic Traffic Telemetry<br>
      • Spatial Sensor Mapping
    </td>
    <td width="33%" valign="top">
      <b>🛡️ Cyber Security &amp; Robustness</b><br>
      • Adversarial VLM Attack Auditing<br>
      • Isolation Forests (Zero-Label)<br>
      • Threat Modeling &amp; OSINT<br>
      • Wireshark &amp; BurpSuite<br>
      • Host Network Log Analysis
    </td>
    <td width="33%" valign="top">
      <b>📐 Scientific Computing &amp; Dev</b><br>
      • LaTeX &amp; Overleaf<br>
      • Docker &amp; Containerization<br>
      • Git &amp; CI/CD GitHub Actions<br>
      • FastAPI &amp; Node.js<br>
      • Linux / WSL2 Environments
    </td>
  </tr>
</table>

<br>

<div align="center">

<!-- ========================================== -->
<!-- 07 · CONTRIBUTION HEATMAP & ACTIVITY       -->
<!-- ========================================== -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-activity-dark.svg" />
  <img src="./cards/title-activity-light.svg" width="100%" alt="GitHub Contribution Calendar and Activity" />
</picture>

<img src="./cards/heatmap.svg" width="100%" alt="Shashwat's contribution calendar in electric cobalt blue, refreshed daily" />
<br>
<img src="./cards/activity.svg" width="100%" alt="Contributions in the last 12 months by month, with streak and peak day telemetry" />

<br><br>

<!-- ========================================== -->
<!-- 08 · FEATURED REPOSITORIES                 -->
<!-- ========================================== -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-repos-dark.svg" />
  <img src="./cards/title-repos-light.svg" width="100%" alt="Featured Repositories" />
</picture>

<a href="https://github.com/Shashwatology/PhysioFM"><img src="./cards/repo-PhysioFM.svg" width="33.333%" alt="PhysioFM" /></a><a href="https://github.com/Shashwatology/SentinelAI"><img src="./cards/repo-SentinelAI.svg" width="33.333%" alt="SentinelAI" /></a><a href="https://github.com/Shashwatology/BreatheSync"><img src="./cards/repo-BreatheSync.svg" width="33.333%" alt="BreatheSync" /></a><br>
<a href="https://github.com/Shashwatology/IITM-Python-Grpa"><img src="./cards/repo-IITM-Python-Grpa.svg" width="33.333%" alt="IITM-Python-Grpa" /></a><a href="https://github.com/Shashwatology/Semantic-Ctrl-F"><img src="./cards/repo-Semantic-Ctrl-F.svg" width="33.333%" alt="Semantic-Ctrl-F" /></a><a href="https://github.com/Shashwatology/semantic-drift-vlm-attacks"><img src="./cards/repo-semantic-drift-vlm-attacks.svg" width="33.333%" alt="semantic-drift-vlm-attacks" /></a>

<br><br>

<!-- ========================================== -->
<!-- 09 · CONNECT & COLLABORATE                 -->
<!-- ========================================== -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./cards/title-connect-dark.svg" />
  <img src="./cards/title-connect-light.svg" width="100%" alt="Connect and Collaborate" />
</picture>

<p align="center">
  <a href="https://github.com/shashwatology"><b>github.com/shashwatology</b></a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/shashwat-upadhyay-13abb020b/"><b>linkedin.com/in/shashwat-upadhyay</b></a> &nbsp;·&nbsp;
  <a href="https://www.researchgate.net/profile/Shashwat-Upadhyay-2"><b>researchgate</b></a> &nbsp;·&nbsp;
  <a href="mailto:shashwatology.s@gmail.com"><b>shashwatology.s@gmail.com</b></a> &nbsp;·&nbsp;
  <a href="https://bento.me/shashwatupadhyay"><b>bento.me</b></a>
</p>

<p align="center">
  <sub>RESEARCHING INTELLIGENCE. BUILDING SYSTEMS. &copy; 2026 SHASHWAT UPADHYAY.</sub>
</p>

</div>
"""

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Generated {README_PATH} ({len(readme_content)} bytes)")

if __name__ == "__main__":
    generate_readme()

