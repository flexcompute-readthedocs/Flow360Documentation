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
    -   Size to roughly :math:`\text{100x}` largest dimension of no-slip surfaces, centered around geometry
    -   Edges should have roughly :math:`20` nodes in all directions, target isotropic elements
    -   Depending on the intended boundary condition(s), a sphere (farfield) or box (inlet-outlet) are typically preferred

-   Rotating interfaces:

    -   On flat, circular surfaces nodes **must** be positioned on concentric rings
    -   On cylindrical surfaces extruding the outer circular edge/nodes with consistent spacing is preferable, target element size for isotropic elements
    -   Should be roughly :math:`\text{3-5%}` larger than diameter of rotating geometry and roughly :math:`10%` larger than max height (axis of rotation direction) of rotating geometry
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
    -   A target of :math:`y^+ < 1` and :math:`\text{GR} < 1.2` is typically appropriate

        -   When transition is important, target :math:`\text{GR} < 1.1` and consider a constant layer height for the first :math:`\text{2-4}` layers
        -   Similarly target the above when separation is important/expected
        -   Additional refinement of the underlying surface mesh may also be required to adequately capture the elevated streamwise gradients that can occur in transitional/separated boundary layers
        -   Simple flat-plate solutions from literature are often appropriate for estimating the required first layer height, see `here <https://www.pointwise.com/yplus/index.html>`_ as an example

    -   It is preferable to generate as many layers as possible until achieving isotropic elements, that is the final layer height is roughly equivalent to underlying surface mesh size

-   Refinement region:

    -   Off-body refinement is important for capturing flow features away from the surface (wakes, shocks) that may impact the accuracy of results
    -   The size and extent of refinement regions is dependent upon the flow features being captured as well as the operating conditions to be simulated

        -   Refinement regions should fully enclose the geometry producing off-body flow features, by roughly :math:`10%` geometry scale in all directions
        -   Extend refinement regions downstream at least :math:`\text{2x}` the local characteristic length (chord, diameter)
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
    -   UGRID (AFRL3) big-\  (\ *.b8.ugrid) and little-\  (\ *.lb8.ugrid) endianness are allowable

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

        -   Multiple blocks (domains) should be at the same level, 2\ :sup:`nd`\
        -   Multiple boundaries (no-slip walls) should be at the same level, 3\ :sup:`rd`\ , within their respective blocks
        -   Block interfaces should be split so that one interface is contained within each adjacent block

    -   A Flow360Mesh.json file is preferable to define no-slip boundaries
    -   Boundary names will be strings for CGNS meshes

        -   If multi-block mesh, format will be <block-name>/<boundary-name>
        -   If tri and quad elements are present, the exported format may be tri_<boundary-name> and quad_<boundary-name>, both need to be specified in Flow360Mesh.json file

    -   CGNS meshes are appropriate for multi-block motion

-   See additional information for Flow360Mesh.json inputs :ref:`here<Flow360Meshjson>`


.. _Targets:
Targets
=======

Recommendations for surface/volume mesh sizing and quality metrics are provided here. These are *target* values and should not be considered absolute requirements. Additional consideration is often required when complex flow and geometric features impose restrictions during mesh generation.

Surface
-------

Sizing
^^^^^^

The following spreadsheet provides guidance for specifying element lengths for the surface mesh. Node spacing, and resulting element sizing, typically is handled along edges bounding surface patches. As such, this spreadsheet provides guidance based on common features (LE, TE) found in traditional aircraft that should be defined by bounding edges. Maximum cell sizes are also provided at the component level and are applicable to interior surface element sizing.

.. csv-table::
    :file: ./meshGuidelines.csv
    :header-rows: 1
    :widths: "auto"

Definitions:

-   MAC = mean aerodynamic chord (from primary aerodynamic surface)
-   D = effective diameter (max width for fuselage, disk diameter for rotor)
-   L = total length (nose-tail for fuselage, largest length otherwise)
-   c = local chord length (component chord for flap, tip chord for wing)
-   b = local span length (semi-span for wing, component span for flap)
-   t = thickness (trailing edge for wing, fore-aft distance for rotor disk)


Directions:

1.  Consider the applicable geometry (components and features) of the working model
2.	Add comparable geometry not defined here, this may include scenarios where features vary significantly within a given component or multiple components of similar type exist
3.	Measure reference geometry directly or copy from specification material and calculate node spacings **using the same units present in the working model**
4.	Apply the resulting node spacing in model, noting that the smaller of two value should be utilized where conflicts arise

.. note::
    It is inevitable that components and features of a given model will not directly align with the guidance provided here. It is recommended to size these elements based on the local flow gradients expected and to consider mesh refinement studies, especially if these components/features will have a significant impact on the overall analysis results.

Quality
^^^^^^^

Quality metrics reported vary by meshing software utilized, surface/volume element type, and the intended export type specified by the user. As such, the following quality metrics are general and may need to be modified for review in various meshing software.

-   :math:`\text{Max included angle} < 160^{\circ}` (measure of skewness)

    -   A highly skewed element will likely have a single large interior angle
    -   Problematic elements are typically found between parallel edges with dissimilar node spacing/distributions and between edges that join tangentially
    -   Match node spacing between parallel edges and/or join surfaces at shared edge

-   :math:`\text{Aspect ratio} < 100` (measure of length/width)

    -   A highly anisotropic element will be much larger in one direction versus another
    -   Problematic elements are typically found at LE and TE
    -   Reduce maximum node spacing along edge in relation to spacing perpendicular to edge

-   :math:`\text{Area ratio} < 20` (measure of growth rate)

    -   Disparate element lengths will result in adjacent elements differing greatly in size
    -   Problematic elements are typically found where node spacing unintentionally varies by large amounts between neighboring edges
    -   Modify node spacing along neighboring edges to match at intersections

-   Additional checks:

    -   Intersecting elements = element faces pass through one another
    -   Distance from geometry = nodes are not located on underlying geometry
    -   Missing elements = surface mesh failed to generate or gaps remain (not watertight)

Volume
-------

Sizing
^^^^^^

As noted above, volume elements in the immediate vicinity of geometry expected to create off-body flow features of importance should have their maximum size restricted to :math:`maxSurfaceElementLength \cdot \sqrt{3}`. Outside of these regions of interest it is generally appropriate to generate volume elements with a :math:`\text{GR} = 1.2` and a maximum size equivalent to the farfield boundaries.

Quality
^^^^^^^

Volume mesh quality metrics also vary widely. The following are general metrics to target. However, solution convergence in Flow360 and investigation of mesh refinement in the vicinity of flow features of interest are often the best assessment of mesh quality.

-   :math:`\text{Equivolume skewness} < 0.95` (measure of actual versus optimal volume)

    -   Only applicable to tetrahedral elements
    -   Tetrahedral elements should be nearly optimal unless adjacent elements influence skewness
    -   Problematic elements are typically found where layers stop growing prematurely
    -   Refine surface mesh underlying stopped layers to allow for more isotropic volume elements

-   Additional checks:

    -   Intersecting elements = element faces pass through one another
    -   Negative volume = degenerate elements that fold/twist back on themselves
