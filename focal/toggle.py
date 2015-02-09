import time
import redis

r = redis.Redis('192.168.122.18')
r.set('tools_cmd', 'start')
r.set('tools_ip_s', '192.168.122.100')
r.set('tools_ip_e', '192.168.122.250')
r.set('tools_nm', '255.255.255.0')
r.set('tools_gw', '192.168.122.1')
r.set('tools_ntp', '192.168.122.18')
r.publish('tools', 'tools_cmd')
time.sleep(10)
r.set('tools_cmd', 'stop')
r.publish('tools', 'tools_cmd')
time.sleep(10)
r.set('tools_cmd', 'end')
r.publish('tools', 'tools_cmd')
time.sleep(2)
r.set('tools_cmd', '')
