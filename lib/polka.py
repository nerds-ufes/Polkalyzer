from sympy.polys.domains import ZZ
import lib.style as style

# Modified function to support progress bas
def modified_create_list_irrpoly_mod2(n):
    from polka.tools import gf_irreducible_p, increment
    p = 2
    # degree of polynomials
    K = ZZ

    f = []
    total = pow(2, n)
    poly = [K.one] + [K(0) for i in range(0, n)]
    with style.alive_bar(int(total/n), title=f"Generating Irreducible Poly List with CRC{n}") as bar:
        for j in range(total):
            if gf_irreducible_p(poly, p, K):
                f.append(poly)
                bar() # Poly Found
            poly = increment(poly)
    return f

# Modified Calculate Route ID
def modified_calculate_routeid(s, o, debug=False):
    from polka.tools import gf_mul, gf_add, gf_rem, inverse
    # Prevent printing undesired things on std output
    if(debug):
        print("S= ", s)
        print("O= ", o)

    # Calculate Ti
    t = []
    for i in range(len(s)):
        current = s[i]
        elem = [1]
        for j in s:
            factor = ZZ.map(j)
            if factor != current:
                elem = gf_mul(ZZ.map(elem), ZZ.map(factor), 2, ZZ)
        t.append(elem)
    if debug:
        print("T= ", t)

    # Calculate Ni
    n = []
    for i in range(len(s)):
        elem = inverse(t[i], s[i], 2)
        n.append(elem)

    if debug:
        print("N= ", n)

    # Calculate Xi
    xx = []
    for i in range(len(s)):
        elem = gf_mul(ZZ.map(o[i]), ZZ.map(n[i]), 2, ZZ)
        elem = gf_mul(ZZ.map(elem), ZZ.map(t[i]), 2, ZZ)
        xx.append(elem)

    if debug:
        print("XX= ", xx)

    # Calculate X = SUM Xi
    x = []
    for i in range(len(s)):
        x = gf_add(x, xx[i], 2, ZZ)
    if debug:
        print("X: ", x)

    # Calculate M
    m = [1]
    for i in range(len(s)):
        m = gf_mul(ZZ.map(m), ZZ.map(s[i]), 2, ZZ)
    if debug:
        print("M: ", m)

    # Calculate F
    f = gf_rem(ZZ.map(x), ZZ.map(m), 2, ZZ)
    if debug:
        print("F: ", f)

    # Check
    for i in range(len(s)):
        if debug:
            print(
                "Check[", i, "] == ", gf_rem(ZZ.map(f), ZZ.map(s[i]), 2, ZZ) == o[i],
            )

    return f
