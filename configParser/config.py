import ConfigParser
import ast

class Config(object):
	"""docstring for Config, must have section_name and attribute"""
	def __init__(self, config_file):
		self.conf = ConfigParser.RawConfigParser()
		self.conf.read(config_file)

	def get(self, section_name, attribute_name):
		return self.conf.get(section_name, attribute_name)

	def get_eval(self, section_name, attribute_name):
		return ast.literal_eval(self.conf.get(section_name, attribute_name))


if __name__ == '__main__':
	conf = Config('example.cfg')

	print conf.get_eval('section1', 'var1')
	print conf.get_eval('section2', 'list1')
	print conf.get_eval('section3', 'dict1')