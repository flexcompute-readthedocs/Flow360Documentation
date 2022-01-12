.. _manualMeshing:

Overview
========

Mesh generation for CFD is a critical aspect of the analysis process. This documentation aims to provide a high-level description of requirements and best-practices recommended for use in Flow360.

Experienced CFD users are likely familiar with most aspects of this documentation and can continue applying their typical meshing processes. Those less experienced with CFD, or meshing for CFD more specifically, are suggested to use this guide as a starting point. Review of initial simulation results will often provide guidance for mesh improvements.

.. note::
    The majority of guidance provided here is presented in the context of traditional aircraft, but should also be similarly applied to comparable geometry.

Objectives
==========

The purpose of any mesh is to provide a stencil for calculation of the discretized governing equations of the flowfield. Stencil spacings, often referred to as mesh refinement, and structure, often characterized by element types, are important to CFD because they influence the numerical solution. That is, the refinement and type of mesh used dictates what flow physics can be solved and how accurate those flow physics are. Keep in mind that the flow solution is discretized on the mesh, not the underlying geometry.

To that end, when considering a CFD analysis and building mesh(es), the user should carefully consider what flow physics are important to the final analysis objectives. Meshes should be purpose built to adequately capture flow features of interest and those impactful to critical analysis results.

Questions to ask oneself\:

- Where are large gradients (boundary layers, tip vortices, shocks, transition) expected in the flowfield?
- What regions of the model (wing, control surface, wake) are most important to the desired results?
- What are the operating conditions (Mach, altitude, attitude, rotation rates) and are they expected to vary?
- What balance of accuracy (flow physics captured) versus speed (solver wall-time) is desired?

Recommendations
===============

The following are recommended best-practices for generating suitable mesh for CFD. Recommendations are intentionally general to allow for users to develop meshes with their own tools and processes.

See the following section, :ref:`Targets.<Targets>`, for element sizing and quality metrics.

Surface
-------

-   Triangular (tri) and quadrilateral (quad) elements are allowable, all tri is preferable

    -   Elements **must** be first-order

-   Adjacent element size should grow by about 1.2, this is applicable to node spacing along edges and within the interior of surfaces
-   Refinement should be present in regions where large gradients are expected

    -   Leading edges (LE) and trailing edges (TE)
    -   Wing/rotor tips
    -   Concave (wing-fuselage juncture) and convex (chine, struts, landing gear) regions
    -   Where opposing surfaces are in close proximity to one another

-   Elements should be isotropic to the greatest extent possible

    -   Most meshing software attempts to follow this guidance
    -   Geometric features, especially edges, can impose constraints that affect isotropy (see below)

-   Anisotropic elements are appropriate for regions where the general flow direction is known *a priori*

    -   LE and TE/: along edge refine in streamwise direction and coarsen in spanwise direction, increase element size progressively away from edge until isotropic
    -   TE (blunt)/: multiple elements should be present between parallel edges

-   Farfield/:

    -   Encloses entire fluid domain where flow solution occurs
    -   Size to roughly 100x largest dimension of no-slip surfaces, centered around geometry
    -   Edges should have roughly 20 nodes in all directions, target isotropic elements
    -   Depending on the intended boundary condition(s), a sphere (farfield) or box (inlet-outlet) are typically preferred

-   Rotating interfaces/:

    -   On flat, circular surfaces nodes must be positioned on concentric rings
    -   On cylindrical surfaces extruding the outer circular edge/nodes with consistent spacing is preferable, target element size for isotropic elements
    -   Should be roughly 3-5% larger than diameter of rotating geometry and roughly 10% larger than max height (axis of rotation direction) of rotating geometry
    -   Generating rotational interface meshes via scripting is often required, the FlexCompute team can aid in providing code and/or mesh for merging into future models

-   Geometry/:

    -   Some additional considerations relative to the underlying geometry
    -   All surfaces should be defined with wall normals pointing towards surrounding fluid
    -   LE should be defined by edge along entire span
    -   TE should be blunt (two parallel edges) or rounded (single edge, similar to LE)
    -   Avoid small acute angles and edges that join tangentially
    -   Must be watertight (locally), that is no gaps or degenerate surfaces can be present
    -   Remove edges (merge shared surfaces) that are not necessary for controlling mesh size
    -   Simplify geometry where impact to flow and results is minimal, and where generating quality mesh is challenging


Volume
------

Flow360
-------

Targets
=======
