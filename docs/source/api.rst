.. _api:
.. currentmodule:: flow360client

*************
API Reference
*************

Installing Flow360 Client
*************************

The Flow360 client can be installed (and updated) from PyPI.  Make sure you have the Python setuptools.  If not, sudo apt-get install python3-setuptools.

.. code-block:: python

    pip3 install flow360client
    pip3 install --upgrade flow360client

Sign in with you Account and Password
*************************************

An account can be created at https://client.flexcompute.com/app/signup.

.. code-block:: python

        python3
        >>> import flow360client
        enter your email registered at flexcompute:********@gmail.com
        Password: ***********
        Do you want to keep logged in on this machine ([Y]es / [N]o)Y

Once you have installed the Flow360 client and signed into it, you can run your first case using the ONERA M6 Wing tutorial in the `Quick Start <quickstart.rst>`_ section of this document.

Configuration Parameters
************************

The current Mesh processor and Solver input configuration parameters for Flow360 are:

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

.. _Flow360json:

Flow360.json
============

Some commonly used symbols in Flow360.json:

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
:math:`U_\text{ref}` (SI unit = :math:`m/s`)
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

runControl
----------

.. table::
   :widths: 25 10 65

   +-----------------------------+---------+--------------------------------------------------------------------------------------+
   | Options                     | Default | Description                                                                          |
   +=============================+=========+======================================================================================+
   | restart                     |  FALSE  | the solutions are initialized from restarting files or not (no need to set by users) |
   +-----------------------------+---------+--------------------------------------------------------------------------------------+
   | startAlphaControlPseudoStep |    -1   | pseudo step at which to start targetCL control. -1 is no trim control. (steady only) |
   +-----------------------------+---------+--------------------------------------------------------------------------------------+
   | targetCL                    |    -1   | The desired trim CL to achieve (assocated with startAlphaControlPseudoStep)          |
   +-----------------------------+---------+--------------------------------------------------------------------------------------+

freestream
----------

.. table::
   :widths: 25 25 50

   +----------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | Options              |              Default              | Description                                                                                                        |
   +======================+===================================+====================================================================================================================+
   |                      |                                   | Non-dimensional Reynolds number based on grid unit, = :math:`\frac{\rho_\infty U_\infty L_{gridUnit}}{\mu_\infty}`.|
   | Reynolds             |   Not required if muRef exists    | For example, for a mesh with phyiscal length 1.5m represented by 1500 grid units (i.e. mesh is in mm),             | 
   |                      |                                   | the :math:`L_{gridUnit}` in the numerator is 0.001m.                                                               |
   +----------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | muRef                | Not required if Reynolds exists   | The refererence dynamic viscosity (non-dimenstional) in our solver,                                                |
   |                      |                                   | = :math:`\frac{\mu_\infty}{\rho_\infty C_\infty L_{gridUnit}}`                                                     |
   +----------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | Mach                 |              REQUIRED             | The Mach number, the ratio of freestream speed to the speed of sound.                                              |
   +----------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | MachRef              |       Required if Mach == 0       | The reference Mach number to compute the mu, CL/CD, coefficients, etc..., = :math:`U_{ref}/C_\infty`.              |
   |                      |                                   | Its default value is "freestream/Mach"                                                                             |
   +----------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | Temperature          |              REQUIRED             | The reference temperature in Kelvin. -1 means globally constant viscosity                                          |
   +----------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | alphaAngle           |              REQUIRED             | The angle of attack in degrees                                                                                     |
   +----------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | betaAngle            |              REQUIRED             | The side slip angle in degrees                                                                                     |
   +----------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | turbulentViscosity   |              1.0                  | The multiplicative factor for the freestream turbulent viscosity for the turbulence model                          |
   +----------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+
   | turbulenceIntensity  |              0.0                  | The turbulence intensity in the freestream in percent. If greater than zero, activates the transition model.       |
   |                      |                                   | A value of 0.5 in this field means turbulenceIntensity=0.5 %.                                                      |
   +----------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------+

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
   |                         |                                                                            | on the wall using the keyword "Velocity".                                        |
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

*Note: "expression" is an expression with "x", "y", "z" as independent variables.*

.. _volumeOutputInputParameters:

volumeOutput
------------

