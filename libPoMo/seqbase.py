#!/usr/bin/env python

"""libPomo.seqbase
----------------------------------------------------------------------

This module provides basic functions and classes needed to work with
sequence data.

Classes:
  - :class:`Seq`, stores a single sequence
  - :class:`Region`, region in a genome

Exception Classes:
  - :class:`SequenceDataError`
  - :class:`NotAValidRefBase`

Functions:
  - :func:`stripFName()`: strip filename off its ending

"""

__docformat__ = 'restructuredtext'

import os


class SequenceDataError(Exception):
    """General sequence data error exception."""
    pass


class NotAValidRefBase(SequenceDataError):
    """Reference base is not valid."""
    pass


class Region():
    """Region in a genome.

    :param str chrom: Chromosome name.
    :param int start: 1-based start position.
    :param int end: 1-based end position.

    The start and end points are converted to 0-based positions
    that are used internally to save all positional data.
    
    :ivar str chrom: Chromosome name.
    :ivar int start: 0-based start position.
    :ivar int end: 0-base end position.

    """
    def __init__(self, chrom, start, end):
        self.chrom = chrom
        """String of chromosome name."""

        self.start = start - 1
        """Integer with start position on `self.chrom`."""

        self.end = end - 1
        """Integer with end position on `self.chrom`."""


class Seq:
    """A class that stores sequence data."""
    def __init__(self):
        self.name = ''
        """Name of the sequence (e.g. species or individual name)."""
        self.descr = ''
        """Description of the sequence."""
        self.data = ''
        """String with sequence data."""
        self.dataLen = 0
        """Number of saved bases."""

    def print_seq_header(self):
        """Print the sequence header line in fasta format."""
        print('>', self.name, ' ', self.descr, sep='')
        return

    def get_base(self, pos):
        """Returns base at position `pos`."""
        if pos > self.dataLen:
            raise SequenceDataError("Position out of range.")
        return self.data[pos-1]

    def purge(self):
        """Purge data saved in this sequence."""
        self.name = ''
        self.descr = ''
        self.data = ''
        self.dataLen = 0


def stripFName(fn):
    """Convenience function to strip filename off the ".xyz" ending."""
    filename_without_path = os.path.split(fn)[-1]
    return filename_without_path.rsplit('.', maxsplit=1)[0]
