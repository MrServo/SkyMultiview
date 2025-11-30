from setuptools import setup
import setup_translate

pkg = 'Extensions.SkyMultiview'
setup(name='enigma2-plugin-extensions-skymultiview',
       version='1.0',
       description='SkyMultiview for E2',
       package_dir={pkg: 'SkyMultiview'},
       packages=[pkg],
       package_data={pkg: ['pics/HD/*.png', 'pics/FHD/*.png', '*.png', '*.cfg']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
