from loguru import logger

from data_juicer.core import Analyser


@logger.catch(reraise=True)
def main():
    analyser = Analyser()
    analyser.run()


if __name__ == '__main__':
    main()
