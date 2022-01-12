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

Questions to ask oneself:

-   Where are large gradients (boundary layers, tip vortices, shocks, transition) expected in the flowfield?
-   What regions of the model (wing, control surface, wake) are most important to the desired results?
-   What are the operating conditions (Mach, altitude, attitude, rotation rates) and are they expected to vary?
-   What balance of accuracy (flow physics captured) versus speed (solver wall-time) is desired?

Recommendations
===============

The following are recommended best-practices for generating suitable mesh for CFD. Recommendations are intentionally general to allow for users to develop meshes with their own tools and processes.

See the following section, :ref:`Targets<Targets>`, for element sizing and quality metrics.

Surface
-------

-   Triangular (tri) and quadrilateral (quad) elements are allowable, all tri is preferable

    -   Elements **must** be first-order

-   Adjacent element size should grow by about :math:`1.2`, this is applicable to node spacing along edges and within the interior of surfaces
-   Refinement should be present in regions where large gradients are expected

    -   Leading edges (LE) and trailing edges (TE)
    -   Wing/rotor tips
    -   Concave (wing-fuselage juncture) and convex (chine, struts, landing gear) regions
    -   Where opposing surfaces are in close proximity to one another

-   Elements should be isotropic to the greatest extent possible

    -   Most meshing software attempts to follow this guidance
    -   Geometric features, especially edges, can impose constraints that affect isotropy (see "Geometry" below)

-   Anisotropic elements are appropriate for regions where the general flow direction is known *a priori*

    -   LE and TE: along edge refine in streamwise direction and coarsen in spanwise direction, increase element size progressively away from edge until isotropic
    -   TE (blunt): multiple elements should be present between parallel edges

-   Farfield:

    -   Encloses entire fluid domain where flow solution occurs
    -   Size to roughly :math:`100\text{x}` largest dimension of no-slip surfaces, centered around geometry
    -   Edges should have roughly :math:`20` nodes in all directions, target isotropic elements
    -   Depending on the intended boundary condition(s), a sphere (farfield) or box (inlet-outlet) are typically preferred

-   Rotating interfaces:

    -   On flat, circular surfaces nodes **must** be positioned on concentric rings
    -   On cylindrical surfaces extruding the outer circular edge/nodes with consistent spacing is preferable, target element size for isotropic elements
    -   Should be roughly :math:`3-5%` larger than diameter of rotating geometry and roughly :math:`10%` larger than max height (axis of rotation direction) of rotating geometry
    -   Generating rotational interface meshes via scripting is often required, the FlexCompute team can aid in providing code and/or mesh for merging into future models

-   Geometry:

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

-   Tetrahedral (tet), pyramid (pyr), prism (pri), and hexahedral (hex) elements are allowable

    -   Elements **must** be first-order

-   Domains:

    -   Multiple fluid domains are allowable but should create a continuous flowfield
    -   Interfaces between domains **must** be conformal
        -   Overset mesh is not currently supported in Flow360
        -   If domain motion is intended see "Rotational interfaces" above
    -   Nearfield domains (geometry enclosures) should be generated with max element size consistent with that of the surface mesh, target isotropic volume elements
    -   Farfield domains (flowfield enclosures) should increase mesh size away from geometry at a growth rate (GR) of roughly :math:`1.2` to a maximum consistent with farfield boundary surface mesh

-   Layers:

    -   Growth of anisotropic layers from surface mesh is an important aspect of CFD meshes for flowfields with boundary layers
    -   In general, the first layer height (node distance from surface to first volume element) should be specified to attain the desired :math:`y^+` values and the total number of layers should be sufficient to fully enclose the resulting boundary layer
    -   A target of :math:`y^+ < 1` and :math:`GR < 1.2` is typically appropriate
        -   When transition is important, target :math:`GR < 1.1` and consider a constant layer height for the first :math:`2-4` layers
        -   Similarly target the above when separation is important/expected
        -   Additional refinement of the underlying surface mesh may also be required to adequately capture the elevated streamwise gradients that can occur in transitional/separated boundary layers
        -   Simple flat-plate solutions from literature are often appropriate for estimating the required first layer height, see `here <https://www.pointwise.com/yplus/index.html>`_ as an example
    -   It is preferable to generate as many layers as possible until achieving isotropic elements, that is the final layer height is roughly equivalent to underlying surface mesh size

