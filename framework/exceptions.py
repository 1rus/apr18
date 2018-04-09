class FrameExceptions(Exception):
    pass


class InvalidLocatorString(FrameExceptions):

    def _get_mes(self):
        return self._mes

    def _set_mes(self, mes):
        self._mes = mes

    mes = property(_get_mes, _set_mes)


class ElementTextTimeout(FrameExceptions):

    def _get_mes(self):
        return self._mes

    def _set_mes(self, mes):
        self._mes = mes

    mes = property(_get_mes, _set_mes)


class ElementVisiblityTimeout(FrameExceptions):

    def _get_mes(self):
        return self._mes

    def _set_mes(self, mes):
        self._mes = mes

    mes = property(_get_mes, _set_mes)


class ElementNotFound(FrameExceptions):

    def _get_mes(self):
        return self._mes

    def _set_mes(self, mes):
        self._mes = mes

    mes = property(_get_mes, _set_mes)


class ProfileNotFound(FrameExceptions):

    def _get_mes(self):
        return self._mes

    def _set_mes(self, mes):
        self._mes = mes

    mes = property(_get_mes, _set_mes)

