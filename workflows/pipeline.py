from dcs import DocFactory, GlobalReadMe
from utils_future import Log

log = Log("pipeline")
if __name__ == "__main__":
    for i_cls, cls in enumerate(DocFactory.list(), start=1):
        log.debug("-" * 60)
        log.info(
            f"[{i_cls}/{len(DocFactory.list())}] Building {cls.get_name()}"
        )
        log.debug("-" * 60)
        cls.build_latest()
    GlobalReadMe.build()
S
