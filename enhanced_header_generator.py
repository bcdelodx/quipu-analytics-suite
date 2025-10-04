#!/usr/bin/env python3
"""
Enhanced Notebook Header Generator for Quipu Analytics Suite

This module generates comprehensive professional headers for analytics notebooks,
integrating detailed learning information seamlessly into existing authorship blocks.

Features:
- Notebook scope and business applications (with counts)
- Models implemented and key visualizations
- Learning outcomes and technical features
- Industry applications and prerequisites
- All integrated into existing professional format

Author: Bryson Charles de los Reyes, PHD
Affiliation: Universidad Católica de Santa María - Advanced Analytics Division
Date: 2025-01-03
Version: v1.3
License: MIT
"""

import json
import uuid
import platform
import sys
from datetime import datetime
from pathlib import Path
from IPython.display import display, Markdown

class EnhancedNotebookHeaderGenerator:
    """
    Enhanced header generator that integrates comprehensive learning information
    into existing professional authorship block structure.
    """
    
    def __init__(self):
        """Initialize the enhanced header generator with registry and metadata."""
        # Set up the registry path relative to this file
        self.base_path = Path(__file__).parent
        self.registry_path = self.base_path / "notebook_registry.json"
        
        # Load the notebook registry
        self.registry = self._load_registry()
        
        # Set up execution metadata
        self.execution_metadata = {
            'execution_timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'platform': platform.platform(),
            'python_version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        }
    
    def _load_registry(self):
        """Load the notebook registry with comprehensive learning information."""
        try:
            if self.registry_path.exists():
                with open(self.registry_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                # Fallback registry if file doesn't exist
                return self._get_fallback_registry()
        except Exception as e:
            print(f"⚠️ Warning: Could not load registry ({e}). Using fallback.")
            return self._get_fallback_registry()
    
    def _get_fallback_registry(self):
        """Provide a fallback registry if the main file is not available."""
        return {
            "repository": {
                "name": "Quipu Analytics Suite",
                "author": "Bryson Charles de los Reyes, PHD",
                "affiliation": "Universidad Católica de Santa María",
                "license": "MIT",
                "version": "v1.3"
            },
            "notebooks": {}
        }
    
    def generate_enhanced_header(self, notebook_key=None, display_immediately=True):
        """
        Generate enhanced header with comprehensive learning information integrated
        into the existing professional authorship block structure.
        """
        try:
            # Get notebook information
            if notebook_key and notebook_key in self.registry.get("notebooks", {}):
                notebook_info = self.registry["notebooks"][notebook_key]
            else:
                # Fallback for unknown notebooks
                notebook_info = {
                    "title": "Analytics Notebook",
                    "version": "v1.3",
                    "date": datetime.now().strftime('%Y-%m-%d'),
                    "format": "simplified"
                }
            
            repo = self.registry["repository"]
            notebook_id = notebook_info.get("notebook_id", str(uuid.uuid4()))
            
            # Generate the enhanced header with integrated learning information
            header = f"""# {notebook_info.get('title', 'Analytics Notebook')}

---

**Author:** {repo['author']}
**Affiliation:** {repo['affiliation']}
**Date:** {notebook_info.get('date', datetime.now().strftime('%Y-%m-%d'))}
**Version:** {notebook_info.get('version', 'v1.3')}
**License:** {repo['license']}
**Notebook ID:** {notebook_id}

---

## Citation
{repo['author']}, "{notebook_info.get('title', 'Analytics Notebook')}," {repo['name']}, {repo['affiliation']}, {notebook_info.get('version', 'v1.3')}, {notebook_info.get('date', datetime.now().strftime('%Y-%m-%d'))}.

Please cite this notebook if used or adapted in publications, presentations, or derivative work.

---

## Contributors / Acknowledgments
- **Primary Author:** {repo['author']} ({repo['affiliation']})
- **Institutional Support:** {repo['affiliation']} - Advanced Analytics Division
- **Technical Framework:** Built on scikit-learn, pandas, numpy, and plotly ecosystems
- **Methodological Foundation:** Statistical learning principles and modern data science best practices
"""
            
            # Integrate comprehensive learning information into Contributors section
            if 'notebook_scope' in notebook_info:
                header += f"\n### 📋 Notebook Scope\n{notebook_info['notebook_scope']}\n"
            
            if 'business_applications' in notebook_info:
                applications = notebook_info['business_applications']
                header += f"\n### 🏢 Business Applications ({len(applications)} total)\n"
                if len(applications) > 5:
                    shown_apps = applications[:5]
                    for app in shown_apps:
                        header += f"- {app}\n"
                    header += f"- *...and {len(applications) - 5} more applications*\n"
                else:
                    for app in applications:
                        header += f"- {app}\n"
            
            if 'models_implemented' in notebook_info:
                models = notebook_info['models_implemented']
                header += f"\n### 🤖 Models Implemented ({len(models)} total)\n"
                if len(models) > 5:
                    shown_models = models[:5]
                    for model in shown_models:
                        header += f"- {model}\n"
                    header += f"- *...and {len(models) - 5} additional models*\n"
                else:
                    for model in models:
                        header += f"- {model}\n"
            
            if 'key_visualizations' in notebook_info:
                visualizations = notebook_info['key_visualizations']
                header += f"\n### 📊 Key Visualizations ({len(visualizations)} total)\n"
                if len(visualizations) > 4:
                    shown_viz = visualizations[:4]
                    for viz in shown_viz:
                        header += f"- {viz}\n"
                    header += f"- *...and {len(visualizations) - 4} additional visualizations*\n"
                else:
                    for viz in visualizations:
                        header += f"- {viz}\n"
            
            if 'learning_outcomes' in notebook_info:
                outcomes = notebook_info['learning_outcomes']
                header += f"\n### 🎓 Learning Outcomes ({len(outcomes)} total)\n"
                if len(outcomes) > 3:
                    shown_outcomes = outcomes[:3]
                    for outcome in shown_outcomes:
                        header += f"- {outcome}\n"
                    header += f"- *...and {len(outcomes) - 3} additional outcomes*\n"
                else:
                    for outcome in outcomes:
                        header += f"- {outcome}\n"
            
            header += """
---

## Version History
| Version | Date | Notes |
|---------|------|-------|
| v1.3 | 2025-10-02 | Enhanced professional formatting, comprehensive documentation, interactive visualizations |
| v1.2 | 2024-09-15 | Updated analysis methods, improved data generation algorithms |
| v1.0 | 2024-06-10 | Initial release with core analytical framework |

---

## Environment Dependencies
- **Python:** 3.8+
- **Core Libraries:** pandas 2.0+, numpy 1.24+, scikit-learn 1.3+
- **Visualization:** plotly 5.0+, matplotlib 3.7+
- **Statistical:** scipy 1.10+, statsmodels 0.14+
- **Development:** jupyter-lab 4.0+, ipywidgets 8.0+

> **Reproducibility Note:** Use requirements.txt or environment.yml for exact dependency matching.

---

## Data Provenance
| Dataset | Source | License | Notes |
|---------|--------|---------|-------|
| Synthetic Data | Generated in-notebook | MIT | Custom algorithms for realistic simulation |
| Statistical Distributions | NumPy/SciPy | BSD-3-Clause | Standard library implementations |
| ML Algorithms | Scikit-learn | BSD-3-Clause | Industry-standard implementations |
| Visualization Schemas | Plotly | MIT | Interactive dashboard frameworks |
"""
            
            # Enhanced Data Provenance with technical features and evaluation methods
            if 'technical_features' in notebook_info:
                features = notebook_info['technical_features']
                if len(features) > 3:
                    examples = ", ".join(features[:3])
                    header += f"| Technical Features | Implementation | {len(features)} | {examples}, ... |\n"
                else:
                    examples = ", ".join(features)
                    header += f"| Technical Features | Implementation | {len(features)} | {examples} |\n"
            
            if 'evaluation_methods' in notebook_info:
                methods = notebook_info['evaluation_methods']
                if len(methods) > 3:
                    examples = ", ".join(methods[:3])
                    header += f"| Evaluation Methods | Statistical/ML Metrics | {len(methods)} | {examples}, ... |\n"
                else:
                    examples = ", ".join(methods)
                    header += f"| Evaluation Methods | Statistical/ML Metrics | {len(methods)} | {examples} |\n"
            
            header += """
---

## Execution Provenance Logs
"""
            header += f"- **Created:** {notebook_info.get('date', datetime.now().strftime('%Y-%m-%d'))}\n"
            header += f"- **Notebook ID:** {notebook_id}\n"
            header += f"- **Execution Environment:** Jupyter Lab / VS Code\n"
            header += f"- **Computational Requirements:** Standard laptop/workstation (2GB+ RAM recommended)\n"
            header += f"- **Current Execution:** {self.execution_metadata['execution_timestamp']}\n"
            header += f"- **Platform:** {self.execution_metadata['platform']}\n"
            header += f"- **Python Version:** {self.execution_metadata['python_version']}\n"
            
            header += """
> **Auto-tracking:** Execution metadata can be programmatically captured for reproducibility.

---

## Disclaimer & Responsible Use
This notebook is provided "as-is" for educational, research, and professional development purposes. Users assume full responsibility for any results, applications, or decisions derived from this analysis.

**Professional Standards:**
- Validate all results against domain expertise and additional data sources
- Respect licensing and attribution requirements for all dependencies
- Follow ethical guidelines for data analysis and algorithmic decision-making
- Credit all methodological sources and derivative frameworks appropriately

**Academic & Commercial Use:**
- Permitted under MIT license with proper attribution
- Suitable for educational curriculum and professional training
- Appropriate for commercial adaptation with citation requirements
- Recommended for reproducible research and transparent analytics
"""
            
            # Add industry applications based on business applications
            if 'business_applications' in notebook_info:
                header += f"\n**Industry Applications:**\n"
                applications = notebook_info['business_applications']
                # Extract industry sectors from applications
                sectors = set()
                for app in applications:
                    if any(term in app.lower() for term in ['financial', 'credit', 'fraud', 'banking']):
                        sectors.add('Financial Services')
                    if any(term in app.lower() for term in ['customer', 'marketing', 'sales', 'retail']):
                        sectors.add('Marketing & Sales')
                    if any(term in app.lower() for term in ['manufacturing', 'quality', 'production']):
                        sectors.add('Manufacturing')
                    if any(term in app.lower() for term in ['healthcare', 'medical', 'clinical']):
                        sectors.add('Healthcare')
                    if any(term in app.lower() for term in ['network', 'security', 'cyber']):
                        sectors.add('Cybersecurity')
                
                if sectors:
                    header += f"- Relevant sectors: {', '.join(sorted(sectors))}\n"
                else:
                    header += f"- Cross-industry applications across multiple business domains\n"
            
            # Add recommended prerequisites based on notebook title
            title_lower = notebook_info.get('title', '').lower()
            if 'tier 1' in title_lower or 'descriptive' in title_lower:
                prerequisites = "Basic statistics, Excel proficiency, curiosity about data"
            elif 'tier 2' in title_lower or 'regression' in title_lower:
                prerequisites = "Tier 1 completion, basic linear algebra, introductory statistics"
            elif 'tier 3' in title_lower or 'time series' in title_lower:
                prerequisites = "Tier 2 completion, time series concepts, intermediate statistics"
            elif 'tier 4' in title_lower or 'unsupervised' in title_lower:
                prerequisites = "Tier 3 completion, linear algebra, unsupervised learning basics"
            elif 'tier 5' in title_lower or 'ensemble' in title_lower:
                prerequisites = "Tier 4 completion, ensemble methods understanding, advanced ML concepts"
            elif 'tier 6' in title_lower or 'advanced' in title_lower:
                prerequisites = "Tier 5 completion, advanced statistics, domain expertise in target application"
            else:
                prerequisites = "Appropriate mathematical background for the analytical complexity level"
            
            header += f"\n**Recommended Prerequisites:**\n- {prerequisites}\n"
            
            header += "\n---\n\n\n"
            
            # Create Markdown object
            header_markdown = Markdown(header)
            
            # Display immediately if requested
            if display_immediately:
                display(header_markdown)
                print("✅ ENHANCED PROFESSIONAL HEADER GENERATED!")
                print(f"📝 Comprehensive learning information integrated into existing format")
                print(f"📄 Notebook: {notebook_key or 'Auto-detected'}")
                if notebook_key in self.registry.get("notebooks", {}):
                    info = self.registry["notebooks"][notebook_key]
                    if 'models_implemented' in info:
                        print(f"🤖 Models: {len(info['models_implemented'])} implemented")
                    if 'business_applications' in info:
                        print(f"🏢 Applications: {len(info['business_applications'])} business cases")
                    if 'learning_outcomes' in info:
                        print(f"🎓 Learning Outcomes: {len(info['learning_outcomes'])} objectives")
            
            return header_markdown
            
        except Exception as e:
            error_msg = f"❌ Error generating enhanced header: {e}"
            print(error_msg)
            return Markdown(f"# Notebook Header\n\n{error_msg}")


# Convenience functions for easy usage
def generate_enhanced_header(notebook_key=None):
    """
    Quick function to generate an enhanced header with comprehensive learning information.
    
    Usage:
        # Auto-detect and generate enhanced header
        generate_enhanced_header()
        
        # Specify specific notebook
        generate_enhanced_header("Tier2_LinearRegression.ipynb")
    """
    generator = EnhancedNotebookHeaderGenerator()
    return generator.generate_enhanced_header(notebook_key)


# For backward compatibility and easy integration
def insert_notebook_header(notebook_key=None):
    """
    Simple one-line function for notebooks - matches the original API.
    
    Usage in notebooks:
        from enhanced_header_generator import insert_notebook_header
        insert_notebook_header()
    """
    return generate_enhanced_header(notebook_key)


if __name__ == "__main__":
    print("🚀 Enhanced Quipu Analytics Suite - Comprehensive Header Generator")
    print("📋 Enhanced with comprehensive learning information integrated seamlessly")
    print("\n📖 Usage:")
    print("   from enhanced_header_generator import insert_notebook_header")
    print("   insert_notebook_header('Tier2_LinearRegression.ipynb')")
    print("\n✅ Features:")
    print("   • Notebook scope and business applications")
    print("   • Models implemented with counts")
    print("   • Key visualizations overview")
    print("   • Learning outcomes and objectives")
    print("   • Technical features and evaluation methods")
    print("   • Industry applications and prerequisites")
    print("   • All integrated into existing professional format!")
    
    # Test with a specific notebook
    print("\n🧪 Testing with Tier2_LinearRegression.ipynb:")
    print("=" * 60)
    generate_enhanced_header("Tier2_LinearRegression.ipynb")