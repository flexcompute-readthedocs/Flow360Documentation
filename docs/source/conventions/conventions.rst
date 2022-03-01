Conventions
********************

.. _nondimensionalization_Flow360:

Non-dimensionalization in Flow360
===================================

In Flow360, most input and output variables are non-dimensional. The non-dimensionalization reduces the number of free parameters and helps to provide better understanding of the underlying physics. A non-dimensional variable is obtained by dividing its dimensional counterpart by an appropriately selected constant like :eq:`def_nondim`

.. math::
   :label: def_nondim

   \text{non-dimensional variable} = \frac{\text{dimensional variable}}{\text{reference value}}

Theoretically speaking, the reference values for non-dimensionalization can be arbitrary as long as the resulting equations are identical to the original ones, but in practice, the reference values are usually selected based on some typical parameters of problems and flow chracteristics to avoid confusion. The following list shows some commonly used non-dimensional variables in both input configuration files and output files:

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

