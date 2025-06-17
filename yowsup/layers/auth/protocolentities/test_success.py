from ....layers.auth.protocolentities.success import SuccessProtocolEntity
from ....structs import ProtocolTreeNode
from ....structs.protocolentity import ProtocolEntityTest
import unittest


class SuccessProtocolEntityTest(ProtocolEntityTest, unittest.TestCase):
    def setUp(self):
        self.ProtocolEntity = SuccessProtocolEntity
        attribs = {
            "creation": "1234",
            "location": "atn",
            "props": "2",
            "t": "1415470561"
        }
        self.node = ProtocolTreeNode("success", attribs)
