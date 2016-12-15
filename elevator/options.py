import shlex

from stix2validator.scripts import stix2_validator
from stix2validator.validators import ValidationOptions


SQUIRREL_GAPS_IN_DESCRIPTIONS = True

INFRASTRUCTURE_IN_20 = False

INCIDENT_IN_20 = True

DEFAULT_TIMESTAMP = ""

DEFAULT_IDENTIFIER = ""


class ElevatorOptions(object):
    """Collection of elevator options which can be set via command line or
    programmatically in a script.

    It can be initialized either by passing in the result of parse_args() from
    argparse to the cmd_args parameter, or by specifying individual options
    with the other parameters.

    Attributes:
        cmd_args: An instance of ``argparse.Namespace`` containing options
            supplied on the command line.
        verbose: True if informational notes and more verbose error messages
            should be printed to stdout/stderr.
        file_: Input file to be elevated.
        no_incidents: False if no incidents should be included in the result.
        infrastructure: True if infrastructure should be included in the result.
        package_created_by_id: If set, this identifier ref will be applied in
            the `created_by_ref` property.
        default_timestamp: If set, this value will be used when: the object
            does not have a timestamp, the parent does not have a timestamp.
            When this value is not set, current time will be used instead.
        validator_args: If set, these values will be used to create a
            ValidationOptions instance if requested.
        enable: Messages to enable.
        disable: Messages to disable.

    """
    def __init__(self, cmd_args=None, file_=None, no_incidents=True,
                 squirrel_gaps=True, infrastructure=False,
                 package_created_by_id=None, default_timestamp=None,
                 validator_args="--lax --strict-types", verbose=False,
                 enable="", disable=""):
        if cmd_args is not None:
            self.file_ = cmd_args.file_
            self.no_incidents = cmd_args.no_incidents
            self.squirrel_gaps = squirrel_gaps
            self.infrastructure = cmd_args.infrastructure
            self.package_created_by_id = cmd_args.default_created_by_id
            self.default_timestamp = cmd_args.default_timestamp
            self.validator_args = cmd_args.validator_args

            self.verbose = cmd_args.verbose
            self.enable = cmd_args.enable
            self.disable = cmd_args.disable

        else:
            self.file_ = file_
            self.no_incidents = no_incidents
            self.squirrel_gaps = squirrel_gaps
            self.infrastructure = infrastructure
            self.package_created_by_id = package_created_by_id
            self.default_timestamp = default_timestamp
            self.validator_args = validator_args

            self.verbose = verbose
            self.enable = enable
            self.disable = disable

        # Convert string of comma-separated checks to a list,
        # and convert check code numbers to names
        if self.disable:
            self.disable = self.disable.split(",")
            self.disable = [CHECK_CODES[x] if x in CHECK_CODES else x
                            for x in self.disable]
        if self.enable:
            self.enable = self.enable.split(",")
            self.enable = [CHECK_CODES[x] if x in CHECK_CODES else x
                           for x in self.enable]

    def get_validator_options(self):
        """Return a stix2validator.validators.ValidationOptions instance."""
        # Parse stix-validator command-line args
        validator_parser = stix2_validator._get_arg_parser(is_script=False)
        validator_args = validator_parser.parse_args(
            shlex.split(self.validator_args))

        validator_args.files = None
        return ValidationOptions(validator_args)


def set_infrastructure(include_infrastructure=False):
    global INFRASTRUCTURE_IN_20
    INFRASTRUCTURE_IN_20 = include_infrastructure


def set_incidents(include_incidents=True):
    global INCIDENT_IN_20
    INCIDENT_IN_20 = include_incidents


def set_gap_descriptions(include_descriptions=True):
    global SQUIRREL_GAPS_IN_DESCRIPTIONS
    SQUIRREL_GAPS_IN_DESCRIPTIONS = include_descriptions


def set_default_identifier(default_identifier=""):
    global DEFAULT_IDENTIFIER
    DEFAULT_IDENTIFIER = default_identifier


def set_default_timestamp(default_timestamp=""):
    global DEFAULT_TIMESTAMP
    DEFAULT_TIMESTAMP = default_timestamp


def set_options(options):
    set_infrastructure(options.infrastructure)
    set_incidents(options.no_incidents)
    set_gap_descriptions(options.squirrel_gaps)
    set_default_identifier(options.package_created_by_id)
    set_default_timestamp(options.default_timestamp)


# Mapping of check code numbers to names
# TODO: complete list
CHECK_CODES = {
    '3': 'append-to-description-property',
    '301': '',
    '302': '',
    '303': '',
    '304': '',
    '305': '',
    '306': '',
    '4': 'drop-content-not-supported',
    '401': '',
    '402': '',
    '403': '',
    '404': '',
    '405': '',
    '406': '',
    '407': '',
    '408': '',
    '409': '',
    '410': '',
    '411': '',
    '412': '',
    '413': '',
    '414': '',
    '415': '',
    '416': '',
    '417': '',
    '418': '',
    '419': '',
    '420': '',
    '421': '',
    '5': 'multiple-values-not-supported',
    '501': '',
    '502': '',
    '503': '',
    '504': '',
    '505': '',
    '506': '',
    '507': '',
    '6': 'issues-in-original-content',
    '601': '',
    '602': '',
    '603': '',
    '604': '',
    '605': '',
    '606': '',
    '607': '',
    '608': '',
    '609': '',
    '610': '',
    '611': '',
    '7': 'conversion-assumptions',
    '701': '',
    '702': '',
    '703': '',
    '704': '',
    '705': '',
    '706': '',
    '707': '',
    '708': '',
    '709': '',
    '710': '',
    '711': '',
    '712': '',
    '713': '',
    '8': 'content-not-supported',
    '801': '',
    '802': '',
    '803': '',
    '804': '',
    '805': '',
    '806': '',
    '807': '',
    '808': '',
    '9': 'using-parent-or-current-timestamp',
    '901': '',
    '902': '',
    '903': '',
    '904': '',
    '905': '',
}
