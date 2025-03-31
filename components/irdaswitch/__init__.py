# See: https://esphome.io/guides/contributing.html#extras

import esphome.codegen as cg
import esphome.config_validation as cv

# Mark the component to depend on other components.
# If the user hasn’t explicitly added these components in their configuration, a validation error will be generated.
DEPENDENCIES = [ ]
# Automatically load a component if the user hasn’t added it manually
AUTO_LOAD = [ ]
# Mark this component to accept an array of configurations.
# If this is an integer instead of a boolean, validation will only permit the given number of entries.
MULTI_CONF = False

# GitHub usernames or team names of people that are responsible for this component
CODEOWNERS = ["@tasmaniandroid"]

# Define constants for configuration keys
CONF_USE_IRDA_ON = "use_irda_on"

# C++ namespace
ns = cg.esphome_ns.namespace("irdaswitch")
irdaswitch = ns.class_("irdaswitch", cg.Component)

# The configuration schema to validate the user config against
CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(irdaswitch),
        cv.Optional(CONF_USE_IRDA_ON, default=0): cv.int_range(min=0, max=7),

    }
)


async def to_code(config):

    # cg.add is used to add a piece of code to the generated main.cpp
    #   transceiver->set_bandwidth(200);
    cg.add(var.use_irda_on(config[CONF_USE_IRDA_ON]))
