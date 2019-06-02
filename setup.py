from setuptools import setup
def _read(file):
    with open(file, 'rb') as fp:
        return fp.read()

setup(name='geyser',
      version='0.1.0.dev1',
      description='geyser',
      long_description=_read('README.md').decode('utf-8'),
      long_description_content_type='text/markdown',
      author='Zhihan Yue',
      author_email='zhihan.yue@foxmail.com',
      url='https://github.com/yuezhihan/geyser',
      license='MIT',
      python_requires=">=2.7",
      install_requires=["torch"],
      packages=["geyser"],
      zip_safe=False)
