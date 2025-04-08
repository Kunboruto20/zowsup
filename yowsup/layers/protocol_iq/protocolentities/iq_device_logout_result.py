from yowsup.structs import  ProtocolTreeNode
from .iq import IqProtocolEntity
from yowsup.common import YowConstants
from proto import wa_struct_pb2
import time


class DeviceLogoutResultIqProtocolEntity(IqProtocolEntity):

    def __init__(self,_id=None,success=True):
        super(DeviceLogoutResultIqProtocolEntity, self).__init__(_id = _id, _type = "result",to=YowConstants.DOMAIN)
        self.success = success         

    @staticmethod
    def fromProtocolTreeNode(node):
        entity = IqProtocolEntity.fromProtocolTreeNode(node)
        entity.__class__ = DeviceLogoutResultIqProtocolEntity
        resultNode = node.getChild("device_logout")  
        if resultNode is not None:
            entity.success = resultNode.getAttributeValue("success")    
            return entity
        else:
            return None    





        


