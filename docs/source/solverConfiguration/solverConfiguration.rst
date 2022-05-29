Solver Configuration
********************

The current Mesh processor and Solver input configuration parameters for Flow360 are:

.. _Flow360Meshjson:

Flow360Mesh.json
================

.. table::
   :widths: 25 25 50

   +-------------------+-------------------+---------+---------------------------------------------------------------------------------------------------------+
   | Type              | Options           | Default | Description                                                                                             |
   +===================+===================+=========+=========================================================================================================+
   | boundaries        | noSlipWalls       | []      | list of names of boundary patches, e.g. [2,3,7] (for .ugrid), ["blk-1/wall1","blk-2/wall2"] (for .cgns) |
   +-------------------+-------------------+---------+---------------------------------------------------------------------------------------------------------+
   | slidingInterfaces |                   | []      | list of pairs of sliding interfaces                                                                     |
   |                   +-------------------+---------+---------------------------------------------------------------------------------------------------------+
   |                   | stationaryPatches | []      | list of names of stationary boundary patches, e.g. ["stationaryField/interface"]                        |
   |                   +-------------------+---------+---------------------------------------------------------------------------------------------------------+
   |                   | rotatingPatches   | []      | list of names of dynamic boundary patches, e.g. ["rotatingField/interface"]                             |
   |                   +-------------------+---------+---------------------------------------------------------------------------------------------------------+
   |                   | axisOfRotation    | []      | axis of rotation, e.g. [0,0,-1]                                                                         |
   |                   +-------------------+---------+---------------------------------------------------------------------------------------------------------+
   |                   | centerOfRotation  | []      | center of rotation, e.g. [0,0,0]                                                                        |
   +-------------------+-------------------+---------+---------------------------------------------------------------------------------------------------------+

.. warning::

   "slidingInterfaces" can be only used for multi-block meshes.

.. _Flow360json:

Flow360.json
==============

Most input quantities in case configuration file Flow360.json is dimensionless. The convention of non-dimentionalization in Flow360 can be found at :ref:`Non-dimensionalization <nondimensionalization_Flow360>`. Some commonly used variables in the table below:

:math:`L_{gridUnit}` (SI unit = :math:`m`)
  physical length represented by unit length in the given mesh file, e.g. if your grid is in feet, :math:`L_{gridUnit}=1 \text{ feet}=0.3048 \text{ meter}`; if your grid is in millimeter, :math:`L_{gridUnit}=1 \text{ millimeter}=0.001 \text{ meter}`.
:math:`C_\infty` (SI unit = :math:`m/s`)
  speed of sound of freestream
:math:`\rho_\infty` (SI unit = :math:`kg/m^3`)
  density of freestream
:math:`\mu_\infty` (SI unit = :math:`N \cdot s/m^2`)
  dynamic viscosity of freestream
:math:`p_\infty` (SI unit = :math:`N/m^2`)
  static pressure of freestream
:math:`U_\text{ref} \triangleq \text{MachRef}\times C_\infty` (SI unit = :math:`m/s`)
  reference velocity

geometry
--------

.. table:: 
   :widths: 25 25 50

   +--------------+-----------------+---------------------------------------------------------+
   | Options      |     Default     | Description                                             |
   +==============+=================+=========================================================+
   | refArea      |        1        | The reference area of the geometry                      |
   +--------------+-----------------+---------------------------------------------------------+
   | momentCenter | [0.0, 0.0, 0.0] | The x, y, z moment center of the geometry in grid units |
   +--------------+-----------------+---------------------------------------------------------+
   | momentLength | [1.0, 1.0, 1.0] | The x, y, z moment reference lengths                    |
   +--------------+-----------------+---------------------------------------------------------+

freestream
----------

.. csv-table::
   :file: ./freestreamTable.csv
   :widths: 20, 20, 70
   :header-rows: 1
   :delim: @

.. _boundariesParameters:

boundaries
----------

