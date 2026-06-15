"""Subpackage to provide all implemented materials and their (optical) material properties."""

from __future__ import annotations

import pyg4ometry.geant4 as g4
from pygeomtools.materials import LegendMaterialRegistry

from .surfaces import OpticalSurfaceRegistry


class OpticalMaterialRegistry(LegendMaterialRegistry):
    def __init__(self, g4_registry: g4.Registry):
        super().__init__(g4_registry)

        self.surfaces = OpticalSurfaceRegistry(g4_registry)
