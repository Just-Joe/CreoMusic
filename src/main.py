import time
import subprocess
import logging

# Initialise global logging
logpath = 'logs/CreoMusic.log'
log = None

def logger_init():
	"""
		Sets up logging process
	"""

	logger = logging.getLogger('creologger')
	logger.setLevel(logging.DEBUG)	
	subprocess.call(['rm', logpath])
	fh = logging.FileHandler(logpath)
	form = logging.Formatter('%(asctime)s | %(message)s')
	fh.setLevel(logging.DEBUG)
	fh.setFormatter(form)
	logger.addHandler(fh)
	global log
	log = logger
	logger.info('Logger started.')

def main():
	"""
		Dispatched initialization procedures and launches the backend and interface
	"""
	logger_init()
	log.critical('Starting CreoMusic!')
	log.critical('Exiting CreoMusic!')
	
if __name__ == "__main__":

	main()

