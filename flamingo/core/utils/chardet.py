from chardet.universaldetector import UniversalDetector

_detector = UniversalDetector()


def chardet_read(path):
    _detector.reset()

    for line in open(path, 'rb'):
        _detector.feed(line)

        if _detector.done:
            break

    if not _detector.done:
        return open(path, 'r')

    return open(path, 'rb', encoding=_detector.result()['encoding']).read()
