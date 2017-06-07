from flask import Flask, request, jsonify

from plugins.kvm import KVMActuator

app = Flask(__name__)


@app.route('/actuator/allocated_resources/', methods=['POST'])
def get_allocated_resources():
    data = request.get_json()

    if data['actuator_plugin'] == 'kvm':
        actuator = KVMActuator()
        result = actuator.allocated_resources(data['vm_id'])
        return str(result), 200

    return 'fail', 500


@app.route('/actuator/set_vcpu_cap/', methods=['POST'])
def set_cap():
    data = request.get_json()

    if data['actuator_plugin'] == 'kvm':
        actuator = KVMActuator()
        actuator.set_vcpu_cap(data['vm_id'], int(data['cap']))
        return 'ok', 200

    return 'fail', 500

@app.route('/actuator/list_vms/', methods=['POST'])
def list_vms():
    data = request.get_json()
    
    if data['actuator_plugin'] == 'kvm':
        actuator = KVMActuator()
        vms = actuator.list_vms()
        vms_resp = ""
        
        if len(vms) > 0:
            vms_resp += vms[0]
            for vm in vms:
                vms_resp += "," + vm
        return vms_resp, 200
        
    return 'fail', 500

if __name__ == '__main__':
    app.run(port=5047, host='0.0.0.0')
