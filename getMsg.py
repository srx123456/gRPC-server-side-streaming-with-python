import psutil
import time

def get_network_usage():
    # 获取网络接口的数据包统计信息
    net_io_before = psutil.net_io_counters()

    # 等待一段时间
    time.sleep(1)

    # 再次获取网络接口的数据包统计信息
    net_io_after = psutil.net_io_counters()

    # 计算这段时间内的网络带宽使用情况
    sent_bytes = net_io_after.bytes_sent - net_io_before.bytes_sent
    recv_bytes = net_io_after.bytes_recv - net_io_before.bytes_recv

    return sent_bytes, recv_bytes

if __name__ == '__main__':
    # 获取CPU使用率
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f'CPU usage: {cpu_percent}%')

    # 获取内存使用率
    mem_info = psutil.virtual_memory()
    mem_percent = mem_info.percent
    print(f'Memory usage: {mem_percent}%')

    sent_bytes, recv_bytes = get_network_usage()
    print(f'Sent: {sent_bytes} bytes, Received: {recv_bytes} bytes')

    # 对于归一化，由于这里获取的已经是百分比，所以已经处于0-100的范围内，可以直接除以100进行归一化
    cpu_percent_normalized = cpu_percent / 100
    mem_percent_normalized = mem_percent / 100
    print(f'Normalized CPU usage: {cpu_percent_normalized}')
    print(f'Normalized Memory usage: {mem_percent_normalized}')

    # 对于归一化，由于网络带宽没有固定的最大值，通常我们会使用某个参考值作为最大值，例如你的网络接口的理论最大带宽
    # 这里假设最大带宽是100Mb/s，即12500000字节/秒
    max_bandwidth = 12500000
    sent_normalized = sent_bytes / max_bandwidth
    recv_normalized = recv_bytes / max_bandwidth
    print(f'Normalized Sent: {sent_normalized}, Normalized Received: {recv_normalized}')
