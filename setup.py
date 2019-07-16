import setuptools

with open('README.md') as f:
	ld = f.read()

setuptools.setup(
	name="rubypass",
	version="0.1.6",
	description="A package to extract video urls from 2 russian websites",
	long_description=ld,
	long_description_content_type="text/markdown",
	author="okawo",
	author_email="okawo.198@gmail.com",
	url="https://github.com/okawo80085/russianWebBypass",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],

	py_modules=['rubypass'],
)
