import base64
import xml.etree.ElementTree as et

def savePng(code, name, path = None):
	#default path: temp folder
	if path is None:
		path = ''
	else:
		path = path + '/'
	#decode base64 png file
	f = open(name + '.png', 'wb')
	f.write(base64.b64decode(code))
	f.close()
	return

def getName(tempRoot, tempName, path = None):
	#traverse the element tree
	for child in tempRoot:
		if child.tag == 'dir':
			#recurrently getName
			if 'name' not in child.attrib:
				print('E: no name! ' + tempName)
				continue
			else:
				getName(child, tempName + '.' + child.attrib['name'])
		elif child.tag == 'png':
			#name = path from root
			if 'name' not in child.attrib:
				print('E: no name! ' + tempName)
				continue
			elif 'value' not in child.attrib:
				print('E: no value! ' + tempName)
				continue
			else:
				savePng(child.attrib['value'], tempName + '.' + child.attrib['name'], path)
		else:
			print('W: wrong tag? ' + child.tag)
	return

def getPng(file, path = None):
	tree = et.parse(file)
	root = tree.getroot()

	#validate root
	if root.tag == 'dir':
		if 'name' not in root.attrib:
			print('E: no name!')
			return
		else:
			getName(root, root.attrib['name'], path)
	else:
		print('W: wrong tag? ' + root.tag)
	return

if __name__ == '__main__':
	getPng('test.img.xml')