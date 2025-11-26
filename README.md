# HiP
HiP (Hesperus is Phosphorus) is a tool that produces clusters formed by the threat actor names (presumably) given to the same entity by different CTI vendors. HiP leverages public catalogs (taxonomies) of threat actor names and mappings among them.

## How to use it

HiP uses Python 3.x and Jupyter notebooks (or JupyterLab) to process and normalize threat actor taxonomies and alias mappings. All required data is provided in the repository. It does require installing some dependencies, as listed in `requirements.txt`.

To use it, clone the repository, install required packages and run the Jupyter notebook:

```bash
git clone https://github.com/0xjet/hip.git
cd hip
pip install -r requirements.txt
jupyter notebook hip_pipeline.ipynb
```

## License
HiP is released under the MIT license.

## References
HiP design, analysis, and limitations are documented in the paper:

* G. Roa, M. Suarez, J. Tapiador. [Hesperus is Phosphorus: Mapping Threat Actor Naming Taxonomies at Scale](foo), November 2025.
