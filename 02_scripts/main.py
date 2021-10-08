# Do-File: 00_main.py
# Purpose: Main file to define general settings and
#          to run python-files
# Author:
# First version:
# Current version:

# OVERVIEW
#   This script generates tables and figures for the paper:
#       <PROJECT> <AUTHOR>

#   All raw data are stored in /01_data/01_orig
#   All tables are outputted to /03_results/02_tables
#   All figures are outputted to /03_results/03_figures

# SOFTWARE REQUIREMENTS
#   Analyses run on ... using Python version ... and ....

# TO PERFORM A CLEAN RUN, DELETE THE FOLLOWING TWO FOLDERS:
#   /03_processed
#   /04_results
#   ...
# Or use the clean.bat Batch script

# Ideally the project should run when clone to some other location
# outside X:\Dataroom

# Import libraries
import os
import logging
import platform
from pathlib import Path

# Import scripts to execute
import settings
import process_raw_data
import clean_data
import regressions
import make_tables_figures


def mkdir(config, dir):
    """Helper function that checks if the directory exists and creates
    one if necessary"""

    # Create path
    complete_path = os.path.join(config["project_dir"], dir)
    Path(complete_path).mkdir(parents=True, exist_ok=True)
    # Create .gitkeep empty file
    with open(os.path.join(complete_path, '.gitkeep'), 'w') as fp:
        pass


def create_directories(config):
    """Here all the other directories are created if they do not exist"""
    mkdir(config, os.path.join(config['data_dir'], '01_orig'))
    mkdir(config, os.path.join(config['data_dir'], '02_external'))
    mkdir(config, os.path.join(config['data_dir'], '03_intermediate'))
    mkdir(config, os.path.join(config['data_dir'], '04_final'))

    mkdir(config, os.path.join(config['publ_dir']))
    # log file has been created
    mkdir(config, os.path.join(config['results_dir'], '02_tables'))
    mkdir(config, os.path.join(config['results_dir'], '03_figures'))


def check_initial_directories(config):
    """Do the intital check for directories so we can start the log file"""

    # Confirm that the for the project root directory has been defined
    if 'project_dir' in config.keys():
        if not os.path.isdir(config["project_dir"]):
            print(
                f"ERROR: Project directory does not exist: \
                    {config['project_dir']}")
            exit()
    else:
        print('`project_dir` not in config file')
        exit()

    # create logging directory
    if 'results_dir' in config.keys():
        Path(os.path.join(config["project_dir"],
                          config["results_dir"],
                          '01_log')).mkdir(parents=True,
                                           exist_ok=True)


def start_logfile(config):
    log_file = os.path.join(
        config["project_dir"], config["results_dir"], '01_log', 'dataroom.log')
    logging.basicConfig(filename=log_file,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO, filemode="w")
    logging.info('Started')


def show_stats():
    """Show statistics of the environment"""
    logging.info("Python version: " + platform.python_version())
    logging.info("Machine Type:   " + platform.machine())
    logging.info("Architecture:   " + platform.architecture()[0])
    logging.info("Processor:      " + platform.processor())
    logging.info("OS:             " + platform.system())
    logging.info("Node:           " + platform.node())


def run_scripts():
    """Execute all the scripts"""
    process_raw_data.main()
    clean_data.main()
    regressions.main()
    make_tables_figures.main()


def main():
    # load config file
    # make sure config.json is the only location with hard-coded paths.
    # Don't put hard-coded paths in the code
    config = settings.config
    check_initial_directories(config)

    start_logfile(config)
    create_directories(config)
    show_stats()
    run_scripts()

    logging.info('Finished')


if __name__ == '__main__':
    main()