.. table::
   :widths: 25 10 65

   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | Options                     |  Default | Description                                                                          |
   +=============================+==========+======================================================================================+
   | outputFormat                | paraview | "paraview" or "tecplot"                                                              |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | animationFrequency          |    -1    | Frequency at which volume output is saved. -1 is at end of simulation                |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | startAverageIntegrationStep |     0    | Sub-iteration or time-step to start averaging forces/moments                         |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | computeTimeAverages         |   FALSE  | Whether or not to compute time-averaged quantities                                   |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | primitiveVars               |   TRUE   | Outputs rho, u, v, w, p                                                              |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | vorticity                   |   FALSE  | Vorticity                                                                            |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | residualNavierStokes        |   FALSE  | 5 components of the N-S residual                                                     |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | residualTurbulence          |   FALSE  | Residual for the turbulence model                                                    |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | residualTransition          |   FALSE  | Residual for the transition model                                                    |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | solutionTurbulence          |   FALSE  | Solution for the turbulence model                                                    |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | solutionTransition          |   FALSE  | Solution for the transition model                                                    |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | T                           |   FALSE  | Temperature                                                                          |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | s                           |   FALSE  | Entropy                                                                              |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | Cp                          |   TRUE   | Coefficient of pressure.                                                             | 
   |                             |          | :math:`C_p=(\frac{p-p_\infty}{\frac{1}{2}\rho_\infty{U_{ref}}^2})`.                  |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | mut                         |   TRUE   | Turbulent viscosity                                                                  |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | nuHat                       |   TRUE   | nuHat                                                                                |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | kOmega                      |   FALSE  | k and omega when using kOmegaSST model                                               |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | mutRatio                    |   FALSE  | :math:`\mu_t/{\mu_\infty}`                                                           |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | Mach                        |   TRUE   | Mach number                                                                          |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | VelocityRelative            |   FALSE  | velocity in rotating frame                                                           |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | qcriterion                  |   FALSE  | Q criterion                                                                          |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | gradW                       |   FALSE  | Gradient of W                                                                        |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | wallDistance                |   FALSE  | wall distance                                                                        |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | wallDistanceDir             |   FALSE  | wall distance direction                                                              |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+
   | betMetrics                  |   FALSE  | 8 quantities related to BET solvers: velocityX, velocityY and velocityZ in rotating  |
   |                             |          | reference frame, alpha angle, Cf in axial direction, Cf in circumferential direction,|
   |                             |          | tip loss factor, local solidity multiplied by integration weight                     |
   +-----------------------------+----------+--------------------------------------------------------------------------------------+

surfaceOutput
-------------

.. table::
   :widths: 25 10 65

   +-----------------------+----------+--------------------------------------------------------------------------------+
   | Options               |  Default | Description                                                                    |
   +=======================+==========+================================================================================+
   | outputFormat          | paraview | "paraview" or "tecplot"                                                        |
   +-----------------------+----------+--------------------------------------------------------------------------------+
   | animationFrequency    |    -1    | Frequency at which surface output is saved. -1 is at end of simulation         |
   +-----------------------+----------+--------------------------------------------------------------------------------+
   | primitiveVars         |   FALSE  | rho, u, v, w, p                                                                |
   +-----------------------+----------+--------------------------------------------------------------------------------+
   | Cp                    |   FALSE  | Coefficient of pressure                                                        |
   +-----------------------+----------+--------------------------------------------------------------------------------+
   | Cf                    |   FALSE  | Skin friction coefficient                                                      |
   +-----------------------+----------+--------------------------------------------------------------------------------+
   | heatFlux              |   FALSE  | Heat Flux                                                                      |
   +-----------------------+----------+--------------------------------------------------------------------------------+
   | CfVec                 |   FALSE  | Viscous stress coefficient vector. For example,                                | 
   |                       |          | :math:`C_{f_{Vec}}[3]=\frac{\tau_{wall}[3]}{\frac{1}{2}\rho_\infty U_{ref}^2}`.|
   |                       |          | The :math:`\tau_{wall}` is the vector of viscous stress on the wall.           |
   +-----------------------+----------+--------------------------------------------------------------------------------+
   | yPlus                 |   FALSE  | y+                                                                             |
   +-----------------------+----------+--------------------------------------------------------------------------------+
   | wallDistance          |   FALSE  | Wall Distance                                                                  |
   +-----------------------+----------+--------------------------------------------------------------------------------+
   | Mach                  |   FALSE  | Mach number                                                                    |
   +-----------------------+----------+--------------------------------------------------------------------------------+
   | nodeForcesPerUnitArea |   FALSE  | :math:`nodeForcesPerUnitArea=\frac{\tau_{wall}[3]-(p-p_\infty)*normal[3]}      |
   |                       |          | {\rho_\infty C_\infty^2}`, where the :math:`normal[3]` is the unit normal      |
   |                       |          | vector pointing from solid to fluid.                                           |
   +-----------------------+----------+--------------------------------------------------------------------------------+
   | residualSA            |   FALSE  | Spalart-Allmaras residual magnitude                                            |
   +-----------------------+----------+--------------------------------------------------------------------------------+

