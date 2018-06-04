# Dockerfile for binder (needs work)

FROM sagemath/sagemath:8.1
RUN sudo apt-get update && sudo apt-get install -y pandoc language-pack-fr

# Inspired from https://mybinder.readthedocs.io/en/latest/dockerfile.html#preparing-your-dockerfile
# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}

RUN sage -pip install .
RUN echo "LC_CTYPE=fr_FR.UTF-8 make ipynb" | sage -sh