-   Refinement region:
    -   Off-body refinement is important for capturing flow features away from the surface (wakes, shocks) that may impact the accuracy of results
    -   The size and extent of refinement regions is dependent upon the flow features being captured as well as the operating conditions to be simulated
        -   Refinement regions should fully enclose the geometry producing off-body flow features, by roughly :math:`10%` geometry scale in all directions
        -   Extend refinement regions downstream at least :math:`2\text{x}` the local characteristic length (chord, diameter)
        -   Choose a shape that is representative of the flow features of interest (cylinder/rotor, box/wing, cone/shock)
        -   Ensure refinement region encloses flow features at different flow angles (:math:`\alpha`, :math:`\beta`) and speeds (:math:`M`, :math:`\Omega`)
    -   Refinement regions should restrict the maximum element size allowable within
        -   Reference the max surface element length
        -   Apply :math:`maxSurfaceElementLength \cdot \sqrt{3}` sizing for refinement regions near surfaces
        -   Larger refinement regions can be extended further downstream, while still enclosing smaller regions, with incrementally larger sizing applied

Flow360
-------

-   Boundary conditions (BCs) should be specified as the mesh is generated
    -   Different components of the model (fuselage, wing) should be separated logically to allow for analysis of respective influences on the overall results
    -   All surface mesh and rotating interfaces should be defined as no-slip wall BCs
    -   Farfield, inlets, and outlets can be defined as their respective BC types
    -   BCs can be modified when a case is submitted, but it is preferable to generate a mesh with appropriate BCs initially specified

-   Flow360 accepts CGNS or UGRID mesh formats, typically exported from meshing software
    -   CGNS single- and multi-block (multiple fluid domains) are allowable
    -   UGRID (AFRL3) big- (*.b8.ugrid) and little- (*.lb8.ugrid) endianness are allowable
        -   Endianness **must** be specified during upload to Flow360 if not defined via mesh filename
    -   *.gz or *.bz2 compressions are allowable
    -   Mesh filename cannot have spaces

-   UGRID considerations:
    -   UGRID exports with an associated *.mapbc file may be used for no-slip wall boundary definition
        -   See flow360client.noSlipWallsFromMapbc() in :ref:`Python API Reference<api>`
    -   Alternatively, a Flow360Mesh.json file can define no-slip boundaries
    -   Boundary names will be integers for UGRID meshes
    -   UGRID meshes are not appropriate for scenarios with multi-block motion

-   CGNS considerations:
    -   CGNS mesh should be export as an HDF5 file type
    -   Boundaries **must** be exported as “Elements_t” type, which contains connectivity information necessary in Flow360
    -   The CGNS tree structure should be of the form base > block > boundary
        -   Multiple blocks (domains) should be at the same level, 2:sup:`nd`
        -   Multiple boundaries (no-slip walls) should be at the same level, 3:sup:`rd`, within their respective blocks
        -   Block interfaces should be split so that one interface is contained within each adjacent block
    -   A Flow360Mesh.json file is preferable to define no-slip boundaries
    -   Boundary names will be strings for CGNS meshes
        -   If multi-block mesh, format must be <block-name>/<boundary-name>
        -   If tri and quad elements are present, exported format may be tri_<boundary-name> and quad_<boundary-name>, both must be specified in Flow360Mesh.json file
    -   CGNS meshes are appropriate for multi-block motion

-   See additional information for Flow360Mesh.json inputs :ref:`here<Flow360Meshjson>`


.. _Targets:
Targets
=======
