import os

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

#with open('requirements.txt') as f:
#    requirements = f.read().splitlines()


def get_dirlist(_rootdir):
    dirlist = []

    with os.scandir(_rootdir) as rit:
        for entry in rit:
            if not entry.name.startswith('.') and entry.is_dir():
                dirlist.append(entry.path)
                dirlist += get_dirlist(entry.path)

    return dirlist


# Get subfolders recursively
rootdir = './waymo_open_dataset'
packages = [d.replace('/', '.').replace('{}.'.format(rootdir), '') for d in get_dirlist(rootdir)]
print(packages)
setuptools.setup(
    name='waymo_open_dataset',
    version='1.0',
    author='Waymo.',
    author_email='',
    description='Waymo loader without native components',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    python_requires='>=3.6',
#    install_requires=requirements,
    packages=packages,
    package_data={'': ['*.json']},
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ],
)