.. table::

   +-------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------+
   | Type                    |        Format                                                              | Description                                                                      |
   +=========================+============================================================================+==================================================================================+
   | SlipWall                | .. code-block:: json                                                       | Slip wall condition.  Also used for symmetry.                                    |
   |                         |                                                                            |                                                                                  |
   |                         |   "boundary_name" :                                                        |                                                                                  |
   |                         |   {                                                                        |                                                                                  |
   |                         |    "type" : "SlipWall"                                                     |                                                                                  |
   |                         |   }                                                                        |                                                                                  |
   +-------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------+
   | NoSlipWall              | .. code-block:: json                                                       | Sets no-slip wall condition. Optionally, a tangential velocity can be prescribed |
   |                         |                                                                            | on the wall using the keyword "Velocity". An example: :ref:`sample <wall_vel>`   |
   |                         |    "boundary_name" :                                                       |                                                                                  |
   |                         |    {                                                                       |                                                                                  |
   |                         |     "type" : "NoSlipWall",                                                 |                                                                                  |  
   |                         |     "Velocity": [                                                          |                                                                                  | 
   |                         |      float or "expression" (default: 0),                                   |                                                                                  |
   |                         |      float or "expression" (default: 0),                                   |                                                                                  |
   |                         |      float or "expression" (default: 0)]                                   |                                                                                  |
   |                         |    }                                                                       |                                                                                  |
   +-------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------+
   | IsothermalWall          | .. code-block:: json                                                       | Isothermal wall boundary condition. "Temperature" is specified in Kelvin.        |
   |                         |                                                                            | Optionally a tangential velocity can be presribed on the wall using the keyword  |
   |                         |    "boundary_name" :                                                       | "Velocity".                                                                      |
   |                         |    {                                                                       |                                                                                  |
   |                         |     "type" : "IsothermalWall",                                             |                                                                                  |
   |                         |     "Temperature":                                                         |                                                                                  |
   |                         |      float or "expression" (REQUIRED),                                     |                                                                                  |  
   |                         |     "Velocity": [                                                          |                                                                                  |
   |                         |      float or "expression" (default: 0),                                   |                                                                                  |
   |                         |      float or "expression" (default: 0),                                   |                                                                                  |
   |                         |      float or "expression" (default: 0)]                                   |                                                                                  |
   |                         |    }                                                                       |                                                                                  |
   +-------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------+
   | Freestream              | .. code-block:: json                                                       | External freestream condition. Optionally, an expression for each of the velocity|
   |                         |                                                                            | components can be specified using the keyword "Velocity".                        |
   |                         |    "boundary_name" :                                                       |                                                                                  |
   |                         |    {                                                                       |                                                                                  |
   |                         |     "type" : "Freestream",                                                 |                                                                                  |
   |                         |     "Velocity": [                                                          |                                                                                  |
   |                         |      float or "expression" (default: freestream),                          |                                                                                  |
   |                         |      float or "expression" (default: freestream),                          |                                                                                  |
   |                         |      float or "expression" (default: freestream)]                          |                                                                                  |
   |                         |    }                                                                       |                                                                                  |
   +-------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------+
   | SubsonicOutflowPressure | .. code-block:: json                                                       | Subsonic outflow, enforced through static pressure ratio.                        |
   |                         |                                                                            |                                                                                  |
   |                         |    "boundary_name" :                                                       |                                                                                  |
   |                         |    {                                                                       |                                                                                  |
   |                         |     "type" : "SubsonicOutflowPressure",                                    |                                                                                  | 
   |                         |     "staticPressureRatio" : float                                          |                                                                                  |
   |                         |    }                                                                       |                                                                                  |
   +-------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------+
   | SubsonicOutflowMach     | .. code-block:: json                                                       | Static pressure outflow boundary condition set via a specified subsonic Mach     |
   |                         |                                                                            | number.                                                                          |
   |                         |    "boundary_name" :                                                       |                                                                                  |
   |                         |    {                                                                       |                                                                                  |
   |                         |     "type" : "SubsonicOutflowMach",                                        |                                                                                  |
   |                         |     "MachNumber" : float                                                   |                                                                                  |
   |                         |    }                                                                       |                                                                                  |
   +-------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------+
   | SubsonicInflow          | .. code-block:: json                                                       | Subsonic inflow (enforced via total pressure ratio and total temperature ratio)  |
   |                         |                                                                            | for nozzle or tunnel plenum.                                                     |
   |                         |    "boundary_name" :                                                       |                                                                                  |
   |                         |    {                                                                       |                                                                                  |
   |                         |     "type" : "SubsonicInflow",                                             |                                                                                  | 
   |                         |     "totalPressureRatio" : float,                                          |                                                                                  |
   |                         |     "totalTemperatureRatio" : float,                                       |                                                                                  |
   |                         |     "rampSteps" : Integer                                                  |                                                                                  |
   |                         |    }                                                                       |                                                                                  |
   +-------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------+
   | MassOutflow             | .. code-block:: json                                                       | Specification of massflow out of the control volume.                             |
   |                         |                                                                            |                                                                                  |
   |                         |    "boundary_name" :                                                       |                                                                                  |
   |                         |    {                                                                       |                                                                                  |
   |                         |     "type" : "MassOutflow",                                                |                                                                                  |
   |                         |     "massFlowRate" : float                                                 |                                                                                  |
   |                         |    }                                                                       |                                                                                  |
   +-------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------+
   | MassInflow              | .. code-block:: json                                                       | Specification of massflow into the control volume.                               |
   |                         |                                                                            |                                                                                  |
   |                         |    "boundary_name" :                                                       |                                                                                  |
   |                         |    {                                                                       |                                                                                  |
   |                         |     "type" : "MassInflow",                                                 |                                                                                  |
   |                         |     "massFlowRate" : float                                                 |                                                                                  |
   |                         |    }                                                                       |                                                                                  |
   +-------------------------+----------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. note::

   Note: "expression" is an expression with "x", "y", "z" as independent variables. An example of NoSlipWall boundary with prescribed velocity is :ref:`NoSlipWall with velocity <wall_vel>`.

