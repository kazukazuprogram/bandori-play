from setuptools import setup

setup(
    name="bandori_play",
    version="0.0.0",
    description="Play and download bandori's music.",
    author="kazukazuprogram",
    install_requires=["requests", "bs4"],
    author_email="dbycvil8yiyf7xnlxvh7@yahoo.co.jp",
    entry_points={
        "console_scripts": [
            "bandori_play = bandori_play.module_name:func_name",
            "foo_dev = package_name.module_name:func_name [develop]"
        ],
        "gui_scripts": [
            "bar = bandori-play.__init__:gui_func_name"
        ]
    }
)
