from manim import *
import os


class Euler(Scene):
    """Euler ID animation scene"""

    def construct(self):
        text = MathTex(r"\mathrm{e}^{\mathrm{i}\pi}+1=0").scale(3)
        self.play(Write(text))
        self.wait(0.5)
        self.play(FadeOut(text))


# Execute rendering
if __name__ == "__main__":  # Only run if file is executed directly
    os.system(r"manim -p -t -qh Animations\EulerIdentity.py Euler")
