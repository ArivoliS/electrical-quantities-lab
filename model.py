import math


def simulate(v, f, r, l_mh, c_uf, topology="Series"):
    """Ideal sinusoidal steady-state RLC; RMS voltage and signed reactive power."""
    if v < 0 or f <= 0 or r <= 0 or l_mh <= 0 or c_uf <= 0:
        raise ValueError("V >= 0; frequency, R, L and C must be positive")
    w = 2 * math.pi * f
    xl, xc = w * l_mh / 1000, 1 / (w * c_uf / 1e6)
    if topology == "Series":
        z = complex(r, xl - xc)
        current = v / z
    elif topology == "Parallel":
        current = v * (1/r + 1/complex(0, xl) + 1/complex(0, -xc))
    else:
        raise ValueError("Unknown topology")
    power = v * current.conjugate()
    i, p, q = abs(current), power.real, power.imag
    s = v * i
    phi = math.degrees(math.atan2(q, p)) if s else 0.0
    return dict(V=v, I=i, P=p, Q=q, S=s, PF=p/s if s else None,
                phi=phi, nature="Unity" if abs(q) < 1e-8 else "Lagging" if q > 0 else "Leading",
                XL=xl, XC=xc)
