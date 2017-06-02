from abc import ABCMeta, abstractmethod


class Plugin:
    __metaclass__ = ABCMeta

    @abstractmethod
    def allocated_resources(self, vm_id): pass

    @abstractmethod
    def set_vcpu_cap(self, vm_id, cap): pass

