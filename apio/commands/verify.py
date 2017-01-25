# -*- coding: utf-8 -*-
# -- This file is part of the Apio project
# -- (C) 2016 FPGAwars
# -- Author Jesús Arroyo
# -- Licence GPLv2

import click

from apio.managers.scons import SCons

# Python3 compat
try:
    unicode = str
except NameError:  # pragma: no cover
    pass


@click.command('verify')
@click.pass_context
@click.option('-p', '--project-dir', type=unicode, metavar='path',
              help='Set the target directory for the project.')
def cli(ctx, project_dir):
    """Verify the verilog code."""
    exit_code = SCons(project_dir).verify()
    ctx.exit(exit_code)
