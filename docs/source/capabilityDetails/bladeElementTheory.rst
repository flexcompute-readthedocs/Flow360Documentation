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

In the :ref:`BETDisks <betDisksInputParameters>` section of the Flow360.json, except the :code:`bladeLineChord` and :code:`initialBladeDirection`, other parameters are necessary for both solvers.

.. _betDiskLoadingNote: 

BET Loading Output
-------------------------

After the simulation is completed, a “bet_forces_v2.csv” file is created for the case, which contains the time history of the following quantities:

1. Integrated x-, y-, z-component of non-dimensional forces and non-dimensional moments acted on each disk, represented by "Disk[diskID]_Force_x,_y,_z" and "Disk[diskID]_Moment_x,_y,_z" in the "bet_forces_v2.csv file" respectively. The non-dimensional force is defined as

.. math::
   :label: defBETForce
   
   \text{Force}_\text{non-dimensional} = \frac{\text{Force}_\text{physical}\text{(SI=N/m)}}{\rho_\infty C_\infty^2 L_{gridUnit}^2}

The non-dimensional moment is defined as

.. math::
   :label: defBETMoment

   \text{Moment}_\text{non-dimensional} = \frac{\text{Moment}_\text{physical}\text{(SI=N)}}{\rho_\infty C_\infty^2 L_{gridUnit}^3},
   
where the moment center is the :code:`centerOfRotation` of each disk, defined in :ref:`BETDisks <betDisksInputParameters>` of Flow360.json. 

2. Sectional thrust coefficient :math:`C_t` and sectional torque coefficient :math:`C_q` on each blade at several radial locations, represented by "Disk[diskID]_Blade[bladeID]_R[radialID]" with suffix "_Radius", "_ThrustCoeff" and "_TorqueCoeff". The number of radial locations is specified in :code:`nLoadingNodes`. 
   
The definition of :math:`C_t` is

.. math::
   :label: defBETCt

   C_t\bigl(r\bigr)=\frac{\text{Thrust per unit blade length (SI=N/m)}}{\frac{1}{2}\rho_{\infty}\left((\Omega r)^2\right)\text{chord}_{\text{ref}}}\cdot\frac{r}{R}

The definition of :math:`C_q` is

.. math::
   :label: defBETCq

   C_q\bigl(r\bigr)=\frac{\text{Torque per unit blade length (SI=N)}}{\frac{1}{2}\rho_{\infty}\left((\Omega r)^2\right)\text{chord}_{\text{ref}}R}\cdot\frac{r}{R}

where :math:`r` is the distance between the node to the axis of rotation. :math:`\text{chord}_\text{ref}` is the dimensional refererence chord length. :math:`R` is the radius of the rotor disk. 

.. note::

   All the quantities in the right hand side of :eq:`defBETForce`, :eq:`defBETMoment`, :eq:`defBETCt` and :eq:`defBETCq` are **dimensional**, which are different from the **non-dimensional** values in :ref:`betDisksInputParameters` of Flow360.json.

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

