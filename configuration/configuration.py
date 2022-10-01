# Import the libraries
import yaml


def configuration() -> yaml:
    # Read the yaml file
    with open(r"configuration\configuration.yaml","r") as f:
        # load the info
        conf: yaml = yaml.safe_load(f)
        return conf

