from setuptools import find_packages, setup

package_name = 'hsrb-display-franco'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='franco',
    maintainer_email='franco@uni-bremen.de',
    description='display image',
    license='',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = display_test.publisher:main',
            'listener = display_test.subscriber:main',
        ],
    },
)
