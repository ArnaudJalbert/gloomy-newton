from abc import ABC


class Entity(ABC):
    """
    Abstract base class for all domain entities.

    This class provides a common interface for all entities in the domain. An entity is an object that has a distinct,
    separate existence within the system, though it need not correspond to a physical object in the real world.

    Each entity in the domain should inherit from this class and implement its own specific behavior and properties.
    """
