# -*- coding: utf-8 -*-

def check_massey(sequence, connection, L=None):
    """
    Teste si la suite 'sequence' vérifie la relation de récurence
    donnée par les coefficients du polynôme 'connection'.

    INPUT:
    - ``sequence`` -- a list/tuple of values
    - ``connection`` -- a polynom
    - ``L`` -- only those coefficients of ``sequence`` of degree `>L`
      are checked to satisfy the recurrence relation

    EXAMPLES::

        sage: F2 = GF(2)
        sage: P2 = F2['X']
        sage: X = P2.gen()
        sage: check_massey(map(F2, [1,0,1,0]),   1+X^2)
        True
        sage: check_massey(map(F2, [1,0,1,0,0]), 1+X^2)
        False
        sage: check_massey(map(F2, [1,0,1,0,0]), 1+X+X^3)
        True
        sage: check_massey(map(F2, [1,0,1,0,0]), P2.one(), 3)
        True
        sage: check_massey(map(F2, [1,0,1,0,0]), P2.one(), 2)
        False
    """
    if L is None:
        L = connection.degree()
    for n in range(L+1, len(sequence)):
        if sum(connection[i] * sequence[n-i]
               for i in range(connection.degree()+1)):
            return False
    return True

# 
# //  en tant que polynome de P, en
# // utilisant l'algorithme de Berlekamp-Massey
# //////////////////////////////////////////////////////////////////////////////
def massey(sequence, P=QQ['x']):
    """
    Renvoie la plus petite relation de récurence vérifiée par la suite 'sequence'

    INPUT:
    - ``sequence`` -- une liste ou un tuple
    - ``P`` -- un anneau de polynomes univarié sur le même corps que la séquence

    OUTPUT: une paire ``(p, L)``, où `p` est la relation de
    récurrence, représentée comme un élément de ``P``, et `L+1`
    indique à partir de quelle position la relation de récurence est
    valide. Apparemment, `L` n'est pas garanti d'être minimal!

    EXAMPLES::

        sage: P = QQ['x']; x = P.gen()
        sage: massey([1, 1, 1, 1, 1, 1]) == (-x + 1, 1)
        True
        sage: massey([1, 1, 1, 1, 0, 0, 0, 0]) == (P.one(), 4)
        True

     Massey 1969's example, fig 2::

        sage: F2 = GF(2); P2 = F2['x']; x = P2.gen()
        sage: massey(map(F2, [1]), P2) == (1+x, 1)
        True
        sage: massey(map(F2, [1, 0]), P2) == (P2.one(), 1)
        True
        sage: massey(map(F2, [1, 0, 1]), P2) == (1+x^2, 2)
        True
        sage: massey(map(F2, [1, 0, 1, 0]), P2) == (1+x^2, 2)
        True
        sage: massey(map(F2, [1, 0, 1, 0, 0]), P2) == (P2.one(), 3)
        True
    """
    # Invariant: connection gives a recurence relation for sequence[1..n-1] which is
    # valid starting from position L+1 (in particular L >= connection.degree())
    connection = P.one()
    L = 0

    # old_connection is a previous value of connection at step m
    # It connects sequence[1..m-1] but not sequence[1..m],
    # the defect being old_defect.
    old_connection = P.one()
    old_defect = P.base_ring().one()
    X = P.gen()
    Xk = X         # X^(n-m)
    for n in range(len(sequence)):
        # We want to update the connectiono for sequence[1..n].
        # How far is connection from a good recurence relation for sequence[n]?
        defect = sum(connection[i] * sequence[n-i]
                      for i in range(connection.degree()+1))
        if not defect:
            # no need to change connection
            Xk = Xk * X
            continue

        # Update connection appropriately
        temporary  = connection
        connection = connection - (defect / old_defect) * Xk * old_connection

        # We either keep the old connection or choose the new one in
        # order to minimize `L`
        if 2*L > n:
            Xk = Xk * X
        else:
            Xk = X
            L = n+1-L
            old_connection = temporary
            old_defect = defect

    assert check_massey(sequence, connection, L)
    # assert not check_massey(sequence, connection, L-1)
    return (connection, L)


