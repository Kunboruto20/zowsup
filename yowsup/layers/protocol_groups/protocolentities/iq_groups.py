from ....structs import ProtocolEntity, ProtocolTreeNode
from ....layers.protocol_iq.protocolentities import IqProtocolEntity
class GroupsIqProtocolEntity(IqProtocolEntity):
    '''
    <iq type="{{get | set?}}" id="{{id}}" xmlns="w:g2", to="{{group_jid}}">
    </iq>
    '''
    def __init__(self, to = None, _from  = None, _id = None, _type = None,xmlns="w:g2"):
        super(GroupsIqProtocolEntity, self).__init__(xmlns, _id, _type, to = to, _from = _from)
