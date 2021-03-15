#!/usr/bin/env python

import distutils.core

name = 'mdbench'

distutils.core.setup(name=name,
    version='1.0',
    description="Metadata operations benchmark",
    long_description="Simple filsystem metadata operations benchmark",
    license="Public Domain",

    scripts=[name],
)