.. _volumeOutputInputParameters:

volumeOutput
------------

.. csv-table::
   :file: ./volumeOutputTable.csv
   :widths: 25 10 65
   :header-rows: 1
   :delim: @

.. _surfaceOutputInputParameters:

surfaceOutput
-------------

.. csv-table::
   :file: ./surfaceOutputTable.csv
   :widths: 25 10 65
   :header-rows: 1
   :delim: @

.. _sliceOutputInputParameters:

sliceOutput
-----------

.. csv-table::
   :file: ./sliceOutputTable.csv
   :widths: 25 10 65
   :header-rows: 1
   :delim: @


navierStokesSolver
------------------

.. table::
   :widths: 25 10 65

   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Options                        |  Default | Description                                                                                                                                         |
   +================================+==========+=====================================================================================================================================================+
   | absoluteTolerance              | 1.00E-10 | Tolerance for the NS residual, below which the solver goes to the next physical step                                                                |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | relativeTolerance              | 1.00E-02 | tolerance to the ratio of residual of current pseudoStep to the initial residual, below which the solver goes to the next physical step             |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | CFLMultiplier                  |     1    | factor to the CFL definitions defined in "timeStepping" section                                                                                     |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | linearIterations               |    30    | Number of linear solver iterations                                                                                                                  |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | kappaMUSCL                     |    -1    | Kappa for the MUSCL scheme, range from [-1, 1], with 1 being unstable.                                                                              |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | updateJacobianFrequency        |     4    | Frequency at which the jacobian is updated.                                                                                                         |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | equationEvalFrequency          |     1    | Frequency at which to update the NS equation in loosely-coupled simulations                                                                         |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | maxForceJacUpdatePhysicalSteps |     0    | when which physical steps, the jacobian matrix is updated every pseudo step                                                                         |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | orderOfAccuracy                |     2    | order of accuracy in space                                                                                                                          |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | extraDissipation               |     0    | add more dissipation to the NS solver                                                                                                               |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | limitVelocity                  |   FALSE  | limiter for velocity                                                                                                                                |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | limitPressureDensity           |   FALSE  | limiter for pressure and density                                                                                                                    |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | viscousWaveSpeedScale          |     0    | Scales the wave speed according to a viscous flux. 0.0 is no speed correction, with larger values providing a larger viscous wave speed correction. |
   +--------------------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

.. _turbulenceModelSolverParameters:

turbulenceModelSolver
---------------------

.. table::
   :widths: 25 15 60

   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | Options                        |     Default     | Description                                                                                                                               |
   +================================+=================+===========================================================================================================================================+
   | modelType                      | SpalartAllmaras | Turbulence model type can be: "SpalartAllmaras" or "kOmegaSST"                                                                            |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | absoluteTolerance              |     1.00E-08    | Tolerance for the turbulence model residual, below which the solver goes to the next physical step                                        |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | relativeTolerance              |     1.00E-02    | Tolerance to the ratio of residual of current pseudoStep to the initial residual, below which the solver goes to the next physical step   |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | linearIterations               |        20       | Number of linear iterations for the turbulence moddel linear system                                                                       |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | updateJacobianFrequency        |        4        | Frequency at which to update the Jacobian                                                                                                 |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | equationEvalFrequency          |        4        | Frequency at which to evaluate the turbulence equation in loosely-coupled simulations                                                     |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | kappaMUSCL                     |        -1       | Kappa for the muscle scheme, range from [-1, 1] with 1 being unstable.                                                                    |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | rotationCorrection             |      FALSE      | Rotation correction for the turbulence model. Only support for SpalartAllmaras                                                            |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | quadrativeConstitutiveRelation |      FALSE      | Use quadratic constitutive relation for turbulence shear stress tensor instead of Boussinesq Approximation                                |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | orderOfAccuracy                |        2        | Order of accuracy in space                                                                                                                |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | maxForceJacUpdatePhysicalSteps |        0        | When which physical steps, the jacobian matrix is updated every pseudo step                                                               |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | DDES                           |      FALSE      | "true" enables Delayed Detached Eddy Simulation. Supported for both SpalartAllmaras and kOmegaSST turbulence models,                      |
   |                                |                 | with and without AmplificationFactorTransport transition model enabled                                                                    |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+

