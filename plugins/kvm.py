from plugins.base import Plugin
from logger import Log, configure_logging

import subprocess


class KVMActuator(Plugin):

    def __init__(self):
        self.logger = Log("kvm-actuator", "actuator.log")
        configure_logging()

    def allocated_resources(self, vm_id):
        try:
            command = "virsh schedinfo %s | grep vcpu_quota | awk '{print $3}'" % vm_id
            output = subprocess.check_output(command, shell = True)
            cap = int(output)
            cap = cap/1000.0
            return cap
        except Exception as e:
            print e.getMessage()
            self.logger.log(e.getMessage())
        
    def set_vcpu_cap(self, vm_id, cap):
        try:
            command = "virsh schedinfo %s --set vcpu_quota=%s > /dev/null" % (vm_id, cap * 1000)
            subprocess.Popen(command, shell = True)
        except Exception as e:
            print e.getMessage()
            self.logger.log(e.getMessage())
