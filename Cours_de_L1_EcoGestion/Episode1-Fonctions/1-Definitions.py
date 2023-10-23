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


class SecondDefinition_functionAtoB(Scene):  # the scene of the second definition 1.2
    def construct(self):
        def_ens = MathTex(
            r"\text{Soient } A \text{ et } B \text{ deux ensembles quelconques.}"
        ).scale(0.75)
        def_ens.move_to(2 * UP)
        self.play(Write(def_ens), run_time=1.5)

        self.wait(2)

        def_f = MathTex(
            r"\text{On appelle } f : A \to B \text{ se lit } A \text{ vers } B \text{.}",
            r"\text{ toute relation qui à chaque élément de } A \text{ associe au plus un élément de } B \text{.}",
        ).scale(0.75)

        def_f[0].next_to(def_ens, 3 * DOWN)
        def_f[1].next_to(def_f[0], DOWN)
        self.play(Write(def_f[0]), run_time=1.5)
        self.play(Write(def_f[1]), run_time=1.5)
        self.wait(2)

        def_f_bis = MathTex(
            r"A \text{ est donc } ",
            r"\text{l'ensemble de départ}",
            r"\text{ et } B",
            r"\text{ l'ensemble d'arrivée.}",
        ).scale(0.75)
        def_f_bis.next_to(def_f[1], DOWN)
        self.play(Write(def_f_bis[0]), Write(def_f_bis[1]), run_time=1.5)
        self.play(Indicate(def_f_bis[1]), run_time=1.5)
        self.wait(1)

        self.play(Write(def_f_bis[2]), Write(def_f_bis[3]), run_time=1.5)
        self.play(Indicate(def_f_bis[3]), run_time=1.5)

        self.wait(1)

        A_to = MathTex(r"\text{élément quelconque de } A").scale(0.75).set_color(RED)
        A_to.next_to(def_f_bis[0], 2 * DOWN)
        to = MathTex(r"\xrightarrow{\hspace*{50px}}").scale(1)
        to.next_to(A_to, RIGHT)
        B_to = (
            MathTex(r"\text{élément de } B \text{ associé}")
            .scale(0.75)
            .set_color(YELLOW)
        )
        B_to.next_to(def_f_bis[3], 2 * DOWN)

        self.play(Write(A_to), run_time=0.5)
        self.play(DrawBorderThenFill(to), run_time=0.5)
        self.play(Write(B_to), run_time=0.5)
        self.wait(2)

        self.play(
            ReplacementTransform(A_to, B_to), ReplacementTransform(to, B_to), run_time=2
        )
        self.play(B_to.animate.move_to(-1 * UP).scale(2), rate_functions=there_and_back)

        self.wait(2)

        self.play(
            FadeOut(VGroup(def_ens, def_f, def_f_bis, A_to), reverse=True),
            run_time=1.5,
        )

        self.wait(2)

        A = MathTex(r"A").scale(2).set_color(GREEN)
        Ab = MathTex(r"x").scale(1.5).set_color(RED)
        B = MathTex(r"B").scale(2).set_color(YELLOW)

        A.move_to(2 * UL + DOWN)

        B.move_to(2 * UR + DOWN)

        self.play(Write(A), Write(B), run_time=1.5)

        # Make a curved arrow from A to B
        arrow = CurvedArrow(
            A.get_center() + 1 / 2 * UP + 1 / 4 * RIGHT,
            B.get_center() + 1 / 2 * UP,
            angle=-TAU / 3,
        )

        self.play(Write(arrow), run_time=1.5)

        # Make x follow the path of the curved arrow from A to B
        n = 0
        while n <= 2:
            Ab.next_to(arrow, LEFT)
            self.play(Write(Ab), run_time=1)
            self.play(MoveAlongPath(Ab, arrow.copy().shift(0.5 * UP), run_time=2))
            self.play(Unwrite(Ab), run_time=1)
            self.wait(1)
            n += 1

        self.wait(2)
