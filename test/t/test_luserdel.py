import pytest


class TestLuserdel:
    @pytest.mark.complete("luserdel ")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("luserdel -")
    def test_2(self, completion):
        assert completion