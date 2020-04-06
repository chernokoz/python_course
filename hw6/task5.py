class UML(type):
    @staticmethod
    def draw_uml(class_to_draw, prefix=''):
        if not isinstance(class_to_draw, UML):
            raise TypeError(f"{class_to_draw.__name__} is not instance of UML")
        pref = prefix
        cls_subclasses = class_to_draw.__subclasses__()
        print(prefix, class_to_draw.__name__)
        for i in cls_subclasses:
            UML.draw_uml(i, prefix=pref + "    ")
