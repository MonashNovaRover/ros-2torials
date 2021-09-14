from setuptools import setup

package_name = 'tutorials'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Monash Nova Rover',
    maintainer_email='novaroverteam@monash.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = tutorials.example_publisher:main',
            'subscriber = tutorials.example_subscriber:main',
            'client = tutorials.example_client:main',
            'service = tutorials.example_service:main',
        ],
    },
)
