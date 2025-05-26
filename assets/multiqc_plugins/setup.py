#!/usr/bin/env python
"""
Setup code for Aladdin Viralrecon pipeline MultiQC plugin.
For more information about MultiQC, see http://multiqc.info
"""

from setuptools import setup, find_packages

version = '0.3.0'

setup(
    name = 'multiqc_aladdin_viralrecon',
    version = version,
    description = "MultiQC plugins for viralrecon pipeline",
    packages = find_packages(),
    include_package_data = True,
    install_requires = ['multiqc==1.17'],
    entry_points = {
        'multiqc.templates.v1': [
            'aladdin = multiqc_aladdin_viralrecon.templates.aladdin'
        ],
        'multiqc.modules.v1': [
            'FASTQC = multiqc_aladdin_viralrecon.modules.FASTQC:MultiqcModule',
        ],
        'multiqc.hooks.v1': [
            'before_config = multiqc_aladdin_viralrecon.custom_code:plugin_before_config',
            'execution_start = multiqc_aladdin_viralrecon.custom_code:plugin_execution_start'
        ]
    }
)