import pytest
from data_classes import Config

@pytest.fixture
def base_config():
    return Config(frequency_hz = 5.1e9, amplitude = 0.5)

class TestConfigDefaults:
    """Config initializes correctly with default values"""

    def test_default_duration_ns(self, base_config):
        assert base_config.duration_ns == 20

    def test_default_backend(self, base_config):
        assert base_config.backend == "ibm_kyoto"

    def test_default_tags_is_empty_list(self, base_config):
        assert base_config.tags == []
    
    def test_default_tags_are_not_shared(self, base_config):
        """Verify field(default_factory=list) creates a new empty list for each instance"""
        c1 = base_config
        c2 = base_config
        c1.tags.append("x")
        assert c2.tags == []