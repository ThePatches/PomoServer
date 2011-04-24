"""Actions for the pomo server client."""

import optparse

import pom_msg


def start(options):
    usage = 'pom start'
    parser = optparse.OptionParser(usage=usage)
    (options, args) = parser.parse_args(options)
    raise Exception('Not implemented.')

def stop(options):
    usage = 'pom stop'
    parser = optparse.OptionParser(usage=usage)
    (options, args) = parser.parse_args(options)
    pom_msg.sendMessage(pom_msg.KILL)

def suspend(options):
    usage = 'pom suspend [options]'
    parser = optparse.OptionParser(usage=usage)
    parser.add_option('-t', '--time', 
        dest='suspend_time',
        help='Time, in seconds, to suspend for. Optional.')
    (options, args) = parser.parse_args(options)
    if options.time:
        raise Exception('Not implemented.')
    pom_msg.sendMessage(pom_msg.SUSPEND)

def resume(options):
    usage = 'pom resume'
    parser = optparse.OptionParser(usage=usage)
    (options, args) = parser.parse_args(options)
    pom_msg.sendMessage(pom_msg.RESUME)

def done(options):
    usage = 'pom done'
    parser = optparse.OptionParser(usage=usage)
    (options, args) = parser.parse_args(options)
    pom_msg.sendMessage(pom_msg.DONE)
    raise Exception('Not implemented.')

def repeat(options):
    usage = 'pom repeat [options]'
    parser = optparse.OptionParser(usage=usage)
    (options, args) = parser.parse_args(options)
    parser.add_option('-n', '--number', 
        dest='num',
        help='Number of times to repeat.')
    (options, args) = parser.parse_args(options)
    raise Exception('Not implemented.')

def postpone(options):
    usage = 'pom postpone'
    parser = optparse.OptionParser(usage=usage)
    (options, args) = parser.parse_args(options)
    raise Exception('Not implemented.')


POM_ACTIONS = {
    'start': start,
    'stop': stop,
    'suspend': suspend,
    'resume': resume,
    'done': done,
    'repeat': repeat,
    'postpone': postpone,
    }
