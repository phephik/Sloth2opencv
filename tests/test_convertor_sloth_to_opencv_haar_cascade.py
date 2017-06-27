#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `convertor_sloth_to_opencv_haar_cascade` package."""


import unittest
from click.testing import CliRunner

from convertor_sloth_to_opencv_haar_cascade import convertor_sloth_to_opencv_haar_cascade
from convertor_sloth_to_opencv_haar_cascade import cli


class TestConvertor_sloth_to_opencv_haar_cascade(unittest.TestCase):
    """Tests for `convertor_sloth_to_opencv_haar_cascade` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'convertor_sloth_to_opencv_haar_cascade.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
