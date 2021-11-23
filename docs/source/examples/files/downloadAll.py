# downloadALL.py

import time
import json
import os
import subprocess

import flow360client
from flow360client import case, mesh, NewMesh, NewCase
import json

rootPath = os.path.dirname(os.path.abspath(__file__))

def getNoSlipWallsFromCaseId(caseId):
    caseObj = case.GetCaseInfo(caseId.strip())
    allBndrys = caseObj['runtimeParams']['boundaries']
    noSlipWalls = list()
    for bndName, bndObj in allBndrys.items():
        if bndObj["type"] == "NoSlipWall":
            noSlipWalls.append(bndName)
    return noSlipWalls

def writeDictToDisk(data, resultDir):
    os.makedirs(resultDir, exist_ok=True)
    for tableName, tableData in data.items():
        filePath = os.path.join(resultDir, tableName+'.txt')
        with open(filePath, 'w') as fh:
            for value in tableData:
                fh.write("{:e}\n".format(value))

def writeSurfaceForce(surfForceDict, resultDir):
    for bndName, dataSet in surfForceDict.items():
        writeDictToDisk(dataSet, os.path.join(resultDir, bndName))

if __name__ == "__main__":
    caseId = 'f9edc8da-1202-4820-9884-88a726163917' ## Replace the caseId with your own caseId
    rootPath = os.path.join(rootPath, './result_'+caseId)
    os.makedirs(rootPath, exist_ok=True)

    caseInfo = case.GetCaseInfo(caseId)
    caseStatus = caseInfo['caseStatus']

    if caseStatus == 'completed':
        solverOutPath = os.path.join(rootPath, 'solver.out')
        surfaceSolPath = os.path.join(rootPath, 'surfaces.tar.gz')
        volumeSolPath = os.path.join(rootPath, 'volumes.tar.gz')
        totalForcePath = os.path.join(rootPath, 'total_forces')
        residualPath = os.path.join(rootPath, 'residual')
        surfaceForcePath = os.path.join(rootPath, 'surface_forces')
        caseIdFile = os.path.join(rootPath, 'caseInfo.json')

        caseInfoJson = json.dumps(caseInfo, indent=4)
        with open(caseIdFile, "w") as fh:
            fh.write(caseInfoJson)

        print("The case is completed, start downloading...")
        # download solver log
        print("Downloading solver log...")
        case.DownloadSolverOut(caseId, solverOutPath)

        # download volume solution
        print("Downloading volume solution...")
        case.DownloadVolumetricResults(caseId, volumeSolPath)

        # download surface solution
        print("Downloading surface solution...")
        case.DownloadSurfaceResults(caseId, surfaceSolPath)

        # download residual convergence history
        print("Downloading residual history...")
        residual = case.GetCaseResidual(caseId)
        writeDictToDisk(residual, residualPath)

        # download total force
        print("Downloading total forces...")
        totalForce = case.GetCaseTotalForces(caseId)
        writeDictToDisk(totalForce, totalForcePath)

        # download surface force by components
        print("Downloading surface forces...")
        noSlipWalls = getNoSlipWallsFromCaseId(caseId)
        surfaceComponentForce = case.GetCaseSurfaceForcesByNames(caseId, noSlipWalls)
        for bndName, dataSet in surfaceComponentForce.items():
            writeDictToDisk(dataSet, os.path.join(surfaceForcePath, bndName))
        # all downloading finishes
    else:
        print("The case's status is not completed, so skip all downloading")
