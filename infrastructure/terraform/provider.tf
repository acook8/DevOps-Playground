terraform {
  backend "remote" {
    organization = "DevOps-Playground-acook8"

    workspaces {
      name = "DevOps-Playground"
    }
  }
  required_providers {
    proxmox = {
      source  = "Telmate/proxmox"
      version = "2.6.7"
    }
    ansible = {
      source = "nbering/ansible"
      version = "1.0.4"
    }
  }
}

provider "proxmox" {
  pm_parallel     = 1
  pm_tls_insecure = true
  pm_api_url      = var.pm_api_url
  pm_password     = var.pm_password
  pm_user         = var.pm_user
}
provider "ansible" {
  
}
