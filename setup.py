from setuptools import setup, find_packages

setup(
    name="translate-comment-out",
    version='1.0',
    description='Translate Comment Out',
    author='Kobori Akira',
    author_email='private.beats@gmail.com',
    url='https://github.com/koboriakira/translate_comment_out',
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      tco = translate_comment_out.main:cli
    """,
    install_requires=open('requirements.txt').read().splitlines(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
