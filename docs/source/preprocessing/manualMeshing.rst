.. _manualMeshing:

Overview
--------

Mesh generation for CFD is a critical aspect of the analysis process. This documentation aims to provide a high-level description of requirements and best-practices recommended for use in Flow360.

Experienced CFD users are likely familiar with most aspects of this documentation and can continue applying their typical meshing processes. Those less experienced with CFD, or meshing for CFD more specifically, are suggested to use this guide as a starting point. Review of initial simulation results will often provide guidance for mesh improvements.

.. note::
    The majority of guidance provided here is presented in the context of traditional aircraft, but should be applied similarly to comparable geometry.

Objectives
----------

The purpose of any mesh is to provide a stencil for calculation of the discretized governing equations of the flowfield. Stencil spacings, often referred to as mesh refinement, and structure, often characterized by element types, are important to CFD because they influence the numerical solution. That is, the refinement and type of mesh used dictates what flow physics can be solved and how accurate those flow physics are. Keep in mind that the flow solution is discretized on the mesh, not the underlying geometry.

To that end, when considering a CFD analysis and building mesh(es), the user should carefully consider what flow physics are important to the final analysis objectives. Meshes should be purpose built to adequately capture flow features of interest and those impactful to critical analysis results.

Questions to ask oneself\:
- Where are large gradients (boundary layers, tip vortices, shocks, transition) expected in the flowfield?
- What regions of the model (wing, control surface, wake) are most important to the desired results?
- What are the operating conditions (Mach, altitude, attitude, rotation rates) and are they expected to vary?
- What balance of accuracy (flow physics captured) versus speed (solver wall-time) is desired?

