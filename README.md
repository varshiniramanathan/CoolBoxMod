<p align="center">
  <img src="docs/images/banner.png">
</p>

<hr>

<p align="center">

  <a href="https://mybinder.org/v2/gh/GangCaoLab/CoolBox/master?filepath=tests%2FTestRegion.ipynb">
    <img src="https://mybinder.org/badge_logo.svg" alt="Binder" />
  </a>
  
  <a href="https://anaconda.org/bioconda/coolbox">
    <img src="https://img.shields.io/conda/v/bioconda/coolbox" alt="Install with conda" />
  </a>
  
  
  <a href="https://pypi.python.org/pypi/coolbox/">
    <img src="https://img.shields.io/pypi/v/coolbox.svg" alt="Install with PyPi" />
  </a>
  
  <a href="https://hub.docker.com/r/nanguage/coolbox">
  	<img src="https://img.shields.io/docker/v/nanguage/coolbox?label=docker&logo=docker&sort=semver" alt="Docker version">
  </a>
  
  <a href="https://github.com/GangCaoLab/CoolBox/releases">
  	<img src="https://img.shields.io/github/v/release/gangcaolab/coolbox?include_prereleases&label=github" alt="Github release">
  </a>
 
  <a href="https://gangcaolab.github.io/CoolBox/index.html">
  	<img src="https://readthedocs.org/projects/ansicolortags/badge/?version=latest" alt="Documentation">
  </a>
  
  <a href="https://pypi.python.org/pypi/coolbox">
    <img src="https://img.shields.io/pypi/pyversions/coolbox.svg" alt="Version">
  </a>
  
  <a href="https://pepy.tech/project/coolbox">
    <img src="https://pepy.tech/badge/coolbox" alt="Downloads">
  </a>

  <a href="https://pepy.tech/project/coolbox">
    <img src="https://pepy.tech/badge/coolbox/week" alt="Downloads per week">
  </a>
  
  <a href="https://github.com/GangCaoLab/coolbox/actions/workflows/python-package-conda.yml">
    <img src="https://github.com/GangCaoLab/coolbox/actions/workflows/python-package-conda.yml/badge.svg" alt="Build Status">
  </a>

  <a href="https://www.biorxiv.org/content/10.1101/2021.04.15.439923v1">
    <img src="https://img.shields.io/badge/preprint-biorxiv-red" alt="biorxiv">
  </a>

  <a href="https://link.springer.com/article/10.1186/s12859-021-04408-w">
    <img src="https://img.shields.io/badge/publication-BMC_Bioinformatics-blue" alt="BMC Bioinformatics" />
  </a>

  <a href="https://github.com/GangCaoLab/CoolBox/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/GangCaoLab/coolbox" alt="license">
  </a>

</p>

Flexible, user-friendly genomic data visualization toolkit. Modified to match Hansen Lab plotting aesthetics with some added convenience modifications, which are a mixture of contributions from Varshini Ramanathan, Domenic Narducci, and Miles Huseyin:

1) Auto-scaling of bigwig-type datasets, with optional sub-groups that scale together.
2) Plotting of a different cooler on the top and bottoms diagonals (only implemented for .mcool)
3) Plotting X-axis directly on the bottom of the heatmap with megabase notation
4) More flexible plotting parameter settings ex. colorbar sizing and notation, tick spacing, etc.

See demo/ for a demo notebook that demonstrates the modifications.
For installation, git clone this repo and install packages from the requirements.txt, then install coolbox:

`# create environment; python 3.12 is needed`\
`python3.12 -m venv coolbox-mod`\
`source coolbox-mod/bin/activate`\
`pip install -r requirements.txt`\
`pip install /path/to/coolbox # installs coolbox`

From there, you can access the environment in a Jupyter notebook as follows:

`source coolbox-mod/bin/activate`\
`python -m ipykernel install --user --name==coolbox_kernel`

Then, you will be able to see the `coolbox_kernel` when you open Jupyter notebook.

From below, I left the README unchanged from the original CoolBox (https://github.com/GangCaoLab/CoolBox).

![](docs/images/api_and_cli.png)

## Highlights:

* Multi-omics data interactively visualization.
* User-friendly [API (ggplot2-like Python EDSL)](https://gangcaolab.github.io/CoolBox/quick_start_API.html) and [CLI](https://gangcaolab.github.io/CoolBox/quick_start_CLI.html).
* Show within Jupyter notebook.
* Ease to fetch data and in cooperation with other Python package.
* Ease to implement/add custom track and integrate into CoolBox.

More details please read the [documentation](https://gangcaolab.github.io/CoolBox/index.html).
Interactively online demo: [binder](https://mybinder.org/v2/gh/GangCaoLab/CoolBox/master?filepath=tests%2FTestRegion.ipynb)

## Develop

See [CONTRIBUTING.md](https://github.com/GangCaoLab/CoolBox/blob/master/CONTRIBUTING.md) 

## Citation

```
@article{xu2021coolbox,
  title={CoolBox: A flexible toolkit for visual analysis of genomics data},
  author={Xu, Weize and Zhong, Quan and Lin, Da and Zuo, Ya and Dai, Jinxia and Li, Guoliang and Cao, Gang},
  journal={BMC bioinformatics},
  volume={22},
  number={1},
  pages={1--9},
  year={2021},
  publisher={Springer}
}
```

## Thanks

+ [pyGenomeTracks](https://github.com/deeptools/pyGenomeTracks),
CoolBox's plot system is fork from it.

### Contributors 
This project exists thanks to all the people who contribute. 

<a href="https://github.com/GangCaoLab/CoolBox/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=GangCaoLab/CoolBox" />
</a>

