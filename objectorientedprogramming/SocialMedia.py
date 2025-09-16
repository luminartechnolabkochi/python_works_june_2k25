
from abc import ABC,abstractmethod

class SocialMedia(ABC):

    @abstractmethod
    def add_post(self):
        pass

    @abstractmethod
    def follow(self):
        pass

    @abstractmethod
    def share(self):
        pass

class FaceBook(SocialMedia):

    def add_post(self):
        print("fb add post method")

    def follow(self):
        print("fb follow method")

    def share(self):

        print("fb share")


fb_instance = FaceBook()

fb_instance.add_post()


