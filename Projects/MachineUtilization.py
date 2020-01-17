from __future__ import print_function
import psutil
import os
import multiprocessing, os, re, sys, time

cgroup_dir = 'C:\\'
node_rgx = u'[a-z]*[0-9]{2}'
interval = 1

def main():
  cpus = multiprocessing.cpu_count()
  startval = get_values()
  time.sleep(interval)
  endval = get_values()
  for key, value in startval.iteritems():
    if key in endval:
      delta = int(endval[key]) - int(startval[key])
      dpns = float(delta / interval)
      dps = dpns / 1000000000
      percent = dps / cpus
      print(key + ':' + '{percent:.2%}'.format(percent=percent))


def get_values():
  values = {}
  if os.path.exists('%s/cpuacct.usage' % cgroup_dir):
    with open('%s/cpuacct.usage' % cgroup_dir, 'rb') as tobj:
      values['total'] = tobj.read()
  else:
    sys.exit(1)
  for fd in os.listdir(cgroup_dir):
    if os.path.isdir('%s/%s' % (cgroup_dir, fd)) and re.match(node_rgx, fd):
      acctf = '%s/%s/cpuacct.usage' % (cgroup_dir, fd)
      if os.path.isfile(acctf):
        with open(acctf, 'rb') as accto:
          values[fd] = accto.read()
  return values


if __name__ == "__main__":
  main()

'''
#To get psutil current version
print(psutil.__version__)


#To get some memory and CPU stats
print(psutil.cpu_percent())

#Physical memory usage
print(psutil.virtual_memory())

#process id
pid=os.getpid()

py=psutil.Process(pid)
#Memory use in GB
memoryUse=py.memory_info()[0]/2**30

print("Memory Use:",memoryUse)


'''
