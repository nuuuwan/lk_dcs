from dcs import DocFactory, GlobalReadMe

if __name__ == '__main__':
    for cls in DocFactory.list():
        cls.build_latest()
    GlobalReadMe.build()
