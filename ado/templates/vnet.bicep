@description('Name of the Virtual Network')
param vnetName string = 'appGatewayVNet'

@description('Address space for the Virtual Network')
param vnetAddressPrefix string = '10.0.0.0/16'

@description('Name of the Subnet for the Application Gateway')
param subnetName string = 'appGatewaySubnet'

@description('Address prefix for the Subnet')
param subnetAddressPrefix string = '10.0.1.0/24'

@description('Location for the resources')
param location string = resourceGroup().location

resource vnet 'Microsoft.Network/virtualNetworks@2021-05-01' = {
  name: vnetName
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [
        vnetAddressPrefix
      ]
    }
    subnets: [
      {
        name: subnetName
        properties: {
          addressPrefix: subnetAddressPrefix
        }
      }
    ]
  }
}

output subnetId string = vnet.properties.subnets[0].id
