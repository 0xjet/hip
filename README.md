# HiP
HiP (Hesperus is Phosphorus) is a tool that produces clusters formed by the threat actor names given to the same entity by different CTI vendors. HiP leverages public catalogs (taxonomies) of threat actor names and mappings among them. 

## How to use it

HiP uses Python 3.x and Jupyter notebooks (or JupyterLab) to process and normalize threat actor taxonomies and alias mappings. All required data is provided in the repository. It does require installing some dependencies, as listed in `requirements.txt`.

To use it, clone the repository (make sure git LFS is installed and configured on your system), install the required packages, and run the Jupyter notebook:

```bash
git clone https://github.com/0xjet/hip.git
cd hip
pip install -r requirements.txt
jupyter notebook hip_pipeline.ipynb
```

The analysis pipeline produces a single JSON file (`nameclusters.json`) with all TA name clusters. The HiP API feeds from this file to perform basic queries and return clusters of aliases. 

## A note of caution

HiP is built on a knowledge base extracted from public sources, some of which are incomplete and may contain errors. Given the open-source nature of the tool, these limitations can be collectively identified and corrected, allowing the knowledge base to be collaboratively refined and updated with new vendor taxonomies and mappings.

We believe that HiP can serve as a valuable tool for numerous applications, but it must be used with caution. The resulting alias clusters  capture the outcome of integrating various mappings, but do not account for the presence of incorrect or questionable alias relationships within those mappings. Therefore, analysts must post-process these outputs according to their specific requirements. The HiP paper (see below) dcouments some of the issues found in the data sources.

## License
HiP is released under the MIT license.

## References
HiP design, analysis, and limitations are documented in the paper:

* G. Roa, M. Suarez-Roman, J. Tapiador. [Hesperus is Phosphorus: Mapping Threat Actor Naming Taxonomies at Scale]([foo](https://arxiv.org/abs/2512.00857)), November 2025.
