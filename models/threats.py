#!/usr/bin/env python3
##
# Nicolas THIBAUT
# nicolas.thibaut@uppersafe.com
##
# -*- coding: utf-8 -*-

import time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

class threats(declarative_base()):
    __tablename__ = "threats"

    id = Column(Integer, primary_key=True)
    ts = Column(Integer, default=0)
    domain = Column(String, unique=True)
    ipaddr = Column(String, unique=True)
    jsondata = Column(String)
    flag = Column(Integer, default=0)
