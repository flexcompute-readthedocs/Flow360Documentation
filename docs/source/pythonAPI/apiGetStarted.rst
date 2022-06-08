Installing Flow360 Client
*************************

The Flow360 client can be installed (and updated) from PyPI.  Make sure you have the Python setuptools.  If not, sudo apt-get install python3-setuptools.

.. code-block:: python

    pip3 install flow360client
    pip3 install --upgrade flow360client

Sign in with your Account and Password
**************************************

An account can be created at https://client.flexcompute.com/app/signup.

.. code-block:: python

        python3
        >>> import flow360client
        enter your email registered at flexcompute:********@gmail.com
        Password: ***********
        Do you want to keep logged in on this machine ([Y]es / [N]o)Y

Once you have installed the Flow360 client and signed into it, you can run your first case using the ONERA M6 Wing tutorial in the :ref:`Quick Start <om6_wing_pyAPI>` section of this document.




