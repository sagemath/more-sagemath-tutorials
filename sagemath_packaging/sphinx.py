sage_doc = "http://doc.sagemath.org/html/en/"

sage_modules = [
    "algebras", "databases", "game_theory", "logic", "monoids", "quadratic_forms",
    "semirings", "arithgroup", "data_structures", "graphs", "manifolds",
    "notebook", "quat_algebras", "stats", "asymptotic",
    "diophantine_approximation", "groups", "matrices", "number_fields",
    "quivers", "structure", "calculus", "discrete_geometry", "hecke", "matroids",
    "numerical", "references", "tensor", "categories", "doctest",
    "history_and_license", "misc", "padics", "repl", "tensor_free_modules",
    "coding", "dynamics", "homology", "modabvar", "parallel",
    "riemannian_geometry", "coercion", "finance", "hyperbolic_geometry",
    "modfrm", "plot3d", "rings", "combinat", "finite_rings", "interfaces",
    "modfrm_hecketriangle", "plotting", "rings_numerical", "constants",
    "function_fields", "knots", "modmisc", "polynomial_rings", "rings_standard",
    "cryptography", "functions", "lfunctions", "modsym", "power_series", "sat",
    "curves", "games", "libs", "modules", "probability", "schemes",
]

import os
import sys
pythonversion = sys.version.split(' ')[0]

def setup(app):
    app.setup_extension('sphinx.ext.todo')
    app.setup_extension('sphinx.ext.mathjax')

    app.setup_extension("sphinx.ext.intersphinx")
    app.config.intersphinx_mapping.update({
        'https://docs.python.org/': None
        })
    app.config.intersphinx_mapping.update({
        sage_doc + doc + "/": None
        for doc in ["prep", "reference", "thematic_tutorials", "tutorial"]
        })
    app.config.intersphinx_mapping.update({
        sage_doc + "reference/" + module: None
        for module in sage_modules
        })

    app.setup_extension("sphinx.ext.extlinks")
    app.config.extlinks.update({
        'python': ('https://docs.python.org/release/'+pythonversion+'/%s', ''),
        # Sage trac ticket shortcuts. For example, :trac:`7549` .
        'trac': ('https://trac.sagemath.org/%s', 'trac ticket #'),
        'wikipedia': ('https://en.wikipedia.org/wiki/%s', 'Wikipedia article '),
        'arxiv': ('http://arxiv.org/abs/%s', 'Arxiv '),
        'oeis': ('https://oeis.org/%s', 'OEIS sequence '),
        'doi': ('https://dx.doi.org/%s', 'doi:'),
        'pari': ('http://pari.math.u-bordeaux.fr/dochtml/help/%s', 'pari:'),
        'mathscinet': ('http://www.ams.org/mathscinet-getitem?mr=%s', 'MathSciNet ')
        })

    app.config.html_theme = 'sage'


# From Sphinx's theme documentation
def themes_path():
    package_dir = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(package_dir, 'themes')
    #return "/opt/more-sagemath-tutorials/themes"
