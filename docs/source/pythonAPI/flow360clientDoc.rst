flow360client module
********************


.. py:module:: flow360client


.. py:function:: NewCase(meshId, config, caseName=None, tags=[], priority='high', parentId=None)
   :module: flow360client

   Submit a new case from mesh Id.
   
   :param meshId: Mesh Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type meshId: str
   :param config: Flow360.json parameters for the case. It can be path to the json file or python dict.
   :type config: path (str) or dict
   :param caseName: Case name, if not provided it will be the same as config file name, required if dict provided as a config, by default None
   :type caseName: str, optional
   :param tags: List of tags, by default []
   :type tags: list, optional
   :param priority: Queueing priority, 'high' or 'low', by default 'high'
   :type priority: str, optional
   :param parentId: Parent case Id for forked cases. Format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx, by default None
   :type parentId: str, optional
   
   :returns: Case id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
   :rtype: str
   

.. py:function:: NewCaseListWithPhase(meshId, config, caseName=None, tags=[], priority='high', parentId=None, phaseCount=1)
   :module: flow360client

   Submits a sequence of cases sharing the same meshId, where each case forks from the previous one.
   The maxPhysicalStep is split equally among the list of cases. This capability should only be used for
   conducting a long unsteady simulation to avoid running a single case for long time. For example, if the
   maxPhysicalStep is 1000 and phaseCount=2, the above API submits 2 cases with maxPhysicalStep=500 for each.
   
   :param meshId: Mesh Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type meshId: str
   :param config: Flow360.json parameters for the case. It can be path to the json file or python dict.
   :type config: path (str) or dict
   :param caseName: Case name, if not provided it will be the same as config file name, required if dict provided as a config, by default None
   :type caseName: str, optional
   :param tags: List of tags, by default []
   :type tags: list, optional
   :param priority: Queueing priority, 'high' or 'low', by default 'high'
   :type priority: str, optional
   :param parentId: Parent case Id for forked cases. Format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx, by default None
   :type parentId: str, optional
   :param phaseCount: [description], by default 1
   :type phaseCount: int, optional
   
   :returns: List of case ids, where case id is of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
   :rtype: str
   

.. py:function:: NewMesh(fname, noSlipWalls=None, meshName=None, tags=[], fmat=None, endianness=None, solverVersion=None, meshJson=None)
   :module: flow360client

   Uploads new mesh. Supports CGNS and UGRID mesh formats. For CGNS mesh format, noSlipWalls are validated with the mesh before upload (requires h5py to by installed).
   
   :param fname: Path to mesh file.
   :type fname: path (str)
   :param noSlipWalls: List of no-slip walls in the mesh, must be provided if meshJson not provided, by default None
   :type noSlipWalls: list, optional
   :param meshName: Mesh name, if not provided mesh file name will be used, by default None
   :type meshName: str, optional
   :param tags: List of mesh tags, by default []
   :type tags: list, optional
   :param fmat: Mesh file format, supported [aflr3, cgns]. Automatically deducted if not provided, by default None
   :type fmat: str, optional
   :param endianness: Endianness for UGIRD mesh, 'big' for .b8.ugrid, and 'little' for .lb8.ugrid, if not provided, read from file extention, by default None
   :type endianness: str, optional
   :param solverVersion: Solver version to be used for mesh and cases created from this mesh. If not provided, the latest will be used, by default None
   :type solverVersion: str, optional
   :param meshJson: Flow360Mesh.json parameters for the mesh. It can be path to the json file or python dict. Must be provided if noSlipWalls not provided, by default None
   :type meshJson: path (str) or dict, optional
   
   :returns: Mesh id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
   :rtype: str
   

.. py:function:: NewMeshFromSurface(surfaceMeshId, config, meshName=None, tags=[], solverVersion=None)
   :module: flow360client

   Generates new volume mesh from surface mesh.
   
   :param surfaceMeshId: Surface mesh Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type surfaceMeshId: str
   :param config: Flow360SurfaceToVolumeMesh.json parameters for the volume mesher. It can be path to the json file or python dict.
   :type config: path (str) or dict
   :param meshName: Mesh name, if not provided it will be the same as config file name, required if dict provided as a config, by default None
   :type meshName: str, optional
   :param tags: List of mesh tags, by default []
   :type tags: list, optional
   :param solverVersion: Solver version to be used for mesh and cases created from this mesh. If not provided, the latest will be used, by default None
   :type solverVersion: str, optional
   
   :returns: Mesh id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
   :rtype: str
   

.. py:function:: NewSurfaceMeshFromGeometry(fileName, geometryToSurfaceMeshJson, meshName=None, tags=[], solverVersion=None)
   :module: flow360client

   Creates new surface mesh from geometry.
   
   :param fileName: Geometry file name. Supported format: CSM (Engineering Sketch Pad)
   :type fileName: path (str)
   :param geometryToSurfaceMeshJson: Flow360GeometryToSurfaceMesh.json parameters for the surface mesher. It can be path to the json file or python dict.
   :type geometryToSurfaceMeshJson: path (str) or dict
   :param meshName: Surface mesh name, by default None
   :type meshName: str, optional
   :param tags: List of surface mesh tags, by default []
   :type tags: list, optional
   :param solverVersion: Solver version to be used for surface mesh, volume mesh and cases created from this mesh. If not provided, the latest will be used, by default None
   :type solverVersion: str, optional
   
   :returns: Surface mesh id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
   :rtype: str
   

