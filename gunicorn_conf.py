from multiprocessing import cpu_count

# Socket Path
bind = 'unix:/home/admin/projectDir/mlapi/fastapi.sock'

# Worker Options
workers = cpu_count() + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Logging Options
loglevel = 'debug'
accesslog = '/home/admin/projectDir/mlapi/access_log'
errorlog =  '/home/admin/projectDir/mlapi/error_log'

