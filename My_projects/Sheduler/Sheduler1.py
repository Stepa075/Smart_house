from datetime import datetime

from pyriodic import DurationJob
from pyriodic import DatetimeJob
from pyriodic import Scheduler

now = datetime.now
s = Scheduler()

start = now()

def func1(arg1=None, arg2=None, arg3=None, arg4=None):
    print('Func1', arg1, arg2, arg3, arg4, now() - start, now())

def func2():
    print('Func2', now() - start, now())

def func3():
    print('Func3', now() - start, now())

s.add_job(DurationJob(func1,
                    when='30m',
                    args=('This', 'is'),
                    kwargs={'arg3': 'the', 'arg4': 'first function'},
                    name='MyJob'))
s.add_job(DurationJob(func2, when='2h'))
s.add_job(DatetimeJob(func3, when='12:00 pm'))

print(s.next_run_times())