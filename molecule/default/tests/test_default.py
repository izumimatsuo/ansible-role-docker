import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_docker_is_installed(host):
    package = host.package("docker-ce")
    assert package.is_installed
    assert package.version.startswith("19.0")


# def test_docker_running_and_enabled(host):
#     service = host.service('docker')
#     assert service.is_running
#     assert service.is_enabled


def test_docker_compose_is_installed(host):
    assert '1.26' in host.check_output('docker-compose --version')
