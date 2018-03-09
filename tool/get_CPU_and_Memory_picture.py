#author csp
#develop this code by python3
import psutil
import time
from pylab import plt
import os
import json


class get_performan:
    def __init__(self, process_name, test_time, cpu_interval):
        self.test_time = test_time
        self.process_name = process_name
        self.cpu_interval = cpu_interval
        self.file_cpu = str(time.ctime().replace(":", "_").replace(" ", "_"))+"cpu.log"
        self.file_memory = str(time.ctime().replace(":", "_").replace(" ", "_"))+"memory.log"

    # get pid of test process
    def run(self):
        all_pid = psutil.pids()#get all process pid
        with open(self.file_cpu, "w+") as f_cpu:
            with open(self.file_memory,"w+") as f_memory:
                for pid in all_pid:
                    try:
                            pid_name = psutil.Process(pid)  ###get all pid and name
                            if pid_name.name() == self.process_name:
                                t = 0
                                while t < (self.test_time * 60 * 60):  # calculate second
                                    data_cpu = pid_name.cpu_percent(1)
                                    print( pid_name.memory_info())
                                    rss= pid_name.memory_info()[0]
                                    print(rss)
                                    data_memory = round(rss/1024/1024/1024, 4)##M
                                    print("%s times cpu %s memory %sM" % (t + 1, data_cpu, data_memory))
                                    f_cpu.write(str(data_cpu) + "\n")
                                    f_memory.write(str(data_memory) + "\n")
                                    time.sleep(self.cpu_interval)  # cpu_interval(second)
                                    t += 1
                            else:
                                print("%s is not my test process " % pid_name.name())
                    except:
                        print("psutil.NoSuchProcess: psutil.NoSuchProcess no process found with pid %s" % pid)
            f_memory.close()
        f_cpu.close()



    def get_picture(self):
        with open(self.file_cpu, "r") as f_cpu:
            with open(self.file_memory, "r") as f_memory:
                cpu_data = f_cpu.read().split("\n")
                cpu_data.remove(cpu_data[-1])
                memory_data = f_memory.read().split("\n")
                memory_data.remove(memory_data[-1])
                m_d = []
                c_d = []
                for n, s in enumerate(cpu_data):
                    c_d = c_d + [float(s)]
                for k, v in enumerate(memory_data):
                    m_d = m_d + [float(v)]
                #return cpu_data
                x = range(len(c_d))
                y = c_d
                y1 = m_d
                plt.plot(x, y,  label='CPU', linewidth=3, color='r', marker='o',markerfacecolor='blue', markersize=6)
                plt.plot(x, y1,  label='memory', linewidth=3, color='r', marker='o',markerfacecolor='blue', markersize=6)
                #plt.legend()
                plt.xticks(x, rotation=10000)
                plt.margins(0)
                plt.subplots_adjust(bottom=0.10)
                plt.xlabel(u"time", fontsize = 15, color = 'green')  # X轴标签
                plt.ylabel(u"CPU", fontsize =15)  # Y轴标签
                plt.title("CPU graph")  # 标题
                plt.show()
        f_cpu.close()

    def load_json(self):
        with open ("config.json") as f_json:
            config_json = json.load(f_json)
            print(config_json)
            self.process_name = config_json["process_name"]
            self.cpu_interval = config_json["cpu_interval"]
            self.test_time = config_json["test_time"]
            return self.process_name, self.cpu_interval, self.test_time

    def json_exist(self):
        if os.path.exists("config.json") is True:
            self.load_json()
        else:
            print("file config_json is  not exist and create a config.json")
            with open("config.json", "w+") as config_f:
                content = {"process_name": self.process_name, "test_time": self.test_time, "cpu_interval": self.cpu_interval}
                json_default_content = json.dumps(content, sort_keys=True, indent=4, separators=(',', ': '))
                config_f.write(json_default_content)
                config_f.close()
                print("json has created success and run the script again")

if __name__ == "__main__":
    # {"process_name": "taskmgr.exe", "test_time": 0.1, "cpu_interval": 0}
    p = get_performan(process_name="taskmgr.exe", test_time=0.0025, cpu_interval=0)
    # if json is not exist, it will input the parameter and create a file
    p.json_exist()
    p.run()
    p.get_picture()
