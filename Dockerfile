# Dockerfile for binder (needs work)
# References:
# - https://mybinder.readthedocs.io/en/latest/dockerfile.html#preparing-your-dockerfile
# - https://github.com/sagemath/sage-binder-env/blob/master/Dockerfile

# Temporary work around: the first 8.2 image that was pushed to dockerhub was incompatible
FROM sagemath/sagemath@sha256:e933509b105f36b9b7de892af847ade7753e058c5d9e0c0f280f591b85ad996d
# FROM sagemath/sagemath:8.2
RUN sudo apt-get update && sudo apt-get install -y pandoc language-pack-fr build-essential

# Copy the contents of the repo in ${HOME}
COPY --chown=sage:sage . ${HOME}

# Install this package and dependencies and build the notebooks
RUN sage -pip install .
RUN echo "LC_CTYPE=fr_FR.UTF-8 make ipynb" | sage -sh
