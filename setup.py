from setuptools import setup, find_packages


setup(
    name="bandp",
    version="0.0.0",
    description="Play and download bandori's music.",
    author="kazukazuprogram",
    author_email="dbycvil8yiyf7xnlxvh7@yahoo.co.jp",
    maintainer='kazukazuprogram',
    maintainer_email="dbycvil8yiyf7xnlxvh7@yahoo.co.jp",
    install_requires=["requests", "bs4"],
    packages=find_packages(),
    license="MIT",
    package_dir={"bandp": "bandp"},
    package_data={"bandp": ["bin\\*.exe"]},
    entry_points={
        "console_scripts": [
            "bandp = bandp.__init__:start",
        ]
    }
)
