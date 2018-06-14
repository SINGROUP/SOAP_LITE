from setuptools import setup, find_packages, Distribution, Extension

ext_list = []
for extname, soname in zip(["src/soapAnalFullPy.c", "src/soapAnalFullCro2Py.c", "src/soapAnalFullCro3Py.c", "src/soapAnalFullCro4Py.c", "src/soapAnalFullCro5Py.c", "src/soapAnalFullCro6Py.c", ], 
    ["lib.libsoapPy","lib.libsoapPy2", "lib.libsoapPy3", "lib.libsoapPy4", "lib.libsoapPy5", "lib.libsoapPy6"]):
    ext_list.append(Extension(soname,
                       [extname],
                       include_dirs=["src"],
                       libraries=["m"],
                       extra_compile_args=["-O3", "-std=c99"]
              ))

extensions = ext_list


if __name__=="__main__":
  setup(name="soaplite",
      url="https://github.com/SINGROUP/SOAPLite",
      version="0.9.11",
      description=("fast lightweight smooth overlap atomic position (SOAP) calculator. see github.com/SINGROUP/SOAPLite for detailed documentations."), author="Eiaki V. Morooka", author_email="eiaki.morooka@aalto.fi",
      packages = find_packages(),
      install_requires =["numpy",
      "scipy",
      "ase"], python_requires='>=2.2, <4', keywords="smooth overlap of atomic positions materials science machine learning soap descriptor fast analytic quantum chemistry local environment materials physics symmetry reduction",
      license="LGPLv3", classifiers=['Topic :: Scientific/Engineering :: Physics', 'Operating System :: POSIX :: Linux' ,'Topic :: Scientific/Engineering :: Chemistry','Topic :: Scientific/Engineering :: Artificial Intelligence','License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)', 'Development Status :: 4 - Beta', 'Intended Audience :: Science/Research','Intended Audience :: Religion', 'Intended Audience :: Education','Intended Audience :: Developers','Programming Language :: Python','Programming Language :: C' ],
      ext_modules=extensions)
      #package_data={
      #  'soaplite':['src/libsoapPy2.so','src/libsoapPy3.so','src/libsoapPy4.so','src/libsoapPy5.so','src/libsoapPy6.so','src/libsoapPy.so']})


