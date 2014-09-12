from distutils.core import setup
setup(name='pygame-ledpixels',
      version='0.1',
      packages=['led'],
      requires=['pyserial>=2.6', 'pygame>=1.9.1']
      )