# //////////////////////////////////////////////////////////////////////////////
# // Transforme une matrice en l'endomorphisme correspondant
# //////////////////////////////////////////////////////////////////////////////

# matrix2function :=
# proc(A)
#     option escape;
# begin
#     proc(v)
#     begin
#       A*v;
#     end_proc;
# end_proc:

# //////////////////////////////////////////////////////////////////////////////
# // Calcul du polynôme minimal d'un endomorphisme par l'algo de Wiedemann
# //////////////////////////////////////////////////////////////////////////////

# wiedemann :=
# proc(f, dim)
#     local v, w, sequence, p, L;
# begin
#     v := matrix(dim,1,random(100));
#     w := matrix(1,dim,random(100));
#     sequence := [(w*v)[1,1],
#                (w * (v := f(v)))[1,1] $ i=1..2*dim-1 ];
#     [p, L] := massey(sequence);
#     p::dom::mapsupport(p, d->L-d);
# end_proc:

# // Quelques tests
# prog::test(expr(wiedemann(0, 3)), X):
# prog::test(wiedemann(id, 3),
#            (Dom::UnivariatePolynomial(X, Dom::ExpressionField(), LexOrder))::fromList([[1, 1], [-1, 0]])):
# prog::test(wiedemann(2*id, 3),
#            (Dom::UnivariatePolynomial(X, Dom::ExpressionField(), LexOrder))::fromList([[1, 1], [-2, 0]])):
# M := matrix(10,10,random(10)):
# prog::test(expr(wiedemann(matrix2function(M),linalg::nrows(M))), expr(linalg::minpoly(M,X))):


# rank :=
# proc(f, dim)
#     local g, diagonalPreconditioner, p;
# begin
#     g := random(1000)+1:
#     diagonalPreconditioner := matrix2function(matrix(n, n, g, Diagonal)):
#     // D @ f = diagonalPreconditioner @ f
#     // The non singular part of D @ f is cyclic. Hence the minimal polynomial
#     // of its non-singular part equates its characteristic polynomial.
#     // Conclusion: the rank of f is the rank of D @ f which is the degree of the
#     // non x^* factor of the minimal polynomial of D @ f
#     p := wiedemann(diagonalPreconditioner @ f, dim);
#     // All we have to do is find the degree of the non x^* factor of p
#     degree(p) - 1;
# end_proc:

# //////////////////////////////////////////////////////////////////////////////
# // Utilisation
# //////////////////////////////////////////////////////////////////////////////
# /*
# read("Wiedemann.mu"):
# n := 15:
# // On fabrique une matrice un peu aléatoire dont les
# // valeurs propres sont dans 0..2, avec 2/3 de blocks de Jordan triviaux
# gDiag:=random(3):
# gUp := random(10):
# T := matrix(n, n, (i,j)-> if i=j then gDiag() elif i<=j and j<=n/3 then gUp(); else 0 end):
# // Une matrice de passage aléatoire
# P := matrix(n, n, gUp):
# M := P * T * P^-1:

# phi := matrix2function(M):
# minPoly := wiedemann(phi, n):
# factor(minPoly);
# rank(phi,n);
# linalg::rank(M);

# // Zut, cela ne colle pas avec ce que j'ai compris de l'exposé ...
# diag := matrix(n, n, [ithprime(i) $i=1..n], Diagonal):
# factor(wiedemann(matrix2function(M*diag), n));


# // Calcul de rang par préconditionnement diagonal

# g := random(1000):
# diag1 := matrix(n, n, g, Diagonal):
# diag2 := matrix(n, n, g, Diagonal):
# degree(wiedemann(matrix2function(diag1 * M * diag2 * linalg::transpose(M)*diag1), n))-1;

# wiedemann(matrix2function(M), n)
# */

