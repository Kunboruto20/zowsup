from yowsup.structs import ProtocolEntity, ProtocolTreeNode
from .iq_groups import GroupsIqProtocolEntity
class SetCommunityGroupsIqProtocolEntity(GroupsIqProtocolEntity):
    '''
    <iq id="998777967160-1735831646-29" to="120363384145081882@g.us" type="set" xmlns="w:g2">
        <links>
            <link link_type="sub_group">
                <group jid="120363386166251465@g.us"/>
            </link>
        </links>
    </iq>
    '''
    def __init__(self, community_jid,group_jids, _id=None):
        super(SetCommunityGroupsIqProtocolEntity, self).__init__(to = community_jid, _id = _id, _type = "set")

        # group_jids 是一个数组
        self.setProps(community_jid,group_jids)

    def setProps(self, community_jid,group_jids):
        self.community_jid = community_jid
        self.group_jids = group_jids

    def __str__(self):
        out = super(SetCommunityGroupsIqProtocolEntity, self).__str__()
        out += "Group JID: %s\n" % self.group_jid
        return out

    def toProtocolTreeNode(self):
        node = super(SetCommunityGroupsIqProtocolEntity, self).toProtocolTreeNode()
        links = ProtocolTreeNode("links",{})
        link = ProtocolTreeNode("link",{"link_type":"sub_group"})

        for jid in self.group_jids:
            group = ProtocolTreeNode("group",{"jid":jid})
            link.addChild(group)
        links.addChild(link)
        node.addChild(links)        
        return node

