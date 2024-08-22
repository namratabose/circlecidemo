import xml.etree.ElementTree as ET
import subprocess
import os


def get_browsers_from_xml(xml_file):
    """Read browser types from XML file."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    browsers = [browser.text for browser in root.findall('browser')]
    return browsers


def run_robot_tests(browsers):
    """Run Robot Framework tests for each browser."""
    for browser in browsers:
        command = [
            'pabot',
            '--processes', '3',  # Number of parallel processes
            '--variable', f'BROWSER:{browser}',  # Set the BROWSER variable
            'test_suite.robot'
        ]
        print(f"Running tests with browser: {browser}")
        subprocess.run(command, check=True)


if __name__ == "__main__":
    xml_file = 'browsers.xml'
    if not os.path.exists(xml_file):
        raise FileNotFoundError(f"XML file '{xml_file}' not found.")

    browsers = get_browsers_from_xml(xml_file)
    run_robot_tests(browsers)
