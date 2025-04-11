@description('Name of the Azure Container Registry')
param acrName string

@description('Location for the Azure Container Registry')
param location string = resourceGroup().location

resource acr 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  name: acrName
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true
  }
}

output loginServer string = acr.properties.loginServer
output adminUsername string = listCredentials(acr.id, '2023-01-01-preview').username
output adminPassword string = listCredentials(acr.id, '2023-01-01-preview').passwords[0].value
