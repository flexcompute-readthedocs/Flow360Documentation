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

   Submits a sequence of cases from mesh Id, where each case consists of <physical time steps>/<phaseCount> and each case is forked from previous one, except for the first one.
   
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
   

.. py:function:: GetCaseInfo(caseId)
   :module: flow360client.case

   Parses information about case of given caseId
   
   :param caseId: Case Id of format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
   :type caseId: str
   
   :returns: Returns http response.
   :rtype: http response
   

.. py:module:: flow360client.casehelper


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
   

.. py:module:: flow360client.studio


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
   

.. py:module:: flow360client.task

