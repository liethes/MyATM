# 工具类: Logger
class Logger:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

	@staticmethod
	def info(info):
		print(Logger.OKBLUE + info + Logger.ENDC)

	@staticmethod
	def high(info):
		print(Logger.OKGREEN + info + Logger.ENDC)

	@staticmethod
	def fail(info):
		print(Logger.FAIL + info + Logger.ENDC)



# END
