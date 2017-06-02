from flask import Flask, request, jsonify

from plugins.kvm import KVMActuator

app = Flask(__name__)


@app.route('/actuator/allocated_resources/', methods=['POST'])
def setup_env():
    data = request.get_json()

    if data['actuator_plugin'] == 'kvm':
        actuator = KVMActuator
        actuator.allocated_resources(data['vm_id'])
        return 'ok', 200

    return 'fail', 500


@app.route('/actuator/set_vcpu_cap/', methods=['POST'])
def setup_cap():
    data = request.get_json()

    if data['actuator_plugin'] == 'kvm':
        actuator = KVMActuator
        actuator.allocated_resources(data['vm_id'], int(data['cap']))
        return 'ok', 200

    return 'fail', 500

if __name__ == '__main__':
    app.run(port=5047, host='0.0.0.0')
