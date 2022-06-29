.. _bladeElementTheory:

Blade Element Theory Model
=============================

Overview
--------

Based on Blade Element Theory, Flow360 provides 2 related solvers, which can be configured in :ref:`BETDisks <betDisksInputParameters>` section of Flow360.json:

- Steady blade disk solver

   To use the steady blade disk solver, the :code:`bladeLineChord` needs to be set as 0, which is its default value if omitted.

- Unsteady blade line solver

   To use the unsteady blade line solver, :code:`bladeLineChord` has to be a positive value and :code:`initialBladeDirection` also needs to be set.

In the :ref:`BETDisks <betDisksInputParameters>` section of the Flow360.json, except the :code:`bladeLineChord` and :code:`initialBladeDirection`, other parameters are necessary for both solvers. A case study on the XV-15 rotor using blade element theory can be found at :ref:`XV15 BET Disk <XV15BETDisk_caseStudy>`.

.. _bet_input:

BET input
-----------

.. note::
   
   #. In the BETDisks section, all input quantities are non-dimensional, except the :code:`twists` and :code:`alphas` (both in degrees). The convention for non-dimensionalization in Flow360 can be found at :ref:`nondimensionalization_Flow360`. 
   #. For users of XROTOR and DFDC, we have a translator script that will convert the XROTOR/DFDC inputs in Flow360 BET inputs.

Some input parameters related to BET solver in Flow360 are explained:

1. **radius**. All grid points enclosed by the cylinder defined by "radius", "center" and "axisOfRotation" will have aerodynamic forces imposed on them according to blade element theory.

2. **rotationDirectionRule**: :code:`leftHand` or :code:`rightHand`. It depends on the design of the rotor blades: whether the blades follow curl left hand rule or the curl right hand rule to generate positive thrust. The following 2 figures show the curl left hand rule and curl right hand rule. The fingers follow the spinning of the blades and the thumb points to the thrust direction. By default, it is :code:`rightHand`.

.. container:: twocol

   .. container:: leftside
      
      .. figure:: ../examples/figures_BET_Tutorial/left_hand_rule.svg
         :width: 80%
         :align: center

   .. container:: rightside
      
      .. figure:: ../examples/figures_BET_Tutorial/right_hand_rule.svg
         :width: 80%
         :align: center

3. **axisOfRotation**: It is the direction of your thumb (thrust) described in "rotationDirectionRule".
4. **omega**: The non-dimensional rotating speed. It should be positive in most cases, which means the leading edge moves in front and the rotation direction of the blades in BET simulations is consistent with the curling fingers described in "rotationDirectionRule" to generate positive thrust. A negative "omega" means the blades rotate in a reverse direction, where the trailing edge moves in front. 

The following 4 pictures give some examples of different rotationDirectionRule and axisOfRotation with **positive omega**. The curved arrow follows the same direction in which rotor spins. The straight arrow points to the direction of thrust.

.. container:: twocol

   .. container:: leftside

      .. code-block:: JSON

         "rotationDirectionRule":"leftHand",
         "axisOfRotation":[0,0,1],
         "omega": 0.3

   .. container:: rightside
      
      .. figure:: ../examples/figures_BET_Tutorial/leftHand_thrust_z+.svg
         :width: 66%
         :align: center

-------------------------------------------------------------

.. container:: twocol

   .. container:: leftside

      .. code-block:: JSON

         "rotationDirectionRule":"leftHand",
         "axisOfRotation":[0,0,-1],
         "omega": 0.5

   .. container:: rightside
      
      .. figure:: ../examples/figures_BET_Tutorial/leftHand_thrust_z-.svg
         :width: 66%
         :align: center

-------------------------------------------------------------

.. container:: twocol

   .. container:: leftside

      .. code-block:: JSON

         "rotationDirectionRule":"rightHand",
         "axisOfRotation":[0,0,1],
         "omega": 0.5

   .. container:: rightside
      
      .. figure:: ../examples/figures_BET_Tutorial/rightHand_thrust_z+.svg
         :width: 66%
         :align: center

-------------------------------------------------------------

.. container:: twocol

   .. container:: leftside

      .. code-block:: JSON

         "rotationDirectionRule":"rightHand",
         "axisOfRotation":[0,0,-1],
         "omega": 0.5

   .. container:: rightside
      
      .. figure:: ../examples/figures_BET_Tutorial/rightHand_thrust_z-.svg
         :width: 66%
         :align: center

-----------------------------------------------------------------

