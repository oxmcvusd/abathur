# coding: utf8

from .base_command import Command
from abathur import build


class BuildCommand(Command):
    def __init__(self):
        super().__init__("build", "help")

    def add_custom_options(self, parser):
        parser.add_argument("--alias", "-a", metavar="alias", required=True)
        parser.add_argument(
            "project_name", meavar="project_name", required=True
        )
        parser.add_argument("--config", "-f", metavar="config")
        parser.add_argument("--output", "-o", metavar="output path")

    def handler(self, args):
        return build(
            args.project_name,
            args.output if args.output else args.project_name,
            args.alias,
            args.config
        )