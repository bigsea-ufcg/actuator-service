from abc import ABCMeta, abstractmethod


class Plugin:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_cpu_cap(self, vm_id, cap): pass

    @abstractmethod
    def set_vcpu_cap(self, vm_id, cap): pass

