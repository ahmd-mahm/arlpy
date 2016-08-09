##############################################################################
#
# Copyright (c) 2016, Mandar Chitre
#
# This file is part of arlpy which is released under Simplified BSD License.
# See file LICENSE or go to http://www.opensource.org/licenses/BSD-3-Clause
# for full license details.
#
##############################################################################

"""Common utility functions."""

from numpy import log10 as _log10, power as _power

def mag2db(x):
    """Convert magnitude quantity to dB."""
    return 20*_log10(x)

def pow2db(x):
    """Convert power quantity to dB."""
    return 10*_log10(x)

def db2mag(x):
    """Convert dB quantity to magnitude."""
    return _power(10, x/20.0)

def db2pow(x):
    """Convert dB quantity to power."""
    return _power(10, x/10.0)
