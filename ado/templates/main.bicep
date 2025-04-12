@description('Name of the Azure Container Registry')
param acrName string = 'flaskacrdeel'

@description('Name of the Azure Container Instance')
param containerName string = 'flask-container'

@description('Location for the resources')
param location string = resourceGroup().location

@description('Docker image tag')
param imageTag string = 'latest'

@description('Name of the Application Gateway')
param appGatewayName string = 'flaskAppGateway'

@description('Public IP name for the Application Gateway')
param publicIpName string = 'flaskAppGatewayPublicIP'

@description('Name of the Virtual Network')
param vnetName string = 'appGatewayVNet'

@description('Address space for the Virtual Network')
param vnetAddressPrefix string = '10.0.0.0/16'

@description('Name of the Subnet for the Application Gateway')
param subnetName string = 'appGatewaySubnet'

@description('Address prefix for the Subnet')
param subnetAddressPrefix string = '10.0.1.0/24'

// Deploy ACR
module acrModule './acr.bicep' = {
  name: 'deployAcr'
  params: {
    acrName: acrName
    location: location
  }
}

// Deploy VNet and Subnet
module vnetModule './vnet.bicep' = {
  name: 'deployVNet'
  params: {
    vnetName: vnetName
    vnetAddressPrefix: vnetAddressPrefix
    subnetName: subnetName
    subnetAddressPrefix: subnetAddressPrefix
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

// Deploy Application Gateway
module appGatewayModule './app-gateway.bicep' = {
  name: 'deployAppGateway'
  params: {
    appGatewayName: appGatewayName
    publicIpName: publicIpName
    location: location
    subnetId: vnetModule.outputs.subnetId
    backendFqdn: aciModule.outputs.dnsName
    backendPort: 5000
  }
}
