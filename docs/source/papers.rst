.. _whitePaper:

White Paper
===========

The White Paper for Flow360 can be found `here <https://www.flexcompute.com/assets/static/flow360_whitepaper.pdf>`_.



.. _rotor5Paper:

Rotor5: Rotor analysis under 5 hours using ultra-fast and high-fidelity CFD simulation and automatic meshing
============================================================================================================

| Runda Ji, Feilin Jia, Philippe Spalart and Zongfu Yu
| *Flexcompute Inc, Belmont, Massachusetts, 02138*

| Qiqi Wang
| *Massachusetts Institute of Technology, Cambridge, Massachusetts 02139*
| *Flexcompute Inc, Belmont, Massachusetts, 02138*


We introduce a novel workflow called Rotor5 to simplify and accelerate the traditional high-fidelity
rotor simulations by integrating (1) CAD preparation (2) mesh generation and (3) CFD solver into an
end-to-end process. We quantify the limitations of a popular low-fidelity rotor design tool called Xrotor
and demonstrate the necessity of using a high-fidelity CFD solver such as Rotor5. Using both Xrotor and
Rotor5, we investigate the tiltrotor XV-15 at two different flight conditions: (1) airplane propeller mode
in forward flight and (2) helicopter hovering mode, where the fundamental limitations of low-fidelity
Xrotor could cause a catastrophic design failure. A major cause for this is the tip vortex of the preceding
blade.

`Full Paper <https://simcloud-public-1.s3.amazonaws.com/publications/Rotor5_arXiv.pdf?download=false>`_

`Slides <https://simcloud-public-1.s3.amazonaws.com/publications/Rotor5_VFS_Presentation.pdf?download=false>`_

.. _DESXV15:

Assessment of Detached Eddy Simulation and Sliding Mesh Interface in Predicting Tiltrotor Performance in Helicopter and Airplane Modes
======================================================================================================================================


| Feilin Jia and John Moore
| *Flexcompute Inc, Belmont, Massachusetts, 02138*

| Qiqi Wang
| *Massachusetts Institute of Technology, Cambridge, Massachusetts 02139*

This paper presents numerical investigation on performance and flow field of the full-scale XV-15 tiltrotor in both helicopter mode (hovering flight and forward flight) and aeroplane propeller mode using Detached Eddy Simulation, in which the movement of the rotor is achieved using a Sliding Mesh Interface. Comparison of our CFD results against experiment data and other CFD results is performed and presented.

`Feilin Jia, John Moore and Qiqi Wang, 2022 Assessment of Detached Eddy Simulation and Sliding Mesh Interface in Predicting Tiltrotor Performance in Helicopter and Airplane Modes <https://arxiv.org/pdf/2201.11560.pdf>`_


.. _aeroParametricAdpative:

Aerodynamic Risk Assessment using Parametric, Three-Dimensional Unstructured, High-Fidelity CFD and Adaptive Sampling
=====================================================================================================================


| Runda Ji
| *Flexcompute Inc, Belmont, Massachusetts, 02138*

| Qiqi Wang
| *Massachusetts Institute of Technology, Cambridge, Massachusetts 02139*

We demonstrate an adaptive sampling approach for computing the probability of a rare event for a set of three-dimensional airplane geometries under various flight conditions. We develop a fully automated method to generate parameterized airplanes geometries and create volumetric mesh for viscous CFD solution. With the automatic geometry and meshing, we perform the adaptive sampling procedure to compute the probability of the rare event. We show that the computational cost of our adaptive sampling approach is hundreds of times lower than a brute-force Monte Carlo method.


`Runda Ji and Qiqi Wang, 2021 Aerodynamic Risk Assessment using Parametric, Three-Dimensional Unstructured, High-Fidelity CFD and Adaptive Sampling <https://arxiv.org/pdf/2109.03335.pdf>`_
