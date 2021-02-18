resource "proxmox_vm_qemu" "web-dev" {
  count       = 1
  name        = "web-dev-${count.index}"
  target_node = "proxmox"

  clone = "CentOS-Template"

  os_type  = "cloud-init"
  cores    = 2
  sockets  = "1"
  cpu      = "host"
  memory   = 2048
  scsihw   = "virtio-scsi-pci"
  bootdisk = "scsi0"
  agent    = 1

  disk {
    size    = "20G"
    type    = "scsi"
    storage = "local-lvm"
  }

  network {
    model  = "virtio"
    bridge = "vmbr0"
  }

  lifecycle {
    ignore_changes = [
      network,
    ]
  }

  # Cloud Init Settings
  ipconfig0    = "ip=192.168.0.11${count.index + 1}/24,gw=192.168.0.1"
  searchdomain = "internal.alexcook.dev"
  nameserver   = "192.168.0.180"
  ciuser       = "centos"

#   sshkeys = <<EOF
#     ${var.ssh_key}
#     EOF
}

resource "proxmox_vm_qemu" "db-dev" {
  count       = 1
  name        = "db-dev-${count.index}"
  target_node = "proxmox"

  clone = "CentOS-Template"

  os_type  = "cloud-init"
  cores    = 2
  sockets  = "1"
  cpu      = "host"
  memory   = 2048
  scsihw   = "virtio-scsi-pci"
  bootdisk = "scsi0"
  agent    = 1

  disk {
    size    = "20G"
    type    = "scsi"
    storage = "local-lvm"
  }

  network {
    model  = "virtio"
    bridge = "vmbr0"
  }

  lifecycle {
    ignore_changes = [
      network,
    ]
  }

  # Cloud Init Settings
  ipconfig0    = "ip=192.168.0.11${count.index + 1}/24,gw=192.168.0.1"
  searchdomain = "internal.alexcook.dev"
  nameserver   = "192.168.0.180"
  ciuser       = "centos"

#   sshkeys = <<EOF
#     ${var.ssh_key}
#     EOF
}

# Ansible inventory
resource "ansible_host" "web-dev" {
  count              = 1
  inventory_hostname = "web-dev-${count.index}"
  vars = {
    ansible_host = "192.168.0.1${count.index + 1}"
  }
  groups              = ["web, dev"]
}

resource "ansible_host" "db-dev" {
  count              = 1
  inventory_hostname = "db-dev-${count.index}"
  vars = {
    ansible_host = "192.168.0.1${count.index + 1}"
  }
  groups              = ["db, dev"]
}

