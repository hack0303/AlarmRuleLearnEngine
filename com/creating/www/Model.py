#-*- coding: UTF-8 -*-
'''
Created on 2018骞�9鏈�20鏃�

@author: Administrator
'''
class AlarmModel(object):
    '''
    classdocs
    '''

    id=0
    mstrbussinessids=""
    code=0
    occurtime=""
    def __init__(self, params):
        '''
        Constructor
        '''
    def __str__(self):
        return str(self.id)+" "+self.mstrbussinessids+" "+self.code+" "+self.occurtime
    
class ElecModel:
    '''
    classdocs
    '''
    id=0
    electype=""
    elecname=""
    serverids=[]
    clientids=[]
    forwardpath=[]
    reversepath=[]
    is_forward_visited=False
    is_reverse_visited=False

    def __init__(self):
        '''
        Constructor
        '''
    def __str__(self, *args, **kwargs):
        return "id="+str(self.id)+" electype="+self.electype+" serverids="+str(self.serverids)+" clientids"+str(self.clientids)    