.. _transitionModelSolverParameters:

transitionModelSolver
---------------------
The laminar to turbulence transition model supported by Flow360 is the 2019b version of the Amplification Factor Transport Model created by James Coder, University of Tennessee.
This models adds two additional equations to the flow solver in order to solve for the amplification factor and intermittency flow quantities.
More details about the model can be found at: https://turbmodels.larc.nasa.gov/aft_transition_3eqn.html.
Below are a list of configuration parameters for the transition model.
Either Ncrit or turbulenceIntensityPercent can be used to tune the location of transition from laminar to turbulent flow.

.. table::
   :widths: 25 15 60

   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | Options                        |     Default                  | Description                                                                                                                  |
   +================================+==============================+==============================================================================================================================+
   | modelType                      |       None                   | Transition model type can either be: "None" (disabled) or "AmplificationFactorTransport" (enabled)                           |
   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | absoluteTolerance              |     1.00E-07                 | Tolerance for the transition model residual, below which the solver goes to the next physical step                           |
   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | relativeTolerance              |     1.00E-02                 | Tolerance to the ratio of residual of current pseudoStep to the initial residual                                             |
   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | linearIterations               |        20                    | Number of linear iterations for the transition model linear system                                                           |
   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | updateJacobianFrequency        |        4                     | Frequency at which to update the Jacobian                                                                                    |
   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | equationEvalFrequency          |        4                     | Frequency at which to evaluate the turbulence equation in loosely-coupled simulations                                        |
   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | orderOfAccuracy                |        2                     | Order of accuracy in space                                                                                                   |
   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | turbulenceIntensityPercent     |        0.1                   | Used to compute Ncrit parameter for AFT transition model. Range: 0.03 - 2.5. Higher values result in earlier transition      |
   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | Ncrit                          |        8.15                  | Scalar parameter for transition model. Range: 1-11. Higher values delays onset of laminar-turbulent transition.              |
   |                                |                              | Only one of "Ncrit" or turbulenceIntensityPercent" can be specified in this section                                          |
   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | maxForceJacUpdatePhysicalSteps |        0                     | When which physical steps, the jacobian matrix is updated every pseudo step                                                  |
   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+


initialCondition
----------------

.. table::
   :widths: 25 15 60

   +---------+--------------+---------------------------------------------------------------------------------+
   | Options |    Default   | Description                                                                     |
   +=========+==============+=================================================================================+
   | type    | "freestream" | Use the flow conditions defined in freestream section to set initial condition. |
   |         |              | Could be "freestream" or an "expression"                                        |
   +---------+--------------+---------------------------------------------------------------------------------+

.. _table_timeStepping:

timeStepping
------------

.. csv-table::
   :file: ./timeSteppingTable.csv
   :widths: 25 10 65
   :header-rows: 1
   :delim: @


.. note::

   The :code:`timeStepSize` is in solver units (non-dimensional), where time-scale is mesh unit divided by freestream speed of sound. So a time of :code:`timeStepSize=1` means the time it takes for sound to travel 1 mesh unit at freestream.

.. _slidingInterfacesParameters:

slidingInterfaces (list)
------------------------

