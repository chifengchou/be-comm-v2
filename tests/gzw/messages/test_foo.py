from datetime import datetime

from gzw.constants.cloud_providers import CloudProvider
from gzw.messages.foo import Foo


def test_foo():
    foo = Foo(
        provider=CloudProvider.aws,
        timestamp=datetime.utcnow(),
    )
    assert foo

