from pydantic import BaseModel, NaiveDatetime

from gzw.constants.cloud_providers import CloudProvider


class Foo(BaseModel):
    provider: CloudProvider
    timestamp: NaiveDatetime