.. table::
   :widths: 25 10 65

   +-------------------+---------+-----------------------------------------------------------------------------------------------+
   | Options           | Default | Description                                                                                   |
   +===================+=========+===============================================================================================+
   | stationaryPatches |  Empty  | a list of static patch names of an interface                                                  |
   +-------------------+---------+-----------------------------------------------------------------------------------------------+
   | rotatingPatches   |  Empty  | a list of dynamic patch names of an interface                                                 |
   +-------------------+---------+-----------------------------------------------------------------------------------------------+
   | thetaRadians      |  Empty  | expression for rotation angle (in radians) as a function of time                              |
   +-------------------+---------+-----------------------------------------------------------------------------------------------+
   | thetaDegrees      |  Empty  | expression for rotation angle (in degrees) as a function of time                              |
   +-------------------+---------+-----------------------------------------------------------------------------------------------+
   | omegaRadians      |  Empty  | non-dimensional rotating speed, radians/nondim-unit-time, =                                   |
   |                   |         | :math:`\Omega*L_{gridUnit}/C_\infty`, where the SI unit of :math:`\Omega` is rad/s.           |
   +-------------------+---------+-----------------------------------------------------------------------------------------------+
   | omegaDegrees      |  Empty  | non-dimensional rotating speed, degrees/nondim-unit-time, = :math:`\text{omegaRadians}*180/PI`|
   +-------------------+---------+-----------------------------------------------------------------------------------------------+
   | centerOfRotation  |  Empty  | a 3D array, representing the origin of rotation, e.g. [0,0,0]                                 |
   +-------------------+---------+-----------------------------------------------------------------------------------------------+
   | axisOfRotation    |  Empty  | a 3D array, representing the rotation axis, e.g. [0,0,1]                                      |
   +-------------------+---------+-----------------------------------------------------------------------------------------------+
   | volumeName        |  Empty  | a list of dynamic volume zones related to the above {omega, centerOfRotation, axisOfRotation} |
   +-------------------+---------+-----------------------------------------------------------------------------------------------+
   | parentVolumeName  |  Empty  | name of the volume zone that the rotating reference frame is contained in,                    |
   |                   |         | used to compute the acceleration in the nested rotating reference frame                       |
   +-------------------+---------+-----------------------------------------------------------------------------------------------+

.. _actuatorDisksParameters:

actuatorDisks (list)
--------------------

.. table::

   +--------------------------------------+---------+----------------------------------------------------------------------------------------------------+
   |                Options               | Default |                                             Description                                            |
   +======================================+=========+====================================================================================================+
   | center                               |  Empty  | center of the actuator disk                                                                        |
   +--------------------------------------+---------+----------------------------------------------------------------------------------------------------+
   | axisThrust                           |  Empty  | direction of the thrust, it is an unit vector                                                      |
   +--------------------------------------+---------+----------------------------------------------------------------------------------------------------+
   | thickness                            |  Empty  | thickness of the actuator disk                                                                     |
   +--------------------------------------+---------+----------------------------------------------------------------------------------------------------+
   | forcePerArea->radius (list)          |  Empty  | radius of the sampled locations in grid unit                                                       |
   +--------------------------------------+---------+----------------------------------------------------------------------------------------------------+
   | forcePerArea->thrust (list)          |  Empty  | force per area along the axisThrust, positive means the axial force follows the same direction of  |
   |                                      |         | "axisThrust". It is non-dimensional, =                                                             |
   |                                      |         | :math:`\frac{\text{thrustPerArea}(SI=N/m^2)}{\rho_\infty C^2_\infty}`                              |
   +--------------------------------------+---------+----------------------------------------------------------------------------------------------------+
   | forcePerArea->circumferential (list) |  Empty  | force per area in circumferential direction, positive means the circumferential force follows the  |
   |                                      |         | same direction of "axisThrust" based on right hand rule. It is non-dimensional,=                   |
   |                                      |         | :math:`\frac{\text{circumferentialForcePerArea}(SI=N/m^2)}{\rho_\infty C^2_\infty}`                |
   +--------------------------------------+---------+----------------------------------------------------------------------------------------------------+

.. _betDisksInputParameters:

BETDisks (list)
--------------------

A introduction of blade element theory model in Flow360 is available at :ref:`BET solver <bladeElementTheory>`. A case study on XV-15 rotor based on steady blade element disk model is available at :ref:`BET case study <XV15BETDisk_caseStudy>`.

.. csv-table::
   :file: ./betTable.csv
   :widths: 20, 10, 70
   :header-rows: 1
   :delim: @

.. _porousMediaParameters:

porousMedia (list)
--------------------
The porous media model supported by Flow360 is the Darcy-Forchheimer model which has two coefficients: Darcy coefficient for viscous losses and Forchheimer coefficient for inertial losses.
The model acts by adding a sink term to the momentum equations.
More details about the model can be found at https://openfoamwiki.net/index.php/DarcyForchheimer.
Below are a list of configuration parameters for the porous media model.

.. csv-table::
   :file: ./porousTable.csv
   :widths: 30, 15, 70
   :header-rows: 1
   :delim: @

.. _examples_Flow360json:

.. _userDefinedDynamicsParameters:

userDefinedDynamics
--------------------

An example of how to use the userDefinedDynamics is available :ref:`here <userDefinedDynamics>`.

.. csv-table::
   :file: ./userDefinedDynamicsTable.csv
   :widths: 20, 10, 70
   :header-rows: 1
   :delim: @

Examples of Flow360.json
========================

.. _wall_vel:

1. a NoSlipWall boundary with a prescribed velocity

.. literalinclude:: sampleJsons/noSlipWall_velocity.json
   :linenos:

