.. _release-22.1.3.0:

release-22.1.3.0
================

A new version of Flow360, release-22.1.3.0, has been deployed. Any
new submissions of mesh will use this new version by default. Any
cases based on previously submitted meshes or forked from submitted
cases using prior versions will still use their originally specified
versions of Flow360.
   
Solver
------

*New features*

1. Added support for nested rotating frames: :ref:`nested rotation<slidingInterfacesParameters>`.

2. Improved the accuracy of steady BET Disk solver

*Resolved issues*

1. kOmega and solutionTurbulence when using kOmegaSST model now uses non-dimensionalization consistent with the NavierStokes non-dimensionalization.

2. Same sectional polars at different radial locations are allowed in BET solver.

*Documentation updates*

1. Explained how to set up the parameters in BET Disk: https://docs.simulation.cloud/projects/flow360/en/latest/capabilities/bladeElementTheory.html

2. Added a case study of BET Disk solver about XV-15 hover and airplane mode: https://docs.simulation.cloud/projects/flow360/en/latest/examples/betDiskSteady_caseStudy.html

3. Added a doc for non-dimensionalization conventions in Flow360: https://docs.simulation.cloud/projects/flow360/en/latest/conventions/conventions.html

flow360client
-------------

Although recent versions of flow360client will still work, it is
highly recommended to upgrade to the latest version for more
convenient capabilities:

Usage:

- If downloading for the first time: :code:`pip3 install flow360client`

- If upgrading from an older version: :code:`pip3 install --upgrade flow360client`

Here is the flow360client on PyPI\: https://pypi.org/project/flow360client/

*New features*

1. Added a case configuration json generator

*Resolved issues*

Web UI
------

*New features*
