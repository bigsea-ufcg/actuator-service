from plugins.base import Plugin

import subprocess


class KVMActuator(Plugin):

    def __init__(self):
        pass

    def allocated_resources(self, vm_id, cap):
        command = "virsh schedinfo %s | grep vcpu_quota | awk '{print $3}'" % (vm_id)
        subprocess.call(command)

    def set_vcpu_cap(self, vm_id, cap):
        command = "virsh schedinfo %s --set vcpu_quota=%s > /dev/null" % (vm_id, cap * 1000)
        subprocess.call(command)
