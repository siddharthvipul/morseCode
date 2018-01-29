#!/bin/bash
sudo dnf update -y
#Setup RH VPN
sudo bash -c 'cat <<EOF> /etc/vpnc/default.conf
IPSec gateway 209.132.188.252
IKE Authmode psk
IPSec ID RH-standard
IPSec secret nodnerip
IKE DH Group dh2
NAT Traversal mode natt
Xauth username vsiddhar
EOF'
cat << EOF | sudo tee /etc/yum.repos.d/rhel7-csb-stage.repo
[rhel7-csb]
name=RHEL7 CSB packages Staging
baseurl=http://hdn.corp.redhat.com/rhel7-csb-stage/
enabled=1
gpgcheck=0
EOF
sudo dnf install -y redhat-internal-cert-install redhat-internal-NetworkManager-openvpn-profiles.noarch
