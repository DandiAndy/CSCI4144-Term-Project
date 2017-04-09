import resource
import psutil
print resource.RLIMIT_AS
print psutil.virtual_memory().available
