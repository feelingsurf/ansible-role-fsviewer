def test_fsviewer_group_exists(host):
    group = host.group("fsviewer")
    assert group.exists


def test_fsviewer_user_exists(host):
    user = host.user("fsviewer")
    assert user.exists
    assert user.group == "fsviewer"
    assert user.shell == "/bin/bash"


def test_feelingsurfviewer_package_is_installed(host):
    package = host.package("feelingsurfviewer")
    assert package.is_installed
    assert package.version == "2.5.1"


def test_systemd_service_file_exists(host):
    config = host.file("/etc/systemd/system/fsviewer.service")
    assert config.exists
    assert config.is_file
    assert config.user == "root"
    assert config.group == "root"
    assert config.mode == 0o644


def test_fsviewer_service_is_running(host):
    service = host.service("fsviewer")
    assert service.is_enabled
    assert service.is_running