.. py:function:: noSlipWallsFromMapbc(mapbcFile)
   :module: flow360client

   Reads noSlipWalls from mapbc file (UGRID).
   
   :param mapbcFile: Path to mapbc file
   :type mapbcFile: path (str)
   
   :returns: List of no-slip walls.
   :rtype: list
   

.. py:module:: flow360client.case


.. py:function:: DeleteCase(caseId)
   :module: flow360client.case

   Deletes case of given caseId
   
   :param caseId: Case Id to be deleted. Format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type caseId: str
   
   :returns: Returns http response of the delete operation.
   :rtype: http response
   

.. py:function:: DownloadResultsFile(caseId, src, target=None)
   :module: flow360client.case

   For a given caseId downloads a result file. The following files can be downloaded through this function:
   
       * `surfaces.tar.gz` - surface data of the case, for visualisation or postprocessing
       * `volumes.tar.gz` - volumetric data of the case, for visualisation or postprocessing
       * `nonlinear_residual_v2.csv`- nonlinear residuals. The header of the file is ``physical_step, pseudo_step, <equation>...``
       * `linear_residual_v2.csv` - linear residuals. The header of the file is ``physical_step, pseudo_step, 0_NavierStokes_linearIterations, <equation>..., 0_<turbulence model>_linearIterations, <equation>...``
       * `cfl_v2.csv` - cfl number. The header of the file is ``physical_step, pseudo_step, <equation>...``
       * `minmax_state_v2.csv` - min and max state of the case. Contains minimum value of pressure, minimum value of density, and maximum value of velocity magnitude, with respective locations. The header of the file is ``physical_step, pseudo_step, min_rho, min_rho_x, min_rho_y, min_rho_z, min_p, min_p_x, min_p_y, min_p_z, max_umag, max_umag_x, max_umag_y, max_umag_z``
       * `surface_forces_v2.csv` - all surface forces splited by boundary (no-slip wall surfaces). The header of the file is ``physical_step, pseudo_step, <name>_CL, <name>_CD, <name>_CFx, <name>_CFy, <name>_CFz, <name>_CMx, <name>_CMy, <name>_CMz, <name>_CLPressure, <name>_CDPressure, <name>_CFxPressure, <name>_CFyPressure, <name>_CFzPressure, <name>_CMxPressure, <name>_CMyPressure, <name>_CMzPressure, <name>_CLViscous, <name>_CDViscous, <name>_CFxViscous, <name>_CFyViscous, <name>_CFzViscous, <name>_CMxViscous, <name>_CMyViscous, <name>_CMzViscous, <name>_HeatTransfer``, where ``name`` is the name of the no-slip wall surface.
       * `total_forces_v2.csv` - total forces of the case integrated over all no-slip walls. The header of the file is ``physical_step, pseudo_step, CL, CD, CFx, CFy, CFz, CMx, CMy, CMz, CLPressure, CDPressure, CFxPressure, CFyPressure, CFzPressure, CMxPressure, CMyPressure, CMzPressure, CLViscous, CDViscous, CFxViscous, CFyViscous, CFzViscous, CMxViscous, CMyViscous, CMzViscous, HeatTransfer``
       * `bet_forces_v2.csv` - forces from BET model. The header of the file is ``physical_step, pseudo_step, Disk<i>_Force_x, Disk<i>_Force_y, Disk<i>_Force_z, Disk<i>_Moment_x, Disk<i>_Moment_y, Disk<i>_Moment_z, Disk<i>_Blade<b>_R<j>_Radius, Disk<i>_Blade<b>_R<j>_ThrustCoeff, Disk<i>_Blade<b>_R<j>_TorqueCoeff``, where ``i`` is an index of BET disk, ``b`` is an index of the blade, and ``j`` is an index of the loading node.
       * `actuatorDisk_output_v2.csv` - output of actuatorDisk model. The header of the file is ``physical_step, pseudo_step, Disk<i>_Power``, where ``i`` is an index of the actuator disk.
   
   :param caseId: Case Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type caseId: str
   :param src: Filename to be downloaded.
   :type src: str
   :param target: Filename to be used to save the file locally. If not provided the local filename will be the same as src, by default None
   :type target: str, optional
   

.. py:function:: DownloadSurfaceResults(caseId, fileName=None)
   :module: flow360client.case

   Downloads surface results for a give caseId.
   
   :param caseId: Case Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type caseId: str
   :param fileName: Filename to be used to save the file. Must end with '.tar.gz'. If not provided, the file will be saved as 'surfaces.tar.gz', by default None
   :type fileName: str, optional
   

