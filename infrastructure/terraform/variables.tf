variable "pm_api_url" {
  default = "https://192.168.0.190:8006/api2/json"
}

variable "pm_user" {
  default ="root@pam"
}

variable "pm_password" {
  sensitive = true
}

variable "ssh_key" {
  default = "id_ed25519 ..."
}