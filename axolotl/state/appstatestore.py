# -*- coding: utf-8 -*-

import abc


class AppStateStore(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def addAppStateKeys(self, keys):
        pass

    @abc.abstractmethod
    def getOneAppStateKey(self):
        pass

    @abc.abstractmethod
    def getAppStateKey(self, key_id):
        pass

    @abc.abstractmethod
    def deleteAppStateKey(self,key_id):  
        pass
