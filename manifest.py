'''
Created on Oct 2, 2014

@author: fabiomignini
'''

class Manifest(object):
    def __init__(self, name = None, expandable = False, vnf_type = None,
                uri = None, memory_size = 0, root_file_system_size = 0, 
                ephemeral_file_system_size = 0, swap_disk_size = 0,
                cpu_requirements = None, ports = None):
        self.name = name
        self.expandable = expandable
        self.vnf_type = vnf_type
        self.uri = uri
        self.memory_size = memory_size
        self.root_file_system_size = root_file_system_size
        self.ephemeral_file_system_size = ephemeral_file_system_size
        self.swap_disk_size = swap_disk_size
        self.cpu_requirements = cpu_requirements
        self.ports = ports
                 
    def parseDict(self, manifest_dict):
        self.name = manifest_dict['name']
        self.vnfType = manifest_dict['vnf-type']
        self.uri = manifest_dict['uri']
        self.memory_size = manifest_dict['memory-size']
        self.root_file_system_size = manifest_dict['root-file-system-size']
        self.ephemeral_file_system_size = manifest_dict['ephemeral-file-system-size']
        self.swap_disk_size = manifest_dict['swap-disk-size']
        self.cpu_requirements = CPURequirement().parseDict(manifest_dict['CPUrequirements'])
        self.expandable = manifest_dict['expandable']
        for port_dict in manifest_dict['ports']:
            self.ports.append(Port().parseDict(port_dict)) 
            
    def getDict(self):
        manifest_dict = {}
        manifest_dict['name'] = self.name
        manifest_dict['vnf-type'] = self.vnfType
        manifest_dict['uri'] = self.uri
        manifest_dict['memory-size'] = self.memorySize
        manifest_dict['root-file-system-size'] = self.rootFileSystemSize
        manifest_dict['ephemeral-file-system-size'] = self.ephemeralFileSystemSize
        manifest_dict['swap-disk-size'] = self.swapDiskSize
        manifest_dict['expandable'] = self.expandable
        manifest_dict['CPUrequirements'] = self.cpu_requirements.getDict()
        ports_dict = []
        for port in self.ports:
            ports_dict.append(port.getDict())
        if ports_dict:
            manifest_dict['ports'] = ports_dict
        return manifest_dict
        
        
class CPURequirement(object):
    def __init__(self, platform_type, socket):
        self.platform_type = platform_type
        self.socket = socket
        
    def parseDict(self, cpu_requirement):
        self.platform_type = cpu_requirement['platformType']
        self.socket = cpu_requirement['socket']
    
    def getDict(self):
        cpu_requirements = {}
        cpu_requirements['platformType'] = self.platform_type
        cpu_requirements['socket'] = self.socket
        return cpu_requirements
    
class Port(object):
    def __init__(self, position, label, minimum, ipv4_config, ipv6_config, name):
        self.position = position
        self.label = label
        self.min = minimum
        self.ipv4_config = ipv4_config
        self.ipv6_config = ipv6_config
        self.name = name
    
    def parseDict(self, port_dict):
        self.position = port_dict['position']
        self.label = port_dict['label']
        self.min = port_dict['min']
        self.ipv4_config = port_dict['ipv4-config']
        self.ipv6_config = port_dict['ipv6-config']
        self.name = port_dict['name']
    
    def getDict(self):
        port_dict = {}
        port_dict['name'] = self.name
        port_dict['position'] = self.position
        port_dict['label'] = self.label
        port_dict['min'] = self.min
        port_dict['ipv4-config'] = self.ipv4_config
        port_dict['ipv6-config'] = self.ipv6_config
        return port_dict