.. py:function:: DownloadVolumetricResults(caseId, fileName=None)
   :module: flow360client.case

   Downloads volumetric results for a give caseId.
   
   :param caseId: Case Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type caseId: str
   :param fileName: Filename to be used to save the file locally. Must end with '.tar.gz'. If not provided, the file will be saved as 'volumes.tar.gz', by default None
   :type fileName: str, optional
   

.. py:function:: GetCaseInfo(caseId)
   :module: flow360client.case

   Parses information about case of given caseId
   
   :param caseId: Case Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type caseId: str
   
   :returns: Returns http response.
   :rtype: http response
   

.. py:function:: GetCaseLinearResidual(caseId)
   :module: flow360client.case

   Gets solver linear residuals for a given caseId
   
   :param caseId: Case Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type caseId: str
   
   :returns: Returns dict consisting linear residuals for all the equations. The format is the following (for a case with SpalartAllmaras turbulence model):
   
             .. code-block::
   
                 {
                     'physical_step':                        [...],
                     'pseudo_step':                          [...],
                     '0_NavierStokes_linearIterations':      [...],
                     '0_cont':                               [...],
                     '1_momx':                               [...],
                     '2_momy':                               [...],
                     '3_momz':                               [...],
                     '4_energ':                              [...],
                     '5_SpalartAllmaras_linearIterations':   [...],
                     '5_nuHat':                              [...]
                 }
   :rtype: dict
   

.. py:function:: GetCaseResidual(caseId)
   :module: flow360client.case

   Gets solver nonlinear residuals for a given caseId
   
   :param caseId: Case Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type caseId: str
   
   :returns: Returns dict consisting nonlinear residuals for all the equations. The format is the following:
   
             .. code-block::
   
                 {
                     'physical_step': [...],
                     'pseudo_step':   [...],
                     '0_cont':        [...],
                     '1_momx':        [...],
                     '2_momy':        [...],
                     '3_momz':        [...],
                     '4_energ':       [...],
                     '5_nuHat':       [...]
                 }
   :rtype: dict
   

.. py:function:: GetCaseTotalForces(caseId)
   :module: flow360client.case

   For a given caseId gets the case's total forces
   
   :param caseId: Case Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type caseId: str
   
   :returns: Returns a dict consisting total forces in the following format:
   
             .. code-block::
   
                 {
                     'physical_step':    [...],
                     'pseudo_step':      [...],
                     'CL':               [...],
                     'CD':               [...],
                     'CFx':              [...],
                     'CFy':              [...],
                     'CFz':              [...],
                     'CMx':              [...],
                     'CMy':              [...],
                     'CMz':              [...],
                     'CLPressure':       [...],
                     'CDPressure':       [...],
                     'CFxPressure':      [...],
                     'CFyPressure':      [...],
                     'CFzPressure':      [...],
                     'CMxPressure':      [...],
                     'CMyPressure':      [...],
                     'CMzPressure':      [...],
                     'CLViscous':        [...],
                     'CDViscous':        [...],
                     'CFxViscous':       [...],
                     'CFyViscous':       [...],
                     'CFzViscous':       [...],
                     'CMxViscous':       [...],
                     'CMyViscous':       [...],
                     'CMzViscous':       [...],
                     'HeatTransfer':     [...]
                 }
   :rtype: dict
   

.. py:module:: flow360client.mesh


.. py:function:: DeleteMesh(meshId)
   :module: flow360client.mesh

   Deleted mesh of given meshId
   
   :param meshId: Mesh Id to be deleted. Format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type meshId: str
   
   :returns: Returns http response of the delete operation.
   :rtype: http response
   

.. py:function:: GetMeshInfo(meshId)
   :module: flow360client.mesh

   Parses information about mesh of given meshId
   
   :param meshId: Mesh Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type meshId: str
   
   :returns: Returns http response.
   :rtype: http response
   

.. py:function:: ListMeshes(include_deleted=False)
   :module: flow360client.mesh

   Gets list of meshes.
   
   :param include_deleted: Whether to include deleted meshes in the list, by default False
   :type include_deleted: bool, optional
   
   :returns: List of meshes
   :rtype: list
   

.. py:module:: flow360client.surfaceMesh


.. py:function:: DeleteSurfaceMesh(surfaceMeshId)
   :module: flow360client.surfaceMesh

   Deletes surface mesh of given surfaceMeshId
   
   :param surfaceMeshId: Surface mesh id to be deleted. Format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type surfaceMeshId: str
   
   :returns: Returns http response of the delete operation.
   :rtype: http response
   

.. py:function:: GetSurfaceMeshInfo(surfaceMeshId)
   :module: flow360client.surfaceMesh

   Parses information about surface mesh of given surfaceMeshId
   
   :param surfaceMeshId: Surface mesh id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type surfaceMeshId: str
   
   :returns: Returns http response.
   :rtype: http response
   

.. py:function:: ListSurfaceMeshes(include_deleted=False)
   :module: flow360client.surfaceMesh

   Gets list of surface meshes
   
   :param include_deleted: Whether to include deleted meshes in the list, by default False
   :type include_deleted: bool, optional
   
   :returns: List of surface meshes
   :rtype: list
   
