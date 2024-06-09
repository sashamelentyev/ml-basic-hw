class Audio:
    def __init__(self, path_or_url):
        """Принимаем на вход путь или ссылку до аудио-файла.
        В случае если принимает ссылку - скачиваем из сети, если из файловой системы - просто открываем.
        """
        self.path_or_url = path_or_url

    def metadata(self):
        """metadata - возвращает мета-информацию о файле
        """
        pass

    def rename(self):
        # Переименовываем файл
        pass

    def save(self):
        # Сохраняем файл локально
        pass

    def upload(self):
        # Загружаем файл в хранилище
        pass


class Video:
    def __init__(self, path_or_url):
        """Принимаем на вход путь или ссылку до видео-файла.
        В случае если принимает ссылку - скачиваем из сети, если из файловой системы - просто открываем.
        """
        self.path_or_url = path_or_url

    def metadata(self):
        """metadata - возвращает мета-информацию о файле
        """
        pass

    def rename(self):
        # Переименовываем файл
        pass

    def save(self):
        # Сохраняем файл локально
        pass

    def upload(self):
        # Загружаем файл в хранилище
        pass

    def change_video_file_format(self):
        # Меняем видео формат на другое
        pass


class Image:
    def __init__(self, path_or_url):
        """Принимаем на вход путь или ссылку до изображения.
        В случае если принимает ссылку - скачиваем из сети, если из файловой системы - просто открываем.
        """
        self.path_or_url = path_or_url

    def metadata(self):
        """metadata - возвращает мета-информацию о файле
        """
        pass

    def rename(self):
        # Переименовываем файл
        pass

    def save(self):
        # Сохраняем файл локально
        pass

    def upload(self):
        # Загружаем файл в хранилище
        pass


def is_url(s: str) -> bool:
    """Функция определяет похожа ли входящая строка на URL или нет
    """
    pass
