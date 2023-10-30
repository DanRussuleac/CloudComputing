
# Azure subscription ID
subscription_id="26e71196-961d-4efa-ba31-3e88fb874482"

# Resource group name
resource_group_name="test"

# Network interface parameters
network_interface_name="cloudnetwork"
network_interface_id="/subscriptions/$subscription_id/resourceGroups/$resource_group_name/providers/Microsoft.Network/networkInterfaces/cloudnetwork"

# VM parameters
vm_name="VMCloud"
vm_size="Standard_D2_v3"
vm_username="druss"
vm_os_disk_name="myVMosdisk"
vm_image_publisher="Canonical"
vm_image_offer="UbuntuServer"
vm_image_sku="16.04-LTS"
vm_image_version="latest"
vm_location="northeurope"

# Public IP parameters
public_ip_name="cloudcomputing"
public_ip_location="northeurope"

# Create Public IP
az network public-ip create --resource-group "test" --name "cloudcomputing" --sku "Basic" --allocation-method "Static" --version "IPv4" --location "northeurope"

# Create Network Interface
az network nic create --resource-group "test" --name "cloudnetwork" --location "northeurope" --subnet "/subscriptions/26e71196-961d-4efa-ba31-3e88fb874482/resourceGroups/test/providers/Microsoft.Network/virtualNetworks/VN1/subnets/mySubnet" --public-ip-address "cloudcomputing" --accelerated-networking true

# Create Virtual Machine
az vm create --resource-group "test" --name "VMCloud" --image Canonical:UbuntuServer:16.04-LTS:latest --size "Standard_D2_v3" --location "northeurope" --admin-username "druss" --os-disk-name "myVMosdisk" --os-disk-size-gb 30 --nics "cloudnetwork" --ssh-key-value "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC6DiYv7FvXebyPu5qRsTomh8hgcyb6Cd/7+Ul51qzQ8GBfa4/4rxgCQCrM+S6MTObHqbhOkubzoWBBbC9YiDWseguXMlzYUEAQVYebwuZ1SIOZ/sYQmArZ52KVFUimqgkP+ymTA4jHhZRHr1tvqkF0fPgNeTXvu6Lt8i/7z4wku+mkXOg/yKkRcXYVk6NpcViyME0FrOsWvP+GVFydcZaOYhfP7CrbnWsM62TmB4rNlUFlnWmmTz/q/cuEAb3QBEkricCNZBVoln3bXirUZwyGCfgEvNEeW4waudRfYmVn9m7W4ClU+N4W8sxzNzjm5RVotlLaSc4xnU0pKx1jpvEmNiCigwouxvAjwJ1aXt9TztQk0QSq+hj8j0PZ1qfSTgK6jqCD8VSYbYLPl0Y+BGA2P3SclWDtLabEyx/FccqGvTe31I8MJEt5kIWr5rrC+ixYd+tZEjBdjuvOxSmMTO/bW4GAqT4nHoUhH3nbqh6rxq7Qlr8X5ALfav0aV0Gp1wY4fjYRxV2GARwmlV34htTHGEFonzWJJzgCS84wsRIhnkqR0wbzNCvCrJOVmxV+PbEaXDijMKG1oyu57rLbIHRaPGJ2UlmFndh49fvQkXY4xw3XA2IbZ5dn/BpH5X7lF36FAKny0sxz0puqEc4hxHKD5OHkbUcYuHoPliOs3/e+CQQ== druss@cloudcomputing"
az vm jit-access set --resource-group "test" --name "VMCloud" --port 22 --protocol Tcp
az vm jit-access request --resource-group "test" --name "VMCloud" --port 22 --protocol Tcp --ip-address 0.0.0.0/0
az vm jit-access approve --resource-group "test" --name "VMCloud" --port 22 --protocol Tcp --id <Access_Request_ID>

