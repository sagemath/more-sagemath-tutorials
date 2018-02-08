# Dockerfile for binder (needs work)

FROM sagemath/sagemath:8.0-2
RUN sudo apt-get update && sudo apt-get install -y pandoc

# Inspired from https://mybinder.readthedocs.io/en/latest/dockerfile.html#preparing-your-dockerfile
# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}

RUN sage -i rst2ipynb
RUN sage -pip install .
#RUN sage -pip install --upgrade pandocfilters # workaround for https://trac.sagemath.org/ticket/23362
# RUN echo make ipynb | sage -sh

# Needs work: to compile the doc here we currently need python3 and
# there are some incompatibilities with sage's sphinx, ...
