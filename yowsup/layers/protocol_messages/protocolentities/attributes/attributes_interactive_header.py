from .attributes_image import ImageAttributes
from .attributes_video import VideoAttributes
from .attributes_document import DocumentAttributes
from yowsup.common.optionalmodules import PILOptionalModule
import io
import requests
import base64


class InteractiveHeaderAttributes(object):
    def __init__(self, title=None, subtitle=None,  
                 document=None, 
                 image=None,
                 thumbnail=None,
                 video=None
                ):
        
        self._title = title
        self._subtitle = subtitle
        self._document = document
        self._image = image
        self._thumbnail= thumbnail
        self._video= video 

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def subtitle(self):
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value

    @property
    def document(self):
        return self._document

    @document.setter
    def document(self, value):
        self._document = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value


    @property
    def thumbnail(self):
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, value):
        self._thumbnail= value

    @property
    def video(self):
        return self._video

    @video.setter
    def video(self, value):
        self._video= value

    @staticmethod
    def fromJson(jsonObj,resultRequestMediaConnIqProtocolEntity=None):
        if jsonObj is None:
            return None
        obj = InteractiveHeaderAttributes()
        obj.title = jsonObj["title"] if "title" in jsonObj else None
        obj.subtitle = jsonObj["subtitle"] if "subtitle" in jsonObj else None
        if "image" in jsonObj:
            if "url" in jsonObj["image"]:
                obj.image = ImageAttributes.from_url(jsonObj["image"]["url"],"image",resultRequestMediaConnIqProtocolEntity)
            if "filepath" in jsonObj["image"]:
                obj.image = ImageAttributes.from_filepath(jsonObj["image"]["filepath"],"image",resultRequestMediaConnIqProtocolEntity)

        if "video" in jsonObj:
            if "filepath" in jsonObj["video"]:
                obj.video = VideoAttributes.from_filepath(jsonObj["video"]["filepath"],"video",resultRequestMediaConnIqProtocolEntity)

        if "document" in jsonObj:
            if "filepath" in jsonObj["document"]:
                obj.document = DocumentAttributes.from_filepath(jsonObj["document"]["filepath"],"document",resultRequestMediaConnIqProtocolEntity)

        if "thumbnail" in jsonObj:
            if "url" in jsonObj["thumbnail"]:
                with PILOptionalModule(failMessage = "No PIL library installed, try install pillow") as imp:
                    Image = imp("Image")
                    src = Image.open(io.BytesIO(
                        requests.get(jsonObj["thumbnail"]["url"]).content))
                    picture = io.BytesIO()        
                    src.resize((300, 300)).save(picture,format="jpeg")    
                    obj.thumbnail=picture.getvalue()
            if "b64" in jsonObj["thumbnail"]:
                obj.thumbnail = base64.b64decode(jsonObj["thumbnail"]["b64"])

        return obj
