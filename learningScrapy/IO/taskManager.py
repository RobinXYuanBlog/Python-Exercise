import random, time, queue
from multiprocessing.managers import BaseManager

# 第一步：建立task_queue和result_queue，存放任务和结果
task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

# 第二步：将创建的两个队列注册在网络上，利用regster方法，callable参数关联了Queue对象
# 将Queue对象在网络中暴露
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue', callable=lambda:result_queue)

# 第三步：绑定端口8001，设置验证口令'qiye'。相当于对象初始化
manager = QueueManager(address=('', 8001), authkey='qiye')

# 第四步：启动管理，监听信息通道
manager.start()

# 第五步：通过管理实例的方法获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 第六步：添加任务
for url in ["ImageUrl_" + i for i in range(10)]:
    print("Put task %s ..." % url)
    task.put(url)

# 获取返回结果
print("Try to get result...")
for i in range(10):
    print("result is %s" % result.get(timeout=10))
# 关闭管理
manager.shutdown()