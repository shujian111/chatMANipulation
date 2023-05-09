import frrpc
import time

# 与机器人控制器建立连接，连接成功返回一个机器人对象
robot = frrpc.RPC('192.168.58.2')

P1=[75.414,568.526,338.135,-178.348,-0.930,52.611]
P2=[-273.856,643.260,259.235,-177.972,-1.494,80.866]
P3=[-423.044,229.703,241.080,-173.990,-5.772,123.971]
robot.MoveCart(P1,0,0,100.0,100.0,100.0,-1.0,-1)       #笛卡尔空间点到点运动
robot.MoveCart(P2,0,0,100.0,100.0,100.0,-1.0,-1)
robot.MoveCart(P3,0,0,100.0,100.0,100.0,0.0,-1)
time.sleep(1)
robot.StopMotion()    #停止运动