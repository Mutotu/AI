class Config:
    """Class representing configuration parameters for a simulation."""

    SIM_NAME = "Ocean Simulation"
    OCEAN_SIZE = 20

    # Agent-specific configuration
    AGENT_COLOURS = {
        "shark": "blue",
        "fish": "yellow",
        "crab": "red"
    }
    AGENT_BREEDING_PROB = {
        "shark": 0.3,
        "fish": 0.6,
        "crab": 0.4
    }
