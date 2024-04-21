from enum  import Enum

class TerrainLocation(Enum):
    """Enum with the possible terrain locations.

    Attributes:
        GRASSED_STRIP: Grassed Strip.
        ASPHALTED_STRIP: Asphalted Strip.
        SIDEWALK: Sidewalk.
        SIDEWALK_END: Sidewalk End.
        PARK: Park.
        GRASSED_FLOWERBED: Grassed Flowerbed.
        ASPHALTED_FLOWERBED: Asphalted Flowerbed.
        FLOWERBED: Flowerbed.
        MEDIAN_STRIP: Median Strip.
    """
    GRASSED_STRIP = "Grassed Strip"
    ASPHALTED_STRIP = "Asphalted Strip"
    SIDEWALK = "Sidewalk"
    SIDEWALK_END = "Sidewalk End"
    PARK = "Park"
    GRASSED_FLOWERBED = "Grassed Flowerbed"
    ASPHALTED_FLOWERBED = "Asphalted Flowerbed"
    FLOWERBED = "Flowerbed"
    MEDIAN_STRIP = "Median Strip"