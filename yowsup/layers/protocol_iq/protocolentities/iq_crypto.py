from .iq import IqProtocolEntity
from ....structs import ProtocolTreeNode
import codecs
class CryptoIqProtocolEntity(IqProtocolEntity):
    def __init__(self):
        super(CryptoIqProtocolEntity, self).__init__("urn:xmpp:whatsapp:account", _type="get")

    def toProtocolTreeNode(self):
        node = super(CryptoIqProtocolEntity, self).toProtocolTreeNode()
        cryptoNode = ProtocolTreeNode("crypto", {"action": "create"})
        googleNode = ProtocolTreeNode("google", data = codecs.decode("fe5cf90c511fb899781bbed754577098e460d048312c8b36c11c91ca4b49ca34", 'hex'))
        cryptoNode.addChild(googleNode)
        node.addChild(cryptoNode)
        return node