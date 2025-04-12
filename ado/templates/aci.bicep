@description('Name of the Azure Container Instance')
param containerName string

@description('Location for the Azure Container Instance')
param location string = resourceGroup().location

@description('Docker image tag')
param imageTag string = 'latest'

@description('ACR login server')
param acrLoginServer string

@description('ACR admin username')
param acrAdminUsername string

@description('ACR admin password')
param acrAdminPassword string

resource containerGroup 'Microsoft.ContainerInstance/containerGroups@2021-10-01' = {
  name: containerName
  location: location
  properties: {
    containers: [
      {
        name: containerName
        properties: {
          image: '${acrLoginServer}/flask-app:${imageTag}'
          resources: {
            requests: {
              cpu: 1
              memoryInGB: 2
            }
          }
          ports: [
            {
              port: 5000
            }
          ]
          environmentVariables: [
            {
              name: 'FLASK_HOST'
              value: '0.0.0.0'
            }
            {
              name: 'FLASK_PORT'
              value: '5000'
            }
          ]
        }
      }
    ]
    osType: 'Linux'
    ipAddress: {
      type: 'Public'
      dnsNameLabel: '${containerName}-${uniqueString(resourceGroup().id)}'
      ports: [
        {
          protocol: 'TCP'
          port: 5000
        }
      ]
    }
    imageRegistryCredentials: [
      {
        server: acrLoginServer
        username: acrAdminUsername
        password: acrAdminPassword
      }
    ]
  }
}