sliceOutput
-----------

.. table::
   :widths: 25 10 65

   +----------------------+----------+------------------------------------------------------------------------+
   | Options              |  Default | Description                                                            |
   +======================+==========+========================================================================+
   | outputFormat         | paraview | "paraview" or "tecplot"                                                |
   +----------------------+----------+------------------------------------------------------------------------+
   | animationFrequency   |    -1    | Frequency at which slice output is saved. -1 is at end of simulation   |
   +----------------------+----------+------------------------------------------------------------------------+
   | primitiveVars        |   TRUE   | Outputs rho, u, v, w, p                                                |
   +----------------------+----------+------------------------------------------------------------------------+
   | vorticity            |   FALSE  | Vorticity                                                              |
   +----------------------+----------+------------------------------------------------------------------------+
   | T                    |   FALSE  | Temperature                                                            |
   +----------------------+----------+------------------------------------------------------------------------+
   | s                    |   FALSE  | Entropy                                                                |
   +----------------------+----------+------------------------------------------------------------------------+
   | Cp                   |   FALSE  | Coefficient of pressure                                                |
   +----------------------+----------+------------------------------------------------------------------------+
   | mut                  |   FALSE  | Turbulent viscosity                                                    |
   +----------------------+----------+------------------------------------------------------------------------+
   | mutRatio             |   FALSE  | :math:`mut/mu_\infty`                                                  |
   +----------------------+----------+------------------------------------------------------------------------+
   | Mach                 |   TRUE   | Mach number                                                            |
   +----------------------+----------+------------------------------------------------------------------------+
   | gradW                |   FALSE  | gradient of W                                                          |
   +----------------------+----------+------------------------------------------------------------------------+
   | slices               |    []    | List of slices to save after the solver has finished                   |
   +----------------------+----------+------------------------------------------------------------------------+
   |            sliceName |          | string                                                                 |
   +----------------------+----------+------------------------------------------------------------------------+
   |          sliceNormal |          | [x, y, z]                                                              |
   +----------------------+----------+------------------------------------------------------------------------+
   |          sliceOrigin |          | [x, y, z]                                                              |
   +----------------------+----------+------------------------------------------------------------------------+

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
   | orderOfAccuracy                |        2        | Order of accuracy in space                                                                                                                |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | maxForceJacUpdatePhysicalSteps |        0        | When which physical steps, the jacobian matrix is updated every pseudo step                                                               |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | DDES                           |      FALSE      | _true_ enables Delayed Detached Eddy Simulation. Only supported for SpalartAllmaras model                                                 |
   +--------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+

transitionModelSolver
---------------------

.. table::
   :widths: 25 15 60

   +--------------------------------+------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | Options                        |     Default                  | Description                                                                                                                  |
   +================================+==============================+==============================================================================================================================+
   | modelType                      | AmplificationFactorTransport | Transition model type can be: "AmplificationFactorTransport"                                                                 |
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

timeStepping
------------

.. table::
   :widths: 25 10 65

   +------------------+---------+----------------------------------------------------------------------+
   | Options          | Default | Description                                                          |
   +==================+=========+======================================================================+
   | maxPhysicalSteps |    1    | Maximum physical steps                                               |
   +------------------+---------+----------------------------------------------------------------------+
   | timeStepSize     |  "inf"  | Nondimensional time step size in physical step marching,             |
   |                  |         | it is calculated as :math:`\frac{\Delta t_{physical} C_\infty}       |
   |                  |         | {L_{gridUnit}}`. :math:`\Delta t_{physical}` is the physical time    |
   |                  |         | step size. "inf" means steady solver.                                |
   +------------------+---------+----------------------------------------------------------------------+
   | maxPseudoSteps   |   2000  | Maximum pseudo steps within one physical step                        |
   +------------------+---------+----------------------------------------------------------------------+
   | CFL->initial     |    5    | Initial CFL for solving pseudo time step                             |
   +------------------+---------+----------------------------------------------------------------------+
   | CFL->final       |   200   | Final CFL for solving pseudo time step                               |
   +------------------+---------+----------------------------------------------------------------------+
   | CFL->rampSteps   |    40   | Number of steps before reaching the final CFL within 1 physical step |
   +------------------+---------+----------------------------------------------------------------------+
 
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
   | volumeName        |  Empty  | a list of dynamic volume names related to the above {omega, centerOfRotation, axisOfRotation} |
   +-------------------+---------+-----------------------------------------------------------------------------------------------+

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

.. csv-table::
   :file: ./betTable.csv
   :widths: 20, 10, 70
   :header-rows: 1
   :delim: @
