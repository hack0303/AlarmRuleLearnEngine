#-*- coding: UTF-8 -*-
'''
Created on 2018骞�9鏈�20鏃�

@author: Administrator
'''
import os
import string
from com.creating.www import Model
from com.creating.www.utils import FileUtil
from com.creating.www.Model import ElecModel
"""
    电路id：1534918656
    电路类型：OCH
    电路名称：广州茂名-λ3-2012广肇云茂湛系统
    服务层电路ID :     1534918657  1534918659  1534918661  1534918674  1534918676  1534918678  1534918680  1534918682  1534918691  1534918693  1534918695  1534918697  1534918699  1534918722  1534918724  
    客户层电路ID :     1534922578  
    工作路径1：
    正向路由 ：
    NEId:13172737--BoardId:19726605--PortName:PTP-PO=1/OCH=1--------->NEId:13172737--BoardId:19726370--PortName:PTP-PO=2/OCH=1--------->NEId:13172737--BoardId:19726370--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172737--BoardId:19726360--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172737--BoardId:19726360--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172739--BoardId:19726395--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172739--BoardId:19726395--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172739--BoardId:19726402--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172739--BoardId:19726402--PortName:PTP-PO=2/OCH=1--------->NEId:13172740--BoardId:19726428--PortName:PTP-PO=2/OCH=1--------->NEId:13172740--BoardId:19726428--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172740--BoardId:19726415--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172740--BoardId:19726415--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172741--BoardId:19726433--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172741--BoardId:19726433--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172741--BoardId:19726442--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172741--BoardId:19726442--PortName:PTP-PO=2/OCH=1--------->NEId:13172742--BoardId:19726466--PortName:PTP-PO=2/OCH=1--------->NEId:13172742--BoardId:19726466--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172742--BoardId:19726454--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172742--BoardId:19726454--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172747--BoardId:19726518--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172747--BoardId:19726518--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172747--BoardId:19726529--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172747--BoardId:19726529--PortName:PTP-PO=2/OCH=1--------->NEId:13172747--BoardId:19726631--PortName:PTP-PO=1/OCH=1--------->
    反向路由 ：
    NEId:13172747--BoardId:19726631--PortName:PTP-PO=1/OCH=1--------->NEId:13172747--BoardId:19726528--PortName:PTP-PO=2/OCH=1--------->NEId:13172747--BoardId:19726528--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172747--BoardId:19726518--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172747--BoardId:19726518--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172742--BoardId:19726454--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172742--BoardId:19726454--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172742--BoardId:19726467--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172742--BoardId:19726467--PortName:PTP-PO=2/OCH=1--------->NEId:13172741--BoardId:19726628--PortName:PTP-PO=2/OCH=1--------->NEId:13172741--BoardId:19726628--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172741--BoardId:19726433--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172741--BoardId:19726433--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172740--BoardId:19726415--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172740--BoardId:19726415--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172740--BoardId:19726429--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172740--BoardId:19726429--PortName:PTP-PO=2/OCH=1--------->NEId:13172739--BoardId:19726627--PortName:PTP-PO=2/OCH=1--------->NEId:13172739--BoardId:19726627--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172739--BoardId:19726395--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172739--BoardId:19726395--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172737--BoardId:19726360--PortName:PTP-PO=3/OTS=1/OMS=1/OCH=50--------->NEId:13172737--BoardId:19726360--PortName:PTP-PO=2/OTS=1/OMS=1/OCH=2--------->NEId:13172737--BoardId:19726371--PortName:PTP-PO=49/OTS=1/OMS=1/OCH=2--------->NEId:13172737--BoardId:19726371--PortName:PTP-PO=2/OCH=1--------->NEId:13172737--BoardId:19726605--PortName:PTP-PO=1/OCH=1--------->

Info    2018-05-31 17:36:38 ------------------------------------------
    电路id：1534932656  (保护电路id：1534932658  )
    电路类型：ODUK
    电路名称：12-14-韶关沙湖.S02.Port-1/ODU1-1<-->15-20-广州电信大厦.S1D.Port-2/ODU1-1-1534932656
    服务层电路ID :     1534927483  1534927485  
    客户层电路ID :     1534932655  
    工作路径1：
    正向路由 ：
    NEId:13172864--BoardId:19729969--PortName:FTP-ODU1=1/ODU1=1--------->NEId:13172864--BoardId:19729960--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172864--BoardId:19729960--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731841--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731841--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731842--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731842--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172908--BoardId:19730766--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172908--BoardId:19730766--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172908--BoardId:19730785--PortName:FTP-ODU1=2/ODU1=1--------->
    反向路由 ：
    NEId:13172908--BoardId:19730785--PortName:FTP-ODU1=2/ODU1=1--------->NEId:13172908--BoardId:19730766--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172908--BoardId:19730766--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731842--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731842--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731841--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731841--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172864--BoardId:19729960--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172864--BoardId:19729960--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172864--BoardId:19729969--PortName:FTP-ODU1=1/ODU1=1--------->
    保护路径1：
    正向路由 ：
    NEId:13172864--BoardId:19729961--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172864--BoardId:19729961--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172863--BoardId:19730050--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172863--BoardId:19730050--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172863--BoardId:19730049--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172863--BoardId:19730049--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731840--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731840--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731830--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731830--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172908--BoardId:19730767--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172908--BoardId:19730767--PortName:FTP-ODU2=1/ODU1=1--------->
    反向路由 ：
    NEId:13172908--BoardId:19730767--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172908--BoardId:19730767--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731830--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731830--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731840--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172978--BoardId:19731840--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172863--BoardId:19730049--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172863--BoardId:19730049--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172863--BoardId:19730050--PortName:FTP-ODU2=1/ODU1=1--------->NEId:13172863--BoardId:19730050--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172864--BoardId:19729961--PortName:PTP-PO=1/OCH=1/ODU2=1/ODU1=1--------->NEId:13172864--BoardId:19729961--PortName:FTP-ODU2=1/ODU1=1--------->
"""
elecs={}
p2w_mapping={}
_p_elecs={}
pattern001="电路id："
pattern002="(保护电路id："
SPLIT001="："
SPLIT002=")"
"""
fileparser=FileUtil()
"""
if __name__ == '__main__':

    document=open("../../../doc/busiaccess.2017-12-11.log","r+")
    context=document.read()
    document.close()
    'print(context)'
    lines=context.splitlines();
    print(len(lines))
    _elec=None
    _protected_elec=None
    for i in range(0,len(lines)):   
        if(lines[i].find("-------------------------------------")!=-1 or lines[i].find("Info")!=-1):
            _elec=ElecModel()
            _protected_elec=ElecModel()
        elif(lines[i].find(pattern001)!=-1):
            if(lines[i].find(pattern002)==-1):
                '''print(lines[i].lstrip('\t').split(SPLIT001,2))'''
                _elec.id=int(lines[i].split(SPLIT001,2)[1])
                elecs.setdefault(_elec.id, _elec)
                '''print(_elec.id)'''
            else:
                parts=lines[i].split(pattern002)
                w=int(parts[0].split(pattern001)[1].rstrip());
                '''print(parts[1])'''
                p=int(parts[1].split(SPLIT002)[0].rstrip().lstrip())
                _elec.id=w
                _protected_elec.id=p
                p2w_mapping.setdefault(p, w)
                elecs.setdefault(w, _elec)
                _p_elecs.setdefault(p,_protected_elec)
                print("%d:%d" % (_elec.id,_protected_elec.id))
    '''print(str(elecs))'''
    pass