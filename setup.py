# from distutils.core import setup
# from Cython.Build import cythonize
#
# setup(
# ext_modules=cythonize("mod_zh.py") # 替换为你的Python文件名
# )
import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="vcpccm",
  version="beta 0.0.1",
  author="missdeep",
  author_email="vercore@163.com",
  description="基于python所写的闭源中文编程模块",
  long_description=long_description,
  long_description_content_type="/README.md",
  url="https://github.com/missdeep/vcppcm",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)