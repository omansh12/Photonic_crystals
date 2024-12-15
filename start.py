import numpy as np
import matplotlib.pylab as plt

import tidy3d as td
import tidy3d.web as web

# set up parameters of simulation (length scales are micrometers)
freq0 = td.C_0 / 0.75

square = td.Structure(
    geometry=td.Box(center=(0, 0, 0), size=(1.5, 1.5, 1.5)),
    medium=td.Medium(permittivity=2.0)
)

# create source
source = td.PointDipole(
    center=(-1.5, 0, 0),
    source_time=td.GaussianPulse(freq0=freq0, fwidth=freq0 / 10.0),
    polarization="Ey",
)

# create monitor
monitor = td.FieldMonitor(
    size=(td.inf, td.inf, 0),
    freqs=[freq0],
    name="fields",
    colocate=True,
)

sim = td.Simulation(
    size=(4, 3, 3),
    grid_spec=td.GridSpec.auto(min_steps_per_wvl=25),
    structures=[square],
    sources=[source],
    monitors=[monitor],
    run_time=120/freq0,
)

# visualize in 3D
sim.plot_3d()