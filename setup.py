from setuptools import setup

setup(
    name='sphinx-nameko-theme',
    version='0.0.1',
    author='onefinestay',
    author_email='nameko-devs@onefinestay.com',
    description='Sphinx Nameko Theme',
    url='https://github.com/onefinestay/sphinx-nameko-theme',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Documentation',
    ],
    packages=['sphinx_nameko_theme'],
    install_requires=['sphinx'],
    entry_points = {
        'sphinx_themes': [
            'path = sphinx_nameko_theme:get_html_theme_path',
        ]
    },
    include_package_data=True,
    zip_safe=False
)
