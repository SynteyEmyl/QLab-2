# -----------------------------------------------------------------------------
# Copyright (c) 2020, Miguel Angel Avila Torres. All Rights Reserved.
# -----------------------------------------------------------------------------
from typing import Callable

import pandas as pd
from os import walk
from builtins import any as b_ins_any

import model.hydrogen as hy
import model.numerical_methods as methods

_, _, filenames = next(walk('../'))

SAMPLES = 1_000


def inspect_eigenfunction(squared_psi: Callable[[float, float, float], float], filename: str):
    if b_ins_any(filename in x for x in filenames):
        pass
    data: list = []
    idx: int = 0
    offset: float = 1E-13
    r_b: float = hy.a_0

    integral: float = 0
    while integral < 1:
        integral, r, theta, phi, v, *_ = methods.spherical_monte_carlo_integral(squared_psi, r_b=r_b, samples=SAMPLES)
        data.append([int(idx + 1), integral, r_b,
                     methods.spherical_monte_carlo_estimation_error(squared_psi, r, theta, phi, v, SAMPLES)])
        idx += 1
        r_b += offset
        print(f'Iteration: {idx}, Integral: {integral}')

    monte_carlo_approximation = pd.DataFrame(data=data, columns=['attempt',
                                                                 '|\u03A8(r)|^2', 'r_b', 'error estimate'])

    monte_carlo_approximation.to_excel(excel_writer=f'{filename}.xlsx',
                                       sheet_name=f'{filename}',
                                       encoding='utf-8', index=False)


# for f in [hy.squared_h1s, hy.squared_h2s, hy.squared_h2p,
#           hy.squared_h3s, hy.squared_h3p, hy.squared_h3d]:
#     inspect_eigenfunction(f, f'monte-carlo {f.__name__}')

f = hy.squared_h3p
inspect_eigenfunction(f, f'monte-carlo {f.__name__}')
