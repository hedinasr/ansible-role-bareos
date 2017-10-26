import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_bareos(host):
    packages = [
        "bareos-common",
        "bareos-filedaemon",
        "bareos-filedaemon-glusterfs-plugin",
        "bareos-storage",
        "bareos-storage-fifo",
        "bareos-storage-glusterfs",
        "bareos-storage-tape",
        "bareos-director",
        "bareos-database-common",
        "bareos-database-mysql",
        "bareos-database-tools",
        "bareos-bconsole",
        "bareos-webui"
    ]

    for pkg in packages:
        assert host.package(pkg).is_installed
