from pylab import plt



def get_cpu():
    with open("cpu.log", "r") as f:
        cpu_data = f.read().split("\n")
        #return cpu_data
        x = range(len(cpu_data))
        y = cpu_data
        plt.plot(x, y, marker='*', mec='b', mfc='w', label=u'y=cpu graph')
        plt.legend()
        plt.xticks( x, rotation=10000)
        plt.margins(0)
        plt.subplots_adjust(bottom=0.10)
        plt.xlabel(u"time")  # X轴标签
        plt.ylabel("CPU")  # Y轴标签
        plt.title("CPU graph")  # 标题
        plt.show()




if __name__ == "__main__":
    get_cpu()


