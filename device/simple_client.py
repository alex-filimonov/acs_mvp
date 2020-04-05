#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests
import json
import sys
import lib.Init as Init
import lib.Processor as Processor
import argparse

parent_parser = argparse.ArgumentParser()
parent_parser.add_argument('--acs_url', type=str,help='URL Auto Configurate Server (default get acs url by configuration file)')
parent_parser.add_argument('--mode', type=str,default="simple",help='device mode (simple/periodic)')
parent_parser.add_argument('--sn', type=str, help='serial number device')
parent_parser.add_argument('--periodic_inform_interval', type=str, help="time (seconds) when device send inform message")

init=Init.Init()
init.config_file='./etc/device.conf'
init.read_config(parent_parser)


processor=Processor.Processor();
processor.do()



