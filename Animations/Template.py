from manim import Scene, Tex, Write, FadeOut
import os


class Template(Scene):
    """Template to create a new animation"""

    def construct(self):
        text = Tex(r"Hello World!").scale(3)
        self.play(Write(text))
        self.wait(1)
        self.play(FadeOut(text))


# Execute rendering
if __name__ == "__main__":  # Only run if file is executed directly
    os.system(r"manim -p -t -qh Animations\Template.py Test")
