Conventions
********************

.. _nondimensionalization_Flow360:

Non-dimensionalization in Flow360
===================================

In Flow360, most input and output variables are non-dimensional. The non-dimensionalization reduces the number of free parameters and helps to provide better understanding of the underlying physics. A non-dimensional variable is obtained by dividing its dimensional counterpart by an appropriately selected constant like :eq:`def_nondim`

.. math::
   :label: def_nondim

   \text{non-dimensional variable} = \frac{\text{dimensional variable}}{\text{reference value}}

Theoretically, the reference values for non-dimensionalization can be arbitrary as long as the resulting equations are identical to the original ones, but in practice, the reference values are usually selected based on some typical parameters of problems and flow characteristics to avoid confusion. The following list shows some commonly used non-dimensional variables in both input configuration files and output files:

.. _tab_nondimensionalization_flow360:
.. csv-table:: Reference values for non-dimensionalization in Flow360
   :file: ./nondimensionalization_flow360.csv
   :widths: 10,10,60
   :header-rows: 1
   :delim: @

.. note::
   The definition on :math:`L_\text{gridUnit}` can be found in :ref:`case configuration <Flow360json>`.

Besides the above non-dimensional quantities, there are also many **coefficients** commonly used in the community of computational fluid dynamics, e.g. pressure coefficient (:math:`C_p`), skin friction coefficient (:math:`C_f`), lift coefficient (:math:`C_L`), drag coefficient (:math:`C_D`), etc. Flow360 also exports the above coefficients found in :ref:`volumeOutput <volumeOutputInputParameters>`, :ref:`surfaceOutput <surfaceOutputInputParameters>`, :ref:`sliceOutput <sliceOutputInputParameters>` as well as the "Forces" tab of web interface. 

.. caution::

   It should be noted that the reference velocity :math:`U_\text{ref}` used to calculate the :math:`C_p, C_f, C_D, C_L` can be set via "freestream/Mach" or "freestream/MachRef" by users. Its definition can be found in :ref:`case configuration <Flow360json>`. It is not the same as the reference velocity (:math:`C_\infty`) for non-dimensionalization in :numref:`tab_nondimensionalization_flow360`.

It should also be noted that the "freestream/Reynolds" is based on the given reference velocity :math:`U_\text{ref}` and :math:`L_\text{gridUnit}`.

.. _ForceMomentCoeff_Flow360:

Force Coefficients and Moment Coefficients
===========================================

The force coefficients and moment coefficients exported by Flow360 are listed in :numref:`tab_forceMomentCoefficients_flow360`. These coefficients are shown in "Forces" tab of each case in Flow360 web portal. These coefficients can also be fetched by :code:`flow360client.case.GetCaseTotalForces(caseId)`. 

.. _tab_forceMomentCoefficients_flow360:
.. csv-table:: Force coefficients and Moment coefficents exported by Flow360
   :file: ./forceMomentCoefficients.csv
   :widths: 10,50
   :header-rows: 1
   :delim: @

.. note::
   
   In the above table, all quantities in "Definition" column are dimensional. :math:`U_\text{ref}` is calculated by :math:`\text{"freestream/MachRef"}\times C_\infty`. The :math:`A_\text{ref}` is equal to :math:`\text{"geometry/refArea"}\times L_\text{gridUnit}^2`. The array :math:`L_\text{Moment}` is equal to "geometry/momentLength".

.. _FAQ_input_nondim_quantity:

FAQ on non-dimensionalization of input parameters:
====================================================

How do I set the non-dimensional time step "timeStepSize"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The definition of "timeStepSize" can be found at :ref:`timeStepping <table_timeStepping>`. Assume the physical time step size is 2 seconds, speed of sound of freestream is 340 m/s and grid unit is 1 feet, so the :math:`\text{timeStepSize}= \frac{2 \text{ s} \times 340\text{ m/s}}{0.3048 \text{ m}}=2230.971128608`.

How do I set non-dimensional rotating speed "omegaRadians" with a given RPM?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The RPM determines the angular speed, and the non-dimensional "omegaRadians" can be calculated by dimensional angular speed from :ref:`slidingInterfacesParameters`. Assume the RPM = 800, speed of sound of freestream is 340 m/s and grid unit is 1 millimeter, so :math:`\text{omegaRadians}=\Omega\times L_\text{gridUnit}/C_\infty=\frac{800\times 2\pi}{60\text{ s}}\times\frac{0.001 \text{ m}}{340\text{ m/s}}=0.00024639942`.

.. _FAQ_output_nondim_quantity:

FAQ on translating non-dimensional outputs:
====================================================

In the Tecplot/Paraview visualization files, how can I translate the "velocityX" into m/s?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Because the reference value of velocity is :math:`C_\infty` from :numref:`tab_nondimensionalization_flow360`, the dimensional velocity in X direction can be obtained by multiplying the "velocityX" with speed of sound of freestream. Assume the speed of sound in the freestream is 340 m/s and "velocityX" is 0.6 in the Paraview/Tecplot file, the dimensional velocity in X direction is :math:`340 \text{ m/s} \times 0.6 = 204 \text{ m/s}`.

In the Tecplot/Paraview visualization files, how can I translate the pressure "p" into Pascal?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The reference value of pressure is :math:`\rho_\infty C_\infty^2` from :numref:`tab_nondimensionalization_flow360`. Assume the speed of sound in the freestream is 340 m/s, freestream density is 1.225 :math:`kg/m^3` and "p" is 0.65 in the Paraview/Tecplot file, the dimensional pressure is :math:`0.65\times 1.225\, kg/m^3\times 340^2\, m^2/s^2=92046.5\,Pascal`.

