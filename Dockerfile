# Dockerfile for binder (needs work)
# References:
# - https://mybinder.readthedocs.io/en/latest/dockerfile.html#preparing-your-dockerfile
# - https://github.com/sagemath/sage-binder-env/blob/master/Dockerfile

FROM sagemath/sagemath:9.0-py3
RUN sudo apt-get update && sudo apt-get install -y pandoc language-pack-fr make

# Copy the contents of the repo in ${HOME}
COPY --chown=sage:sage . ${HOME}

# Install this package and dependencies and build the notebooks
RUN sage -pip install .
RUN echo "LC_CTYPE=fr_FR.UTF-8 make ipynb" | sage -sh
# Fake the installation of media (will eventually be done by sphinx)
RUN ln -s ../../media _build/html
