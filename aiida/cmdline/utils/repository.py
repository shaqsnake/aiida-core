# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida-core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
"""Utility functions for command line commands operating on the repository."""

import click


def list_repository_contents(node, path, color):
    """Print the contents of the directory `path` in the repository of the given node to stdout.

    :param node: the node
    :param path: directory path
    :raises FileNotFoundError: if the `path` does not exist in the repository of the given node
    """
    from aiida.orm.utils.repository import FileType

    for entry in node.list_objects(path):
        bold = bool(entry.type == FileType.DIRECTORY)

        if color:
            click.secho(entry.name, bold=bold, fg='blue')
        else:
            click.secho(entry.name, bold=bold)
