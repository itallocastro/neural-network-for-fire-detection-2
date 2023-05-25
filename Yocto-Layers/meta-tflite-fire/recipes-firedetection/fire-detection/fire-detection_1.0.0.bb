SUMMARY = "Fire detection with webcam image."
DESCRIPTION = "Recipe created by bitbake-layers"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta/files/common-licenses/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

FILESEXTRAPATHS_prepend := "${THISDIR}:"


SRC_URI += "file://setup.py \
      file://firedetection/__init__.py \
      file://firedetection/main.py \ 
      file://firedetection/model.tflite"

S = "${WORKDIR}" 

inherit setuptools3 

do_install_append () { 
    install -d ${D}${bindir} 
} 