.. note::

   In the above 4 examples, if the omega is negative, the rotor rotates in the opposite direction of what is shown.

5. **chords** and **twists**: The sampled radial distribution of chord length and twist angle. The "twist" affects the local angle of attack. The "chords" affects the amount of lift and drag imposed on the blade (or fluid). For a radial location where chord=0, there is no lift or drag imposed. It should be noted that for any radial location within the given sampling range, the chord or twist is linearly interpolated between its two neighboring sampled data points. For any radial location beyond the given sampling range, the chord or twist is set to be the nearest sampled chord or twist, i.e. constant extrapolation. Here are 3 examples of the given "chords" and the corresponding radial distribution of chord length:

.. rst-class:: left2

   5.1. The root of blade starts at r=20 with chord length=15. The chord shrinks to 10 linearly up to r=60. The chord keeps as 10 for the rest of blade. In this setting, the chord=0 for r in [0,20], there is no aerodynamic lift and drag imposed no matter what the twist angle it has, so this setting fits the rotor without hub.

.. container:: twocol

   .. container:: leftside

      .. literalinclude:: ./BET_chords_1.json
         :language: JSON

   .. container:: rightside
      
      .. figure:: ./chords_distribution_1.svg
         :scale: 49%
         :align: center

.. rst-class:: left2

   5.2. The root of blade starts at r=0 with chord=0. The chord expands to 15 linearly up to r=20, then shrinks to 10 linearly up to r=60. The chord keeps as 10 for the rest of blade. This setting could be used for a mesh with the geometry of hub. Because the chord length changes gradually near the root region, there won't be tip vortices in root region.

.. container:: twocol

   .. container:: leftside

      .. literalinclude:: ./BET_chords_2.json
         :language: JSON

   .. container:: rightside

      .. figure:: ./chords_distribution_2.svg
         :scale: 49%
         :align: center

.. rst-class:: left2
   
   5.3. This is an exmpale of wrong setting of chords, because the chord length at r=0 is not 0, so the local solidity is infinity, which is not realistic.

.. container:: twocol

   .. container:: leftside

      .. literalinclude:: ./BET_chords_3.json
         :language: JSON

   .. container:: rightside

      .. figure:: ./chords_distribution_3.svg
         :scale: 49%
         :align: center

.. note::

   The number of sampling data points in :code:`chords` and :code:`twists` doesn't have to be the same. They are served as sampled data for interpolation of chord length and twist angle respectively and separately. 

.. _betDiskLoadingNote: 

BET Loading Output
-------------------------

After the simulation is completed, a “bet_forces_v2.csv” file is created for the case, which contains the time history of the following quantities:

1. Integrated x-, y-, z-component of non-dimensional forces and non-dimensional moments acted on each disk, represented by "Disk[diskID]_Force_x,_y,_z" and "Disk[diskID]_Moment_x,_y,_z" in the "bet_forces_v2.csv file" respectively. The "xyz" axis is based on the inertial frame of reference. The non-dimensional force is defined as

.. math::
   :label: defBETForce
   
   \text{Force}_\text{non-dimensional} = \frac{\text{Force}_\text{physical}\text{(SI=N)}}{\rho_\infty C_\infty^2 L_{gridUnit}^2}

The non-dimensional moment is defined as

.. math::
   :label: defBETMoment

   \text{Moment}_\text{non-dimensional} = \frac{\text{Moment}_\text{physical}\text{(SI=N$\cdot$m)}}{\rho_\infty C_\infty^2 L_{gridUnit}^3},
   
where the moment center is the :code:`centerOfRotation` of each disk, defined in :ref:`BETDisks <betDisksInputParameters>` of Flow360.json. 

.. note::

   The above Force and Moment values mean the force and moment acted on **solid**. If you want to know the force and moment acted on **fluid**, just add a negative sign in front of it. 

.. attention::

   The x-, y-, z-component of Disk[diskID]_Force and Disk[diskID]_Moment is reported in the global inertial reference frame. This reference frame is defined in the mesh file.

2. Sectional thrust coefficient :math:`C_t` and sectional torque coefficient :math:`C_q` on each blade at several radial locations, represented by "Disk[diskID]_Blade[bladeID]_R[radialID]" with suffix "_Radius" (non-dimensional), "_ThrustCoeff" and "_TorqueCoeff". The number of radial locations is specified in :code:`nLoadingNodes`. 
   
The definition of :math:`C_t` is

