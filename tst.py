#!/usr/bin/env python3
from parsetfvars import ParseTfvars

var = ParseTfvars('terraform.tfvars')

print(var.st('cadena'))
print(var.lt('lista'))
print(var.nb('numero'))
