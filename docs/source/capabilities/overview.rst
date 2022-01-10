.. _capabilities:

.. |omega|    unicode:: U+03C9 .. OMEGA SIGN
   :ltrim:

Overview
============

Meshing
-------

- :ref:`Engineering Sketch Pad (ESP) to Surface Mesh.<ESPtoSurfaceMeshSection>`
- :ref:`Surface Mesh to Volume Mesh.<SurfaceToVolumeMeshSection>`
- Automatic labelling, automatic edge and faces refinement.
- :ref:`Refinement sources: box and cylinder.<JSON volume mesher sources>`
- :ref:`Actuator Disk meshing.<JSON volume mesher actuatorDisks>`

Equations
---------

- Steady and unsteady viscous flows.
- Coupled stationary and rotating domains.
- :ref:`Reynolds-Averaged Navier-Stokes. <turbulenceModelSolverParameters>`
- :ref:`Detached Eddy Simulation. <turbulenceModelSolverParameters>`
- :ref:`Laminar-Turbulent Transition model. <transitionModelSolverParameters>`
- :ref:`Blade Element Theory model <bladeElementTheory>`
- :ref:`Actuator Disk model. <actuatorDisksParameters>`
- Porous Media model.


Turbulence Models
-----------------

- Spalart-Allmaras (sa-neg).
- Spalart-Allmaras with Rotation-Curvature correction.
- k- |omega| SST. 

See :ref:`here <turbulenceModelSolverParameters>` for details.


Boundary Conditions
-------------------

- Freestream (with optional location dependent velocity).
- Slip Wall.
- No-slip Wall (with optional tangential wall velocity).
- Isothermal Wall.
- Subsonic Inflow (total pressure, total temperature).
- Subsonic Outflow (back pressure).
- Subsonic Outflow (Mach).
- Mass Flow In.
- Mass Flow Out.

See :ref:`here <boundariesParameters>` for details.
