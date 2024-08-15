from enum import Enum


class CloudProvider(str, Enum):
    # Amazon Web Services
    aws = "aws"
    # Google Cloud Platform
    gcp = "gcp"
    # Azure
    azr = "azr"
    # Alibaba Cloud
    ali = "ali"
    # Huawei Cloud
    hwa = "hwa"
