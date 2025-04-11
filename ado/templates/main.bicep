@description('Name of the Azure Container Registry')
param acrName string = 'flaskacrdeel'

@description('Name of the Azure Container Instance')
param containerName string = 'flask-container'

@description('Location for the resources')
param location string = resourceGroup().location

@description('Docker image tag')
param imageTag string = 'latest'

// Deploy ACR
module acrModule './acr.bicep' = {
  name: 'deployAcr'
  params: {
    acrName: acrName
    location: location
  }
}

// Deploy ACI
module aciModule './aci.bicep' = {
  name: 'deployAci'
  params: {
    containerName: containerName
    location: location
    imageTag: imageTag
    acrLoginServer: acrModule.outputs.loginServer
    acrAdminUsername: acrModule.outputs.adminUsername
    acrAdminPassword: acrModule.outputs.adminPassword
  }
}
