# coding=UTF-8
import os,sys
sys.path.append(os.getcwd())
from unicodedata import name
from conf.constants import SysVar
from proto import wsend_pb2

from common.utils import Utils

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

import logging
import threading
import time
import json
import shlex

logger = logging.getLogger(__name__)

class InteractiveProcess:

    def __init__(self,bot):                                
        self.bot = bot            

        self.thread = threading.Thread(target=self.runThread)
        self.thread.daemon=True

    def waitLogin(self):
        return self.bot.waitLogin() 

    def runThread(self):
        logger.info("Waiting BOT %s " % self.bot.botId) 

        if self.waitLogin():       
            if self.bot.sendLayer.detect40x:
                logger.info("BOT %s login failed" % self.bot.botId)    
                self.bot.disconnect()                 
            else:
                logger.info("BOT %s ready." % self.bot.botId)      

                time.sleep(1)

                while True:

                    cmd = input("CMD > ")
                    cmd = "CMD "+cmd #
                    params,options = Utils.cmdLineParser(shlex.split(cmd))

                    if len(params)==0:
                        continue

                    if len(params)==1 and params[0]=="exit":
                        self.bot.quit()
                        break

                    if len(params[0].strip())>0:

                        waitTime = 0            

                        if params[0]=="init":                
                            waitTime = 10                            
                        elif params[0]=="mdlink":
                            waitTime = 60
                        else:
                            waitTime = 20

                        if SysVar.CMD_WAIT is not None:                
                            waitTime = SysVar.CMD_WAIT             
                                        
                        cmdId,errMsg = self.bot.callDirect(params[0],params[1:] if  len(params)>1 else [],options)        

                        if errMsg is not None:
                            logger.info("Commmand %s error(execute stage），info=%s" % (params[0],errMsg))      
                        else:                    
                            if cmdId=="JUSTWAIT":                         
                                logger.info("Command complete") 
                            else:
                                result,errMsg = self.bot.getCmdResult(cmdId,waitTime)                    
                                if errMsg is not None:
                                    logger.info("Command %s error (result stage），info=%s" % (params[0],errMsg)) 
                                else:
                                    logger.info("Command %s complete，result=%s" % (params[0],json.dumps(result)))

                                   
                self.bot.disconnect()           

        else:
            logger.info("BOT %s connection timeout" % self.bot.botId)    
            self.bot.disconnect() 
    
    def run(self):       

        self.thread.start()




        

        




        
        
                

