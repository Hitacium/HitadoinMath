from manim import *
from random import *

class RappelEnsemble(Scene):  # notes about ensembles
    def construct(self):
        listIncl = (  # Inclusion chain
            MathTex(
                r"\mathbb{N}\subset\mathbb{Z}\subset\mathbb{D}\subset\mathbb{Q}\subset\mathbb{R}",
            )
            .scale(2)
            .move_to(3 * UP)
        )
        self.play(Write(listIncl), run_time=2)

        self.wait(4)

        defN = (  # definition of N
            MathTex(r"\mathbb{N} = \{0,1,\ldots\}").scale(1.5).next_to(listIncl, DOWN)
        )
        self.play(Write(defN), run_time=1)

        self.wait(5)

        defZ = (  # definition of Z
            MathTex(r"\mathbb{Z} = \{\ldots,-1,0,1,\ldots\}")
            .scale(1.5)
            .next_to(defN, DOWN)
        )
        self.play(Write(defZ), run_time=1)

        self.wait(5)

        defD = (  # definition of D
            MathTex(
                r"\mathbb{D}",
                r"= \left \{ \dfrac{n}{10^p},n\in\mathbb{Z},p\in\mathbb{N} \right \}",
            )
            .scale(1.5)
            .next_to(defZ, DOWN)
        )
        self.play(Write(defD[0]), run_time=1)
        framebox = SurroundingRectangle(defD[0], buff=0.2)
        self.play(
            Create(framebox),
        )
        self.wait(5)

        self.play(Uncreate(framebox), Write(defD[1]), run_time=1)

        self.wait(5)

        exempleD = (  # exemple of D
            MathTex(
                r"\text{Exemple: } 1,75 ",
                r" = \dfrac{175}{100}",
                r"= \dfrac{175}{10^2}",
            )
            .scale(1.5)
            .next_to(defD, DOWN)
        )
        self.play(Write(exempleD[0]), run_time=1)
        self.wait(2)
        self.play(Write(exempleD[1]), run_time=1)
        self.wait(2)
        self.play(Write(exempleD[2]), run_time=1)
        self.wait(4)

        self.play(  # unwrite everything on the screen
            Unwrite(listIncl, reverse=True),
            Unwrite(defN, reverse=True),
            Unwrite(defZ, reverse=True),
            Unwrite(defD, reverse=True),
            Unwrite(exempleD, reverse=True),
            run_time=1,
        )

        self.wait(1)

        defQ = (  # definition of Q
            MathTex(
                r"\mathbb{Q}",
                r"= \left\{\left.{\dfrac {m}{n}}\right|(m,n)\in \mathbb{Z } \times (\mathbb{Z } \setminus \{0\})\right\}",
            )
            .scale(1.5)
            .move_to(3 * UP)
        )
        self.play(Write(defQ[0]), run_time=1)
        self.play(Indicate(defQ[0]), run_time=1)

        self.wait(5)

        self.play(Write(defQ[1]), run_time=1)
        self.wait(5)

        couple_m_n = (  # explaning the couple (m, n)
            MathTex(r"(m,n)", r"\in \mathbb{Z}^2")
            .move_to(1.5 * UP + 4 * LEFT)
            .scale(1.25)
        )
        self.play(Write(couple_m_n[0]), run_time=1)
        self.wait(1)
        self.play(Write(couple_m_n[1]), run_time=1)

        self.wait(5)

        axe = (  # explanation axe with tip text and dot axes with lines
            Axes(
                x_range=[0, 10, 1],
                y_range=[0, 10, 2],
                axis_config={"tip_shape": StealthTip},
            )
            .add_coordinates()
            .scale(0.5)
        )
        lines = axe.get_lines_to_point(axe.c2p(1, 2))
        dot_axes = Dot(axe.coords_to_point(1, 2), color=GREEN)
        tip_text = (
            MathTex(r"(m, n)").scale(0.5).next_to(dot_axes.get_center(), 0.5 * UR)
        )

        self.play(
            Write(
                VGroup(axe, lines, dot_axes, tip_text)
                .next_to(defQ, DOWN)
                .move_to(2 * RIGHT)
            ),
            run_time=1,
        )

        self.wait(3)

        for i in range(4):  # randomize the (m,n) movement
            m = randint(1, 6)
            n = randint(1, 9)

            target_dot = Dot(axe.coords_to_point(m, n), color=GREEN)
            target_lines = axe.get_lines_to_point(axe.c2p(m, n))
            target_tip_text = (
                MathTex(r"(m, n)").scale(0.5).next_to(target_dot.get_center(), 0.5 * UR)
            )

            self.play(
                lines.animate.become(target_lines),
                dot_axes.animate.move_to(target_dot.get_center()),
                tip_text.animate.move_to(target_tip_text.get_center()),
                run_time=1,
            )

            self.wait(1.5)

        self.play(
            Unwrite(
                VGroup(dot_axes, lines, tip_text, axe, defQ, couple_m_n), reverse=True
            ),
            run_time=0.5,
        )

        self.wait(2)


class RappelEnsembleBis(Scene):
    def construct(self):
        defR = MathTex(
            r"\mathbb{R}", r"= \{\pi, e, \ln, \cos(\dfrac{\pi}{4}), \sqrt{2}, \ldots\}"
        ).scale(2)
        self.play(Write(defR[0]), run_time=1)
        self.wait(3)
        self.play(Write(defR[1]), run_time=1)
        self.wait(1)


class FirstDefinition(Scene):  # the scene of the first definition
    def construct(self):
        def_of_q1_and_q2 = MathTex(
            r"\text{On pose } q_1 \text{ et } q_2 \text{ deux biens avec une quantité respective}."
        )  # definition of q1 and q2 a quantity
        def_of_q1_and_q2.move_to(1.5 * UP)
        self.play(Write(def_of_q1_and_q2), run_time=2)

        self.wait(1)

        q1_q2_inZ = MathTex(
            r"(q_1,q_2)\in \mathbb{Z}"
        )  # precise that q1 and q2 are relative numbers
        q1_q2_inZ.next_to(def_of_q1_and_q2, DOWN)
        self.play(Write(q1_q2_inZ), run_time=1)

        self.wait(2)

        def_of_p1_and_p2 = MathTex(
            r"\text{On pose aussi } p_1 \text{ et } p_2 \text{ le prix de ces deux biens}."
        )
        self.play(Write(def_of_p1_and_p2), run_time=2)

        self.wait(1)

        p1_p2_inQ = MathTex(
            r"(p_1,p_2)\in \mathbb{Q}"
        )  # precise that q1 and q2 are relative numbers
        p1_p2_inQ.next_to(def_of_p1_and_p2, DOWN)
        self.play(Write(p1_p2_inQ), run_time=1)

        self.wait(2)

        Total = MathTex(
            r"\text{On notera alors } R = q_1\times p_1 + q_2\times p_2 \text{ le revenu total obtenu.}"
        )
        Everything = VGroup(
            p1_p2_inQ,
            def_of_p1_and_p2,
            q1_q2_inZ,
            def_of_q1_and_q2,
        )
        self.play(Unwrite(Everything, reverse=True), run_time=0.75)

        self.play(Write(Total), run_time=2)
        self.wait(2)
