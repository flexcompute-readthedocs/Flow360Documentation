Frequently Asked Questions
==========================


Where are my AWS credentials stored locally?
--------------------------------------------

Your AWS credentials are encrypted and stored locally (if you hit Yes previously at authentication step) at

.. code-block:: python

   ~/.flow360/

For security, your password is stored as hashed value, so nobody can guess your password.


How to check my mesh processing status?
---------------------------------------

To list all your mesh files:

.. code-block:: python

   >>> flow360client.mesh.ListMeshes()

To view one particular mesh:

.. code-block:: python

   >>> flow360client.mesh.GetMeshInfo('')


My case is still running, but how can I check the current residual and surface force result?
--------------------------------------------------------------------------------------------

.. code-block:: python

   >>> caseResid = flow360client.case.GetCaseResidual('')


How do I download or view a finished case result?
-------------------------------------------------

To download the surface data (surface distributions and slices):

.. code-block:: python

   >>> flow360client.case.DownloadSurfaceResults('', '/tmp/surfaces.tar.gz')

Replace the second parameter with your target location and output file name, ending with '.tar.gz'.

To download the entire flowfield:

.. code-block:: python

   >>> flow360client.case.DownloadVolumetricResults('', '/tmp/volume.tar.gz')


How can I delete my mesh or case?
---------------------------------

To delete a mesh:

.. code-block:: python

   >>> flow360client.mesh.DeleteMesh('')

To delete a case:

.. code-block:: python

   >>> flow360client.case.DeleteCase('')

*Caution*: You won't be able to recover your deleted cases or mesh files including its results after your deletion.

