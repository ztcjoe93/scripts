from main import *

def test_convert_header_to_anchor():
    assert convert_header_to_anchor('Auto-scaling groups (ASGs)') == '#auto-scaling-groups-asgs'
    assert convert_header_to_anchor('!@#$%^&*()_+') == '#_'