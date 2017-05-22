"""Models for Hydra Classes."""
from flask_restful import Resource


class SubSystem(Resource):
    """Class definition for general SubSystem."""

    def __init__(self, category, name):
        """Constructor."""
        self.category = category
        self.name = name


class Spacecraft_Communication(SubSystem):
    """Class definition for communication SubSystem."""

    def __init__(self, name, power, mass, cost, volume, minWorkingTemp, maxWorkingTemp):
        """Constructor."""
        SubSystem.__init__(self, "COM", name)
        self.power = power
        self.mass = mass
        self.cost = cost
        self.volume = volume
        self.minWorkingTemp = minWorkingTemp
        self.maxWorkingTemp = maxWorkingTemp


class Spacecraft_Propulsion(SubSystem):
    """Class definition for propulsion SubSystem."""

    def __init__(self, name, power, mass, cost, volume, minWorkingTemp, maxWorkingTemp):
        """Constructor."""
        SubSystem.__init__(self, "PROP", name)
        self.power = power
        self.mass = mass
        self.cost = cost
        self.volume = volume
        self.minWorkingTemp = minWorkingTemp
        self.maxWorkingTemp = maxWorkingTemp


class Spacecraft_Detector(SubSystem):
    """Class definition for detector SubSystem."""

    def __init__(self, name, power, mass, cost, volume, type_, minWorkingTemp, maxWorkingTemp):
        """Constructor."""
        SubSystem.__init__(self, "DTR", name)
        self.power = power
        self.mass = mass
        self.cost = cost
        self.volume = volume
        self.type = type_
        self.minWorkingTemp = minWorkingTemp
        self.maxWorkingTemp = maxWorkingTemp


class Spacecraft_PrimaryPower(SubSystem):
    """Class definition for primary power SubSystem."""

    def __init__(self, name, power, mass, cost, volume, minWorkingTemp, maxWorkingTemp):
        """Constructor."""
        SubSystem.__init__(self, "PPW", name)
        self.power = power
        self.mass = mass
        self.cost = cost
        self.volume = volume
        self.minWorkingTemp = minWorkingTemp
        self.maxWorkingTemp = maxWorkingTemp


class Spacecraft_BackupPower(SubSystem):
    """Class definition for backup power SubSystem."""

    def __init__(self, name, power, mass, cost, volume, minWorkingTemp, maxWorkingTemp):
        """Constructor."""
        SubSystem.__init__(self, "BCK", name)
        self.power = power
        self.mass = mass
        self.cost = cost
        self.volume = volume
        self.minWorkingTemp = minWorkingTemp
        self.maxWorkingTemp = maxWorkingTemp


class Spacecraft_Thermal(SubSystem):
    """Class definition for thermal SubSystem."""

    def __init__(self, name, power, mass, cost, volume, type_, minTemperature, maxTemperature):
        """Constructor."""
        SubSystem.__init__(self, "THR", name)
        self.power = power
        self.mass = mass
        self.cost = cost
        self.volume = volume
        self.type = type_
        self.minTemperature = minTemperature
        self.maxTemperature = maxTemperature


class Spacecraft_Structure(SubSystem):
    """Class definition for structure SubSystem."""

    def __init__(self, name, power, mass, cost, volume, minWorkingTemp, maxWorkingTemp):
        """Constructor."""
        SubSystem.__init__(self, "STR", name)
        self.power = power
        self.mass = mass
        self.cost = cost
        self.volume = volume
        self.minWorkingTemp = minWorkingTemp
        self.maxWorkingTemp = maxWorkingTemp


class Spacecraft_CDH(SubSystem):
    """Class definition for command and data SubSystem."""

    def __init__(self, name, power, mass, cost, volume, minWorkingTemp, maxWorkingTemp):
        """Constructor."""
        SubSystem.__init__(self, "CDH", name)
        self.power = power
        self.mass = mass
        self.cost = cost
        self.volume = volume
        self.minWorkingTemp = minWorkingTemp
        self.maxWorkingTemp = maxWorkingTemp


class Spacecraft_AODCS(SubSystem):
    """Class definition for altitude and orbit control SubSystem."""

    def __init__(self, name, power, mass, cost, volume, type_, mechanism, minWorkingTemp, maxWorkingTemp):
        """Constructor."""
        SubSystem.__init__(self, "AODCS", name)
        self.power = power
        self.mass = mass
        self.cost = cost
        self.volume = volume
        self.type = type_
        self.mechanism = mechanism
        self.minWorkingTemp = minWorkingTemp
        self.maxWorkingTemp = maxWorkingTemp
