from yowsup.structs import ProtocolEntity, ProtocolTreeNode
from .ib import IbProtocolEntity
class EdgeRoutingIbProtocolEntity(IbProtocolEntity):
    '''
    <ib from="s.whatsapp.net">
        <edge_routing>
            <routing_info>
               XXXXXX
            </rounting_info
        </edge_routing>
    </ib>
    '''
    def __init__(self, routing_info):
        super(IbProtocolEntity, self).__init__()
        self.setProps(routing_info)


    def setProps(self, routing_info):
        self.routing_info = routing_info
    
    def toProtocolTreeNode(self):
        node = super(EdgeRoutingIbProtocolEntity, self).toProtocolTreeNode()
        riNode = ProtocolTreeNode("routing_info", {},None, self.routing_info.encode())
        erNode = ProtocolTreeNode("edge_routing",{},[riNode])
        node.addChild(erNode)
        return node
        
    def __str__(self):
        out = super(EdgeRoutingIbProtocolEntity, self).__str__()
        out += "edge_routing: %s\n" % self.routing_info
        return out

    @staticmethod
    def fromProtocolTreeNode(node):
        entity = IbProtocolEntity.fromProtocolTreeNode(node)
        entity.__class__ = EdgeRoutingIbProtocolEntity
        entity.setProps(node.getChild("edge_routing").getChild("routing_info").getData())
        return entity
