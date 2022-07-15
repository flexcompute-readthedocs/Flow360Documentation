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
- :ref:`Rotor Disk meshing.<JSON volume mesher rotorDisks>`
- :ref:`Sliding Interfaces.<JSON volume mesher slidingInterfaces>`

Equations
---------

- Steady and unsteady viscous flows.
- :ref:`Coupled stationary and rotating domains. <slidingInterfacesParameters>`
- :ref:`Reynolds-Averaged Navier-Stokes. <turbulenceModelSolverParameters>`
- :ref:`Detached Eddy Simulation. <turbulenceModelSolverParameters>`
- :ref:`Laminar-Turbulent Transition model. <transitionModelSolverParameters>`
- :ref:`Blade Element Theory model <bladeElementTheory>`
- :ref:`Actuator Disk model. <actuatorDisksParameters>`
- :ref:`Porous Media model. <porousMediaParameters>`
- :ref:`User Defined Dynamics. <userDefinedDynamics>`


Turbulence Models
-----------------

- Spalart-Allmaras (SA-neg).
- Spalart-Allmaras with Rotation-Curvature correction (SA-RC).
- Spalart-Allmaras with Quadratic Constitutive Relation (SA-QCR).
- k- |omega| SST. 
- k- |omega| SST with Quadratic Constitutive Relation (SST-QCR).

See :ref:`here <turbulenceModelSolverParameters>` for details.


Boundary Conditions
-------------------

- Freestream (with optional location dependent velocity).
- Slip Wall.
- No-slip Wall (with optional tangential wall velocity).
- Isothermal Wall.
- Wall Model.
- Subsonic Inflow (total pressure, total temperature).
- Subsonic Outflow (back pressure).
- Subsonic Outflow (Mach).
- Mass Flow In.
- Mass Flow Out.
- Periodic.

See :ref:`here <boundariesParameters>` for details.