.. math::
   :label: defBETCt

   C_t\bigl(r\bigr)=\frac{\text{Thrust per unit blade span (SI=N/m)}}{\frac{1}{2}\rho_{\infty}\left((\Omega r)^2\right)\text{chord}_{\text{ref}}}\cdot\frac{r}{R}

The definition of :math:`C_q` is

.. math::
   :label: defBETCq

   C_q\bigl(r\bigr)=\frac{\text{Torque per unit blade span (SI=N)}}{\frac{1}{2}\rho_{\infty}\left((\Omega r)^2\right)\text{chord}_{\text{ref}}R}\cdot\frac{r}{R}

where :math:`r` is the dimensional distance between the node to the axis of rotation. :math:`\text{chord}_\text{ref}` is the dimensional reference chord length. :math:`R` is the dimensional radius of the rotor disk. 

.. important::

   All the quantities in the right hand side of :eq:`defBETForce`, :eq:`defBETMoment`, :eq:`defBETCt` and :eq:`defBETCq` are **dimensional**, which are different from the **non-dimensional** values in :ref:`betDisksInputParameters` of Flow360.json. For example, at the first disk's first blade's first radial location :math:`r=\text{Disk0_Blade0_R0_Radius}\times L_\text{gridUnit}`. The conventions for non-dimensionalization in Flow360 can be found at :ref:`nondimensionalization_Flow360`.

.. warning::
   For simulations of the steady blade disk solver, the resulting :math:`C_t` and :math:`C_q` are only saved on the first blade, named by "Blade0". They are written as all zeros for other blades, because all the blades have the same sectional loadings in steady blade disk simulations. For the unsteady blade line solver, each blade has its own :math:`C_t` and :math:`C_q` values. 

Here is an example of the header of a "bet_forces_v2.csv" file from a simulation containing two BET disks (assume :code:`nLoadingNodes` = 20, :code:`numberOfBlades` = 3 for each disk)::

    physical_step, pseudo_step, 
    Disk0_Force_x, Disk0_Force_y, Disk0_Force_z, Disk0_Moment_x, Disk0_Moment_y, Disk0_Moment_z, 
    Disk0_Blade0_R0_Radius, Disk0_Blade0_R0_ThrustCoeff, Disk0_Blade0_R0_TorqueCoeff, 
    Disk0_Blade0_R1_Radius, Disk0_Blade0_R1_ThrustCoeff, Disk0_Blade0_R1_TorqueCoeff, 
    ... 
    Disk0_Blade0_R19_Radius, Disk0_Blade0_R19_ThrustCoeff, Disk0_Blade0_R19_TorqueCoeff, 
    Disk0_Blade1_R0_Radius, Disk0_Blade1_R0_ThrustCoeff, Disk0_Blade1_R0_TorqueCoeff, 
    Disk0_Blade1_R1_Radius, Disk0_Blade1_R1_ThrustCoeff, Disk0_Blade1_R1_TorqueCoeff, 
    ... 
    Disk0_Blade1_R19_Radius, Disk0_Blade1_R19_ThrustCoeff, Disk0_Blade1_R19_TorqueCoeff, 
    Disk0_Blade2_R0_Radius, Disk0_Blade2_R0_ThrustCoeff, Disk0_Blade2_R0_TorqueCoeff, 
    Disk0_Blade2_R1_Radius, Disk0_Blade2_R1_ThrustCoeff, Disk0_Blade2_R1_TorqueCoeff, 
    ... 
    Disk0_Blade2_R19_Radius, Disk0_Blade2_R19_ThrustCoeff, Disk0_Blade2_R19_TorqueCoeff, 
    Disk1_Force_x, Disk1_Force_y, Disk1_Force_z, Disk1_Moment_x, Disk1_Moment_y, Disk1_Moment_z,
    ...
    ...
    ...
    Disk1_Blade2_R19_Radius, Disk1_Blade2_R19_ThrustCoeff, Disk1_Blade2_R19_TorqueCoeff

BET Visualization
-------------------

An additional option :code:`betMetrics` in :ref:`volumeOutput <volumeOutputInputParameters>` is available to visualize the BET related quantities.


.. raw:: html

    <div style="position: relative; padding-bottom: 20px; height: 0; overflow: hidden; max-width: 100%; height: auto;">
        <iframe width="560" height="315" src="https://www.youtube.com/embed/sIQk0sguKmI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>

.. note::

   A case study about the XV-15 rotor using steady BET Disk solver can be found at :ref:`XV15 BET Disk case <XV15BETDisk_caseStudy>`.
