#!/usr/bin/python2.7

import stack
import config

### Check method for push function.
def check_push_method(s):
    s.push('A')
    config.log_example.debug('push A into the stack')
    s.push('B')
    config.log_example.debug('push B into the stack')
    s.push('C')
    config.log_example.debug('push C into the stack')
    s.push('D')
    config.log_example.debug('push D into the stack')
    s.isFull()
    s.print_all()

### Check method for pop function.
def check_pop_method(s):
    config.log_example.debug('Start pop method')
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    config.log_example.debug('Stack should be empty')
    s.isEmpty()
    s.print_all()
    config.log_example.debug('End pop method')

### Main function.
def main():
    s=stack.Stack()
    s.size = 3
    check_push_method(s)
    check_pop_method(s)

main()

