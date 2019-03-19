import unittest
from rocketEngineModels import Engine
from rocketEngineModels import MerlinEngine
from rocketEngineModels import RaptorEngine


class EngineTest(unittest.TestCase):
    """
    Test base Engine class.
    """
    def setUp(self):
        self.engineA = Engine(
            cycle='Gas-generator',
            thrust=914,
            weight=470,
            modelNumber='generic engine'
            )
        self.engineB = Engine(
            cycle='Gas-generator',
            thrust=1145,
            weight=415,
            modelNumber='generic engine 2'
            )

    def test_repr(self):
        self.assertEqual(
            repr(self.engineA),
            "Engine('Gas-generator', 914, 470, 'generic engine')"
            )
        self.assertEqual(
            repr(self.engineB),
            "Engine('Gas-generator', 1145, 415, 'generic engine 2')"
            )

    def test_str(self):
        self.assertEqual(
            str(self.engineA),
            'Engine: generic engine'
            )
        self.assertEqual(
            str(self.engineB),
            'Engine: generic engine 2'
            )


class MerlinEngineTest(unittest.TestCase):
    """
    Test MerlinEngine class.
    """
    def setUp(self):
        self.merlinEngineA = MerlinEngine(
            cycle='Gas-generator',
            thrust=815,
            weight=550,
            modelNumber='generic engine',
            balanceList=[11, 2, 8, 16, 2]
            )

    def test_init(self):
        self.assertEqual(
            self.merlinEngineA.balanceList,
            [2, 2, 8, 11, 16]
            )
        with self.assertRaises(TypeError) as e:
            self.merlinEngineB = MerlinEngine(
                cycle='Gas-generator',
                thrust=815,
                weight=550,
                modelNumber='generic engine',
                balanceList='not a list'
                )

    def test_len(self):
        self.assertEqual(
            len(self.merlinEngineA),
            5
            )


class RaptorEngineTest(unittest.TestCase):
    """
    Test RaptorEngine class.
    """
    def setUp(self):
        self.raptorEngine = RaptorEngine(
            cycle='Gas-generator',
            thrust=815,
            weight=550,
            modelNumber='generic engine',
            actuators=15
            )

    def test_instance(self):
        self.assertTrue(isinstance(self.raptorEngine, Engine))


if __name__ == '__main__':
    unittest.main()
