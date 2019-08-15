"""Documentation at documentation.org file.

"""

from manimlib.imports import *
import os
import pyclbr


class PlainCow(SVGMobject):
    CONFIG = {"file_name": "./sleepy_cow_plain.svg",
              "height": 3,
              "stroke_width": 5,
              "fill_opacity": 0,
              "background_stroke_color": WHITE,
              "background_stroke_width": 1,
              "close_new_points": True,
              "fill_color": WHITE,
    }


class HideThePainCow(SVGMobject):
    CONFIG = {"file_name": "./hide_the_pain_cow.svg",
              "height": 3,
              "stroke_width": 5,
              "fill_opacity": 0,
    }

    def __init__(self):
        super().__init__()


class RelativisticCows(Scene):
    """The pain is relative."""
    def construct(self):
        start_man = PlainCow()
        plain_man = PlainCow()
        pain_cow = HideThePainCow()

        self.add(start_man)
        self.wait()
        self.play(Transform(start_man, pain_cow))
        self.play(Transform(start_man,plain_man))

        self.wait()


class Clock(Scene):
    """Relativistic clocks.

    These clocks are composed of a circle, an arrow and numbers.

    Tasks
    -----
    - Add numbers.
    - Set rotate speed.

    """
    def construct(self):
        circle = Circle(color=GREEN)
        circle.set_fill(GREEN, opacity=1)
        arrow = Arrow(ORIGIN, UP)

        number1 = TextMobject("1")
        number2 = TextMobject("2")
        number1.move_to(UP)
        number2.move_to(RIGHT)

        arrow.shift(DOWN * 1 / 2)
        # arrow.set_length(4 / 6)

        self.add(circle)
        self.add(arrow)
        self.play(Write(number1))
        self.play(Write(number2))
        # self.play(Rotate(arrow, angle=-PI/2, about_point=ORIGIN))
        self.play(FadeOut(circle))


if __name__ == "__main__":
    module_name = 'manim_tutorial_P37'   #Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module == module_name:
            print(item.name)
            os.system("python -m manim manim_tutorial_P37.py %s -l" % item.name)  #Does not play files
